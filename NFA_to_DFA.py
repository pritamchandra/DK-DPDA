# regular function to check if A and B has common elements
def non_empty_intersection(A, B):
    for b in B:
        if b in A: 
            return True
    return False

# given a delta function calculate a list of closures of every state
def calculate_closure(delta):
    closure = [[] for i in range(len(delta))]
    
    # Closure[i] = union(closure(a) : i -> a is an 'e' transition)
    def Closure(i):
        res = closure[i]
        # Recursively, if closure[i] is already calculated 
        # in a previous step, then proceed
        if not res:
            A = delta[i]['e']
            res = [i] + A
            for a in A:
                res = list(set(res + Closure(a)))
        return res
            
    for i in range(len(delta)):
        closure[i] = Closure(i)
 
    return closure

def NFA_to_DFA(N):
    # extract the parameters of the NFA N
    _delta, _sigma, _F = N['delta'], N['alphabet'], N['final']
    _sigma.remove('e')
    
    # calculate the closure of every state
    closure = calculate_closure(_delta)
    
    # initialize the DFA: delta function, alphabets, final states
    delta, sigma, F = [], _sigma, []
    
    state_index = [closure[0]] # state_index[j] = {states of the NFA N 
    j, n = 0, 1                # stored inside the j-th state of D}
                               # j: current state, n: #states seen so far
    
    while j < n:
        delta_j = {}
        for a in sigma:
            # delta(j, a): res = union of the closures of the states 
            # where q is taken to by the NFA under the symbol a
            res = []
            for q in state_index[j]:
                for p in _delta[q][a]:
                    res = list(set(res + closure[p]))
                
            # if res is already a state then,
            # delta(j, a) = index of res in state_index
            try: delta_j[a] = state_index.index(res)
            
            # otherwise, add res to state index and update n
            except ValueError:
                state_index.append(res)
                delta_j[a] = n
                n = n + 1
                
        delta.append(delta_j)
        
        # determine if j is a final state
        if non_empty_intersection(state_index[j], _F): F.append(j)
        
        j = j + 1
        
    return ({'delta': delta, 'alphabet': sigma, 'final': F}, state_index)