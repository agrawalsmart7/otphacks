import math, random
import smtplib
import sys


recipient_email =  sys.argv[1]
gmail_username = ""
gmail_password = ""


def generateOTP():
	digits = '0123456789'
	otp = ""
	for i in range(4):
		otp += digits[math.floor(random.random()*10)]



def send_otp_to_mail(otp):

	with smtplib.SMTP_SSL("smtp.gmail.com", "465") as smtp:
		smtp.login(gmail_username, gmail_password)
		smtp.sendmail(gmail_username, recipient_email, "Hello there, your test OTP is "+otp)
		smtp.quit()

	with open("data.txt", 'w') as file:
		file.write(otp)
	

otp = generateOTP()
print (otp)
send_otp_to_mail(otp)
