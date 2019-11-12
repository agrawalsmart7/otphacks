import math, random
import smtplib
import sys


sender_email =  sys.argv[1]


def generateOTP():
	digits = '0123456789'
	otp = ""
	for i in range(4):
		otp += digits[math.floor(random.random()*10)]



def send_otp_to_mail(otp):

	with smtplib.SMTP_SSL("smtp.gmail.com", "465") as smtp:
		smtp.login("", "")
		smtp.sendmail("", sender_email, "Hello there, your test OTP is "+otp)
		smtp.quit()

	with open("data.txt", 'w') as file:
		file.write(otp)
	

otp = generateOTP()
print (otp)
send_otp_to_mail(otp)
