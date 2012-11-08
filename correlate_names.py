#!/usr/bin/env python
"""
disambiguate SCM commit authors
"""
import re
import networkx
from collections import OrderedDict
from itertools import ifilter
from itertools import imap
from itertools import combinations_with_replacement

scm_name_regex = re.compile(r'(.*)[\s]+<(.*)>') # TODO: more fuzzy
def split_scm_name(n):
    if '@' in n: # probably contains email
        if '<' in n:
            match = scm_name_regex.match(n) #n.split('<')
            name,email = match and match.groups() or (n, None)
        else:
            email = n # TODO
            name = None
    else:
        email = None
        name = n
    return (name,email)


def score_match(username1, username2):
    name1, email1 = split_scm_name(username1) # TODO: memoize
    name2, email2 = split_scm_name(username2)
    email1 = email1 and email1.lower()
    email2 = email2 and email2.lower()

    scores = OrderedDict()
    if name1 and name2:
        if name1 == name2:
            scores['name:match'] = 5 #
        elif name1.lower() == name2.lower():
            scores['name_lower:match'] = 4

    if email1 and email2:
        if email1 == email2:
            scores['emails:match'] = 100
        elif email1.split('@')[0] == email2.split('@')[0]:
            scores['email_username:match'] = 3

    # TODO: string distance

    return sum(scores.values())


def build_namepair_edges(names):
    namepairs = combinations_with_replacement(names, 2)
    return ((p, score_match(*p)) for p in namepairs)


def build_name_graph(names, threshold=5):
    g = networkx.Graph()
    g.add_nodes_from(names)
    for k,v in ifilter(
            lambda item: item[1] > threshold,
                build_namepair_edges(names)):
        #print(k, v)
        g.add_edge(*k, weight=v)

    return g


def find_components(g):
    return ifilter(lambda s: len(s)>1,
        networkx.strongly_connected_components(g))


def read_hg_repo_graph():
    from hgrepostats import read_hg_csv
    df = read_hg_csv()
    names = sorted(df.groupby(df['author']).groups.keys())
    return build_name_graph(names, 5)


def main():
    g = read_hg_repo_graph()
    for s in sorted( find_components(g) ):
        print(len(s), s)


if __name__=="__main__":
    main()
