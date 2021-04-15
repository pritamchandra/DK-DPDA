from CFG_to_NFA import CFG_to_NFA
from NFA_to_DFA import NFA_to_DFA

def DK_test(G):
    terminals = G['terminals']
    N, rule_in = CFG_to_NFA(G)
    D, state_index = NFA_to_DFA(N)
    F = D['final']
    
    # collect all the rules in all the final states
    Final_rules = [[rule_in[q] for q in state_index[j]] for j in F]

    print('\nRules in the final states:')
    for rules in Final_rules: print(rules)
        
    for rules in Final_rules:
        c_rules = 0     # initialize the number of completed rules
        for rule in rules:
            a = rule['dot']

            # rule is complete, then check if c_rules is already 1
            if a == '':
                if c_rules == 1:
                    return('\nFails, Failing rule: ' + str(rule) + '\n')
                c_rules = c_rules + 1
                
            # check for rules of type A -> u.av where a in terminal    
            if a in terminals:
                return('\nFails, Failing rule: ' + str(rule) + '\n')

    # G has passed the test if it has not failed yet
    return('\nPasses\n')