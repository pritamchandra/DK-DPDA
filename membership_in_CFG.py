from CFG_to_NFA import CFG_to_NFA
from NFA_to_DFA import NFA_to_DFA

# Check membership of W in L(G) by finding an equivalent DPDA for DCFG G
# Additionally, use DK(G) to obtain the leftmost reduction of members
def membership(G, W):
    # extract DK(G) from G
    N, rule_in = CFG_to_NFA(G)
    D, state_index = NFA_to_DFA(N)
    delta, F = D['delta'], D['final']
    
    # extract the finished rule in every final state
    finished_rules = {}
    for j in F:
        for q in state_index[j]:
            if rule_in[q]['dot'] == '':
                finished_rules[j] = rule_in[q]['rule']

    # initialize the DPDA, along with U: the current string 
    # in the reduce step, V: string reduced from U
    stack, reduction = [0], [W]
    U, V = W, ''   
    q = 0
    
    for w in W:
        # add the states of DK to the stack while reading
        # W, until DK reaches a final state
        V = V + w
        q = delta[q][w]
        stack.append(q)
        
        while q in F:
            A, h = finished_rules[q]
            # return if the current string U -> S
            if A == 'S' and h == U: 
                print(' -> '.join(reduction + [h, 'S']))
                return 'accept'
            for j in range(len(h)): stack.pop()
                
            # Identify x, h, y, where h is the forced handle
            # apply xhy -> xAy; update U, V; store the reduce steps
            x, y = U[:len(V) - len(h)], U[len(V):]
            reduction += ['.'.join([x, h, y]), '.'.join([x, A, y])]
            V, U = x + A, x + A + y
            
            # proceed transition after tracing |h| steps back
            q = delta[stack[-1]][A]
            stack.append(q)
            
    return 'reject'