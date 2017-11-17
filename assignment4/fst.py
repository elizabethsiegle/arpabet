class FST:
    def __init__(self, alphabet, q, i, f, trans_func):
        self.alphabet = alphabet
        self.q = q # q = finite set of states
        self.i = i # i = 1 initial state in q
        self.f = f # f = set of final states in q
        self.trans_func = trans_func

    def transduce(self, color):
        curr = self.i
        i = 0
        uppercase_letters = []
        for x in self.alphabet:
            #print x
            uppercase_letters.append(x.capitalize())
        uppercase_letters.append(" ")
        # print uppercase_letters
        
        while i < len(color):
            if not color[i] in self.alphabet:
                return color[i] + " not lowercase letter in alphabet"
            for j in self.trans_func[curr][color[i]][1]:
                if not j in uppercase_letters:
                    return j + " not uppercase letter"
            next_state = self.trans_func[curr][color[i]][0]
            nextx = self.trans_func[curr][color[i]][1]
            color = color[:i] + self.trans_func[curr][color[i]][1] + color[i+1:]
            i += len(nextx)
            curr = next_state

        if not curr in self.f:
            return curr + " not a final state in this FST"

        return color