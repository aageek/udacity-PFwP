import time
import webbrowser

total_break = 3
break_count = 0

print ("This Program started on "+ time.ctime())
while(break_count < total_break) :
    time.sleep(1)
    webbrowser.open("http://www.youtube.com/watch?v=iJllh7l-D3g")

    break_count = break_count + 1

print ("This Program finished on "+ time.ctime())
