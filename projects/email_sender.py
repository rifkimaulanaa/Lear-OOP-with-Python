import smtplib

email = input("Sender Email:")
receiver_email = input("Receiver Email:")

subject = input("Subject:")
message = input("Message:")

text = f"subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",2525)

server.login(email,"kpvcqlmgbjssxbbz") #kpvc qlmg bjss xbbz

server.sendmail(receiver_email,email,text)

print("Email telah terkirim ke !" + receiver_email)