import win10toast
toaster = win10toast.ToastNotifier()
toaster.show_toast("python","success ! This is working!", duration=10)

from win10toast import ToastNotifier
import time
while True:
  current_time = time.strftime("%H:%M:%S")
  if current_time=="00.36.00":
    print(current_time)
    break
  else:
    pass
hr=ToastNotifier()
hr.show_toast("alarm","this is the message")