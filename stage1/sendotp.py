import math, random
import smtplib
import sys


recipient_email =  sys.argv[1]
sender_email = ""
gmail_password = ""

def generateOTP():
	digits = '0123456789'
	otp = ""
	for i in range(4):
		otp += digits[math.floor(random.random()*10)]

	return otp

def send_otp_to_mail(otp):
	
	try:
	
		with smtplib.SMTP_SSL("smtp.gmail.com", "465") as smtp:
			smtp.login(sender_email, gmail_password)
			smtp.sendmail(sender_email, recipient_email, "Hello there, your test OTP is "+otp)
			smtp.quit()

		with open("data.txt", 'w') as file:
			file.write(str(otp))
	except Exception as e:
		pass

otp = generateOTP()
print (otp)
send_otp_to_mail(otp)
