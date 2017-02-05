import smtplib

fromaddr = 'leon.facey@gmail.com'
toaddr  = ''
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}"""
fromname = ''
toname = ''
subject = ''
msg = ''

messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)

# Credentials (if needed)
username = ''
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()
