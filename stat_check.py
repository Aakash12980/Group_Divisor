import sqlite3
import pandas
import random
from os import system
from time import sleep

conn = sqlite3.connect('STAT.db')
cur = conn.cursor()

def main():
    system('cls')
    print("\n\n\n\n\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||")
    print("\t\t\t\t\t\t\t\t ||   Data Management System    ||")
    print("\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||\n")
    print("\t\t\t\t\t\t<>|-------------------------------------------------------------|<>")
    print("\n\n\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>><<<<<<<<<<<<<<<||")
    print("\t\t\t\t\t\t\t\t ||   	    1. Add Data         ||")
    print("\t\t\t\t\t\t\t\t ||     2. Select the Group     ||")
    print("\t\t\t\t\t\t\t\t || 3. View Table/Delete Record ||")
    print("\t\t\t\t\t\t\t\t ||     4. Update a Record      ||")
    print("\t\t\t\t\t\t\t\t ||           E. Exit           ||")
    print("\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>><<<<<<<<<<<<<<<||")
    print("\n\n\t\t\t\t\t\t\t\t<>|-----------------------------|<>")
    try:
        choice = input("\n\n\t\t\t\t\t\t\t\t\tEnter your choice: ").upper()
        if choice == '1':
            add()
        elif choice == '2':
            select()
        elif choice == '3':
            view()
        elif choice == '4':
            update()
        elif choice == 'E':
            system('cls')
            exit()
        else:
            main()
    except KeyboardInterrupt:
        main()

def add():
    system('cls')
    try:
        fname = input("\n\n\n\t\t\t\t\t\t\t\t\tEnter your First Name: ").capitalize()
        mname = input("\t\t\t\t\t\t\t\t\tEnter your Middle Name: ").capitalize()
        lname = input("\t\t\t\t\t\t\t\t\tEnter your Last Name: ").capitalize()
        while True:
            zone = input("\n\n\t\t\t\t\t\t\t\t\tEnter your Zone(A/B/C/D): ").upper()
            if zone not in ['A', 'B', 'C', 'D']:
                print("\n\n\t\t\t\t\t\t\t\t\tPlease Enter Valid Zone.")
                continue
            break
    except KeyboardInterrupt:
        print("\n\n\t\t\t\t\t\t\t\t\tPlease Enter Valid Information.")
        sleep(3)
        add()
    cur.execute('INSERT INTO Data (FNAME, MNAME, LNAME, ZONE) VALUES (?, ?, ?, ?)',
                                    (fname, mname, lname, zone))
    conn.commit()
    system('cls')
    print("\n\n\n\n\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||")
    print("\t\t\t\t\t\t\t\t || Your Data Has been Updated ||")
    print("\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||\n")
    sleep(3)
    system('cls')
    while True:
        try:
            choice1 = input("\n\n\t\t\t\t\t\tPress Y to add more Data or Press B to Go Back or Press E to Exit: ").upper()
            if choice1 == 'Y':
                add()
            elif choice1 == 'B':
                main()
            elif choice1 == 'E':
                system('cls')
                exit()
            else:
                print("\n\n\n\n\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||")
                print("\t\t\t\t\t\t\t\t ||        Invalid Input!      ||")
                print("\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||\n")
                sleep(3)
                continue
        except KeyboardInterrupt:
            continue

def select():
    system('cls')
    try:
        choice = input("\n\n\n\t\t\t\t\t\t\t\t\tSelect a Group(A/B/C/D): ").upper()
        if choice in ['A', 'B', 'C', 'D']:
            cur.execute("SELECT ID, FNAME, MNAME, LNAME, ZONE FROM Data WHERE ZONE == '%s'" %choice)
        else:
            print("\n\n\n\n\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||")
            print("\t\t\t\t\t\t\t\t ||  Please Select Valid Zone  ||")
            print("\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||\n")
            select()
    except KeyboardInterrupt:
        select()
    data = cur.fetchall()
    length = len(data)
    print("\n\n\t\t\t\t\t\t\t\t<>|-----------------------------|<>")
    print("\t\t\t\t\t\t\t\t\tThis Zone has ", length, "data.")
    print("\t\t\t\t\t\t\t\t<>|-----------------------------|<>")
    while True:
        try:
            percent = int(input("\n\n\t  \t\t\t\t\t\tHow many percentage of data do you want to retrieve(1-100): "))
        except:
            print("\n\n\t\t\t\t\t\t\t\t<>|-----------------------------|<>")
            print("\t\t\t\t\t\t\tPlease enter numeric value between 1 to 100.")
            print("\n\n\t\t\t\t\t\t\t\t<>|-----------------------------|<>")
            continue
        if percent > 0 and percent <= 100:
            total = int(percent*length/100)
            if (total-1)<0:
                print("\n\n\t\t\t\t\t\t\t\t<>|-------------------------------------|<>")
                print("\t\t\t\t\t\t\t\t    Please enter higher value of Percent.")
                print("\t\t\t\t\t\t\t\t<>|-------------------------------------|<>")
                continue
            break
        else:
            print("\n\n\t\t\t\t\t\t\t\t<>|-------------------------------------|<>")
            print("\t\t\t\t\t\t\t\t    Please enter value between 1 to 100.")
            print("\t\t\t\t\t\t\t\t<>|-------------------------------------|<>")
            continue
    print("\n\n\t\t\t\t\t\t\t\t<>|---------------------------------|<>")
    print("\t\t\t\t\t\t\t\t   ", percent, "Percent of this data is:", total)
    print("\t\t\t\t\t\t\t\t<>|---------------------------------|<>")
    i=0
    flag = set()
    selected_data = list()
    while(i<total):
        rand = random.randint(0, length-1)
        if rand in flag:
            continue
        else:
            selected_data.append(data[rand])
        flag.add(rand)
        i += 1
    input("\n\n\t\t\t\t\t\t\t\t\tPress any key to see Data.\n\n")
    system('cls')
    title = ['ID', 'FNAME', 'MNAME', 'LNAME', 'ZONE']
    output = pandas.DataFrame(selected_data, columns = title)
    print("\n\n ", output)

    del selected_data
    del data
    del flag
    del output

    while True:
        try:
            choice1 = input("\n\nPlease press Y to Continue or B to Go Back or E to Exit: ").upper()
            if choice1 == 'Y':
                select()
            elif choice1 == 'B':
                main()
            elif choice1 == 'E':
                system('cls')
                exit()
            else:
                system('cls')
                print("Invalid Input! Please press Y to Continue or B to Go Back or E to Exit: ")
                continue
        except KeyboardInterrupt:
            continue

def view():
    system('cls')
    cur.execute("SELECT * FROM Data")
    data = cur.fetchall()
    title = ['ID', 'FNAME', 'MNAME', 'LNAME', 'ZONE']
    output = pandas.DataFrame(data, columns = title)
    print(output)
    del data
    while True:
        print("\n\n<>|*****************************************************************************|<>")
        try:
            choice = input("\n\nPress 1 to Update Record, 2 to Delete Record, B to Go Back or E to Exit: ").upper()
            if choice == '1':
                update()
            elif choice == '2':
                delet()
            elif choice == 'B':
                main()
            elif choice == 'E':
                system('cls')
                exit()
            else:
                print("\n\n\n\n\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||")
                print("\t\t\t ||        Invalid Input!      ||")
                print("\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||\n")
                continue
        except KeyboardInterrupt:
            continue
    del output
    del title
    system('cls')

def update():
    system('cls')
    try:
        id = int(input("\n\n\n\t\t\t\t\t\t\t\t    Enter the ID of data to Update: "))
    except:
        update()
    cur.execute('SELECT * FROM Data WHERE ID == ?', (id,))
    i_data = cur.fetchall()
    if(i_data == []):
        print("\n\n\t\t\t\t\t\t\t\t<>|-------------------------------------|<>")
        print("\t\t\t\t\t\t\t\t    Invalid ID. Please Enter Valid ID.")
        print("\t\t\t\t\t\t\t\t<>|-------------------------------------|<>")
        while True:
            try:
                choice = input("\n\n\t\t\t\t\t\t\t\tPress 1 to Continue, B to Go Back or E to Exit: ").upper()
                if choice == '1':
                    update()
                elif choice == 'B':
                    main()
                elif choice == 'E':
                    system('cls')
                    exit()
                else:
                    print("\n\n\n\n\t\t\t\t\t\t\t\t   ||>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<||")
                    print("\t\t\t\t\t\t\t\t   ||  Please Enter Valid Option.   ||")
                    print("\t\t\t\t\t\t\t\t   ||>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<||\n")
                    continue
            except KeyboardInterrupt:
                continue

    while True:
        try:
            choice = input("\n\t\t\t\t\t    Press 1 to Update First Name, 2 for Middle Name, 3 for Last Name and 4 for Zone: ")
            if choice == '1':
                fname = input("\n\n\n\t\t\t\t\t\t\t\t Enter First Name: ").capitalize()
                cur.execute('UPDATE Data SET FNAME = ? WHERE ID == ?', (fname, id))
                conn.commit()
                break
            elif choice =='2':
                mname = input("\n\n\n\t\t\t\t\t\t\t\t Enter Middle Name: ").capitalize()
                cur.execute('UPDATE Data SET MNAME = ? WHERE ID == ?', (mname, id))
                conn.commit()
                break
            elif choice == '3':
                lname = input("\n\n\n\t\t\t\t\t\t\t\t Enter Last Name: ").capitalize()
                cur.execute('UPDATE Data SET LNAME = ? WHERE ID == ?', (lname, id))
                conn.commit()
                break
            elif choice == '4':
                zone = input("\n\n\n\t\t\t\t\t\t\t\t Enter Zone: ").capitalize()
                cur.execute('UPDATE Data SET ZONE = ? WHERE ID == ?', (zone, id))
                conn.commit()
                break
            else:
                print("\n\n\n\n\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<||")
                print("\t\t\t\t\t\t\t\t ||         Wrong Choice!       ||")
                print("\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<||\n")
                choice = input("\n\t\t\t\t\t\t\t\tPress 1 to Continue, B to Go Back and E to Exit:").upper()
                if choice == '1':
                    continue
                elif choice == 'B':
                    main()
                elif choice == 'E':
                    exit
                else:
                    continue
        except:
            print("\n\n\t\t\t\t\t\t\t\t\t<>|-----------------------------------------------------|<>")
            print("\t\t\t\t\t\t\t\t\t   Wrong data Entered. Please Enter Valid Information.")
            print("\t\t\t\t\t\t\t\t\t<>|-----------------------------------------------------|<>")
            sleep(3)
            while True:
                system('cls')
                try:
                    choice1 = input("\n\t\t\t\t\t\t\t\tPress 1 to continue, B to Go Back or E to Exit: ").upper()
                    if choice1 == '1':
                        break
                    elif choice1 == 'B':
                        update()
                    elif choice1 == 'E':
                        exit()
                    else:
                        print("\n\n\n\n\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||")
                        print("\t\t\t\t\t\t\t\t || Please Enter Valid Option. ||")
                        print("\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||\n")
                        continue
                except KeyboardInterrupt:
                    continue
        continue
    del i_data
    system('cls')
    print("\n\n\n\n\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||")
    print("\t\t\t\t\t\t\t\t || Your Data Has been Updated ||")
    print("\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||\n")
    sleep(3)
    main()

def delet():
    system('cls')
    try:
        id = int(input("\n\n\n\t\t\t\t\t\t\t\t\tEnter ID Data to Delete: "))
    except:
        delet()
    cur.execute('SELECT * FROM Data WHERE ID == ?', (id,))
    del_info = cur.fetchall()
    if del_info == []:
        print("\n\n\t\t\t\t\t\t\t\t<>|-------------------------------------|<>")
        print("\t\t\t\t\t\t\t\t    Invalid ID. Please Enter Valid ID.")
        print("\t\t\t\t\t\t\t\t<>|-------------------------------------|<>")
        while True:
            try:
                choice = input("\n\n\t\t\t\t\t\t\t      Press 1 to Continue, B to Go Back or E to Exit: ").upper()
                if choice == '1':
                    delet()
                elif choice == 'B':
                    main()
                elif choice == 'E':
                    system('cls')
                    exit()
                else:
                    print("\n\n\n\n\t\t\t\t\t\t\t\t    ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||")
                    print("\t\t\t\t\t\t\t\t    ||  Please Enter Valid Option  ||")
                    print("\t\t\t\t\t\t\t\t    ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||\n")
                    continue
            except KeyboardInterrupt:
                continue
    print("\n\n\n\t\t\t\t\t\t<>|---------------------------------------------------------------------------------|<>")
    print("\t\t\t\t\t\t\t    Are you sure to Delete the data of", del_info[0][1], del_info[0][2], del_info[0][3], "?")
    print("\t\t\t\t\t\t<>|---------------------------------------------------------------------------------|<>")
    del del_info
    while True:
        try:
            choice = input("\n\n\n\t\t\t\t\t\t\t\t    Press 1 to delete or B to Go Back: ").upper()
            if choice == '1':
                cur.execute('DELETE FROM Data WHERE ID == ?', (id,))
                conn.commit()
                system('cls')
                print("\n\n\n\n\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||")
                print("\t\t\t\t\t\t\t\t || Your Data Has been Deleted ||")
                print("\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||\n")
                sleep(3)
                main()
            elif choice == 'B':
                view()
            else:
                print("\n\n\n\n\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||")
                print("\t\t\t\t\t\t\t\t ||        Invalid Input!      ||")
                print("\t\t\t\t\t\t\t\t ||>>>>>>>>>>>>>>><<<<<<<<<<<<<<||\n")
                continue
        except KeyboardInterrupt:
            continue

main()
conn.close()
