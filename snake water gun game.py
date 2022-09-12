print('''
█───█ █▀▀ █── █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 █▀▀ █▀▀▄ █▀▀█ █─█ █▀▀ 　 █───█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀█ 
█▄█▄█ █▀▀ █── █── █──█ █─▀─█ █▀▀ 　 ──█── █──█ 　 ▀▀█ █──█ █▄▄█ █▀▄ █▀▀ 　 █▄█▄█ █▄▄█ ──█── █▀▀ █▄▄▀ 
─▀─▀─ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀───▀ ▀▀▀ 　 ──▀── ▀▀▀▀ 　 ▀▀▀ ▀──▀ ▀──▀ ▀─▀ ▀▀▀ 　 ─▀─▀─ ▀──▀ ──▀── ▀▀▀ ▀─▀▀ 

█▀▀▀ █──█ █▀▀▄ 　 █▀▀▀ █▀▀█ █▀▄▀█ █▀▀ 
█─▀█ █──█ █──█ 　 █─▀█ █▄▄█ █─▀─█ █▀▀ 
▀▀▀▀ ─▀▀▀ ▀──▀ 　 ▀▀▀▀ ▀──▀ ▀───▀ ▀▀▀''')


import random  #"here random module is used to generate random choice.
import pyttsx3 #use to convert text into speech.


#declaration section.
engine=pyttsx3.init()
i=1
your_score=0
system_score=0

engine.say("welcome to game  enter your name")
engine.runAndWait()
j=input("\n\nenter your name:")
engine.say("wellcome")
engine.say(j)
engine.say("enjoy the game")
engine.runAndWait()
print("wellcome",j," enjoy the game ")



while i<=5:
    d=["snake","water","gun"]
    c=str(input("\nchoose any one[snake,water, gun]:"))
    c=c.lower()
    
    #"""use of random.choice function to give random strings from list d"""
    e=random.choice(d)


#now compare expresions using conditional statement
    
    if e==c:
        print ("your=",c,"system=",e,"\n",'''
▀▀█▀▀ █░░█ ░▀░ █▀▀ 　 █▀▀█ █▀▀█ █░░█ █▀▀▄ █▀▀▄ 　 ▀▀█▀▀ ░▀░ █▀▀ 
░▒█░░ █▀▀█ ▀█▀ ▀▀█ 　 █▄▄▀ █░░█ █░░█ █░░█ █░░█ 　 ░░█░░ ▀█▀ █▀▀ 
░▒█░░ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀░▀▀ ▀▀▀▀ ░▀▀▀ ▀░░▀ ▀▀▀░ 　 ░░▀░░ ▀▀▀ ▀▀▀''',"\n")

# we use comment to avoid confusion for other .
    elif c=="snake" and e=="water":
        print("your=",c,"system=",e,"\n",'''
█░░█ █▀▀█ █░░█ 　 █░░░█ █▀▀█ █▀▀▄ 　 ▀▀█▀▀ █░░█ ░▀░ █▀▀ 　 █▀▀█ █▀▀█ █░░█ █▀▀▄ █▀▀▄ 
█▄▄█ █░░█ █░░█ 　 █▄█▄█ █░░█ █░░█ 　 ░░█░░ █▀▀█ ▀█▀ ▀▀█ 　 █▄▄▀ █░░█ █░░█ █░░█ █░░█ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ░▀░▀░ ▀▀▀▀ ▀░░▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀░▀▀ ▀▀▀▀ ░▀▀▀ ▀░░▀ ▀▀▀░''',"\n")
        your_score=your_score+1

#THis is other expersion of conditional statement.

    elif c=="water" and e=="snake":
        print("your=",c,"system=",e,"\n",'''
█░░█ █▀▀█ █░░█ 　 █░░ █▀▀█ █▀▀ █▀▀ 　 ▀▀█▀▀ █░░█ ░▀░ █▀▀ 　 █▀▀█ █▀▀█ █░░█ █▀▀▄ █▀▀▄ 
█▄▄█ █░░█ █░░█ 　 █░░ █░░█ ▀▀█ █▀▀ 　 ░░█░░ █▀▀█ ▀█▀ ▀▀█ 　 █▄▄▀ █░░█ █░░█ █░░█ █░░█ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀░▀▀ ▀▀▀▀ ░▀▀▀ ▀░░▀ ▀▀▀░''',"\n")
        system_score=system_score+1

    elif c=="gun" and e=="snake":
        print("your=",c,"system=",e,"\n",'''
█░░█ █▀▀█ █░░█ 　 █░░░█ █▀▀█ █▀▀▄ 　 ▀▀█▀▀ █░░█ ░▀░ █▀▀ 　 █▀▀█ █▀▀█ █░░█ █▀▀▄ █▀▀▄ 
█▄▄█ █░░█ █░░█ 　 █▄█▄█ █░░█ █░░█ 　 ░░█░░ █▀▀█ ▀█▀ ▀▀█ 　 █▄▄▀ █░░█ █░░█ █░░█ █░░█ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ░▀░▀░ ▀▀▀▀ ▀░░▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀░▀▀ ▀▀▀▀ ░▀▀▀ ▀░░▀ ▀▀▀░''',"\n")
        your_score=your_score+1
        
    elif c=="water" and e=="gun":
        print("your=",c,"system=",e,"\n",'''
█░░█ █▀▀█ █░░█ 　 █░░░█ █▀▀█ █▀▀▄ 　 ▀▀█▀▀ █░░█ ░▀░ █▀▀ 　 █▀▀█ █▀▀█ █░░█ █▀▀▄ █▀▀▄ 
█▄▄█ █░░█ █░░█ 　 █▄█▄█ █░░█ █░░█ 　 ░░█░░ █▀▀█ ▀█▀ ▀▀█ 　 █▄▄▀ █░░█ █░░█ █░░█ █░░█ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ░▀░▀░ ▀▀▀▀ ▀░░▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀░▀▀ ▀▀▀▀ ░▀▀▀ ▀░░▀ ▀▀▀░''',"\n")
        your_score=your_score+1
        
    elif c=="gun" and e=="water":
        print("your=",c,"system=",e,"\n",'''
█░░█ █▀▀█ █░░█ 　 █░░ █▀▀█ █▀▀ █▀▀ 　 ▀▀█▀▀ █░░█ ░▀░ █▀▀ 　 █▀▀█ █▀▀█ █░░█ █▀▀▄ █▀▀▄ 
█▄▄█ █░░█ █░░█ 　 █░░ █░░█ ▀▀█ █▀▀ 　 ░░█░░ █▀▀█ ▀█▀ ▀▀█ 　 █▄▄▀ █░░█ █░░█ █░░█ █░░█ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀░▀▀ ▀▀▀▀ ░▀▀▀ ▀░░▀ ▀▀▀░''',"\n")
        system_score=system_score+1
        
    elif c=="snake" and e=="gun":
        print("your=",c,"system=",e,"\n",'''
█░░█ █▀▀█ █░░█ 　 █░░ █▀▀█ █▀▀ █▀▀ 　 ▀▀█▀▀ █░░█ ░▀░ █▀▀ 　 █▀▀█ █▀▀█ █░░█ █▀▀▄ █▀▀▄ 
█▄▄█ █░░█ █░░█ 　 █░░ █░░█ ▀▀█ █▀▀ 　 ░░█░░ █▀▀█ ▀█▀ ▀▀█ 　 █▄▄▀ █░░█ █░░█ █░░█ █░░█ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀░▀▀ ▀▀▀▀ ░▀▀▀ ▀░░▀ ▀▀▀░''',"\n")
        system_score=system_score+1
    else:
        print("wrong choice ")
        
    i=i+1



        #this part of code prints output.

print("\n\nyour final score=",your_score,"systems final score=",system_score,)

if system_score>your_score:
    engine.say("System wins better luck next time")
    engine.runAndWait()
    print('''
█▀▀ █░░█ █▀▀ ▀▀█▀▀ █▀▀ █▀▄▀█ 　 █░░░█ ░▀░ █▀▀▄ 　 █▀▀▄ █▀▀ ▀▀█▀▀ ▀▀█▀▀ █▀▀ █▀▀█ 　 █░░ █░░█ █▀▀ █░█ 
▀▀█ █▄▄█ ▀▀█ ░░█░░ █▀▀ █░▀░█ 　 █▄█▄█ ▀█▀ █░░█ 　 █▀▀▄ █▀▀ ░░█░░ ░░█░░ █▀▀ █▄▄▀ 　 █░░ █░░█ █░░ █▀▄ 
▀▀▀ ▄▄▄█ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░░▀ 　 ░▀░▀░ ▀▀▀ ▀░░▀ 　 ▀▀▀░ ▀▀▀ ░░▀░░ ░░▀░░ ▀▀▀ ▀░▀▀ 　 ▀▀▀ ░▀▀▀ ▀▀▀ ▀░▀ 

█▀▀▄ █▀▀ █░█ ▀▀█▀▀ 　 ▀▀█▀▀ ░▀░ █▀▄▀█ █▀▀ 
█░░█ █▀▀ ▄▀▄ ░░█░░ 　 ░░█░░ ▀█▀ █░▀░█ █▀▀ 
▀░░▀ ▀▀▀ ▀░▀ ░░▀░░ 　 ░░▀░░ ▀▀▀ ▀░░░▀ ▀▀▀''')
elif system_score==your_score:
    engine.say("This match tie well done")
    engine.runAndWait()
    print("match tie")
else:
    engine.say("yeaaahhhh hhhaaa   congraulation   you won")
    engine.runAndWait()
    print('''
█▀▀ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ █░░█ █░░ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀█ █▀▀▄ 
█░░ █░░█ █░░█ █░▀█ █▄▄▀ █▄▄█ █░░█ █░░ █▄▄█ ░░█░░ ▀█▀ █░░█ █░░█ 
▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀▀ ▀░▀▀ ▀░░▀ ░▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀▀ ▀░░▀''',"\n",'''
█░░█ █▀▀█ █░░█ 　 █░░░█ █▀▀█ █▀▀▄ 
█▄▄█ █░░█ █░░█ 　 █▄█▄█ █░░█ █░░█ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ░▀░▀░ ▀▀▀▀ ▀░░▀''',"\n")

