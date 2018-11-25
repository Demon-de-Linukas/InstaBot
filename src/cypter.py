import random

def enCode(code):
    key = int(random.random()*15)
    engbk=bytearray(code.encode('gbk'))
    result = bytearray(len(engbk)*3)
    for i in range(len(engbk)):
        origi = engbk[i]
        firsrencode = origi^key
        third = firsrencode%16
        fourth = firsrencode//16
        result[i*3]=third+65
        result[i*3+1]=fourth+65
        result[i*3+2]=key
    return result.decode('gbk')


def deCode(code):
    degbk = bytearray(code.encode('gbk'))
    result = bytearray(int(len(degbk)/3))
    for i in range(len(result)):
       code =  degbk[i*3]-65+(degbk[i*3+1]-65)*16
       result[i] = code^degbk[i*3+2]
    return result.decode('gbk')