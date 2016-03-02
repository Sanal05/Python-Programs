import webbrowser
import time

take_breaks = 3
break_count = 0
print("This program started on "+time.ctime()) 
while( break_count<take_breaks):
   time.sleep(15*60);
   webbrowser.open("https://www.youtube.com/watch?v=K99NPSkf8k4")
   break_count = break_count +1

