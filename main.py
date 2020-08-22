import pyautogui 
import schedule 
import time 
from datetime import datetime
import calendar
meettime=50
def findDay(): 
    now=datetime.today().strftime('%Y-%m-%d')
    year,month,day=now.split("-")
    year=int(year)
    month=int(month)
    day=int(day)
    dayNumber = calendar.weekday(year, month, day) 
    days =["monday", "tuesday", "wednesday", "thursday", 
                         "friday", "saturday", "sunday"] 
    return (days[dayNumber])
def attendClass(id1,password):
    time.sleep(0.1)
    pyautogui.press('esc',interval=0.06)
    time.sleep(0.08)
    pyautogui.press('win',interval=0.3)
    pyautogui.write('zoom')
    pyautogui.press('enter',interval=0.5)
    time.sleep(5)
    x,y = pyautogui.locateCenterOnScreen('join.png')
    pyautogui.click(x,y)
    pyautogui.press('enter',interval=3)
    pyautogui.write(id1)
    pyautogui.press('enter',interval=1)
    pyautogui.write(password)
    pyautogui.press('enter',interval = 5)
    time.sleep(meettime) 
    pyautogui.hotkey('alt','f4')
    time.sleep(0.5)
    pyautogui.hotkey('alt','f4')
def Class1():
	c1={"monday":[,],"tuesday":[],
	"wednesday":[],"thursday":[],
	"friday":[],"saturday":[]}
	day=findDay()
	id=c1[day][0]
	password=c1[day][1]
	attendClass(str(id1),str(password))	
def Class2():
	c2={"monday":[],"tuesday":[],
	"wednesday":[],"thursday":[],
	"friday":[],"saturday":[]}
	day=findDay()
	id=c2[day][0]
	password=c2[day][1]
	attendClass(str(id1),str(password))
def Class3():
	c3={"monday":[],"tuesday":[],
	"wednesday":[],"thursday":[],
	"friday":[],"saturday":[]}
	day=findDay()
	id1=c3[day][0]
	password=c3[day][1]
	attendClass(str(id1),str(password))
def Class4():
	c4={"monday":[],"tuesday":[],
	"wednesday":[],"thursday":[],
	"friday":[],"saturday":[]}
	day=findDay()
	id1=c4[day][0]
	password=c4[day][1]
	attendClass(str(id1),str(password))	
schedule.every().day.at("09:00").do(Class1)
schedule.every().day.at("10:00").do(Class2)
schedule.every().day.at("11:00").do(Class3)
schedule.every().day.at("12:00").do(Class4)
while True: 
	schedule.run_pending() 
	time.sleep(1)