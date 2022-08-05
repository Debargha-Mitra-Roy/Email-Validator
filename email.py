# Email Validator / Email Verifier using regex

'''
    Rules for Email Validator :-
     1. Length of email is greater then 6
     2. First letter of email must be an alphabet
     3. Email must contain only one '@'
     4. Email must contain atleast one '.'
     5. Email does not contain any space
     6. Email does not contain any uppercase character
     7. Email does not contain any other special character except {'_', '.', '@'}
'''


import re

print("ALERT : This email verifier does not work for official mails.")

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input("Enter your Email : ")  # Input from user

# email = email.lower()  # For AI based email verifier i.e. gmail

if re.search(email_condition, user_email):
    print("This email is valid.")

else:
    print("Wrong Email!!!")


'''
    Drawback : This email verifier does not works for official mail.
'''
