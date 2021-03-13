import pdb
#import unicode
#import sys
#import os
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
F_TEAM_A_PITCH='TeamA_pitch.txt'
#знак подачи на экране
F_TEAM_B_PITCH='TeamB_pitch.txt'
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
MATCH_DATA['A']['pitch']=''
#знак подачи команды B
MATCH_DATA['B']['pitch']=''
#значок подачи который отображается на табло как знак чья подача была/будет при розыгрыше
PITCH_SIGN='●'
#флаг подает ли это команда А (в течение сета)
A_PITCH = True
#флаг - начинала ли подавать команда А в начале сета
A_FIRST_PITCH = True
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
  fp.write("{}:{}\n".format(MATCH_DATA['A']['points'],MATCH_DATA['B']['points']).encode('utf-8'))
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
def write_pitch():
  fp = open(WORKING_DIR + "\\" + F_TEAM_A_PITCH, 'wb')
  fp.write(str(MATCH_DATA['A']['pitch']).encode('utf-8'))
  fp.close()
  fp = open(WORKING_DIR + "\\" + F_TEAM_B_PITCH, 'wb')
  fp.write(str(MATCH_DATA['B']['pitch']).encode('utf-8'))
  fp.close()

def intro():
  global MATCH_DATA
  global A_PITCH
  global A_FIRST_PITCH
  global MAX_SET
  global MATCH_WIN_CONDITION
  value = input("Введите имя первой команды:")
  MATCH_DATA['A']['name'] = value
  value = input("Введите имя второй команды:")
  MATCH_DATA['B']['name'] = value
  value = input("Подача у первой команды? (Yy/Nn)")
  if (value == 'Y') or (value == 'y'):
    MATCH_DATA['A']['pitch'] = PITCH_SIGN
    MATCH_DATA['B']['pitch'] = ''
  else:
    MATCH_DATA['B']['pitch'] = PITCH_SIGN
    MATCH_DATA['A']['pitch'] = ''
    A_FIRST_PITCH = False
    A_PITCH = A_FIRST_PITCH
  value = input("Стандартная игра (до 3х побед из 5 партий)? (Yy/Nn)")
  if (value == 'Y') or (value == 'y'):
    MAX_SET = 5
    MATCH_WIN_CONDITION = 3
  else:
    MAX_SET = 3
    MATCH_WIN_CONDITION = 2
  #pdb.set_trace()
  #quit()
#ввод начальных значений
intro()
#запись всех данных что были введены на интро в файлы (чтобы изменения ушли в OBS)
write_names()
write_sets()
write_points()
write_pitch()
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
      value = input("Какая команда выиграла право подачи? {} - нажмите А или а".format(MATCH_DATA['A']['name']))
      if (value == "A") or (value == "a"):
        #нужно назначить право первой подачи на команду А
        #далее по алгоритму идет процедура инверсии первой подачи.
        #следовательно если мы хотим чтобы подавала команда А, то мы должны установить флаг False 
        #т.к. он инвертируется и получится True
        #возможно это костыли, но уже лень писать строки кода
        A_FIRST_PITCH = False
    A_FIRST_PITCH = not A_FIRST_PITCH
    if A_FIRST_PITCH:
      MATCH_DATA['A']['pitch'] = PITCH_SIGN
      MATCH_DATA['B']['pitch'] = ''
    else:
      MATCH_DATA['B']['pitch'] = PITCH_SIGN
      MATCH_DATA['A']['pitch'] = ''
    A_PITCH = A_FIRST_PITCH
    write_pitch()
  #пока не закончится сет выполнять цикл
  while not END_SET:
    value = input("Кто выиграл розыгрыш? Если {} то нажать A или a, иначе выиграла команда {} и нужно нажать B или b".format(MATCH_DATA['A']['name'],MATCH_DATA['B']['name']))
    # проверка введенного значения и набор очка одной из команд
    if (value == 'A') or (value == 'a'):
      MATCH_DATA['A']['points'] = MATCH_DATA['A']['points'] + 1
      if not A_PITCH:
        A_PITCH = True
        MATCH_DATA['A']['pitch'] = PITCH_SIGN
        MATCH_DATA['B']['pitch'] = ''
        write_pitch()
    else:
      MATCH_DATA['B']['points'] = MATCH_DATA['B']['points'] + 1
      if A_PITCH:
        A_PITCH = False
        MATCH_DATA['B']['pitch'] = PITCH_SIGN
        MATCH_DATA['A']['pitch'] = ''
        write_pitch()
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
      if (CURRENT_SET == MAX_SET) or ((MATCH_DATA['A']['sets'] == MATCH_WIN_CONDITION) or (MATCH_DATA['A']['sets'] == MATCH_WIN_CONDITION)):
        #игра окончена. нужно выходить из всех циклов
        END_GAME = True
      else:
        #игра не окончена. нужно сделать паузу
        #увеличить счетчик сетов
        #обнулить значения очков в сете и начать новый сет
        write_points()
        value = input("Партия закончена. Чтобы перейти к следующей нажмите ВВОД")
        CURRENT_SET = CURRENT_SET + 1
        MATCH_DATA['A']['points'] = 0
        MATCH_DATA['B']['points'] = 0
        write_points()
value = input("Игра окончена. Для выхода нажмите ВВОД")