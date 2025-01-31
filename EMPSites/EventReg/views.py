from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Hiển thị form đăng ký sự kiện
def form_reg(request):
    return render(request, 'EventReg/form_reg.html')

# Xử lý dữ liệu khi form được gửi
def submit_registration(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        role = request.POST.get('role')
        event = request.POST.get('event')
        event_date = request.POST.get('event_date')
        payment_method = request.POST.get('payment_method')

        # Gửi email xác nhận
        try:
            send_mail(
                'Xác nhận đăng ký sự kiện',
                f'Chào {full_name},\n\nCảm ơn bạn đã đăng ký tham gia sự kiện {event} vào ngày {event_date}.\n\nTrân trọng,\nBan tổ chức',
                'tumakiss2005a@gmail.com',  # Email gửi (cần cấu hình trong settings.py)
                [email],  # Email người nhận
                fail_silently=False,
            )
        except Exception as e:
            print(f"Lỗi khi gửi email: {e}")
            return HttpResponse("Đăng ký thành công nhưng có lỗi khi gửi email xác nhận.")

        # Trả về thông báo thành công
        return HttpResponse(f"Cảm ơn {full_name} đã đăng ký thành công!")
    else:
        # Nếu không phải phương thức POST, hiển thị thông báo lỗi
        return HttpResponse("Chỉ hỗ trợ phương thức POST.")

