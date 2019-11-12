import math, random
import smtplib
import sys


recipient_email = sys.argv[1]
gmail_username = ""
gmail_password = ""



def generateOTP():
	digits = '0123456789'
	otp = str(0)+""
	for i in range(3):
		
		otp += digits[math.floor(random.random()*10)]

	return otp

def send_otp_to_mail(otp):

	try:

		with smtplib.SMTP_SSL("smtp.gmail.com", "465") as smtp:
			smtp.login(gmail_username, gmail_password)
			smtp.sendmail(gmail_username, recipient_email, "Hello there, you test2 OTP is "+otp)
			smtp.quit()
			
	except 	Exception as e:
		with open("smtp_error.txt", "w") as file:
			file.write(str(e))
			

	with open("data.txt", 'w') as file:
		file.write(otp)
	

otp = generateOTP()
print (otp)
send_otp_to_mail(otp)
