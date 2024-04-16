from main import *

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        dist, S_aligned, T_aligned = fast_align_MED(S, T)
        assert (S_aligned[0] == alignments[i][0] and T_aligned[0] == alignments[i][1])

