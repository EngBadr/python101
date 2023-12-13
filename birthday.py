# Software name : BirthDay Calculator #
# Developed in 12/12/2023 #
#------------------------------------#
# This program written as part of satr.code plateform 
# I wrote this program for training pourposes 
# You are free to run,modify or alter any part of this program under your knowledge 
# To run this program use your terminal i.e C:/python.exe birthday
#------------------------------------#

def getuserentry(**kwargs):

    print(kwargs)


def menu():
        print('Please enter persons names followed by date and press enter after each entry')
        print('Please use comma to seperate person name and birth date. i.e Ahmed Khalid, 15-10-1995')
        print('Once you have done enter the letter s to save your work')

def getuserInput():
    r=True
    allentries=""
    print('Please enter person name followed by birthdate\n' )
    while(r):
        
        userdataentry=input()
        if userdataentry!='s':
            allentries+=userdataentry+' , '
        else:    
            r=False
            break


    return allentries



def prepareDctionary(allentries):
    dic=allentries.replace(',',':')
    print (dic)



menu()
prepareDctionary(getuserInput())