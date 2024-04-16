import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    if (S, T) in MED:
      return MED[(S, T)]
    if not S:
      return len(T)
    elif not T:
      return len(S)
    else:
      if S[0] == T[0]:
          MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
      else:
          MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED), fast_MED(S[1:], T[1:], MED))
      return MED[(S, T)]

def fast_align_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]
  if not S:
    return len(T), "-" * len(T), T
  elif not T:
    return len(S), S, "-" * len(S)
  else:
    if S[0] == T[0]:
        dist, S_aligned, T_aligned = fast_align_MED(S[1:], T[1:], MED)
        MED[(S, T)] = dist, S[0] + S_aligned, T[0] + T_aligned
    else:
        ins_dist, ins_S_aligned, ins_T_aligned = fast_align_MED(S, T[1:], MED)
        del_dist, del_S_aligned, del_T_aligned = fast_align_MED(S[1:], T, MED)
        sub_dist, sub_S_aligned, sub_T_aligned = fast_align_MED(S[1:], T[1:], MED)
        min_dist = min(ins_dist, del_dist, sub_dist)
        if min_dist == ins_dist:
            MED[(S, T)] = 1 + ins_dist, "-" + ins_S_aligned, T[0] + ins_T_aligned
        elif min_dist == del_dist:
            MED[(S, T)] = 1 + del_dist, S[0] + del_S_aligned, "-" + del_T_aligned
        else:
            MED[(S, T)] = 1 + sub_dist, S[0] + sub_S_aligned, T[0] + sub_T_aligned
    return MED[(S, T)]

