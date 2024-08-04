import random
import smtplib
from email.message import EmailMessage

def generate_otp():
    return str(random.randint(100000, 999999))

# Function to simulate sending OTP to user's email address
def send_otp_email(email, otp):

      sender_email= "srijeetamondal304@gmail.com"
      sender_password= "kgzr tgcm enuc boyc"

      msg = EmailMessage()
      msg['Subject'] = 'OTP Verification'
      msg['From'] = sender_email
      msg['To'] = email
      msg.set_content(f"Your OTP is: {otp}")

      with smtplib.SMTP_SSL("SMTP.gmail.com", 465) as smtp:
           smtp.login(sender_email, sender_password)
           smtp.send_message(msg)
           
   # Function to prompt the user to enter OTP:

def enter_otp():
    return input("Please enter the OTP send on your email: ")


# Function to verify if entered OTP matches generated OTP:

def verify_otp(otp, entered_otp):
    return otp == entered_otp      

def main():
    email = input("Enter your email address: ")
    otp = generate_otp()
    send_otp_email(email, otp)


    # Verifying the OTP
    attempts = 1
    max_attempts = 3

    for attempts in range(max_attempts):
        entered_otp = enter_otp()
        if verify_otp(otp, entered_otp):
            entered_otp = enter_otp()
            print("OTP verification successful. Access granted!")
            return
        else:
            print("Incorrect OTP. Please try again.")

    print("Maximum attempts reached. Access denied.") # If maximum attempts reached

main()  