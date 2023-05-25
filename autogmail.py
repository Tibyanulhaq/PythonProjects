import smtplib as s

ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('tibyanulhaq82@gmail.com','Thiland2@2@')
subject=str(input("Enter Subject"))
body=str(input("Enter massage"))
to=input("Enter Reciever Email")
masage="subject:{}\n\n{}".format(subject,body)
ob.sendmail("tibyanulhaq82@gmail.com",to,masage)
print("Email Sended")
ob.quit()