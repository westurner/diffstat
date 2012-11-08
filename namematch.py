# IPython log file

from hgrepostats import read_hg_csv
df = read_hg_csv()
df
df['tags']
col = df['tags']
col[not col.isnull()]
get_ipython().magic(u'pinfo col.any')
get_ipython().magic(u'pinfo df.any')
get_ipython().magic(u'pinfo df.dropna')
df2=df.dropna()
df2
get_ipython().magic(u'pinfo df.groupby')
df.groupby(df['author'],as_index=False)
get_ipython().magic(u'pinfo df.groupby')
df.groupby(df['author'],as_index=False).groups
df.groupby(df['author']).groups
grouped = df.groupby(df['author'])
for name,group in grouped:
    print name
    print group

df.groupby(df['author']).groups.keys()
df.groupby(df['author']).groups.keys().sort()
sorted(df.groupby(df['author']).groups.keys())
get_ipython().system(u'pip install jellyfish')
import jellyfish
from itertools import product
names = sorted(df.groupby(df['author']).groups.keys())
namepairs = product(names, names)
namepairs = list(product(names, names))
# TODO: cominations
namepairs
from itertools import combinations,permutations
get_ipython().magic(u'pinfo combinations')
get_ipython().magic(u'pinfo permutations')
from itertools import combinations_with_replacement
get_ipython().magic(u'pinfo combinations_with_replacement')
get_ipython().magic(u'pinfo combinations')
combinations(names, 2)
list(combinations(names, 2))
def matching_algo(names):
    for n in names:
        if '@' in n: # probably contains email
            if '<' in n:
                name,email = n.split('<') # TODO: regex
            else:
                email = n
                name = None
        else:
            email = None
            name = n
        yield (name,email)

names
list(matching_algo(names))
name_emails = list(matching_algo(names))
get_ipython().system(u'pip install networkx')
from networkx import MultiGraph
get_ipython().magic(u'pinfo MultiGraph')
name_emails
def score_match(name1, email1, name2, email2):
    if name1 == name2:
        if email1 == email2:
            return 100
        if email1.split('@')[0] == email2.split('@')[1]:
            return 95
        else:
            return 20
    if email1 == email2:
        return 1000
    if email1.split('@')[0] == email2.split('@')[0]:
        return 5
    if name1.lower() == name2.lower():
        return -1 # should be additive match weights

get_ipython().magic(u'logstart namematch.py')
