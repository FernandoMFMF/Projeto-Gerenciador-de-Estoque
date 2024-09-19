import itertools

# Definindo as variáveis booleanas P, E, L, R
variaveis = ['P', 'E', 'L', 'R']

# Gerando todas as combinações possíveis de True (T) e False (F)
combinacoes = list(itertools.product([False, True], repeat=4))

# Cabeçalho da tabela
print(f"{'P':^5} {'E':^5} {'L':^5} {'R':^5} {'Solução Completa':^20}")
print('-' * 40)

# Gerando a tabela verdade
for combinacao in combinacoes:
    P, E, L, R = combinacao
    solucao_completa = P and E and L and R
    print(f"{P!s:^5} {E!s:^5} {L!s:^5} {R!s:^5} {solucao_completa!s:^20}")

"""
 P     E     L     R     Solução Completa  
----------------------------------------    
False False False False        False        
False False False True         False        
False False True  False        False        
False False True  True         False        
False True  False False        False        
False True  False True         False        
False True  True  False        False        
False True  True  True         False        
True  False False False        False        
True  False False True         False
True  False True  False        False
True  False True  True         False
True  True  False False        False
True  True  False True         False
True  True  True  False        False
True  True  True  True          True

"""