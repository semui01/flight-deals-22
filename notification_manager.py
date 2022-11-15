import smtplib
import os

my_email = os.environ.get('my_email')
my_password =os.environ.get('my_password')
gmail_app_password= os.environ.get('gmail_app_key')
TO_ADDRESS = os.environ.get('to_address')


class NotificationManager:
        def send_email(self,message):
            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()  # make the connection secure
                connection.login(user=my_email, password=gmail_app_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=TO_ADDRESS,
                                    msg=message)




