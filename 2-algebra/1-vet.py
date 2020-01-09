#uma lista com 3 numeros corresponde a um vetor em um espaço tridimensional

peso_altura_idade = [70,#peso em quilos
                     170,#altura em centimentros
                     40] #anos
 
  #um dos problemas é que listas em python, não são vetores
   #quando se trata de vetores, se somarmos [1,3] + [1,3] o resultado é [2,6]. 
   #porem em listas o resulto seria [1,3,1,3]
   #A ferramenta mais apropriada pra função é np.array() visto que np.array[1,3] + np.array[1,3] 
  
#soma de vetors

np.array([1,4]) + np.array([3,4])

#subtração de vetores

np.array([2,2]) - np.array([3,3])

#multiplicação por escalar
4 * np.array([1,2])

#media de vetor
np.array([1,2,3]).mean()

#produto escalar de dois vetores
np.sum(np.array([1,2,3])*np.array([2,3,4]))

#soma dos quadrados dos elementos do vetor

(np.array([1,2,3,4,5])**2).sum()
#output 
#55

#magnitude do vetor
from math import sqrt
np.sqrt((np.array([1,2,3,4,5])**2).sum())

#distancia de 2 dotores

sqrt(((np.array([1,2,4]) - np.array([2,1,1]))**2).sum())
