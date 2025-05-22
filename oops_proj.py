class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

    
    def menu(self):
        user_input=input("""welcome to chatbook !! how would u like to proceed"
                         1. press 1 to signup
                         2. press 2 to signin
                         3. press 3 to write a post
                         4. press 4 to message a frnd
                         5.press any other key to exit""")
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
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


obj = chatbook()
            
        
