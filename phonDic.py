# Software name : Phone Directory #
# Developed in 10/12/2023 #
#------------------------------------#
# This program written as part of satr.code plateform 
# I wrote this program for training pourposes 
# You are free to run,modify or alter any part of this program under your knowledge 
# To run this program use your terminal i.e C:/python.exe phoneDic.py
#------------------------------------#


persons_dict={'Amal':'1111111111',
              'Mohammed':'2222222222',
              'Khadijah':'3333333333',
              'Abdullah':'4444444444',
              'Rawan':'5555555555',
              'Faisal':'6666666666',
              'Layla':'7777777777'}

def search_by_number(n):

    result=""
    if str(n).isdigit() and len(n)==10:
        for k,v in persons_dict.items():
            if v==n:
                result=k
                break
            else:
                result='Sorry, the number is not found'
    else:
        result="This is invalid number"
    return result

def search_by_name(s):
    
    result=""
    if str(s).isalpha():
        for k,v in persons_dict.items():
            if k==s:
                result=v
                break
            else:
                result='Sorry, the name is not found\n'
    else:
        result="This is invalid name\n"
    return result
def list_dictionary():
    print(35*'*')
    print ('Here your Phone Directory!')
    [print(k , ':' , v,'\n',30*'-') for k,v in persons_dict.items() ]
    print('Total Recored is :',len(persons_dict))

def add_new_contact(name,number):
    current_items=len(persons_dict)
    persons_dict[name]=number
    if len(persons_dict)-current_items==1:
        print ('New contact was succesfully added!')
        print ('Your new dictionary has ', len(persons_dict) , 'entry.')
    else:
        print ('Sorry , somthing goes wrong please try again later!')
    list_dictionary()
    
def banner():    
    print(65*'#')
    print('Welcome to Phone Dictionary.')
    print('This program was written as solution of satr.code project.')
    print('Please use this project for educational and training pourposes.')
    print('You are free to change and edit any line based on your kowlegde.')
    print('You will run this software under your responsability.')
    print(65*'#')

def menu():
    print('N to search for contact number')
    print('S to search for person contact')
    print('L to list the directory')
    print('A to add new contact')
    print('Q to quite\n')

def entry_validation(msg,c):
    entry=""
    Error=""
    Inv=True
    while(Inv):
        getuser_input=input(msg)
        if str(c).isdigit():
           if len(getuser_input)==c:
              entry = getuser_input
              Inv=False
              break
           else:
                Error='Please enter exactly '+str(c)+'digits'
        elif str(c).isalpha():
            if str(getuser_input).isalpha():
              entry = getuser_input
              Inv=False
              break
        else:
            Error='Please correct your entry'
        print(Error)
    return entry

        

banner()

r=True
while(r):
    menu()
    getuserinput=input('Please enter your search method:\n')
    getuserinput=str(getuserinput).lower()
    if getuserinput=='n':
        msg='Please enter 10 digits Numbers:\n'
        print(search_by_number(entry_validation(msg,10)),'\n')
    elif getuserinput=='s':        
        msg='Please enter a person name:\n'
        print(search_by_name(entry_validation(msg,'s')),'\n')
    elif getuserinput=='l':
        list_dictionary()
    elif getuserinput=='a':
        msg='Please Enter Name:'
        ginam=entry_validation(msg,'s')
        msg='Please Enter Number:'
        ginum=entry_validation(msg,10)    
        add_new_contact(ginam,ginum)
    elif getuserinput=='q':
        print('Good Bye!')
        r=False
        
    else:
        print('Please select n or s for search or q for quite')
