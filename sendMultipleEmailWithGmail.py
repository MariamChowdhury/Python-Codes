import smtplib
li = ["ghi@gmail.com", "def@gmail.com","ghi@gmail.com","abc@gmail.com", "abc@gmail.com","def@gmail.com","abc@gmail.com","abc@gmail.com", "def@gmail.com","ghi@gmail.com"]
liSorted=sorted(li)
for dest in liSorted :
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("my_email@gmail.com", "my_password")
	message = "testing email from python"
	s.sendmail("my_email@gmail.com", dest, message)
	s.quit()
