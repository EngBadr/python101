import datetime
class Account:
    op_date=datetime.datetime.today().date()
    op_time=datetime.datetime.today().time()
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance
        #self.holder_name=holder_name

    def get_balance(self):
        return self.balance
    
    def set_balance(self,balance):
        self.balance=balance
        
    def prepare_balance(self):
        self.balance=0
        print('Your account is prepared current Balance is ',self.balance )

class Withdraw():
    def operation(self,balance):
        Account.balance-=balance
        print('Amount of {} was withdrawen from your account on {} at {}'.format(self.balance,self.op_date,Account.op_time))
    
class Deposit():
    def operation(self):
        get_user_deposite=float(input('Please Enter Your deposit: '))
        Account.set_balance(get_user_deposite)
        print('Amount of {} deposited into your account on {} at {}'.format(Account.get_balance(),self.op_date,Account.op_time))

class Show():
    def operation(self):
        print('Your Current Balance is : {} '.format(self.get_balance()))


def Show_menu():
    print('Press Q To Query Your Account\n'+
          'Press W To Withdraw Form Your Account\n'+
          'Press D To Deposit To Your Account\n'+
          'To Exit Press E')
    
def get_user_input(question_type=True):
    if question_type:
        user_input=input('Please select your operation: ')
    else:
        user_input=input('Would you like to make another transaction? (Y/N)')
    return user_input

bkacc=Account('10000050607000',2000)
bkacc.prepare_balance()
Q=Show()
D=Deposit()
W=Withdraw()
Show_menu()
r=True
while(r):

    if get_user_input().upper()=='Q':
        Q.operation()
    elif get_user_input().upper()=='D':
        D.operation()
    elif get_user_input().upper()=='W':
        W.operation()
    elif get_user_input(False).upper()=='Y':
        pass
    else:
        print('Good Day!!')
        r=False


