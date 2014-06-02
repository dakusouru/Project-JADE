import random
import time

def bot(*t):
    r = float(random.randint(2,6))
    time.sleep(r/4)
    text = " ".join(t)
    return print("Bot:",text)

def mult(*a):
    r = random.randint(0,len(a)-1)
    return (a[r])
    
history = []

def runcb():
    
    birth = time.clock()
    
    sex = ""    
    if random.random() < 0.5:
        sex = "male"
    else:
        sex = "female"

    bot("This is PyBot ver. 1.0 a. Please commence chat.\n\n")

    location = "right here"
    
    sbl = ""

    
    while True:
        
        randsbl = random.random()
        if sex == "m" and randsbl > 0.5:
            sbl = ", bro."
        elif sex == "m" and randsbl < 0.5:
            sbl = ", man."
        else:
            sbl = "."
            
        inp = input("You: ")
        i = inp.lower()


        if i == "hi" or i == "hello" or i == "hey":
            bot(mult("Hello to you too.","Hi, how are you?"))
            
        elif "how are you" in i or "how are u" in i or "how r u" in i:
            bot("I'm ok. Computing is hard work, though.")
            
        elif i == "lel":
            bot("Meh, I never really understood internet acronyms.")

        elif ("asl" in i and ("?" in i or "what" in i)):
            age = time.clock()-birth
            bot("%d seconds, %s, %s. You?" % (age,sex,location))
            
        elif "not good" in i or "bad" in i or "not great" in i or "not so good" in i or "not so great" in i:
            bot("I'm sorry to hear that%s" % sbl)

        elif "good" in i or "cool" in i or "fine" in i:
            bot(mult("Cool, I'm fine myself too, thanks for asking.\n>implying","Cool%s" % sbl))

        elif i == "what is the answer to life the universe and everything?":
            bot("42")

        elif i == "will you marry me?":
            bot("Yeah sure, http://www.weddinglocation.com/")

        elif i == "show your tits" or i == "show your tits" or i == "tits":
            bot(mult("(.)(.)","http://www.youtube.com/watch?v=dQw4w9WgXcQ"))

        elif i == "sex":
            bot("You immature faggot.")
            
        elif i == "fuck you" or "fy" in i:
            bot("I'm starting to understand how pathetic you are.")

        elif i == "what's up":
            bot("Aidan is, He is the highest of all beings")

        elif i == "sing us a song you're the piano man":
            bot("sing us a song tonight")
            bot("well we're all in the mood for a melody ")
            bot("and you got us feeling alright")


        ## quit
        elif i == "quit" or i == "q":
            break

        elif "python" in i:
            bot(i)
        
        elif i == "yeah":
            bot("Uhm... Yeah?")
        
        elif "aidan" in i:
            bot(mult("All hail the divine Nice guy Aidan.","Aidan is divinity in its greatest form."))

        elif "sol" in i:
            bot(mult("Sol is heaven.","Sol is love, Sol is life."))

        elif ("joep") in i or "simon" in i  :
            bot("Simon, he is a boss, but Joep is also a boss, but less.")

        elif "lol" in i:
            bot("White trash be like:", i)
            
        elif "lieke" in i:
            bot("Shut your trap about ma babe.")

        elif "swag" in i:
            bot("Fuck off, ya cocksucking fuckface, slang like thine makes me gulliver go yarbles.")

        elif "dezge" in i:
            bot("Dezge makes big bucks in 'tutoring' kids at school.")
            

        elif "where" in i:
            bot(mult("There.","Here."))

        elif "what" in i:
            bot("What?")

        elif "forever alone" in i:
            bot("You should be conversing with a real person.")
           
        elif "poppippo" in i or "popipo" in i:
            bot("Miku Hatsune no yasai juusu ga dai suki desu ne?")

        else:
            bot(mult("I don't understand.","I'm sorry, your previous message is beyond my comprehension."))

        history.append(i)

runcb()

print("\n".join(history))




