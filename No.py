
class No(object):
    __proximo = None
    __troca = None
    __final = False

    __custoReal = 0
    __heuristica = 0

    def __init__(self, proximo=None, troca=None, final=False):
        self.__proximo = proximo
        self.__troca = troca
        self.__final = final

        self.__custoReal = 0
        self.__heuristica = 0

    def setProximo(self, proximo):
        self.__proximo = proximo

    def setTroca(self, troca):
        self.__troca = troca

    def setFinal(self, final):
        self.__final = final

    def setCustoReal(self, custoReal):
        self.__custoReal = custoReal

    def setHeuristica(self, heuristica):
        self.__heuristica = heuristica

    def getProximo(self):
        return self.__proximo

    def getTroca(self):
        return self.__troca

    def getFinal(self):
        return self.__final

    def getCustoReal(self):
        return self.__custoReal

    def getHeuristica(self):
        return self.__heuristica
