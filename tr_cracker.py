import os, time
from colorama import Fore
import pyfiglet
import random
import string

def home_menu():
    print(f"\n{Fore.BLUE}[1] {Fore.WHITE}Brutal Mobile Number\n")
    print(f"{Fore.LIGHTGREEN_EX}[2] {Fore.WHITE}Customize Password list\n")
    print(f"{Fore.LIGHTCYAN_EX}[3] {Fore.WHITE}Brutal PIN (5/6/8/9) Digit\n")
    print(f"{Fore.RED}[00] {Fore.WHITE}EXIT")
    
def brutal_home():
    print(f"\n{Fore.YELLOW}[A] {Fore.WHITE}Airtel Number Passlist")
    print(f"{Fore.BLUE}[B] {Fore.WHITE}Banglalink Number Passlist")
    print(f"{Fore.LIGHTGREEN_EX}[G] {Fore.WHITE}Grameenphone Number Passlist")
    print(f"{Fore.RED}[R] {Fore.WHITE}Robi Number Passlist")
    print(f"{Fore.CYAN}[T] {Fore.WHITE}Teletalk Number Passlist")
    print(f"{Fore.MAGENTA}[99] {Fore.WHITE}All Number Brutal Passlist")
    print(f"{Fore.LIGHTBLUE_EX}[0] {Fore.WHITE}Back Home")

def pen_generate_home():
    print(f"\n{Fore.BLUE}[4] {Fore.WHITE}4 Digit PIN Generate")
    print(f"{Fore.GREEN}[5] {Fore.WHITE}5 Digit PIN Generate")
    print(f"{Fore.LIGHTCYAN_EX}[6] {Fore.WHITE}6 Digit PIN Generate")
    print(f"{Fore.LIGHTRED_EX}[7] {Fore.WHITE}7 Digit PIN Generate")
    print(f"{Fore.YELLOW}[8] {Fore.WHITE}8 Digit PIN Generate")
    print(f"{Fore.LIGHTCYAN_EX}[9] {Fore.WHITE}9 Digit PIN Generate")
    print(f"{Fore.LIGHTMAGENTA_EX}[0] {Fore.WHITE}Back Home")
    
def back_home():
    back_hm = input(f"\n{Fore.GREEN}[B] {Fore.WHITE}Back Home {Fore.RED}[E] {Fore.WHITE}Exit >>> ").lower()
    if back_hm == "e":
        main_banner()
        cl()
        time.sleep(2)
        print(f"\n{Fore.GREEN}[+] Clear all logs")
        time.sleep(1)
        print(f"{Fore.GREEN}[+] Clear all data")
        time.sleep(2)
        print(F"\n{Fore.LIGHTRED_EX}EXIT SUCESSFUL !!!\n{Fore.WHITE}")
        os._exit(0)
    else:
        main()
def cl():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def warning():
    print(f"\n{Fore.YELLOW}Warning: {Fore.RED}This is very powerful program.You must have a good device and almost 10GB+ free stroage")
    confrom = input(Fore.CYAN+"\nDo you run this heavy program [y/n] >>> ").lower()
    if confrom == "y":
        print("")
    else:
        main()
def main_banner():
    title = pyfiglet.figlet_format("TR CRACKER")
    print(Fore.LIGHTMAGENTA_EX+title)
    print(f"{Fore.WHITE}Github: {Fore.YELLOW}trfahim")
    print(f"{Fore.WHITE}Youtube: {Fore.RED}TR CYBER LAB\n")
def banner_1():
    ban_1_input = input(f"\n{Fore.RED}Press Enter to start the process: ") 
    print(f"{Fore.GREEN}\nIt takes time. Its depends on your device capability.\n{Fore.WHITE}Wait some times......\n") 
   
def brutal_number():
    brutal_home()
    home_input = input(f"\n{Fore.CYAN}>>>>> {Fore.WHITE}")
    
    if home_input == "A" or home_input == "a":
        banner_1()
        num_title = "Airtel"
        num_input = "016"
        file_name = (f"{num_title}_Passlist.txt")
    elif home_input == "B" or home_input == "b":
        banner_1()
        num_title = "Banglalink"
        num_input = "019"
        file_name = (f"{num_title}_Passlist.txt")       
    elif home_input == "G" or home_input == "g":
        banner_1()
        num_title = "Grameenphone"
        num_input = "017"
        file_name = (f"{num_title}_Passlist.txt")   
    elif home_input == "R" or home_input == "r":
        banner_1()
        num_title = "Robi"
        num_input = "018"
        file_name = (f"{num_title}_Passlist.txt")  
    elif home_input == "T" or home_input == "t":
        banner_1()
        num_title = "Teletalk"
        num_input = "015"
        file_name = (f"{num_title}_Passlist.txt")    
    elif home_input == "99":
        warning()
        banner_1()
        num_title = "Brutal Number"
        num_input = "016"
        num_input_2 = "019"
        num_input_3 = "017"
        num_input_4 = "018"
        num_input_5 = "015"
        num_input_6 = "013"
        num_input_7 = "014"
        file_name = (f"{num_title}_Passlist.txt")   
    elif home_input == "0":
        back_home()
    else:
        cl()
        print(Fore.RED+"\nInvalid Input !!! TRY AGAIN....")
        time.sleep(3)
        main()
                        
    with open(file_name, "w") as file:
        if home_input != "99":
            for pass_num in range (9999999, 99999999):
                password_number = (f"{num_input}{pass_num}")
                file.write(password_number + "\n")       
        else:
            for pass_num in range (9999999, 99999999):
                password_number = (f"{num_input}{pass_num}")
                file.write(password_number + "\n")                   
                if num_input_2:
                    password_number_2 = (f"{num_input_2}{pass_num}")
                    file.write(password_number_2 + "\n")
                if num_input_3:
                    password_number_3 = (f"{num_input_3}{pass_num}")
                    file.write(password_number_3 + "\n") 
                if num_input_4:
                    password_number_4 = (f"{num_input_4}{pass_num}")
                    file.write(password_number_4 + "\n")   
                if num_input_5:
                    password_number_5 = (f"{num_input_5}{pass_num}")
                    file.write(password_number_5 + "\n")
                if num_input_6:
                    password_number_6 = (f"{num_input_6}{pass_num}")
                    file.write(password_number_6 + "\n")
                if num_input_7:
                    password_number_7 = (f"{num_input_7}{pass_num}")
                    file.write(password_number_7 + "\n")
    cl()
    main_banner()
    print("\n")
    print(Fore.RED+"-"*60)
    print(f"{Fore.YELLOW}'{file_name}' {Fore.WHITE}Password List Save Sucessful") 
    print(Fore.RED+"-"*60)  
    back_home()

def customize_passlist(first_name, middle_name, last_name,
                        first_name_ca, first_name_lo,first_name_ti,
                        middle_name_ca,middle_name_lo,middle_name_ti,
                        last_name_ca,last_name_lo,last_name_ti, phone_num,
                        birth_day, birth_month,birth_year,file_name):
    passwords = []
    symbol_at = ("@")
    symbol_hash = ("#")
    symbol_and = ("&")
    passwords.append(f"{first_name}")
    passwords.append(f"{first_name_ca}")
    passwords.append(f"{first_name_lo}")
    passwords.append(f"{first_name_ti}")
    passwords.append(f"{first_name}{symbol_at}")
    passwords.append(f"{first_name_ca}{symbol_at}")
    passwords.append(f"{first_name_lo}{symbol_at}")
    passwords.append(f"{first_name_ti}{symbol_at}")
    passwords.append(f"{first_name}{symbol_hash}")
    passwords.append(f"{first_name_ca}{symbol_hash}")
    passwords.append(f"{first_name_lo}{symbol_hash}")
    passwords.append(f"{first_name_ti}{symbol_hash}")
    passwords.append(f"{first_name}{symbol_and}")
    passwords.append(f"{first_name_ca}{symbol_and}")
    passwords.append(f"{first_name_lo}{symbol_and}")
    passwords.append(f"{first_name_ti}{symbol_and}")
    if middle_name:
        passwords.append(f"{middle_name}")
        passwords.append(f"{middle_name_ca}")
        passwords.append(f"{middle_name_lo}")
        passwords.append(f"{middle_name_ti}")
        
    for zero in range (5, 21):
        passwords.append("0"*zero)      
    passwords.append(f"{last_name}")
    passwords.append(f"{last_name_ca}")
    passwords.append(f"{last_name_lo}")
    passwords.append(f"{last_name_ti}")
    passwords.append(f"{last_name}{symbol_at}")
    passwords.append(f"{last_name_ca}{symbol_at}")
    passwords.append(f"{last_name_lo}{symbol_at}")
    passwords.append(f"{last_name_ti}{symbol_at}")
    passwords.append(f"{last_name}{symbol_hash}")
    passwords.append(f"{last_name_ca}{symbol_hash}")
    passwords.append(f"{last_name_lo}{symbol_hash}")
    passwords.append(f"{last_name_ti}{symbol_hash}")
    passwords.append(f"{last_name}{symbol_and}")
    passwords.append(f"{last_name_ca}{symbol_and}")
    passwords.append(f"{last_name_lo}{symbol_and}")
    passwords.append(f"{last_name_ti}{symbol_and}")
    full_name_1 = f"{first_name}{middle_name}{last_name}" if middle_name else f"{first_name}{last_name}"
    passwords.append(f"{full_name_1}")
    passwords.append(f"{full_name_1.upper()}")
    passwords.append(f"{full_name_1.lower()}")
    passwords.append(f"{full_name_1.title()}")
    full_name_2 = f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"
    passwords.append(f"{full_name_2.upper()}")
    passwords.append(f"{full_name_2.lower()}")
    passwords.append(f"{full_name_2.title()}")
    ## NEW UPDATE 2.0
    if phone_num:
        passwords.append(f"{phone_num}")
        passwords.append(f"{first_name}{symbol_at}{phone_num}")
        passwords.append(f"{first_name}{symbol_hash}{phone_num}")
        passwords.append(f"{first_name}{symbol_and}{phone_num}")
        passwords.append(f"{last_name}{symbol_at}{phone_num}")
        passwords.append(f"{last_name}{symbol_hash}{phone_num}")
        passwords.append(f"{last_name}{symbol_and}{phone_num}")
        
    if birth_day:
        all_birth = (birth_day+birth_month+birth_year)
        passwords.append(f"{birth_day}")
        passwords.append(f"{birth_month}")
        passwords.append(f"{birth_year}")
        passwords.append(f"{all_birth}")  
        passwords.append(f"{birth_day}{birth_month}")
        passwords.append(f"{birth_month}{birth_year}")
        passwords.append(f"{birth_day}{birth_year}")
        passwords.append(f"{first_name}{phone_num}")
        passwords.append(f"{last_name}{phone_num}")
        passwords.append(f"{first_name}{birth_day}")
        passwords.append(f"{first_name}{birth_month}")
        passwords.append(f"{first_name}{birth_year}")
        passwords.append(f"{last_name}{birth_day}")
        passwords.append(f"{last_name}{birth_month}")
        passwords.append(f"{last_name}{birth_year}")
        passwords.append(f"{first_name}{symbol_at}{birth_day}")
        passwords.append(f"{first_name}{symbol_at}{birth_month}")
        passwords.append(f"{first_name}{symbol_at}{birth_year}")
        passwords.append(f"{first_name}{symbol_hash}{birth_day}")
        passwords.append(f"{first_name}{symbol_hash}{birth_month}")
        passwords.append(f"{first_name}{symbol_hash}{birth_year}")
        passwords.append(f"{first_name}{symbol_and}{birth_day}")
        passwords.append(f"{first_name}{symbol_and}{birth_month}")
        passwords.append(f"{first_name}{symbol_and}{birth_year}")
        passwords.append(f"{last_name}{symbol_at}{birth_day}")
        passwords.append(f"{last_name}{symbol_at}{birth_month}")
        passwords.append(f"{last_name}{symbol_at}{birth_year}")
        passwords.append(f"{last_name}{symbol_hash}{birth_day}")
        passwords.append(f"{last_name}{symbol_hash}{birth_month}")
        passwords.append(f"{last_name}{symbol_hash}{birth_year}")
        passwords.append(f"{last_name}{symbol_and}{birth_day}")
        passwords.append(f"{last_name}{symbol_and}{birth_month}")
        passwords.append(f"{last_name}{symbol_and}{birth_year}")
        passwords.append(f"{first_name}{all_birth}")
        passwords.append(f"{first_name}{symbol_at}{all_birth}")
        passwords.append(f"{first_name}{symbol_hash}{all_birth}")
        passwords.append(f"{first_name}{symbol_and}{all_birth}")
        passwords.append(f"{last_name}{all_birth}")
        passwords.append(f"{last_name}{symbol_at}{all_birth}")
        passwords.append(f"{last_name}{symbol_hash}{all_birth}")
        passwords.append(f"{last_name}{symbol_and}{all_birth}")
    
    if middle_name and birth_day:
        passwords.append(f"{middle_name}{phone_num}")
        passwords.append(f"{middle_name}{birth_day}")
        passwords.append(f"{middle_name}{birth_month}")
        passwords.append(f"{middle_name}{birth_year}")
        passwords.append(f"{middle_name}{symbol_at}{phone_num}")
        passwords.append(f"{middle_name}{symbol_hash}{phone_num}")
        passwords.append(f"{middle_name}{symbol_and}{phone_num}")
        passwords.append(f"{middle_name}{symbol_at}{birth_day}")
        passwords.append(f"{middle_name}{symbol_at}{birth_month}")
        passwords.append(f"{middle_name}{symbol_at}{birth_year}")
        passwords.append(f"{middle_name}{symbol_hash}{birth_day}")
        passwords.append(f"{middle_name}{symbol_hash}{birth_month}")
        passwords.append(f"{middle_name}{symbol_hash}{birth_year}")
        passwords.append(f"{middle_name}{symbol_and}{birth_day}")
        passwords.append(f"{middle_name}{symbol_and}{birth_month}")
        passwords.append(f"{middle_name}{symbol_and}{birth_year}")
        passwords.append(f"{middle_name}{all_birth}")
        passwords.append(f"{middle_name}{symbol_at}{all_birth}")
        passwords.append(f"{middle_name}{symbol_hash}{all_birth}")
        passwords.append(f"{middle_name}{symbol_and}{all_birth}")

    for num in range(1000001): 
        digit = str(num)  
        
        passwords.append(f"{first_name}{digit}")
        passwords.append(f"{first_name_ca}{digit}")
        passwords.append(f"{first_name_lo}{digit}")
        passwords.append(f"{first_name_ti}{digit}")
        #Symbol_firstname
        #symbol_hash = ("@") FIRSTNAME 
        passwords.append(f"{first_name}{symbol_at}{digit}")
        passwords.append(f"{first_name_ca}{symbol_at}{digit}")
        passwords.append(f"{first_name_lo}{symbol_at}{digit}")
        passwords.append(f"{first_name_ti}{symbol_at}{digit}")
        #symbol_hash = ("#") FIRSTNAME
        passwords.append(f"{first_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{first_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{first_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{first_name}{symbol_hash}{digit}")
        #symbol_and = ("&") FIRSTNAME
        passwords.append(f"{first_name_ca}{symbol_and}{digit}")
        passwords.append(f"{first_name}{symbol_and}{digit}")
        passwords.append(f"{first_name_lo}{symbol_and}{digit}")
        passwords.append(f"{first_name_ti}{symbol_and}{digit}")
        if middle_name: 
            passwords.append(f"{middle_name}{digit}")
            passwords.append(f"{middle_name_ca}{digit}")
            passwords.append(f"{middle_name_lo}{digit}")
            passwords.append(f"{middle_name_ti}{digit}")
            #Symbol_middlename
            # symbol_at = ("@") Middle Name
            passwords.append(f"{middle_name_ca}{symbol_at}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_at}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_at}{digit}")
            passwords.append(f"{middle_name}{symbol_at}{digit}")
            # symbol_hash = ("#")
            passwords.append(f"{middle_name_ca}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_hash}{digit}")
            passwords.append(f"{middle_name}{symbol_hash}{digit}")
            # symbol_and = ("&")
            passwords.append(f"{middle_name_ca}{symbol_and}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_and}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_and}{digit}")
            passwords.append(f"{middle_name}{symbol_and}{digit}")
            # Symbol FirstName+MiddleName
            passwords.append(f"{first_name}{middle_name}{symbol_at}{digit}")
            passwords.append(f"{first_name_ca}{middle_name_ca}{symbol_at}{digit}")
            passwords.append(f"{first_name_lo}{middle_name_lo}{symbol_at}{digit}")
            passwords.append(f"{first_name_ti}{middle_name_ti}{symbol_at}{digit}")
            passwords.append(f"{first_name}{middle_name}{symbol_hash}{digit}")
            passwords.append(f"{first_name_ca}{middle_name_ca}{symbol_hash}{digit}")
            passwords.append(f"{first_name_lo}{middle_name_lo}{symbol_hash}{digit}")
            passwords.append(f"{first_name_ti}{middle_name_ti}{symbol_hash}{digit}")
            passwords.append(f"{first_name}{middle_name}{symbol_and}{digit}")
            passwords.append(f"{first_name_ca}{middle_name_ca}{symbol_and}{digit}")
            passwords.append(f"{first_name_lo}{middle_name_lo}{symbol_and}{digit}")
            passwords.append(f"{first_name_ti}{middle_name_ti}{symbol_and}{digit}")
            #Special Symbol MiddleName+LastName
            passwords.append(f"{middle_name}{last_name}{symbol_at}{digit}")
            passwords.append(f"{middle_name_ca}{last_name_ca}{symbol_at}{digit}")
            passwords.append(f"{middle_name_lo}{last_name_lo}{symbol_at}{digit}")
            passwords.append(f"{middle_name_ti}{last_name_ti}{symbol_at}{digit}")
            passwords.append(f"{middle_name}{last_name}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_ca}{last_name_ca}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_lo}{last_name_lo}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_ti}{last_name_ti}{symbol_hash}{digit}")
            passwords.append(f"{middle_name}{last_name}{symbol_and}{digit}")
            passwords.append(f"{middle_name_ca}{last_name_ca}{symbol_and}{digit}")
            passwords.append(f"{middle_name_lo}{last_name_lo}{symbol_and}{digit}")
            passwords.append(f"{middle_name_ti}{last_name_ti}{symbol_and}{digit}")
        #Symbol_lastname
        # symbol_at = ("@")
        passwords.append(f"{last_name_ca}{symbol_at}{digit}")
        passwords.append(f"{last_name_lo}{symbol_at}{digit}")
        passwords.append(f"{last_name_ti}{symbol_at}{digit}")
        passwords.append(f"{last_name}{symbol_at}{digit}")
        # symbol_hash = ("#")
        passwords.append(f"{last_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{last_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{last_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{last_name}{symbol_hash}{digit}")
        # symbol_and = ("&")
        passwords.append(f"{last_name_ca}{symbol_and}{digit}")
        passwords.append(f"{last_name_lo}{symbol_and}{digit}")
        passwords.append(f"{last_name_ti}{symbol_and}{digit}")
        passwords.append(f"{last_name}{symbol_and}{digit}")
        passwords.append(f"{last_name}{digit}")
        passwords.append(f"{last_name_ca}{digit}")
        passwords.append(f"{last_name_lo}{digit}")
        passwords.append(f"{last_name_ti}{digit}")
        full_name = f"{first_name}{middle_name}{last_name}" if middle_name else f"{first_name}{last_name}"
        passwords.append(f"{full_name}{digit}")
        passwords.append(f"{full_name.upper()}{digit}")
        passwords.append(f"{full_name.lower()}{digit}")
        passwords.append(f"{full_name.title()}{digit}")
        full_name_space = f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"
        passwords.append(f"{full_name_space}{digit}")
        passwords.append(f"{full_name_space.upper()}{digit}")
        passwords.append(f"{full_name_space.lower()}{digit}")
        passwords.append(f"{full_name_space.title()}{digit}")
        full_name_cap = f"{first_name.capitalize()}{middle_name.capitalize()}{last_name.capitalize()}" if middle_name else f"{first_name.capitalize()}{last_name.capitalize()}"
        passwords.append(f"{full_name_cap}{digit}")
        # Special Symbol FastName+LastName
        passwords.append(f"{first_name}{last_name}{symbol_at}{digit}")
        passwords.append(f"{first_name_ca}{last_name_ca}{symbol_at}{digit}")
        passwords.append(f"{first_name_lo}{last_name_lo}{symbol_at}{digit}")
        passwords.append(f"{first_name_ti}{last_name_ti}{symbol_at}{digit}")
        passwords.append(f"{first_name}{last_name}{symbol_hash}{digit}")
        passwords.append(f"{first_name_ca}{last_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{first_name_lo}{last_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{first_name_ti}{last_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{first_name}{last_name}{symbol_and}{digit}")
        passwords.append(f"{first_name_ca}{last_name_ca}{symbol_and}{digit}")
        passwords.append(f"{first_name_lo}{last_name_lo}{symbol_and}{digit}")
        passwords.append(f"{first_name_ti}{last_name_ti}{symbol_and}{digit}")
        # Special Symbol LastName+FirstName
        passwords.append(f"{last_name}{first_name}{symbol_at}{digit}")
        passwords.append(f"{last_name_ca}{first_name_ca}{symbol_at}{digit}")
        passwords.append(f"{last_name_lo}{first_name_lo}{symbol_at}{digit}")
        passwords.append(f"{last_name_ti}{first_name_ti}{symbol_at}{digit}")
        passwords.append(f"{last_name}{first_name}{symbol_hash}{digit}")
        passwords.append(f"{last_name_ca}{first_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{last_name_lo}{first_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{last_name_ti}{first_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{last_name}{first_name}{symbol_and}{digit}")
        passwords.append(f"{last_name_ca}{first_name_ca}{symbol_and}{digit}")
        passwords.append(f"{last_name_lo}{first_name_lo}{symbol_and}{digit}")
        passwords.append(f"{last_name_ti}{first_name_ti}{symbol_and}{digit}")
        passwords.append(f"{digit}") 
        passwords.append(f"{digit}{digit}")    
                         
    with open(file_name, "w") as file:
        for password in passwords:
            file.write(password + "\n")
    cl()
    main_banner()
    print("\n")
    print(Fore.RED+"-"*60)
    print(Fore.YELLOW+f"\nPassword list saved to {Fore.WHITE}'{file_name}'\n")
    print(Fore.RED+"-"*60)
    back_home()   

def pin_generate(): 
    pen_generate_home() 
    passwords = []
    pin_input = input("\n>>>> ")
    if pin_input == "4":
        start_num = 999
        end_num = 10000
        file_name = ("4_digit_pin.txt")
    elif pin_input == "5":
        start_num = 9999
        end_num = 100000
        file_name = ("5_digit_pin.txt")
    elif pin_input == "6":
        start_num = 99999
        end_num = 1000000
        file_name = ("6_digit_pin.txt")
    elif pin_input == "7":
        start_num = 999999
        end_num = 10000000
        file_name = ("7_digit_pin.txt")
    elif pin_input == "8":
        start_num = 9999999
        end_num = 100000000
        file_name = ("8_digit_pin.txt")
    elif pin_input == "9":
        warning()
        start_num = 99999999
        end_num = 1000000000
        file_name = ("9_digit_pin.txt")
    elif pin_input == "0":
        main()
    else:
        cl()
        print(f"\n{Fore.RED}Invalid Input !! TRY AGAIN...")
        time.sleep(3)
        main()
    time.sleep(2)
    banner_1()
    for pin in range(start_num, end_num):
        digit = int(pin)
        passwords.append(digit)
    
    with open(file_name, "w") as file:
        for pin_list in passwords:
            file.write(f"{pin_list}\n")
    cl()
    main_banner()
    print("\n")
    print(Fore.WHITE+"-"*60)
    print(f"{Fore.RED}Password Save as {Fore.YELLOW}'{file_name}'")
    print(Fore.WHITE+"-"*60)
    back_home()        
        
def main():
    cl()
    main_banner()
    home_menu()
    home_input = input(f"\n{Fore.CYAN}>>>>> ")
    
    if home_input == "1":
        cl()
        main_banner()
        brutal_number()
        
    elif home_input == "2":
        cl()
        main_banner()
        first_name = input(Fore.CYAN+f"\nTarget First Name >>{Fore.GREEN} ").strip()
        middle_name = input(Fore.CYAN+f"Target Middle Name {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ").strip()
        last_name = input(Fore.CYAN+f"Target Last Name >>{Fore.GREEN} ").strip()
        first_name_ca = first_name.upper()
        first_name_lo = first_name.lower()
        first_name_ti = first_name.title()
        middle_name_ca = middle_name.upper()
        middle_name_lo = middle_name.lower()
        middle_name_ti = middle_name.title()
        last_name_ca = last_name.upper()
        last_name_lo = last_name.lower()
        last_name_ti = last_name.title()
        phone_num = input(Fore.CYAN+f"Target Phone Number {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ").strip()
        birth_day = input(Fore.CYAN+f"\nTarget Birth Day {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ")
        birth_month = input(Fore.CYAN+f"Target Birth Month {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ")
        birth_year = input(Fore.CYAN+f"Target Birth Year {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ")
        banner_1()
        case1 = random.choice(string.ascii_letters)
        case2 = random.choice(string.digits)
        random_case = (f"{first_name.upper()}_{case1}{case2}")
        
        file_name = (f"Passwordlist_{random_case}.txt")
        customize_passlist(first_name, middle_name, last_name,
                            first_name_ca, first_name_lo,first_name_ti,
                            middle_name_ca,middle_name_lo,middle_name_ti,
                            last_name_ca,last_name_lo,last_name_ti, phone_num,
                            birth_day, birth_month,birth_year,file_name)                                  
    
    elif home_input == "3":
        cl()
        main_banner()
        pin_generate()
    
    elif home_input == "00":
        exit_in = input(f"\n{Fore.WHITE}Do you want to exit [{Fore.RED}y{Fore.WHITE}/{Fore.GREEN}n{Fore.WHITE}] >>> ").upper()
        if exit_in == "Y":
            cl()
            time.sleep(2)
            print(f"\n{Fore.GREEN}[+] Clear all logs")
            time.sleep(1)
            print(f"{Fore.GREEN}[+] Clear all data")
            time.sleep(2)
            print(F"\n{Fore.LIGHTRED_EX}EXIT SUCESSFUL !!!\n{Fore.WHITE}")
            os._exit(0)
        else:
            main()
    
    else:
        cl()
        print(Fore.RED+f"\n\n({home_input}) Invalid Input !! Try Again...")
        time.sleep(3)
        main()

if __name__ == "__main__":
    main()
