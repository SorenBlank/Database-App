import sqlite3
con = sqlite3.connect("Family.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Family (Name TEXT, Type TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Secret (Username Text, Email TEXT, PASS TEXT)")

while True:
    #questions_id
    print("Chose Option- ")
    print("1/ Login")
    print("2/ Sign Up")
    print("3/ Close")
    ask_id = int(input())
    if ask_id == 1:
        try:
            ask_email = input("Email: ")
            cur.execute("SELECT*FROM Secret WHERE Email = ?", (ask_email,))
            row = cur.fetchone()
            if ask_email in row:
                ask_pass = input("Password: ")
                if row == (row[0], ask_email, ask_pass):
                    print()
                    print("        DATABASE ACCESSED")
                    print()
                    while True:
                        #questions
                        print("Choose Option- ")
                        print("1/ Add More Members.")
                        print("2/ Remove Members.")
                        print("3/ See the list of all members.")
                        print("4/ Get Information about one specific member.")
                        print("5/ Go Back")
                        ask = int(input("Input: "))

                        #option_1
                        if ask == 1:
                            while True:
                                print()
                                que1_of_1 = input("Member Name: ")
                                que2_of_1 = input("Member Type: ")
                                cur.execute("INSERT INTO Family (Name, Type) VALUES(?, ?)", (que1_of_1, que2_of_1))
                                con.commit()
                                cur.execute("SELECT*FROM Family")
                                all = cur.fetchall()
                                print()
                                if (que1_of_1, que2_of_1) in all:
                                    print("Operation Successfull")
                                else:
                                    print("Operation Unsuccessfull")
                                print()
                                cur.execute("SELECT*FROM Family")
                                all = cur.fetchall()
                                print("Do you want to add more? y/n")
                                que3_of_1 = input()
                                if que3_of_1 == "n":
                                    break

                        #option_2
                        elif ask ==2:
                            cur.execute("SELECT*FROM Family")
                            all = cur.fetchall()
                            if len(all) > 0:
                                while True:
                                    print()
                                    cur.execute("SELECT*FROM Family ORDER BY NAME ASC")
                                    all = cur.fetchall()
                                    ii = 1
                                    for i in all:
                                        print(ii, i[0])
                                        ii = ii + 1
                                    que1_of_2 = int(input("Which member you want to remove: "))
                                    element = all[que1_of_2 - 1][1]
                                    cur.execute("DELETE FROM Family WHERE Type = ?", (element,))
                                    con.commit()
                                    if element not in all:
                                        print()
                                        print("Operation Successful")
                                    else:
                                        print()
                                        print("Operation Unsccessful")
                                    print()
                                    cur.execute("SELECT*FROM Family")
                                    all = cur.fetchall()
                                    if len(all) > 0:
                                        print("Do you want to remove more? y/n")
                                        que2_of_2 = input()
                                        if que2_of_2 == "n":
                                            break
                                    else:
                                        break
                            else:
                                print()
                                print("No member")
                                print()

                        #option_3
                        elif ask == 3:
                            print()
                            cur.execute("SELECT*FROM Family ORDER BY NAME ASC")
                            all = cur.fetchall()
                            if len(all) > 0:
                                ii = 1
                                for i in all:
                                    print(ii, i[0])
                                    ii = ii + 1
                                print()
                            else:
                                print("The list is empty")

                        #option_4
                        elif ask == 4:
                            cur.execute("SELECT*FROM Family ORDER BY NAME ASC")
                            all = cur.fetchall()
                            if len(all) > 0:
                                print()
                                cur.execute("SELECT*FROM Family ORDER BY NAME ASC")
                                all = cur.fetchall()
                                ii = 1
                                for i in all:
                                    print(ii, i[0])
                                    ii = ii + 1
                                print()
                                que4_of_1 = int(input("About which member you want to get information: "))
                                print()
                                print("Name:",all[que4_of_1-1][0])
                                print("Type:",all[que4_of_1-1][1])
                                print()
                            else:
                                print("The list is empty")

                        #option_5
                        elif ask == 5:
                            break

                        else:
                            print()
                            print("Wrong input. Please try again.")
                            print()
                else:
                    print("The password is wrong. Press T for trying again or Q to exit.")
                    last = input()
                    if last == "Q" or 'q':
                        break
        
        except:
            print("There's no account connected to the email. Please try again")

    elif ask_id == 2:
        ask_username_signup = input("Username: ")
        ask_email_signup = input("Email: ")
        ask_pass_signup = input("Password: ")
        cur.execute("INSERT INTO Secret(Username, Email, PASS) VALUES (?,?,?)",(ask_username_signup, ask_email_signup, ask_pass_signup))
        con.commit()

    elif ask_id == 3:
        break

    else:
        print()
        print("Wrong input. Please try again.")
        print()

con.commit()
con.close()