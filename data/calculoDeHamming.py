from hermetrics.hamming import Hamming

ham = Hamming()
def get_name_materia_similar(name, nombres):
    if (name != None and nombres != None):
        max = 0
        maxCadena=None
        for cadena in nombres:
            h = ham.similarity(cadena, name)
            if (h > max):
                max = h
                maxCadena = cadena
        
        if (max > 0.5):
            return maxCadena
        else:
            return None
    else:
        return None
