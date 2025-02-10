import qrcode
from io import BytesIO
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event, EventRegistration
import base64

# Hiển thị form đăng ký sự kiện
def form_reg(request, event_id):
    # Lấy sự kiện từ ID
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'EventReg/form_reg.html', {'event': event})

def submit_registration(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        role = request.POST.get('role')
        event_id = request.POST.get('event_id')  # Lấy ID sự kiện từ form
        
        # Kiểm tra xem có thiếu trường thông tin nào không
        if not all([name, email, phone, address, role, event_id]):
            return HttpResponse("Vui lòng điền đầy đủ thông tin.")

        # Tạo một đối tượng đăng ký sự kiện và lưu vào cơ sở dữ liệu
        event = get_object_or_404(Event, id=event_id)
        registration = EventRegistration(
            event=event,
            name=name,
            email=email,
            phone=phone,
            address=address,
            role=role
        )
        registration.save()

        # Tạo nội dung QR code
        qr_data = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nRole: {role}"
        
        # Tạo mã QR
        qr = qrcode.make(qr_data)
        qr_image = BytesIO()
        qr.save(qr_image, format="PNG")
        qr_image.seek(0)

        # Chuyển mã QR thành dữ liệu base64 để gửi lên trang
        qr_image_base64 = base64.b64encode(qr_image.read()).decode('utf-8')

        # Gửi email xác nhận kèm QR code
        try:
            email_message = EmailMessage(
                subject='Xác nhận đăng ký sự kiện',
                body=f'Chào {name},\n\nCảm ơn bạn đã đăng ký tham gia sự kiện. Vui lòng sử dụng mã QR đính kèm để check-in.\n\nTrân trọng,\nBan tổ chức',
                from_email='tumakiss2005a@gmail.com',
                to=[email],
            )
            email_message.attach('event_qr.png', qr_image.read(), 'image/png')
            email_message.send()
        except Exception as e:
            print(f"Lỗi khi gửi email: {e}")
            return HttpResponse("Đăng ký thành công nhưng có lỗi khi gửi email xác nhận.")

        # Sau khi đăng ký thành công, chuyển hướng đến trang thông báo với mã QR
        return render(request, 'EventReg/noti.html', {'name': name, 'qr_image_base64': qr_image_base64})
    
    else:
        return HttpResponse("Chỉ hỗ trợ phương thức POST.")
