# Author: Kelvin Sung
# Assignment 3: Solution
# Date: Sep 20, 2018
# 
#

# Input file formate expectation:
#   Text files, each line with
#
#   Senator-Last-Name Party-Affiliation State-Abbrev List-of-0-or-1-or-1
#                                                     1 voted yes
#                                                     0 did not vote
#                                                    -1 voted against


# Creates from the input file, dictionary where:
#
#     Senator-name:  State
#
def create_state_dict(file):
    f = open(file)
    mylist = list(f)
    s_dict = dict()
    for line in mylist:
        aslist = line.split() # split by space (default)
        s_dict[aslist[0]] = aslist[2]
    return s_dict


# Creates from the input file, dictionary where:
#
#     Senator-name:  Party-affiliation (D or R)
#
def create_party_dict(file):
    f = open(file)
    mylist = list(f)
    p_dict = dict()
    for line in mylist:
        aslist = line.split() # split by space (default)
        p_dict[aslist[0]] = aslist[1]
    return p_dict


# Creates from the input file, dictionary where:
#
#     Senator-name:  voting record list
#
def create_voting_dict(file):
    f = open(file)
    mylist = list(f)
    e_dict = dict()
    for line in mylist:
        # print(line)
        aslist = line.split() # split by space (default)
        # print(aslist[0])
        votes = [int(aslist[v]) for v in range(len(aslist)) if v > 2] # v > 2, is where the voting list begins
        # print(votes)
        e_dict[aslist[0]] = votes
    return e_dict


voting_dict = create_voting_dict("voting_record_dump109.txt")
party_dict = create_party_dict("voting_record_dump109.txt")
state_dict = create_state_dict("voting_record_dump109.txt")
#
#
# create a constant [1, 1, 1, ... ] vector of the same length as senator voting record
total_vote_count = len(voting_dict['Obama'])
one_vector = [1 for v in range(total_vote_count)]

def dot_vectors(va, vb):
    return sum([i*j for (i, j) in zip(va, vb)])

#
print("============================================")
print("(A): Testing Task 2.12.1: The senator voting dictionary:")
#print("A.1: Senator-state dictionary:")
#print(state_dict)
#print()
#print("A.2: Senator-party dictionary:")
#print(party_dict)
#print()
#print("A.3: Senator-vote dictionary:")
print(voting_dict)
print("=================================================")
print()


#
# sen: Senator name
# voting_dict:
# formatted print and returns a list: [yes  no  absent]
def dump_senator(sen):
    votes = voting_dict[sen]
    yesPlusNo = dot_vectors(votes, votes)       # dot with self, count number of 1 and -1
    yesMinusNo = dot_vectors(one_vector, votes) # dot with [1 1 1], returns total 1 minus total -1
    yesVote = int(0.5 * (yesPlusNo + yesMinusNo))
    absentVote = len(votes) - yesPlusNo
    noVote = yesPlusNo - yesVote
    l = [yesVote, noVote, absentVote]
    p = party_dict[sen]
    print(f'{sen:11}:  {p:1}   Yes:{l[0]:2d}   No:{l[1]:2d}   Absent:{l[2]:1d}')
    return l
    

print("============================================")
print("(B): Dumping all senator voting records (Total votes=", total_vote_count, ")")
for i in voting_dict.keys():
    dump_senator(i)
print("=================================================")
print()

#
# Task 2.12.2
def policy_compare(sen_a, sen_b, voting_dict):
    va = voting_dict[sen_a]
    vb = voting_dict[sen_b]
    return dot_vectors(va, vb)

print("============================================")
print("(C): Testing Task 2.12.2 Compare Policies: Total votes=", total_vote_count)
dump_senator('Obama')
print("Obama and Biden      :", policy_compare('Obama', 'Biden', voting_dict))
print("Obama and McCain     :", policy_compare('Obama', 'McCain', voting_dict))
print("Obama and Bunning(KY):", policy_compare('Obama', 'Bunning', voting_dict))
print("Obama and Cantwell   :", policy_compare('Obama', 'Cantwell', voting_dict))
print("Obama and Murray     :", policy_compare('Obama', 'Murray', voting_dict))
print()
dump_senator('Shelby')
print("Shelby and Biden      :", policy_compare('Shelby', 'Biden', voting_dict))
print("Shelby and McCain     :", policy_compare('Shelby', 'McCain', voting_dict))
print("Shelby and Bunning(KY):", policy_compare('Shelby', 'Bunning', voting_dict))
print("Shelby and Cantwell   :", policy_compare('Shelby', 'Cantwell', voting_dict))
print("Shelby and Murray     :", policy_compare('Shelby', 'Murray', voting_dict))
print()
dump_senator('Mikulski')
print("Mikulski and Biden      :", policy_compare('Mikulski', 'Biden', voting_dict))
print("Mikulski and McCain     :", policy_compare('Mikulski', 'McCain', voting_dict))
print("Mikulski and Bunning(KY):", policy_compare('Mikulski', 'Bunning', voting_dict))
print("Mikulski and Cantwell   :", policy_compare('Mikulski', 'Cantwell', voting_dict))
print("Mikulski and Murray     :", policy_compare('Mikulski', 'Murray', voting_dict))
print("=================================================")
print()


# For sentor: sen, policy_compares all senators with a different name
# return dictionary {compare_sum: Senator name}
# if more than one senator has same policy comparison, the last one compared is saved
def policy_compare_dict(sen, voting_dict):
    """ output in the form: e.g., for Obama
              { policySimilarity: Senator-A, policySimilarity: senator-B ...}
    """
    return {policy_compare(sen, s, voting_dict): s for s in voting_dict.keys() if s != sen}


def policy_compare_tuple(sen, voting_dict):
    """ output in the form, e.g., for Obama
           [ (policySimilarity, senator-A), (policySimilarity, senator-B), ... ]
    """    
    return [(policy_compare(sen, s, voting_dict), s) for s in voting_dict.keys() if s != sen]


def policy_compare_vector(sen, voting_dict):
    """ outout in the form, e.g., for Obama
          [policySimilarity_forSenator-A, policySimilarity_forSenator-B, ... ]
    """
    return [policy_compare(sen, s, voting_dict) for s in voting_dict.keys() if s != sen]


#
# Task 2.12.3
#    returns a list [number, name]
def most_similar(sen, e_dict):
    sens = e_dict.keys()
    r = [-1, '']
    for s in sens:
        if s != sen:
            p = policy_compare(sen, s, e_dict)
            if p > r[0]:
                r[1] = s
                r[0] = p
    return r

#
# Task 2.12.3 (V2: more compact solution)
#    returns a list [number, name]
def most_similar_v2(sen, e_dict):    # short hand
    pv = policy_compare_dict(sen, e_dict)
    m = max(pv.keys())
    return [m, pv[m]]

# remember: the resulting number is the same, but names may be different (not unique)
assert most_similar("Obama", voting_dict)[0] == most_similar_v2("Obama", voting_dict)[0]
assert most_similar("McCain", voting_dict)[0] == most_similar_v2("McCain", voting_dict)[0]
assert most_similar("Lincoln", voting_dict)[0] == most_similar_v2("Lincoln", voting_dict)[0]
assert most_similar("Cantwell", voting_dict)[0] == most_similar_v2("Cantwell", voting_dict)[0]


# Returns the set of senators all with same max
def most_similar_set(sen, e_dict):
    m = max(policy_compare_dict(sen, e_dict))
    pt = policy_compare_tuple(sen, e_dict)
    return [m, [n for (v, n) in pt if v == m]]

# l: [policy_similarity, name]
def print_most_similar(l):
    print(f'             Most similar: Policy similarity={l[0]:2d}')
    print(f'                           Senator: {l[1]:12}')

# l: [policy_similarity, [list of names]]
def print_similar_set(msg, l):
    print(f'            {msg:5} similar: Policy similarity={l[0]:2d}')
    print(f'            {msg:5} similar senator set (size={len(l[1]):1d}):', end='')
    for i in l[1]:
        print(' ', i, end='')
    print()
    

print("============================================")
print("(D): Testing Task 2.12.3 Most simliar set: Total votes=", total_vote_count)
dump_senator('Obama')
#print_most_similar(most_similar("Obama", voting_dict))
print_similar_set(" Most", most_similar_set("Obama", voting_dict))
print()
dump_senator('McCain')
#print_most_similar(most_similar("McCain", voting_dict))
print_similar_set(" Most", most_similar_set("McCain", voting_dict))
print()
dump_senator('Lincoln')
#print_most_similar(most_similar("Lincoln", voting_dict))
print_similar_set(" Most", most_similar_set("Lincoln", voting_dict))
print()
dump_senator('Santorum')
#print_most_similar(most_similar("Santorum", voting_dict))
print_similar_set(" Most", most_similar_set("Santorum", voting_dict))
print()
dump_senator('Cantwell')
#print_most_similar(most_similar("Cantwell", voting_dict))
print_similar_set(" Most", most_similar_set("Cantwell", voting_dict))
print()
dump_senator('Murray')
#print_most_similar(most_similar("Murray", voting_dict))
print_similar_set(" Most", most_similar_set("Murray", voting_dict))
print("=================================================")
print()

#
# Task 2.12.4
#    returns a list [number, name]
#    more compact solution
def least_similar(sen, e_dict):    # short hand
    pv = policy_compare_dict(sen, e_dict)
    m = min(pv.keys())
    return [m, pv[m]]


def least_similar_set(sen, e_dict):
    m = min(policy_compare_dict(sen, e_dict))
    pt = policy_compare_tuple(sen, e_dict)
    return [m, [n for (v, n) in pt if v == m]]

print("============================================")
print("(E): Testing Task 2.12.4: Least simliar set: Total votes=", total_vote_count)
dump_senator('Obama')
# print("Obama least similar:", least_similar("Obama", voting_dict))
print_similar_set("Least", least_similar_set("Obama", voting_dict))
print()
dump_senator('McCain')
# print("McCain least similar:", least_similar("McCain", voting_dict))
print_similar_set("Least", least_similar_set("McCain", voting_dict))
print()
dump_senator('Lincoln')
# print("Lincoln(AR) least similar:", least_similar("Lincoln", voting_dict))
print_similar_set("Least", least_similar_set("Lincoln", voting_dict))
print()
dump_senator('Santorum')
# print("Santorum(PA) least similar:", least_similar("Santorum", voting_dict))
print_similar_set("Least", least_similar_set("Santorum", voting_dict))
print()
dump_senator('Cantwell')
# print("Cantwell least similar:", least_similar("Cantwell", voting_dict))
print_similar_set("Least", least_similar_set("Cantwell", voting_dict))
print()
dump_senator('Murray')
# print("Murray least similar:", least_similar("Murray", voting_dict))
print_similar_set("Least", least_similar_set("Murray", voting_dict))
print("=================================================")
print("")

# Task 
# return average for _all_ senators
def find_average_similarity(e_dict):
    all_sen = e_dict.keys()
    total_num = len(all_sen)-1 # minus the senator her/him self
    return {i: sum(policy_compare_vector(i, e_dict)) / total_num for i in all_sen}


def highest_avg(s_dict, p_dict, e_dict):
    avg_of_all = find_average_similarity(e_dict)
    m = max(avg_of_all.values())
    return [m, [(a, p_dict[a], s_dict[a]) for a in avg_of_all.keys() if avg_of_all[a] == m ]]


def lowest_avg(s_dict, p_dict, e_dict):
    avg_of_all = find_average_similarity(e_dict)
    m = min(avg_of_all.values())
    return [m, [(a, p_dict[a], s_dict[a]) for a in avg_of_all.keys() if avg_of_all[a] == m ]]


def highest_avg_by_party(party, s_dict, p_dict, e_dict):
    avg_of_all = find_average_similarity(e_dict)
    avg_of_party = {n: avg_of_all[n] for n in avg_of_all.keys() if p_dict[n] == party}
    m = max(avg_of_party.values())
    return [m, [(a, p_dict[a], s_dict[a]) for a in avg_of_party.keys() if avg_of_party[a] == m]]


def lowest_avg_by_party(party, s_dict, p_dict, e_dict):
    avg_of_all = find_average_similarity(e_dict)
    avg_of_party = {n: avg_of_all[n] for n in avg_of_all.keys() if p_dict[n] == party}
    m = min(avg_of_party.values())
    return [m, [(a, p_dict[a], s_dict[a]) for a in avg_of_party.keys() if avg_of_party[a] == m]]


# l: [avg nubmer, [(Name, Party, State), ...]]
def print_avg(msg, l):
    print(f'{msg}: {l[0]:5.2f}')
    for i in l[1]:
        print(f'       Senator: {i[0]:12}  from State:{i[2]:2}   Party:{i[1]}')
        
print("")
print("Following are not part of our assignment, just for fun ...")
print("Highest averages:")
print("=================")
print_avg("Highest average policy similarities", highest_avg(state_dict, party_dict, voting_dict))
print("")
print_avg("Highest average Democratic Senators", highest_avg_by_party('D', state_dict, party_dict, voting_dict))
print("")
print_avg("Highest average Republican Senators", highest_avg_by_party('R', state_dict, party_dict, voting_dict))
print("==================================")
print("")
print("Lowest averages:")
print("================")
print_avg("Lowest average policy similarities", lowest_avg(state_dict, party_dict, voting_dict))
print("")
print_avg("Lowest average Democratic Senators", lowest_avg_by_party('D', state_dict, party_dict, voting_dict))
print("")
print_avg("Lowest average Republican Senators", lowest_avg_by_party('R', state_dict, party_dict, voting_dict))
print("==================================")
print("")


def rival_dict(e_dict):
    return {n: least_similar_set(n, e_dict) for n in e_dict.keys()}


def friend_dict(e_dict):
    return {n: most_similar_set(n, e_dict) for n in e_dict.keys()}

def worst_rival(r_dict):
    rival_score = min([v[0] for v in r_dict.values()])
    return [(n, rival_score, r_dict[n][1]) for n in r_dict.keys() if rival_score == r_dict[n][0]]


def best_friend(f_dict):
    f_score = max([v[0] for v in f_dict.values()])
    return [(n, f_score, f_dict[n][1]) for n in f_dict.keys() if f_score == f_dict[n][0]]


# name: senator
# rival: [rival names]
def print_one_rival(name, rivals):
    print(f'          {name:12}:', end='')
    for i in rivals:
        print(' ', i, end='')
    print()
    
    
# l: [(name, policy similarity, [names ...]), (...)]
def print_rival(msg, l):
    print(f'{msg}: policy similarities={l[0][1]:5.2f}')
    for i in l:
        print_one_rival(i[0], i[2])


r = rival_dict(voting_dict)  # name: [vote, [name1, name2]
f = friend_dict(voting_dict)

print("=================================")
print("Rivals and friends:")
print("===================")
print_rival("Worst Rivals", worst_rival(r))
print("")
print_rival("Best Friends", best_friend(f))
