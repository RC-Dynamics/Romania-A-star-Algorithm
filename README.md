# Romania-A*-Algorithm
Adaptive Cognitive Agents Class

## Output of program:
Programa com busca herística A* no mapa da Romenia

        Lugoj => Bucharest

=======================================================

    Fronteira de Busca              : [(311, 'Mehadia'), (440, 'Timisoara')] 
    Cidades Expandidas              : ['Lugoj']  #1

    Fronteira de Busca              : [(387, 'Dobreta'), (440, 'Timisoara')] 
    Cidades Expandidas              : ['Lugoj', 'Mehadia']  #2

    Fronteira de Busca              : [(425, 'Craiova'), (440, 'Timisoara')] 
    Cidades Expandidas              : ['Lugoj', 'Mehadia', 'Dobreta']  #3

    Fronteira de Busca              : [(440, 'Timisoara'), (503, 'Pitesti'), (604, 'Rimnicu Vilcea')] 
    Cidades Expandidas              : ['Lugoj', 'Mehadia', 'Dobreta', 'Craiova']  #4

    Fronteira de Busca              : [(503, 'Pitesti'), (595, 'Arad'), (604, 'Rimnicu Vilcea')] 
    Cidades Expandidas              : ['Lugoj', 'Mehadia', 'Dobreta', 'Craiova', 'Timisoara']  #5

    Fronteira de Busca              : [(504, 'Bucharest'), (595, 'Arad'), (604, 'Rimnicu Vilcea')] 
    Cidades Expandidas              : ['Lugoj', 'Mehadia', 'Dobreta', 'Craiova', 'Timisoara', 'Pitesti']  #6

    Fronteira de Busca              : [(595, 'Arad'), (604, 'Rimnicu Vilcea')] 
    Cidades Expandidas              : ['Lugoj', 'Mehadia', 'Dobreta', 'Craiova', 'Timisoara', 'Pitesti', 'Bucharest']  #7


=======================================================

    Menor caminho   : ['Lugoj', 'Mehadia', 'Dobreta', 'Craiova', 'Pitesti', 'Bucharest'] 
    Número de cidade visitas                        : 6 
    Distância total percorrida                      : 504
