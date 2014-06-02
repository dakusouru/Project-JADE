# Jaded Artificial Discussion Simulator v. 1.02a

import random
import time
import math
import webbrowser
import urllib.request
import os
import re
import platform ##platform.node() => 'NSAisWatchingU'
import getpass ##getpass.getuser()

dictionary_page = "http://www.oxforddictionaries.com/definition/english/SEARCHSTRING?q=SEARCHSTRING"

'''
def split_data_OLD(line,st):
    st_ind = 0
    li = []
    if st in line:
        line_e = line.replace('\n','')
        if ']]' in line_e:
            line_e = line_e.replace(']]','\n')
        li = list(line_e)
    st_ind = li.index(st)
    a = []
    for z in range(st_ind):
        a.append(li[z])
    b = []
    for z in range(len(li) - st_ind - 1):
        b.append(li[st_ind + z + 1])
    el1 = ''.join(a)
    el2 = ''.join(b)
    final = [el1,el2]
    return final
'''

def parse(line,sep_main='$',sep_inor='|',sep_inand='&',sep_outor='#',sep_linefeed=']]'):

    line_charlist = []
    list_inor = []
    list_inand = []
    list_outor = []
    list_all = []

    if sep_main in line:
        line = line.replace('\n','')
        if sep_linefeed in line:
            line = line.replace(sep_linefeed,'\n')
            
        ## start real parse
        if sep_outor in line.split(sep_main)[1]:
            list_outor = line.split(sep_main)[1].split(sep_outor)
        else:
            list_outor = line.split(sep_main)[1]
        ##print('OUTOR:',list_outor)

        if sep_inand in line and sep_inor in line:
            list_inand = line.split(sep_main)[0].split(sep_inand)
            list_inand[0] = list_inand[0].split(sep_inor)
            list_all = [list_inand,list_outor]
            #print('ALL ORAND:',list_all)
        elif sep_inand in line:
            list_inand = line.split(sep_main)[0].split(sep_inand)
            list_all = [list_inand,list_outor]
            #print('ALL AND:',list_all)
        elif sep_inor in line:
            list_inor = line.split(sep_main)[0].split(sep_inor)
            list_all = [[list_inor,''],list_outor]
            #print('ALL OR:',list_all)
        else:
            list_all = line.split(sep_main)
            list_all = [[['',''],list_all[0]],list_outor]
            #print('ALL NONE:',list_all)
        
##        for y in list_all:
##            for x in y:
##                print(x)
##            print()
        ##print(list_all)
        return list_all

def make_readable(inp):
    s = inp.lower()

    if ',' in s:
        s = s.replace(',','')
    if '\n' in s:
        s = s.replace('\n',' ')
    if '\'' in s:
        s = s.replace('\'','')
    if ' u ' in s:
        s = s.replace(' u ',' you ')
    if ' r ' in s:
        s = s.replace(' r ',' are ')
    if 'pls' in s:
        s = s.replace('pls','please')
    if 'thnx' in s:
        s = s.replace('thnx','thanks')
    if 'thx' in s:
        s = s.replace('thx','thanks')
    if ' ur ' in s:
        s = s.replace(' ur ',' your ')
    if '?' in s:
        s = s.replace('?','')
    if 'ok' in s:
        s = s.replace('ok','okay')
    if 'oke' in s:
        s = s.replace('oke','okay')
    if 'oky' in s:
        s = s.replace('oky','okay')
    if 'okey' in s:
        s = s.replace('okey','okay')
    if '$' in s:
        s = s.replace('$','DOLLAR')
    if '&' in s:
        s = s.replace('&','and')
    if '#' in s:
        s = s.replace('#','NUMBER')
    if ']]' in s:
        s = s.replace(']]','BRACKETS')
    
    return s

def read(b, path):
    inputt = []
    outputt = []

    with open(path,'r') as file:
        lines = file.readlines()
        txt = ''
        for x in lines:
                ##parse() is here
            p = parse(x)
            inputt.append(p[0])
            outputt.append(p[1])

    if b == 'in':
        #print(inputt)
        return inputt
    else:
        #print(outputt)
        return outputt

def bot(*t):
    #average_typing_speed = 300
    #average_lettres_per_word = 5
    #speedfac = (average_lettres_per_word * average_typing_speed / 60) ** (-1)

    for x in range(len(t)):
        #r = speedfac * len(str(t[x]))
        #if r > 5:
        #    r = 5
        r = 0.5
        time.sleep(r)
        print('JADE: '+str(t[x]))

def mult(*a):
    r = random.randint(0,len(a)-1)
    p = random.choice(a)
    return p #(str(a[r]))

def browse(inp,url):
    bot(inp)
    time.sleep(2)
    webbrowser.open(url)

def define(term):
    website = 'http://www.yourdictionary.com/{0}'.format(str(term))
##    print(website)
    code = ''
    with urllib.request.urlopen(website) as page:
        code = str(page.read())
    matches = []
    for m in re.finditer('custom_entry', code):
        matches.append([m.start(), m.end()])
##        print('Found')
    code = code[matches[2][1]+11:len(code)]
    endnum = code.find('<')
    code = code[0:endnum]
##    print(matches[2])
    try:
        if code[0:6] == 'The def' or code[0:6] == 'An exam' or (code[0].isupper() and code[1].islower()):
            return code
        else:
            return 'Sorry, I can\'t find the definition of {0}.'.format(term)
    except:
        return 'Sorry, I can\'t find the definition of {0}.'.format(term)

def store(inp,path):
     with open(path,'a') as out_file:
        out_file.write(str(inp) + '\n')

def JADE():

    input_count = 0
    input_history = []
    path_files = 'lib'

    if os.path.exists('./' + path_files):
        pass
    else:
        path_files = path_files
        os.mkdir('./' + path_files)
        with open(path_files + '\\lib_match.aiso','w') as f1:
            f1.write('match$outmatch')
        with open(path_files + '\\lib_contain.aiso','w') as f2:
            f2.write('contain$outcontain\n')
        with open(path_files + '\\lib_history.aiso','w') as f3:
            f3.write('historyout\n')
        
    input_match = read('in',path_files + '\\lib_match.aiso')
    output_match = read('out',path_files + '\\lib_match.aiso')
    input_contain = read('in',path_files + '\\lib_contain.aiso')
    output_contain = read('out',path_files + '\\lib_contain.aiso')

    error_messages = ['I don\'t understand.','I can\'t quite grasp the essence of what you said.']
    error_messages.append('I\'m sorry, your previous message is beyond my comprehension.')
    error_messages.append('I didn\'t really catch that, I\'m afraid.')
    error_messages.append('Could you try rephrasing that, please?')
    
    
    print(r'           _____  _________  ____________  _____________   ')
    print(r'           \   / / _______ \ \   _______ \ \   ________/   ')
    print(r'            | | | |       | | | |       | | | |            ')
    print(r'            | | | |       | | | |       | | | |            ')
    print(r'            | | | |_______| | | |       | | | |______      ')
    print(r'     ____   | | |  _______  | | |       | | |  ______\     ')
    print(r'    / __ \  | | | |       | | | |       | | | |            ')
    print(r'   / /  \_| | | | |       | | | |       | | | |            ')
    print(r'  | |_______| | | |       | | | |_______| | | |_________   ')
    print(r'  |___________| |_|       |_| |__________/ /____________\  ')
    print(r'                                                           ')
 
    print('You are now chatting with Jaded Artificial Discussion Emulator, or JADE.')
    print('Ask for a definition by using \'define /term/\'.')
    print('')
    print('Type \'quit\' to abort the session.\n')

    while True:
        #Temporary:
        #print(input_contain,'<<>>',output_contain)
        #print('')
        #print(input_match,'<<>>',output_match)
        
        inp = str(input('User: '))
        i = make_readable(inp)

        store(inp,path_files + '\\lib_history.aiso')
        input_count += 1
        input_history.append(inp)

        if i == 'quit':
            bot(mult('I hope to see you soon.','Goodbye.'))
            store('---END OF SESSION---',path_files + '\\lib_history.aiso')
            #Temporary:
            for w in input_history:
                print(w)
            break
        elif not any(x in i for x in 'abcdefghijklmnopqrstuvwxyz:;)!?@\\#&|\'"'):
            bot(mult('Why didn\'t you say anything?','Try and actually say something?'))
        elif i.split(' ')[0] == 'define':
            bot(define(i[7:]))
        elif 'what is my name' in i:
            yourname = getpass.getuser()
            time.sleep(1)
            bot('Your name is {0}, I think.'.format(yourname))
        elif 'fibonacci' in i:
            phi = 0.5*math.sqrt(5)+0.5
            def fib(n):
                return int((math.pow(phi,n)-math.pow(1-phi,n))/math.sqrt(5))
            for x in range(42):
                bot(fib(x))
                ##time.sleep(x/21)
            bot('Et cetera.')
            time.sleep(1)
            bot('I think I\'ll just stop at the 42nd.')
        elif 'python' in i:
            bot(i)
        elif any(x[1] == i for x in input_match):
            for x in input_match:
                if x[1] == i:
                    bot(mult(output_match[input_match.index(x)]))
                    break
        
        elif any(x[1] in i for x in input_contain):
            for x in input_contain:
                if x[1] in i:
                    for z in x[0]:
                        if z in i:
                            bot(mult(output_contain[input_contain.index(x)]))
                            continue
        else:
            bot('ERROR')
            #itemlist = error_messages
            
##        OLD IF CONTAIN            
##        elif any(x in i for x in input_contain):
##            for x in input_contain:
##                if x in i:
##                    bot(output_contain[input_contain.index(x)])
    
    print('\nEnd of session.\nInput count = {}'.format(input_count))
    #browse('I\'ll open facebook for you :)','http://facebook.com')

JADE()



