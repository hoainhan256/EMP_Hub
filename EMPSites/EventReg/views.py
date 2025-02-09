import qrcode
from io import BytesIO
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponse


# Hiển thị form đăng ký sự kiện
def form_reg(request):
    return render(request, 'EventReg/form_reg.html')


def submit_registration(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        role = request.POST.get('role')
    

        # Tạo nội dung QR code
        qr_data = f"Name: {name}\nEmail: {email}\nPhone: {phone}"
        
        # Tạo mã QR
        qr = qrcode.make(qr_data)
        qr_image = BytesIO()
        qr.save(qr_image, format="PNG")
        qr_image.seek(0)

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

        return HttpResponse(f"Cảm ơn {name} đã đăng ký thành công! Mã QR đã được gửi đến email của bạn.")
    else:
        return HttpResponse("Chỉ hỗ trợ phương thức POST.")