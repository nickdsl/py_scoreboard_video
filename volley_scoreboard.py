import pdb
#import unicode
#import sys
#import os
#корректные ответы
VALID_ANSWERS = ['A', 'B', 'Y', 'N', 'D', '?']
#рабочий каталог
WORKING_DIR=".\\"
#рабочие файлы
#имя первой команды
F_TEAM_A_NAME='TeamA_name.txt'
#имя второй команды
F_TEAM_B_NAME='TeamB_name.txt'
#количество выигранных партий первой команды
F_TEAM_A_SETS_WON='TeamA_sets_won.txt'
#количество выигранных партий второй команды
F_TEAM_B_SETS_WON='TeamB_sets_won.txt'
#количество набранных очков в текущей партии первой команды
F_TEAM_A_SET_POINTS='TeamA_set_points.txt'
#количество набранных очков в текущей партии второй команды
F_TEAM_B_SET_POINTS='TeamB_set_points.txt'
#знак подачи на экране
F_TEAM_A_SERVE='TeamA_serve.txt'
#знак подачи на экране
F_TEAM_B_SERVE='TeamB_serve.txt'
#итоги матча
F_MATCH_RESULTS='MatchResults.txt'

#переменные для хранения данных о командах
#словарь хранения данных о матче
MATCH_DATA={}
#по ключу доступен словарь с данными о команде А
MATCH_DATA['A']={}
#аналогично по команде B
MATCH_DATA['B']={}
#имя команды А
MATCH_DATA['A']['name']=''
#имя команды B
MATCH_DATA['B']['name']=''
#партии команды А
MATCH_DATA['A']['sets']=0
#партии команды B
MATCH_DATA['B']['sets']=0
#очки команды A
MATCH_DATA['A']['points']=0
#очки команды B
MATCH_DATA['B']['points']=0
#знак подачи команды A
MATCH_DATA['A']['serve']=''
#знак подачи команды B
MATCH_DATA['B']['serve']=''
#значок подачи который отображается на табло как знак чья подача была/будет при розыгрыше
SERVE_SIGN='●'
#флаг подает ли это команда А (в течение сета)
A_SERVE = True
#флаг - начинала ли подавать команда А в начале сета
A_FIRST_SERVE = True
#максимальное количество очков в партии (по умолчанию)
MAX_SET_POINTS=25
LAST_SET_MAX_POINTS=15
#если 3 - до 2х побед (из трех партий)
#иначе из 5 - до 3х побед (из пяти партий)
MAX_SET=5
#счетчик сетов
CURRENT_SET=1
#условние победы в партии
SET_WIN_CONDITION=2
#условие победы в матче
MATCH_WIN_CONDITION=3
#флаг конца игры
END_GAME = False
#флаг конца сета
END_SET = False

#записать что либо в указанный файл
def write_and_save(target_filename, target_value):
  fp = open(target_filename, 'w')
  fp.write(target_value)
  fp.close()
def flush_results():
  fp = open(WORKING_DIR + "\\" + F_MATCH_RESULTS, 'wb')
  fp.write("".encode('utf-8'))
  fp.close()
def write_results():
  fp = open(WORKING_DIR + "\\" + F_MATCH_RESULTS, 'ab')
  fp.write("{}:{}\n".format(MATCH_DATA['A']['points'], MATCH_DATA['B']['points']).encode('utf-8'))
  fp.close()
def write_names():
  fp = open(WORKING_DIR + "\\" + F_TEAM_A_NAME, 'wb')
  fp.write(str(MATCH_DATA['A']['name']).encode('utf-8'))
  fp.close()
  fp = open(WORKING_DIR + "\\" + F_TEAM_B_NAME, 'wb')
  fp.write(str(MATCH_DATA['B']['name']).encode('utf-8'))
  fp.close()
def write_sets():
  fp = open(WORKING_DIR + "\\" + F_TEAM_A_SETS_WON, 'wb')
  fp.write(str(MATCH_DATA['A']['sets']).encode('utf-8'))
  fp.close()
  fp = open(WORKING_DIR + "\\" + F_TEAM_B_SETS_WON, 'wb')
  fp.write(str(MATCH_DATA['B']['sets']).encode('utf-8'))
  fp.close()
def write_points():
  fp = open(WORKING_DIR + "\\" + F_TEAM_A_SET_POINTS, 'wb')
  value = MATCH_DATA['A']['points']
  if value < 10:
    value = " {}".format(MATCH_DATA['A']['points']).encode('utf-8')
  else:
    value = str(value).encode('utf-8')
  fp.write(value)
  fp.close()
  fp = open(WORKING_DIR + "\\" + F_TEAM_B_SET_POINTS, 'wb')
  value = MATCH_DATA['B']['points']
  if value < 10:
    value = " {}".format(MATCH_DATA['B']['points']).encode('utf-8')
  else:
    value = str(value).encode('utf-8')
  fp.write(value)
  fp.close()
def write_serve():
  fp = open(WORKING_DIR + "\\" + F_TEAM_A_SERVE, 'wb')
  fp.write(str(MATCH_DATA['A']['serve']).encode('utf-8'))
  fp.close()
  fp = open(WORKING_DIR + "\\" + F_TEAM_B_SERVE, 'wb')
  fp.write(str(MATCH_DATA['B']['serve']).encode('utf-8'))
  fp.close()

def intro():
  global MATCH_DATA
  global A_SERVE
  global A_FIRST_SERVE
  global MAX_SET
  global MATCH_WIN_CONDITION
  value = input("Enter team A name:")
  MATCH_DATA['A']['name'] = value
  value = input("Enter team B name:")
  MATCH_DATA['B']['name'] = value
  value = input("Type Y/y if team {} will serve first, else type N/n if team {} will serve:".format(
    MATCH_DATA['A']['name'],
    MATCH_DATA['B']['name']))
  if (value == 'Y') or (value == 'y'):
    MATCH_DATA['A']['serve'] = SERVE_SIGN
    MATCH_DATA['B']['serve'] = ''
    print("Team {} will serve the ball".format(MATCH_DATA['A']['name']))
  else:
    MATCH_DATA['B']['serve'] = SERVE_SIGN
    MATCH_DATA['A']['serve'] = ''
    A_FIRST_SERVE = False
    A_SERVE = A_FIRST_SERVE
    print("Team {} will serve the ball".format(MATCH_DATA['B']['name']))
  value = input("Type Y/y for long game (5 sets) or N/n for short game (3 sets):")
  if (value == 'Y') or (value == 'y'):
    MAX_SET = 5
    MATCH_WIN_CONDITION = 3
  else:
    MAX_SET = 3
    MATCH_WIN_CONDITION = 2
  print("Match with {} sets chosen".format(MAX_SET))
  #pdb.set_trace()
  #quit()
#ввод начальных значений
intro()
#запись всех данных что были введены на интро в файлы (чтобы изменения ушли в OBS)
write_names()
write_sets()
write_points()
write_serve()
flush_results()
#основной цикл игры. играем пока не закончится игра =)
while not END_GAME:
  #если мы тут, то игра либо только началась, либо начинается очередной сет
  END_SET = False
  #если это не первый сет, то нужно менять первую подачу (метка)
  if CURRENT_SET != 1:
    #перед сетом проверим последний ли он
    if CURRENT_SET == MAX_SET:
      #если да, то переопределяем количество мячей по-умолчанию для победы
      MAX_SET_POINTS = LAST_SET_MAX_POINTS
      #и тут должна быть вторая процедура розыгрыша подачи по правилам волейбола
      value = input("If team {} won the toss press A/a, else press B/b (or any key) for team {}:".format(
        MATCH_DATA['A']['name'],
        MATCH_DATA['B']['name']))
      if (value.upper() == "A") or (value.upper() == "a"):
        #нужно назначить право первой подачи на команду А
        #далее по алгоритму идет процедура инверсии первой подачи.
        #следовательно если мы хотим чтобы подавала команда А, то мы должны установить флаг False 
        #т.к. он инвертируется и получится True
        #возможно это костыли, но уже лень писать строки кода
        A_FIRST_SERVE = False
    A_FIRST_SERVE = not A_FIRST_SERVE
    if A_FIRST_SERVE:
      MATCH_DATA['A']['serve'] = SERVE_SIGN
      MATCH_DATA['B']['serve'] = ''
    else:
      MATCH_DATA['B']['serve'] = SERVE_SIGN
      MATCH_DATA['A']['serve'] = ''
    A_SERVE = A_FIRST_SERVE
    write_serve()
  #пока не закончится сет выполнять цикл
  while not END_SET:
    #базовая обработка ввода
    VALID_INPUT = False
    while not VALID_INPUT:
      value = input("Who scored? If {} then press A/a, else B/b for {}. Type ? for more options".format(
        MATCH_DATA['A']['name'],
        MATCH_DATA['B']['name']))
      if value.upper() in VALID_ANSWERS:
        VALID_INPUT = True
      #case - A - point to team A
      #case - B - point to team B
      #case - D - double fault
      #case - ? - all options / help
    if (value.upper() == '?'):
      print('Valid options:')
      print("A - team {} scored".format(MATCH_DATA['A']['name']))
      print("B - team {} scored".format(MATCH_DATA['B']['name']))
      print("D - double fault. No score. Team have to serve again.")
      print("Y - yes")
      print("N - no")
      print("? - show valid options")
      continue
    if (value.upper() == 'D'):
      print("Double fault")
      continue
    # проверка введенного значения и набор очка одной из команд
    if (value.upper() == 'A'):
      MATCH_DATA['A']['points'] = MATCH_DATA['A']['points'] + 1
      if not A_SERVE:
        A_SERVE = True
        MATCH_DATA['A']['serve'] = SERVE_SIGN
        MATCH_DATA['B']['serve'] = ''
        write_serve()
    if (value.upper() == 'B'):
      MATCH_DATA['B']['points'] = MATCH_DATA['B']['points'] + 1
      if A_SERVE:
        A_SERVE = False
        MATCH_DATA['B']['serve'] = SERVE_SIGN
        MATCH_DATA['A']['serve'] = ''
        write_serve()
    #зафиксируем изменения на экране
    write_points()
    # проверка условия победы в сете/матче
    if (MATCH_DATA['A']['points'] >= MAX_SET_POINTS) and ((MATCH_DATA['A']['points'] - MATCH_DATA['B']['points']) >= SET_WIN_CONDITION):
      #мы достигли условия победы команды А в сете
      MATCH_DATA['A']['sets'] = MATCH_DATA['A']['sets'] + 1
      END_SET = True
    else:
      #иначе или команда А имеет недостаточное для победы количество очков, или же команда А вообще имеет очков меньше чем команда В
      if (MATCH_DATA['B']['points'] >= MAX_SET_POINTS) and ((MATCH_DATA['B']['points'] - MATCH_DATA['A']['points']) >= SET_WIN_CONDITION):
        #мы достигли условия победы команды B в сете
        MATCH_DATA['B']['sets'] = MATCH_DATA['B']['sets'] + 1
        END_SET = True
    if END_SET:
      #запишем изменения в сетах
      write_sets()
      write_results()
      if (CURRENT_SET == MAX_SET) or ((MATCH_DATA['A']['sets'] == MATCH_WIN_CONDITION) or (MATCH_DATA['B']['sets'] == MATCH_WIN_CONDITION)):
        #игра окончена. нужно выходить из всех циклов
        END_GAME = True
      else:
        #игра не окончена. нужно сделать паузу
        #увеличить счетчик сетов
        #обнулить значения очков в сете и начать новый сет
        write_points()
        value = input("Set is over. Press ENTER to continue")
        CURRENT_SET = CURRENT_SET + 1
        MATCH_DATA['A']['points'] = 0
        MATCH_DATA['B']['points'] = 0
        write_points()
value = input("Match is over. Press ENTER to exit")