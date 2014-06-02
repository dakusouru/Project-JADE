#
#                   _____                     _____                     _____                     _____          
#                  /\    \                   /\    \                   /\    \                   /\    \         
#                 /::\    \                 /::\    \                 /::\    \                 /::\    \        
#                 \:::\    \               /::::\    \               /::::\    \               /::::\    \       
#                  \:::\    \             /::::::\    \             /::::::\    \             /::::::\    \      
#                   \:::\    \           /:::/\:::\    \           /:::/\:::\    \           /:::/\:::\    \     
#                    \:::\    \         /:::/__\:::\    \         /:::/  \:::\    \         /:::/__\:::\    \    
#                    /::::\    \       /::::\   \:::\    \       /:::/    \:::\    \       /::::\   \:::\    \   
#           _____   /::::::\    \     /::::::\   \:::\    \     /:::/    / \:::\    \     /::::::\   \:::\    \  
#          /\    \ /:::/\:::\    \   /:::/\:::\   \:::\    \   /:::/    /   \:::\ ___\   /:::/\:::\   \:::\    \ 
#         /::\    /:::/  \:::\____\ /:::/  \:::\   \:::\____\ /:::/____/     \:::|    | /:::/__\:::\   \:::\____\
#         \:::\  /:::/    \::/    / \::/    \:::\  /:::/    / \:::\    \     /:::|____| \:::\   \:::\   \::/    /
#          \:::\/:::/    / \/____/   \/____/ \:::\/:::/    /   \:::\    \   /:::/    /   \:::\   \:::\   \/____/ 
#           \::::::/    /                     \::::::/    /     \:::\    \ /:::/    /     \:::\   \:::\    \     
#            \::::/    /                       \::::/    /       \:::\    /:::/    /       \:::\   \:::\____\    
#             \::/    /                        /:::/    /         \:::\  /:::/    /         \:::\   \::/    /    
#              \/____/                        /:::/    /           \:::\/:::/    /           \:::\   \/____/     
#                                            /:::/    /             \::::::/    /             \:::\    \         
#                                           /:::/    /               \::::/    /               \:::\____\        
#                                           \::/    /                 \::/____/                 \::/    /        
#                                            \/____/                   ~~                        \/____/         
#
#

import random
import time
import math
import webbrowser

def split_data(line,st):
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

def parse(line,sep_main='$',sep_inor='|',sep_inand='&',sep_outor='#',sep_linefeed=']]'):
    line_charlist = []
    list_inor = []
    list_inand = []
    if sep_main in line:
        line = line.replace('\n','')
        if sep_linefeed in line:
            line = line.replace(sep_linefeed,'\n')
    if sep_inor in line:
        list_inor = line.split(sep_main)[0].split(sep_inor)
        ##list_inor.pop()
        print(x for x in list_inor)
        
    line_charlist = list(line)



def make_readable(inp):
    ast = inp.lower()
    
    if ',' in ast:
        ast = ast.replace(',','')\
    
    if '\n' in ast:
        ast = ast.replace('\n',' ')
        
    #if '\'s' in ast:
    #    ast = ast.replace('\'s',' is')
        
    if ' u ' in ast:
        ast = ast.replace(' u ',' you ')
    
    if ' r ' in ast:
        ast = ast.replace(' r ',' are ')
    
    if 'pls' in ast:
        ast = ast.replace('pls','please')
        
    if 'thnx' in ast:
        ast = ast.replace('thnx','thanks')
        
    if 'thx' in ast:
        ast = ast.replace('thx','thanks')
    
    if ' ur ' in ast:
        ast = ast.replace(' ur ',' your ')
    
    if '?' in ast:
        ast = ast.replace('?','')
    
    if 'ok' in ast:
        ast = ast.replace('ok','okay')
    
    if 'oke' in ast:
        ast = ast.replace('oke','okay')
    
    if 'oky' in ast:
        ast = ast.replace('oky','okay')
    
    if 'okey' in ast:
        ast = ast.replace('okey','okay')
    
    if '$' in ast:
        ast = ast.replace('$','DOLLAR')
    
    return ast

def read(b, path):
    inputt = []
    outputt = []
    
    with open(path,'r') as file:
        lines = file.readlines()
        txt = ''
        
        for x in lines:
            p = split_data(x,'$')
            inputt.append(p[0])
            outputt.append(p[1])
        
    if b == 1:
        return inputt
    else:
        return outputt
   
def bot(*t):
    average_typing_speed = 300
    average_lettres_per_word = 5
    speedfac = (average_lettres_per_word * average_typing_speed / 60) ** (-1)
    
    for x in range(len(t)):
        r = speedfac * len(t[x])
        if r > 10:
            r = 10
        time.sleep(r)
        print('JADE: '+str(t[x]))

def mult(*a):
    r = random.randint(0,len(a)-1)
    return (a[r])

def browse(inp,url):
    bot(inp)
    time.sleep(2)
    webbrowser.open(url)
    
def store(inp,path):
     with open(path,'a') as out_file:
        out_file.write(str(inp) + '\n')

def JADE():
    
    input_count = 0
    path_files = 'lib\\'
    input_match = read(1,path_files + 'lib_match.aiso')
    output_match = read(0,path_files + 'lib_match.aiso')
    input_contain = read(1,path_files + 'lib_contain.aiso')
    output_contain = read(0,path_files + 'lib_contain.aiso')
    
    print('                                                  ')
    print('            _/     _/_/     _/_/_/     _/_/_/_/   ')
    print('           _/   _/    _/   _/    _/   _/          ')
    print('          _/   _/_/_/_/   _/    _/   _/_/_/       ')
    print('   _/    _/   _/    _/   _/    _/   _/            ')
    print('    _/_/     _/    _/   _/_/_/     _/_/_/_/       ')
    print('                                                  ')
    print('\nYou are now chatting with Jaded Artificial Discussion Emulator, or JADE.')
    print('')
    print('Type \'quit\' to abort the session.\n')
    
    
    while True:
        inp = str(input('User: '))
        i = make_readable(inp)
        
        store(inp,path_files + 'lib_history.aiso')
        input_count += 1
        
        #print(input_contain,input_match)
        
        if i == 'quit':
            bot(mult('I hope to see you soon.','Goodbye.'))
            break
        elif not any(x in i for x in 'abcdefghijklmnopqrstuvwxyz:;)!?@\\#\'"'):
            bot(mult('Why didn\'t you say anything?','Try and actually say something?'))
        elif 'python' in i:
            bot(i)
        elif i in input_match:
            bot(output_match[input_match.index(i)])
        elif any(x in i for x in input_contain):
            for x in input_contain:
                if x in i:
                    bot(output_contain[input_contain.index(x)])
        else:
            bot(mult('I don\'t understand.','I''m sorry, your previous message is beyond my comprehension.','I didn\'t really catch that, I\'m afraid.','Could you try rephrasing that, please?'))
       
    print('\nEnd of session.\nInput count = {}'.format(input_count))
    #browse('I\'ll open facebook for ya :)','http://facebook.com')

JADE()



