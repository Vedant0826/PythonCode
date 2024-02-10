from pywhatkit import *
from datetime import datetime


if __name__ == "__main__":
    
    contact_dict = {
        # add your contact list here like
        #"name":"+91xxxxxxxxxx"
    }

    #showing contacts to send messages
    for name in contact_dict:
        print(name, end="\t")

    print()
    selected_contact = input("enter name to whom send messages> ").capitalize()

    if selected_contact in contact_dict:
        mobile_no = contact_dict.get(selected_contact)

        #asking for troll message
        troll = input("do you want to send 100 msg(yes/no)> ")
        if troll == "yes":
            msg = input("enter msg> ")
            
            ls = []
            for i in range(100):
                ls.append(msg)
                troll_msg = "\n".join(ls)
            
            now = datetime.now()
            str_time = now.strftime("%H:%M")
            hour, min = str_time.split(":")
            hour = int(hour)
            min = int(min)+1
            sendwhatmsg(mobile_no, troll_msg, hour, min, wait_time=8, tab_close=True)

        #if troll is not selected
        else:
            print("=======enter message========")

            #getting multiline input
            buffer = []
            while True:
                print("> ", end="")
                line = input()
                if line == ".":
                    break
                buffer.append(line)

            multiline_string = "\n".join(buffer)
            print("You entered...")
            print()
            print(multiline_string)

            #asking for targeted time
            ask_for_time = input("do you want to send message now(yes/no)> ").lower()
        
            if ask_for_time == "yes":
                now = datetime.now()
                str_time = now.strftime("%H:%M")

                hour, min = str_time.split(":")
                hour = int(hour)
                min = int(min) + 1

                sendwhatmsg(mobile_no, multiline_string, hour, min, wait_time=10, tab_close=True)
        
            elif ask_for_time == "no":
                late_hour = int(input("enter hour> "))
                late_min = int(input("enter minute> "))

                sendwhatmsg(mobile_no, multiline_string, late_hour, late_min, wait_time=10, tab_close=True)
        
            else:
                print("invalid option selected")

    #if contect is out of list
    else:
        print("please check contact")
