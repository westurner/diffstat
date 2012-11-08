
from pandas import read_csv

def read_hg_csv(filename='./log.txt'):
    df = read_csv(filename,sep='\|\|\|',index_col='rev')
    df['fileschanged'] = df['diffstat'].apply(lambda x: int(x.split(':')[0]))
    df['added'] = df['diffstat'].apply(lambda x: int(x.split(':')[1].split('/')[0].strip()[1:]))
    df['removed'] = df['diffstat'].apply(lambda x: int(x.split(':')[1].split('/')[1].strip()[1:]))
    return df


from collections import OrderedDict

stats = OrderedDict()

def print_stats_dict(d, name):
    print("#"*20, name, '#'*20)
    for (k,v) in d.iteritems():
        print('#'*10, k, '#'*10)
        print(v)

def do_stats(df):

    commit_stats = OrderedDict()

    commit_stats['most_fileschanged'] = df.ix[df['fileschanged'].argmax()]
    commit_stats['most_added'] = df.ix[df['added'].argmax()]
    commit_stats['most_removed'] = df.ix[df['removed'].argmax()]
    stats['commits'] = commit_stats

    print_stats_dict(commit_stats, 'commit_stats')

    repo_norms = OrderedDict()
    repo_norms['fileschanged'] = df['fileschanged'].describe()
    repo_norms['added'] = df['added'].describe()
    repo_norms['removed'] = df['removed'].describe()
    stats['repo_norms'] = repo_norms

    print_stats_dict(repo_norms, 'repo_norms')
    return stats

if __name__=="__main__":
    df = read_hg_csv()
    do_stats(df)
