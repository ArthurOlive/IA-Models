import random as random
class perceptron():
    def __init__(self):
        self.__x = [] #variaveis de entrada
        self.__y = [] #variaveis de saida 
        self.__n = 0.2#taxa de aprendizado
        self.__w = []
        self.__u = 0
        self.epoca = 0#epoca de loop

    def fit(self, X, Y):
        self.__x = X
        self.__y = Y
        for _ in range(len(self.__x[0])):
            self.__w.append(random.random() * - 1) #um x tal que 0.0 < x < 1.0, valores aleatorios pequenos
        self.epoca = 0
        erro = 1
        while(erro):
            erro = 0 #erro <- inexistente
            for i in range(len(self.__x)):
                for j in range(len(self.__x[i])):
                    self.__u += self.__w[i] * self.__x[i][j] #u = somatorio(w * x - 0) 
                k = self.g(self.__u) #k representa o y, a saida da rede com os pessos atuais
                print(" ==== Resumo =====")
                print(self.__w)
                print(self.__u)
                print(self.__x[i])
                print(self.__y[i])
                print(" =================")
                if (k != self.__y[i][0]):
                    for j in range(len(self.__x[i])):
                        self.__w[j] = self.__w[j] + self.__n * (self.__y[i][0] - k) * self.__x[i][j]
                    erro = 1
            self.epoca += 1

    def g(self, u):
        #1, se u > 0 
        #-1, se u < 0
        if (u > 0):
            return 1
        else:
            return -1

if __name__ == "__main__":
    redeneural = perceptron()
    redeneural.fit([[-1,0.1,0.4,0.7], [-1, 0.3, 0.7, 0.2]], [[1], [-1]])