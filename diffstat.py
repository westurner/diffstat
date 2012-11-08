#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
diffstatvis
"""

import subprocess
def sh(cmd, *args, **kwargs):
    try:
        p = subprocess.Popen(cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        #stdout,stderr = p.communicate()
        #if p.returncode is not 0:
        #    raise Exception(
        #            '%r exited with status %d: %r' %
        #                (cmd, p.returncode, stderr))
        #return stdout.split('\n') # TODO
        return p.stdout
    except Exception, e:
        raise

from IPython.external.path import path
def sniff_repository_type(_path):
    if (path(_path) / '.hg').exists():
        return 'hg'
    if (path(_path) / '.git').exists():
        return 'git'
    if (path(_path) / '.svn').exists():
        return 'svn'
    raise NotImplementedError("unabled to determine repository type")

# note: gaps are not handled
hg_diffstat_modes = {
    'minutely': '%Y-%m-%d.%H:%M',
    'hourly': '%Y-%m-%d.%H',
    'daily': '%Y-%m-%d',
    'monthly': '%Y-%m',
    'yearly': '%Y'
}

def diffstat_hg(path, mode='daily', revset=None):
    cmd = ('hg','churn',
            '-f', hg_diffstat_modes[mode],
            '-s',
            '--diffstat',
            '-R', path)
    # XXX: should this be a mercurial extension [to churn]?
    for line in sh(cmd, cwd=path):
        if line:
            label,changes = line.split(None,1)
            added,removed = changes.split()[0].split('/',1)
            yield (label,added[1:],removed[1:])

def diffstat_git(path, revset=None):
    cmd = ('git', '...')
    # TODO
    for line in sh(cmd, cwd=path):
        # TODO
        label = adds = removes = None
        yield (label, adds, removes)

diffstat_funcs = {
    'hg': diffstat_hg,
    'git': diffstat_git,
}

try:
    import simplejson as json
except ImportError:
    import json
def diffstat_to_json(iterable):
    iterable = list(enumerate(iterable))
    data = [
        list(dict(x=i,y=int(a),label=l) for (i,(l,a,r)) in iterable if l),
        list(dict(x=i,y=int(r),label=l) for (i,(l,a,r)) in iterable if l),
    ]
    return json.dumps(data)

from string import Template

def diffstatvis(repo_path, repo_type=None, launchbrowser=False):
    """
    generate a streamgraph from a repository log
    """
    repo_type = repo_type or sniff_repository_type(repo_path)
    diffstat_func = diffstat_funcs[repo_type]
    data = diffstat_to_json( diffstat_func(repo_path) )

    title = repo_path # TODO
    tmpl = Template(open('./stack_tmpl.html','r').read())
    output_path = './diffstat_id-xyz.html' # TODO
    with open(output_path,'w') as f:
        f.write(tmpl.substitute(data=data, title=title))
    if launchbrowser:
        subprocess.call(('sensible-browser', output_path))


import unittest
class Test_diffstatvis(unittest.TestCase):
    def test_diffstatvis(self):
        pass

    def test_diffstat_hg(self):
        for l in diffstat_hg('/home/wturner/workspace/hours/src/workhours'):
            print(l)


def main():
    import optparse
    import logging

    prs = optparse.OptionParser(usage="./%prog : args")

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true',)
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true',)
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true',)

    (opts, args) = prs.parse_args()

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        import sys
        sys.argv = [sys.argv[0]] + args
        import unittest
        exit(unittest.main())

    diffstatvis(len(args) and args[0] or '.')

if __name__ == "__main__":
    main()
