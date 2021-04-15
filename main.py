from DK_test import DK_test
from membership_in_CFG import membership

# each grammar is a dictionary with keys: variables, terminals, rules    
test_grammars = ({'variables': ['S', 'R', 'T'], 
                  'terminals': ['a', 'b', '0', '1'],
                  'rules': [['S', 'aR'], 
                            ['S', 'bT'], 
                            ['R', '0R1'], 
                            ['R', '01'], 
                            ['T', '0T11'],
                            ['T', '011']] },
                 
                 {'variables': ['S', 'R', 'T'], 
                  'terminals': ['0', '1'],
                  'rules': [['S', 'R'], 
                            ['S', 'T'], 
                            ['R', '0R1'], 
                            ['R', '01'], 
                            ['T', '0T11'],
                            ['T', '011']] },

                 {'variables': ['S', 'E', 'T'], 
                  'terminals': ['a', '+', '*'], 
                  'rules': [['S', 'Ea'],
                            ['E', 'E+T'],
                            ['E', 'T'],
                            ['T', 'T*a'],
                            ['T', 'a'] ] },

                 {'variables': ['S', 'A'],
                  'terminals': ['0', '1'],
                  'rules': [['S', 'A1'],
                            ['A', 'A0'],
                            ['A', '0'] ] } )

for G in test_grammars: print(DK_test(G))

G = test_grammars[0]
print(membership(G, 'b000111111'))