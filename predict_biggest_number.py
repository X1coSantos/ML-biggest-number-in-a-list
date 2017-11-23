# importa as dependencias
from sklearn import tree
from sklearn.model_selection import train_test_split
from gerar_listas import *

# Gera a lista dos inputs
x = gerar_lista_numeros(10000,3)

# Gera os outputs da lista x
y = gerar_lista_numeros_respostas(x)

# Divide entre o treino e o teste, treino 80%, teste 20%
treino_x, treino_x2, treino_y, treino_y2 = train_test_split(x, y, test_size=0.2)

# Usa classificador de decisao em arvore
clf = tree.DecisionTreeClassifier()

# Treina o programa
clf.fit(treino_x,treino_y)

# Faz predicões para o treino
prediction = clf.predict(treino_x2)

# inicializa score
score = 0
# loop que passa pelas predicoes
for i in range(len(prediction)):
    # verifica se a predicao foi bem feita, caso tenha sido, adiciona 1 ao score
    if prediction[i] == treino_y2[i]:
        score += 1

# print da percentagem de vezes que acertou
print(f"% corretos: {score/len(prediction) * 100}%")

# lista manual para verificar os resultados
lista_manual = [[100,100,100], [356,563,452], [266,734,235]]
prediction2 = clf.predict(lista_manual)
print(lista_manual)
print(prediction2)