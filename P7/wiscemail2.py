import smtplib
from email.mime.text import MIMEText

def sendEmail(sendFlag, name, report, emailAddress, template, submissionName):
    fp = open(template, 'r')
    fileCon = fp.read()
    emailCon = fileCon.replace('{Submission-Name}', submissionName).replace('{Student-Name}',name).replace('{Report}', report)
    msg = MIMEText(emailCon)
    msg['Subject'] = 'Warning for Your Recent Submission(CS 301)'
    msg['From'] = 'szou28@wisc.edu'
    msg['To'] = emailAddress
    print 'subject:',msg['Subject']
    print 'from:',msg['From']
    print 'to:',msg['To']
    print emailCon
    if sendFlag:
        s = smtplib.SMTP('localhost')
        s.sendmail('szou28@wisc.edu', [emailAddress], msg.as_string())
        s.quit()
    else:
        print 'SEND TEST. NOT SEND.'





