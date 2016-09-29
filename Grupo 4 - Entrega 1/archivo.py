import pickle


def desarchivar(texto):

    f = open(texto, 'rb')
    dic = pickle.load(f)
    f.close()
    return dic

def archivar(dic, texto):

    f = open(texto, 'wb')
    pickle.dump(dic, f)
    f.close()
