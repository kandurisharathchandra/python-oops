class chatbook:

    __user_id=0
    def __init__(self):
        self.__name="default user"
        self.id=chatbook.__user_id
        chatbook.__user_id+=1
        self.username=''
        self.password=''
        self.loggedin=False
        # self.menu()
    def get_name(self):
        return self.__name
    def set_name(self,value):
        self.__name=value
    @staticmethod
    def get_id():
        return chatbook.__user_id
    def set_id(value):
        chatbook.__user_id=value

    
    def menu(self):
        user_input=input("""welcome to chatbook !! how would u like to proceed"
                         1. press 1 to signup
                         2. press 2 to signin
                         3. press 3 to write a post
                         4. press 4 to message a frnd
                         5.press any other key to exit
                         
                         ->""")
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.write_post()
        elif user_input=="4":
            self.message_frnd()
        else:
            exit()

    def signup(self):
        email=input("enter a email here -> ")
        pwd=input("enter a password -> ")
        self.username=email
        self.password=pwd
        print("u have sgned up successfully")
        print("\n")
        self.menu()
    def signin(self):
        if self.username == '' and self.password == '':
            print("please signup")
        else:
            email=input("enter a email here -> ")
            pwd=input("enter a password -> ")
            if self.username ==email and self.password==pwd:
                print("u have logged in succesfully")
                self.loggedin=True
            else:
                print("please input correct credentials..")
        print("\n")
        self.menu()
    def write_post(self):
        if self.loggedin == True:
            txt=input("enter ur message")
            print(f"following content has been posted ->{txt}")
        else:
            print("please sign in to post something")
        print("\n")
        self.menu()
    def message_frnd(self):
        if self.loggedin == True:
            txt=input("enter a message->")
            frnd=input("whom to send ->")
        else:
            print("please sign in to post something")
        print("\n")
        self.menu()




obj = chatbook()
            
        
