from gmail import *
gmail = GMail('jaydeepsingh7021@gmail.com','7021561137')
msg = Message('Test Message',to='jaydeepsingh7021@gmail.com',text='Hello')
gmail.send(msg)
