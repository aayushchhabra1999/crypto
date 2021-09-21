## Random Thought

# Algorithm (Max Likelihood Estimate)
# c = Cyphertext
# results = {}
# vocab = vocabulary
# Let S = space of all encoding algos.
# For s in S:
#         P = space of all possible parameters for s
#         for p in P:
#               plain = decode(c, s, p)
#               results[(s,p)] = (no of words in plain from vocab)/(len of vocab)
# Return s, p, decode(c,s,p) from results with highest value.