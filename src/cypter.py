import random
weight=20
move = 50

def enCode(code):
    key = int(random.random()*15)
    engbk=bytearray(code.encode('utf-8'))
    result = bytearray(len(engbk)*3)
    for i in range(len(engbk)):
        origi = engbk[i]
        firsrencode = origi^key
        third = firsrencode%weight
        fourth = firsrencode//weight
        result[i*3]=third+move
        result[i*3+1]=fourth+move
        result[i*3+2]=key
    return result.decode('utf-8')


def deCode(code):
    degbk = bytearray(code.encode('utf-8'))
    result = bytearray(int(len(degbk)/3))
    for i in range(len(result)):
       code =  degbk[i*3]-move+(degbk[i*3+1]-move)*weight
       result[i] = code^degbk[i*3+2]
    return result.decode('utf-8')