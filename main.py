# Email Validator / Email Verifier

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


email = input("Enter your Email : ")  # Input from user

# email = email.lower()  # For AI based email verifier i.e. gmail

# k, j, d = 0, 0, 0  # Initialising k, j, d with 0
k = 0
j = 0
d = 0

if len(email) >= 6:  # If length of email is greater then 6 (g@g.in)

    if email[0].isalpha():  # First letter of email must be an alphabet

        if ("@" in email) and (email.count("@") == 1):  # Email must contain only one '@'

            if (email[-4] == ".") ^ (email[-3] == "."):  # Email must contain only one '.'

                for i in email:

                    if i == i.isspace():  # Email does not contain any space
                        k = 1

                    elif i.isalpha():

                        if i == i.upper():  # Email does not contain any uppercase character
                            j = 1

                    elif i.isdigit():  # Return to the loop
                        continue

                    elif i == "_" or i == "." or i == "@":
                        continue

                    else:  # If there exist any other special character
                        d = 1

                if k == 1:
                    print("Wrong Email!!! Email does not contain space(s).")

                elif j == 1:
                    print("Wrong Email!!! Email does not contain uppercase character.")

                elif d == 1:
                    print("Wrong Email!!! Email does not contain any other special character.")

                else:
                    print("This email is valid.")

            else:
                print("Wrong Email!!! Email must contain atleast one '.'.")

        else:
            print("Wrong Email!!! Email must contain only one '@'.")

    else:
        print("Wrong Email!!! First character of email must be an Alphabet.")

else:
    print("Wrong Email!!! Email must contain atleast 6 character.")
