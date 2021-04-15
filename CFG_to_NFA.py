# for a CFG G, return the NFA N that leads to DK with a list of 
# rules stored in each state
def CFG_to_NFA(G):
    V, rules = G['variables'], G['rules']
    
    # state_of[A] = {all states which store a rule of kind A -> .w}
    # rulw_in[q] = {A -> uav, 'a'} => A stores A -> u.av, a in V or sigma
    state_of = {A : [] for A in V}      
    rule_in = [{'rule': [], 'dot':'$'}] 
     
    # initialize the NFA: delta function, alphabet, and final states
    delta, sigma, F = [{}], G['terminals'], []
    sigma.append('e')
    q = 0

    for rule in rules:
        q = q + 1 # current state

        A, W = rule[0], rule[1]
        state_of[A].append(q) # q holds the rule A -> .W

        for w in W:
            # create the intermediate dotted rules
            delta.append({w: [q + 1]})
            rule_in.append({'rule': rule, 'dot': w})

            q = q + 1

        # after W is processed, add the finished rule in the final states
        rule_in.append({'rule': rule,'dot': ''})
        delta.append({})
        F.append(q)

    count_state = q + 1

    # Add 'e' arrows from first state (0) to all states that contain 
    # rules of type S -> .w
    delta[0]['e'] = state_of['S']

    for q in range(0, count_state):
        # Add 'e' arrows from q to q' if q contains B -> u.Av and
        # q' contains B -> .W
        A = rule_in[q]['dot']
        if A in V:
            delta[q]['e'] = [p for p in state_of[A] if p != q]
            # !caution: avoid the situation delta(q, e) = [q, ...]
            
        # For every other variable or terminal a, set delta(q, a) = []
        for a in V + sigma:
            if a not in delta[q].keys():
                delta[q][a] = []
    
    return({'delta': delta, 'alphabet': V + sigma, 'final': F}, rule_in)