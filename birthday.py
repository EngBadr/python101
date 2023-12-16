# Software name : BirthDay Calculator #
# Developed in 12/12/2023 #
#------------------------------------#
# This program written as part of satr.code plateform 
# I wrote this program for training pourposes 
# You are free to run,modify or alter any part of this program under your knowledge 
# To run this program use your terminal i.e C:/python.exe birthday
#------------------------------------#
import datetime



def menu():
        print('Please enter persons names followed by date and press enter after each entry')
        print('Please use comma to seperate person name and birth date. i.e Ahmed Khalid, 15-10-1995')
        print('Once you have done enter the letter s to save your work')


def getuserInput():
    r=True
    allentries=""
    clean_dict=''
    print('Please enter person name followed by birthdate\n' )
    while(r):
        
        userdataentry=input()
        if userdataentry!='s':
            allentries+=userdataentry+' | '
        else:    
            r=False
            break
    
    #print(cleaned_data)
    try:
        cleaned_data=clean_entry(allentries)
        if cleaned_data[1]:
            clean_dict=prepareDctionary(cleaned_data[0])
    except BaseException as e:
            err_printer(e)
            err_printer('Please Correct Your Entry')
            if check_user_descion().upper()=='Y':
                getuserInput()
            else:
                err_printer('Good Day!')
                exit()
                
    return clean_dict

def clean_entry(allentries):
    data=allentries.strip()
    data=str(data).rstrip('|')
    data=(data).split('|')
    data=[i.strip() for i in data] 
    #print(data)
    persons=[]
    cleaned=False
    for i in data:
        person_name=i[0:i.rfind(' ')].strip()
        person_bd=i[i.rfind(' '):len(i)].strip()
        if valid_names(person_name) and valid_date(person_bd):
            persons.append(person_name)
            persons.append(person_bd)
            cleaned=True
        else:
            persons=[]
            cleaned=False
            break

    return [persons,cleaned]
        

def prepareDctionary(persons):
    dict_list=[]
    #print(persons)
    for i in range(0,len(persons),2):
        dict_list.append({'name':persons[i],'birthdate':persons[i+1]})

    return dict_list

def valid_names(name):
    spc='"\'[@_!#$%^&*()<>?/\|}{~:]'
    valid_name=False
    if (i for i in name if i not in spc and (str(i).isalpha() or str(i).isspace())) :
         valid_name=True
    return valid_name
     
def valid_date(birth_date):
     valid_date=False
     if  bool(datetime.datetime.strptime(birth_date,'%d-%m-%Y')):
        valid_date=True
     return valid_date 
            
#


def format_entry(name, birthdate):
    print('person name is {} his/her age is {}'.format(name,age_calaulate(birthdate)))
    print(70*'-')

def age_calaulate(birthdate):
    today=datetime.datetime.today().date().strftime('%d-%m-%Y')
    today=datetime.datetime.strptime(today,"%d-%m-%Y") 
    to_date=datetime.datetime.strptime(birthdate,"%d-%m-%Y")
    years=str(today.year-to_date.year)
    months=str(today.month-to_date.month)
    days=str(today.day-to_date.day)
    result=years+' years  and ' + months + ' months and ' + days + ' days , he/she was born on ' + str(to_date.strftime('%A'))
    
    return result

def check_user_descion():
    input_again=input('Would you like to start over? (Y/N) :')
    return input_again

def err_printer(msg):
    print(msg)

def prepare_tuple(results):
    age_lists=tuple()
    for i in range(0,len(results)):
        age_list_to_date=datetime.datetime.strptime(results[i]['birthdate'],'%d-%m-%Y')
        age_lists+=(age_list_to_date,)
    return age_lists

def get_old_young(results):
    age_lists=prepare_tuple(results)
    oldest_person=age_lists.index(min(age_lists))
    youngest_person=age_lists.index(max(age_lists))

    return [results[oldest_person]['name'],results[youngest_person]['name']]

def sorted_results(results):
    #for i in range(0,len(results)):
        #age_date_to_str=sorted(datetime.datetime.strftime('%d-%m-%Y'))
    list_of_dates=[]
    for i in range(0,len(results)):
        item_date=datetime.datetime.strptime(results[i]['birthdate'],'%d-%m-%Y')
        item_name=results[i]['name']
        list_of_dates.append([item_date,item_name])
    sorted_names=sorted([k for k in list_of_dates])
    print('Here your Sorted Entry from older to younger : \n' )
    for i in range(0,len(sorted_names)):
        print(sorted_names[i][1])
    

def reveresd_list(results):
    list_of_items=[]
    for i in range(0,len(results)):
        item_date=results[i]['birthdate']
        item_name=results[i]['name']
        list_of_items.append([item_name,item_date])
    list_of_items=list_of_items[::-1]
    print('Here Your revered Entry: \n')
    for i in range(0,len(list_of_items)):
        print('{} {} '.format(list_of_items[i][0],list_of_items[i][1])) 

def born_on_sunday_only(results):
    list_of_items=[]
    for i in range(0,len(results)):
        if datetime.datetime.strptime(results[i]['birthdate'],'%d-%m-%Y').weekday()==6:
            list_of_items.append(results[i]['name'])
    if len(list_of_items)>0:
        print('People born on Sunday are:')
        [print(i) for i in list_of_items]
        
    else:
        print('No one born on Sunday \n')
    

r=True
while(r):
    menu()
    results=getuserInput()
    if len(results)>0:
        for i in results:
            format_entry(**i)

        print('The oldest person is : ', get_old_young(results)[0])
        print('The youngest person is : ', get_old_young(results)[1])
        print(70*'-')
        sorted_results(results)
        print(70*'-')
        print('Total Persons: ',len(results))
        print(70*'-')
        reveresd_list(results)
        print(70*'-')
        born_on_sunday_only(results)
        print(70*'-')
    if check_user_descion().upper()=='N':
        err_printer('Good Day!!')
        r=False
