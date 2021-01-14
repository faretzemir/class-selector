from datetime import datetime
import calendar
import webbrowser
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


'''

print("Current Time =", current_time)
if(current_time == "20:22:00"):
    print("correct.")

print(datetime.today().strftime('%A'))

if (datetime.today().strftime('%A') == "Thursday"):
    print("Correct.")
    
'''

'''
print("Welcome to the Google Meet Chooser.")
print("1. Analog and Digital Communications")
print("2. Law for Engineers")
print("3. Software Engineering")
print("4. Engineer and Society")
print("5. Operating Systems")

subject = input("Please choose a subject.\n")
if(subject == 1):
    sub_type = input("Please choose lecture or tutorial.")
        if(sub_type == 1):
            selection = input("Please select a class.")

'''
print("Today's date is:")
print(datetime.today().strftime('%A')) 
print("The time is:")
print(current_time)

if (datetime.today().strftime('%A') == "Monday"): 
    if(current_time >= "08:55:00" and current_time < "10:55:00"):
        webbrowser.open("https://meet.google.com/lookup/cdve6muia3")
    elif(current_time >= "12:55:00" and current_time < "13:55:00"):
        webbrowser.open("https://meet.google.com/xog-dzek-oia")
    elif(current_time >= "16:55:00" and current_time < "17:55:00"):
        webbrowser.open("https://meet.google.com/lookup/g7lcbulcbe")
    elif(current_time >= "17:55:00" and current_time < "18:55:00"):
        webbrowser.open("https://meet.google.com/vsx-cswp-fmh")

elif (datetime.today().strftime('%A') == "Tuesday"):
    if(current_time >= "11:55:00" and current_time < "13:55:00"):
        webbrowser.open("https://meet.google.com/ipo-bvnn-eiq")
    elif(current_time >= "13:55:00" and current_time < "15:55:00"):
        webbrowser.open("https://meet.google.com/csn-ziom-sdd")

elif (datetime.today().strftime('%A') == "Wednesday"):
    if (current_time >= "11:55:00" and current_time < "13:55:00"):
        webbrowser.open("https://meet.google.com/nvy-xjxj-iwv")
    elif (current_time >= "13:55:00" and current_time < "14:55:00"):
        webbrowser.open("https://meet.google.com/lookup/g7lcbulcbe")

elif (datetime.today().strftime('%A') == "Thursday"):
    if (current_time >= "09:55:00" and current_time < "10:55:00"):
        webbrowser.open("https://meet.google.com/csn-ziom-sdd")
    elif(current_time >= "10:55:00" and current_time < "11:55:00"):
        webbrowser.open("https://meet.google.com/csn-ziom-sdd")
    elif(current_time >= "11:55:00" and current_time < "12:55:00"):
        webbrowser.open("https://meet.google.com/lookup/cdve6muia3")
    elif(current_time >= "12:55:00" and current_time <= "13:55:00"):
        webbrowser.open("https://meet.google.com/ner-svxs-ord")
    elif(current_time >= "16:55:00" and current_time <= "17:55:00"):
        webbrowser.open("https://meet.google.com/bda-opfi-nmp")
    
elif (datetime.today().strftime('%A') == "Friday"):
    if (current_time >= "09:55:00" and current_time < "11:55:00"):
        webbrowser.open("https://meet.google.com/lookup/g7lcbulcbe")

    

        