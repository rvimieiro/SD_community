import pandas as pd
import numpy as np
import re
import time


def evaluateRule(rule, example):
    return all(map(lambda x: example[x[0]]==x[1], rule[0]))

def Qg(rule,df,target='community'):    
    examples = df.apply(lambda x: evaluateRule(rule,x), axis=1)
    tp = np.sum(df.loc[examples,target]==int(rule[1]))
    fp = np.sum(examples) - tp
#    print(tp,fp,np.argwhere(examples))
    return tp/(fp+1.0)


def permutation_test(rule,matrix,target='community',repetition=1000,seed=time.time()):
    np.random.seed(int(seed))    
    df = matrix.copy()
    def randomtest(i):        
        df.loc[:,target] = np.random.permutation(df[target])     
        return Qg(rule,df,target)
    return np.fromfunction(np.vectorize(randomtest),shape=(repetition,))


if __name__ == '__main__':
	regex_regra = re.compile('{(.*?)}->(\w+)')
	regex_feat_value = re.compile('([\w\s]+)=([\w\s]+),?')

	with open('regras_freq_top10qg_stem.txt') as f:    
	    regras = [regex_regra.match(a).groups() for a in f]
	    regras = [(regex_feat_value.findall(cond),target) for cond,target in regras]

	freq_matrix = pd.read_csv('doc_term_matrix_freq_discrete.csv')


	with open('random_test_freq.csv','w') as f:
	    pvalue = []
	    rep=1000
	    for rule in regras:
	        a = permutation_test(rule,freq_matrix,repetition=rep,seed=0)
	        f.write(','.join(map(lambda x: '{0:.3g}'.format(x),a)))
	        f.write('\n')        
	        f.flush()
	        qg = Qg(rule,freq_matrix)
	        pvalue.append((np.sum(a>qg)+1)/(rep+1.0))
	print(','.join(map(lambda x: '{0:5e}'.format(x),pvalue)))

