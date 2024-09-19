# Rammos Thomas         


import sys, os

numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# commited words
commited_words = ['program', 'declare', 'if', 'else', 'while', 'case', 'forcase', 'incase', 'switchcase', 'default',
                  'return', 'and', 'or', 'not', 'call', 'in', 'inout', 'input', 'function', 'procedure', 'print']

global relOps
relOps = {"=" :"beq","<>":"bne",">" :"bgt","<":"blt",">=":"bge","<=":"ble"}
global operators
operators = {"+":"add","-":"sub","*" :"mul","/":"div"}
global checkForPar
checkForPar=True
asmFile = open("test.asm", "w")
# open file
file =  open(sys.argv[1], "r")

# statements
start_state = 0
digit_state = 1
idk_state = 2
assigment_state = 3
smaller_state = 4
larger_state = 5
rem_state = 6

# names for transfer board
empty_char = 0
num = 1
characters = 2
sub = 3
adder = 4
div = 5
mul = 6
left_bracket = 7
right_bracket = 8
left_parenthesis = 9
right_parenthesis = 10
open_block = 11
close_block = 12
comma = 13
question_mark = 14
colon = 15
equal = 16
greater_than = 17
less_than = 18
hashtag = 19
EOF = 20
new_line = 21
dot = 22
invalid_symbol = 23

# tokens
digtk = 200
idtk = 201
subtk = 202
addertk = 203
divtk = 204
multk = 205
left_brackettk = 206
right_brackettk = 207
left_parenthesistk = 208
right_parenthesistk = 209
open_blocktk = 210
close_blocktk = 211
commatk = 212
question_marktk = 213
equaltk = 214
not_equaltk = 215
greaterthantk = 216
lessthantk = 217
greater_or_equaltk = 218
less_or_equaltk = 219
EOFtk = 220
assigmenttk = 221
dottk = 222

programtk = 300
declaretk = 301
iftk = 302
elsetk = 303
whiletk = 304
casetk = 305
forcasetk = 306
incasetk = 307
switchcasetk = 308
defaulttk = 309
returntk = 310
andtk = 311
ortk = 312
nottk = 313
calltk = 314
intk = 315
inouttk = 316
inputtk = 317
functiontk = 318
proceduretk = 319
printtk = 320

# errors
ERROR_NUMBER_OUT_OF_RANGE = -10
ERROR_IDK = -20
ERROR_MORE_THAN_30_CHARACTERS = -30
ERROR_INVALID_SYMBOL = -40
ERROR_OPEN_HASTAG_WITH_EOF = -50
ERROR_COLON = -60

transfer_board = [
    # start_state
    [start_state, digit_state, idk_state, subtk, addertk, divtk, multk, left_brackettk, right_brackettk,
     left_parenthesistk, right_parenthesistk, open_blocktk, close_blocktk, commatk, question_marktk,
     assigment_state, equaltk, larger_state, smaller_state, rem_state, EOFtk, start_state, dottk, ERROR_INVALID_SYMBOL],

    # digit_state
    [digtk, digit_state, ERROR_IDK, digtk, digtk, digtk,
     digtk, digtk, digtk, digtk, digtk, digtk, digtk, digtk,
     digtk, digtk, digtk, digtk, digtk, digtk, digtk, digtk, digtk, ERROR_INVALID_SYMBOL],

    # idk_state
    [idtk, idk_state, idk_state, idtk, idtk, idtk, idtk, idtk, idtk, idtk, idtk,
     idtk, idtk, idtk, idtk, idtk, idtk, idtk, idtk, idtk, idtk, idtk, idtk, ERROR_INVALID_SYMBOL],

    # assigment_state
    [ERROR_COLON, ERROR_COLON, ERROR_COLON, ERROR_COLON, ERROR_COLON, ERROR_COLON,
     ERROR_COLON, ERROR_COLON, ERROR_COLON, ERROR_COLON, ERROR_COLON, ERROR_COLON,
     ERROR_COLON, ERROR_COLON, ERROR_COLON, ERROR_COLON, assigmenttk, ERROR_COLON,
     ERROR_COLON, ERROR_COLON, ERROR_COLON, ERROR_COLON, ERROR_COLON, ERROR_INVALID_SYMBOL],

    # smaller_state
    [lessthantk, lessthantk, lessthantk, lessthantk, lessthantk, lessthantk,
     lessthantk, lessthantk, lessthantk, lessthantk, lessthantk, lessthantk,
     lessthantk, lessthantk, lessthantk, lessthantk, less_or_equaltk,
     not_equaltk, lessthantk, lessthantk, lessthantk, lessthantk, lessthantk, ERROR_INVALID_SYMBOL],

    # larger_state
    [greaterthantk, greaterthantk, greaterthantk, greaterthantk, greaterthantk, greaterthantk,
     greaterthantk, greaterthantk, greaterthantk, greaterthantk, greaterthantk, greaterthantk,
     greaterthantk, greaterthantk, greaterthantk, greaterthantk, greater_or_equaltk, greaterthantk,
     greaterthantk, greaterthantk, greaterthantk, greaterthantk, greaterthantk, ERROR_INVALID_SYMBOL],

    # rem_state
    [rem_state, rem_state, rem_state, rem_state, rem_state, rem_state, rem_state, rem_state, rem_state,
     rem_state, rem_state, rem_state, rem_state, rem_state, rem_state, rem_state, rem_state, rem_state,
     rem_state, start_state, rem_state, rem_state, rem_state, ERROR_OPEN_HASTAG_WITH_EOF]
]
line = 1


def lex():
    my_state = start_state
    word = ''
    global line
    counter_line = line
    res = []
    char = ''
    while (my_state <= 6 and my_state >= 0):
        char = file.read(1)
        if (char == ' ' or char == '\t'):
            chartk = empty_char
        elif (char in numerals):
            chartk = num
        elif (char in alphabet):
            chartk = characters
        elif (char == '-'):
            chartk = sub
        elif (char == '+'):
            chartk = adder
        elif (char == '/'):
            chartk = div
        elif (char == '*'):
            chartk = mul
        elif (char == '['):
            chartk = left_bracket
        elif (char == ']'):
            chartk = right_bracket
        elif (char == '('):
            chartk = left_parenthesis
        elif (char == ')'):
            chartk = right_parenthesis
        elif (char == '{'):
            chartk = open_block
        elif (char == '}'):
            chartk = close_block
        elif (char == ','):
            chartk = comma
        elif (char == ';'):
            chartk = question_mark
        elif (char == ':'):
            chartk = colon
        elif (char == '='):
            chartk = equal
        elif (char == '>'):
            chartk = greater_than
        elif (char == '<'):
            chartk = less_than
        elif (char == ''):
            chartk = EOF
        elif (char == '.'):
            chartk = dot
        elif (char == '#'):
            chartk = hashtag
        elif (char == '\n'):
            counter_line = counter_line + 1
            chartk = new_line
        else:
            chartk = invalid_symbol

        my_state = transfer_board[my_state][chartk]
        if (len(word) < 30):
            if (my_state != start_state and my_state != rem_state):
                word += char
        else:
            my_state = ERROR_MORE_THAN_30_CHARACTERS

    # i have found token
    if (my_state == digtk or my_state == idtk or my_state == greaterthantk or my_state == lessthantk):
        if (char == '\n'):
            counter_line -= 1
        char = file.seek(file.tell() - 1, 0)  # epistrefei to teleutaio char pou diabase sto File (px avd+)
        word = word[:-1]  # kovei to +

    # limit number of digits and range of numbers 
    if (my_state == digtk):
        if (word.isdigit() >= pow(2, 32)):
            my_state = ERROR_NUMBER_OUT_OF_RANGE

    if (my_state == idtk):
        if (word in commited_words):
            if (word == 'program'):
                my_state = programtk
            elif (word == 'declare'):
                my_state = declaretk
            elif (word == 'if'):
                my_state = iftk
            elif (word == 'else'):
                my_state = elsetk
            elif (word == 'while'):
                my_state = whiletk
            elif (word == 'case'):
                my_state = casetk
            elif (word == 'forcase'):
                my_state = forcasetk
            elif (word == 'incase'):
                my_state = incasetk
            elif (word == 'switchcase'):
                my_state = switchcasetk
            elif (word == 'default'):
                my_state = defaulttk
            elif (word == 'return'):
                my_state = returntk
            elif (word == 'and'):
                my_state = andtk
            elif (word == 'or'):
                my_state = ortk
            elif (word == 'not'):
                my_state = nottk
            elif (word == 'call'):
                my_state = calltk
            elif (word == 'in'):
                my_state = intk
            elif (word == 'inout'):
                my_state = inouttk
            elif (word == 'input'):
                my_state = inputtk
            elif (word == 'function'):
                my_state = functiontk
            elif (word == 'procedure'):
                my_state = proceduretk
            elif (word == 'print'):
                my_state = printtk

    # erorrs
    if (my_state == ERROR_NUMBER_OUT_OF_RANGE):
        print("ERROR MESSAGE: Number out of range!")
    elif (my_state == ERROR_IDK):
        print("ERROR MESSAGE: It has letter after digit!")
    elif (my_state == ERROR_MORE_THAN_30_CHARACTERS):
        print("ERROR MESSAGE: The word is more than 30 characters!")
    elif (my_state == ERROR_INVALID_SYMBOL):
        print("ERROR MESSAGE: We have invalid symbol!")
    elif (my_state == ERROR_OPEN_HASTAG_WITH_EOF):
        print("ERROR MESSAGE: Missing hastag at the end of line!")
    elif (my_state == ERROR_COLON):
        print("ERROR MESSAGE: Colon without equal symbol!")

    line = counter_line
    res.append(word)
    res.append(my_state)
    res.append(counter_line)
    return res


# Endiamesos kodikas
QuadsList = []  # lista me Oles tis tetrades pou tha paraxthoun apo to programma.
quadList = []   # gia teliko kwdika
global FileC  
QuadsCounter = 1  # O arithmos pou xarakthrizei thn tetrada. Brisketai mprosta apo thn 4ada.


def nextQuad():             # returns the next quad
    global QuadsCounter
    return QuadsCounter


def genQuad(first, second, third, fourth): # create a quad in a list
    global QuadsCounter
   

    tempList = []
    #tempList.append([nextQuad(), first , second, third, fourth])
    QuadsList.append([nextQuad(), first , second, third, fourth])
    quadList.append([nextQuad(), first , second, third, fourth])
    # Bazw prwta ton arithmo. Epeita ta orismata

    QuadsCounter += 1  # Ayksanw kata 1 ton arithmo ths epomenhs 4adas.
    return [nextQuad(), first , second, third, fourth]


T_i = 1
VarTempList = []


def newTemp():          # crate new temporary variable
    global T_i, VarTempList
    
    Var_temp =  'T_' + str(T_i)
    T_i += 1
    # Save them in VarTempList
    VarTempList += [Var_temp]

    # create Entity for Temporary Variable
    T = TemporaryVariable()
    T.name = Var_temp
    T.type = "TEMP"
    T.dataType = 'Int'
    T.offset = compute_offset()
    add_entity(T)

    return Var_temp


def emptyList():  # return an empty list
    return []


def makeList(label): # make a lista with this label
    return [label]


def merge(list1, list2): # concatenate two lists
    return list1 + list2


def backPatch(list, z): 
   
    global QuadsList

    for i in range(len(list)):                    # gia kathe item ths list  
        for j in range(len(QuadsList)): # gia kathe quad ths quadlist
            # Briskoume tetrada me sygkekrimeno label kai sto telos tou pername thn parametro z
            if (list[i] == QuadsList[j][0]): # mporei kai na paralhftei
                QuadsList[j][4] = z
                break  
    
    for i in range(len(list)):                    # gia kathe item ths list  
        for j in range(len(quadList)): # gia kathe quad ths quadlist
            # Briskoume tetrada me sygkekrimeno label kai sto telos tou pername thn parametro z
            if (list[i] == quadList[j][0]): # mporei kai na paralhftei
                quadList[j][4] = z
                break
    return


###############################################################################
#	Synarthseis PINAKA SYMBOLWN:											  #
###############################################################################	
class Entity():
    def __init__(self):
        self.name = ''
        self.type = ''  # 'VAR' or 'FUNC' or 'PARAM' or 'TEMP' or 'PROC'


class FormalParameter(Entity):  # Arguments
    def __init__(self):
        super().__init__()
        self.dataType = 'Int'
        self.mode = ''  # eite 'cv' eite 'ref'


class Variable(Entity):

    def __init__(self):
        super().__init__()
        self.datatype = 'Int'
        self.offset = 0


class Procedure(Entity):
    def __init__(self):
        super().__init__()
        self.startingQuad = 0
        self.frameLength = 0
        self.argumentList = []  # h lista parametrwn


class Function(Procedure):
    def __init__(self):
        super().__init__()  # 'Procedure' h' 'Function' .
        self.dataype = ''


class Parameter(Variable, FormalParameter):
    def __init__(self):
        Variable().__init__()
        FormalParameter().mode = ''  # 'CV', 'REF'


class TemporaryVariable(Entity):
    def __init__(self):
        super().__init__()
        self.datatype = 'Int'
        self.offset = 0


class Scope():
    def __init__(self):
        self.entityList = []  # h lista apo entities
        self.level = 0  # Bathos fwliasmatos


class Table():
    def __init__(self):
        self.scopes = []


def add_argument(object):  # SubProg : flag gia na xerw an eimai se function h procedure
    'Add given object to list'
    global table

    # Tha pame sto teleutaio entity(pou tha einai procedure h function) kai ekei sto pedio
    # argumentList tha kanoume append to object

    table.scopes[-1].entityList[-1].argumentList.append(object)

def add_entity(object):  # ftiaxnw entity
    'Add given object to list'
    global table

    table.scopes[-1].entityList.append(object)  # bazei sto telos ths listas apo entities to kainourgio entity pou dhmiourghthhke


def add_scope(name):  # ftiaxnw kyklo
    global table

    if not len(table.scopes):
        scopeZero = Scope()  # otan prosthetoume prwth fora scope
        table.scopes.append(scopeZero)
    else:
        nextLevelScope = Scope()
        nextLevelScope.level = (table.scopes[-1].level) + 1  # to epomeno scope +1 level se sxesh me to prohgoumeno
        table.scopes.append(nextLevelScope)  # to prosthetoume sth lista


def compute_offset():
    global table

    counter = 0  # mono gia entites me 'VAR' or 'PARAM' or 'TEMP'

    if len(table.scopes[-1].entityList) > 0:
        for i in range(len(table.scopes[-1].entityList)):
            if (table.scopes[-1].entityList[i].type == "VAR" or table.scopes[-1].entityList[i].type == "TEMP" or table.scopes[-1].entityList[i].type == "PARAM"):
                counter += 1

    offset = 12 + (counter * 4)
    return offset

def add_parameters():  # kaleite stin "block" amesos meta tin "add_scope" kai metatrepei ta orismata tou apo katw epipedou se entitties sto top Scope

    # proteleuataio scope (katw tou top scope)
    for arg in range(len(table.scopes[-2].entityList[-1].argumentList)):
        E = Parameter()
        E.name = table.scopes[-2].entityList[-1].argumentList[arg].name
        E.type = "PARAM"
        E.dataType = "Int"
        E.mode = table.scopes[-2].entityList[-1].argumentList[arg].mode
        E.offset = compute_offset()
        add_entity(E)


def extract_symbolic_table():
    global table

    # anoigma arxeiou gia grapsimo sto telos kathe fora pou to anoigoume
    f = open("test.symb", "a")

    for i in range(len(table.scopes)):
        f.write("SCOPE: " + str(table.scopes[i].level) + "\n")
        f.write("\tENTITIES:" + "\n")
        counter_Entities = 0
        for ent in table.scopes[i].entityList:
            if (ent.type == 'VAR'):
                counter_Entities += 1
                f.write("\tENTITY{" + str(
                    counter_Entities) + "}: " + " NAME:" + ent.name + "\t TYPE:" + ent.type + "\t VARIABLE-TYPE:" + ent.dataType + "\t OFFSET:" + str(
                    ent.offset) + "\n")
            elif (ent.type == 'TEMP'):
                counter_Entities += 1
                f.write("\tENTITY{" + str(
                    counter_Entities) + "}: " + " NAME:" + ent.name + "\t TYPE:" + ent.type + "\t Temporary VARIABLE-TYPE:" + ent.dataType + "\t OFFSET:" + str(
                    ent.offset) + "\n")
            elif (ent.type == 'PAR'):
                counter_Entities += 1
                f.write("\tENTITY{" + str(
                    counter_Entities) + "}: " + " NAME:" + ent.name + "\t TYPE:" + ent.type + "\t PARAMETER-TYPE:" + ent.dataType + "\t MODE:" + ent.mode + "\t OFFSET:" + str(
                    ent.offset) + "\n")
            elif (ent.type == "FUNC"):
                counter_Entities += 1
                f.write("\tENTITY{" + str(
                    counter_Entities) + "}: " + " NAME:" + ent.name + "\t TYPE:" + ent.type + "\t STARTING QUAD:" + str(
                    ent.startingQuad) + "\t FRAME LENGTH:" + str(
                    ent.frameLength) + "\t RETURN TYPE:" + ent.dataType + "\n")
                f.write("\t\tARGUMENTS:" + "\n")
                counter_Arguments = 0
                for arg in range(len(ent.argumentList)):
                    counter_Arguments += 1
                    f.write(
                        "\t\t\tARGUMENT{"+str(counter_Arguments)+"} : " + " NAME:" + ent.argumentList[arg].name + "\t ARGUMENT TYPE : " + ent.argumentList[arg].dataType + "\t MODE:" + ent.argumentList[arg].mode + "\n")
            elif (ent.type == 'PROC'):
                counter_Entities += 1
                f.write("\tENTITY{" + str(
                    counter_Entities) + "}: " + " NAME:" + ent.name + "\t TYPE:" + ent.type + "\t STARTING QUAD:" + str(
                    ent.startingQuad) + "\t FRAME LENGTH:" + str(ent.frameLength) + "\n")
                f.write("\t\tARGUMENTS :" + "\n")
                counter_Arguments = 0
                for arg in range(len(ent.argumentList)):
                    counter_Arguments += 1
                    f.write(
                        "\t\t\tARGUMENT{"+str(counter_Arguments)+"}: " + " NAME:" + ent.argumentList[arg].name + "\t ARGUMENT TYPE : " + ent.argumentList[arg].dataType + "\t MODE:" + ent.argumentList[arg].mode + "\n")
    f.write(
        "\n\n###############################################################################################################################################\n\n")

    f.close()

def searchEntity(name):
    global table
    scope=table.scopes[-1]
    j = 1
    while table.scopes != []:
        for i in scope.entityList:
            if (i.name==name):
                return scope,i
        j += 1
        if (j > len(table.scopes)):
           break
        scope = table.scopes[-j]
    if name.isdigit():
        return "digit",name
    print(" not found in symbol table : " + str(name)+" Program crashed  \n")
    sys.exit()

table = Table()  # einai to pio PANW scope kathe stigmi

#Synarthseis Telikou kwdika
def gnvlcode(name):
    global table,asmFile
    scope,entity=searchEntity(name)
    asmFile.write("lw t0,-4(sp)\n")
    for i in range(0,(table.scopes[-1].level-scope.level)-1):
        asmFile.write("lw t0,-4(t0)\n")
    entityOffset = entity.offset
    asmFile.write("addi t0,t0,-"+str(entityOffset)+"\n")

def loadvr(v,r):
    global table,asmFile
    scope,entity=searchEntity(v)
    if (scope=="digit"):
        asmFile.write("li t"+str(r)+","+str(v)+"\n")
    elif(entity.type=="VAR"):
        if (scope.level==0):
            asmFile.write("lw t"+str(r)+",-"+str(entity.offset)+"(gp)"+"\n")
        elif(scope.level==table.scopes[-1].level):
            asmFile.write("lw t"+str(r)+",-"+str(entity.offset)+"(sp)"+"\n")
        else :
            gnvlcode(v)
            asmFile.write("lw t"+str(r)+",(t0)"+"\n")
    elif(entity.type=="TEMP"):
        if (scope.level == 0):
            asmFile.write("lw t" + str(r) + ",-" + str(entity.offset) + "(gp)" + "\n")
        elif(scope.level==table.scopes[-1].level):
            asmFile.write("lw t" + str(r) + ",-" + str(entity.offset) + "(sp)" + "\n")
    elif(entity.type=="PAR" and entity.mode=="CV"):
        if (scope.level == table.scopes[-1].level):
            asmFile.write("lw t" + str(r) + ",-" + str(entity.offset) + "(sp)" + "\n")
        elif (scope.lLevel < table.scopes[-1].level):
            gnvlcode(v)
            asmFile.write("lw t" + str(r) + ",(t0)" + "\n")
    elif (entity.type == "PAR" and entity.mode == "REF"):
        if (scope.level == table.scopes[-1].level):
            asmFile.write("lw t0,-"+ str(entity.offset) + "(sp)" + "\n")
            asmFile.write("lw t"+str(r)+",(t0)"+"\n")
        elif (scope.nestingLevel < scopeList[-1].nestingLevel):
            gnvlcode(v)
            asmFile.write("lw t0,(t0)\n")
            asmFile.write("lw t"+str(r)+",(t0)"+"\n")

def storerv(r,v):
    global table, asmFile
    scope, entity = searchEntity(v)
    if(entity.type=="VAR"):
        if (scope.level==0):
            asmFile.write("sw t"+str(r)+",-"+str(entity.offset)+"(gp)"+"\n")
        elif(scope.level==tabel.scopes[-1].level):
            asmFile.write("sw t"+str(r)+",-"+str(entity.offset)+"(sp)"+"\n")
        else :
            gnvlcode(v)
            asmFile.write("sw t"+str(r)+",(t0)"+"\n")
    elif(entity.type=="TEMP"):
        if (scope.level == 0):
            asmFile.write("sw t"+str(r)+",-"+str(entity.offset)+"(gp)"+"\n")
        elif(scope.level==table.scopes[-1].level):
            asmFile.write("sw t"+str(r)+",-"+str(entity.offset)+"(sp)"+"\n")
    elif(entity.type=="PAR" and entity.mode=="CV"):
        if (scope.level == table.scopes[-1].level):
            asmFile.write("sw t" + str(r) + ",-" + str(entity.offset) + "(sp)" + "\n")
        elif (scope.level < table.scopes[-1].level):
            gnvlcode(v)
            asmFile.write("sw t" + str(r) + ",(t0)" + "\n")
    elif (entity.type == "PAR" and entity.mode == "REF"):
        if (scope.level == table.scopes[-1].level):
            asmFile.write("sw t" + str(r) + ",-" + str(entity.offset) + "(sp)" + "\n")
            asmFile.write("sw t"+str(r)+",(t0)"+"\n")
        elif (scope.level < table.scopes[-1].level):
            gnvlcode(v)
            asmFile.write("lw t0,(t0)\n")
            asmFile.write("sw t"+str(r)+",(t0)"+"\n")

def produce():
    global quadList,table,finalCounter,asmFile,checkForPar
    for i in range(len(quadList)-1):
        count = quadList[i][0]
        op = quadList[i][1]
        x = quadList[i][2]
        y = quadList[i][3]
        z = quadList[i][4]
        asmFile.write("L%d: \n" % (count))
        if(op=="jump"):
            asmFile.write("b L"+str(z)+"\n")
        elif (op in relOps):
            loadvr(x,1)
            loadvr(y,2)
            asmFile.write(relOps.get(op) + ",t1,t2, L"+str(z)+"\n")
        elif (op== ":="):
            loadvr(x,1)
            storerv(1,z)
        elif (op in operators):
            loadvr(x, 1)
            loadvr(y, 2)
            asmFile.write(operators.get(op) + ",t1,t1,t2"+"\n")
            storerv(1, z)
        elif(op == "out"):
            loadvr(x, 1)
            asmFile.write("li a0, t1"+"\n")      
            asmFile.write("li a7, 1"+"\n")                        
            asmFile.write("ecall"+"\n")
        elif (op == "inp"):
            asmFile.write("li a7, 5"+"\n")
            asmFile.write("ecall"+"\n")                                # tha topotheththei ston a0 o akeraios pou tha diabastei apo to plhktrologio
            asmFile.write("mv t1, a0"+"\n") 
            storerv(1, x)
        elif (op == "retv"):
            loadvr(x, 1)
            asmFile.write("lw t0,-8(sp)"+ "\n")
            asmFile.write("sw t1,(t0)"+ "\n")
        elif (op == "par"):
            if (checkForPar == True):
                checkForPar=False
                for j in range(i,len(quadList)):
                    if (quadList[j][1] == "call"):
                        FuncOrProcName = str(quadList[j][2])
                        break
                scope,entity=searchEntity(FuncOrProcName)
                asmFile.write("addi fp, sp,"+str(entity.frameLength)+ "\n")
                finalCounter=0
            if (y=="CV"):
                loadvr(x, 0)
                asmFile.write("sw t0,-" + str(12 + 4 * finalCounter) + "(fp)\n")
                finalCounter+=1
            elif (y == "REF"):
                scope,entity=searchEntity(x)
                if (scope.level==table.scopes[-1].level):
                    if (entity.type=="VAR"):
                        asmFile.write("addi t0,sp,-"+str(entity.offset)+"\n")
                        asmFile.write("sw t0,-"+str(12+4*finalCounter)+"(fp)\n")
                    elif (entity.type=="PAR" and entity.mode=="CV"):
                        asmFile.write("addi t0,sp,-"+str(entity.offset)+"\n")
                        asmFile.write("sw t0,-"+str(12+4*finalCounter)+"(fp)\n")
                    elif (entity.type == "PAR" and entity.mode == "REF"):
                        asmFile.write("lw t0,-"+str(entity.offset)+"(sp) \n")
                        asmFile.write("sw t0,-" + str(12 + 4 * finalCounter) + "(fp) \n")
                elif(scope.level<table.scopes[-1].level):
                        gnvlcode(x)
                        if(entity.type == "PAR" and entity.mode == "REF"):
                            asmFile.write("lw t0,(t0)\n")
                            asmFile.write("sw t0,-"+str(12 + 4 * finalCounter)+"(fp)\n")
                        else:
                            asmFile.write("sw t0,-" + str(12 + 4 * finalCounter) + "(fp)\n")
                finalCounter+=1
            elif (y == "RET"):
                scope,entity=searchEntity(x)
                asmFile.write("addi t0,sp,-"+str(entityoffset)+"\n")
                asmFile.write("sw t0,-8(fp)\n")     
        elif (op == "call"):
            checkForPar=True
            scope, entity = searchEntity(x)
            if (scope.level == table.scopes[-1].level):
                asmFile.write("lw t0,-4(sp)\n")
                asmFile.write("sw t0,-4(fp)\n")
            elif(table.scopes[-1].level<scope.level):
                asmFile.write("sw sp,-4(fp)\n")
            asmFile.write("addi sp, sp, "+str(entity.frameLength)+"\n")
            asmFile.write("jal  L"+str(entity.startingQuad)+"\n")
            asmFile.write("addi sp, sp, -"+str(entity.frameLength)+"\n")        
        elif(op=="begin_block" and table.scopes[-1].level!=0):
            asmFile.write("sw ra,(sp)\n")
        elif (op == "end_block" and table.scopes[-1].level!=0):
            asmFile.write("lw ra,(sp)\n")
            asmFile.write("jr ra\n")
        elif (op == "begin_block" and table.scopes[-1].level == 0):
            asmFile.seek(0, os.SEEK_SET)
            asmFile.write("b L"+str(count)+"\n")
            asmFile.seek(0, os.SEEK_END)
            asmFile.write("addi sp,sp,"+str(compute_offset())+"\n")
            asmFile.write("mv gp,sp\n")
        elif (op == "halt"):
            asmFile.write("li a0, 0\n")
            asmFile.write("li a7, 93\n")
            asmFile.write("ecall\n")
    quadList=[]

# Syntaktikos Analyths
def syntax_an():
    global result_lex, line

    result_lex = lex()
    line = result_lex[2]

    def program():
        global result_lex, line

        if (result_lex[1] == programtk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == idtk):
                this_id = result_lex[0]  
                result_lex = lex()
                line = result_lex[2]
                block(this_id, 1)

                if (result_lex[1] == dottk):
                    result_lex = lex()
                    line = result_lex[2]
                    return
                else:
                    print("ERROR MESSAGE: Missing dot at the end of program", line)
                    exit(-1)
            else:
                print("ERROR MESSAGE: Missing file name ", line)
                exit(-1)
        else:
            print("ERROR MESSAGE: The word 'program' missing at the start of program", line)
            exit(-1)

    def block(name, flag):
        global result_lex, table

        if (result_lex[1] == open_blocktk):

            add_scope(name)  # ftiaxnw kainourgio scope kathe fora pou mpainw edw
            if (flag == 0):  # an den eimaste sthn main prosthese tis parametrous tou subprogram sto topScope
                add_parameters()
            result_lex = lex()
            line = result_lex[2]
            declarations()
            subprograms()
            genQuad('begin_block', name, 'null', 'null')  
            if (flag == 0):  # an den eimaste sthn main bale to starting Quad gia to subprogram
                table.scopes[-1].startingQuad = nextQuad()
            blockstatements()
            if (flag == 1):
                genQuad('halt', 'null', 'null', 'null')
            else:
                table.scopes[-1].frameLength = compute_offset()
            genQuad('end_block', name, 'null', 'null')
            if (result_lex[1] == close_blocktk):
                
                extract_symbolic_table()  # grapsimo sto arxeio to ekastote stigmiotypo
                produce()                 # produce teliko kwdika
                table.scopes.pop()  # delete to teleutaio scope

                result_lex = lex()
                line = result_lex[2]
                return

    def declarations():
        global result_lex, FileC

        while (result_lex[1] == declaretk):
            result_lex = lex()
            line = result_lex[2]
            FileC.write("int ")
            varlist()
            FileC.write(';\n\t')

            if (result_lex[1] == question_marktk):
                result_lex = lex()
                line = result_lex[2]
            else:
                print("ERROR MESSAGE: Missing question mark at the end of varlist", line)
                exit(-1)
        return

    def varlist():
        global result_lex, FileC

        if (result_lex[1] == idtk):
            # add variable to scope    
            V = Variable()
            V.name = result_lex[0]
            V.type = "VAR"
            V.dataType = "Int"
            V.offset = compute_offset()
            add_entity(V)
            FileC.write(result_lex[0])
            result_lex = lex()
            line = result_lex[2]

            while (result_lex[1] == commatk):
                FileC.write(result_lex[0])
                result_lex = lex()
                line = result_lex[2]

                if (result_lex[1] == idtk):
                    # add variable to scope    
                    V = Variable()
                    V.name = result_lex[0]
                    V.type = "VAR"
                    V.dataType = "Int"
                    V.offset = compute_offset()
                    add_entity(V)
                    FileC.write(result_lex[0])
                    result_lex = lex()
                    line = result_lex[2]
                else:
                    print(
                        "ERROR MESSAGE: Missing comma before id or there are two or more id without comma between them",
                        line)
                    exit(-1)
        return

    def subprograms():
        global result_lex

        while (result_lex[1] == functiontk or result_lex[1] == proceduretk):
            subprogram()
        return

    def subprogram():
        global result_lex

        if (result_lex[1] == proceduretk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == idtk):
                P = Procedure()
                P.name = result_lex[0]
                P.type = "PROC"
                P.dataType = "Int"
                add_entity(P)

                this_id = result_lex[0]  
                result_lex = lex()
                line = result_lex[2]

                if (result_lex[1] == left_parenthesistk):
                    result_lex = lex()
                    line = result_lex[2]
                    formalparlist()

                    if (result_lex[1] == right_parenthesistk):
                        result_lex = lex()
                        line = result_lex[2]
                        block(this_id, 0)  
                        return
                    else:
                        print("ERROR MESSAGE : Right parenthesis doesnt close after formalparlist", line)
                        exit(-1)
                else:
                    print("ERROR MESSAGE: Left parenthesis doesnt close after formalparlist", line)
                    exit(-1)
            else:
                print("ERROR MESSAGE: Waiting id after procedure ", line)
                exit(-1)

        elif (result_lex[1] == functiontk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == idtk):
                this_id = result_lex[0]  
                F = Function()
                F.name = result_lex[0]
                F.type = "FUNC"
                F.dataType = "Int"
                add_entity(F)

                result_lex = lex()
                line = result_lex[2]

                if (result_lex[1] == left_parenthesistk):
                    result_lex = lex()
                    line = result_lex[2]
                    formalparlist()

                    if (result_lex[1] == right_parenthesistk):
                        result_lex = lex()
                        line = result_lex[2]
                        block(this_id, 0)
                        return
                    else:
                        print("ERROR MESSAGE : Right parenthesis doesnt close after formalparlist", line)
                        exit(-1)
                else:
                    print("ERROR MESSAGE: Left parenthesis doesnt close after formalparlist", line)
                    exit(-1)
            else:
                print("ERROR MESSAGE: Waiting id after procedure", line)
                exit(-1)

    def formalparlist():
        global result_lex

        formalparitem()
        while (result_lex[1] == commatk):
            result_lex = lex()
            line = result_lex[2]
            formalparitem()
        return

    def formalparitem():
        global result_lex, line

        if (result_lex[1] == intk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == idtk):
                # add formal parameter to a list
                FP = FormalParameter()
                FP.name = result_lex[0]
                FP.mode = "CV"
                add_argument(FP)

                result_lex = lex()
                line = result_lex[2]
            else:
                print("ERROR MESSAGE: Waiting normal name after variable 'in' ", line)
                exit(-1)
        elif (result_lex[1] == inouttk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == idtk):

                # add formal parameter to a list
                FP = FormalParameter()
                FP.name = result_lex[0]
                FP.mode = "REF"
                add_argument(FP)

                result_lex = lex()
                line = result_lex[2]
            else:
                print("ERROR MESSAGE: Waiting normal name after variable 'inout' ", line)
                exit(-1)
        return

    def statements():
        global result_lex, line

        if (result_lex[1] == open_blocktk):
            result_lex = lex()
            line = result_lex[2]
            statement()

            while (result_lex[1] == question_marktk):
                result_lex = lex()
                line = result_lex[2]
                statement()

            if (result_lex[1] == close_blocktk):
                result_lex = lex()
                line = result_lex[2]
                return
            else:
                print("ERROR MESSAGE: Block doesn't close at statements", line)
                exit(-1)
        else:
            statement()
            if (result_lex[1] == question_marktk):
                result_lex = lex()
                line = result_lex[2]
                return
            else:
                print("ERROR MESSAGE: Question mark doesn't exist after statement ", line)
                exit(-1)

    def blockstatements():
        global result_lex, line

        statement()
        while (result_lex[1] == question_marktk):
            result_lex = lex()
            line = result_lex[2]
            statement()

    def statement():
        global result_lex

        if (result_lex[1] == idtk):
            assignment_stat()
        elif (result_lex[1] == iftk):
            if_stat()
        elif (result_lex[1] == whiletk):
            while_stat()
        elif (result_lex[1] == forcasetk):
            forcase_stat()
        elif (result_lex[1] == incasetk):
            incase_stat()
        elif (result_lex[1] == switchcasetk):  
            switchcase_stat()  
        elif (result_lex[1] == returntk):  
            return_stat()  
        elif (result_lex[1] == calltk):
            call_stat()
        elif (result_lex[1] == inputtk):
            input_stat()
        elif (result_lex[1] == printtk):
            print_stat()
        return

    def assignment_stat():
        global result_lex, line

        if (result_lex[1] == idtk):
            this_id = result_lex[0]  
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == assigmenttk):
                result_lex = lex()
                line = result_lex[2]
                Eplace = expression()  
                genQuad(':=', Eplace, "null", this_id)  
                return
            else:
                print("ERROR MESSAGE: Assigment symbol must be exist after the name of variable.", line)
                exit(-1)
        else:
            print("ERROR MESSAGE: Not exist", line)
            exit(-1)

    def if_stat():
        global result_lex, line

        if (result_lex[1] == iftk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == left_parenthesistk):
                result_lex = lex()
                line = result_lex[2]
                Cond = condition()  
                backPatch(Cond[0], nextQuad())  

                if (result_lex[1] == right_parenthesistk):
                    result_lex = lex()
                    line = result_lex[2]
                    statements()
                    ifStatList = makeList(nextQuad())  
                    genQuad('jump', 'null', 'null', 'null')  
                    backPatch(Cond[1], nextQuad())  
                    elsepart()
                    backPatch(ifStatList, nextQuad())  
                    return
                else:
                    print("ERROR MESSAGE: Parenthesis doesn't close on IF condition", line)
                    exit(-1)
            else:
                print("ERROR MESSAGE: Parenthesis doesn't open on IF condition", line)
                exit(-1)
        else:
            print("ERROR MESSAGE: Problem on IF open", line)
            exit(-1)

    def elsepart():
        global result_lex, line

        if (result_lex[1] == elsetk):
            result_lex = lex()
            line = result_lex[2]
            statements()
        return

    def while_stat():
        global result_lex, line

        if (result_lex[1] == whiletk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == left_parenthesistk):
                result_lex = lex()
                line = result_lex[2]
                CountQuad = nextQuad()  
                Cond = condition()  
                backPatch(Cond[0], nextQuad())  

                if (result_lex[1] == right_parenthesistk):
                    result_lex = lex()
                    line = result_lex[2]
                    statements()
                    genQuad('jump', 'null', 'null', CountQuad)  
                    backPatch(Cond[1], nextQuad())  
                    return
                else:
                    print("ERROR MESSAGE: Parenthesis doesn't close on WHILE condition", line)
                    exit(-1)
            else:
                print("ERROR MESSAGE: Parenthesis doesn't open on WHILE condition", line)
                exit(-1)
        else:
            print("ERROR MESSAGE: WHILE problem", line)
            exit(-1)

    def switchcase_stat():
        global result_lex, line

        if (result_lex[1] == switchcasetk):
            result_lex = lex()
            line = result_lex[2]
            outputlst = emptyList()  

            while (result_lex[1] == casetk):
                result_lex = lex()
                line = result_lex[2]

                if (result_lex[1] == left_parenthesistk):
                    result_lex = lex()
                    line = result_lex[2]
                    Cond = condition()  
                    backPatch(Cond[0], nextQuad())  

                    if (result_lex[1] == right_parenthesistk):
                        result_lex = lex()
                        line = result_lex[2]
                        statements()
                        outputjump = makeList(nextQuad())  
                        genQuad("jump", "null", "null", "null")  
                        outputlst = merge(outputlst, outputjump)  
                        backPatch(Cond[1], nextQuad())  
                    else:
                        print("ERROR MESSAGE: Left paranthesis doesn't exist on FORECASE", line)
                        exit(-1)
                else:
                    print("ERROR MESSAGE: Right paranthesis doesn't exist on  FORECASE", line)
                    exit(-1)

            if (result_lex[1] == defaulttk):
                result_lex = lex()
                line = result_lex[2]
                statements()
                backPatch(outputlst, nextQuad())  
            else:
                print("ERROR MESSAGE: DEFAULT doesn't start correctly at the begging of FORECASE", line)
                exit(-1)
        else:
            print("ERROR MESSAGE: FORECASE doesn't start correctly", line)
            exit(-1)

    def forcase_stat():
        global result_lex, line

        if (result_lex[1] == forcasetk):
            result_lex = lex()
            line = result_lex[2]
            CountQuad = nextQuad()  

            while (result_lex[1] == casetk):
                result_lex = lex()
                line = result_lex[2]

                if (result_lex[1] == left_parenthesistk):
                    result_lex = lex()
                    line = result_lex[2]
                    Cond = condition()  
                    backPatch(Cond[0], nextQuad())  

                    if (result_lex[1] == right_parenthesistk):
                        result_lex = lex()
                        line = result_lex[2]
                        statements()
                        genQuad('jump', 'null', 'null', CountQuad)  
                        backPatch(Cond[1], nextQuad())  
                    else:
                        print("ERROR MESSAGE: Right parenthesis not exist on FORECASE", line)
                        exit(-1)
                else:
                    print("ERROR MESSAGE: Left parenthesis not exist on FORECASE", line)
                    exit(-1)

            if (result_lex[1] == defaulttk):
                result_lex = lex()
                line = result_lex[2]
                statements()
            else:
                print("ERROR MESSAGE: Default doesn't start carrectly on FORECASE", line)
                exit(-1)
        else:
            print("ERROR MESSAGE: FORECASE doesn't start correctly ", line)
            exit(-1)

    def incase_stat():
        global result_lex, line

        if (result_lex[1] == incasetk):
            result_lex = lex()
            line = result_lex[2]
            CountQuad = nextQuad()  
            w = newTemp()  
            genQuad(':=', '0', 'null', w)

            while (result_lex[1] == casetk):
                result_lex = lex()
                line = result_lex[2]

                if (result_lex[1] == left_parenthesistk):
                    result_lex = lex()
                    line = result_lex[2]
                    Cond = condition()  
                    backPatch(Cond[0], nextQuad())  

                    if (result_lex[1] == right_parenthesistk):
                        result_lex = lex()
                        line = result_lex[2]
                        statements()
                        genQuad(':=', '1', 'null', w)  
                        backPatch(Cond[1], nextQuad())  
                    else:
                        print("ERROR MESSAGE: Right parenthesis not exist on FORECASE", line)
                        exit(-1)
                else:
                    print("ERROR MESSAGE: Left parenthesis not exist on FORCASE", line)
                    exit(-1)
            genQuad('=', w, '1', CountQuad)  
        else:
            print("ERROR MESSAGE: FORECASE doesn't start correctly", line)
            exit(-1)

    def return_stat():
        global result_lex, line

        if (result_lex[1] == returntk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == left_parenthesistk):
                result_lex = lex()
                line = result_lex[2]
                Eplace = expression()  
                genQuad('retv', Eplace, "null", "null")  

                if (result_lex[1] == right_parenthesistk):
                    result_lex = lex()
                    line = result_lex[2]
                    return
                else:
                    print("ERROR MESSAGE: Parenthesis doesn't close correctly on RETURN", line)
                    exit(-1)
            else:
                print("ERROR MESSAGE: Parenthesis doesn't open on RETURN", line)
                exit(-1)

    def call_stat():
        global result_lex, line

        if (result_lex[1] == calltk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == idtk):
                this_id = result_lex[0]  
                result_lex = lex()
                line = result_lex[2]

                if (result_lex[1] == left_parenthesistk):
                    result_lex = lex()
                    line = result_lex[2]
                    actualparlist()
                    genQuad('call', this_id, 'null', 'null')  

                    if (result_lex[1] == right_parenthesistk):
                        result_lex = lex()
                        line = result_lex[2]
                        return
                    else:
                        print("ERROR MESSAGE: Parenthesis doesn't close on  CALL", line)
                        exit(-1)
                else:
                    print("ERROR MESSAGE: Parenthesis doesn't open on  CALL", line)
                    exit(-1)
            else:
                print("ERROR MESSAGE: ID doesn't exist on CALL", line)
                exit(-1)
        else:
            print("ERROR MESSAGE: CALL doesn't start correctly", line)
            exit(-1)
        return

    def print_stat():
        global result_lex, line

        if (result_lex[1] == printtk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == left_parenthesistk):
                result_lex = lex()
                line = result_lex[2]
                Eplace = expression()  
                genQuad('out', Eplace, 'null', 'null') 

                if (result_lex[1] == right_parenthesistk):
                    result_lex = lex()
                    line = result_lex[2]
                else:
                    print("ERROR MESSAGE: Parenthesis doesn't close on PRINT", line)
                    exit(-1)
            else:
                print("ERROR MESSAGE: Parenthesis doesn't open on PRINT", line)
                exit(-1)
        else:
            print("ERROR MESSAGE: PRINT doesn't start correctly", line)
            exit(-1)
        return

    def input_stat():
        global result_lex, line

        if (result_lex[1] == inputtk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == left_parenthesistk):
                result_lex = lex()
                line = result_lex[2]

                if (result_lex[1] == idtk):
                    this_id = result_lex[0]  
                    genQuad('inp', this_id, 'null', 'null')  
                    result_lex = lex()
                    line = result_lex[2]

                    if (result_lex[1] == right_parenthesistk):
                        result_lex = lex()
                        line = result_lex[2]
                        return
                    else:
                        print("ERROR MESSAGE: Parenthesis doesn't close on INPUT", line)
                        exit(-1)
                else:
                    print("ERROR MESSAGE: ID doesn't exist on INPUT", line)
                    exit(-1)
            else:
                print("ERROR MESSAGE: Parenthesis doesn't open  on INPUT", line)
                exit(-1)
        else:
            print("ERROR MESSAGE: INPUT doesn't start correctly", line)
            exit(-1)

    def actualparlist():
        global result_lex, line

        actualparitem()
        while (result_lex[1] == commatk):
            result_lex = lex()
            line = result_lex[2]
            actualparitem()
        return

    def actualparitem():
        global result_lex, line

        if (result_lex[1] == intk):
            result_lex = lex()
            line = result_lex[2]
            thisExpression = expression()  
            genQuad('par', thisExpression, 'CV', 'null')

        elif (result_lex[1] == inouttk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == idtk):
                this_id = result_lex[0]  
                result_lex = lex()
                line = result_lex[2]
                genQuad('par', this_id, 'REF', 'null')  
            else:
                print("ERROR MESSAGE: It hasn't variable name after 'inout' ", line)
                exit(-1)
        return

    def condition():
        global result_lex, line
        CondTrue = []
        CondFalse = []
        BoolTerm1 = boolterm()
        CondFalse = BoolTerm1[1]
        CondTrue = BoolTerm1[0]

        while (result_lex[1] == ortk):
            result_lex = lex()
            line = result_lex[2]
            backPatch(CondFalse, nextQuad())  
            BoolTerm2 = boolterm()  
            CondTrue = merge(CondTrue, BoolTerm2[0])  
            CondFalse = BoolTerm2[1]  
        return CondTrue, CondFalse  

    def boolterm():
        global result_lex, line
        BoolTerm_True = []
        BoolTerm_False = []
        BoolFactor1 = boolfactor()
        BoolTerm_False = BoolFactor1[1]
        BoolTerm_True = BoolFactor1[0]

        while (result_lex[1] == andtk):
            result_lex = lex()
            line = result_lex[2]
            backPatch(BoolTerm_True, nextQuad())
            BoolFactor2 = boolfactor()
            BoolTerm_False = merge(BoolTerm_False, BoolFactor2[1])
            BoolTerm_True = BoolFactor2[0]
        return BoolTerm_True, BoolTerm_False

    def boolfactor():
        global result_lex, line
        BoolFactor_True = []
        BoolFactor_False = []

        if (result_lex[1] == nottk):
            result_lex = lex()
            line = result_lex[2]

            if (result_lex[1] == left_brackettk):
                result_lex = lex()
                line = result_lex[2]
                Cond = condition()

                if (result_lex[1] == right_brackettk):
                    result_lex = lex()
                    line = result_lex[2]
                    BoolFactor_False = Cond[0]
                    BoolFactor_True = Cond[1]
                else:
                    print("ERROR MESSAGE: Close bracket doesn't exist after BOOLFACTOR condition", line)
                    exit(-1)
            else:
                print("ERROR MESSAGE: Want open bracket after not on  BOOLFACTOR condition", line)
                exit(-1)
        elif (result_lex[1] == left_brackettk):
            result_lex = lex()
            line = result_lex[2]
            Cond = condition()  

            if (result_lex[1] == right_brackettk):
                result_lex = lex()
                line = result_lex[2]
                BoolFactor_False = Cond[1]  
                BoolFactor_True = Cond[0]  
            else:
                print("ERROR MESSAGE: Close bracket doesn't exist after BOOLFACTOR condition", line)
                exit(-1)
        else:
            Eplace1 = expression()
            rel_op = relational_oper()
            Eplace2 = expression()
            BoolFactor_True = makeList(nextQuad())
            genQuad(rel_op, Eplace1, Eplace2, 'null')
            BoolFactor_False = makeList(nextQuad())
            genQuad('jump', 'null', 'null', 'null')
        return BoolFactor_True, BoolFactor_False

    def expression():
        global result_lex, line
        optional_sign()
        Tplace1 = term()  

        while (result_lex[1] == addertk or result_lex[1] == subtk):
            this_oper = add_oper()  
            Tplace2 = term()
            w = newTemp()
            genQuad(this_oper, Tplace1, Tplace2, w)
            Tplace1 = w

        Eplace = Tplace1
        return Eplace

    def term():
        global result_lex, line
        Fplace1 = factor()  

        while (result_lex[1] == multk or result_lex[1] == divtk):
            this_oper = mul_oper()  
            Fplace2 = factor()
            w = newTemp()
            genQuad(this_oper, Fplace1, Fplace2, w)
            Fplace1 = w

        Tplace = Fplace1
        return Tplace

    def factor():
        global result_lex, line

        if (result_lex[1] == digtk):
            fact = result_lex[0]  
            result_lex = lex()
            line = result_lex[2]

        elif (result_lex[1] == left_parenthesistk):
            result_lex = lex()
            line = result_lex[2]
            Eplace = expression()  
            fact = Eplace  

            if (result_lex[1] == right_parenthesistk):
                result_lex = lex()
                line = result_lex[2]
            else:
                print("ERROR MESSAGE: Want right parenthesis ')' after expression on FACTOR ", line)
                exit(-1)

        elif (result_lex[1] == idtk):
            fact_temp = result_lex[0]  
            result_lex = lex()
            line = result_lex[2]
            fact = idtail(fact_temp)  
        else:
            print("ERROR MESSAGE: Want constant or expression or variable on FACTOR", line)
            exit(-1)
        return fact

    def idtail(this_id):
        global result_lex, line

        if (result_lex[1] == left_parenthesistk):
            result_lex = lex()
            line = result_lex[2]
            actualparlist()
            w = newTemp()  
            genQuad('par', w, 'RET', 'null')  
            genQuad('call', this_id, 'null', 'null') 
            if (result_lex[1] == right_parenthesistk):
                result_lex = lex()
                line = result_lex[2]
                return w  
            else:
                print("ERROR MESSAGE: In IDTAIL we want right parenthesis ')' after actualparlist", line)
                exit(-1)
        else:
            return this_id

    def optional_sign():
        global result_lex, line

        if (result_lex[1] == addertk or result_lex[1] == subtk):
            add_oper()
        return

    def relational_oper():
        global result_lex, line

        if (result_lex[1] == equaltk):
            rel_op = result_lex[0]
            result_lex = lex()
            line = result_lex[2]
        elif (result_lex[1] == not_equaltk):
            rel_op = result_lex[0]
            result_lex = lex()
            line = result_lex[2]
        elif (result_lex[1] == greaterthantk):
            rel_op = result_lex[0]
            result_lex = lex()
            line = result_lex[2]
        elif (result_lex[1] == lessthantk):
            rel_op = result_lex[0]
            result_lex = lex()
            line = result_lex[2]
        elif (result_lex[1] == greater_or_equaltk):
            rel_op = result_lex[0]
            result_lex = lex()
            line = result_lex[2]
        elif (result_lex[1] == less_or_equaltk):
            rel_op = result_lex[0]
            result_lex = lex()
            line = result_lex[2]
        else:
            print("ERROR MESSAGE: Missing = , < , <= , <> ,>= , > ", line)
            exit(-1)
        return rel_op

    def add_oper():
        global result_lex, line

        if (result_lex[1] == addertk):
            this_oper = result_lex[0]  
            result_lex = lex()
            line = result_lex[2]

        elif (result_lex[1] == subtk):
            this_oper = result_lex[0]  
            result_lex = lex()
            line = result_lex[2]
        return this_oper

    def mul_oper():
        global result_lex, line

        if (result_lex[1] == multk):
            this_oper = result_lex[0]  
            result_lex = lex()
            line = result_lex[2]

        elif (result_lex[1] == divtk):
            this_oper = result_lex[0]  
            result_lex = lex()
            line = result_lex[2]
        return this_oper

    program()
    return


def cFileExtract():
    global VarTempList
    length = len(VarTempList)

    if (length > 0): FileC.write("int ")
    # Temp_i variables.
    for i in range(length):
        FileC.write(VarTempList[i])
        if (length != i + 1):
            FileC.write(",")
        else:
            FileC.write(";\n\n\t")

    for j in QuadsList:
        j_temp = "L_" + str(j[0]) + ": "
        if (j[1] == 'begin_block'):
            FileC.write("L_" + str(j[0]) + ":\n\t")
        elif (j[1] == ":="):
            FileC.write(j_temp + j[4] + "=" + j[2] + ";\n\t")
        elif (j[1] == "+"):
            FileC.write(
                j_temp + j[4] + "=" + j[2] + "+" + j[3] + ";\n\t")
        elif (j[1] == "-"):
            FileC.write(
                j_temp + j[4] + "=" + j[2] + "-" + j[3] + ";\n\t")
        elif (j[1] == "*"):
            FileC.write(
                j_temp + j[4] + "=" + j[2] + "*" + j[3] + ";\n\t")
        elif (j[1] == "/"):
            FileC.write(
                j_temp + j[4] + "=" + j[2] + "/" + j[3] + ";\n\t")
        elif (j[1] == "jump"):
            FileC.write(j_temp + "goto L_" + str(j[4]) + ";\n\t")
        elif (j[1] == "<"):
            FileC.write(j_temp + "if (" + j[2] + "<" + j[3] + ") goto L_" + str(
                j[4]) + ";\n\t")
        elif (j[1] == ">"):
            FileC.write(j_temp + "if (" + j[2] + ">" + j[3] + ") goto L_" + str(
                j[4]) + ";\n\t")
        elif (j[1] == ">="):
            FileC.write(
                j_temp + "if (" + j[2] + ">=" + j[3] + ") goto L_" + str(
                    j[4]) + ";\n\t")
        elif (j[1] == "<="):
            FileC.write(
                j_temp + "if (" + j[2] + "<=" + j[3] + ") goto L_" + str(
                    j[4]) + ";\n\t")
        elif (j[1] == "<>"):
            FileC.write(j_temp + "if (" + str(j[2]) + "!=" + str(
                j[3]) + ") goto L_" + str(j[4]) + ";\n\t")
        elif (j[1] == "="):
            FileC.write(
                j_temp + "if (" + j[2] + "==" + j[3] + ") goto L_" + str(
                    j[4]) + ";\n\t")
        elif (j[1] == "out"):  # print to apotelesma tou expression.
            FileC.write(
                j_temp + "printf(\"" + j[2] + "= %d\", " + j[2] + ");\n\t")
        elif (j[1] == 'halt'):
            FileC.write("L_" + str(j[0]) + ": {}\n\t")
            break
        else:
             FileC.write("L_" + str(j[0]) + ":\n\t")   


def makefiles():
    global FileC, asmFile
    # Open files to write
    intFile = open('intFile.int', 'w')
    FileC = open('FileC.c', 'w')

    FileC.write("int main(){\n\t")
    f = open("test.symb", "w")
    f.close()


   
    asmFile.write('         \n\n\n\n\n')
    
    syntax_an()

    # write in int filee
    for quad in QuadsList:
        intFile.write(str(quad[0]) + ":  " + str(quad[1]) + "  " + str(quad[2]) + "  " + str(
            quad[3]) + "  " + str(quad[4]))
        intFile.write("\n")

    cFileExtract()

    FileC.write("\n}")

    # Close open file
    FileC.close()
    intFile.close()
    asmFile.close()


makefiles()
