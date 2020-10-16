import smtplib

#create the connection object
conn = smtplib.SMTP('smtp.gmail.com', 587)

type(conn)

#connects to server, needed to start
conn.ehlo()

#encrypts things
conn.starttls()

#username@gmail.com, password
conn.login('', '')

#from, to, message
conn.sendmail('', '', '')

#dc from the smtp server
conn.quit()
