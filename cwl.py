class createlists:
    def __init__(self,file_name):
        

        #Desiging App#
        print('''
        ------------  \---\                                /---/  ||||  
        ||||||||||||   \---\                              /---/   ||||
        ------------    \---\                            /---/    ||||
        ||||             \---\          ______          /---/     ||||
        ||||              \---\       | ------|        /---/      ||||
        ||||               \---\     /---/  \---\     /---/       ||||
        ||||                \---\   /---/    \---\   /---/        ||||
        -------------        \---\ /---/      \---\ /---/         ||||
        |||||||||||||         \------|         \------/           |||||||||||||||||
        -------------          |-----|          |-----|           |||||||||||||||||
                                                        
                                                                BY: iamEZMUTH\n
        ''')









        self.uname = file_name
        self.f = open(f"{self.uname}.txt",'a')
        self.get_names()
        self.get_numbers()
        self.get_dates()
        self.get_info()
        self.get_keywords()
        self.create_lists()



        #Outro
        print("Completed\n")
        print("Thanks For Using Hope You Love it!!\n")

    def get_names(self):
        
        self.names = []
        while(1):
            self.uinp = input("Enter all names and name-combinations possible to exit press e and exit\n")
            if(self.uinp == "e"):
                break
            else:
                self.names.append(self.uinp)
            
        print(self.names)
    def get_numbers(self):
        
        self.numbers = []
        while(1):
            self.uinp = input("Enter all mobile numbers possible (include girlfriend's number ifany) to exit press e and exit\n")
            if(self.uinp == "e"):
                break
            else:
                self.numbers.append(self.uinp)
            
        print(self.numbers)
    def get_dates(self):
        self.dates = []
        while(1):
            self.uinp = input("Enter all dates with fromat(ddmmyyyy) possible (include girlfriend's birthdate (if any) and his own) to exit press e and exit\n")
            if(self.uinp == "e"):
                break
            else:
                self.dates.append(self.uinp)
            
        print(self.dates)
    def get_info(self):
        pass
    def get_keywords(self):
        self.keywords = []
        while(1):
            self.uinp = input("Enter all keywords (like ben10 or pokemon or else types) to exit press e and exit\n")
            if(self.uinp == "e"):
                break
            else:
                self.keywords.append(self.uinp)
            
        print(self.keywords)
    def create_lists(self):
        print("Started Creating Files...\n")
        #Manuplating Names
        self.addons = ["123","@123","@1234","@","1234","123456789","123@","1234@"]
        self.f.write("123456789\n")
        self.f.write("12345678\n")
        self.f.write("1234567890\n")
        self.f.write("012345678\n")
        self.f.write("0123456789\n")

        for self.name in self.names:
            self.f.write(f"{self.name}\n")
            self.f.write(f"{self.name.capitalize()}\n")
            for self.addon in self.addons:
                self.f.write(f"{self.name}{self.addon}\n")
                self.f.write(f"{self.name.capitalize()}{self.addon}\n")
        print("Loading.\n")            
        #Manuplating Numbers
        for self.number in self.numbers:
            self.f.write(f"{self.number}\n")
            for self.name in self.names:
                self.f.write(f"{self.name}{self.number}\n")            
                self.f.write(f"{self.name}{self.number[0:3]}\n")            
                self.f.write(f"{self.name}{self.number[0:4]}\n")            
                self.f.write(f"{self.name}{self.number[0:5]}\n") 
                self.f.write(f"{self.name}@{self.number[0:3]}\n")            
                self.f.write(f"{self.name}@{self.number[0:4]}\n")            
                self.f.write(f"{self.name}@{self.number[0:5]}\n")            
                self.f.write(f"{self.name.capitalize()}{self.number[0:3]}\n")            
                self.f.write(f"{self.name.capitalize()}{self.number[0:4]}\n")            
                self.f.write(f"{self.name.capitalize()}{self.number[0:5]}\n")            
                self.f.write(f"{self.name.capitalize()}@{self.number[0:3]}\n")            
                self.f.write(f"{self.name.capitalize()}@{self.number[0:4]}\n")            
                self.f.write(f"{self.name.capitalize()}@{self.number[0:5]}\n")
        print("Loading...\n")            
        
        #Manuplating Dates
        for self.date in self.dates:
            self.f.write(f"self.date\n")
            for self.name in self.names:
                self.f.write(f"{self.name.capitalize()}@{self.date[0:2]}\n")
                self.f.write(f"{self.name.capitalize()}@{self.date[0:4]}\n")   
                self.f.write(f"{self.name.capitalize()}@{self.date[4:8]}\n")   
                self.f.write(f"{self.name.capitalize()}@{self.date[0:8]}\n")   
                self.f.write(f"{self.name}@{self.date[0:2]}\n")   
                self.f.write(f"{self.name}@{self.date[0:4]}\n")   
                self.f.write(f"{self.name}@{self.date[0:8]}\n")
                self.f.write(f"{self.name}@{self.date[4:8]}\n")  

                self.f.write(f"{self.name.capitalize()}{self.date[0:2]}\n")
                self.f.write(f"{self.name.capitalize()}{self.date[0:4]}\n")   
                self.f.write(f"{self.name.capitalize()}{self.date[4:8]}\n")   
                self.f.write(f"{self.name.capitalize()}{self.date[0:8]}\n")   
                self.f.write(f"{self.name}{self.date[0:2]}\n")   
                self.f.write(f"{self.name}{self.date[0:4]}\n")   
                self.f.write(f"{self.name}{self.date[0:8]}\n")
                self.f.write(f"{self.name}{self.date[4:8]}\n") 
        print("Loading.....\n")            
        
        #Manuplating Keywords
        for self.keyword in self.keywords:
            self.f.write(f"{self.keyword}\n")
            self.f.write(f"Iam{self.keyword}\n")
            self.f.write(f"Iam{self.keyword.capitalize()}\n")
            self.f.write(f"iam{self.keyword}\n")
            self.f.write(f"iam{self.keyword.capitalize()}\n")
            self.f.write(f"1am{self.keyword}\n")
            self.f.write(f"1am{self.keyword.capitalize()}\n")


            for self.name in self.names:
                self.f.write(f"{self.keyword}{self.name}\n") 
                self.f.write(f"{self.keyword.capitalize()}{self.name}\n")                   
                self.f.write(f"{self.keyword.capitalize()}{self.name.capitalize()}\n")                   
                self.f.write(f"{self.keyword}{self.name.capitalize()}\n")   
        
        #Manuplating keywords names and addons
        for self.name in self.names:
            for self.keyword in self.keywords:
                for self.addon in self.addons:
                    self.f.write(f"{self.keyword}{self.name}{self.addon}\n")
                    self.f.write(f"{self.name}{self.keyword}{self.addon}\n")
                    self.f.write(f"{self.name}{self.addon}{self.keyword}\n")
                    self.f.write(f"{self.keyword}{self.addon}{self.name}\n")

                                    







wordlist = createlists("My_wordlists")
