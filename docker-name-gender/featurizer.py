from numpy import array
from re import fullmatch

def extract(name):
    '''
    Given a string name, this function creates the sequence for LSTM
    maxlen is set to 15
    '''
    if fullmatch("[a-zA-Z]+",name):
        try:
            nameasc = ( 15 - name[:15].__len__() ) * [0] + [ord(ch) for ch in name[:15].lower()]
            nameasc = [max(el - 96,0) for el in nameasc]
            for idx in range(nameasc.__len__()):
                tmparr = [0] * 27
                tmparr[nameasc[idx]] = 1
                nameasc[idx] = tmparr
            return array([nameasc])
        except Exception as e:
            return ''.join("Error on line " + str(exc_info()[-1].tb_lineno) + " | " + str(type(e).__name__) + " | " + str(e))
    else:
        return "not supported"