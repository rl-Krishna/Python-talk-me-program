import os
while True :
  print("Enter your choice of program which need to be opened:" , end ='')
  y = input()
  x = y.lower()
  if (('run' in x) or ('open' in x) or ('execute' in x))  and (('notepad' in x) or ('editor' in x) or ('text' in x))  :
    os.system('notepad')
  elif (('run' in x) or ('open' in x) or ('execute' in x))  and (('calculator' in x) or ('calc' in x) or ('cal' in x))  :
    os.system('calc')
  elif (('run' in x) or ('open' in x) or ('execute' in x))  and (('chrome' in x) or ('browser' in x) or ('webapp' in x))  :
    os.system('chrome')
  elif (('run' in x) or ('open' in x) or ('execute' in x))  and (('windows media player' in x) or ('media player' in x) or ('wmplayer' in x) or ('player' in x))  :
    os.system('wmplayer')
  elif 'break' in x:
    break
  else:
    print('The program you asked is not availabe. As of now we support only notepad, calculator, browser, media player')
  

 