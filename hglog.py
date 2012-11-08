# IPython log file

from pandas import read_csv
df = read_csv('./log.txt',sep='\|\|\|')
df
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 0 to 16663
#[Out]# Data columns:
#[Out]# n            16664  non-null values
#[Out]# node         16664  non-null values
#[Out]# author       16664  non-null values
#[Out]# changestr    16664  non-null values
#[Out]# dtypes: int64(1), object(3)
df[0]
df = read_csv('./log.txt',sep='\|\|\|',index_col='n')
df
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 16663 to 0
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df[0]
df[1]
df
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 16663 to 0
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df['node']
#[Out]# n
#[Out]# 16663    43c6b542c85c
#[Out]# 16662    e78ebfbbd72d
#[Out]# 16661    51064efff902
#[Out]# 16660    ba5d77da40df
#[Out]# 16659    000d427d9340
#[Out]# 16658    01eb88248937
#[Out]# 16657    ccde69ab6a7a
#[Out]# 16656    a63f8502d7e6
#[Out]# 16655    7efdea341ab2
#[Out]# 16654    d1a0ac9b6b8a
#[Out]# 16653    0fdd8193c8b5
#[Out]# 16652    d9238286964e
#[Out]# 16651    a2d6e336e9cc
#[Out]# 16650    51932c835b74
#[Out]# 16649    15159abc5ab6
#[Out]# ...
#[Out]# 14    e0e5c1b9febd
#[Out]# 13    eb87b7dc4236
#[Out]# 12    8b64243ee17b
#[Out]# 11    7f16aaeed62f
#[Out]# 10    e76ed1e480ef
#[Out]# 9     b4d0c3786ad3
#[Out]# 8     e5a480dadca3
#[Out]# 7     510265b68bbf
#[Out]# 6     207fa2778d65
#[Out]# 5     5f249577ac40
#[Out]# 4     ce3bd728b858
#[Out]# 3     3a6392190075
#[Out]# 2     ecf3fd948051
#[Out]# 1     273ce12ad8f1
#[Out]# 0     9117c6561b0b
#[Out]# Name: node, Length: 16664
df['author']
#[Out]# n
#[Out]# 16663                         Wes Turner <wes@wrd.nu>
#[Out]# 16662                         Wes Turner <wes@wrd.nu>
#[Out]# 16661                         Wes Turner <wes@wrd.nu>
#[Out]# 16660                         Wes Turner <wes@wrd.nu>
#[Out]# 16659                         Wes Turner <wes@wrd.nu>
#[Out]# 16658     Martin Schröder <martinschroeder@vcp-sh.de>
#[Out]# 16657     Martin Schröder <martinschroeder@vcp-sh.de>
#[Out]# 16656     Martin Schröder <martinschroeder@vcp-sh.de>
#[Out]# 16655    Wagner Bruna <wbruna@softwareexpress.com.br>
#[Out]# 16654           Adrian Buehlmann <adrian@cadifra.com>
#[Out]# 16653               David Champion <dgc@uchicago.edu>
#[Out]# 16652                  Matt Mackall <mpm@selenic.com>
#[Out]# 16651            Alexander Boyd <alex@opengroove.org>
#[Out]# 16650     Thomas Arendsen Hein <thomas@intevation.de>
#[Out]# 16649                  Matt Mackall <mpm@selenic.com>
#[Out]# ...
#[Out]# 14              mpm@selenic.com
#[Out]# 13              mpm@selenic.com
#[Out]# 12              mpm@selenic.com
#[Out]# 11    oxymoron@cinder.waste.org
#[Out]# 10    oxymoron@cinder.waste.org
#[Out]# 9               mpm@selenic.com
#[Out]# 8               mpm@selenic.com
#[Out]# 7               mpm@selenic.com
#[Out]# 6               mpm@selenic.com
#[Out]# 5               mpm@selenic.com
#[Out]# 4               mpm@selenic.com
#[Out]# 3               mpm@selenic.com
#[Out]# 2               mpm@selenic.com
#[Out]# 1               mpm@selenic.com
#[Out]# 0               mpm@selenic.com
#[Out]# Name: author, Length: 16664
df.groupby('author')
#[Out]# <pandas.core.groupby.DataFrameGroupBy object at 0x9cc73ec>
_12.keys
#[Out]# 'author'
_12.ngroups
#[Out]# 589
_12
#[Out]# <pandas.core.groupby.DataFrameGroupBy object at 0x9cc73ec>
from pandas import DataFrame
DataFrame(_12)
_12
#[Out]# <pandas.core.groupby.DataFrameGroupBy object at 0x9cc73ec>
list(_12)
#[Out]# [('"Andrei Vermel <avermel@mail.ru>"',               node                             author changestr
#[Out]# n                                                              
#[Out]# 4134  a33ddd20105c  "Andrei Vermel <avermel@mail.ru>"  1: +9/-3
#[Out]# 4075  28cbe9e01f17  "Andrei Vermel <avermel@mail.ru>"  1: +9/-3), ('"Aurelien Jacobs <aurel@gnuage.org>"',               node                                author changestr
#[Out]# n                                                                 
#[Out]# 2589  dc63db82b530  "Aurelien Jacobs <aurel@gnuage.org>"  1: +6/-6
#[Out]# 2296  6e8e3dd7976e  "Aurelien Jacobs <aurel@gnuage.org>"  1: +4/-4), ('"Daniel Santa Cruz <byteshack@gmail.com>"',               node                                     author changestr
#[Out]# n                                                                      
#[Out]# 2430  4ccd71b83d5e  "Daniel Santa Cruz <byteshack@gmail.com>"  1: +3/-0), ('"Daniel Santa Cruz <dansan@vikus.com>"',               node                                  author changestr
#[Out]# n                                                                   
#[Out]# 2338  391c5d0f9ef3  "Daniel Santa Cruz <dansan@vikus.com>"  1: +1/-1), ('"Hidetaka Iwai  <tyuyu@debian.or.jp>"',               node                                 author    changestr
#[Out]# n                                                                     
#[Out]# 1489  a64fdaf60f9d  "Hidetaka Iwai  <tyuyu@debian.or.jp>"  5: +1712/-0), ('"Hiroshi Funai" <hfunai@gmail.com>',               node                              author   changestr
#[Out]# n                                                                 
#[Out]# 7120  c9b88695d894  "Hiroshi Funai" <hfunai@gmail.com>  1: +461/-0), ('"Mathieu Clabaut <mathieu.clabaut@gmail.com>"',               node                                         author     changestr
#[Out]# n                                                                              
#[Out]# 2773  871ca5b9d348  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"    2: +54/-20
#[Out]# 2695  c995d68333cf  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"      1: +6/-1
#[Out]# 2694  0fb28dbf0dc7  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"   4: +125/-29
#[Out]# 2692  2ab464771b7d  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"      1: +2/-0
#[Out]# 2677  ec05ce9cbf47  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"     1: +10/-2
#[Out]# 2675  d99a92b7acad  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"      1: +3/-0
#[Out]# 2637  fcfd46c4a27a  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"     1: +10/-5
#[Out]# 2636  733fff9b23f7  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"    1: +28/-28
#[Out]# 2635  37bcccf8a683  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"      1: +1/-1
#[Out]# 2634  105708ba518f  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"     1: +11/-7
#[Out]# 2633  f7be7babc75a  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"      0: +0/-0
#[Out]# 2607  070736e20dfd  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"     1: +10/-6
#[Out]# 2606  5cef1a92aa04  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"      1: +6/-3
#[Out]# 2605  4ad79eeebf96  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"     1: +0/-10
#[Out]# 2604  d93c23b31797  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"  1: +427/-728
#[Out]# 2603  f80057407c07  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"  2: +720/-568
#[Out]# 2592  457846f400e8  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"  2: +665/-837
#[Out]# 2591  61f2008cd6bf  "Mathieu Clabaut <mathieu.clabaut@gmail.com>"   3: +2031/-0), ('"Paul Moore <p.f.moore@gmail.com>"',               node                              author  changestr
#[Out]# n                                                                
#[Out]# 6632  479847ccabe0  "Paul Moore <p.f.moore@gmail.com>"  1: +17/-2), ('"Peter Arrenbrecht" <peter.arrenbrecht@gmail.com>',               node                                             author changestr
#[Out]# n                                                                              
#[Out]# 6309  7240204121af  "Peter Arrenbrecht" <peter.arrenbrecht@gmail.com>  1: +1/-0), ('"Rafael Villar Burke <pachi@rvburke.com>"',               node                                     author changestr
#[Out]# n                                                                      
#[Out]# 5483  07bdb5e5d08c  "Rafael Villar Burke <pachi@rvburke.com>"  1: +9/-7), ('"Shun-ichi GOTO" <shunichi.goto@gmail.com>',               node                                      author changestr
#[Out]# n                                                                       
#[Out]# 5884  07ca22a72dcc  "Shun-ichi GOTO" <shunichi.goto@gmail.com>  1: +3/-1), ('"Wallace, Eric S" <eric.s.wallace@intel.com>',              node                                        author changestr
#[Out]# n                                                                        
#[Out]# 827  a61728b58dc0  "Wallace, Eric S" <eric.s.wallace@intel.com>  1: +2/-1), ('"Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>',                node                                             author    changestr
#[Out]# n                                                                                  
#[Out]# 15532  1f677c7e494d  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>     1: +1/-1
#[Out]# 15166  143c78b4fc8c  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>   2: +140/-0
#[Out]# 15165  f4a8d754cd0a  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>   3: +133/-0
#[Out]# 15164  aa2e908c521e  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>    1: +29/-0
#[Out]# 15163  fa0a464e4ca5  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>  3: +118/-19
#[Out]# 15157  395ca8cd2669  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>    4: +53/-0
#[Out]# 15156  b39d85be78a8  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>   3: +90/-58
#[Out]# 15149  0834e0bb445a  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>    1: +46/-0
#[Out]# 15148  883d28233a4d  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>    3: +59/-0
#[Out]# 15147  91f93dcd72aa  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>    3: +53/-0
#[Out]# 15146  18219c0789ae  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>   3: +113/-2
#[Out]# 15145  f19de58af225  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>    2: +15/-7
#[Out]# 15144  81adf7777f8f  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>    2: +20/-5
#[Out]# 15143  b1c62c754bf8  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>     1: +1/-1
#[Out]# 15047  3709cca378ff  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>     1: +7/-2
#[Out]# 14393  51f444e85734  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>     1: +1/-1
#[Out]# 14392  a599431b0ab6  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>     1: +4/-2
#[Out]# 14391  be0daa0eeb3e  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>    2: +10/-8
#[Out]# 12087  66521d25c2a6  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>     1: +1/-1
#[Out]# 12086  6e3875a80533  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>    3: +34/-1
#[Out]# 12085  22f1994fb669  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>   1: +18/-15
#[Out]# 12065  7d2ea5ce4aac  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>    3: +66/-0
#[Out]# 12064  b8b1e6e78486  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>     1: +3/-1
#[Out]# 11924  dc5ce9c95d00  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>    1: +11/-0
#[Out]# 11923  9b771b4ce2f3  "Yann E. MORIN" <yann.morin.1998@anciens.enib.fr>     3: +7/-1), ('"Yann E. MORIN" <yann.morin.1998@free.fr>',                node                                     author  changestr
#[Out]# n                                                                        
#[Out]# 16323  db68ee3289b6  "Yann E. MORIN" <yann.morin.1998@free.fr>  2: +18/-0
#[Out]# 16322  684864d54903  "Yann E. MORIN" <yann.morin.1998@free.fr>   1: +7/-2
#[Out]# 16310  eb39bbda167b  "Yann E. MORIN" <yann.morin.1998@free.fr>   1: +4/-2), ('A. S. Budden <abudden@gmail.com>',                node                            author     changestr
#[Out]# n                                                                  
#[Out]# 16564  770190bff625  A. S. Budden <abudden@gmail.com>      2: +4/-1
#[Out]# 16353  46b991a1f428  A. S. Budden <abudden@gmail.com>  7: +324/-117
#[Out]# 16315  95e45abe7e8e  A. S. Budden <abudden@gmail.com>      1: +7/-0), ('Aaron Digulla <digulla@hepe.com>',                node                            author   changestr
#[Out]# n                                                                
#[Out]# 10770  46bb49134498  Aaron Digulla <digulla@hepe.com>  1: +67/-64), ('Abderrahim Kitouni <a.kitouni@gmail.com>',               node                                    author changestr
#[Out]# n                                                                     
#[Out]# 9237  9aebeea7ac00  Abderrahim Kitouni <a.kitouni@gmail.com>  1: +5/-6
#[Out]# 8727  353b1c160c2d  Abderrahim Kitouni <a.kitouni@gmail.com>  1: +4/-4), ('Adam Hupp <adam@hupp.org>',               node                     author   changestr
#[Out]# n                                                        
#[Out]# 5598  40a06e39f010  Adam Hupp <adam@hupp.org>  2: +212/-0), ('Adam Spiers <hg@adamspiers.org>',               node                           author  changestr
#[Out]# n                                                             
#[Out]# 4916  cc7a43af709d  Adam Spiers <hg@adamspiers.org>   1: +1/-0
#[Out]# 4915  6def53be19fb  Adam Spiers <hg@adamspiers.org>   1: +1/-1
#[Out]# 4914  e5e6dd8ba6bb  Adam Spiers <hg@adamspiers.org>  1: +13/-0
#[Out]# 4913  620cea146b19  Adam Spiers <hg@adamspiers.org>   2: +8/-5
#[Out]# 4912  cc0fb3500dd5  Adam Spiers <hg@adamspiers.org>  1: +25/-1
#[Out]# 4910  87a35bb58b88  Adam Spiers <hg@adamspiers.org>   1: +1/-1), ('Adrian Buehlmann <adrian at cadifra.com>',               node                                    author  changestr
#[Out]# n                                                                      
#[Out]# 6717  944a292d522a  Adrian Buehlmann <adrian at cadifra.com>  1: +16/-0), ('Adrian Buehlmann <adrian@cadifra.com>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 326 entries, 16654 to 6338
#[Out]# Data columns:
#[Out]# node         326  non-null values
#[Out]# author       326  non-null values
#[Out]# changestr    326  non-null values
#[Out]# dtypes: object(3)), ('Afuna',                node author  changestr
#[Out]# n                                    
#[Out]# 13399  eff102facb15  Afuna  1: +19/-2
#[Out]# 13398  661331407163  Afuna   1: +4/-2), ('Afuna <afunamatata@gmail.com>',                node                         author  changestr
#[Out]# n                                                            
#[Out]# 13047  69238d0ca60f  Afuna <afunamatata@gmail.com>  2: +53/-5), ('Alain  Leufroy <alain.leufroyATgmailMYDOTcom>',                node                                         author     changestr
#[Out]# n                                                                               
#[Out]# 15992  963c8a553524  Alain  Leufroy <alain.leufroyATgmailMYDOTcom>     2: +14/-1
#[Out]# 15991  85ec8036d0b9  Alain  Leufroy <alain.leufroyATgmailMYDOTcom>     2: +14/-1
#[Out]# 15917  e66084ef8449  Alain  Leufroy <alain.leufroyATgmailMYDOTcom>  8: +245/-122), ('Alain Leufroy <alain.leufroy@logilab.fr>',                node                                    author   changestr
#[Out]# n                                                                        
#[Out]# 16442  9dd10a574af2  Alain Leufroy <alain.leufroy@logilab.fr>    1: +4/-1
#[Out]# 16441  692bf06bb1af  Alain Leufroy <alain.leufroy@logilab.fr>    1: +1/-0
#[Out]# 15918  4f9853e7f690  Alain Leufroy <alain.leufroy@logilab.fr>  1: +31/-13), ('Alecs King <alecsk@gmail.com>',                node                         author  changestr
#[Out]# n                                                            
#[Out]# 12071  5094e6b2f640  Alecs King <alecsk@gmail.com>   1: +1/-1
#[Out]# 11967  d12fe809e1ee  Alecs King <alecsk@gmail.com>   1: +1/-1
#[Out]# 11966  e1359ad582f6  Alecs King <alecsk@gmail.com>   1: +6/-3
#[Out]# 11918  e27a0fa7ba59  Alecs King <alecsk@gmail.com>   1: +2/-1
#[Out]# 11616  d157e040ac4c  Alecs King <alecsk@gmail.com>  1: +10/-3
#[Out]# 612    9cd745437269  Alecs King <alecsk@gmail.com>  2: +23/-8), ('Aleix Conchillo Flaque <aleix@member.fsf.org>',               node                                         author    changestr
#[Out]# n                                                                             
#[Out]# 8177  1bef3656d9fe  Aleix Conchillo Flaque <aleix@member.fsf.org>     1: +9/-0
#[Out]# 6085  ea34059b89de  Aleix Conchillo Flaque <aleix@member.fsf.org>  4: +161/-10
#[Out]# 6084  ebc23d34102f  Aleix Conchillo Flaque <aleix@member.fsf.org>   4: +146/-1
#[Out]# 6061  a3d8b1f8721d  Aleix Conchillo Flaque <aleix@member.fsf.org>   1: +34/-18
#[Out]# 6055  348132c112cf  Aleix Conchillo Flaque <aleix@member.fsf.org>   2: +27/-18
#[Out]# 6050  9360a58a09e6  Aleix Conchillo Flaque <aleix@member.fsf.org>   1: +10/-10
#[Out]# 6043  dd3267698d84  Aleix Conchillo Flaque <aleix@member.fsf.org>     1: +7/-3
#[Out]# 6041  df659eb23360  Aleix Conchillo Flaque <aleix@member.fsf.org>   4: +278/-1), ('Alejandro Santos <alejolp@alejolp.com>',               node                                  author    changestr
#[Out]# n                                                                      
#[Out]# 9187  a232b90ffb51  Alejandro Santos <alejolp@alejolp.com>     1: +1/-1
#[Out]# 9186  32e678f9045f  Alejandro Santos <alejolp@alejolp.com>     2: +4/-3
#[Out]# 9185  8e34f363dd77  Alejandro Santos <alejolp@alejolp.com>     1: +4/-1
#[Out]# 9184  8429062de8d3  Alejandro Santos <alejolp@alejolp.com>     1: +5/-6
#[Out]# 9183  98a5652bfed9  Alejandro Santos <alejolp@alejolp.com>     1: +1/-1
#[Out]# 9182  1fa80c5428b8  Alejandro Santos <alejolp@alejolp.com>   6: +18/-31
#[Out]# 9181  3b76321aa0de  Alejandro Santos <alejolp@alejolp.com>  13: +23/-23
#[Out]# 9180  3f56055ff1d7  Alejandro Santos <alejolp@alejolp.com>     2: +2/-2
#[Out]# 9179  0001e49f1c11  Alejandro Santos <alejolp@alejolp.com>   5: +10/-10
#[Out]# 9178  bea567ae3ff6  Alejandro Santos <alejolp@alejolp.com>    1: +19/-1), ('Alex Unden <alu@zpuppet.org>',               node                        author  changestr
#[Out]# n                                                          
#[Out]# 7817  cb516e788238  Alex Unden <alu@zpuppet.org>  3: +19/-1), ('Alexander Boyd <alex@opengroove.org>',                node                                author changestr
#[Out]# n                                                                  
#[Out]# 16651  a2d6e336e9cc  Alexander Boyd <alex@opengroove.org>  1: +2/-1), ('Alexander Krauss <krauss@in.tum.de>',                node                               author  changestr
#[Out]# n                                                                  
#[Out]# 14966  a35d6f822e3e  Alexander Krauss <krauss@in.tum.de>  2: +22/-2
#[Out]# 14965  3db92e3948d5  Alexander Krauss <krauss@in.tum.de>   1: +2/-2
#[Out]# 14964  01e0091679c0  Alexander Krauss <krauss@in.tum.de>   1: +1/-1), ('Alexander Sauta <demosito@gmail.com>',                node                                author       changestr
#[Out]# n                                                                        
#[Out]# 16647  74abb39adef8  Alexander Sauta <demosito@gmail.com>        1: +4/-1
#[Out]# 16632  2478594b37c2  Alexander Sauta <demosito@gmail.com>      1: +39/-27
#[Out]# 16620  6253677114dd  Alexander Sauta <demosito@gmail.com>   1: +1561/-728
#[Out]# 16045  0f99e709ce08  Alexander Sauta <demosito@gmail.com>      1: +76/-30
#[Out]# 16034  312d215b013a  Alexander Sauta <demosito@gmail.com>       1: +47/-6
#[Out]# 16033  9d85384c1c93  Alexander Sauta <demosito@gmail.com>        1: +6/-4
#[Out]# 16006  0d898ebb424e  Alexander Sauta <demosito@gmail.com>      1: +82/-69
#[Out]# 15813  aceed923a1f8  Alexander Sauta <demosito@gmail.com>      1: +50/-20
#[Out]# 15811  a52e42e48e0e  Alexander Sauta <demosito@gmail.com>     1: +140/-95
#[Out]# 15810  0e3a2b71f29a  Alexander Sauta <demosito@gmail.com>     1: +120/-92
#[Out]# 15809  a6c8faa4a7d2  Alexander Sauta <demosito@gmail.com>     1: +309/-99
#[Out]# 15776  84bcc9e7d3f2  Alexander Sauta <demosito@gmail.com>    1: +452/-372
#[Out]# 15775  ea6940833d71  Alexander Sauta <demosito@gmail.com>     1: +211/-33
#[Out]# 15774  5fef00ce7409  Alexander Sauta <demosito@gmail.com>    1: +329/-214
#[Out]# 15773  2edd59f398dc  Alexander Sauta <demosito@gmail.com>     1: +189/-42
#[Out]# 15761  d56e9df61010  Alexander Sauta <demosito@gmail.com>     1: +143/-11
#[Out]# 15760  2e98875e3fa4  Alexander Sauta <demosito@gmail.com>     1: +121/-64
#[Out]# 15759  81d8d31b2b4c  Alexander Sauta <demosito@gmail.com>    1: +168/-138
#[Out]# 15758  4f5b16ad2e84  Alexander Sauta <demosito@gmail.com>     1: +252/-55
#[Out]# 15757  ad913b187621  Alexander Sauta <demosito@gmail.com>    1: +295/-268
#[Out]# 15722  78626e11f3c5  Alexander Sauta <demosito@gmail.com>    1: +228/-113
#[Out]# 15713  2cbc4c2838b0  Alexander Sauta <demosito@gmail.com>      1: +98/-38
#[Out]# 15712  7a61a1acecd0  Alexander Sauta <demosito@gmail.com>    1: +542/-292
#[Out]# 15711  34cb1fd2b3b9  Alexander Sauta <demosito@gmail.com>      1: +41/-38
#[Out]# 15690  912525f7b8e2  Alexander Sauta <demosito@gmail.com>    1: +704/-326
#[Out]# 15689  04425770d162  Alexander Sauta <demosito@gmail.com>   1: +1861/-553
#[Out]# 14919  4b85c6963748  Alexander Sauta <demosito@gmail.com>       1: +2/-14
#[Out]# 14918  b50d7510545a  Alexander Sauta <demosito@gmail.com>     1: +191/-19
#[Out]# 14917  68d1e4e5e0a4  Alexander Sauta <demosito@gmail.com>       1: +61/-7
#[Out]# 14913  a8663a3b72a0  Alexander Sauta <demosito@gmail.com>     1: +313/-19
#[Out]# 14912  7a7394f9171e  Alexander Sauta <demosito@gmail.com>     1: +186/-34
#[Out]# 14911  96383c8242a1  Alexander Sauta <demosito@gmail.com>      1: +56/-12
#[Out]# 14909  219273cc548d  Alexander Sauta <demosito@gmail.com>   1: +3268/-413
#[Out]# 14792  8c5a0d4377aa  Alexander Sauta <demosito@gmail.com>       1: +19/-8
#[Out]# 14791  5b7dc16b331b  Alexander Sauta <demosito@gmail.com>      2: +84/-69
#[Out]# 14787  5c046e4b9652  Alexander Sauta <demosito@gmail.com>       1: +45/-4
#[Out]# 14786  e40e9fe17840  Alexander Sauta <demosito@gmail.com>      1: +297/-3
#[Out]# 14783  9a6c497729e3  Alexander Sauta <demosito@gmail.com>     1: +238/-22
#[Out]# 14781  7f5a7bffc1f4  Alexander Sauta <demosito@gmail.com>     1: +191/-19
#[Out]# 14780  7e2f172027e8  Alexander Sauta <demosito@gmail.com>       1: +61/-7
#[Out]# 14774  acb9d11af744  Alexander Sauta <demosito@gmail.com>     1: +313/-19
#[Out]# 14773  fe49e3a66cb1  Alexander Sauta <demosito@gmail.com>     1: +186/-34
#[Out]# 14772  8d361ee4a151  Alexander Sauta <demosito@gmail.com>      1: +56/-12
#[Out]# 14771  fa76956b0ea6  Alexander Sauta <demosito@gmail.com>   1: +3268/-413
#[Out]# 14627  166776f97c9c  Alexander Sauta <demosito@gmail.com>    1: +693/-242
#[Out]# 14626  92f5c244e3a8  Alexander Sauta <demosito@gmail.com>   1: +268/-1919
#[Out]# 14625  72613f4a9016  Alexander Sauta <demosito@gmail.com>   1: +1962/-147
#[Out]# 14489  f361e2f84eb7  Alexander Sauta <demosito@gmail.com>  1: +2095/-1773
#[Out]# 14488  6c2e55f2b1ec  Alexander Sauta <demosito@gmail.com>     1: +127/-65
#[Out]# 14487  de759c9d3088  Alexander Sauta <demosito@gmail.com>  1: +1683/-1725
#[Out]# 14486  ce6f9a234d7e  Alexander Sauta <demosito@gmail.com>    1: +13896/-0), ('Alexander Schremmer <alex AT alexanderweb DOT de>',               node                                             author   changestr
#[Out]# n                                                                                
#[Out]# 2124  27fd8b7a6c51  Alexander Schremmer <alex AT alexanderweb DOT de>    2: +9/-7
#[Out]# 2123  c0729a7f6f8a  Alexander Schremmer <alex AT alexanderweb DOT de>   1: +18/-8
#[Out]# 2122  9383ba6b069a  Alexander Schremmer <alex AT alexanderweb DOT de>   2: +10/-2
#[Out]# 2121  150cdd6c3c90  Alexander Schremmer <alex AT alexanderweb DOT de>   1: +23/-6
#[Out]# 2120  c0994047c5ff  Alexander Schremmer <alex AT alexanderweb DOT de>    1: +1/-0
#[Out]# 2119  f62195054c5b  Alexander Schremmer <alex AT alexanderweb DOT de>  1: +18/-18), ('Alexander Solovyov <alexander@solovyov.net>',                node                                       author     changestr
#[Out]# n                                                                             
#[Out]# 14293  e4ab5ae193f2  Alexander Solovyov <alexander@solovyov.net>     2: +22/-6
#[Out]# 14135  9f5a0acb0056  Alexander Solovyov <alexander@solovyov.net>    5: +126/-4
#[Out]# 14101  e4bfb9c337f3  Alexander Solovyov <alexander@solovyov.net>   15: +17/-20
#[Out]# 14093  421d56a055fd  Alexander Solovyov <alexander@solovyov.net>    3: +10/-13
#[Out]# 14082  1c1e1232abdc  Alexander Solovyov <alexander@solovyov.net>   4: +517/-47
#[Out]# 14081  9966c95b8c4f  Alexander Solovyov <alexander@solovyov.net>  4: +296/-200
#[Out]# 14079  9d2be7e17fc1  Alexander Solovyov <alexander@solovyov.net>      1: +1/-2
#[Out]# 13645  89e7d35e0ef0  Alexander Solovyov <alexander@solovyov.net>    7: +46/-17
#[Out]# 13545  38c9837b1f75  Alexander Solovyov <alexander@solovyov.net>   23: +124/-3
#[Out]# 13544  270f57d35525  Alexander Solovyov <alexander@solovyov.net>   10: +36/-10
#[Out]# 13542  e42d18538e1d  Alexander Solovyov <alexander@solovyov.net>      1: +9/-0
#[Out]# 13182  8f29a08e7bbc  Alexander Solovyov <alexander@solovyov.net>      1: +1/-2
#[Out]# 12983  789e0fa2fcea  Alexander Solovyov <alexander@solovyov.net>      1: +3/-1), ('Alexander Solovyov <piranha at piranha.org.ua>',               node                                          author  changestr
#[Out]# n                                                                            
#[Out]# 7928  5c4026a289a4  Alexander Solovyov <piranha at piranha.org.ua>  5: +45/-1), ('Alexander Solovyov <piranha@piranha.org.ua>',                node                                       author    changestr
#[Out]# n                                                                            
#[Out]# 11268  ffd85ab578be  Alexander Solovyov <piranha@piranha.org.ua>     3: +8/-2
#[Out]# 11267  30c620e48d1c  Alexander Solovyov <piranha@piranha.org.ua>    3: +11/-4
#[Out]# 11249  1107888a1ad1  Alexander Solovyov <piranha@piranha.org.ua>     1: +1/-1
#[Out]# 11185  c5c190822501  Alexander Solovyov <piranha@piranha.org.ua>     1: +5/-1
#[Out]# 10760  17031fea4e95  Alexander Solovyov <piranha@piranha.org.ua>    5: +12/-4
#[Out]# 10662  16df09a54113  Alexander Solovyov <piranha@piranha.org.ua>    3: +18/-0
#[Out]# 10105  b5f352f33520  Alexander Solovyov <piranha@piranha.org.ua>     1: +3/-1
#[Out]# 10094  af04a3dea4cd  Alexander Solovyov <piranha@piranha.org.ua>    1: +15/-1
#[Out]# 10068  e600ad9bc257  Alexander Solovyov <piranha@piranha.org.ua>   3: +109/-0
#[Out]# 10044  2fcbef9a349a  Alexander Solovyov <piranha@piranha.org.ua>     1: +5/-3
#[Out]# 10042  ea3acaae25bb  Alexander Solovyov <piranha@piranha.org.ua>     1: +6/-0
#[Out]# 10027  3d718761157b  Alexander Solovyov <piranha@piranha.org.ua>     1: +2/-9
#[Out]# 9920   9d1195b2f00d  Alexander Solovyov <piranha@piranha.org.ua>    3: +12/-1
#[Out]# 9899   1fa9f6850dee  Alexander Solovyov <piranha@piranha.org.ua>   3: +109/-0
#[Out]# 9672   5bbf4f130684  Alexander Solovyov <piranha@piranha.org.ua>     1: +6/-6
#[Out]# 9670   7d56b6ffef72  Alexander Solovyov <piranha@piranha.org.ua>     3: +8/-1
#[Out]# 9669   9b127e888640  Alexander Solovyov <piranha@piranha.org.ua>   3: +41/-15
#[Out]# 9648   6064de41b7e4  Alexander Solovyov <piranha@piranha.org.ua>     1: +2/-4
#[Out]# 9643   013cc052a926  Alexander Solovyov <piranha@piranha.org.ua>     1: +1/-1
#[Out]# 9612   d051db8e9e44  Alexander Solovyov <piranha@piranha.org.ua>    3: +13/-6
#[Out]# 9610   d78fe60f6bda  Alexander Solovyov <piranha@piranha.org.ua>    5: +14/-9
#[Out]# 9527   cec4b0d3fb02  Alexander Solovyov <piranha@piranha.org.ua>     1: +2/-1
#[Out]# 9526   33a6213a974e  Alexander Solovyov <piranha@piranha.org.ua>   1: +16/-17
#[Out]# 8356   dcebff8a25dd  Alexander Solovyov <piranha@piranha.org.ua>   2: +44/-45
#[Out]# 8353   b24290c72a1d  Alexander Solovyov <piranha@piranha.org.ua>    2: +17/-8
#[Out]# 8295   36c704b0e7ab  Alexander Solovyov <piranha@piranha.org.ua>     1: +2/-2
#[Out]# 8278   63ea850b3312  Alexander Solovyov <piranha@piranha.org.ua>    1: +13/-8
#[Out]# 8151   b0d945b95105  Alexander Solovyov <piranha@piranha.org.ua>     1: +6/-3
#[Out]# 8006   5c794e7331e7  Alexander Solovyov <piranha@piranha.org.ua>     1: +1/-1
#[Out]# 7965   5a5396f49420  Alexander Solovyov <piranha@piranha.org.ua>    1: +24/-0
#[Out]# 7964   f779e1996e23  Alexander Solovyov <piranha@piranha.org.ua>   3: +21/-11
#[Out]# 7927   8c09952cd39a  Alexander Solovyov <piranha@piranha.org.ua>   1: +29/-22
#[Out]# 7921   f680a1bd679b  Alexander Solovyov <piranha@piranha.org.ua>    1: +15/-1
#[Out]# 7914   c2cd8d772805  Alexander Solovyov <piranha@piranha.org.ua>     1: +3/-2
#[Out]# 7778   e3425726b80d  Alexander Solovyov <piranha@piranha.org.ua>     1: +1/-1
#[Out]# 7687   ee3364d3d859  Alexander Solovyov <piranha@piranha.org.ua>     1: +1/-1
#[Out]# 7680   6a0bc2dc9da6  Alexander Solovyov <piranha@piranha.org.ua>    1: +83/-0
#[Out]# 7673   bd5c37d792e6  Alexander Solovyov <piranha@piranha.org.ua>     1: +2/-2
#[Out]# 7574   4949729ee9ee  Alexander Solovyov <piranha@piranha.org.ua>  7: +106/-54
#[Out]# 7536   187a13bd14c6  Alexander Solovyov <piranha@piranha.org.ua>    1: +15/-0
#[Out]# 7318   98408cb74137  Alexander Solovyov <piranha@piranha.org.ua>    2: +80/-0
#[Out]# 7230   9b72c732ed2f  Alexander Solovyov <piranha@piranha.org.ua>    1: +16/-6
#[Out]# 7229   e1afb50ec2aa  Alexander Solovyov <piranha@piranha.org.ua>  2: +103/-63
#[Out]# 7139   23bd7383891c  Alexander Solovyov <piranha@piranha.org.ua>   1: +72/-72
#[Out]# 7085   c29d3f4ed967  Alexander Solovyov <piranha@piranha.org.ua>     1: +4/-4
#[Out]# 7081   2627ef59195d  Alexander Solovyov <piranha@piranha.org.ua>   5: +36/-89
#[Out]# 7076   9bc46d069a76  Alexander Solovyov <piranha@piranha.org.ua>  3: +176/-49
#[Out]# 6781   bacfee67c1a9  Alexander Solovyov <piranha@piranha.org.ua>     1: +3/-0
#[Out]# 6778   9080f7031f69  Alexander Solovyov <piranha@piranha.org.ua>     1: +1/-1), ('Alexandre Fayolle <alexandre.fayolle@logilab.fr>',                node                                            author changestr
#[Out]# n                                                                              
#[Out]# 11708  ca5fd84d62c6  Alexandre Fayolle <alexandre.fayolle@logilab.fr>  1: +0/-3), ('Alexandre Vassalotti <mercurial-bugs@selenic.com>',               node                                             author  changestr
#[Out]# n                                                                               
#[Out]# 5857  dd5a501cb97f  Alexandre Vassalotti <mercurial-bugs@selenic.com>  4: +15/-2), ('Alexis S. L. Carvalho <alexis@cecm.usp.br>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 533 entries, 6449 to 1149
#[Out]# Data columns:
#[Out]# node         533  non-null values
#[Out]# author       533  non-null values
#[Out]# changestr    533  non-null values
#[Out]# dtypes: object(3)), ('Ali Gholami Rudi <aligrudi@users.sourceforge.net>',               node                                             author changestr
#[Out]# n                                                                              
#[Out]# 5959  e160f2312815  Ali Gholami Rudi <aligrudi@users.sourceforge.net>  1: +4/-1), ('Ali Saidi <saidi@eecs.umich.edu>',               node                            author changestr
#[Out]# n                                                             
#[Out]# 6475  782dbbdfb1d7  Ali Saidi <saidi@eecs.umich.edu>  1: +1/-1), ('Alistair Bell <alistair.bell@netronome.com>',                node                                       author changestr
#[Out]# n                                                                         
#[Out]# 15493  43e068c15619  Alistair Bell <alistair.bell@netronome.com>  1: +4/-3), ('Alistair Bell <alistair@bellsonline.com>',                node                                    author   changestr
#[Out]# n                                                                        
#[Out]# 10498  e96597c8d0ea  Alistair Bell <alistair@bellsonline.com>  1: +16/-12), ('Alpar Juttner <alpar@cs.elte.hu>',               node                            author   changestr
#[Out]# n                                                               
#[Out]# 7426  df0962f6c54e  Alpar Juttner <alpar@cs.elte.hu>  1: +177/-2), ('Andreas Freimuth <andreas.freimuth@united-bits.de>',                node                                             author       changestr
#[Out]# n                                                                                     
#[Out]# 15217  42d0d4f63bf0  Andreas Freimuth <andreas.freimuth@united-bits.de        1: +3/-5
#[Out]# 14040  1cafa0426a1a  Andreas Freimuth <andreas.freimuth@united-bits.de        1: +1/-1
#[Out]# 12038  2afefc01259e  Andreas Freimuth <andreas.freimuth@united-bits.de  3: +2119/-2074), ('Andreas Hartmetz <ahartmetz@gmail.com>',               node                                  author changestr
#[Out]# n                                                                   
#[Out]# 6876  4a8b9cf62a6b  Andreas Hartmetz <ahartmetz@gmail.com>  1: +6/-6), ('Andrei Polushin <polushin@gmail.com>',                node                                author     changestr
#[Out]# n                                                                      
#[Out]# 16032  c9f79421e0bd  Andrei Polushin <polushin@gmail.com>   1: +206/-13
#[Out]# 16031  ccaa17c8f630  Andrei Polushin <polushin@gmail.com>    1: +30/-46
#[Out]# 15981  1b3d952f1544  Andrei Polushin <polushin@gmail.com>   1: +307/-95
#[Out]# 15870  c37479fb81bd  Andrei Polushin <polushin@gmail.com>    1: +12/-12
#[Out]# 15869  4a9387a97d5e  Andrei Polushin <polushin@gmail.com>    1: +20/-20
#[Out]# 15868  811044244287  Andrei Polushin <polushin@gmail.com>    1: +10/-10
#[Out]# 15867  43ca9b1a275d  Andrei Polushin <polushin@gmail.com>    1: +30/-33
#[Out]# 15866  8306c5e35eef  Andrei Polushin <polushin@gmail.com>    1: +14/-14
#[Out]# 15848  a1bf5e1c4416  Andrei Polushin <polushin@gmail.com>    1: +80/-80
#[Out]# 15847  3bbc7f024f05  Andrei Polushin <polushin@gmail.com>    1: +34/-36
#[Out]# 15846  38937bc2f4e6  Andrei Polushin <polushin@gmail.com>      1: +3/-3
#[Out]# 15812  7551b2cf2fed  Andrei Polushin <polushin@gmail.com>   1: +163/-57
#[Out]# 15721  c5ba674a98aa  Andrei Polushin <polushin@gmail.com>    1: +32/-31
#[Out]# 15720  25c50d0836a8  Andrei Polushin <polushin@gmail.com>  1: +147/-148
#[Out]# 15719  f40d3fd21043  Andrei Polushin <polushin@gmail.com>    1: +14/-14
#[Out]# 15718  ef4787b6bc74  Andrei Polushin <polushin@gmail.com>    1: +64/-64
#[Out]# 15717  d80aae4480e3  Andrei Polushin <polushin@gmail.com>  1: +437/-438
#[Out]# 15716  588a16fcf62e  Andrei Polushin <polushin@gmail.com>      1: +9/-9
#[Out]# 15715  0649c448c0b2  Andrei Polushin <polushin@gmail.com>  1: +193/-194
#[Out]# 15714  0c5d7d86c55b  Andrei Polushin <polushin@gmail.com>  1: +251/-252), ('Andrei Vermel <avermel@mail.ru>',                node                           author changestr
#[Out]# n                                                             
#[Out]# 14840  9e9d4a762586  Andrei Vermel <avermel@mail.ru>  1: +1/-0
#[Out]# 7008   5e1a867e5d65  Andrei Vermel <avermel@mail.ru>  1: +4/-3
#[Out]# 3963   0d94e4a3ddb4  Andrei Vermel <avermel@mail.ru>  1: +8/-1
#[Out]# 3943   18dcc22666a0  Andrei Vermel <avermel@mail.ru>  1: +6/-1
#[Out]# 3935   31a679ae7eef  Andrei Vermel <avermel@mail.ru>  1: +1/-1
#[Out]# 3933   c620376b8fd6  Andrei Vermel <avermel@mail.ru>  1: +1/-1), ('Andrew Bachmann <andrewbachmann@gmail.com>',               node                                      author changestr
#[Out]# n                                                                       
#[Out]# 4232  95ffa36d1d2a  Andrew Bachmann <andrewbachmann@gmail.com>  2: +9/-1), ('Andrew Beekhof <beekhof@gmail.com>',               node                              author changestr
#[Out]# n                                                               
#[Out]# 6747  d8ae6a3a1833  Andrew Beekhof <beekhof@gmail.com>  1: +1/-1
#[Out]# 6744  bc553c6d1ef9  Andrew Beekhof <beekhof@gmail.com>  1: +2/-2), ('Andrew Pritchard <andrewp@fogcreek.com>',                node                                   author  changestr
#[Out]# n                                                                      
#[Out]# 15061  f4522df38c65  Andrew Pritchard <andrewp@fogcreek.com>  7: +37/-0
#[Out]# 14973  207935cda6dc  Andrew Pritchard <andrewp@fogcreek.com>   2: +6/-5
#[Out]# 14838  192e02680d09  Andrew Pritchard <andrewp@fogcreek.com>  2: +15/-1), ('Andrew Pritchard <awpritchard@gmail.com>',                node                                    author  changestr
#[Out]# n                                                                       
#[Out]# 15336  83debcd7064b  Andrew Pritchard <awpritchard@gmail.com>  1: +89/-0), ('Andrew Thompson <andrewkt@aktzero.com>',               node                                  author  changestr
#[Out]# n                                                                    
#[Out]# 2104  f1085d34d20d  Andrew Thompson <andrewkt@aktzero.com>  2: +18/-0
#[Out]# 761   0fb498458905  Andrew Thompson <andrewkt@aktzero.com>   5: +8/-8
#[Out]# 676   32f7dc81c07e  Andrew Thompson <andrewkt@aktzero.com>   4: +0/-8
#[Out]# 673   8e518e11f6cf  Andrew Thompson <andrewkt@aktzero.com>   1: +1/-1), ('Andrey <py4fun@gmail.com>',               node                     author changestr
#[Out]# n                                                      
#[Out]# 9414  9be91129c96e  Andrey <py4fun@gmail.com>  1: +3/-3), ('Andrey Somov <py4fun@gmail.com>',                node                           author    changestr
#[Out]# n                                                                
#[Out]# 15688  a2edccdfb86a  Andrey Somov <py4fun@gmail.com>  1: +219/-57
#[Out]# 9486   96379c93ba6f  Andrey Somov <py4fun@gmail.com>     3: +4/-3), ('Andrzej Bieniek <andyhelp@gmail.com>',                node                                author  changestr
#[Out]# n                                                                   
#[Out]# 15046  70e11de6964d  Andrzej Bieniek <andyhelp@gmail.com>  3: +31/-6), ('Andr\xc3\xa9 Sintzoff <andre.sintzoff@gmail.com>',                node                                     author  changestr
#[Out]# n                                                                        
#[Out]# 13409  9e5df8719ad4  André Sintzoff <andre.sintzoff@gmail.com>  1: +2/-0), ('Angel Ezquerra',                node          author  changestr
#[Out]# n                                             
#[Out]# 10774  e655b378ce73  Angel Ezquerra  1: +29/-0
#[Out]# 10773  157f9de9ad2a  Angel Ezquerra  1: +12/-1), ('Angel Ezquerra <angel.ezquerra@gmail.com>',                node                                     author     changestr
#[Out]# n                                                                           
#[Out]# 16468  2fb521d75dc2  Angel Ezquerra <angel.ezquerra@gmail.com>      1: +2/-0
#[Out]# 16454  92c7e917b647  Angel Ezquerra <angel.ezquerra@gmail.com>      1: +2/-2
#[Out]# 16448  60c379da12aa  Angel Ezquerra <angel.ezquerra@gmail.com>      1: +5/-0
#[Out]# 16447  984e0412e82b  Angel Ezquerra <angel.ezquerra@gmail.com>     1: +13/-0
#[Out]# 16446  453c8670566c  Angel Ezquerra <angel.ezquerra@gmail.com>      1: +9/-6
#[Out]# 16445  432f198600c6  Angel Ezquerra <angel.ezquerra@gmail.com>      1: +3/-0
#[Out]# 16444  9e02e032b522  Angel Ezquerra <angel.ezquerra@gmail.com>     1: +23/-0
#[Out]# 16431  6883c2363f44  Angel Ezquerra <angel.ezquerra@gmail.com>    3: +36/-15
#[Out]# 16430  71dcce391a44  Angel Ezquerra <angel.ezquerra@gmail.com>     3: +24/-3
#[Out]# 16404  1fb2f1400ea8  Angel Ezquerra <angel.ezquerra@gmail.com>     1: +79/-0
#[Out]# 16345  17a9a1f5cee2  Angel Ezquerra <angel.ezquerra@gmail.com>     2: +66/-4
#[Out]# 16342  a740fa28d718  Angel Ezquerra <angel.ezquerra@gmail.com>  2: +179/-173
#[Out]# 15739  309e49491253  Angel Ezquerra <angel.ezquerra@gmail.com>     2: +14/-8
#[Out]# 15265  460135339d74  Angel Ezquerra <angel.ezquerra@gmail.com>     2: +16/-0
#[Out]# 15000  ec18cd254156  Angel Ezquerra <angel.ezquerra@gmail.com>      1: +6/-0
#[Out]# 14981  44382887d012  Angel Ezquerra <angel.ezquerra@gmail.com>   21: +23/-19), ('Anthony Foiani <anthony.foiani@gmail.com>',                node                                     author changestr
#[Out]# n                                                                       
#[Out]# 11706  ffcceca7406d  Anthony Foiani <anthony.foiani@gmail.com>  1: +4/-5), ('Antoine Pitrou <solipsis@pitrou.net>',                node                                author  changestr
#[Out]# n                                                                   
#[Out]# 13501  50b825c1adb1  Antoine Pitrou <solipsis@pitrou.net>  2: +29/-0), ('Anupam Kapoor<anupam.kapoor@gmail.com>',               node                                  author changestr
#[Out]# n                                                                   
#[Out]# 1313  1cc7c0cbc30b  Anupam Kapoor<anupam.kapoor@gmail.com>  1: +4/-1), ('Armin Ronacher <armin.ronacher@active-4.com>',               node                                        author changestr
#[Out]# n                                                                         
#[Out]# 6005  a7817ad608ea  Armin Ronacher <armin.ronacher@active-4.com>  1: +2/-2), ('Arnab Bose <hirak99@gmail.com>',                node                          author changestr
#[Out]# n                                                            
#[Out]# 11504  8d827f4a23f1  Arnab Bose <hirak99@gmail.com>  1: +2/-1), ('Arne Babenhauserheide <arne@draketo.de>',                node                                   author   changestr
#[Out]# n                                                                       
#[Out]# 12992  b98d7ffa5c5b  Arne Babenhauserheide <arne@draketo.de>  1: +30/-14), ('Arne Babenhauserheide <bab@draketo.de>',                node                                  author   changestr
#[Out]# n                                                                      
#[Out]# 15661  dbdb8aa70503  Arne Babenhauserheide <bab@draketo.de>  2: +16/-16
#[Out]# 14803  968c301a1005  Arne Babenhauserheide <bab@draketo.de>    1: +1/-1
#[Out]# 13952  1bd9f3a6a0d0  Arne Babenhauserheide <bab@draketo.de>    1: +1/-1
#[Out]# 13029  deab25946eb2  Arne Babenhauserheide <bab@draketo.de>   1: +17/-9
#[Out]# 13028  71333cfffb34  Arne Babenhauserheide <bab@draketo.de>   1: +21/-2
#[Out]# 7899   48da69ff79bd  Arne Babenhauserheide <bab@draketo.de>    1: +5/-0), ('Arun Sharma <arun@sharma-home.net>',               node                              author changestr
#[Out]# n                                                               
#[Out]# 1566  8befbb4e30b2  Arun Sharma <arun@sharma-home.net>  1: +4/-1), ('Arun Thomas <arun.thomas@gmail.com>',               node                               author changestr
#[Out]# n                                                                
#[Out]# 5797  4fba4fee0718  Arun Thomas <arun.thomas@gmail.com>  1: +2/-0), ('Augie Fackler <durin42@gmail.com>',                node                             author     changestr
#[Out]# n                                                                   
#[Out]# 16357  a5a3af000e0d  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 16164  101c8a1befb1  Augie Fackler <durin42@gmail.com>      1: +2/-0
#[Out]# 16012  f1208827df7c  Augie Fackler <durin42@gmail.com>      1: +2/-1
#[Out]# 15990  76630fbbf4fa  Augie Fackler <durin42@gmail.com>     1: +51/-0
#[Out]# 15972  341c58282b25  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 15785  83a140752239  Augie Fackler <durin42@gmail.com>     1: +2/-13
#[Out]# 15784  425c1309718f  Augie Fackler <durin42@gmail.com>     1: +2/-13
#[Out]# 15695  88a82069be4a  Augie Fackler <durin42@gmail.com>      1: +6/-0
#[Out]# 15443  62c9183a0bbb  Augie Fackler <durin42@gmail.com>     3: +24/-4
#[Out]# 15237  7196ed7a1505  Augie Fackler <durin42@gmail.com>      2: +4/-1
#[Out]# 15233  81c97964d123  Augie Fackler <durin42@gmail.com>      2: +5/-3
#[Out]# 15218  c81dce8a7bb6  Augie Fackler <durin42@gmail.com>     3: +44/-0
#[Out]# 15041  5a0fdc715769  Augie Fackler <durin42@gmail.com>      1: +3/-1
#[Out]# 15040  1dbd42a02153  Augie Fackler <durin42@gmail.com>      1: +5/-4
#[Out]# 15039  04a950b1c2ad  Augie Fackler <durin42@gmail.com>      1: +2/-0
#[Out]# 15038  b64538363dbe  Augie Fackler <durin42@gmail.com>      1: +1/-2
#[Out]# 15037  a2aa75118837  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 15036  5656cb5b9028  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 15035  bcba68e81a81  Augie Fackler <durin42@gmail.com>      1: +2/-2
#[Out]# 15034  0b21ae0a2366  Augie Fackler <durin42@gmail.com>      5: +6/-9
#[Out]# 15033  592e45b7d43e  Augie Fackler <durin42@gmail.com>      1: +4/-3
#[Out]# 15032  a3f97038c1c2  Augie Fackler <durin42@gmail.com>      1: +3/-2
#[Out]# 15031  b7dbe957585c  Augie Fackler <durin42@gmail.com>      1: +6/-5
#[Out]# 15030  376091a4ad23  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 15029  0588fb0e2e8d  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 15028  194b043dfa51  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 15027  376c32a5ccdc  Augie Fackler <durin42@gmail.com>      1: +3/-3
#[Out]# 15026  c035f1c53e39  Augie Fackler <durin42@gmail.com>      1: +5/-5
#[Out]# 15025  1c917bc66ccc  Augie Fackler <durin42@gmail.com>      1: +5/-9
#[Out]# 15024  5523529bd1af  Augie Fackler <durin42@gmail.com>      1: +2/-2
#[Out]# 15023  497819817307  Augie Fackler <durin42@gmail.com>      1: +4/-3
#[Out]# 15022  b1dcc5ab86cd  Augie Fackler <durin42@gmail.com>      1: +1/-3
#[Out]# 15021  fd246aefedd3  Augie Fackler <durin42@gmail.com>      1: +4/-3
#[Out]# 15020  16e5271b216f  Augie Fackler <durin42@gmail.com>      2: +2/-2
#[Out]# 15019  1b3f5f603aef  Augie Fackler <durin42@gmail.com>      1: +1/-2
#[Out]# 15018  6349a9eb0178  Augie Fackler <durin42@gmail.com>      1: +1/-2
#[Out]# 15017  ce7e3014fda7  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 15016  6ee6ecf1ee89  Augie Fackler <durin42@gmail.com>      1: +2/-2
#[Out]# 15015  4c523a2af6e7  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 15014  61807854004e  Augie Fackler <durin42@gmail.com>      1: +3/-3
#[Out]# 15013  144e97421f6b  Augie Fackler <durin42@gmail.com>      1: +5/-5
#[Out]# 15012  a4435770cf57  Augie Fackler <durin42@gmail.com>      1: +3/-2
#[Out]# 15011  32302480b402  Augie Fackler <durin42@gmail.com>      1: +4/-4
#[Out]# 15010  3aa34005a73d  Augie Fackler <durin42@gmail.com>      1: +3/-7
#[Out]# 15009  28762bf809d8  Augie Fackler <durin42@gmail.com>      1: +2/-3
#[Out]# 15008  11aad09a6370  Augie Fackler <durin42@gmail.com>     6: +11/-8
#[Out]# 15007  e2c413bde8a5  Augie Fackler <durin42@gmail.com>      3: +5/-5
#[Out]# 15006  d3bb825ddae3  Augie Fackler <durin42@gmail.com>    7: +13/-12
#[Out]# 15005  5b072d4b62f2  Augie Fackler <durin42@gmail.com>      1: +4/-0
#[Out]# 15004  4a28cb4df1f8  Augie Fackler <durin42@gmail.com>      3: +3/-3
#[Out]# 14975  84af56cc673b  Augie Fackler <durin42@gmail.com>      1: +5/-2
#[Out]# 14974  7c3c8f37e84f  Augie Fackler <durin42@gmail.com>     2: +15/-2
#[Out]# 14929  5d261fd00446  Augie Fackler <durin42@gmail.com>     3: +65/-3
#[Out]# 14928  ec4ba216ddef  Augie Fackler <durin42@gmail.com>      1: +6/-1
#[Out]# 14927  925cab23d7d5  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 14874  1f581a8b1948  Augie Fackler <durin42@gmail.com>      1: +3/-3
#[Out]# 14842  4f39610996fa  Augie Fackler <durin42@gmail.com>      2: +4/-2
#[Out]# 14841  494b26ad8736  Augie Fackler <durin42@gmail.com>     2: +3/-10
#[Out]# 14834  2957b8b1e809  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 14664  0ae98cd2a83f  Augie Fackler <durin42@gmail.com>    2: +50/-13
#[Out]# 14663  88cb01c4575e  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 14506  5cc7905bccc9  Augie Fackler <durin42@gmail.com>    1: +55/-36
#[Out]# 14505  f0f965098810  Augie Fackler <durin42@gmail.com>     1: +12/-8
#[Out]# 14438  639f26cab2f5  Augie Fackler <durin42@gmail.com>      1: +3/-0
#[Out]# 14395  a75e0f4ba0ab  Augie Fackler <durin42@gmail.com>   6: +120/-50
#[Out]# 14394  436e5379d7ba  Augie Fackler <durin42@gmail.com>      1: +4/-1
#[Out]# 14369  bf85c2639700  Augie Fackler <durin42@gmail.com>      1: +6/-5
#[Out]# 14364  5c3de67e7402  Augie Fackler <durin42@gmail.com>   5: +147/-23
#[Out]# 14318  84256ba2fbf7  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 14317  9adbb5ef0964  Augie Fackler <durin42@gmail.com>      2: +6/-1
#[Out]# 14271  13d44e4235f8  Augie Fackler <durin42@gmail.com>      1: +4/-0
#[Out]# 14270  e7525a555a64  Augie Fackler <durin42@gmail.com>   3: +276/-79
#[Out]# 14269  861f28212398  Augie Fackler <durin42@gmail.com>   9: +1651/-2
#[Out]# 14243  08d84bdce1a5  Augie Fackler <durin42@gmail.com>      1: +7/-1
#[Out]# 14232  5fa21960b2f4  Augie Fackler <durin42@gmail.com>  3: +133/-102
#[Out]# 14221  c4de16642861  Augie Fackler <durin42@gmail.com>      1: +7/-7
#[Out]# 14220  38e387a64f58  Augie Fackler <durin42@gmail.com>      1: +3/-0
#[Out]# 14163  8468ec1109d1  Augie Fackler <durin42@gmail.com>      1: +8/-0
#[Out]# 14138  0c5228836fcd  Augie Fackler <durin42@gmail.com>     1: +16/-2
#[Out]# 14132  877390020477  Augie Fackler <durin42@gmail.com>      1: +8/-5
#[Out]# 14100  87ebf72878ed  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 14080  bcc6ed0f6c3b  Augie Fackler <durin42@gmail.com>      1: +9/-1
#[Out]# 14073  1f667030b139  Augie Fackler <durin42@gmail.com>      1: +4/-1
#[Out]# 14072  33e04d3d17f6  Augie Fackler <durin42@gmail.com>     1: +23/-0
#[Out]# 14071  d98af1420930  Augie Fackler <durin42@gmail.com>  2: +174/-171
#[Out]# 14070  bc61a4b46734  Augie Fackler <durin42@gmail.com>  2: +105/-105
#[Out]# 14069  e5dd974a99fa  Augie Fackler <durin42@gmail.com>      1: +4/-3
#[Out]# 14068  83d3f87c059e  Augie Fackler <durin42@gmail.com>      1: +3/-3
#[Out]# 14067  7e453770b364  Augie Fackler <durin42@gmail.com>      1: +1/-2
#[Out]# 13988  3d83c7d70a98  Augie Fackler <durin42@gmail.com>      1: +4/-1
#[Out]# 13987  34f577007ffe  Augie Fackler <durin42@gmail.com>      2: +9/-3
#[Out]# 13982  518344d02761  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 13704  84bd3fd63afc  Augie Fackler <durin42@gmail.com>      1: +5/-1
#[Out]# 13703  617a87cb7eb2  Augie Fackler <durin42@gmail.com>     3: +27/-1
#[Out]# 13668  733af5d9f6b2  Augie Fackler <durin42@gmail.com>     1: +12/-8
#[Out]# 13631  1052b1421a48  Augie Fackler <durin42@gmail.com>     1: +10/-1
#[Out]# 13511  392b5684d0b4  Augie Fackler <durin42@gmail.com>    1: +49/-45
#[Out]# 13433  0b1bbc46516e  Augie Fackler <durin42@gmail.com>     1: +11/-0
#[Out]# 13211  e11c14f14491  Augie Fackler <durin42@gmail.com>      2: +8/-0
#[Out]# 13206  735dd8e8a208  Augie Fackler <durin42@gmail.com>      4: +4/-0
#[Out]# 13205  ab5fcc473fd1  Augie Fackler <durin42@gmail.com>      1: +2/-2
#[Out]# 13204  082f5be788d9  Augie Fackler <durin42@gmail.com>    1: +19/-15
#[Out]# 13203  43575c67add3  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 13202  ce4cd176634e  Augie Fackler <durin42@gmail.com>     1: +46/-0
#[Out]# 13192  24e3349cba8e  Augie Fackler <durin42@gmail.com>    1: +14/-10
#[Out]# 13190  f139f34ba330  Augie Fackler <durin42@gmail.com>    2: +12/-10
#[Out]# 13184  c36dad4f6e54  Augie Fackler <durin42@gmail.com>  3: +640/-616
#[Out]# 13183  bda5f35fbf67  Augie Fackler <durin42@gmail.com>     2: +22/-4
#[Out]# 12767  21a50fe47a92  Augie Fackler <durin42@gmail.com>      1: +9/-8
#[Out]# 12740  8dcd3203a261  Augie Fackler <durin42@gmail.com>     2: +13/-2
#[Out]# 12735  098dfb2b7596  Augie Fackler <durin42@gmail.com>      1: +2/-2
#[Out]# 12728  61c0df2b089a  Augie Fackler <durin42@gmail.com>     2: +49/-1
#[Out]# 12727  24f16c2c6d41  Augie Fackler <durin42@gmail.com>      1: +5/-0
#[Out]# 12726  66e7ba85585b  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 12720  c7e619e30ba3  Augie Fackler <durin42@gmail.com>     3: +29/-0
#[Out]# 12719  33820dccbea4  Augie Fackler <durin42@gmail.com>     3: +18/-6
#[Out]# 12718  f5178fbcd197  Augie Fackler <durin42@gmail.com>     2: +44/-1
#[Out]# 12717  bd37e7492478  Augie Fackler <durin42@gmail.com>      2: +0/-2
#[Out]# 12694  1b1a9038a71a  Augie Fackler <durin42@gmail.com>      3: +8/-8
#[Out]# 12693  94e7bd38d9a3  Augie Fackler <durin42@gmail.com>      1: +6/-1
#[Out]# 12692  c52c629ce19e  Augie Fackler <durin42@gmail.com>   10: +18/-16
#[Out]# 12685  58a3e2608ae4  Augie Fackler <durin42@gmail.com>     2: +52/-4
#[Out]# 12683  d664547ef540  Augie Fackler <durin42@gmail.com>   40: +92/-14
#[Out]# 12669  ead4e21f49f1  Augie Fackler <durin42@gmail.com>  39: +415/-15
#[Out]# 12657  646eb9337c87  Augie Fackler <durin42@gmail.com>      1: +2/-1
#[Out]# 12179  70f4a0f4e9a3  Augie Fackler <durin42@gmail.com>     1: +11/-7
#[Out]# 12178  1f71dffabc53  Augie Fackler <durin42@gmail.com>      1: +3/-2
#[Out]# 12177  a88a4720c2f0  Augie Fackler <durin42@gmail.com>     2: +13/-5
#[Out]# 12176  dba2db7a7c28  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 11740  7adb1274a4f9  Augie Fackler <durin42@gmail.com>      1: +5/-0
#[Out]# 11458  ec21d91c79b3  Augie Fackler <durin42@gmail.com>     1: +10/-2
#[Out]# 11041  479f15f3faa9  Augie Fackler <durin42@gmail.com>      1: +2/-2
#[Out]# 11040  91c58cf54eee  Augie Fackler <durin42@gmail.com>     1: +17/-7
#[Out]# 11039  7faef79a89c7  Augie Fackler <durin42@gmail.com>      1: +3/-2
#[Out]# 11038  aa0426c79664  Augie Fackler <durin42@gmail.com>     2: +11/-1
#[Out]# 10995  83af68e38be3  Augie Fackler <durin42@gmail.com>     3: +16/-2
#[Out]# 10660  1b45468d3deb  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 10659  ca6ba6cac6cd  Augie Fackler <durin42@gmail.com>    2: +18/-16
#[Out]# 10606  f6ee02933af9  Augie Fackler <durin42@gmail.com>      1: +1/-0
#[Out]# 10441  dc0d1ca2d378  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 10435  ad104a786d35  Augie Fackler <durin42@gmail.com>    1: +182/-0
#[Out]# 10434  767fbacb3ddc  Augie Fackler <durin42@gmail.com>     1: +20/-1
#[Out]# 10433  8a8030fc57d6  Augie Fackler <durin42@gmail.com>    3: +497/-0
#[Out]# 10432  ba5e508b5e92  Augie Fackler <durin42@gmail.com>    14: +94/-1
#[Out]# 10431  5cef810e588f  Augie Fackler <durin42@gmail.com>    3: +147/-4
#[Out]# 10426  f8a9de664a1c  Augie Fackler <durin42@gmail.com>      1: +4/-2
#[Out]# 10425  93b5abcf5101  Augie Fackler <durin42@gmail.com>      1: +2/-0
#[Out]# 10424  caaa1f99d681  Augie Fackler <durin42@gmail.com>      1: +3/-2
#[Out]# 10423  600142e7a028  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 10419  5fc090ba08a6  Augie Fackler <durin42@gmail.com>     3: +64/-0
#[Out]# 10384  e54e3f6e6789  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 10374  27d542bc0f5b  Augie Fackler <durin42@gmail.com>    3: +12/-20
#[Out]# 10234  cd477be6f2fc  Augie Fackler <durin42@gmail.com>    3: +203/-1
#[Out]# 10233  5ca0d220ae21  Augie Fackler <durin42@gmail.com>    3: +28/-10
#[Out]# 10232  24ce8f0c0a39  Augie Fackler <durin42@gmail.com>    5: +17/-12
#[Out]# 10231  fc32b2fc468e  Augie Fackler <durin42@gmail.com>      1: +2/-1
#[Out]# 10114  30d51a0df46c  Augie Fackler <durin42@gmail.com>     1: +15/-0
#[Out]# 9998   192083a3e6fe  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 9726   430e59ff3437  Augie Fackler <durin42@gmail.com>     2: +77/-3
#[Out]# 8181   6f14253416bd  Augie Fackler <durin42@gmail.com>     1: +14/-3
#[Out]# 8104   fc78313cba53  Augie Fackler <durin42@gmail.com>     1: +33/-1
#[Out]# 7861   99e5f97c9a97  Augie Fackler <durin42@gmail.com>    2: +42/-42
#[Out]# 7838   74c3baca65c9  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 7821   9fe7e6acf525  Augie Fackler <durin42@gmail.com>   11: +23/-22
#[Out]# 7773   88887054d277  Augie Fackler <durin42@gmail.com>    4: +38/-11
#[Out]# 7772   09d0fe02988d  Augie Fackler <durin42@gmail.com>     2: +17/-0
#[Out]# 7466   3e5db4228f8f  Augie Fackler <durin42@gmail.com>   4: +124/-42
#[Out]# 7458   03dd55115985  Augie Fackler <durin42@gmail.com>    4: +284/-0
#[Out]# 7296   66d0fc108044  Augie Fackler <durin42@gmail.com>      1: +5/-1
#[Out]# 7089   2fdbf2ccd03a  Augie Fackler <durin42@gmail.com>      1: +1/-1
#[Out]# 6805   84294e3710b8  Augie Fackler <durin42@gmail.com>    4: +14/-19
#[Out]# 6804   f4b6dec99950  Augie Fackler <durin42@gmail.com>      1: +2/-2
#[Out]# 6771   7f58dec6aeb7  Augie Fackler <durin42@gmail.com>   29: +359/-2), ('Augie Fackler <raf@durin42.com>',                node                           author changestr
#[Out]# n                                                             
#[Out]# 16626  23a125545c3d  Augie Fackler <raf@durin42.com>  1: +1/-1
#[Out]# 16486  70b5e25f1598  Augie Fackler <raf@durin42.com>  1: +6/-0), ('Aurelien Jacobs <aurel@gnuage.org>',               node                              author changestr
#[Out]# n                                                               
#[Out]# 3397  f0415b61949d  Aurelien Jacobs <aurel@gnuage.org>  1: +1/-0), ('Azhagu Selvan SP <tamizhgeek@gmail.com>',                node                                   author changestr
#[Out]# n                                                                     
#[Out]# 13480  69418d4525d1  Azhagu Selvan SP <tamizhgeek@gmail.com>  1: +6/-6
#[Out]# 13479  b14ed1692b27  Azhagu Selvan SP <tamizhgeek@gmail.com>  1: +2/-0
#[Out]# 12796  bc69ba99e34b  Azhagu Selvan SP <tamizhgeek@gmail.com>  1: +1/-1), ('Bart Trojanowski <bart@jukie.net>',               node                             author changestr
#[Out]# n                                                              
#[Out]# 1073  7b35a980b982  Bart Trojanowski <bart@jukie.net>  3: +8/-6), ('Bartosz SKOWRON <getxsick at gmail dot com>',               node                                       author changestr
#[Out]# n                                                                        
#[Out]# 7245  127a624406b4  Bartosz SKOWRON <getxsick at gmail dot com>  1: +2/-3), ('Bartosz SKOWRON <getxsick@gmail.com>',               node                                author changestr
#[Out]# n                                                                 
#[Out]# 7559  e4ab4802f261  Bartosz SKOWRON <getxsick@gmail.com>  1: +1/-3), ('Bela Babik <teki321@gmail.com>',               node                          author changestr
#[Out]# n                                                           
#[Out]# 4082  b2338c0cf468  Bela Babik <teki321@gmail.com>  1: +3/-3), ('Ben Hockey <neonstalwart@gmail.com>',                node                               author  changestr
#[Out]# n                                                                  
#[Out]# 15110  a051f8a6a7cc  Ben Hockey <neonstalwart@gmail.com>  1: +13/-0), ('Ben Thomas <bthomas@virtualiron.com>',               node                                author  changestr
#[Out]# n                                                                  
#[Out]# 4242  c30c922f907a  Ben Thomas <bthomas@virtualiron.com>  1: +29/-5), ('Benjamin Pollack <benjamin@bitquabit.com>',                node                                     author   changestr
#[Out]# n                                                                         
#[Out]# 15323  19368c54a774  Benjamin Pollack <benjamin@bitquabit.com>    1: +3/-6
#[Out]# 15320  681267a5f491  Benjamin Pollack <benjamin@bitquabit.com>    1: +9/-1
#[Out]# 15319  9da7e96cd5c2  Benjamin Pollack <benjamin@bitquabit.com>   3: +4/-10
#[Out]# 15317  41f371150ccb  Benjamin Pollack <benjamin@bitquabit.com>  4: +33/-23
#[Out]# 15316  c65f5b6e26d4  Benjamin Pollack <benjamin@bitquabit.com>  5: +39/-39
#[Out]# 15315  ca51a5dd5d0b  Benjamin Pollack <benjamin@bitquabit.com>    1: +5/-4
#[Out]# 12656  5096faaa280e  Benjamin Pollack <benjamin@bitquabit.com>    1: +1/-1
#[Out]# 11559  52e4ac3e63f7  Benjamin Pollack <benjamin@bitquabit.com>    3: +6/-0
#[Out]# 10650  bdc3256a318e  Benjamin Pollack <benjamin@bitquabit.com>    1: +3/-1
#[Out]# 7843   aa1a87f7544f  Benjamin Pollack <benjamin@bitquabit.com>   2: +27/-0
#[Out]# 7842   423b4482c5cb  Benjamin Pollack <benjamin@bitquabit.com>    1: +4/-1
#[Out]# 7617   3e592067515d  Benjamin Pollack <benjamin@bitquabit.com>    1: +7/-9), ('Benjamin Wohlwend <bw@piquadrat.ch>',               node                               author changestr
#[Out]# n                                                                
#[Out]# 8193  c8cb471fc9c2  Benjamin Wohlwend <bw@piquadrat.ch>  1: +3/-0), ('Benoit Allard <benoit@aeteurope.nl>',                node                               author      changestr
#[Out]# n                                                                      
#[Out]# 16372  6097ede2be4d  Benoit Allard <benoit@aeteurope.nl>      5: +31/-5
#[Out]# 15455  3da1f60fc80d  Benoit Allard <benoit@aeteurope.nl>       1: +1/-1
#[Out]# 14823  2e54387976d4  Benoit Allard <benoit@aeteurope.nl>      1: +23/-5
#[Out]# 14085  b24e5a708fad  Benoit Allard <benoit@aeteurope.nl>  48: +373/-232
#[Out]# 10663  1148a968a070  Benoit Allard <benoit@aeteurope.nl>       1: +2/-0
#[Out]# 9164   07a62819b309  Benoit Allard <benoit@aeteurope.nl>      3: +13/-0
#[Out]# 7832   b61e918ea767  Benoit Allard <benoit@aeteurope.nl>       1: +1/-1
#[Out]# 7818   b6b9065c20b3  Benoit Allard <benoit@aeteurope.nl>       1: +1/-1
#[Out]# 7726   6a888d491eaf  Benoit Allard <benoit@aeteurope.nl>  24: +234/-245
#[Out]# 7545   8649b2a3de75  Benoit Allard <benoit@aeteurope.nl>       1: +5/-5
#[Out]# 7487   b7d4db95e95a  Benoit Allard <benoit@aeteurope.nl>       1: +1/-1
#[Out]# 7484   e60aaae83323  Benoit Allard <benoit@aeteurope.nl>     5: +64/-18
#[Out]# 7413   0b6428da1f22  Benoit Allard <benoit@aeteurope.nl>      3: +15/-0
#[Out]# 7409   0fa3b6677027  Benoit Allard <benoit@aeteurope.nl>       2: +7/-3
#[Out]# 7408   f031a12dfc31  Benoit Allard <benoit@aeteurope.nl>      4: +50/-4
#[Out]# 7407   7b2a77b20964  Benoit Allard <benoit@aeteurope.nl>      6: +37/-2
#[Out]# 7373   e17dbf140035  Benoit Allard <benoit@aeteurope.nl>     3: +136/-1
#[Out]# 7300   288dda59233c  Benoit Allard <benoit@aeteurope.nl>     13: +54/-0
#[Out]# 7205   b1aea76f7001  Benoit Allard <benoit@aeteurope.nl>      2: +11/-5
#[Out]# 7132   63579aa36c8e  Benoit Allard <benoit@aeteurope.nl>       4: +3/-9
#[Out]# 6810   936a9073bb73  Benoit Allard <benoit@aeteurope.nl>       3: +7/-6
#[Out]# 6791   3c715fdc7495  Benoit Allard <benoit@aeteurope.nl>       1: +0/-1
#[Out]# 6782   8251ffb35725  Benoit Allard <benoit@aeteurope.nl>       1: +1/-1
#[Out]# 6679   626cb86a6523  Benoit Allard <benoit@aeteurope.nl>     3: +108/-4
#[Out]# 6678   c15bfe9cdcd6  Benoit Allard <benoit@aeteurope.nl>       1: +7/-4
#[Out]# 6425   c30849d4c8ba  Benoit Allard <benoit@aeteurope.nl>       1: +2/-2), ('Benoit Boissinot <bboissin@gmail.com>',               node                                 author  changestr
#[Out]# n                                                                   
#[Out]# 1564  34579a67fa71  Benoit Boissinot <bboissin@gmail.com>  1: +10/-3), ('Benoit Boissinot <benoit.boissinot@ens-lyon.org',               node                                           author   changestr
#[Out]# n                                                                              
#[Out]# 1401  fbf2b10011aa  Benoit Boissinot <benoit.boissinot@ens-lyon.org    1: +6/-3
#[Out]# 1400  cf9a1233738a  Benoit Boissinot <benoit.boissinot@ens-lyon.org  13: +24/-0), ('Benoit Boissinot <benoit.boissinot@ens-lyon.org>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 926 entries, 14839 to 1045
#[Out]# Data columns:
#[Out]# node         926  non-null values
#[Out]# author       926  non-null values
#[Out]# changestr    926  non-null values
#[Out]# dtypes: object(3)), ('Benoit Boissinot <mercurial-bugs@selenic.com>',               node                                         author changestr
#[Out]# n                                                                          
#[Out]# 1454  f4250806dbeb  Benoit Boissinot <mercurial-bugs@selenic.com>  1: +2/-0
#[Out]# 1424  918cb47d725e  Benoit Boissinot <mercurial-bugs@selenic.com>  1: +9/-4), ('Beno\xc3\xaet Allard <benoit@aeteurope.nl>',               node                               author  changestr
#[Out]# n                                                                 
#[Out]# 6305  e8d447d91cdb  Benoît Allard <benoit@aeteurope.nl>  1: +2/-2), ('Bernhard Leiner <bleiner@gmail.com>',                node                               author   changestr
#[Out]# n                                                                   
#[Out]# 13770  e798e430c5e5  Bernhard Leiner <bleiner@gmail.com>   5: +16/-6
#[Out]# 13658  ffcb7e4d719f  Bernhard Leiner <bleiner@gmail.com>   5: +16/-6
#[Out]# 7579   21233de9c053  Bernhard Leiner <bleiner@gmail.com>   3: +28/-1
#[Out]# 7512   f9fcb189c8e2  Bernhard Leiner <bleiner@gmail.com>    4: +4/-1
#[Out]# 7118   75fdc39b6172  Bernhard Leiner <bleiner@gmail.com>  2: +114/-0
#[Out]# 7117   528b7fc1216c  Bernhard Leiner <bleiner@gmail.com>   1: +7/-34
#[Out]# 7116   1ca878d7b849  Bernhard Leiner <bleiner@gmail.com>  1: +167/-0
#[Out]# 6547   be2daa324ddf  Bernhard Leiner <bleiner@gmail.com>    1: +1/-1
#[Out]# 6503   6d904eb19c2a  Bernhard Leiner <bleiner@gmail.com>   2: +55/-1
#[Out]# 6502   9369095779a1  Bernhard Leiner <bleiner@gmail.com>  2: +382/-0
#[Out]# 6501   8f256bf98219  Bernhard Leiner <bleiner@gmail.com>   2: +30/-7), ('Bill Barry <after.fallout@gmail.com>',               node                                author   changestr
#[Out]# n                                                                   
#[Out]# 9078  df21a009c9c4  Bill Barry <after.fallout@gmail.com>    1: +8/-7
#[Out]# 7819  14b703252f14  Bill Barry <after.fallout@gmail.com>  1: +12/-10
#[Out]# 7696  2ceeb1423544  Bill Barry <after.fallout@gmail.com>    1: +7/-1
#[Out]# 7695  e040f9d6b2f3  Bill Barry <after.fallout@gmail.com>  2: +71/-49
#[Out]# 7693  bcdc2fe3fd07  Bill Barry <after.fallout@gmail.com>    1: +5/-6), ('Bill Schroeder <bschroeder@allstontrading.com>',               node                                          author changestr
#[Out]# n                                                                           
#[Out]# 9825  0d850f8beea6  Bill Schroeder <bschroeder@allstontrading.com>  2: +7/-6), ('Brad Schick <schickb@gmail.com>',               node                           author   changestr
#[Out]# n                                                              
#[Out]# 5199  2be225ea5722  Brad Schick <schickb@gmail.com>   3: +36/-6
#[Out]# 5198  841568ccc09d  Brad Schick <schickb@gmail.com>   2: +4/-14
#[Out]# 5197  1830bc7676ee  Brad Schick <schickb@gmail.com>  1: +56/-53), ('Brandon Parsons <parsonsb@rsn.hp.com>',                node                                 author changestr
#[Out]# n                                                                   
#[Out]# 10715  278d45703ac2  Brandon Parsons <parsonsb@rsn.hp.com>  1: +2/-0), ('Brendan Cully <brendan@kublai.com>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 624 entries, 16488 to 1664
#[Out]# Data columns:
#[Out]# node         624  non-null values
#[Out]# author       624  non-null values
#[Out]# changestr    624  non-null values
#[Out]# dtypes: object(3)), ('Brett Cannon <brett@python.org>',                node                           author  changestr
#[Out]# n                                                              
#[Out]# 10719  33119d0252c1  Brett Cannon <brett@python.org>  3: +16/-9), ('Brett Carter <brett@rdnzl.net>',               node                          author  changestr
#[Out]# n                                                            
#[Out]# 8428  39cf453da958  Brett Carter <brett@rdnzl.net>  3: +57/-2), ('Brodie Rao <brodie@bitheap.org>',                node                           author      changestr
#[Out]# n                                                                  
#[Out]# 15398  474279be5add  Brodie Rao <brodie@bitheap.org>       2: +7/-1
#[Out]# 15375  fe9d36a6853e  Brodie Rao <brodie@bitheap.org>    30: +72/-72
#[Out]# 15151  16dc9a32ca04  Brodie Rao <brodie@bitheap.org>      1: +13/-9
#[Out]# 14759  9adce4b38ed1  Brodie Rao <brodie@bitheap.org>      1: +13/-7
#[Out]# 14758  55db12e54450  Brodie Rao <brodie@bitheap.org>       1: +4/-3
#[Out]# 14140  a36e8c99d51c  Brodie Rao <brodie@bitheap.org>       1: +4/-3
#[Out]# 14139  7f45b1911893  Brodie Rao <brodie@bitheap.org>      3: +84/-2
#[Out]# 14114  c285bdb0572a  Brodie Rao <brodie@bitheap.org>      1: +21/-1
#[Out]# 14113  924c82157d46  Brodie Rao <brodie@bitheap.org>  16: +310/-311
#[Out]# 14108  b23a8dd36a21  Brodie Rao <brodie@bitheap.org>      1: +0/-74
#[Out]# 14092  ef1217a7f206  Brodie Rao <brodie@bitheap.org>       1: +1/-1
#[Out]# 13921  9f97de157aad  Brodie Rao <brodie@bitheap.org>      4: +65/-8
#[Out]# 13920  b2798c1defff  Brodie Rao <brodie@bitheap.org>       2: +9/-2
#[Out]# 13904  e574207e3bcd  Brodie Rao <brodie@bitheap.org>     7: +52/-38
#[Out]# 13903  cc383142e738  Brodie Rao <brodie@bitheap.org>       1: +3/-3
#[Out]# 13902  ec1695350361  Brodie Rao <brodie@bitheap.org>       1: +7/-5
#[Out]# 13901  ad179644750f  Brodie Rao <brodie@bitheap.org>       2: +3/-6
#[Out]# 13900  fbf32a6c903e  Brodie Rao <brodie@bitheap.org>      1: +16/-2
#[Out]# 13899  a35aff48d577  Brodie Rao <brodie@bitheap.org>      1: +7/-15
#[Out]# 13898  65b89e80f892  Brodie Rao <brodie@bitheap.org>     1: +10/-21
#[Out]# 13897  d16894e29f91  Brodie Rao <brodie@bitheap.org>     4: +15/-40
#[Out]# 13896  bf6156bab41b  Brodie Rao <brodie@bitheap.org>     2: +12/-16
#[Out]# 13895  7f18bab2c0b0  Brodie Rao <brodie@bitheap.org>      3: +16/-0
#[Out]# 13894  2540f8087e02  Brodie Rao <brodie@bitheap.org>      1: +19/-0
#[Out]# 13893  d066d8d652c8  Brodie Rao <brodie@bitheap.org>       3: +4/-5
#[Out]# 13892  03dfe0c85c1a  Brodie Rao <brodie@bitheap.org>       1: +4/-1
#[Out]# 13852  463aca32a937  Brodie Rao <brodie@bitheap.org>      1: +9/-19
#[Out]# 13851  ce6227306c9a  Brodie Rao <brodie@bitheap.org>     1: +10/-15
#[Out]# 13850  4e8f2310f310  Brodie Rao <brodie@bitheap.org>     2: +328/-0
#[Out]# 13562  994510694b1d  Brodie Rao <brodie@bitheap.org>       1: +5/-2
#[Out]# 13170  a08b49d2f116  Brodie Rao <brodie@bitheap.org>      2: +11/-2
#[Out]# 12979  6e79a3bb8c79  Brodie Rao <brodie@bitheap.org>       1: +8/-2
#[Out]# 12978  2956945c3bee  Brodie Rao <brodie@bitheap.org>       1: +2/-0
#[Out]# 12700  14853ca7e11b  Brodie Rao <brodie@bitheap.org>      2: +19/-1
#[Out]# 12698  05077896ffe2  Brodie Rao <brodie@bitheap.org>      1: +31/-4
#[Out]# 12697  04f6de46bf3a  Brodie Rao <brodie@bitheap.org>      1: +17/-3
#[Out]# 12696  33f0682ba8b1  Brodie Rao <brodie@bitheap.org>       1: +5/-4
#[Out]# 12684  bc13e17067d9  Brodie Rao <brodie@bitheap.org>     4: +10/-10
#[Out]# 12663  6ed5ae6264c2  Brodie Rao <brodie@bitheap.org>       1: +4/-0
#[Out]# 12662  5aa5cbaf6efc  Brodie Rao <brodie@bitheap.org>      1: +22/-6
#[Out]# 12660  7de9033167f3  Brodie Rao <brodie@bitheap.org>       1: +1/-1
#[Out]# 12640  42ca7aef28d3  Brodie Rao <brodie@bitheap.org>      2: +13/-3
#[Out]# 12639  c24215aa7e69  Brodie Rao <brodie@bitheap.org>       1: +2/-5
#[Out]# 12638  45ef87f41f98  Brodie Rao <brodie@bitheap.org>      1: +14/-0
#[Out]# 12635  6c98107f787e  Brodie Rao <brodie@bitheap.org>     3: +54/-61
#[Out]# 12622  7178f6fedb9d  Brodie Rao <brodie@bitheap.org>       1: +1/-1
#[Out]# 12610  f1646efc54a6  Brodie Rao <brodie@bitheap.org>     3: +59/-58
#[Out]# 12534  e7d45e41338c  Brodie Rao <brodie@bitheap.org>       1: +1/-1
#[Out]# 12533  b37d5ecc2227  Brodie Rao <brodie@bitheap.org>       1: +2/-2
#[Out]# 12532  f7dd8bffe18c  Brodie Rao <brodie@bitheap.org>      1: +13/-0
#[Out]# 12528  deeef07c6e7d  Brodie Rao <brodie@bitheap.org>       1: +1/-1
#[Out]# 12527  596ad02eabe4  Brodie Rao <brodie@bitheap.org>       1: +2/-2
#[Out]# 12437  0eaf7d32a5d8  Brodie Rao <brodie@bitheap.org>       2: +8/-1
#[Out]# 12436  78a97859b90d  Brodie Rao <brodie@bitheap.org>      3: +24/-5
#[Out]# 12421  4f8067c94729  Brodie Rao <brodie@bitheap.org>    11: +16/-16
#[Out]# 12416  97ffc68f71d3  Brodie Rao <brodie@bitheap.org>  39: +201/-175
#[Out]# 12415  02990e22150b  Brodie Rao <brodie@bitheap.org>  41: +249/-220
#[Out]# 12414  4e7dd28db0dd  Brodie Rao <brodie@bitheap.org>       1: +2/-1
#[Out]# 12413  58885f00b998  Brodie Rao <brodie@bitheap.org>       1: +1/-1
#[Out]# 12412  5163e3c8aa52  Brodie Rao <brodie@bitheap.org>    17: +92/-92
#[Out]# 12366  f2daa6ab514a  Brodie Rao <brodie@bitheap.org>    15: +32/-32
#[Out]# 12236  c85e07a2d783  Brodie Rao <brodie@bitheap.org>       1: +6/-0
#[Out]# 12220  b6cc68ef2702  Brodie Rao <brodie@bitheap.org>       1: +1/-1
#[Out]# 12182  cd895084a4cd  Brodie Rao <brodie@bitheap.org>       1: +6/-1
#[Out]# 12181  4982fa38e544  Brodie Rao <brodie@bitheap.org>       1: +4/-2
#[Out]# 12169  49463314c24f  Brodie Rao <brodie@bitheap.org>      7: +35/-8
#[Out]# 12159  516b000fbb7e  Brodie Rao <brodie@bitheap.org>       8: +4/-9
#[Out]# 12158  c327bfa5e831  Brodie Rao <brodie@bitheap.org>     9: +10/-12
#[Out]# 12125  8508dd698c02  Brodie Rao <brodie@bitheap.org>   3: +110/-109
#[Out]# 11914  26e413f55b5e  Brodie Rao <brodie@bitheap.org>     2: +23/-22
#[Out]# 11739  89df79b3c011  Brodie Rao <brodie@bitheap.org>     3: +40/-15
#[Out]# 11707  9a93f4fb141b  Brodie Rao <brodie@bitheap.org>       1: +1/-1
#[Out]# 11692  40c40c6f20b8  Brodie Rao <brodie@bitheap.org>       3: +8/-1
#[Out]# 11684  4481f8a93c7a  Brodie Rao <brodie@bitheap.org>     3: +31/-14
#[Out]# 11654  07ac2a560fce  Brodie Rao <brodie@bitheap.org>      3: +34/-9
#[Out]# 11651  ebfc46929f3e  Brodie Rao <brodie@bitheap.org>    10: +42/-39
#[Out]# 11636  18e1e7520b67  Brodie Rao <brodie@bitheap.org>       1: +7/-3
#[Out]# 11624  3145951e50fe  Brodie Rao <brodie@bitheap.org>       2: +6/-6
#[Out]# 11623  d2796a3cb816  Brodie Rao <brodie@bitheap.org>       1: +1/-1
#[Out]# 11572  386e56ecfb78  Brodie Rao <brodie@bitheap.org>      3: +15/-1
#[Out]# 11570  c34a1ab80550  Brodie Rao <brodie@bitheap.org>       1: +2/-2
#[Out]# 11556  e4357c214bf1  Brodie Rao <brodie@bitheap.org>      3: +20/-1
#[Out]# 11547  91af149b5cd7  Brodie Rao <brodie@bitheap.org>     2: +21/-18
#[Out]# 11528  e5aaaef91a27  Brodie Rao <brodie@bitheap.org>       3: +9/-1
#[Out]# 11527  d8d0fc3988ca  Brodie Rao <brodie@bitheap.org>     5: +73/-60
#[Out]# 11237  ebc90fd4ebc0  Brodie Rao <brodie@bitheap.org>      1: +10/-3
#[Out]# 10949  441f5d66da03  Brodie Rao <brodie@bitheap.org>       1: +5/-2
#[Out]# 10945  b66388f6adfa  Brodie Rao <brodie@bitheap.org>       2: +7/-9
#[Out]# 10944  717c35d55fb3  Brodie Rao <brodie@bitheap.org>  16: +184/-297
#[Out]# 10943  781689b9b6bb  Brodie Rao <brodie@bitheap.org>      1: +12/-1
#[Out]# 10942  18def0d5692d  Brodie Rao <brodie@bitheap.org>       1: +9/-9
#[Out]# 10941  581d5e3095ef  Brodie Rao <brodie@bitheap.org>      1: +13/-6
#[Out]# 10940  4c63f8e787b8  Brodie Rao <brodie@bitheap.org>      1: +11/-1
#[Out]# 10939  a6ac91c313af  Brodie Rao <brodie@bitheap.org>       1: +4/-2
#[Out]# 10938  da809085bc9f  Brodie Rao <brodie@bitheap.org>      1: +11/-4
#[Out]# 10937  36c6a667d733  Brodie Rao <brodie@bitheap.org>     1: +35/-20
#[Out]# 10936  d14d45fae927  Brodie Rao <brodie@bitheap.org>      2: +63/-5
#[Out]# 10935  2096496b40ec  Brodie Rao <brodie@bitheap.org>       1: +7/-3
#[Out]# 10934  635d601e8f21  Brodie Rao <brodie@bitheap.org>      1: +10/-2
#[Out]# 10933  32b213b9b22c  Brodie Rao <brodie@bitheap.org>     2: +70/-13
#[Out]# 10903  92ff2d0b751a  Brodie Rao <brodie@bitheap.org>       1: +1/-0
#[Out]# 10780  ccb4057e19e6  Brodie Rao <brodie@bitheap.org>      1: +10/-3
#[Out]# 10766  3c368a1c962d  Brodie Rao <brodie@bitheap.org>      2: +24/-3), ('Brodie Rao <brodie@sf.io>',                node                     author   changestr
#[Out]# n                                                         
#[Out]# 16592  369741ef7253  Brodie Rao <brodie@sf.io>  1: +17/-27), ('Brodie Rao <me+hg@dackz.net>',                node                        author     changestr
#[Out]# n                                                              
#[Out]# 10613  181cbb23572e  Brodie Rao <me+hg@dackz.net>      1: +8/-7
#[Out]# 10513  80a1161bc3b5  Brodie Rao <me+hg@dackz.net>      1: +1/-0
#[Out]# 10505  79dd96774187  Brodie Rao <me+hg@dackz.net>      3: +8/-6
#[Out]# 10504  42afde35e9f7  Brodie Rao <me+hg@dackz.net>      3: +5/-0
#[Out]# 10476  2253715fde97  Brodie Rao <me+hg@dackz.net>    5: +73/-42
#[Out]# 10463  5ddde896a19d  Brodie Rao <me+hg@dackz.net>      7: +3/-7
#[Out]# 10455  40dfd46d098f  Brodie Rao <me+hg@dackz.net>     5: +56/-1
#[Out]# 10453  7edc649f9f7e  Brodie Rao <me+hg@dackz.net>      1: +4/-1
#[Out]# 10452  59f8fff4f887  Brodie Rao <me+hg@dackz.net>      1: +1/-7
#[Out]# 10368  de1e7099d100  Brodie Rao <me+hg@dackz.net>   6: +158/-20
#[Out]# 10367  c07974215b3d  Brodie Rao <me+hg@dackz.net>    1: +34/-20
#[Out]# 10110  0022f5c5459e  Brodie Rao <me+hg@dackz.net>     4: +17/-0
#[Out]# 9841   7cd6dee6fe37  Brodie Rao <me+hg@dackz.net>      1: +8/-3
#[Out]# 9642   7d17794f08a9  Brodie Rao <me+hg@dackz.net>    5: +30/-10
#[Out]# 9641   9b99f158348a  Brodie Rao <me+hg@dackz.net>     3: +23/-1
#[Out]# 9640   9e76232fbfbe  Brodie Rao <me+hg@dackz.net>     6: +67/-6
#[Out]# 9639   5384a22ab698  Brodie Rao <me+hg@dackz.net>      1: +2/-2
#[Out]# 9585   c06e7581bbaa  Brodie Rao <me+hg@dackz.net>     2: +30/-1
#[Out]# 9518   32ec70799172  Brodie Rao <me+hg@dackz.net>      1: +1/-1
#[Out]# 9458   3fb8c6dbeeec  Brodie Rao <me+hg@dackz.net>      1: +5/-5
#[Out]# 9406   be2a13153372  Brodie Rao <me+hg@dackz.net>     1: +11/-8
#[Out]# 9192   95046688f80f  Brodie Rao <me+hg@dackz.net>    3: +16/-16
#[Out]# 9168   ef440eab290f  Brodie Rao <me+hg@dackz.net>      2: +0/-2
#[Out]# 9025   5e4654f5522d  Brodie Rao <me+hg@dackz.net>      1: +5/-6
#[Out]# 9015   438f0b1d4684  Brodie Rao <me+hg@dackz.net>    3: +16/-16
#[Out]# 8982   9c0cecb71350  Brodie Rao <me+hg@dackz.net>      1: +2/-1
#[Out]# 8963   a4ceae3aa7be  Brodie Rao <me+hg@dackz.net>     1: +15/-3
#[Out]# 8962   4aade1a0115b  Brodie Rao <me+hg@dackz.net>      1: +1/-1
#[Out]# 8352   493d23d923ea  Brodie Rao <me+hg@dackz.net>      1: +1/-1
#[Out]# 7854   f62482848d1b  Brodie Rao <me+hg@dackz.net>      1: +1/-1
#[Out]# 7792   089cb73f8ecc  Brodie Rao <me+hg@dackz.net>      1: +1/-0
#[Out]# 7459   3fb5c142a9f0  Brodie Rao <me+hg@dackz.net>  3: +130/-135
#[Out]# 7456   79eb16db5e4a  Brodie Rao <me+hg@dackz.net>    1: +80/-11
#[Out]# 7455   c9fd5474a707  Brodie Rao <me+hg@dackz.net>     1: +17/-8), ("Bryan O'Sullivan <bos@serpentine.com>", <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 427 entries, 10821 to 613
#[Out]# Data columns:
#[Out]# node         427  non-null values
#[Out]# author       427  non-null values
#[Out]# changestr    427  non-null values
#[Out]# dtypes: object(3)), ("Bryan O'Sullivan <bryano@fb.com>",                node                            author     changestr
#[Out]# n                                                                  
#[Out]# 16637  9da5a2864f3f  Bryan O'Sullivan <bryano@fb.com>      1: +1/-1
#[Out]# 16609  2950d186a927  Bryan O'Sullivan <bryano@fb.com>    2: +10/-10
#[Out]# 16602  e6dfbc5df76f  Bryan O'Sullivan <bryano@fb.com>      1: +5/-3
#[Out]# 16590  e22d6b1dec1d  Bryan O'Sullivan <bryano@fb.com>      1: +6/-2
#[Out]# 16589  bc84a1aeaf5a  Bryan O'Sullivan <bryano@fb.com>     2: +28/-0
#[Out]# 16576  e462313ef1bd  Bryan O'Sullivan <bryano@fb.com>      1: +1/-0
#[Out]# 16567  8d44b5a2974f  Bryan O'Sullivan <bryano@fb.com>    1: +22/-31
#[Out]# 16467  7f59900e3f8b  Bryan O'Sullivan <bryano@fb.com>      1: +2/-1
#[Out]# 16428  d54d4de56aa7  Bryan O'Sullivan <bryano@fb.com>      2: +6/-7
#[Out]# 16424  a150923b49ba  Bryan O'Sullivan <bryano@fb.com>      1: +4/-4
#[Out]# 16416  e8d37b78acfb  Bryan O'Sullivan <bryano@fb.com>   4: +577/-51
#[Out]# 16406  9fca5b056c0a  Bryan O'Sullivan <bryano@fb.com>    1: +18/-18
#[Out]# 16405  efae1fea4bbd  Bryan O'Sullivan <bryano@fb.com>     1: +18/-0
#[Out]# 16397  ee3f423df1b4  Bryan O'Sullivan <bryano@fb.com>    2: +93/-38
#[Out]# 16395  4df76d5506a9  Bryan O'Sullivan <bryano@fb.com>     1: +14/-5
#[Out]# 16376  28bb4daf070c  Bryan O'Sullivan <bryano@fb.com>     1: +27/-7
#[Out]# 16373  2cdd7e63211b  Bryan O'Sullivan <bryano@fb.com>  2: +404/-100), ('Carey Evans <carey@carey.geek.nz>',               node                             author changestr
#[Out]# n                                                              
#[Out]# 9102  7116494c48ab  Carey Evans <carey@carey.geek.nz>  1: +1/-1), ('Cesar Mena <cesarmena@gmail.com>',                node                            author changestr
#[Out]# n                                                              
#[Out]# 16493  72c6240a4b7d  Cesar Mena <cesarmena@gmail.com>  1: +1/-1), ('Chad Dombrova <chadrik@gmail.com>',                node                             author   changestr
#[Out]# n                                                                 
#[Out]# 11330  713ae78bb583  Chad Dombrova <chadrik@gmail.com>  3: +21/-10
#[Out]# 11244  d6dbd5e4ee72  Chad Dombrova <chadrik@gmail.com>   3: +27/-0
#[Out]# 11243  f23f87462c18  Chad Dombrova <chadrik@gmail.com>    3: +7/-4), ('Chia-Huan Wu <willie.tw@gmail.com>',                node                              author       changestr
#[Out]# n                                                                      
#[Out]# 12903  13fb555677fe  Chia-Huan Wu <willie.tw@gmail.com>  1: +6556/-4495
#[Out]# 8828   49273e107818  Chia-Huan Wu <willie.tw@gmail.com>     1: +9255/-0), ('Chris Mason <mason@suse.com>',               node                        author      changestr
#[Out]# n                                                              
#[Out]# 2699  f8bcaf5696d5  Chris Mason <mason@suse.com>       1: +3/-0
#[Out]# 2698  c1123e83c8e2  Chris Mason <mason@suse.com>      1: +11/-2
#[Out]# 2697  6c540dd14c38  Chris Mason <mason@suse.com>      1: +14/-5
#[Out]# 2696  be273f6074de  Chris Mason <mason@suse.com>     1: +69/-15
#[Out]# 2609  6c5b1b5cc160  Chris Mason <mason@suse.com>       1: +7/-1
#[Out]# 2512  e4deeaac5e74  Chris Mason <mason@suse.com>       1: +0/-1
#[Out]# 2511  041d8f0a8437  Chris Mason <mason@suse.com>      1: +12/-4
#[Out]# 2491  ffde9eb23f59  Chris Mason <mason@suse.com>       1: +1/-1
#[Out]# 2474  1e32e2fe8a67  Chris Mason <mason@suse.com>      1: +12/-4
#[Out]# 2101  c6c019fd5db1  Chris Mason <mason@suse.com>       1: +5/-1
#[Out]# 2098  190c6a81e6ad  Chris Mason <mason@suse.com>       1: +0/-1
#[Out]# 2085  f71e9656524f  Chris Mason <mason@suse.com>  15: +1224/-98
#[Out]# 2084  d66278012853  Chris Mason <mason@suse.com>      2: +34/-7
#[Out]# 2083  345107e167a0  Chris Mason <mason@suse.com>    10: +49/-47
#[Out]# 2081  416d8b2a75b8  Chris Mason <mason@suse.com>      1: +18/-0
#[Out]# 1245  d0a960b437a8  Chris Mason <mason@suse.com>       1: +1/-1), ('Chris Winter <elwintro@gmail.com>',               node                             author   changestr
#[Out]# n                                                                
#[Out]# 7361  42f1b8cb9a60  Chris Winter <elwintro@gmail.com>  3: +125/-2), ('Christian Boos <cboos@bct-technology.com>',               node                                     author   changestr
#[Out]# n                                                                        
#[Out]# 9856  ed362d41d1f6  Christian Boos <cboos@bct-technology.com>    1: +2/-0
#[Out]# 9815  49efeed49c94  Christian Boos <cboos@bct-technology.com>  5: +58/-15
#[Out]# 9807  f359d4f528aa  Christian Boos <cboos@bct-technology.com>    1: +3/-3), ('Christian Boos <cboos@neuf.fr>',                node                          author  changestr
#[Out]# n                                                             
#[Out]# 11468  1c1126b1d919  Christian Boos <cboos@neuf.fr>  1: +20/-2
#[Out]# 6881   6a9025a667ae  Christian Boos <cboos@neuf.fr>   1: +1/-1
#[Out]# 2243   caf2c6ef5b0e  Christian Boos <cboos@neuf.fr>   1: +4/-0
#[Out]# 1562   2f97af0b522c  Christian Boos <cboos@neuf.fr>   1: +4/-4
#[Out]# 1504   0fcdd126642d  Christian Boos <cboos@neuf.fr>   1: +4/-4), ('Christian Ebert <blacktrash@gmx.net>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 244 entries, 15669 to 1647
#[Out]# Data columns:
#[Out]# node         244  non-null values
#[Out]# author       244  non-null values
#[Out]# changestr    244  non-null values
#[Out]# dtypes: object(3)), ('Christian Fischer <christian@fi12.de>',                node                                 author changestr
#[Out]# n                                                                   
#[Out]# 11548  48163c39e1f1  Christian Fischer <christian@fi12.de>  1: +2/-1), ('Christoph  <christoph@webvariants.de>',                node                                 author         changestr
#[Out]# n                                                                           
#[Out]# 12572  5a19b576df52  Christoph  <christoph@webvariants.de>        1: +91/-67
#[Out]# 12570  0788d6194a2c  Christoph  <christoph@webvariants.de>   1: +1625/-10520
#[Out]# 12568  2eadea60ae67  Christoph  <christoph@webvariants.de>       1: +255/-87
#[Out]# 12567  d9b82da3db29  Christoph  <christoph@webvariants.de>  1: +24508/-19479
#[Out]# 12349  5f1f0ff652a9  Christoph  <christoph@webvariants.de>      1: +157/-156
#[Out]# 12348  e1ec3b7e879d  Christoph  <christoph@webvariants.de>       1: +310/-63
#[Out]# 12347  c078dc5d9ca3  Christoph  <christoph@webvariants.de>        1: +77/-19), ('Christoph <christoph@webvariants.de>',                node                                author      changestr
#[Out]# n                                                                       
#[Out]# 12581  4360afc3c3cd  Christoph <christoph@webvariants.de>  2: +168/-1116), ('Christoph Mewes <christoph@webvariants.de>',                node                                      author     changestr
#[Out]# n                                                                            
#[Out]# 12588  12f58fa94a31  Christoph Mewes <christoph@webvariants.de>     1: +16/-2
#[Out]# 12587  8b0c72802f7c  Christoph Mewes <christoph@webvariants.de>     1: +35/-2
#[Out]# 12586  4873744a9a3b  Christoph Mewes <christoph@webvariants.de>     1: +15/-2
#[Out]# 12585  14a266c36a64  Christoph Mewes <christoph@webvariants.de>    1: +14/-15
#[Out]# 12584  7d58c09887cc  Christoph Mewes <christoph@webvariants.de>     1: +61/-6
#[Out]# 12583  35b68005726e  Christoph Mewes <christoph@webvariants.de>  1: +438/-197
#[Out]# 12580  7e6ac934a167  Christoph Mewes <christoph@webvariants.de>   1: +110/-30
#[Out]# 12579  5663ff50073c  Christoph Mewes <christoph@webvariants.de>     1: +13/-3
#[Out]# 12578  e91302597078  Christoph Mewes <christoph@webvariants.de>    1: +23/-23), ('Christoph Spiel <cspiel@freenet.de>',               node                               author changestr
#[Out]# n                                                                
#[Out]# 5348  5737845fd974  Christoph Spiel <cspiel@freenet.de>  1: +3/-2
#[Out]# 5347  058e93c3d07d  Christoph Spiel <cspiel@freenet.de>  1: +9/-2), ('Colin Caughie <c.caughie@indigovision.com>',                node                                      author  changestr
#[Out]# n                                                                         
#[Out]# 13086  278e3c9b939e  Colin Caughie <c.caughie@indigovision.com>   1: +3/-0
#[Out]# 12936  75e4fade4ad9  Colin Caughie <c.caughie@indigovision.com>  2: +44/-0
#[Out]# 8817   6c9dce20ed70  Colin Caughie <c.caughie@indigovision.com>   3: +8/-7), ('Colin McMillen <mcmillen@cs.cmu.edu>',               node                                author changestr
#[Out]# n                                                                 
#[Out]# 2170  29eeb2717915  Colin McMillen <mcmillen@cs.cmu.edu>  2: +3/-1
#[Out]# 2168  dd4ec4576cc8  Colin McMillen <mcmillen@cs.cmu.edu>  1: +7/-2
#[Out]# 2162  dac432a521d8  Colin McMillen <mcmillen@cs.cmu.edu>  1: +1/-0
#[Out]# 2148  c72e618c1204  Colin McMillen <mcmillen@cs.cmu.edu>  2: +8/-2), ('Constantine Linnick <theaspect@gmail.com>',                node                                     author    changestr
#[Out]# n                                                                          
#[Out]# 16250  33f702e52906  Constantine Linnick <theaspect@gmail.com>   4: +32/-15
#[Out]# 16249  5e50982c633c  Constantine Linnick <theaspect@gmail.com>  5: +158/-45), ('Craig Leres <leres@ee.lbl.gov>',                node                          author changestr
#[Out]# n                                                            
#[Out]# 13753  537899158396  Craig Leres <leres@ee.lbl.gov>  1: +1/-0), ('C\xc3\xa9dric Duval <cedricduval@free.fr>',                node                              author      changestr
#[Out]# n                                                                     
#[Out]# 11273  d1aca0863a9d  Cédric Duval <cedricduval@free.fr>     3: +15/-5
#[Out]# 11184  f66ca4431eb9  Cédric Duval <cedricduval@free.fr>     3: +76/-2
#[Out]# 10894  7a0502a6f9a1  Cédric Duval <cedricduval@free.fr>     3: +56/-2
#[Out]# 10627  47fbbc4845ff  Cédric Duval <cedricduval@free.fr>      2: +7/-0
#[Out]# 10620  a778a367c20b  Cédric Duval <cedricduval@free.fr>     3: +29/-1
#[Out]# 10619  ea85c01c7835  Cédric Duval <cedricduval@free.fr>      2: +3/-3
#[Out]# 10618  3b3bf520b428  Cédric Duval <cedricduval@free.fr>      2: +0/-2
#[Out]# 9389   5724cd7b3688  Cédric Duval <cedricduval@free.fr>     1: +11/-0
#[Out]# 9367   a8fdcec4ab34  Cédric Duval <cedricduval@free.fr>      2: +4/-4
#[Out]# 9195   8263d98ffb1c  Cédric Duval <cedricduval@free.fr>    2: +40/-40
#[Out]# 9194   1547126630e9  Cédric Duval <cedricduval@free.fr>      2: +5/-5
#[Out]# 9172   609b803dd252  Cédric Duval <cedricduval@free.fr>      1: +0/-4
#[Out]# 9165   ada93c6bf554  Cédric Duval <cedricduval@free.fr>      1: +2/-2
#[Out]# 9076   b6cb3af61582  Cédric Duval <cedricduval@free.fr>      1: +2/-4
#[Out]# 9070   2ab9ec0f9703  Cédric Duval <cedricduval@free.fr>    1: +33/-21
#[Out]# 9069   38d8b0255189  Cédric Duval <cedricduval@free.fr>    1: +40/-30
#[Out]# 9068   e4e7430bf1d2  Cédric Duval <cedricduval@free.fr>    1: +21/-18
#[Out]# 9067   a3a22aa6bf82  Cédric Duval <cedricduval@free.fr>     1: +36/-9
#[Out]# 9066   f27de22d39cd  Cédric Duval <cedricduval@free.fr>    1: +49/-20
#[Out]# 9042   335f749cc369  Cédric Duval <cedricduval@free.fr>      1: +3/-1
#[Out]# 9013   2ccb527c7b1a  Cédric Duval <cedricduval@free.fr>      1: +3/-1
#[Out]# 9006   901cdaa2349d  Cédric Duval <cedricduval@free.fr>  1: +310/-153
#[Out]# 9005   5d032751a610  Cédric Duval <cedricduval@free.fr>     1: +18/-0
#[Out]# 9004   a071bf50e984  Cédric Duval <cedricduval@free.fr>     1: +36/-8
#[Out]# 9003   a4f2b694b404  Cédric Duval <cedricduval@free.fr>     1: +22/-2
#[Out]# 9002   134b37b27c20  Cédric Duval <cedricduval@free.fr>    1: +84/-63
#[Out]# 8977   d414749e059f  Cédric Duval <cedricduval@free.fr>     1: +41/-1
#[Out]# 8976   8b4e20617216  Cédric Duval <cedricduval@free.fr>    1: +24/-11
#[Out]# 8975   09a35d1aaaa9  Cédric Duval <cedricduval@free.fr>   1: +178/-39
#[Out]# 8974   d48080feb1ae  Cédric Duval <cedricduval@free.fr>     1: +80/-0
#[Out]# 8973   ba322663d157  Cédric Duval <cedricduval@free.fr>   1: +8574/-0
#[Out]# 8964   119d1f664eae  Cédric Duval <cedricduval@free.fr>      1: +6/-1
#[Out]# 8904   8be38b624902  Cédric Duval <cedricduval@free.fr>      1: +7/-9
#[Out]# 8896   b793ce68f082  Cédric Duval <cedricduval@free.fr>      1: +1/-1
#[Out]# 8895   ef59f4634a15  Cédric Duval <cedricduval@free.fr>      1: +1/-1
#[Out]# 8894   868670dbc237  Cédric Duval <cedricduval@free.fr>   30: +36/-38
#[Out]# 8893   cc0593af30d4  Cédric Duval <cedricduval@free.fr>    1: +24/-16
#[Out]# 8892   30b25ebaa63b  Cédric Duval <cedricduval@free.fr>    1: +15/-13
#[Out]# 8879   d0a3eadfbdb3  Cédric Duval <cedricduval@free.fr>    2: +28/-31
#[Out]# 8878   231f9d92fd7a  Cédric Duval <cedricduval@free.fr>      1: +1/-8
#[Out]# 8877   08636e18268f  Cédric Duval <cedricduval@free.fr>      1: +3/-1
#[Out]# 8871   20a25042fadc  Cédric Duval <cedricduval@free.fr>    3: +79/-82
#[Out]# 8866   87c30fb7e8df  Cédric Duval <cedricduval@free.fr>    10: +4/-60
#[Out]# 8865   37d8a5ddd499  Cédric Duval <cedricduval@free.fr>     1: +30/-6
#[Out]# 8864   cad6370a15cb  Cédric Duval <cedricduval@free.fr>    2: +35/-16
#[Out]# 8863   7b19c3c0172b  Cédric Duval <cedricduval@free.fr>    3: +116/-1
#[Out]# 8826   2aff285b902f  Cédric Duval <cedricduval@free.fr>      1: +7/-0
#[Out]# 8824   67ee7587abea  Cédric Duval <cedricduval@free.fr>    1: +19/-17
#[Out]# 8823   d9f4c182aeca  Cédric Duval <cedricduval@free.fr>     1: +14/-9
#[Out]# 8822   1027da7d2fb9  Cédric Duval <cedricduval@free.fr>      1: +1/-1
#[Out]# 8657   f6cc3638f468  Cédric Duval <cedricduval@free.fr>      1: +4/-4
#[Out]# 8656   aa011d123f71  Cédric Duval <cedricduval@free.fr>    1: +84/-87
#[Out]# 8640   c88c8d59979f  Cédric Duval <cedricduval@free.fr>      2: +2/-2
#[Out]# 8621   cf6f567e27e9  Cédric Duval <cedricduval@free.fr>      1: +1/-1
#[Out]# 8620   7af21dfae9d5  Cédric Duval <cedricduval@free.fr>      1: +1/-1
#[Out]# 8519   252232621165  Cédric Duval <cedricduval@free.fr>     3: +82/-1
#[Out]# 8517   b87e5ad94229  Cédric Duval <cedricduval@free.fr>      1: +5/-5
#[Out]# 8516   32ff5ba0d312  Cédric Duval <cedricduval@free.fr>      1: +3/-3
#[Out]# 8515   f3ad1ed099e1  Cédric Duval <cedricduval@free.fr>      1: +1/-1
#[Out]# 8479   69f51fd9fb48  Cédric Duval <cedricduval@free.fr>      1: +3/-2
#[Out]# 8477   e88cc16ba603  Cédric Duval <cedricduval@free.fr>      1: +5/-5), ('C\xc3\xa9dric Krier <ced@b2ck.com>',                node                       author   changestr
#[Out]# n                                                           
#[Out]# 14812  a95242af945c  Cédric Krier <ced@b2ck.com>  2: +50/-5
#[Out]# 14338  c322890b03e6  Cédric Krier <ced@b2ck.com>  2: +28/-4), ('Dan Connolly <http://www.w3.org/People/Connolly/>',                node                                             author changestr
#[Out]# n                                                                               
#[Out]# 10733  3b89899934a6  Dan Connolly <http://www.w3.org/People/Connolly/>  1: +3/-2), ('Dan Drake <drake@kaist.edu>',                node                       author changestr
#[Out]# n                                                         
#[Out]# 11546  88b89ace643b  Dan Drake <drake@kaist.edu>  1: +1/-1), ('Dan Villiom Podlaski Christiansen  <danchr@gmail.com>',                node                                             author  changestr
#[Out]# n                                                                                
#[Out]# 16093  f346de4dff57  Dan Villiom Podlaski Christiansen  <danchr@gmail.  2: +22/-4
#[Out]# 15807  c7a8164c61ab  Dan Villiom Podlaski Christiansen  <danchr@gmail.   2: +5/-4
#[Out]# 15806  3e5b6045ccfc  Dan Villiom Podlaski Christiansen  <danchr@gmail.  2: +11/-6
#[Out]# 15795  927712d9853b  Dan Villiom Podlaski Christiansen  <danchr@gmail.   1: +0/-2
#[Out]# 15102  adad8d68fb1f  Dan Villiom Podlaski Christiansen  <danchr@gmail.   1: +2/-1
#[Out]# 14883  deed405e8980  Dan Villiom Podlaski Christiansen  <danchr@gmail.   1: +1/-1), ('Dan Villiom Podlaski Christiansen <dan@cabo.dk>',                node                                           author changestr
#[Out]# n                                                                             
#[Out]# 15101  110d6804bfc6  Dan Villiom Podlaski Christiansen <dan@cabo.dk>  1: +1/-0
#[Out]# 14884  db0646afb725  Dan Villiom Podlaski Christiansen <dan@cabo.dk>  1: +1/-1), ('Dan Villiom Podlaski Christiansen <danchr@gmail.com>',                node                                             author         changestr
#[Out]# n                                                                                       
#[Out]# 14200  1b4b82063ce2  Dan Villiom Podlaski Christiansen <danchr@gmail.c         1: +12/-0
#[Out]# 14199  135e244776f0  Dan Villiom Podlaski Christiansen <danchr@gmail.c       22: +48/-45
#[Out]# 14198  0e4753807c93  Dan Villiom Podlaski Christiansen <danchr@gmail.c         2: +20/-6
#[Out]# 14197  9cbff8a39a2a  Dan Villiom Podlaski Christiansen <danchr@gmail.c         1: +12/-7
#[Out]# 14185  839086b25c36  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +6/-5
#[Out]# 14182  4b7e4b9db8fb  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +1/-1
#[Out]# 14136  0824a0a3cefc  Dan Villiom Podlaski Christiansen <danchr@gmail.c         1: +14/-0
#[Out]# 14134  ca3376f044f8  Dan Villiom Podlaski Christiansen <danchr@gmail.c         1: +14/-0
#[Out]# 14133  dea93484cf9f  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +2/-1
#[Out]# 14129  222c8ec7a274  Dan Villiom Podlaski Christiansen <danchr@gmail.c        1: +10/-10
#[Out]# 14128  0aa60e4e0b76  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +8/-8
#[Out]# 14127  e24b5e3c2f27  Dan Villiom Podlaski Christiansen <danchr@gmail.c         2: +13/-3
#[Out]# 14126  d3f7e110c3c0  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +8/-1
#[Out]# 14103  14fac6c0536a  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +4/-2
#[Out]# 14102  8f7132fa5e59  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +4/-4
#[Out]# 14094  bcfe78c3d15c  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +4/-2
#[Out]# 13828  26f8844d1757  Dan Villiom Podlaski Christiansen <danchr@gmail.c          2: +2/-1
#[Out]# 13817  16118b4859a1  Dan Villiom Podlaski Christiansen <danchr@gmail.c         3: +41/-2
#[Out]# 13400  14f3795a5ed7  Dan Villiom Podlaski Christiansen <danchr@gmail.c       19: +89/-20
#[Out]# 13252  1775382ff833  Dan Villiom Podlaski Christiansen <danchr@gmail.c          2: +9/-3
#[Out]# 13186  bf763946f8b0  Dan Villiom Podlaski Christiansen <danchr@gmail.c          2: +3/-2
#[Out]# 13169  f7d6750dcd01  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +4/-1
#[Out]# 13155  c97ded7b6e79  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +4/-3
#[Out]# 13154  c0290fc6b486  Dan Villiom Podlaski Christiansen <danchr@gmail.c          2: +2/-1
#[Out]# 13153  4db5bfea1b07  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +7/-4
#[Out]# 13152  79184986658c  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +2/-0
#[Out]# 13151  bdb73eede5fb  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +0/-1
#[Out]# 13112  6bdae8ea0b48  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +2/-2
#[Out]# 12945  e98bf6948092  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +1/-1
#[Out]# 12944  ea68947ad0ce  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +1/-1
#[Out]# 12927  e339346a9b05  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +2/-2
#[Out]# 12865  4c50552fc9bc  Dan Villiom Podlaski Christiansen <danchr@gmail.c        14: +0/-23
#[Out]# 12864  ef0b8b1bcd63  Dan Villiom Podlaski Christiansen <danchr@gmail.c          0: +0/-0
#[Out]# 12758  62c8f7691bc3  Dan Villiom Podlaski Christiansen <danchr@gmail.c          5: +7/-6
#[Out]# 12689  fe31f834a9ff  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +1/-1
#[Out]# 12686  ada47c38f4e5  Dan Villiom Podlaski Christiansen <danchr@gmail.c         2: +26/-2
#[Out]# 12682  5ce3a1eb7f88  Dan Villiom Podlaski Christiansen <danchr@gmail.c        1: +23/-23
#[Out]# 12665  10da5a1f25dd  Dan Villiom Podlaski Christiansen <danchr@gmail.c         2: +57/-2
#[Out]# 12661  97d7ee445e98  Dan Villiom Podlaski Christiansen <danchr@gmail.c         2: +13/-1
#[Out]# 12658  5192b24f309c  Dan Villiom Podlaski Christiansen <danchr@gmail.c          2: +5/-2
#[Out]# 12430  b014f998959d  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +3/-0
#[Out]# 12411  48a4acd1ccf1  Dan Villiom Podlaski Christiansen <danchr@gmail.c          2: +5/-1
#[Out]# 12410  f98010f57a5e  Dan Villiom Podlaski Christiansen <danchr@gmail.c   21: +1307/-1173
#[Out]# 12407  3acd5f7ab9d0  Dan Villiom Podlaski Christiansen <danchr@gmail.c          2: +2/-1
#[Out]# 12396  e7e3b0618d8d  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +5/-3
#[Out]# 12231  0a0592f8e11a  Dan Villiom Podlaski Christiansen <danchr@gmail.c      3: +152/-149
#[Out]# 12168  f585c9bb85c1  Dan Villiom Podlaski Christiansen <danchr@gmail.c      3: +305/-311
#[Out]# 12167  35c143e85b1b  Dan Villiom Podlaski Christiansen <danchr@gmail.c      3: +975/-989
#[Out]# 12166  adfff89e6058  Dan Villiom Podlaski Christiansen <danchr@gmail.c      3: +744/-741
#[Out]# 12143  31f02288bbc4  Dan Villiom Podlaski Christiansen <danchr@gmail.c         2: +26/-8
#[Out]# 12068  50a4e55aa278  Dan Villiom Podlaski Christiansen <danchr@gmail.c        1: +27/-13
#[Out]# 11968  1c00577b0298  Dan Villiom Podlaski Christiansen <danchr@gmail.c         3: +24/-4
#[Out]# 11889  ee8f36a6c766  Dan Villiom Podlaski Christiansen <danchr@gmail.c         3: +35/-0
#[Out]# 11698  5be733b20bd1  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +2/-2
#[Out]# 11613  2be70ca17311  Dan Villiom Podlaski Christiansen <danchr@gmail.c        1: +30/-10
#[Out]# 11610  3b65c3c3cc8d  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +1/-1
#[Out]# 11507  3efadce5b346  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +3/-0
#[Out]# 11506  94b3bbc886cf  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +2/-2
#[Out]# 11505  bbdf1fb1d3e3  Dan Villiom Podlaski Christiansen <danchr@gmail.c         1: +12/-0
#[Out]# 11328  d357d147f0d4  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +1/-0
#[Out]# 11327  6c469f2f9f12  Dan Villiom Podlaski Christiansen <danchr@gmail.c          2: +4/-4
#[Out]# 11326  c89309fa907d  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +1/-5
#[Out]# 11325  22a737306ba5  Dan Villiom Podlaski Christiansen <danchr@gmail.c         1: +39/-0
#[Out]# 11324  cdf6d861b207  Dan Villiom Podlaski Christiansen <danchr@gmail.c         1: +15/-0
#[Out]# 11021  29c39fe2491b  Dan Villiom Podlaski Christiansen <danchr@gmail.c         2: +11/-7
#[Out]# 10736  59d0d715fbfa  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +1/-1
#[Out]# 10713  61cd6653f846  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +3/-1
#[Out]# 10711  214a518a4b6e  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +1/-1
#[Out]# 10327  0aa59f532ef9  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +5/-8
#[Out]# 10312  56b50194617f  Dan Villiom Podlaski Christiansen <danchr@gmail.c          5: +6/-6
#[Out]# 10095  68964567e406  Dan Villiom Podlaski Christiansen <danchr@gmail.c    5: +1534/-1525
#[Out]# 10089  f91e5630ce7e  Dan Villiom Podlaski Christiansen <danchr@gmail.c  267: +6252/-6249
#[Out]# 10048  3aa420c56ac4  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +5/-2
#[Out]# 10009  0a8a43b4ca75  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +1/-1
#[Out]# 10007  54b518fc6671  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +1/-1
#[Out]# 9999   d355cebde5e6  Dan Villiom Podlaski Christiansen <danchr@gmail.c      2: +136/-170
#[Out]# 9874   c51494c53841  Dan Villiom Podlaski Christiansen <danchr@gmail.c         3: +14/-7
#[Out]# 9390   e37e9904bf10  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +4/-7
#[Out]# 9328   26fa0e31011d  Dan Villiom Podlaski Christiansen <danchr@gmail.c          3: +6/-2
#[Out]# 9327   40196d036a71  Dan Villiom Podlaski Christiansen <danchr@gmail.c         2: +48/-1
#[Out]# 9170   c24c9ce0cdcf  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +5/-3
#[Out]# 9169   894c5b4be275  Dan Villiom Podlaski Christiansen <danchr@gmail.c         1: +10/-5
#[Out]# 9088   fb66a7d3f28f  Dan Villiom Podlaski Christiansen <danchr@gmail.c          1: +4/-1
#[Out]# 9040   98d90ad54749  Dan Villiom Podlaski Christiansen <danchr@gmail.c         3: +51/-2), ('Danek Duvall <danek.duvall@sun.com>',               node                               author  changestr
#[Out]# n                                                                 
#[Out]# 2968  4cdb68d7eb92  Danek Duvall <danek.duvall@sun.com>  1: +59/-0
#[Out]# 2932  d77022db1bca  Danek Duvall <danek.duvall@sun.com>   2: +6/-2
#[Out]# 2831  0b9ac7dfcf56  Danek Duvall <danek.duvall@sun.com>  5: +15/-9
#[Out]# 2299  dacf718e1d48  Danek Duvall <danek.duvall@sun.com>  2: +13/-6
#[Out]# 2270  afd7c4ec000f  Danek Duvall <danek.duvall@sun.com>   1: +2/-1), ('Danek Duvall <duvall@comfychair.org>',                node                                author    changestr
#[Out]# n                                                                     
#[Out]# 14749  1e6661e09818  Danek Duvall <duvall@comfychair.org>     1: +5/-2
#[Out]# 14748  f0b047a24c57  Danek Duvall <duvall@comfychair.org>    2: +30/-1
#[Out]# 14031  e0f07847f8de  Danek Duvall <duvall@comfychair.org>  7: +150/-14), ('Daniel <byteshack@gmail.com>',               node                        author changestr
#[Out]# n                                                         
#[Out]# 2277  066d0055e430  Daniel <byteshack@gmail.com>  1: +9/-1), ('Daniel Atallah <daniel.atallah@gmail.com>',                node                                     author   changestr
#[Out]# n                                                                         
#[Out]# 13871  a916e8de4313  Daniel Atallah <daniel.atallah@gmail.com>  2: +39/-19
#[Out]# 13859  c13bfa451656  Daniel Atallah <daniel.atallah@gmail.com>   2: +17/-2
#[Out]# 13841  aeb41f0048e7  Daniel Atallah <daniel.atallah@gmail.com>    1: +1/-8
#[Out]# 13840  ed97955e0c04  Daniel Atallah <daniel.atallah@gmail.com>  1: +134/-0
#[Out]# 13839  49b818fd26d8  Daniel Atallah <daniel.atallah@gmail.com>   1: +15/-7), ('Daniel Dumitriu <daniel.dumitriu@gmail.com>',                node                                       author       changestr
#[Out]# n                                                                               
#[Out]# 14657  d80e06575547  Daniel Dumitriu <daniel.dumitriu@gmail.com>    1: +240/-264
#[Out]# 14656  4d36013ab330  Daniel Dumitriu <daniel.dumitriu@gmail.com>  1: +6811/-3249
#[Out]# 12306  f6a6d661953c  Daniel Dumitriu <daniel.dumitriu@gmail.com>    1: +748/-449
#[Out]# 12305  4403ba5f9009  Daniel Dumitriu <daniel.dumitriu@gmail.com>     1: +166/-86
#[Out]# 12304  403bb6067736  Daniel Dumitriu <daniel.dumitriu@gmail.com>     1: +158/-71
#[Out]# 12303  cf175b34a268  Daniel Dumitriu <daniel.dumitriu@gmail.com>      1: +11/-11
#[Out]# 12302  206859808904  Daniel Dumitriu <daniel.dumitriu@gmail.com>    1: +155/-143
#[Out]# 12301  474b4cd54e86  Daniel Dumitriu <daniel.dumitriu@gmail.com>       1: +28/-7
#[Out]# 12300  561a3eb2aece  Daniel Dumitriu <daniel.dumitriu@gmail.com>     1: +109/-81
#[Out]# 12299  0ef71bff56b7  Daniel Dumitriu <daniel.dumitriu@gmail.com>      1: +69/-44
#[Out]# 12298  faf2592b6f96  Daniel Dumitriu <daniel.dumitriu@gmail.com>        1: +8/-8
#[Out]# 12297  80fff5e32ca8  Daniel Dumitriu <daniel.dumitriu@gmail.com>      1: +76/-35
#[Out]# 12296  6a4ddae65397  Daniel Dumitriu <daniel.dumitriu@gmail.com>      1: +31/-26
#[Out]# 11973  663c6bb575e9  Daniel Dumitriu <daniel.dumitriu@gmail.com>    2: +12280/-0), ('Daniel Holth <dholth@fastmail.fm>',               node                             author   changestr
#[Out]# n                                                                
#[Out]# 4925  b6a1f2c46c6c  Daniel Holth <dholth@fastmail.fm>  3: +522/-0
#[Out]# 4924  6a16ef0d1c7c  Daniel Holth <dholth@fastmail.fm>  1: +134/-0
#[Out]# 4470  8fa54b9c6c5a  Daniel Holth <dholth@fastmail.fm>  1: +33/-12
#[Out]# 4468  af013ae3ca10  Daniel Holth <dholth@fastmail.fm>    1: +7/-7
#[Out]# 4467  1b75e0eff532  Daniel Holth <dholth@fastmail.fm>   1: +81/-0
#[Out]# 4234  6b2909e84203  Daniel Holth <dholth@fastmail.fm>    1: +4/-3), ('Daniel J. Lauk <daniel.lauk@gmail.com>',                node                                  author  changestr
#[Out]# n                                                                     
#[Out]# 11598  14db59e3b248  Daniel J. Lauk <daniel.lauk@gmail.com>  2: +50/-0
#[Out]# 11590  7e5f5e5858f9  Daniel J. Lauk <daniel.lauk@gmail.com>   1: +1/-0), ('Daniel Kobras <kobras@debian.org>',               node                             author  changestr
#[Out]# n                                                               
#[Out]# 1587  851bc33ff545  Daniel Kobras <kobras@debian.org>  1: +12/-4), ('Daniel Santa Cruz <byteshack@gmail.com>',               node                                   author changestr
#[Out]# n                                                                    
#[Out]# 1713  03ee100b8c21  Daniel Santa Cruz <byteshack@gmail.com>  1: +1/-1), ('David Champion <dgc@uchicago.edu>',                node                             author   changestr
#[Out]# n                                                                 
#[Out]# 16653  0fdd8193c8b5  David Champion <dgc@uchicago.edu>  2: +82/-72
#[Out]# 11183  d3c1eddfdbcf  David Champion <dgc@uchicago.edu>   2: +11/-2
#[Out]# 11182  a912f26777d3  David Champion <dgc@uchicago.edu>   2: +19/-8
#[Out]# 11181  bdc8f048166e  David Champion <dgc@uchicago.edu>    1: +1/-1
#[Out]# 11180  523330d567cf  David Champion <dgc@uchicago.edu>   2: +17/-4
#[Out]# 9541   f8048c334066  David Champion <dgc@uchicago.edu>   1: +26/-8
#[Out]# 9191   6e5e548452de  David Champion <dgc@uchicago.edu>    1: +1/-1
#[Out]# 9190   4743d1a65dfe  David Champion <dgc@uchicago.edu>    1: +2/-1
#[Out]# 9082   b3ee4c2e1ff5  David Champion <dgc@uchicago.edu>    1: +1/-1
#[Out]# 9016   d4d4da54ab05  David Champion <dgc@uchicago.edu>    2: +2/-2
#[Out]# 7605   9811cc670c51  David Champion <dgc@uchicago.edu>    1: +8/-2), ('David Frey <dpfrey@shaw.ca>',               node                       author changestr
#[Out]# n                                                        
#[Out]# 8105  1f0a5a5fff43  David Frey <dpfrey@shaw.ca>  1: +4/-0
#[Out]# 7896  73d80d5bf478  David Frey <dpfrey@shaw.ca>  1: +1/-0), ('David Golub',                node       author changestr
#[Out]# n                                         
#[Out]# 14729  b39ed8c8e5e5  David Golub  1: +1/-1), ('David Golub <davidg@fogcreek.com>',                node                             author changestr
#[Out]# n                                                               
#[Out]# 14831  41c3a71c318d  David Golub <davidg@fogcreek.com>  2: +4/-4), ('David Greenaway <hg-dev@davidgreenaway.com>',                node                                       author   changestr
#[Out]# n                                                                           
#[Out]# 11117  e6df01776e08  David Greenaway <hg-dev@davidgreenaway.com>  1: +59/-15
#[Out]# 11116  ef4aa90b1e58  David Greenaway <hg-dev@davidgreenaway.com>  2: +62/-48), ('David J. Mellor <dmellor@whistlingcat.com>',               node                                      author changestr
#[Out]# n                                                                       
#[Out]# 5510  924fd86f0579  David J. Mellor <dmellor@whistlingcat.com>  1: +1/-1), ('David M. Carr  <david@carrclan.us>',                node                              author   changestr
#[Out]# n                                                                  
#[Out]# 15912  2bd54ffaa27e  David M. Carr  <david@carrclan.us>  5: +56/-54
#[Out]# 15911  c654eac03452  David M. Carr  <david@carrclan.us>  4: +11/-16
#[Out]# 15910  2b8d5c55ae67  David M. Carr  <david@carrclan.us>   1: +24/-0
#[Out]# 15583  95174c381525  David M. Carr  <david@carrclan.us>   4: +42/-9
#[Out]# 15582  d90b0b30464b  David M. Carr  <david@carrclan.us>   1: +13/-3
#[Out]# 15534  9e99d2bbb1b1  David M. Carr  <david@carrclan.us>  4: +28/-14
#[Out]# 15533  83c2e6772408  David M. Carr  <david@carrclan.us>  1: +123/-0
#[Out]# 15407  e48f0913f018  David M. Carr  <david@carrclan.us>    1: +1/-1
#[Out]# 15406  da81da6caa6b  David M. Carr  <david@carrclan.us>    1: +8/-8
#[Out]# 15405  2a3ab9e81a3e  David M. Carr  <david@carrclan.us>    1: +7/-6), ('David Reiss <davidn@gmail.com>',               node                          author changestr
#[Out]# n                                                           
#[Out]# 6467  aa3f61884a48  David Reiss <davidn@gmail.com>  1: +6/-3), ('David Soria Parra <dsp <at> php.net>',               node                                author  changestr
#[Out]# n                                                                  
#[Out]# 6578  13fafd8cc4a1  David Soria Parra <dsp <at> php.net>  1: +30/-5
#[Out]# 6412  fb76d58f5fee  David Soria Parra <dsp <at> php.net>   1: +1/-1), ('David Soria Parra <dsp@php.net>',                node                           author       changestr
#[Out]# n                                                                   
#[Out]# 16606  2fdd1902ed2d  David Soria Parra <dsp@php.net>        1: +1/-3
#[Out]# 16593  0c0c1101e46d  David Soria Parra <dsp@php.net>        1: +4/-8
#[Out]# 15984  894f83a35653  David Soria Parra <dsp@php.net>        1: +2/-1
#[Out]# 15479  06671371e634  David Soria Parra <dsp@php.net>        1: +7/-3
#[Out]# 14705  8083f4d00bd1  David Soria Parra <dsp@php.net>        3: +7/-7
#[Out]# 14700  1ec8bd909ac3  David Soria Parra <dsp@php.net>        1: +2/-2
#[Out]# 13884  8ba08a16e4e0  David Soria Parra <dsp@php.net>       2: +46/-4
#[Out]# 13768  d16c99f16f00  David Soria Parra <dsp@php.net>       3: +44/-1
#[Out]# 13767  80d6e1f63ed9  David Soria Parra <dsp@php.net>        2: +1/-4
#[Out]# 13761  a1dae38acbc6  David Soria Parra <dsp@php.net>        1: +0/-1
#[Out]# 13757  c0c599709846  David Soria Parra <dsp@php.net>        1: +1/-7
#[Out]# 13756  31eac42d9123  David Soria Parra <dsp@php.net>      5: +28/-29
#[Out]# 13755  3786b810ea75  David Soria Parra <dsp@php.net>       1: +23/-0
#[Out]# 13742  2ad66e6b2cc8  David Soria Parra <dsp@php.net>       1: +11/-6
#[Out]# 13727  3f6a4579f803  David Soria Parra <dsp@php.net>      5: +105/-1
#[Out]# 13660  4d958d1bb072  David Soria Parra <dsp@php.net>       2: +46/-4
#[Out]# 13578  8c397d7b25d2  David Soria Parra <dsp@php.net>     1: +52/-119
#[Out]# 13577  af02626b0b15  David Soria Parra <dsp@php.net>     1: +144/-46
#[Out]# 13532  2cefee00a5b9  David Soria Parra <dsp@php.net>        1: +1/-1
#[Out]# 13489  101826e2b7da  David Soria Parra <dsp@php.net>        1: +9/-5
#[Out]# 13488  0a1ee8f42a49  David Soria Parra <dsp@php.net>  1: +2448/-1078
#[Out]# 13478  c631ac076375  David Soria Parra <dsp@php.net>       2: +47/-2
#[Out]# 13474  6c2e476b7a11  David Soria Parra <dsp@php.net>        1: +9/-0
#[Out]# 13469  07a6460f829a  David Soria Parra <dsp@php.net>       6: +0/-20
#[Out]# 13463  22f948c027a9  David Soria Parra <dsp@php.net>        1: +9/-1
#[Out]# 13462  8641cb094c81  David Soria Parra <dsp@php.net>      1: +25/-14
#[Out]# 13461  81af2040b586  David Soria Parra <dsp@php.net>      1: +45/-13
#[Out]# 13454  afc84a879ac8  David Soria Parra <dsp@php.net>       2: +20/-0
#[Out]# 13453  c1b808020819  David Soria Parra <dsp@php.net>        1: +6/-0
#[Out]# 13450  b3f9af7c22c5  David Soria Parra <dsp@php.net>        1: +6/-1
#[Out]# 13448  97b69883e929  David Soria Parra <dsp@php.net>      2: +18/-11
#[Out]# 13425  0fe36c347c00  David Soria Parra <dsp@php.net>       2: +24/-1
#[Out]# 13416  5431b3f3e52e  David Soria Parra <dsp@php.net>      7: +36/-51
#[Out]# 13415  25b5694b9337  David Soria Parra <dsp@php.net>        1: +3/-1
#[Out]# 13388  a184dbd9b2c5  David Soria Parra <dsp@php.net>   23: +384/-253
#[Out]# 13387  0be2fe6a0843  David Soria Parra <dsp@php.net>        2: +8/-6
#[Out]# 13386  f78bc5ddbe4f  David Soria Parra <dsp@php.net>       4: +18/-0
#[Out]# 13385  d012d95499f7  David Soria Parra <dsp@php.net>       3: +0/-11
#[Out]# 13384  caa561759538  David Soria Parra <dsp@php.net>        2: +9/-0
#[Out]# 13381  d073468e3c5f  David Soria Parra <dsp@php.net>        1: +1/-1
#[Out]# 13249  6f011cf52f9a  David Soria Parra <dsp@php.net>        3: +5/-4
#[Out]# 13026  7f2b8aac7bdc  David Soria Parra <dsp@php.net>       2: +20/-3
#[Out]# 13025  146bad852ede  David Soria Parra <dsp@php.net>        1: +2/-3
#[Out]# 11884  1135e42f0049  David Soria Parra <dsp@php.net>        1: +0/-1
#[Out]# 11879  b5f61da929c8  David Soria Parra <dsp@php.net>        1: +0/-1
#[Out]# 11627  31dde4c3bb83  David Soria Parra <dsp@php.net>        1: +4/-1
#[Out]# 11434  86eea1f97eac  David Soria Parra <dsp@php.net>        1: +2/-2
#[Out]# 11431  cac256790aa4  David Soria Parra <dsp@php.net>       1: +38/-1
#[Out]# 10457  4f38d03d4975  David Soria Parra <dsp@php.net>        3: +4/-4
#[Out]# 10328  55d134ef8ab7  David Soria Parra <dsp@php.net>        1: +1/-1
#[Out]# 10132  0c23b0b3516b  David Soria Parra <dsp@php.net>       1: +25/-0
#[Out]# 10131  d1f9640e9a67  David Soria Parra <dsp@php.net>        1: +4/-0
#[Out]# 9983   04207f5e7344  David Soria Parra <dsp@php.net>        1: +2/-2
#[Out]# 9608   d097bc2d1945  David Soria Parra <dsp@php.net>        1: +4/-3
#[Out]# 9363   b694531a5aa7  David Soria Parra <dsp@php.net>        1: +4/-1
#[Out]# 9326   abc198bca7c1  David Soria Parra <dsp@php.net>        1: +7/-6
#[Out]# 9325   a15b0412de06  David Soria Parra <dsp@php.net>        1: +8/-2
#[Out]# 9324   dde454349864  David Soria Parra <dsp@php.net>        1: +2/-2
#[Out]# 9084   53fdf18fd63b  David Soria Parra <dsp@php.net>       3: +52/-0
#[Out]# 9081   2de7d96593db  David Soria Parra <dsp@php.net>        1: +4/-1
#[Out]# 9074   7ee61afc655f  David Soria Parra <dsp@php.net>        1: +1/-1
#[Out]# 7816   f420eafe59cd  David Soria Parra <dsp@php.net>       3: +10/-4
#[Out]# 7796   5043def56a80  David Soria Parra <dsp@php.net>        1: +1/-1
#[Out]# 7618   e86ca711544d  David Soria Parra <dsp@php.net>       1: +23/-0
#[Out]# 7577   cab1cf26ca58  David Soria Parra <dsp@php.net>       2: +59/-0
#[Out]# 7576   fead6cf99a09  David Soria Parra <dsp@php.net>        1: +3/-1
#[Out]# 7543   1c1e6fa67377  David Soria Parra <dsp@php.net>       1: +0/-30
#[Out]# 7542   9b64589b1112  David Soria Parra <dsp@php.net>       1: +0/-15
#[Out]# 7541   e80a734ba1fc  David Soria Parra <dsp@php.net>       1: +0/-19
#[Out]# 7540   63446383dfb7  David Soria Parra <dsp@php.net>       1: +0/-15
#[Out]# 7539   d3b6c6179323  David Soria Parra <dsp@php.net>       1: +0/-15
#[Out]# 7538   ecfb683675ed  David Soria Parra <dsp@php.net>      3: +130/-4
#[Out]# 7537   167853c7e54a  David Soria Parra <dsp@php.net>        1: +7/-1
#[Out]# 7535   42cb14f20d76  David Soria Parra <dsp@php.net>        2: +6/-0
#[Out]# 7534   5f681a143ede  David Soria Parra <dsp@php.net>       1: +75/-4
#[Out]# 7532   cae586246331  David Soria Parra <dsp@php.net>        1: +2/-2
#[Out]# 7317   9737041646bc  David Soria Parra <dsp@php.net>       3: +70/-5
#[Out]# 7241   135003a470f3  David Soria Parra <dsp@php.net>      1: +220/-0
#[Out]# 6323   6e1308a09ffd  David Soria Parra <dsp@php.net>       1: +54/-0
#[Out]# 6302   8e3dc3de7e73  David Soria Parra <dsp@php.net>       2: +26/-0), ('David Wolever <david@wolever.net>',                node                             author  changestr
#[Out]# n                                                                
#[Out]# 13765  a56c1b2bff18  David Wolever <david@wolever.net>  2: +10/-1
#[Out]# 10838  9ea7238ad935  David Wolever <david@wolever.net>  3: +44/-4), ('David Wolever <wolever@cs.toronto.edu>',               node                                  author changestr
#[Out]# n                                                                   
#[Out]# 9174  cd92a6968f70  David Wolever <wolever@cs.toronto.edu>  1: +7/-5
#[Out]# 9014  42956a93db3a  David Wolever <wolever@cs.toronto.edu>  1: +7/-5), ('Dennis Schoen <dennis.schoen@epublica.de>',               node                                     author changestr
#[Out]# n                                                                      
#[Out]# 7007  8997b81a33da  Dennis Schoen <dennis.schoen@epublica.de>  1: +1/-1), ('Dennis Schoen <ds@1d10t.de>',               node                       author  changestr
#[Out]# n                                                         
#[Out]# 6543  b714aac1f7b3  Dennis Schoen <ds@1d10t.de>  2: +78/-0
#[Out]# 6322  108636b9b981  Dennis Schoen <ds@1d10t.de>  1: +15/-2
#[Out]# 5862  89ea99c7bdfd  Dennis Schoen <ds@1d10t.de>  1: +11/-6), ('Dhruva Krishnamurthy <dhruvakm@gmail.com>',               node                                     author changestr
#[Out]# n                                                                      
#[Out]# 7130  3cf699e89e48  Dhruva Krishnamurthy <dhruvakm@gmail.com>  1: +1/-0
#[Out]# 6490  e30c56f337b1  Dhruva Krishnamurthy <dhruvakm@gmail.com>  1: +8/-8), ('Diego de Oliveira <diego@diegooliveira.com>',               node                                       author    changestr
#[Out]# n                                                                           
#[Out]# 8146  aef8b864a304  Diego de Oliveira <diego@diegooliveira.com>  1: +8283/-0), ('Dirkjan Ochtman <dirkjan@ochtman.nl>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 498 entries, 13729 to 4877
#[Out]# Data columns:
#[Out]# node         498  non-null values
#[Out]# author       498  non-null values
#[Out]# changestr    498  non-null values
#[Out]# dtypes: object(3)), ('Dirkjan Ochtman <djc.ochtman@kentyde.com>',                node                                     author     changestr
#[Out]# n                                                                           
#[Out]# 10835  63948e7d37f7  Dirkjan Ochtman <djc.ochtman@kentyde.com>    2: +16/-28
#[Out]# 10834  1874697a8863  Dirkjan Ochtman <djc.ochtman@kentyde.com>    1: +50/-51
#[Out]# 10833  812b85d02c92  Dirkjan Ochtman <djc.ochtman@kentyde.com>    1: +12/-12
#[Out]# 10832  dedf88fe945a  Dirkjan Ochtman <djc.ochtman@kentyde.com>      1: +6/-5
#[Out]# 10831  90a095c24bc4  Dirkjan Ochtman <djc.ochtman@kentyde.com>    1: +15/-13
#[Out]# 10830  a6808629f450  Dirkjan Ochtman <djc.ochtman@kentyde.com>    1: +10/-16
#[Out]# 10829  92209ae8610a  Dirkjan Ochtman <djc.ochtman@kentyde.com>     1: +9/-10
#[Out]# 10605  58128004cca1  Dirkjan Ochtman <djc.ochtman@kentyde.com>  3: +39/-1203
#[Out]# 10366  2e3ec7ef5349  Dirkjan Ochtman <djc.ochtman@kentyde.com>     3: +60/-1
#[Out]# 10365  49cd2e7fd91c  Dirkjan Ochtman <djc.ochtman@kentyde.com>      2: +8/-5
#[Out]# 10364  bcf90e712dc3  Dirkjan Ochtman <djc.ochtman@kentyde.com>      2: +9/-7), ('Dmitriy Kostunin <dmitriy.kostunin@gmail.com>',               node                                         author  changestr
#[Out]# n                                                                           
#[Out]# 8604  021de2d12355  Dmitriy Kostunin <dmitriy.kostunin@gmail.com>  2: +36/-0), ('Dmitriy Taychenachev <dimichxp@gmail.com>',               node                                     author changestr
#[Out]# n                                                                      
#[Out]# 7263  3cbadcf28a4c  Dmitriy Taychenachev <dimichxp@gmail.com>  1: +2/-0), ('Dmitry Panov <dop@itoolabs.com>',                node                           author  changestr
#[Out]# n                                                              
#[Out]# 15427  ae04af1ce78d  Dmitry Panov <dop@itoolabs.com>  1: +8/-10), ('Dongsheng Song <dongsheng.song@gmail.com>',               node                                     author       changestr
#[Out]# n                                                                            
#[Out]# 9804  fe0fb1cca911  Dongsheng Song <dongsheng.song@gmail.com>  1: +7897/-7555
#[Out]# 8908  105343f9f744  Dongsheng Song <dongsheng.song@gmail.com>        2: +9/-9
#[Out]# 7952  fef5f3ef84c4  Dongsheng Song <dongsheng.song@gmail.com>        1: +2/-2
#[Out]# 7934  d4839577fa44  Dongsheng Song <dongsheng.song@gmail.com>    1: +208/-154
#[Out]# 7831  f51e2263d2aa  Dongsheng Song <dongsheng.song@gmail.com>        1: +1/-1
#[Out]# 7789  0896c008cb52  Dongsheng Song <dongsheng.song@gmail.com>    1: +200/-177
#[Out]# 7752  9294c0158c42  Dongsheng Song <dongsheng.song@gmail.com>  1: +2590/-1753
#[Out]# 7691  9e70287086c7  Dongsheng Song <dongsheng.song@gmail.com>     1: +8344/-0), ('Dongsheng Song <songdongsheng@live.cn>',               node                                  author       changestr
#[Out]# n                                                                         
#[Out]# 8965  4df5d07fb532  Dongsheng Song <songdongsheng@live.cn>  1: +2122/-2215), ('Doug Philips <dgou@mac.com>',               node                       author changestr
#[Out]# n                                                        
#[Out]# 6504  d923a051f84c  Doug Philips <dgou@mac.com>  1: +1/-1), ('Dov Feldstern <dfeldstern@fastimap.com>',               node                                   author  changestr
#[Out]# n                                                                     
#[Out]# 6512  24fd94ed1cc0  Dov Feldstern <dfeldstern@fastimap.com>  2: +24/-0
#[Out]# 6429  2b181fb3a70a  Dov Feldstern <dfeldstern@fastimap.com>   1: +2/-0
#[Out]# 6428  a3668330f14a  Dov Feldstern <dfeldstern@fastimap.com>  2: +99/-0), ('Dustin Sallings <dustin@spy.net>',               node                            author   changestr
#[Out]# n                                                               
#[Out]# 6073  57c1a7052982  Dustin Sallings <dustin@spy.net>   3: +43/-0
#[Out]# 5481  e5eedd74e70f  Dustin Sallings <dustin@spy.net>  5: +19/-13), ('D\xc3\xa9vai Tam\xc3\xa1s <devait@vnet.hu>',                node                        author   changestr
#[Out]# n                                                            
#[Out]# 11035  ce6d56b95f2e  Dévai Tamás <devait@vnet.hu>  1: +1/-1), ('Edouard Gomez <ed.gomez@free.fr>',                node                            author    changestr
#[Out]# n                                                                 
#[Out]# 16326  589aab2ca716  Edouard Gomez <ed.gomez@free.fr>    1: +14/-4
#[Out]# 13928  2f93a4a10144  Edouard Gomez <ed.gomez@free.fr>     1: +7/-0
#[Out]# 13837  043238abda94  Edouard Gomez <ed.gomez@free.fr>     1: +3/-0
#[Out]# 13836  6b7077df4aa5  Edouard Gomez <ed.gomez@free.fr>    3: +46/-4
#[Out]# 13826  d80b768545cb  Edouard Gomez <ed.gomez@free.fr>    1: +11/-1
#[Out]# 13825  9ff22f600c6c  Edouard Gomez <ed.gomez@free.fr>    1: +10/-0
#[Out]# 13824  7e525d2f9a75  Edouard Gomez <ed.gomez@free.fr>    1: +14/-0
#[Out]# 11153  4a9bee613737  Edouard Gomez <ed.gomez@free.fr>   4: +21/-11
#[Out]# 11152  d2da9e6dd13e  Edouard Gomez <ed.gomez@free.fr>    2: +10/-9
#[Out]# 11151  22f5ad0b5857  Edouard Gomez <ed.gomez@free.fr>   3: +126/-1
#[Out]# 11150  a2bc2f2d77a9  Edouard Gomez <ed.gomez@free.fr>    4: +81/-4
#[Out]# 10849  05856e682521  Edouard Gomez <ed.gomez@free.fr>     3: +8/-7
#[Out]# 10622  c90d923fff64  Edouard Gomez <ed.gomez@free.fr>     2: +6/-3
#[Out]# 10610  664bb0ce95ed  Edouard Gomez <ed.gomez@free.fr>     1: +1/-1
#[Out]# 8765   46b5b4301fcc  Edouard Gomez <ed.gomez@free.fr>     1: +7/-4
#[Out]# 7604   75ad51257c82  Edouard Gomez <ed.gomez@free.fr>    1: +13/-4
#[Out]# 7603   cac40e310f92  Edouard Gomez <ed.gomez@free.fr>     1: +2/-1
#[Out]# 7597   075b7ef0f84d  Edouard Gomez <ed.gomez@free.fr>   1: +56/-33
#[Out]# 7596   28563e94c471  Edouard Gomez <ed.gomez@free.fr>     1: +5/-0
#[Out]# 7595   77fec2d270ae  Edouard Gomez <ed.gomez@free.fr>     1: +3/-0
#[Out]# 7594   3b2383c90034  Edouard Gomez <ed.gomez@free.fr>     1: +4/-6
#[Out]# 7593   3742981341c1  Edouard Gomez <ed.gomez@free.fr>     1: +1/-1
#[Out]# 7592   8c5afb3cdb67  Edouard Gomez <ed.gomez@free.fr>     1: +3/-1
#[Out]# 7591   a8db971dc258  Edouard Gomez <ed.gomez@free.fr>     1: +2/-1
#[Out]# 7590   7971650bdc73  Edouard Gomez <ed.gomez@free.fr>   1: +12/-15
#[Out]# 7589   bd96fcb696d8  Edouard Gomez <ed.gomez@free.fr>     1: +0/-2
#[Out]# 7442   a14ce129cfcd  Edouard Gomez <ed.gomez@free.fr>   1: +16/-14
#[Out]# 7244   a8e4e599e17f  Edouard Gomez <ed.gomez@free.fr>     1: +1/-1
#[Out]# 5894   8b95f598097c  Edouard Gomez <ed.gomez@free.fr>  3: +153/-28
#[Out]# 5881   1cf99a3e269e  Edouard Gomez <ed.gomez@free.fr>     1: +1/-1
#[Out]# 4767   439e2f2fde42  Edouard Gomez <ed.gomez@free.fr>     2: +3/-3
#[Out]# 4597   451e91ed535e  Edouard Gomez <ed.gomez@free.fr>    3: +65/-2
#[Out]# 4596   9855939d0c82  Edouard Gomez <ed.gomez@free.fr>   1: +51/-31
#[Out]# 4530   d634b61e9cec  Edouard Gomez <ed.gomez@free.fr>    1: +23/-4
#[Out]# 4529   ce1fed4a5b94  Edouard Gomez <ed.gomez@free.fr>     0: +0/-0
#[Out]# 4523   ec889780f28b  Edouard Gomez <ed.gomez@free.fr>    1: +25/-0
#[Out]# 4522   ac2fe196ac9b  Edouard Gomez <ed.gomez@free.fr>   1: +70/-81
#[Out]# 4250   b53c6f7dbb1f  Edouard Gomez <ed.gomez@free.fr>     1: +2/-2
#[Out]# 4249   59de487f43d7  Edouard Gomez <ed.gomez@free.fr>     1: +1/-1
#[Out]# 4140   be5d099e7a62  Edouard Gomez <ed.gomez@free.fr>     1: +2/-1
#[Out]# 4139   79cf097774ef  Edouard Gomez <ed.gomez@free.fr>     1: +2/-2
#[Out]# 3903   4874ca8a53c1  Edouard Gomez <ed.gomez@free.fr>     1: +2/-1
#[Out]# 3792   4670470b97bd  Edouard Gomez <ed.gomez@free.fr>     1: +1/-1
#[Out]# 3214   a5603ad915c5  Edouard Gomez <ed.gomez@free.fr>    2: +25/-0
#[Out]# 3213   d7d53e3d9590  Edouard Gomez <ed.gomez@free.fr>    1: +15/-2
#[Out]# 3009   abcd6ae3cf5a  Edouard Gomez <ed.gomez@free.fr>     1: +5/-3
#[Out]# 2047   ebf1ecb5f4e8  Edouard Gomez <ed.gomez@free.fr>     1: +1/-0
#[Out]# 1185   2ae9c319e6fe  Edouard Gomez <ed.gomez@free.fr>     1: +8/-1
#[Out]# 859    6390c377a9e6  Edouard Gomez <ed.gomez@free.fr>     1: +5/-2
#[Out]# 672    dbe0ce2ae196  Edouard Gomez <ed.gomez@free.fr>   4: +10/-10
#[Out]# 668    d93f0b127b6a  Edouard Gomez <ed.gomez@free.fr>     1: +2/-1), ('Eduard-Cristian Stefan <alexandrul.ct@gmail.com>',                node                                            author  changestr
#[Out]# n                                                                               
#[Out]# 13016  b335882c2f21  Eduard-Cristian Stefan <alexandrul.ct@gmail.com>   3: +7/-4
#[Out]# 12637  43f42de733d0  Eduard-Cristian Stefan <alexandrul.ct@gmail.com>  1: +10/-1), ('Edward Lee <edward.lee@engineering.uiuc.edu>',               node                                        author   changestr
#[Out]# n                                                                           
#[Out]# 6122  800e2756c9ab  Edward Lee <edward.lee@engineering.uiuc.edu>  4: +41/-23
#[Out]# 5320  18091102a633  Edward Lee <edward.lee@engineering.uiuc.edu>  1: +42/-23), ('Eli Carter <eli.carter@tektronix.com>',                node                                 author  changestr
#[Out]# n                                                                    
#[Out]# 15370  8af6c6d91c92  Eli Carter <eli.carter@tektronix.com>   1: +1/-1
#[Out]# 15369  b4ea79f88268  Eli Carter <eli.carter@tektronix.com>  2: +24/-1
#[Out]# 15318  acecb419e5b0  Eli Carter <eli.carter@tektronix.com>  1: +29/-0
#[Out]# 15313  3eb1a90ea409  Eli Carter <eli.carter@tektronix.com>  2: +17/-1
#[Out]# 15312  8d862e7b96d4  Eli Carter <eli.carter@tektronix.com>   1: +1/-5
#[Out]# 15303  07811b3b119b  Eli Carter <eli.carter@tektronix.com>  2: +29/-0
#[Out]# 15301  a0583f984fd1  Eli Carter <eli.carter@tektronix.com>   1: +1/-1
#[Out]# 15300  c2a75faf3b49  Eli Carter <eli.carter@tektronix.com>   2: +3/-3
#[Out]# 15299  10b2bd7f1125  Eli Carter <eli.carter@tektronix.com>   1: +1/-1
#[Out]# 14796  7ef125fa9b35  Eli Carter <eli.carter@tektronix.com>  2: +67/-1), ('Elifarley Callado Coelho Cruz',                node                         author   changestr
#[Out]# n                                                             
#[Out]# 15207  0f7f9f06c759  Elifarley Callado Coelho Cruz  2: +91/-76), ('Elifarley Callado Coelho Cruz <elifarley@gmail.com>',                node                                             author   changestr
#[Out]# n                                                                                 
#[Out]# 11157  2a857f9d2c6c  Elifarley Callado Coelho Cruz <elifarley@gmail.co    1: +3/-0
#[Out]# 11156  b3d5619f1f2b  Elifarley Callado Coelho Cruz <elifarley@gmail.co    1: +5/-0
#[Out]# 11155  62714143742f  Elifarley Callado Coelho Cruz <elifarley@gmail.co   2: +20/-6
#[Out]# 11136  b27a43eceda3  Elifarley Callado Coelho Cruz <elifarley@gmail.co   1: +66/-0
#[Out]# 11135  2dd91779eb27  Elifarley Callado Coelho Cruz <elifarley@gmail.co  1: +86/-22
#[Out]# 11102  08681cb66231  Elifarley Callado Coelho Cruz <elifarley@gmail.co  2: +375/-1
#[Out]# 11101  d82f3651cd13  Elifarley Callado Coelho Cruz <elifarley@gmail.co  1: +54/-13
#[Out]# 11100  623fe42a649e  Elifarley Callado Coelho Cruz <elifarley@gmail.co   1: +16/-2
#[Out]# 11029  470a6ace7574  Elifarley Callado Coelho Cruz <elifarley@gmail.co    1: +4/-3
#[Out]# 10667  fcfe2e50faab  Elifarley Callado Coelho Cruz <elifarley@gmail.co    1: +1/-1), ('Elliott Peele <elliot@rpath.com>',               node                            author changestr
#[Out]# n                                                             
#[Out]# 5479  81bef3c355c5  Elliott Peele <elliot@rpath.com>  1: +1/-1), ('Emanuele Aina <em@nerd.ocracy.org>',               node                              author     changestr
#[Out]# n                                                                   
#[Out]# 4695  c3da7b6cc975  Emanuele Aina <em@nerd.ocracy.org>      1: +1/-1
#[Out]# 4691  ca4971347e0a  Emanuele Aina <em@nerd.ocracy.org>     3: +15/-5
#[Out]# 4482  a73cf208b2a0  Emanuele Aina <em@nerd.ocracy.org>     3: +55/-5
#[Out]# 4392  1043e4b27ab9  Emanuele Aina <em@nerd.ocracy.org>  3: +160/-160
#[Out]# 4391  c8919eb0f315  Emanuele Aina <em@nerd.ocracy.org>     3: +79/-2
#[Out]# 4279  15cd36db4230  Emanuele Aina <em@nerd.ocracy.org>    2: +10/-60
#[Out]# 4257  d250076824e3  Emanuele Aina <em@nerd.ocracy.org>      1: +1/-3
#[Out]# 4256  f9dc36b1bdd5  Emanuele Aina <em@nerd.ocracy.org>      1: +7/-6), ('Emanuele Aina <faina.mail@tiscali.it>',               node                                 author   changestr
#[Out]# n                                                                    
#[Out]# 4278  af72395580e8  Emanuele Aina <faina.mail@tiscali.it>  1: +32/-37
#[Out]# 4277  1c0488b58ece  Emanuele Aina <faina.mail@tiscali.it>  1: +11/-18
#[Out]# 4276  337010e50dcd  Emanuele Aina <faina.mail@tiscali.it>  1: +21/-24
#[Out]# 4275  cf26f4564000  Emanuele Aina <faina.mail@tiscali.it>   1: +7/-17
#[Out]# 4274  e59286f15189  Emanuele Aina <faina.mail@tiscali.it>    1: +1/-3
#[Out]# 4273  de85ff0aaac5  Emanuele Aina <faina.mail@tiscali.it>  1: +11/-59
#[Out]# 4272  691f9168a815  Emanuele Aina <faina.mail@tiscali.it>  1: +17/-15
#[Out]# 4271  e287d61dd268  Emanuele Aina <faina.mail@tiscali.it>    1: +6/-1
#[Out]# 4270  2ebdd33fe456  Emanuele Aina <faina.mail@tiscali.it>   2: +93/-0), ('Eric Bloodworth <ergosys@gmail.com>',               node                               author changestr
#[Out]# n                                                                
#[Out]# 1429  45bd7925dceb  Eric Bloodworth <ergosys@gmail.com>  1: +1/-0
#[Out]# 1428  9346a7fb3fe2  Eric Bloodworth <ergosys@gmail.com>  1: +1/-1), ('Eric Eisner <ede@alum.mit.edu>',                node                          author  changestr
#[Out]# n                                                             
#[Out]# 13654  2fdea636f254  Eric Eisner <ede@alum.mit.edu>  2: +37/-3), ('Eric Eisner <ede@mit.edu>',                node                     author   changestr
#[Out]# n                                                         
#[Out]# 13702  3ab3b892d223  Eric Eisner <ede@mit.edu>   2: +11/-4
#[Out]# 13677  c12088259f64  Eric Eisner <ede@mit.edu>   2: +10/-8
#[Out]# 13582  a7c9735307bd  Eric Eisner <ede@mit.edu>    1: +5/-0
#[Out]# 13531  dea6efdd7ec4  Eric Eisner <ede@mit.edu>   2: +35/-1
#[Out]# 13466  f2295f7cd468  Eric Eisner <ede@mit.edu>    1: +1/-5
#[Out]# 13465  fa88fabc1d66  Eric Eisner <ede@mit.edu>    1: +2/-1
#[Out]# 13460  64bb8e586a92  Eric Eisner <ede@mit.edu>   2: +16/-2
#[Out]# 13337  9f2c6892e004  Eric Eisner <ede@mit.edu>  1: +17/-10
#[Out]# 13235  2537bd17421d  Eric Eisner <ede@mit.edu>   2: +35/-0
#[Out]# 13234  413bef846806  Eric Eisner <ede@mit.edu>  2: +53/-17
#[Out]# 13233  a79e0688a5ee  Eric Eisner <ede@mit.edu>    1: +7/-2
#[Out]# 13232  b512a7074349  Eric Eisner <ede@mit.edu>    1: +3/-2
#[Out]# 13231  c4d857f5405d  Eric Eisner <ede@mit.edu>  1: +23/-12
#[Out]# 13213  d79fdff55627  Eric Eisner <ede@mit.edu>   2: +32/-1
#[Out]# 13210  dca5488f0e4f  Eric Eisner <ede@mit.edu>    1: +2/-3
#[Out]# 13209  70d80907e4b8  Eric Eisner <ede@mit.edu>  1: +14/-10
#[Out]# 13208  519ac79d680b  Eric Eisner <ede@mit.edu>   1: +9/-20
#[Out]# 13207  8617b8b74fae  Eric Eisner <ede@mit.edu>  1: +22/-23
#[Out]# 13179  560b8001f765  Eric Eisner <ede@mit.edu>    2: +7/-4
#[Out]# 13178  cad35f06c031  Eric Eisner <ede@mit.edu>    1: +4/-7
#[Out]# 13177  53341289eaf8  Eric Eisner <ede@mit.edu>    1: +5/-1
#[Out]# 13176  dcaad69cfd6a  Eric Eisner <ede@mit.edu>    1: +2/-9
#[Out]# 13175  3bc237b0eaea  Eric Eisner <ede@mit.edu>    1: +1/-3
#[Out]# 13174  c869bd9e1193  Eric Eisner <ede@mit.edu>    1: +1/-1
#[Out]# 13168  c922aacf6f1f  Eric Eisner <ede@mit.edu>    1: +7/-2
#[Out]# 13167  6e74b912fa5c  Eric Eisner <ede@mit.edu>    1: +4/-1
#[Out]# 13166  49c7e875482d  Eric Eisner <ede@mit.edu>   1: +10/-8
#[Out]# 13165  a1dd7bd26a2b  Eric Eisner <ede@mit.edu>    1: +3/-4
#[Out]# 13164  d0cbddfe3f4c  Eric Eisner <ede@mit.edu>    1: +4/-5
#[Out]# 13163  83986af605e5  Eric Eisner <ede@mit.edu>    1: +9/-8
#[Out]# 13162  8cecea387574  Eric Eisner <ede@mit.edu>  1: +13/-17
#[Out]# 13158  cca0779b4832  Eric Eisner <ede@mit.edu>   2: +70/-5
#[Out]# 13157  8db85e39d59c  Eric Eisner <ede@mit.edu>  1: +18/-15
#[Out]# 13156  b4814f1f415c  Eric Eisner <ede@mit.edu>   1: +6/-10
#[Out]# 13124  f930032aa6d5  Eric Eisner <ede@mit.edu>   2: +54/-3
#[Out]# 13122  7f2ecb64140d  Eric Eisner <ede@mit.edu>   2: +38/-7
#[Out]# 13102  3a42651b0a62  Eric Eisner <ede@mit.edu>   2: +44/-1
#[Out]# 13101  d90fc91c8377  Eric Eisner <ede@mit.edu>   2: +57/-8
#[Out]# 13100  845c602b8635  Eric Eisner <ede@mit.edu>  2: +109/-0
#[Out]# 13099  a91334380699  Eric Eisner <ede@mit.edu>   2: +48/-0
#[Out]# 13098  2b73a3279a9f  Eric Eisner <ede@mit.edu>  2: +139/-1
#[Out]# 11448  25430ff23cfa  Eric Eisner <ede@mit.edu>    3: +6/-0
#[Out]# 11176  d061ef1d781c  Eric Eisner <ede@mit.edu>    1: +2/-2
#[Out]# 11106  c7dbd6c4877a  Eric Eisner <ede@mit.edu>  8: +16/-14
#[Out]# 10950  420bc8124904  Eric Eisner <ede@mit.edu>   1: +22/-9
#[Out]# 10836  4ba41eebb3a8  Eric Eisner <ede@mit.edu>   1: +6/-13), ('Eric Hopper <hopper@omnifarious.org>',               node                                author        changestr
#[Out]# n                                                                        
#[Out]# 6341  63bdfcc3eaaf  Eric Hopper <hopper@omnifarious.org>       3: +136/-0
#[Out]# 6318  308988071b90  Eric Hopper <hopper@omnifarious.org>         1: +4/-2
#[Out]# 6317  b0d937869417  Eric Hopper <hopper@omnifarious.org>         1: +1/-1
#[Out]# 6285  4b81eecc8aa2  Eric Hopper <hopper@omnifarious.org>        2: +14/-2
#[Out]# 6284  c93b6c0e6e84  Eric Hopper <hopper@omnifarious.org>        2: +31/-3
#[Out]# 6267  d036ea711140  Eric Hopper <hopper@omnifarious.org>         1: +1/-1
#[Out]# 4822  f94dbc6c7eaf  Eric Hopper <hopper@omnifarious.org>        2: +23/-7
#[Out]# 4698  30e826bd8ed1  Eric Hopper <hopper@omnifarious.org>         1: +5/-4
#[Out]# 4675  6858a7477a5e  Eric Hopper <hopper@omnifarious.org>       5: +79/-15
#[Out]# 4648  8e503fa54d2d  Eric Hopper <hopper@omnifarious.org>       4: +803/-9
#[Out]# 4647  7c80e3e6f030  Eric Hopper <hopper@omnifarious.org>         1: +6/-0
#[Out]# 4600  5243cece3d97  Eric Hopper <hopper@omnifarious.org>         1: +5/-2
#[Out]# 4465  af8db3b42a4a  Eric Hopper <hopper@omnifarious.org>         1: +1/-0
#[Out]# 4464  32ea809e5bd1  Eric Hopper <hopper@omnifarious.org>         2: +8/-0
#[Out]# 4463  eff2eefdb65a  Eric Hopper <hopper@omnifarious.org>         2: +7/-4
#[Out]# 4462  871ff96a86cc  Eric Hopper <hopper@omnifarious.org>        2: +41/-0
#[Out]# 4461  3900f684a150  Eric Hopper <hopper@omnifarious.org>         2: +4/-3
#[Out]# 4459  a764edb6fc95  Eric Hopper <hopper@omnifarious.org>         1: +3/-0
#[Out]# 3449  c8686e3f0291  Eric Hopper <hopper@omnifarious.org>       4: +542/-0
#[Out]# 3448  6ca49c5fe268  Eric Hopper <hopper@omnifarious.org>        3: +13/-8
#[Out]# 3447  ef1032c223e7  Eric Hopper <hopper@omnifarious.org>        2: +13/-2
#[Out]# 3446  0b450267cf47  Eric Hopper <hopper@omnifarious.org>        2: +34/-1
#[Out]# 3444  3505fcd5a231  Eric Hopper <hopper@omnifarious.org>        2: +52/-1
#[Out]# 2538  f4b7d71c1c60  Eric Hopper <hopper@omnifarious.org>         2: +4/-5
#[Out]# 2537  b6975008d44f  Eric Hopper <hopper@omnifarious.org>         1: +1/-1
#[Out]# 2536  8106e477f584  Eric Hopper <hopper@omnifarious.org>         3: +9/-2
#[Out]# 2535  b8ccf6386db7  Eric Hopper <hopper@omnifarious.org>        4: +23/-4
#[Out]# 2534  d5a3cc6520d5  Eric Hopper <hopper@omnifarious.org>         2: +8/-1
#[Out]# 2533  589474a1dc36  Eric Hopper <hopper@omnifarious.org>        2: +99/-0
#[Out]# 2532  84655f721f39  Eric Hopper <hopper@omnifarious.org>        3: +46/-0
#[Out]# 2514  419c42223bee  Eric Hopper <hopper@omnifarious.org>       4: +25/-16
#[Out]# 2508  ab460a3f0e3a  Eric Hopper <hopper@omnifarious.org>        1: +15/-1
#[Out]# 2507  7e01da2bc7f3  Eric Hopper <hopper@omnifarious.org>         2: +2/-2
#[Out]# 2506  d0db3462d568  Eric Hopper <hopper@omnifarious.org>      7: +193/-41
#[Out]# 2505  01b856927970  Eric Hopper <hopper@omnifarious.org>         1: +8/-7
#[Out]# 2392  8238a3f039e6  Eric Hopper <hopper@omnifarious.org>         2: +6/-7
#[Out]# 2391  d351a3be3371  Eric Hopper <hopper@omnifarious.org>         6: +6/-6
#[Out]# 2356  2db831b33e8f  Eric Hopper <hopper@omnifarious.org>    5: +1019/-981
#[Out]# 2355  eb08fb4d41e1  Eric Hopper <hopper@omnifarious.org>     4: +197/-158
#[Out]# 2311  b832b6eb65ab  Eric Hopper <hopper@omnifarious.org>   3: +1145/-1143
#[Out]# 1929  85daa4e03b4c  Eric Hopper <hopper@omnifarious.org>  51: +2657/-1057
#[Out]# 1630  5ecf05541e11  Eric Hopper <hopper@omnifarious.org>         1: +8/-4
#[Out]# 1559  59b3639df0a9  Eric Hopper <hopper@omnifarious.org>      11: +20/-20
#[Out]# 1468  dc1bbc456b96  Eric Hopper <hopper@omnifarious.org>       2: +185/-0
#[Out]# 1467  06d5d8794e5f  Eric Hopper <hopper@omnifarious.org>         1: +1/-1
#[Out]# 1466  b6d9ea0bc107  Eric Hopper <hopper@omnifarious.org>      1: +137/-12
#[Out]# 1465  be6b5ce60b7f  Eric Hopper <hopper@omnifarious.org>        1: +16/-7
#[Out]# 1464  00117edce2dd  Eric Hopper <hopper@omnifarious.org>         1: +1/-1
#[Out]# 1463  26e73acc0cdf  Eric Hopper <hopper@omnifarious.org>         1: +9/-3
#[Out]# 1462  12a8d772fa32  Eric Hopper <hopper@omnifarious.org>        1: +25/-9
#[Out]# 1461  02099220ad49  Eric Hopper <hopper@omnifarious.org>        2: +11/-4
#[Out]# 1460  40d08cf1c544  Eric Hopper <hopper@omnifarious.org>       1: +17/-13
#[Out]# 1459  106fdec8e1fb  Eric Hopper <hopper@omnifarious.org>         1: +2/-0
#[Out]# 1458  1033892bbb87  Eric Hopper <hopper@omnifarious.org>      2: +173/-34
#[Out]# 1457  518da3c3b6ce  Eric Hopper <hopper@omnifarious.org>      3: +146/-29
#[Out]# 1403  bc3e66edb04c  Eric Hopper <hopper@omnifarious.org>         1: +2/-0
#[Out]# 1380  27add82ad845  Eric Hopper <hopper@omnifarious.org>         1: +1/-3
#[Out]# 1377  854775b27d1a  Eric Hopper <hopper@omnifarious.org>         2: +2/-2
#[Out]# 1376  524ca4a06f70  Eric Hopper <hopper@omnifarious.org>        1: +6/-16
#[Out]# 1374  c3654cfaa77d  Eric Hopper <hopper@omnifarious.org>        1: +7/-15
#[Out]# 1366  136920d13fc2  Eric Hopper <hopper@omnifarious.org>         1: +1/-0
#[Out]# 1355  9116fe491b06  Eric Hopper <hopper@omnifarious.org>        2: +18/-0
#[Out]# 1354  8cf364c65425  Eric Hopper <hopper@omnifarious.org>         1: +4/-1
#[Out]# 1353  a0c68981a5f4  Eric Hopper <hopper@omnifarious.org>         1: +4/-2
#[Out]# 1199  78ceaf83f28f  Eric Hopper <hopper@omnifarious.org>       2: +70/-16), ('Eric Roshan Eisner <ede@alum.mit.edu>',                node                                 author  changestr
#[Out]# n                                                                    
#[Out]# 15434  0810ccc51f0a  Eric Roshan Eisner <ede@alum.mit.edu>  2: +18/-0
#[Out]# 15234  5d700b7edd85  Eric Roshan Eisner <ede@alum.mit.edu>   1: +3/-2
#[Out]# 15231  cd6f10dccf16  Eric Roshan Eisner <ede@alum.mit.edu>  2: +12/-0), ('Eric St-Jean <esj@wwd.ca>',               node                     author  changestr
#[Out]# n                                                       
#[Out]# 4355  4a1504264261  Eric St-Jean <esj@wwd.ca>   1: +4/-3
#[Out]# 4354  ad33eeeeb50a  Eric St-Jean <esj@wwd.ca>   1: +2/-1
#[Out]# 4353  1eaa8d90c689  Eric St-Jean <esj@wwd.ca>  1: +12/-5), ('Erik Zielke <ez@aragost.com>',                node                        author     changestr
#[Out]# n                                                              
#[Out]# 13417  0748e18be470  Erik Zielke <ez@aragost.com>   4: +429/-15
#[Out]# 13413  fa921dcd9993  Erik Zielke <ez@aragost.com>      1: +1/-1
#[Out]# 13332  e5617047c926  Erik Zielke <ez@aragost.com>     2: +39/-5
#[Out]# 13225  84cec5895d01  Erik Zielke <ez@aragost.com>    3: +10/-92
#[Out]# 13212  f02d7a562a21  Erik Zielke <ez@aragost.com>    3: +92/-10
#[Out]# 13113  4936a04b6792  Erik Zielke <ez@aragost.com>   4: +133/-25
#[Out]# 13111  54be08fa4d1d  Erik Zielke <ez@aragost.com>      3: +8/-1
#[Out]# 13058  58f0c60b7f40  Erik Zielke <ez@aragost.com>  2: +122/-113
#[Out]# 13033  c19b9282d3a7  Erik Zielke <ez@aragost.com>    4: +75/-13
#[Out]# 12985  cc5f0c0c19bc  Erik Zielke <ez@aragost.com>    1: +16/-10
#[Out]# 12925  158ca54a79cc  Erik Zielke <ez@aragost.com>      1: +3/-2
#[Out]# 12783  6dc3d3cd729b  Erik Zielke <ez@aragost.com>      1: +8/-0
#[Out]# 12782  0d09991f91ee  Erik Zielke <ez@aragost.com>     1: +41/-3
#[Out]# 12781  bdc1cf692447  Erik Zielke <ez@aragost.com>      1: +9/-5
#[Out]# 12780  891ddf76b73e  Erik Zielke <ez@aragost.com>      1: +2/-1
#[Out]# 12779  dce09f82f619  Erik Zielke <ez@aragost.com>      2: +9/-5
#[Out]# 12772  c77f6276c9e7  Erik Zielke <ez@aragost.com>    3: +88/-14
#[Out]# 12757  13f0acfa974a  Erik Zielke <ez@aragost.com>    1: +18/-14
#[Out]# 12756  db79d3627872  Erik Zielke <ez@aragost.com>      1: +1/-1
#[Out]# 12607  4b9f23885a55  Erik Zielke <ez@aragost.com>      1: +0/-4
#[Out]# 12606  663d96f33367  Erik Zielke <ez@aragost.com>      1: +1/-1
#[Out]# 12605  57ad5c4e4213  Erik Zielke <ez@aragost.com>      1: +3/-3
#[Out]# 12604  41fa32a6b6f8  Erik Zielke <ez@aragost.com>    1: +18/-19
#[Out]# 12603  e3247ceaca5e  Erik Zielke <ez@aragost.com>   10: +53/-56
#[Out]# 12566  dece1f46f7a2  Erik Zielke <ez@aragost.com>     1: +10/-9
#[Out]# 12565  c87216e5e43e  Erik Zielke <ez@aragost.com>    1: +58/-12
#[Out]# 12428  40852b4b910c  Erik Zielke <ez@aragost.com>    3: +35/-12
#[Out]# 12423  4ac734b9b3fd  Erik Zielke <ez@aragost.com>    4: +21/-16
#[Out]# 12422  75f044d4dbf5  Erik Zielke <ez@aragost.com>     3: +85/-0
#[Out]# 11714  552e0cfbddbd  Erik Zielke <ez@aragost.com>      1: +1/-1), ('Erling Ellingsen <erlingalf@gmail.com>',               node                                  author  changestr
#[Out]# n                                                                    
#[Out]# 4263  6cb6cfe43c5d  Erling Ellingsen <erlingalf@gmail.com>  3: +66/-8
#[Out]# 3962  1ca664c964e0  Erling Ellingsen <erlingalf@gmail.com>   1: +2/-2), ('Eung-Ju PARK <eungju@gmail.com>',               node                           author changestr
#[Out]# n                                                            
#[Out]# 2402  82cef38fea56  Eung-Ju PARK <eungju@gmail.com>  2: +2/-2), ('Eung-Ju Park <eungju@gmail.com>',               node                           author changestr
#[Out]# n                                                            
#[Out]# 2013  65634e1038dd  Eung-Ju Park <eungju@gmail.com>  1: +4/-4), ('Eung-ju Park <eungju@gmail.com>',               node                           author changestr
#[Out]# n                                                            
#[Out]# 1841  7f12a63568ae  Eung-ju Park <eungju@gmail.com>  1: +8/-2), ('FUJIWARA Katsunori <foozy@lares.dti.ne.jp>',                node                                      author       changestr
#[Out]# n                                                                              
#[Out]# 16633  9aa590007c7b  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     1: +111/-92
#[Out]# 16629  c17ce7cd5090  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +4/-1
#[Out]# 16623  0a730d3c5aae  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +4/-0
#[Out]# 16561  00182b3d0879  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +33/-20
#[Out]# 16558  6b7f8d0e2ff9  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +63/-37
#[Out]# 16543  715a9fb8ef22  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>   1: +1501/-711
#[Out]# 16528  5d803620ca05  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +16/-12
#[Out]# 16514  363e808de349  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        5: +7/-5
#[Out]# 16504  e3c7ca15cde2  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        2: +8/-0
#[Out]# 16503  c27a769d9703  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +4/-2
#[Out]# 16502  8298d220cbf9  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +3/-0
#[Out]# 16501  340d047ea577  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-1
#[Out]# 16500  8436a4e21417  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        2: +2/-2
#[Out]# 16499  0b463f52b948  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +3/-3
#[Out]# 16487  cbf2ea2f5ca1  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     2: +184/-72
#[Out]# 16469  dd68c972d089  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-1
#[Out]# 16375  913d1fa61398  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       1: +13/-3
#[Out]# 16374  5d61e007d957  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-1
#[Out]# 16246  0c4bec9596d8  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      4: +36/-34
#[Out]# 16245  83925d3a4559  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     1: +144/-71
#[Out]# 16226  e7701459fb42  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-1
#[Out]# 16225  d2e8e79a6361  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-1
#[Out]# 16224  67a5bc8aeb1d  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-1
#[Out]# 16186  900767dfa80d  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +8/-3
#[Out]# 16183  0789d1bbf6c1  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       2: +15/-3
#[Out]# 16177  e785456f9631  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       2: +43/-1
#[Out]# 16176  ab09347f8c5c  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     1: +204/-16
#[Out]# 16159  3c147aca78dd  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>    1: +923/-323
#[Out]# 16157  50247a7a9983  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       2: +18/-4
#[Out]# 16156  d8cc67114dc3  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        2: +3/-1
#[Out]# 16151  1228b5528945  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>    1: +665/-216
#[Out]# 16145  594fc9329628  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-5
#[Out]# 16127  4d80a5705a28  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     1: +184/-72
#[Out]# 16096  616c2e278f18  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +6/-5
#[Out]# 16095  4546a8513dcd  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       2: +39/-1
#[Out]# 16094  fceb2964fa6c  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       2: +22/-0
#[Out]# 16079  41417443b7d0  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       2: +50/-2
#[Out]# 16061  f11eee00c652  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        2: +7/-3
#[Out]# 16059  73aaff46175b  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-1
#[Out]# 16058  467a85ced564  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-1
#[Out]# 16057  6a42846cf769  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +3/-3
#[Out]# 16046  cff72771e63b  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>    1: +896/-239
#[Out]# 16011  02a497a17257  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       1: +18/-0
#[Out]# 16010  f06c53ca59a9  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +2/-2
#[Out]# 16009  39e60576ac98  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +2/-2
#[Out]# 15756  bc2a22357538  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       1: +43/-0
#[Out]# 15755  917f263eeb26  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +5/-4
#[Out]# 15754  9b822edecb4c  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       2: +65/-6
#[Out]# 15753  988409e44a76  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       2: +67/-7
#[Out]# 15752  9e6a13c2aeb9  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +9/-2
#[Out]# 15751  3bcfea777efc  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +2/-1
#[Out]# 15750  1dd60426b061  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +3/-4
#[Out]# 15749  c604a3d1969d  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-2
#[Out]# 15742  c51c9dc13a58  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       1: +32/-0
#[Out]# 15741  f63e40047372  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       1: +4/-13
#[Out]# 15740  a1f4bd47d18e  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +19/-11
#[Out]# 15507  f21de8d2c724  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     1: +90/-187
#[Out]# 15501  e47ba02ad06b  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     1: +156/-83
#[Out]# 15498  1581da01d5c4  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-1
#[Out]# 15497  417127af3996  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +3/-2
#[Out]# 15496  4751d5133f15  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-0
#[Out]# 15490  d550168f11ce  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      2: +119/-2
#[Out]# 15489  2ebe3d0ce91d  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       5: +29/-3
#[Out]# 15488  3c5e818ac679  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        2: +5/-2
#[Out]# 15487  d6c19cfa03ce  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        2: +7/-3
#[Out]# 15486  390bcd01775a  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +6/-5
#[Out]# 15485  8e020155e76c  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +1/-0
#[Out]# 15484  eacfd851cb9e  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +6/-3
#[Out]# 15483  37a6e9765015  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +5/-1
#[Out]# 15482  081e795c60e0  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +9/-3
#[Out]# 15481  ec8730886f36  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +3/-3
#[Out]# 15476  7f01ad702405  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        2: +5/-6
#[Out]# 15454  6c5e6ebe0812  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        2: +3/-4
#[Out]# 15417  6a7e874390b0  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       2: +75/-1
#[Out]# 15394  84980b00fbcb  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>   1: +2890/-623
#[Out]# 15393  87bb6b7644f6  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       2: +23/-2
#[Out]# 14893  978358ce722d  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     1: +125/-58
#[Out]# 14876  24efa83d81cb  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     4: +345/-16
#[Out]# 14847  f091c142fdc1  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +62/-35
#[Out]# 14837  28e98a8b173d  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       3: +48/-5
#[Out]# 14788  68a697421a57  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>  1: +5625/-3002
#[Out]# 13513  4c54c1d5d012  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +49/-17
#[Out]# 13490  6bff7d066352  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +42/-21
#[Out]# 13483  726492a96dd2  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +19/-11
#[Out]# 13482  7458b7e0d8d5  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>   1: +1041/-707
#[Out]# 12884  f2e2ef5c6a1b  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>  1: +2803/-1979
#[Out]# 11732  ae8a3b785f88  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>    1: +624/-336
#[Out]# 11554  c29012a73518  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +16/-12
#[Out]# 11534  4f5a6df2af92  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     4: +185/-17
#[Out]# 11482  fa19c7418f83  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>  1: +3769/-1750
#[Out]# 11464  521c8e0c93bf  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       1: +11/-4
#[Out]# 11321  40c06bbf58be  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>   26: +460/-278
#[Out]# 11299  d320e70442a5  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      6: +69/-34
#[Out]# 10582  0364445e6e6a  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +13/-13
#[Out]# 10564  461c2159937f  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +51/-45
#[Out]# 10554  8522310dcaf1  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +62/-41
#[Out]# 10531  093008fc4078  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>    1: +415/-150
#[Out]# 10314  35bcb3152e67  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>  1: +1431/-1198
#[Out]# 9982   acf001ee5ef8  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +3/-1
#[Out]# 9863   20f95fc4c58e  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>   1: +1127/-941
#[Out]# 9007   9e839f0c9689  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>    1: +139/-105
#[Out]# 8972   5edd998e8d55  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>  1: +4747/-4026
#[Out]# 8849   80cc4b1a62d0  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      3: +70/-31
#[Out]# 7907   c2e962bdcc37  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>    1: +182/-111
#[Out]# 7794   9915283e8ae2  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     1: +637/-30
#[Out]# 7761   fe4052a512fa  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>     1: +8568/-0
#[Out]# 4995   e45c5120ca27  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       1: +21/-3
#[Out]# 2668   7a32b7e6c563  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +3/-1
#[Out]# 2667   92ba858ed640  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +2/-1
#[Out]# 2455   ff83112332f9  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +32/-15
#[Out]# 2454   74518478d2bf  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +28/-11
#[Out]# 2453   b5902db74ba3  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +6/-2
#[Out]# 2452   d1a7c8a5b835  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +4/-3
#[Out]# 2318   94d628499235  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>        1: +4/-1
#[Out]# 2316   3d58376a7103  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>      1: +51/-22
#[Out]# 2315   c4a2d8502cc0  FUJIWARA Katsunori <foozy@lares.dti.ne.jp>       1: +11/-8), ('Fabian Kreutz <fabian.kreutz@qvantel.com>',                node                                     author       changestr
#[Out]# n                                                                             
#[Out]# 16214  d66af10b648c  Fabian Kreutz <fabian.kreutz@qvantel.com>    1: +442/-194
#[Out]# 16213  605ed03b0cbe  Fabian Kreutz <fabian.kreutz@qvantel.com>    1: +217/-148
#[Out]# 15746  bd280b2bf669  Fabian Kreutz <fabian.kreutz@qvantel.com>      1: +50/-67
#[Out]# 15745  9c4adcb785ee  Fabian Kreutz <fabian.kreutz@qvantel.com>    1: +398/-183
#[Out]# 15692  7c3bfa8105dc  Fabian Kreutz <fabian.kreutz@qvantel.com>        1: +7/-8
#[Out]# 15691  5b6d8f42f4f0  Fabian Kreutz <fabian.kreutz@qvantel.com>  1: +8179/-5972
#[Out]# 7945   852fef4d9152  Fabian Kreutz <fabian.kreutz@qvantel.com>     1: +106/-51
#[Out]# 7944   e6d3999c0cb0  Fabian Kreutz <fabian.kreutz@qvantel.com>      1: +40/-34
#[Out]# 7943   7f158aeab751  Fabian Kreutz <fabian.kreutz@qvantel.com>      1: +74/-57), ('Fabian Kreutz <fabian.kreutz@starnet.fi>',               node                                    author       changestr
#[Out]# n                                                                           
#[Out]# 9865  7196258e4a99  Fabian Kreutz <fabian.kreutz@starnet.fi>    1: +572/-212
#[Out]# 9775  fb7f02082eab  Fabian Kreutz <fabian.kreutz@starnet.fi>     1: +120/-53
#[Out]# 9755  d64bdaeaa2b9  Fabian Kreutz <fabian.kreutz@starnet.fi>   1: +956/-1429
#[Out]# 9579  620d6b20ef85  Fabian Kreutz <fabian.kreutz@starnet.fi>    1: +258/-176
#[Out]# 9571  9432b78d895c  Fabian Kreutz <fabian.kreutz@starnet.fi>    1: +466/-184
#[Out]# 9570  a95e2833dda5  Fabian Kreutz <fabian.kreutz@starnet.fi>  1: +2384/-1850
#[Out]# 8140  ccf20c92534b  Fabian Kreutz <fabian.kreutz@starnet.fi>      1: +45/-33
#[Out]# 8139  ad3ba2de2cba  Fabian Kreutz <fabian.kreutz@starnet.fi>     1: +140/-51
#[Out]# 8009  7da575c56710  Fabian Kreutz <fabian.kreutz@starnet.fi>      1: +61/-22
#[Out]# 7986  e2e13a7af148  Fabian Kreutz <fabian.kreutz@starnet.fi>      1: +47/-29), ('Fabian Kreutz <project+hg@fabian-kreutz.de>',               node                                       author changestr
#[Out]# n                                                                        
#[Out]# 9909  60cefb8b3c85  Fabian Kreutz <project+hg@fabian-kreutz.de>  1: +2/-2), ('Fabian Otto <sigsegv@alchiba.ni.cs.tu-berlin.de>',               node                                            author changestr
#[Out]# n                                                                             
#[Out]# 1759  5afd459db177  Fabian Otto <sigsegv@alchiba.ni.cs.tu-berlin.de>  1: +4/-0), ('Fabio Zadrozny <fabiofz at gmail dot com>',               node                                     author  changestr
#[Out]# n                                                                       
#[Out]# 6103  e668fd796b8b  Fabio Zadrozny <fabiofz at gmail dot com>  1: +35/-3), ('Faheem Mitha <faheem@email.unc.edu>',                node                               author   changestr
#[Out]# n                                                                   
#[Out]# 11356  511445840148  Faheem Mitha <faheem@email.unc.edu>  4: +363/-0
#[Out]# 10772  1b8aa9ffa7dc  Faheem Mitha <faheem@email.unc.edu>  1: +16/-13
#[Out]# 10744  ee5b112aa529  Faheem Mitha <faheem@email.unc.edu>  2: +33/-13
#[Out]# 10726  a0102da324ab  Faheem Mitha <faheem@email.unc.edu>   1: +10/-4
#[Out]# 10705  e3396b218e10  Faheem Mitha <faheem@email.unc.edu>    1: +5/-0
#[Out]# 9880   b755a886e8b7  Faheem Mitha <faheem@email.unc.edu>    1: +1/-1), ('Florent Guillaume <fg@nuxeo.com>',               node                            author   changestr
#[Out]# n                                                               
#[Out]# 6359  25e74cd3f023  Florent Guillaume <fg@nuxeo.com>   2: +12/-3
#[Out]# 6358  7cb9af02e250  Florent Guillaume <fg@nuxeo.com>    1: +1/-1
#[Out]# 6357  62980dd86bf6  Florent Guillaume <fg@nuxeo.com>    1: +1/-1
#[Out]# 6356  b34b876d1f6f  Florent Guillaume <fg@nuxeo.com>  2: +22/-48
#[Out]# 6250  bf0dd23f55fa  Florent Guillaume <fg@nuxeo.com>   8: +15/-4
#[Out]# 6249  cf1fa60fdaf4  Florent Guillaume <fg@nuxeo.com>   1: +23/-0), ('Florian La Roche <laroche@redhat.com>',               node                                 author   changestr
#[Out]# n                                                                    
#[Out]# 1335  bea6356b8bca  Florian La Roche <laroche@redhat.com>  1: +11/-18
#[Out]# 1275  a1a84dd489ff  Florian La Roche <laroche@redhat.com>    1: +2/-2
#[Out]# 1274  fe3dd937e803  Florian La Roche <laroche@redhat.com>    1: +4/-4
#[Out]# 1273  ab22af71386f  Florian La Roche <laroche@redhat.com>   1: +6/-14
#[Out]# 1272  060c08bf9e2f  Florian La Roche <laroche@redhat.com>    1: +1/-1), ('Francis Barber <fedora@barber-family.id.au>',               node                                       author changestr
#[Out]# n                                                                        
#[Out]# 8190  36b935cad495  Francis Barber <fedora@barber-family.id.au>  1: +1/-1), ('Frank Kingswood <frank@kingswood-consulting.co.uk>',                node                                             author     changestr
#[Out]# n                                                                                   
#[Out]# 11347  18680b0e20a7  Frank Kingswood <frank@kingswood-consulting.co.uk      1: +3/-3
#[Out]# 10165  69ce7a10e593  Frank Kingswood <frank@kingswood-consulting.co.uk     5: +53/-1
#[Out]# 8829   ce4b92f5cea7  Frank Kingswood <frank@kingswood-consulting.co.uk   3: +782/-10
#[Out]# 7823   11efa41037e2  Frank Kingswood <frank@kingswood-consulting.co.uk    7: +379/-0
#[Out]# 7606   a204547790bc  Frank Kingswood <frank@kingswood-consulting.co.uk     2: +45/-2
#[Out]# 7550   16905fc2690f  Frank Kingswood <frank@kingswood-consulting.co.uk  3: +123/-155
#[Out]# 7478   fed8f75f29ce  Frank Kingswood <frank@kingswood-consulting.co.uk      1: +0/-3
#[Out]# 7465   8f0305874701  Frank Kingswood <frank@kingswood-consulting.co.uk      2: +5/-4
#[Out]# 6872   ceb28b67204e  Frank Kingswood <frank@kingswood-consulting.co.uk     2: +88/-0
#[Out]# 6777   386561a5179a  Frank Kingswood <frank@kingswood-consulting.co.uk      1: +0/-1
#[Out]# 6768   127e8c3466d1  Frank Kingswood <frank@kingswood-consulting.co.uk   5: +467/-76
#[Out]# 6767   d2ac53fe216e  Frank Kingswood <frank@kingswood-consulting.co.uk    1: +154/-0
#[Out]# 6765   f8ef39206f6a  Frank Kingswood <frank@kingswood-consulting.co.uk    1: +547/-0
#[Out]# 2666   ebf033bc8eb2  Frank Kingswood <frank@kingswood-consulting.co.uk    2: +23/-11), ('Frank Wierzbicki <fwierzbicki@gmail.com>',               node                                    author changestr
#[Out]# n                                                                     
#[Out]# 7793  cf427b04d5c0  Frank Wierzbicki <fwierzbicki@gmail.com>  1: +1/-1), ('Fred Wulff <frew@cs.stanford.edu>',               node                             author  changestr
#[Out]# n                                                               
#[Out]# 8907  e9ef409e6399  Fred Wulff <frew@cs.stanford.edu>  3: +22/-1), ('Friedrich Kastner-Masilko <kastner_masilko@at.festo.com>',                node                                             author changestr
#[Out]# n                                                                               
#[Out]# 16115  8ae7626d8bf1  Friedrich Kastner-Masilko <kastner_masilko@at.fes  1: +1/-1), ('Garth Roxburgh-Kidd <garth@deadlybloodyserious.com>',               node                                             author changestr
#[Out]# n                                                                              
#[Out]# 8651  ca443bac7ed4  Garth Roxburgh-Kidd <garth@deadlybloodyserious.co  1: +5/-0), ('Gast\xc3\xb3n Kleiman <gaston.kleiman@gmail.com>',                node                                     author   changestr
#[Out]# n                                                                         
#[Out]# 13395  104c9ed93fc5  Gastón Kleiman <gaston.kleiman@gmail.com>  2: +21/-2), ('Georg Brandl <georg@python.org>',                node                           author   changestr
#[Out]# n                                                               
#[Out]# 13529  bbfae32f178e  Georg Brandl <georg@python.org>    1: +1/-1
#[Out]# 12802  c82cd7b08158  Georg Brandl <georg@python.org>    1: +1/-1
#[Out]# 12295  ff927933442b  Georg Brandl <georg@python.org>    1: +1/-1
#[Out]# 12162  d01e28657429  Georg Brandl <georg@python.org>    1: +6/-4
#[Out]# 11411  5834e79b24f7  Georg Brandl <georg@python.org>    1: +1/-1
#[Out]# 11349  cf8a9154a362  Georg Brandl <georg@python.org>    1: +1/-1
#[Out]# 10262  51421ab573de  Georg Brandl <georg@python.org>   3: +67/-9
#[Out]# 9992   0824aedd0079  Georg Brandl <georg@python.org>    1: +1/-1
#[Out]# 7457   a70fb83cbb9e  Georg Brandl <georg@python.org>  1: +18/-10
#[Out]# 7449   f848d7f96195  Georg Brandl <georg@python.org>    1: +1/-1), ('Georg.Koltermann@mscsoftware.com',               node                            author  changestr
#[Out]# n                                                              
#[Out]# 5464  7dafd9ab3979  Georg.Koltermann@mscsoftware.com  1: +77/-6), ('Gerard Korsten <soonkia77@gmail.com>',               node                                author  changestr
#[Out]# n                                                                  
#[Out]# 7303  972737252d05  Gerard Korsten <soonkia77@gmail.com>  3: +57/-4), ('Gil <gil@fooplanet.com>',               node                   author changestr
#[Out]# n                                                    
#[Out]# 2670  93eb49419760  Gil <gil@fooplanet.com>  1: +5/-1), ('Gilles Moris <gilles.moris@free.fr>',                node                               author    changestr
#[Out]# n                                                                    
#[Out]# 16113  6ba530122d8b  Gilles Moris <gilles.moris@free.fr>     1: +6/-5
#[Out]# 13515  2616325766e3  Gilles Moris <gilles.moris@free.fr>   2: +19/-18
#[Out]# 13449  8b1125eb361e  Gilles Moris <gilles.moris@free.fr>     1: +1/-1
#[Out]# 13446  1e497df514e2  Gilles Moris <gilles.moris@free.fr>  21: +93/-46
#[Out]# 12863  60d9692921ea  Gilles Moris <gilles.moris@free.fr>     1: +2/-1
#[Out]# 12729  52971985be14  Gilles Moris <gilles.moris@free.fr>   2: +62/-27
#[Out]# 11562  4f9dfb54c8b5  Gilles Moris <gilles.moris@free.fr>    3: +40/-8
#[Out]# 11445  4061205ad9e1  Gilles Moris <gilles.moris@free.fr>   1: +16/-15
#[Out]# 11439  778377be3662  Gilles Moris <gilles.moris@free.fr>     1: +1/-1
#[Out]# 11438  88fc876a4833  Gilles Moris <gilles.moris@free.fr>     1: +4/-2
#[Out]# 11318  7d780c04f074  Gilles Moris <gilles.moris@free.fr>    2: +98/-0
#[Out]# 11317  b66e414d38b0  Gilles Moris <gilles.moris@free.fr>    7: +36/-3
#[Out]# 11206  21a7ae13208f  Gilles Moris <gilles.moris@free.fr>     1: +2/-1
#[Out]# 11195  e8915e19205a  Gilles Moris <gilles.moris@free.fr>     1: +3/-0
#[Out]# 11194  e84600b0d81b  Gilles Moris <gilles.moris@free.fr>     2: +6/-0
#[Out]# 11193  acd61dc44a39  Gilles Moris <gilles.moris@free.fr>     1: +4/-0
#[Out]# 10104  54cd28258ea7  Gilles Moris <gilles.moris@free.fr>    5: +62/-4
#[Out]# 9814   5070e4d57276  Gilles Moris <gilles.moris@free.fr>   1: +43/-11
#[Out]# 9813   2059795bb5d0  Gilles Moris <gilles.moris@free.fr>    1: +9/-11
#[Out]# 9812   dd2c95fc4fe5  Gilles Moris <gilles.moris@free.fr>   1: +12/-21
#[Out]# 9811   c92ac5a56f69  Gilles Moris <gilles.moris@free.fr>     1: +3/-2
#[Out]# 9810   326a0a6453a3  Gilles Moris <gilles.moris@free.fr>     1: +8/-0
#[Out]# 9809   ce145bf2ca5e  Gilles Moris <gilles.moris@free.fr>    1: +14/-6
#[Out]# 9638   8f8f9685ac5e  Gilles Moris <gilles.moris@free.fr>   1: +15/-15
#[Out]# 9635   5d8125bbbbf4  Gilles Moris <gilles.moris@free.fr>     1: +1/-1
#[Out]# 9615   f51d1822d6fd  Gilles Moris <gilles.moris@free.fr>   1: +36/-28
#[Out]# 9614   58edd448da4f  Gilles Moris <gilles.moris@free.fr>    3: +39/-3
#[Out]# 7767   2b2548342265  Gilles Moris <gilles.moris@free.fr>   2: +22/-15
#[Out]# 7759   e81e6c996e99  Gilles Moris <gilles.moris@free.fr>    3: +26/-6
#[Out]# 7567   92c373f8135f  Gilles Moris <gilles.moris@free.fr>     1: +1/-0
#[Out]# 7494   c5e37dc38a52  Gilles Moris <gilles.moris@free.fr>   8: +58/-56
#[Out]# 6971   03916abdfb64  Gilles Moris <gilles.moris@free.fr>    9: +28/-8
#[Out]# 6968   d557749c627a  Gilles Moris <gilles.moris@free.fr>    9: +20/-4
#[Out]# 6413   db5324d3c257  Gilles Moris <gilles.moris@free.fr>     1: +1/-1
#[Out]# 6161   bc1ba9124799  Gilles Moris <gilles.moris@free.fr>   4: +18/-11), ('Giorgos Keramidas <keramida@ceid.upatras.gr>',                node                                        author     changestr
#[Out]# n                                                                              
#[Out]# 11512  92342fa9fbd8  Giorgos Keramidas <keramida@ceid.upatras.gr>     2: +26/-0
#[Out]# 10127  fe142808dd93  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +6/-0
#[Out]# 10126  1d69de7c91d2  Giorgos Keramidas <keramida@ceid.upatras.gr>     1: +38/-2
#[Out]# 10125  8c0126fc060f  Giorgos Keramidas <keramida@ceid.upatras.gr>     1: +54/-0
#[Out]# 10124  3f9b1651cc03  Giorgos Keramidas <keramida@ceid.upatras.gr>    1: +155/-1
#[Out]# 10123  928a01feb4a9  Giorgos Keramidas <keramida@ceid.upatras.gr>    1: +0/-117
#[Out]# 10122  9e2b35dc7e97  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +9/-8
#[Out]# 10121  96a04d712c0c  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +1/-1
#[Out]# 10120  ccb179013813  Giorgos Keramidas <keramida@ceid.upatras.gr>  1: +690/-461
#[Out]# 10119  6950dd804e69  Giorgos Keramidas <keramida@ceid.upatras.gr>     1: +2/-83
#[Out]# 10002  e553a425751d  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +6/-2
#[Out]# 8919   ec32797aa9b1  Giorgos Keramidas <keramida@ceid.upatras.gr>   1: +8779/-0
#[Out]# 8322   e0eb03bfa5af  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +2/-2
#[Out]# 8311   947cb53dbeed  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +1/-1
#[Out]# 6656   4d2cd2d26a4b  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +1/-1
#[Out]# 6320   9a9b02bcbcf4  Giorgos Keramidas <keramida@ceid.upatras.gr>      2: +9/-0
#[Out]# 6319   8999d1249171  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +1/-0
#[Out]# 5907   b6d8972ce339  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +1/-1
#[Out]# 5898   e7ed5d07cc4c  Giorgos Keramidas <keramida@ceid.upatras.gr>      5: +8/-8
#[Out]# 5417   ca890c0c3f1f  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +8/-8
#[Out]# 4770   242026115e6a  Giorgos Keramidas <keramida@ceid.upatras.gr>      3: +9/-1
#[Out]# 4699   a6b62584d0b2  Giorgos Keramidas <keramida@ceid.upatras.gr>    5: +36/-16
#[Out]# 4696   59b8f9361545  Giorgos Keramidas <keramida@ceid.upatras.gr>     2: +51/-0
#[Out]# 4577   9b3a818adae6  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +2/-1
#[Out]# 4374   b90e323a4781  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +2/-2
#[Out]# 4337   9e3e975258a9  Giorgos Keramidas <keramida@ceid.upatras.gr>     2: +48/-0
#[Out]# 4265   26596a6b6518  Giorgos Keramidas <keramida@ceid.upatras.gr>     3: +27/-2
#[Out]# 4264   eb5d4fec1487  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +2/-1
#[Out]# 4085   1e11e8b6acab  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +3/-1
#[Out]# 3709   38291d9c8c1c  Giorgos Keramidas <keramida@ceid.upatras.gr>     2: +64/-0
#[Out]# 3351   50a18815e3f0  Giorgos Keramidas <keramida@ceid.upatras.gr>     3: +57/-1
#[Out]# 3129   f01efb4bc258  Giorgos Keramidas <keramida@ceid.upatras.gr>    2: +223/-0
#[Out]# 2951   5ddf7d305a27  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +1/-1
#[Out]# 2926   13cd2cdeff6a  Giorgos Keramidas <keramida@ceid.upatras.gr>    1: +34/-11
#[Out]# 2924   d62ce27d925a  Giorgos Keramidas <keramida@ceid.upatras.gr>    2: +253/-0
#[Out]# 2923   cd47230a4eb9  Giorgos Keramidas <keramida@ceid.upatras.gr>     2: +36/-0
#[Out]# 2904   8ca608c1eb02  Giorgos Keramidas <keramida@ceid.upatras.gr>     2: +45/-0
#[Out]# 2901   05f357b70cb0  Giorgos Keramidas <keramida@ceid.upatras.gr>     1: +21/-9
#[Out]# 2885   26c37ebda1bb  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +1/-1
#[Out]# 2878   66eff8355168  Giorgos Keramidas <keramida@ceid.upatras.gr>     2: +46/-0
#[Out]# 2877   982c3237c63d  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +2/-2
#[Out]# 2876   0ffca0cb9f4b  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +1/-1
#[Out]# 2875   cf86bbb8ed68  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +1/-1
#[Out]# 2736   a5c43944e1ee  Giorgos Keramidas <keramida@ceid.upatras.gr>      1: +5/-1), ('Grauw <laurens.hg@grauw.nl>',               node                       author changestr
#[Out]# n                                                        
#[Out]# 9152  e3ce0c30798b  Grauw <laurens.hg@grauw.nl>  1: +4/-2), ('Greg Lindahl <greg@blekko.com>',                node                          author changestr
#[Out]# n                                                            
#[Out]# 10609  9602fc4e6914  Greg Lindahl <greg@blekko.com>  1: +1/-1), ('Greg Onufer <gonufer@jazzhaiku.com>',               node                               author  changestr
#[Out]# n                                                                 
#[Out]# 9939  9a4034b630c4  Greg Onufer <gonufer@jazzhaiku.com>  3: +83/-2), ('Greg Ward <gerg-hg@gerg.ca>',               node                       author changestr
#[Out]# n                                                        
#[Out]# 7880  4b76746a988b  Greg Ward <gerg-hg@gerg.ca>  1: +1/-1), ('Greg Ward <gerg.ward+hg@gmail.com>',               node                              author  changestr
#[Out]# n                                                                
#[Out]# 7277  08dc0152bb5e  Greg Ward <gerg.ward+hg@gmail.com>  1: +15/-8), ('Greg Ward <greg-hg@gerg.ca>',                node                       author     changestr
#[Out]# n                                                             
#[Out]# 15465  b8d8599410da  Greg Ward <greg-hg@gerg.ca>      1: +1/-1
#[Out]# 15107  cda7a87c1871  Greg Ward <greg-hg@gerg.ca>    1: +42/-38
#[Out]# 13219  115a9760c382  Greg Ward <greg-hg@gerg.ca>      2: +7/-1
#[Out]# 12069  2d3cbcace897  Greg Ward <greg-hg@gerg.ca>      2: +1/-1
#[Out]# 11605  8f40125a0ed8  Greg Ward <greg-hg@gerg.ca>      1: +4/-2
#[Out]# 11540  79231258503b  Greg Ward <greg-hg@gerg.ca>      1: +9/-0
#[Out]# 11536  68a30daead3f  Greg Ward <greg-hg@gerg.ca>      1: +1/-1
#[Out]# 11402  367ce8514da0  Greg Ward <greg-hg@gerg.ca>     1: +32/-0
#[Out]# 11365  c3d7daa0928e  Greg Ward <greg-hg@gerg.ca>      2: +5/-4
#[Out]# 11353  f2b25e8ea6c1  Greg Ward <greg-hg@gerg.ca>     1: +10/-9
#[Out]# 11352  b19067ee4507  Greg Ward <greg-hg@gerg.ca>     1: +1/-33
#[Out]# 11351  1cdc8b5e5729  Greg Ward <greg-hg@gerg.ca>     1: +5/-33
#[Out]# 11346  e740f36cfb4b  Greg Ward <greg-hg@gerg.ca>    4: +16/-13
#[Out]# 11296  7b5d05e0fb1e  Greg Ward <greg-hg@gerg.ca>      1: +1/-7
#[Out]# 11187  9936ed1d04f4  Greg Ward <greg-hg@gerg.ca>     3: +49/-8
#[Out]# 11003  cf016c9831d1  Greg Ward <greg-hg@gerg.ca>      1: +3/-1
#[Out]# 10828  23ab3b05bd66  Greg Ward <greg-hg@gerg.ca>   2: +184/-31
#[Out]# 10816  432eb853a2c6  Greg Ward <greg-hg@gerg.ca>     1: +20/-0
#[Out]# 10815  64e286c22f29  Greg Ward <greg-hg@gerg.ca>     1: +83/-0
#[Out]# 10814  bc81f126139f  Greg Ward <greg-hg@gerg.ca>     1: +19/-3
#[Out]# 10813  c93f0a23f381  Greg Ward <greg-hg@gerg.ca>    1: +16/-16
#[Out]# 10812  1ee14abe07b4  Greg Ward <greg-hg@gerg.ca>     1: +12/-0
#[Out]# 10800  3077ee5ca750  Greg Ward <greg-hg@gerg.ca>      1: +1/-1
#[Out]# 10791  d3ebb1a0bc49  Greg Ward <greg-hg@gerg.ca>      1: +5/-0
#[Out]# 10697  b7ca37b90762  Greg Ward <greg-hg@gerg.ca>     3: +67/-2
#[Out]# 10696  f2ecc5733c89  Greg Ward <greg-hg@gerg.ca>      1: +3/-1
#[Out]# 10652  08870cf7d388  Greg Ward <greg-hg@gerg.ca>     3: +27/-2
#[Out]# 10614  c2e1e637d4da  Greg Ward <greg-hg@gerg.ca>     3: +16/-3
#[Out]# 10604  86dc21148bdb  Greg Ward <greg-hg@gerg.ca>   2: +184/-31
#[Out]# 10598  1037bd445768  Greg Ward <greg-hg@gerg.ca>      1: +3/-0
#[Out]# 10558  b1339234080e  Greg Ward <greg-hg@gerg.ca>    1: +25/-20
#[Out]# 10503  b3311e26f94f  Greg Ward <greg-hg@gerg.ca>     3: +19/-7
#[Out]# 10502  d2c1fc440533  Greg Ward <greg-hg@gerg.ca>     2: +10/-9
#[Out]# 10270  49a8625b8cac  Greg Ward <greg-hg@gerg.ca>      1: +9/-5
#[Out]# 10083  c1d940d31aea  Greg Ward <greg-hg@gerg.ca>     2: +87/-0
#[Out]# 10057  bc3f762af82e  Greg Ward <greg-hg@gerg.ca>      2: +6/-8
#[Out]# 10047  48b81d9bca8d  Greg Ward <greg-hg@gerg.ca>     3: +26/-2
#[Out]# 10046  720f70b720d3  Greg Ward <greg-hg@gerg.ca>     5: +34/-2
#[Out]# 9975   279c8a73fde1  Greg Ward <greg-hg@gerg.ca>      1: +9/-2
#[Out]# 9958   43f8abcec42d  Greg Ward <greg-hg@gerg.ca>      1: +2/-2
#[Out]# 9928   ffa6f2eb934e  Greg Ward <greg-hg@gerg.ca>      1: +2/-1
#[Out]# 9917   27267b1f68b4  Greg Ward <greg-hg@gerg.ca>    1: +43/-21
#[Out]# 9707   38deec407f8d  Greg Ward <greg-hg@gerg.ca>     1: +29/-5
#[Out]# 9706   f8b4df4b033d  Greg Ward <greg-hg@gerg.ca>    1: +22/-11
#[Out]# 9559   f57640bf10d4  Greg Ward <greg-hg@gerg.ca>      2: +9/-8
#[Out]# 9543   bc19a0b04e83  Greg Ward <greg-hg@gerg.ca>    1: +44/-11
#[Out]# 9540   f7d85980261c  Greg Ward <greg-hg@gerg.ca>    1: +218/-0
#[Out]# 9487   1c4e4004f3a6  Greg Ward <greg-hg@gerg.ca>     3: +21/-9
#[Out]# 9433   9ff178e7b627  Greg Ward <greg-hg@gerg.ca>     3: +15/-1
#[Out]# 9388   cfdcb7a465af  Greg Ward <greg-hg@gerg.ca>     2: +16/-1
#[Out]# 9322   8a4da1388553  Greg Ward <greg-hg@gerg.ca>      1: +4/-0
#[Out]# 9271   4017291c4c48  Greg Ward <greg-hg@gerg.ca>    5: +63/-23
#[Out]# 9270   f528d1a93491  Greg Ward <greg-hg@gerg.ca>   6: +238/-11
#[Out]# 9269   09a1ee498756  Greg Ward <greg-hg@gerg.ca>     2: +12/-0
#[Out]# 9268   abb7d4d43a5f  Greg Ward <greg-hg@gerg.ca>   2: +125/-93
#[Out]# 9267   b7837f0ed9fe  Greg Ward <greg-hg@gerg.ca>     1: +20/-9
#[Out]# 9266   234a230cc33b  Greg Ward <greg-hg@gerg.ca>    1: +44/-41
#[Out]# 9265   5614a628d173  Greg Ward <greg-hg@gerg.ca>    3: +18/-12
#[Out]# 9264   6b03f93b8ff3  Greg Ward <greg-hg@gerg.ca>    3: +35/-25
#[Out]# 9263   ad72e3b08bc0  Greg Ward <greg-hg@gerg.ca>     2: +66/-0
#[Out]# 9262   a604c98dbf62  Greg Ward <greg-hg@gerg.ca>   2: +120/-78
#[Out]# 9234   60e88d321171  Greg Ward <greg-hg@gerg.ca>      1: +3/-1
#[Out]# 9148   49b62395e910  Greg Ward <greg-hg@gerg.ca>    3: +18/-10
#[Out]# 9144   8d7d68dd91fd  Greg Ward <greg-hg@gerg.ca>    1: +17/-15
#[Out]# 9033   a85a3d398cc3  Greg Ward <greg-hg@gerg.ca>      1: +1/-1
#[Out]# 9022   89fd11257d75  Greg Ward <greg-hg@gerg.ca>      1: +3/-1
#[Out]# 8945   7b3d837ca60e  Greg Ward <greg-hg@gerg.ca>     3: +22/-2
#[Out]# 8943   09ff905cdc86  Greg Ward <greg-hg@gerg.ca>      1: +3/-1
#[Out]# 8880   a3a936a2fe46  Greg Ward <greg-hg@gerg.ca>     1: +11/-9
#[Out]# 8821   c66e324d3961  Greg Ward <greg-hg@gerg.ca>    2: +21/-16
#[Out]# 8820   e8cb1fa0d4a9  Greg Ward <greg-hg@gerg.ca>      1: +3/-3
#[Out]# 8819   e93ab347c814  Greg Ward <greg-hg@gerg.ca>    2: +69/-50
#[Out]# 8818   727f7aaefaab  Greg Ward <greg-hg@gerg.ca>  6: +262/-246
#[Out]# 8690   78ab2a12b4d9  Greg Ward <greg-hg@gerg.ca>      1: +6/-3
#[Out]# 8677   0941ee76489e  Greg Ward <greg-hg@gerg.ca>    3: +94/-21
#[Out]# 8676   a8066f2fd1aa  Greg Ward <greg-hg@gerg.ca>      1: +5/-3
#[Out]# 8675   d6b243731763  Greg Ward <greg-hg@gerg.ca>    1: +33/-27
#[Out]# 8674   a434c94b48e7  Greg Ward <greg-hg@gerg.ca>      1: +7/-2
#[Out]# 8654   27cc4fa6722d  Greg Ward <greg-hg@gerg.ca>      1: +1/-1
#[Out]# 8450   057e96fe2955  Greg Ward <greg-hg@gerg.ca>      2: +6/-2
#[Out]# 8376   94e91205d9b6  Greg Ward <greg-hg@gerg.ca>      1: +1/-1
#[Out]# 8319   1268b895f69b  Greg Ward <greg-hg@gerg.ca>      1: +1/-1
#[Out]# 8316   7a0fcdd3828f  Greg Ward <greg-hg@gerg.ca>     3: +23/-2
#[Out]# 8264   2c7c973c2abd  Greg Ward <greg-hg@gerg.ca>   2: +144/-25
#[Out]# 8189   4e5bd9b97bb3  Greg Ward <greg-hg@gerg.ca>    3: +70/-30
#[Out]# 8188   6c4fdde87f90  Greg Ward <greg-hg@gerg.ca>    2: +209/-0
#[Out]# 8124   f5428d4ffd97  Greg Ward <greg-hg@gerg.ca>    1: +21/-24
#[Out]# 8123   60a9e3cf0cf4  Greg Ward <greg-hg@gerg.ca>    1: +63/-59
#[Out]# 8122   70d8f70264c4  Greg Ward <greg-hg@gerg.ca>    1: +39/-39
#[Out]# 8121   c49578c5122f  Greg Ward <greg-hg@gerg.ca>      1: +7/-7
#[Out]# 8120   e85cc856d2e1  Greg Ward <greg-hg@gerg.ca>    1: +65/-53
#[Out]# 8113   5b3fee9c1f4d  Greg Ward <greg-hg@gerg.ca>      1: +4/-0
#[Out]# 8110   19229b0b292d  Greg Ward <greg-hg@gerg.ca>     1: +11/-0
#[Out]# 8109   fb162c47000b  Greg Ward <greg-hg@gerg.ca>      1: +1/-0
#[Out]# 8107   d051342f1ad1  Greg Ward <greg-hg@gerg.ca>      1: +1/-1
#[Out]# 7996   9bbcfa898cd3  Greg Ward <greg-hg@gerg.ca>      1: +3/-2
#[Out]# 7977   026bcd12a0ad  Greg Ward <greg-hg@gerg.ca>      2: +2/-2
#[Out]# 7870   6c3b8132078e  Greg Ward <greg-hg@gerg.ca>    2: +60/-44
#[Out]# 7847   02981000012e  Greg Ward <greg-hg@gerg.ca>    3: +195/-2), ('Greg Ward <greg@gerg.ca>',                node                    author    changestr
#[Out]# n                                                         
#[Out]# 16344  d76b9abd1509  Greg Ward <greg@gerg.ca>   2: +14/-19
#[Out]# 16343  90ca62bb9e78  Greg Ward <greg@gerg.ca>     1: +1/-2
#[Out]# 16165  bc1d949261c4  Greg Ward <greg@gerg.ca>     1: +3/-2
#[Out]# 16162  aae219a99a6e  Greg Ward <greg@gerg.ca>     1: +5/-1
#[Out]# 16107  82ce91a9fd94  Greg Ward <greg@gerg.ca>    1: +12/-4
#[Out]# 16106  be6ac2ecc7f8  Greg Ward <greg@gerg.ca>     1: +4/-1
#[Out]# 15366  06b8db3f25c6  Greg Ward <greg@gerg.ca>    1: +45/-0
#[Out]# 15365  ca1412c15efe  Greg Ward <greg@gerg.ca>    1: +15/-0
#[Out]# 15350  8b8dd13295db  Greg Ward <greg@gerg.ca>     1: +1/-1
#[Out]# 15349  63455eb771af  Greg Ward <greg@gerg.ca>    2: +4/-11
#[Out]# 15343  7fe8b7e097a4  Greg Ward <greg@gerg.ca>   1: +43/-16
#[Out]# 15342  b2e00d67f590  Greg Ward <greg@gerg.ca>    1: +91/-0
#[Out]# 15341  7ef13e53434e  Greg Ward <greg@gerg.ca>   1: +51/-23
#[Out]# 15340  0e58513cc59a  Greg Ward <greg@gerg.ca>    2: +12/-5
#[Out]# 15339  be1377d19018  Greg Ward <greg@gerg.ca>   2: +25/-20
#[Out]# 15338  f4b29792fcda  Greg Ward <greg@gerg.ca>   2: +63/-55
#[Out]# 15332  0db47b8d025f  Greg Ward <greg@gerg.ca>     2: +4/-4
#[Out]# 15331  bc4d8804855c  Greg Ward <greg@gerg.ca>    1: +19/-2
#[Out]# 15330  1e6fcce4aab3  Greg Ward <greg@gerg.ca>   1: +10/-12
#[Out]# 15329  944f9b7cfe4e  Greg Ward <greg@gerg.ca>    1: +22/-6
#[Out]# 15328  9b4ab5f7ad2a  Greg Ward <greg@gerg.ca>   1: +25/-27
#[Out]# 15306  94527d67f3da  Greg Ward <greg@gerg.ca>    1: +7/-11
#[Out]# 15305  683f417fa538  Greg Ward <greg@gerg.ca>    2: +3/-10
#[Out]# 15304  9aa9d4bb3d88  Greg Ward <greg@gerg.ca>     3: +5/-5
#[Out]# 15264  157d93c41c10  Greg Ward <greg@gerg.ca>    2: +26/-1
#[Out]# 15255  7ab05d752405  Greg Ward <greg@gerg.ca>   6: +53/-44
#[Out]# 15254  dd03d3a9f888  Greg Ward <greg@gerg.ca>   4: +60/-58
#[Out]# 15253  67d010779907  Greg Ward <greg@gerg.ca>   6: +17/-14
#[Out]# 15252  6e809bb4f969  Greg Ward <greg@gerg.ca>  10: +97/-92
#[Out]# 15230  697289c5d415  Greg Ward <greg@gerg.ca>   2: +91/-26
#[Out]# 15229  89e19ca2a90e  Greg Ward <greg@gerg.ca>     1: +1/-2
#[Out]# 15228  ee625de3541e  Greg Ward <greg@gerg.ca>     2: +3/-3
#[Out]# 15227  a7686abf73a6  Greg Ward <greg@gerg.ca>   3: +18/-21
#[Out]# 15204  3ce9b1a7538b  Greg Ward <greg@gerg.ca>    2: +18/-1
#[Out]# 15199  56da00994067  Greg Ward <greg@gerg.ca>     1: +3/-1
#[Out]# 15198  62dc0e7ab092  Greg Ward <greg@gerg.ca>   4: +39/-15
#[Out]# 15197  7f65ce5cc011  Greg Ward <greg@gerg.ca>     1: +2/-1
#[Out]# 15196  7f78a4137f8f  Greg Ward <greg@gerg.ca>     1: +1/-1
#[Out]# 15195  5b2a3bb06cef  Greg Ward <greg@gerg.ca>    1: +9/-10
#[Out]# 15194  0705f2ac79d6  Greg Ward <greg@gerg.ca>   5: +21/-17
#[Out]# 15189  8e115063950d  Greg Ward <greg@gerg.ca>     3: +3/-4
#[Out]# 15187  59e8bc22506e  Greg Ward <greg@gerg.ca>   6: +61/-12
#[Out]# 15170  7bddec632821  Greg Ward <greg@gerg.ca>  2: +120/-47
#[Out]# 15169  d67a15b2e608  Greg Ward <greg@gerg.ca>   1: +18/-19
#[Out]# 15141  7c26ce9edbd2  Greg Ward <greg@gerg.ca>  13: +57/-57
#[Out]# 15140  3d44e68360a6  Greg Ward <greg@gerg.ca>   2: +28/-23
#[Out]# 15118  4c1ec0fe59d6  Greg Ward <greg@gerg.ca>   1: +23/-23
#[Out]# 15111  a21ccf4412d5  Greg Ward <greg@gerg.ca>    2: +10/-1
#[Out]# 15086  774da7121fc9  Greg Ward <greg@gerg.ca>  13: +25/-27
#[Out]# 14052  da65edcac72a  Greg Ward <greg@gerg.ca>     1: +8/-5
#[Out]# 14051  d764463b433e  Greg Ward <greg@gerg.ca>   3: +65/-13
#[Out]# 13790  a464763e99f1  Greg Ward <greg@gerg.ca>   2: +145/-0
#[Out]# 10016  4f1ee228e577  Greg Ward <greg@gerg.ca>     1: +5/-1
#[Out]# 9883   be574a37a8ae  Greg Ward <greg@gerg.ca>     1: +5/-1
#[Out]# 9175   10532b29cdee  Greg Ward <greg@gerg.ca>     1: +3/-1), ('Guillaume Chazarain <guichaz@yahoo.fr>',               node                                  author changestr
#[Out]# n                                                                   
#[Out]# 4839  c13610d5642c  Guillaume Chazarain <guichaz@yahoo.fr>  1: +1/-1), ('Guy Brand <gb@isis.u-strasbg.fr>',               node                            author changestr
#[Out]# n                                                             
#[Out]# 1613  17e39fd24cb4  Guy Brand <gb@isis.u-strasbg.fr>  3: +3/-2), ('Haakon Riiser <haakon.riiser@fys.uio.no>',               node                                    author   changestr
#[Out]# n                                                                       
#[Out]# 2580  a20a1bb0c396  Haakon Riiser <haakon.riiser@fys.uio.no>  5: +65/-16), ('Hao Lian <hao@fogcreek.com>',                node                       author   changestr
#[Out]# n                                                           
#[Out]# 15404  db8b0ee74025  Hao Lian <hao@fogcreek.com>    1: +3/-1
#[Out]# 15391  a5a6a9b7f3b9  Hao Lian <hao@fogcreek.com>  2: +21/-12
#[Out]# 15371  f26ed4ea46d8  Hao Lian <hao@fogcreek.com>    3: +4/-8
#[Out]# 15302  225d30bacabd  Hao Lian <hao@fogcreek.com>    1: +1/-1), ('Henri Precheur <henry@precheur.org>',               node                               author changestr
#[Out]# n                                                                
#[Out]# 4072  2d3379c598c1  Henri Precheur <henry@precheur.org>  1: +1/-1), ('Henri Wiechers <hwiechers@gmail.com>',                node                                author   changestr
#[Out]# n                                                                    
#[Out]# 14308  1f9e11f65cd7  Henri Wiechers <hwiechers@gmail.com>  4: +103/-4
#[Out]# 10324  86a6bc519592  Henri Wiechers <hwiechers@gmail.com>    1: +1/-1
#[Out]# 10323  808c187fc556  Henri Wiechers <hwiechers@gmail.com>    1: +1/-1
#[Out]# 10206  69a974125938  Henri Wiechers <hwiechers@gmail.com>   2: +33/-0
#[Out]# 10205  f6ac05b5684b  Henri Wiechers <hwiechers@gmail.com>   2: +11/-0
#[Out]# 10204  44fa0e205ec9  Henri Wiechers <hwiechers@gmail.com>   2: +77/-0
#[Out]# 10203  827b7d6f9016  Henri Wiechers <hwiechers@gmail.com>   2: +27/-0
#[Out]# 10202  5d868e0565f6  Henri Wiechers <hwiechers@gmail.com>   2: +16/-0
#[Out]# 10201  d09bed527343  Henri Wiechers <hwiechers@gmail.com>   2: +11/-0
#[Out]# 10188  ac212bcc852b  Henri Wiechers <hwiechers@gmail.com>   2: +29/-0
#[Out]# 10182  9ed13f718e53  Henri Wiechers <hwiechers@gmail.com>   2: +66/-0
#[Out]# 10019  cb2a1836c50a  Henri Wiechers <hwiechers@gmail.com>    1: +8/-8
#[Out]# 10003  d6a95c5f6ff9  Henri Wiechers <hwiechers@gmail.com>    1: +4/-4
#[Out]# 9167   87c05a78e588  Henri Wiechers <hwiechers@gmail.com>   2: +21/-0
#[Out]# 9039   35c3f94233a0  Henri Wiechers <hwiechers@gmail.com>   1: +13/-7
#[Out]# 8733   f037187a6f68  Henri Wiechers <hwiechers@gmail.com>    2: +2/-2), ('Henrik Stuart <henrik.stuart at edlund.dk>',               node                                      author  changestr
#[Out]# n                                                                        
#[Out]# 8068  1280934dd2dd  Henrik Stuart <henrik.stuart at edlund.dk>  3: +40/-1), ('Henrik Stuart <henrik.stuart@edlund.dk>',                node                                   author    changestr
#[Out]# n                                                                        
#[Out]# 15900  73c4b3d0c711  Henrik Stuart <henrik.stuart@edlund.dk>     1: +4/-3
#[Out]# 10685  4f11978ae45d  Henrik Stuart <henrik.stuart@edlund.dk>    3: +39/-0
#[Out]# 10684  9606edb8777e  Henrik Stuart <henrik.stuart@edlund.dk>     1: +1/-3
#[Out]# 9861   0262bb59016f  Henrik Stuart <henrik.stuart@edlund.dk>    2: +10/-1
#[Out]# 9671   9471d9a900b4  Henrik Stuart <henrik.stuart@edlund.dk>    3: +76/-9
#[Out]# 9021   89ae64a4e2ec  Henrik Stuart <henrik.stuart@edlund.dk>     1: +1/-1
#[Out]# 8566   f8ff65a83169  Henrik Stuart <henrik.stuart@edlund.dk>    2: +27/-1
#[Out]# 8565   e3495c399006  Henrik Stuart <henrik.stuart@edlund.dk>    4: +30/-9
#[Out]# 8375   fa901423ac23  Henrik Stuart <henrik.stuart@edlund.dk>    1: +27/-0
#[Out]# 8304   f00573bc93f8  Henrik Stuart <henrik.stuart@edlund.dk>   2: +33/-27
#[Out]# 8103   e8a28556a0a8  Henrik Stuart <henrik.stuart@edlund.dk>  4: +141/-10
#[Out]# 8102   ecf7795479d5  Henrik Stuart <henrik.stuart@edlund.dk>     1: +3/-2
#[Out]# 8101   9f14b66830a8  Henrik Stuart <henrik.stuart@edlund.dk>     1: +9/-3
#[Out]# 8002   3e7611a83230  Henrik Stuart <henrik.stuart@edlund.dk>   4: +283/-2), ('Henrik Stuart <hg@hstuart.dk>',                node                         author     changestr
#[Out]# n                                                               
#[Out]# 12951  6c800e7ef2f6  Henrik Stuart <hg@hstuart.dk>     2: +42/-1
#[Out]# 12618  64db820c66a2  Henrik Stuart <hg@hstuart.dk>     2: +96/-1
#[Out]# 11770  c20c2c4c0c63  Henrik Stuart <hg@hstuart.dk>    5: +73/-60
#[Out]# 11769  f4b03295b1d9  Henrik Stuart <hg@hstuart.dk>      0: +0/-0
#[Out]# 11768  724362365ea0  Henrik Stuart <hg@hstuart.dk>  25: +329/-74
#[Out]# 11526  164eb14a4a7c  Henrik Stuart <hg@hstuart.dk>  18: +186/-34
#[Out]# 11274  e8a66a40474d  Henrik Stuart <hg@hstuart.dk>      2: +2/-2
#[Out]# 11272  457813cb3024  Henrik Stuart <hg@hstuart.dk>     3: +48/-8
#[Out]# 11247  1e701ffd9df4  Henrik Stuart <hg@hstuart.dk>    4: +186/-1
#[Out]# 11089  4efdccaca21d  Henrik Stuart <hg@hstuart.dk>      1: +2/-1
#[Out]# 11054  0a548640e012  Henrik Stuart <hg@hstuart.dk>   4: +137/-23
#[Out]# 10418  4cfd0d56be6d  Henrik Stuart <hg@hstuart.dk>      1: +3/-0
#[Out]# 10412  b59fba37e5e6  Henrik Stuart <hg@hstuart.dk>      1: +1/-1
#[Out]# 10411  4c94a3df4b10  Henrik Stuart <hg@hstuart.dk>     2: +76/-2
#[Out]# 10347  b8e3aeb7542c  Henrik Stuart <hg@hstuart.dk>      1: +3/-3
#[Out]# 10346  579aae5aa549  Henrik Stuart <hg@hstuart.dk>      1: +8/-1
#[Out]# 10345  c203878e58ba  Henrik Stuart <hg@hstuart.dk>    6: +10/-10
#[Out]# 10086  931d2c757627  Henrik Stuart <hg@hstuart.dk>     3: +13/-1
#[Out]# 10014  510122bb3c7f  Henrik Stuart <hg@hstuart.dk>     3: +11/-2
#[Out]# 9853   a033929bd34e  Henrik Stuart <hg@hstuart.dk>  1: +144/-117
#[Out]# 9851   917cf6bb6d0c  Henrik Stuart <hg@hstuart.dk>  1: +144/-117
#[Out]# 9609   aa404f3f661b  Henrik Stuart <hg@hstuart.dk>    2: +16/-17
#[Out]# 9419   d0474b184347  Henrik Stuart <hg@hstuart.dk>      1: +3/-0
#[Out]# 9032   d3b995dd4eab  Henrik Stuart <hg@hstuart.dk>      1: +2/-3
#[Out]# 9029   eef406165507  Henrik Stuart <hg@hstuart.dk>      1: +1/-0
#[Out]# 9020   0b2b269ba3d0  Henrik Stuart <hg@hstuart.dk>     3: +32/-1
#[Out]# 9012   5ed463d0ebdb  Henrik Stuart <hg@hstuart.dk>      1: +1/-1
#[Out]# 8951   835a51e63c5b  Henrik Stuart <hg@hstuart.dk>    2: +4/-139
#[Out]# 8903   d403cf4eb32d  Henrik Stuart <hg@hstuart.dk>      1: +5/-3
#[Out]# 8848   89b71acdac9a  Henrik Stuart <hg@hstuart.dk>      1: +6/-0
#[Out]# 8847   7951f385fcb7  Henrik Stuart <hg@hstuart.dk>     2: +46/-8
#[Out]# 8846   b30775386d40  Henrik Stuart <hg@hstuart.dk>     2: +14/-5
#[Out]# 8845   296767acbb55  Henrik Stuart <hg@hstuart.dk>      1: +2/-1
#[Out]# 8757   6019e6517f95  Henrik Stuart <hg@hstuart.dk>   5: +201/-18
#[Out]# 8606   b60617a9cd3c  Henrik Stuart <hg@hstuart.dk>      1: +2/-2
#[Out]# 8598   b8f45ad20772  Henrik Stuart <hg@hstuart.dk>      1: +5/-5
#[Out]# 8597   06edf7982958  Henrik Stuart <hg@hstuart.dk>    1: +12/-12
#[Out]# 8596   13b69b40006f  Henrik Stuart <hg@hstuart.dk>      1: +2/-2
#[Out]# 8594   08c93b07f5ad  Henrik Stuart <hg@hstuart.dk>      2: +2/-0
#[Out]# 8593   59acb9c7d90f  Henrik Stuart <hg@hstuart.dk>    1: +149/-2
#[Out]# 8563   4429751f5da7  Henrik Stuart <hg@hstuart.dk>      1: +1/-1
#[Out]# 8374   c8e81f557da7  Henrik Stuart <hg@hstuart.dk>     2: +25/-0
#[Out]# 8305   48a382c23226  Henrik Stuart <hg@hstuart.dk>    3: +39/-40
#[Out]# 8302   f5c1a9094e41  Henrik Stuart <hg@hstuart.dk>     1: +12/-2
#[Out]# 8301   560af1bbfd6e  Henrik Stuart <hg@hstuart.dk>      1: +6/-2
#[Out]# 8300   fe8a3e56039f  Henrik Stuart <hg@hstuart.dk>     1: +19/-1
#[Out]# 8179   094e0d982c8a  Henrik Stuart <hg@hstuart.dk>     3: +32/-2
#[Out]# 8063   777a9efdae2d  Henrik Stuart <hg@hstuart.dk>     3: +33/-6), ('Hidetaka Iwai  <tyuyu@debian.or.jp>',               node                               author     changestr
#[Out]# n                                                                    
#[Out]# 1500  cadde8ebf167  Hidetaka Iwai  <tyuyu@debian.or.jp>     2: +24/-1
#[Out]# 1499  874efc57e00a  Hidetaka Iwai  <tyuyu@debian.or.jp>  3: +683/-683), ('Hiroshi Funai <hfunai@gmail.com>',               node                            author    changestr
#[Out]# n                                                                
#[Out]# 7119  91b0ada2d94b  Hiroshi Funai <hfunai@gmail.com>  19: +836/-0), ('Hollis Blanchard <hollisb@us.ibm.com>',               node                                 author  changestr
#[Out]# n                                                                   
#[Out]# 5482  ec2cc1dadbf7  Hollis Blanchard <hollisb@us.ibm.com>   1: +6/-0
#[Out]# 4719  1069205a8894  Hollis Blanchard <hollisb@us.ibm.com>  1: +12/-7
#[Out]# 1950  5f581f337b05  Hollis Blanchard <hollisb@us.ibm.com>   1: +2/-2), ('Idan Kamara <idankk86@gmail.com>',                node                            author     changestr
#[Out]# n                                                                  
#[Out]# 16643  9c86ef980d9e  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 16635  9a99224a6409  Idan Kamara <idankk86@gmail.com>      1: +3/-3
#[Out]# 16591  f30226b1a46a  Idan Kamara <idankk86@gmail.com>     2: +40/-1
#[Out]# 16473  7adc521259d4  Idan Kamara <idankk86@gmail.com>    2: +52/-48
#[Out]# 16472  14a4e17f0817  Idan Kamara <idankk86@gmail.com>      1: +5/-1
#[Out]# 16471  85c7602e283a  Idan Kamara <idankk86@gmail.com>    1: +22/-16
#[Out]# 16470  b2e1da5db6df  Idan Kamara <idankk86@gmail.com>    1: +40/-36
#[Out]# 16458  55982f62651f  Idan Kamara <idankk86@gmail.com>   5: +482/-18
#[Out]# 16393  e03d8a40521f  Idan Kamara <idankk86@gmail.com>      1: +2/-2
#[Out]# 16313  e8eecfe37d4e  Idan Kamara <idankk86@gmail.com>      1: +0/-4
#[Out]# 16312  b5c0c7d0f83f  Idan Kamara <idankk86@gmail.com>      1: +9/-1
#[Out]# 16311  97efd26eb957  Idan Kamara <idankk86@gmail.com>     1: +11/-7
#[Out]# 16121  53e2cd303ecf  Idan Kamara <idankk86@gmail.com>     3: +28/-1
#[Out]# 16120  fb7c4c14223f  Idan Kamara <idankk86@gmail.com>     3: +26/-1
#[Out]# 16119  9d4a2942a732  Idan Kamara <idankk86@gmail.com>      2: +7/-3
#[Out]# 16118  8181bd808dc5  Idan Kamara <idankk86@gmail.com>      1: +5/-2
#[Out]# 16117  fa8488565afd  Idan Kamara <idankk86@gmail.com>     2: +19/-6
#[Out]# 16111  7c75924a6926  Idan Kamara <idankk86@gmail.com>     4: +41/-2
#[Out]# 16109  41bef17e6ad8  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 16086  6ecf5fb2a475  Idan Kamara <idankk86@gmail.com>      2: +4/-2
#[Out]# 16085  ce0ad184f489  Idan Kamara <idankk86@gmail.com>     3: +25/-0
#[Out]# 16084  236bb604dc39  Idan Kamara <idankk86@gmail.com>     4: +32/-4
#[Out]# 16083  acfca07a8f26  Idan Kamara <idankk86@gmail.com>      3: +6/-0
#[Out]# 16082  3f75fb837638  Idan Kamara <idankk86@gmail.com>      1: +1/-0
#[Out]# 15989  6548a2e32285  Idan Kamara <idankk86@gmail.com>     2: +14/-0
#[Out]# 15988  827e0126738d  Idan Kamara <idankk86@gmail.com>      1: +8/-4
#[Out]# 15987  b5f6a63b4ded  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 15958  0d2ac0299020  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 15259  1d1f6dff9364  Idan Kamara <idankk86@gmail.com>     1: +47/-0
#[Out]# 15258  fe9677449331  Idan Kamara <idankk86@gmail.com>    1: +20/-15
#[Out]# 15249  f30c0a7b8346  Idan Kamara <idankk86@gmail.com>     1: +14/-0
#[Out]# 15248  3efbb5e8bf5c  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 15247  3cd1605e9d8e  Idan Kamara <idankk86@gmail.com>      1: +9/-5
#[Out]# 15236  4fae5df4b1bb  Idan Kamara <idankk86@gmail.com>     1: +22/-2
#[Out]# 15235  f7044da7a793  Idan Kamara <idankk86@gmail.com>      1: +9/-0
#[Out]# 15001  b4c06b97dfe0  Idan Kamara <idankk86@gmail.com>     3: +41/-0
#[Out]# 14998  9dca7653b525  Idan Kamara <idankk86@gmail.com>    1: +45/-30
#[Out]# 14997  4ae7473f5b73  Idan Kamara <idankk86@gmail.com>      1: +9/-3
#[Out]# 14996  019fe0b0a7af  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14995  f61a85b2affa  Idan Kamara <idankk86@gmail.com>      1: +2/-2
#[Out]# 14994  d3ac759a6d66  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14993  a710936c3037  Idan Kamara <idankk86@gmail.com>      1: +8/-1
#[Out]# 14992  372d9d8b1da4  Idan Kamara <idankk86@gmail.com>     1: +24/-3
#[Out]# 14991  4bf9493e7b07  Idan Kamara <idankk86@gmail.com>      2: +7/-0
#[Out]# 14990  dca59d5be12d  Idan Kamara <idankk86@gmail.com>    3: +202/-0
#[Out]# 14989  2aa3e07b2f07  Idan Kamara <idankk86@gmail.com>     4: +35/-0
#[Out]# 14931  11b5a5d2ca8b  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14930  510c893a726f  Idan Kamara <idankk86@gmail.com>      1: +2/-2
#[Out]# 14868  17ffb30d9174  Idan Kamara <idankk86@gmail.com>      1: +2/-2
#[Out]# 14856  f4b7be3f8430  Idan Kamara <idankk86@gmail.com>      1: +9/-0
#[Out]# 14849  68b5d7005cca  Idan Kamara <idankk86@gmail.com>      1: +9/-6
#[Out]# 14844  e5b2ee5157ae  Idan Kamara <idankk86@gmail.com>     1: +10/-6
#[Out]# 14843  188936b334b1  Idan Kamara <idankk86@gmail.com>     2: +26/-6
#[Out]# 14827  d2d592718e90  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14826  a59058fd074a  Idan Kamara <idankk86@gmail.com>     3: +22/-0
#[Out]# 14824  bb2cffe81a94  Idan Kamara <idankk86@gmail.com>     3: +33/-2
#[Out]# 14822  5233df79deed  Idan Kamara <idankk86@gmail.com>      1: +3/-1
#[Out]# 14817  1b872599f39f  Idan Kamara <idankk86@gmail.com>     3: +19/-2
#[Out]# 14816  1c148e935244  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14804  35f5cfdd0427  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14760  95a8c0f5dd3f  Idan Kamara <idankk86@gmail.com>    2: +167/-0
#[Out]# 14745  189a7562d72e  Idan Kamara <idankk86@gmail.com>      1: +5/-1
#[Out]# 14744  10dcb3e7cb55  Idan Kamara <idankk86@gmail.com>      1: +5/-0
#[Out]# 14743  99ace3cb7352  Idan Kamara <idankk86@gmail.com>      1: +8/-3
#[Out]# 14742  712954a67be3  Idan Kamara <idankk86@gmail.com>      1: +4/-1
#[Out]# 14741  f5f97a0f983f  Idan Kamara <idankk86@gmail.com>      1: +4/-1
#[Out]# 14740  e3be7dc9a5e1  Idan Kamara <idankk86@gmail.com>      1: +2/-1
#[Out]# 14739  1b8c70c9f47c  Idan Kamara <idankk86@gmail.com>    2: +12/-16
#[Out]# 14736  23325c5ef6a7  Idan Kamara <idankk86@gmail.com>      1: +6/-1
#[Out]# 14735  84a680daa4b2  Idan Kamara <idankk86@gmail.com>      1: +3/-2
#[Out]# 14734  271424fdbeec  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14733  39235b398248  Idan Kamara <idankk86@gmail.com>      1: +2/-1
#[Out]# 14732  d83ad13a280e  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14731  a95efd378641  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14730  bcc1a9fd0b8c  Idan Kamara <idankk86@gmail.com>      1: +2/-1
#[Out]# 14725  e9ed3506f066  Idan Kamara <idankk86@gmail.com>    3: +17/-92
#[Out]# 14722  350dcd481410  Idan Kamara <idankk86@gmail.com>      1: +2/-2
#[Out]# 14721  d4b9d3b91ce7  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14714  c19de7f32961  Idan Kamara <idankk86@gmail.com>      1: +6/-2
#[Out]# 14708  8a62bae94425  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14707  ac70f8d5987c  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14704  964a72038bb0  Idan Kamara <idankk86@gmail.com>      1: +4/-1
#[Out]# 14703  5fd5dd9a610a  Idan Kamara <idankk86@gmail.com>      1: +3/-0
#[Out]# 14647  2e9f379de0ac  Idan Kamara <idankk86@gmail.com>    4: +231/-4
#[Out]# 14646  001788ef4bbb  Idan Kamara <idankk86@gmail.com>      1: +3/-1
#[Out]# 14640  406b6d7bdcb9  Idan Kamara <idankk86@gmail.com>      2: +2/-2
#[Out]# 14639  e59a7b8f521a  Idan Kamara <idankk86@gmail.com>      1: +4/-4
#[Out]# 14638  1bdbca0b6604  Idan Kamara <idankk86@gmail.com>     1: +16/-1
#[Out]# 14637  5e9d691229d5  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14636  b98063487a6f  Idan Kamara <idankk86@gmail.com>      1: +2/-2
#[Out]# 14635  217b7d83afc3  Idan Kamara <idankk86@gmail.com>    5: +10/-10
#[Out]# 14618  110d75f0abb3  Idan Kamara <idankk86@gmail.com>    1: +10/-10
#[Out]# 14615  9fba795dd030  Idan Kamara <idankk86@gmail.com>     1: +20/-4
#[Out]# 14614  afccc64eea73  Idan Kamara <idankk86@gmail.com>    4: +36/-25
#[Out]# 14613  ea8938d3a5aa  Idan Kamara <idankk86@gmail.com>      1: +6/-1
#[Out]# 14612  4e1ccd4c2b6d  Idan Kamara <idankk86@gmail.com>      1: +8/-0
#[Out]# 14604  b1a534335548  Idan Kamara <idankk86@gmail.com>      1: +5/-3
#[Out]# 14601  25c1f3ddd927  Idan Kamara <idankk86@gmail.com>     2: +24/-6
#[Out]# 14600  17c16bcf6926  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14599  b28004513977  Idan Kamara <idankk86@gmail.com>    2: +15/-12
#[Out]# 14598  259ba7502370  Idan Kamara <idankk86@gmail.com>      1: +1/-0
#[Out]# 14516  842a9179132c  Idan Kamara <idankk86@gmail.com>     3: +29/-2
#[Out]# 14515  76f295eaed86  Idan Kamara <idankk86@gmail.com>    4: +20/-19
#[Out]# 14510  eccbb9980ada  Idan Kamara <idankk86@gmail.com>    1: +26/-20
#[Out]# 14485  755aabb3eada  Idan Kamara <idankk86@gmail.com>      1: +3/-3
#[Out]# 14479  f6a433671c06  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14466  7d171c05a631  Idan Kamara <idankk86@gmail.com>     1: +30/-0
#[Out]# 14465  7d367e8f892d  Idan Kamara <idankk86@gmail.com>      2: +2/-1
#[Out]# 14464  f63b7fb4b5f6  Idan Kamara <idankk86@gmail.com>     1: +12/-1
#[Out]# 14463  95715c2f90bf  Idan Kamara <idankk86@gmail.com>      1: +3/-5
#[Out]# 14458  39e81b9377e6  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14456  80c599eee3f3  Idan Kamara <idankk86@gmail.com>     1: +13/-8
#[Out]# 14455  08bfec2ef031  Idan Kamara <idankk86@gmail.com>    2: +19/-12
#[Out]# 14444  9d4cabd189df  Idan Kamara <idankk86@gmail.com>      1: +5/-1
#[Out]# 14443  1df64ccef23e  Idan Kamara <idankk86@gmail.com>    2: +372/-0
#[Out]# 14442  e89534504fb9  Idan Kamara <idankk86@gmail.com>    1: +18/-14
#[Out]# 14441  4eb88d296f63  Idan Kamara <idankk86@gmail.com>     3: +11/-1
#[Out]# 14440  7230aef66b7c  Idan Kamara <idankk86@gmail.com>     1: +5/-24
#[Out]# 14439  2e77525e52d9  Idan Kamara <idankk86@gmail.com>      1: +8/-0
#[Out]# 14433  253bda94372e  Idan Kamara <idankk86@gmail.com>      1: +4/-4
#[Out]# 14432  c238b12a1ed4  Idan Kamara <idankk86@gmail.com>     2: +22/-3
#[Out]# 14425  054da1e0afbe  Idan Kamara <idankk86@gmail.com>    1: +11/-16
#[Out]# 14424  51cabd567ac6  Idan Kamara <idankk86@gmail.com>      1: +5/-4
#[Out]# 14414  0368ad7963be  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14413  170747a3e139  Idan Kamara <idankk86@gmail.com>     2: +18/-1
#[Out]# 14412  dc961471efde  Idan Kamara <idankk86@gmail.com>     2: +12/-7
#[Out]# 14292  8e00906066c9  Idan Kamara <idankk86@gmail.com>      1: +2/-2
#[Out]# 14291  7352ff757a48  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14282  d04ba50e104d  Idan Kamara <idankk86@gmail.com>    3: +81/-21
#[Out]# 14281  576256a81cb6  Idan Kamara <idankk86@gmail.com>     1: +22/-0
#[Out]# 14267  45f7aa35f2fd  Idan Kamara <idankk86@gmail.com>      1: +6/-5
#[Out]# 14266  28762bb767dc  Idan Kamara <idankk86@gmail.com>      1: +2/-2
#[Out]# 14265  967be4bb42a7  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 14245  8f551386abf0  Idan Kamara <idankk86@gmail.com>      1: +1/-5
#[Out]# 14244  68ade2a6b30a  Idan Kamara <idankk86@gmail.com>     2: +23/-1
#[Out]# 14219  e1c34ce39fae  Idan Kamara <idankk86@gmail.com>      3: +7/-7
#[Out]# 14124  f3d585c9b042  Idan Kamara <idankk86@gmail.com>     1: +8/-20
#[Out]# 14099  643381286e0c  Idan Kamara <idankk86@gmail.com>      1: +1/-0
#[Out]# 14091  3c616f512a5b  Idan Kamara <idankk86@gmail.com>    2: +18/-10
#[Out]# 14078  3fc7154396d2  Idan Kamara <idankk86@gmail.com>      1: +3/-1
#[Out]# 14077  0e6f622f31ca  Idan Kamara <idankk86@gmail.com>     1: +12/-9
#[Out]# 14076  4ab1e987941b  Idan Kamara <idankk86@gmail.com>      1: +2/-2
#[Out]# 14054  64de9ca66511  Idan Kamara <idankk86@gmail.com>     1: +26/-7
#[Out]# 14049  bb391e0515ba  Idan Kamara <idankk86@gmail.com>      1: +1/-0
#[Out]# 14048  97ed99d1f419  Idan Kamara <idankk86@gmail.com>   12: +18/-17
#[Out]# 14009  190e5f2043d9  Idan Kamara <idankk86@gmail.com>      2: +6/-1
#[Out]# 14005  ae10a5e8e558  Idan Kamara <idankk86@gmail.com>    1: +63/-55
#[Out]# 13992  e44ebd2a142a  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 13984  cff56a0ed18e  Idan Kamara <idankk86@gmail.com>     3: +37/-4
#[Out]# 13980  c315ffc13a25  Idan Kamara <idankk86@gmail.com>     2: +10/-0
#[Out]# 13974  67f20625703f  Idan Kamara <idankk86@gmail.com>     1: +11/-9
#[Out]# 13970  8f81d6f4047f  Idan Kamara <idankk86@gmail.com>  1: +365/-365
#[Out]# 13969  27573f2ddfb9  Idan Kamara <idankk86@gmail.com>      1: +5/-2
#[Out]# 13967  6bc340940c18  Idan Kamara <idankk86@gmail.com>     2: +10/-8
#[Out]# 13965  184cf2fa1046  Idan Kamara <idankk86@gmail.com>      1: +1/-4
#[Out]# 13964  ba669bc7f851  Idan Kamara <idankk86@gmail.com>      1: +1/-5
#[Out]# 13954  1aea86673dee  Idan Kamara <idankk86@gmail.com>    1: +10/-13
#[Out]# 13953  31d15f761631  Idan Kamara <idankk86@gmail.com>      1: +6/-1
#[Out]# 13934  e6bd5b403de0  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 13860  bc7b5d1c1999  Idan Kamara <idankk86@gmail.com>      2: +8/-1
#[Out]# 13845  7fc79055a62b  Idan Kamara <idankk86@gmail.com>     4: +0/-10
#[Out]# 13844  8ed67e44c71c  Idan Kamara <idankk86@gmail.com>      1: +3/-1
#[Out]# 13662  e880433a2e00  Idan Kamara <idankk86@gmail.com>     3: +37/-4
#[Out]# 13661  a281981e2033  Idan Kamara <idankk86@gmail.com>      1: +6/-1
#[Out]# 13644  b00ab6890fe9  Idan Kamara <idankk86@gmail.com>      2: +4/-3
#[Out]# 13633  2b1226693c70  Idan Kamara <idankk86@gmail.com>      2: +7/-1
#[Out]# 13618  1416b9118540  Idan Kamara <idankk86@gmail.com>      1: +6/-6
#[Out]# 13616  5f126c01ebfa  Idan Kamara <idankk86@gmail.com>      1: +1/-1
#[Out]# 11551  18c47562d331  Idan Kamara <idankk86@gmail.com>      3: +8/-0), ('Inaky Perez-Gonzalez <inaky.perez-gonzalez@intel.com>',               node                                             author  changestr
#[Out]# n                                                                               
#[Out]# 2763  0eb3a0d1c454  Inaky Perez-Gonzalez <inaky.perez-gonzalez@intel.   1: +3/-1
#[Out]# 2762  2df98f616645  Inaky Perez-Gonzalez <inaky.perez-gonzalez@intel.  1: +16/-5), ('Ingo Bressler <dev@ingobressler.net>',                node                                author changestr
#[Out]# n                                                                  
#[Out]# 14617  23f4e1e40988  Ingo Bressler <dev@ingobressler.net>  2: +9/-3), ('Ingo Proetel <proetel@aicas.de>',                node                           author  changestr
#[Out]# n                                                              
#[Out]# 14597  3f1dccea9510  Ingo Proetel <proetel@aicas.de>  2: +23/-4), ('Ion Savin <comp_@gmx.net>',                node                     author changestr
#[Out]# n                                                       
#[Out]# 15687  e5fd140a4e69  Ion Savin <comp_@gmx.net>  1: +3/-1), ('Ion Savin <ion.savin@tora.com>',                node                          author  changestr
#[Out]# n                                                             
#[Out]# 15835  2c480532f36e  Ion Savin <ion.savin@tora.com>  2: +15/-0), ('Isaac Jurado <diptongo@gmail.com>',                node                             author   changestr
#[Out]# n                                                                 
#[Out]# 11030  a156ce543a5b  Isaac Jurado <diptongo@gmail.com>    1: +1/-1
#[Out]# 10712  ede19417c3c4  Isaac Jurado <diptongo@gmail.com>    1: +1/-1
#[Out]# 8944   dda4ad7c9ea9  Isaac Jurado <diptongo@gmail.com>    1: +9/-9
#[Out]# 6625   938319418d8c  Isaac Jurado <diptongo@gmail.com>  4: +50/-67), ('Jacek Sowi\xc5\x84ski <mruwek.gentoo@vcf.pl>',                node                                 author  changestr
#[Out]# n                                                                    
#[Out]# 13011  0a1eefaf98f2  Jacek Sowiński <mruwek.gentoo@vcf.pl>  1: +1/-1), ('Jacob Lee <artdent@gmail.com>',               node                         author  changestr
#[Out]# n                                                           
#[Out]# 8191  d3fb413667e5  Jacob Lee <artdent@gmail.com>  3: +42/-2), ('James Abbatiello <abbeyj at gmail.com>',               node                                  author changestr
#[Out]# n                                                                   
#[Out]# 9044  705278e70457  James Abbatiello <abbeyj at gmail.com>  3: +3/-2
#[Out]# 9041  395b0e132836  James Abbatiello <abbeyj at gmail.com>  1: +2/-0), ('Jan Sorensen <js@aragost.com>',                node                         author changestr
#[Out]# n                                                           
#[Out]# 11315  666b62c52767  Jan Sorensen <js@aragost.com>  1: +0/-2), ('Jason Harris <jason@jasonfharris.com>',                node                                 author  changestr
#[Out]# n                                                                    
#[Out]# 11848  83eb6b1465bf  Jason Harris <jason@jasonfharris.com>  2: +10/-0
#[Out]# 11847  6faf015e0ba0  Jason Harris <jason@jasonfharris.com>   2: +8/-0), ('Jason Orendorff <jorendorff@mozilla.com>',               node                                    author    changestr
#[Out]# n                                                                        
#[Out]# 7508  12df451ce205  Jason Orendorff <jorendorff@mozilla.com>    3: +46/-8
#[Out]# 6752  034f444902d9  Jason Orendorff <jorendorff@mozilla.com>  5: +120/-28
#[Out]# 6448  c242fc76958e  Jason Orendorff <jorendorff@mozilla.com>     1: +2/-0), ('Javi Merino <cibervicho@gmail.com>',                node                              author changestr
#[Out]# n                                                                
#[Out]# 16194  825565136235  Javi Merino <cibervicho@gmail.com>  1: +4/-0
#[Out]# 16146  0628290d98df  Javi Merino <cibervicho@gmail.com>  1: +1/-3
#[Out]# 16136  d4d35fd0889d  Javi Merino <cibervicho@gmail.com>  1: +1/-1
#[Out]# 16133  7cf8de5a82d8  Javi Merino <cibervicho@gmail.com>  1: +1/-1
#[Out]# 14351  d943412e2fba  Javi Merino <cibervicho@gmail.com>  2: +3/-3
#[Out]# 13380  d11405848abd  Javi Merino <cibervicho@gmail.com>  1: +3/-3
#[Out]# 13346  b8214d871338  Javi Merino <cibervicho@gmail.com>  1: +1/-1
#[Out]# 13345  6367459decf7  Javi Merino <cibervicho@gmail.com>  1: +3/-3
#[Out]# 13035  551856dea9a6  Javi Merino <cibervicho@gmail.com>  1: +1/-1
#[Out]# 11435  7c58cde598fe  Javi Merino <cibervicho@gmail.com>  1: +9/-2
#[Out]# 11269  2b440bb8a66b  Javi Merino <cibervicho@gmail.com>  1: +4/-4
#[Out]# 11215  43337076ba92  Javi Merino <cibervicho@gmail.com>  1: +1/-1), ('Jean-Francois PIERONNE <jf.pieronne@laposte.net>',               node                                            author  changestr
#[Out]# n                                                                              
#[Out]# 4720  72fb6f10fac1  Jean-Francois PIERONNE <jf.pieronne@laposte.net>  1: +19/-6), ('Jeff Schiller <codedread@gmail.com>',                node                               author   changestr
#[Out]# n                                                                   
#[Out]# 10959  6514935e223d  Jeff Schiller <codedread@gmail.com>  1: +3/-622), ('Jeff Sipek <jeffpc@optonline.net>',              node                             author   changestr
#[Out]# n                                                               
#[Out]# 858  c333dfa8fa1a  Jeff Sipek <jeffpc@optonline.net>    2: +5/-1
#[Out]# 857  41b344235bb7  Jeff Sipek <jeffpc@optonline.net>  1: +18/-18), ('Jeff Walden <jwalden@mit.edu>',               node                         author changestr
#[Out]# n                                                          
#[Out]# 6453  ff5ef3c0fe10  Jeff Walden <jwalden@mit.edu>  1: +1/-1), ('Jens B\xc3\xa4ckman <jens.backman@gmail.com>',                node                                 author        changestr
#[Out]# n                                                                          
#[Out]# 16035  b2392a395fcf  Jens Bäckman <jens.backman@gmail.com>      1: +191/-9
#[Out]# 15985  740b1b4c7958  Jens Bäckman <jens.backman@gmail.com>        1: +6/-2
#[Out]# 15980  cc7693768c83  Jens Bäckman <jens.backman@gmail.com>        1: +8/-3
#[Out]# 15979  2be0253f6249  Jens Bäckman <jens.backman@gmail.com>      1: +29/-29
#[Out]# 15978  ec6ac46f6127  Jens Bäckman <jens.backman@gmail.com>      1: +50/-39
#[Out]# 15973  c6464e943a9a  Jens Bäckman <jens.backman@gmail.com>   1: +1999/-584
#[Out]# 14846  4fdab926e111  Jens Bäckman <jens.backman@gmail.com>     1: +271/-37
#[Out]# 14785  06189ef78d2d  Jens Bäckman <jens.backman@gmail.com>      1: +76/-17
#[Out]# 13496  017f509c973c  Jens Bäckman <jens.backman@gmail.com>      1: +87/-27
#[Out]# 13495  cf9303aa3bc2  Jens Bäckman <jens.backman@gmail.com>    1: +703/-434
#[Out]# 13007  4a39a6afc892  Jens Bäckman <jens.backman@gmail.com>     1: +119/-43
#[Out]# 12904  b6fd8157515b  Jens Bäckman <jens.backman@gmail.com>    1: +629/-345
#[Out]# 12832  64f5ae917020  Jens Bäckman <jens.backman@gmail.com>  1: +1930/-1284
#[Out]# 11573  5491c9644388  Jens Bäckman <jens.backman@gmail.com>       1: +24/-8
#[Out]# 11479  6e8cf1024497  Jens Bäckman <jens.backman@gmail.com>     1: +100/-21
#[Out]# 11475  bb28125acddc  Jens Bäckman <jens.backman@gmail.com>       1: +16/-5
#[Out]# 11474  56186ab6a2da  Jens Bäckman <jens.backman@gmail.com>      1: +21/-18
#[Out]# 11471  4da206812ce7  Jens Bäckman <jens.backman@gmail.com>  1: +3344/-2137
#[Out]# 11091  e21fcbbfa27e  Jens Bäckman <jens.backman@gmail.com>    1: +132/-103
#[Out]# 11090  5172261b92af  Jens Bäckman <jens.backman@gmail.com>      1: +56/-41
#[Out]# 10729  8227a631c6b4  Jens Bäckman <jens.backman@gmail.com>      1: +34/-32
#[Out]# 10728  af4fe14a6f7d  Jens Bäckman <jens.backman@gmail.com>      1: +23/-10
#[Out]# 10656  f58d5fbd941c  Jens Bäckman <jens.backman@gmail.com>       1: +49/-8
#[Out]# 10653  e703af672d9d  Jens Bäckman <jens.backman@gmail.com>    1: +243/-114
#[Out]# 10583  24a6da583b71  Jens Bäckman <jens.backman@gmail.com>     1: +105/-22
#[Out]# 10568  c4b321baf4a4  Jens Bäckman <jens.backman@gmail.com>      1: +64/-53
#[Out]# 10561  90414215041f  Jens Bäckman <jens.backman@gmail.com>        1: +7/-7
#[Out]# 10548  167030b1757b  Jens Bäckman <jens.backman@gmail.com>      1: +93/-12
#[Out]# 10487  93b5a957294c  Jens Bäckman <jens.backman@gmail.com>      1: +67/-18
#[Out]# 10459  c14530294269  Jens Bäckman <jens.backman@gmail.com>    1: +683/-424
#[Out]# 10307  caeb7163492e  Jens Bäckman <jens.backman@gmail.com>     1: +292/-72
#[Out]# 10264  192c39586787  Jens Bäckman <jens.backman@gmail.com>        1: +1/-1
#[Out]# 10223  23409637fedd  Jens Bäckman <jens.backman@gmail.com>    1: +757/-642
#[Out]# 10029  f1ee8009fe10  Jens Bäckman <jens.backman@gmail.com>     1: +149/-39
#[Out]# 10028  0ebef7e813df  Jens Bäckman <jens.backman@gmail.com>    1: +162/-144
#[Out]# 9964   712dc3b6db68  Jens Bäckman <jens.backman@gmail.com>        1: +1/-1
#[Out]# 9845   22dae78227f5  Jens Bäckman <jens.backman@gmail.com>    1: +304/-119
#[Out]# 9776   f1ed441ab8e9  Jens Bäckman <jens.backman@gmail.com>      1: +71/-64
#[Out]# 9568   6aece8fc7f3c  Jens Bäckman <jens.backman@gmail.com>     1: +9006/-0), ('Jens B\xc3\xa4ckman <jens@titv.se>',                node                       author        changestr
#[Out]# n                                                                
#[Out]# 14767  5435b84c6df6  Jens Bäckman <jens@titv.se>  1: +5469/-2890
#[Out]# 11564  a34aad272014  Jens Bäckman <jens@titv.se>    1: +198/-144), ('Jeremy Whitlock <jcscoobyrs@gmail.com>',                node                                  author   changestr
#[Out]# n                                                                      
#[Out]# 12088  52ec5c813723  Jeremy Whitlock <jcscoobyrs@gmail.com>   3: +67/-2
#[Out]# 8552   3ccbe42ff72f  Jeremy Whitlock <jcscoobyrs@gmail.com>   1: +14/-6
#[Out]# 8534   a767998f0a78  Jeremy Whitlock <jcscoobyrs@gmail.com>  2: +71/-30
#[Out]# 8004   73fa2be69ea9  Jeremy Whitlock <jcscoobyrs@gmail.com>  1: +13/-13
#[Out]# 7900   4c030ada58d2  Jeremy Whitlock <jcscoobyrs@gmail.com>  1: +13/-13), ('Jesse Glick <jesse.glick@oracle.com>',                node                                author changestr
#[Out]# n                                                                  
#[Out]# 16600  00290bd359fe  Jesse Glick <jesse.glick@oracle.com>  1: +1/-1), ('Jesse Glick <jesse.glick@sun.com>',               node                             author     changestr
#[Out]# n                                                                  
#[Out]# 9749  1b1b33ae5a24  Jesse Glick <jesse.glick@sun.com>      1: +2/-2
#[Out]# 9748  67e5d5a2f625  Jesse Glick <jesse.glick@sun.com>      1: +3/-2
#[Out]# 9729  aa9ccab5af37  Jesse Glick <jesse.glick@sun.com>  2: +149/-128
#[Out]# 6265  be76e54570f0  Jesse Glick <jesse.glick@sun.com>      1: +3/-3
#[Out]# 6204  f8a86ea7521b  Jesse Glick <jesse.glick@sun.com>     3: +11/-4
#[Out]# 6174  434139080ed4  Jesse Glick <jesse.glick@sun.com>     3: +19/-0
#[Out]# 6150  aafdea37f796  Jesse Glick <jesse.glick@sun.com>     3: +20/-3
#[Out]# 6096  f5b00b6e426a  Jesse Glick <jesse.glick@sun.com>     6: +21/-1
#[Out]# 6072  f3a8b5360100  Jesse Glick <jesse.glick@sun.com>     3: +74/-1
#[Out]# 5995  f8ad3b76e923  Jesse Glick <jesse.glick@sun.com>    4: +75/-14
#[Out]# 5981  e7f1be4bf40a  Jesse Glick <jesse.glick@sun.com>     3: +35/-3
#[Out]# 5977  48d01b1e315f  Jesse Glick <jesse.glick@sun.com>      3: +9/-3
#[Out]# 5971  ffaf2419de44  Jesse Glick <jesse.glick@sun.com>     4: +19/-2
#[Out]# 5880  2580d418e3f0  Jesse Glick <jesse.glick@sun.com>      3: +3/-3
#[Out]# 5727  1d8ef9fb3e88  Jesse Glick <jesse.glick@sun.com>      1: +1/-1
#[Out]# 5726  d3909674fcea  Jesse Glick <jesse.glick@sun.com>    1: +15/-10
#[Out]# 5723  a5fe27b83a4a  Jesse Glick <jesse.glick@sun.com>    3: +269/-0
#[Out]# 5015  001e8a745834  Jesse Glick <jesse.glick@sun.com>      1: +1/-1), ('Jesse Long <jesse@virtualpostman.co.za>',               node                                   author   changestr
#[Out]# n                                                                      
#[Out]# 7421  196b05a548d0  Jesse Long <jesse@virtualpostman.co.za>  1: +15/-14), ('Jesse Long <jpl@unknown.za.net>',                node                           author changestr
#[Out]# n                                                             
#[Out]# 14761  0cc66f13bea0  Jesse Long <jpl@unknown.za.net>  1: +3/-3), ('Jesus Espino Garcia <jesus.espino@kaleidos.net>',                node                                           author changestr
#[Out]# n                                                                             
#[Out]# 15971  089ee59a8658  Jesus Espino Garcia <jesus.espino@kaleidos.net>  1: +2/-2
#[Out]# 15970  9f2ed48f8cda  Jesus Espino Garcia <jesus.espino@kaleidos.net>  1: +2/-0
#[Out]# 15969  80f3ae36f908  Jesus Espino Garcia <jesus.espino@kaleidos.net>  1: +1/-0), ('Jim Correia <jim.correia@pobox.com>',               node                               author    changestr
#[Out]# n                                                                   
#[Out]# 7764  cdc913e7fc5f  Jim Correia <jim.correia@pobox.com>     2: +3/-3
#[Out]# 7763  fece056bf240  Jim Correia <jim.correia@pobox.com>  11: +57/-11
#[Out]# 7731  5fb312ba29a8  Jim Correia <jim.correia@pobox.com>     1: +2/-1), ('Jim Hague <jim.hague@acm.org>',                node                         author    changestr
#[Out]# n                                                              
#[Out]# 16645  fdc879042414  Jim Hague <jim.hague@acm.org>     1: +3/-2
#[Out]# 16304  d52a6b542db1  Jim Hague <jim.hague@acm.org>    1: +20/-1
#[Out]# 16303  ac4fd3238ead  Jim Hague <jim.hague@acm.org>   1: +80/-12
#[Out]# 16302  d7b7b453c035  Jim Hague <jim.hague@acm.org>   1: +50/-14
#[Out]# 16301  4fc9fcd991c1  Jim Hague <jim.hague@acm.org>   1: +68/-55
#[Out]# 16203  f64b25f147d7  Jim Hague <jim.hague@acm.org>     3: +4/-2
#[Out]# 16134  674ecd23c42c  Jim Hague <jim.hague@acm.org>     1: +1/-1
#[Out]# 16112  b468cea3f29d  Jim Hague <jim.hague@acm.org>     1: +1/-0
#[Out]# 16071  c6c9b83a1e8a  Jim Hague <jim.hague@acm.org>     5: +8/-8
#[Out]# 16062  8134ec8627e7  Jim Hague <jim.hague@acm.org>     1: +1/-1
#[Out]# 16060  f680ed10e2c4  Jim Hague <jim.hague@acm.org>     1: +3/-3
#[Out]# 15524  f4c859293ed4  Jim Hague <jim.hague@acm.org>    1: +25/-8
#[Out]# 14805  0407b7613e99  Jim Hague <jim.hague@acm.org>   3: +27/-26
#[Out]# 13955  3b4025dcb223  Jim Hague <jim.hague@acm.org>     1: +3/-3
#[Out]# 13933  22d200e49b10  Jim Hague <jim.hague@acm.org>     1: +5/-4
#[Out]# 13932  ce066d424bba  Jim Hague <jim.hague@acm.org>   1: +26/-12
#[Out]# 13880  49b5a1aaf726  Jim Hague <jim.hague@acm.org>  1: +114/-20
#[Out]# 13879  60256f7f30c1  Jim Hague <jim.hague@acm.org>  1: +224/-59
#[Out]# 13878  c2ef8159dabe  Jim Hague <jim.hague@acm.org>   1: +74/-38
#[Out]# 13877  d04fc5582772  Jim Hague <jim.hague@acm.org>    1: +10/-9
#[Out]# 13876  9c9fa78f4e2d  Jim Hague <jim.hague@acm.org>     1: +2/-2
#[Out]# 13459  acbe171c8fbe  Jim Hague <jim.hague@acm.org>     1: +1/-1
#[Out]# 13246  684a977c2ae0  Jim Hague <jim.hague@acm.org>     2: +6/-2
#[Out]# 9973   b190a8125b43  Jim Hague <jim.hague@acm.org>     2: +2/-2
#[Out]# 7627   6c89dd0a7797  Jim Hague <jim.hague@acm.org>   1: +45/-16
#[Out]# 7552   d8cd79fbed3c  Jim Hague <jim.hague@acm.org>  1: +101/-47
#[Out]# 7546   518afef5e350  Jim Hague <jim.hague@acm.org>     1: +1/-0
#[Out]# 7477   0d488f7f321d  Jim Hague <jim.hague@acm.org>     1: +5/-1
#[Out]# 7044   6b1ece890f9a  Jim Hague <jim.hague@acm.org>    1: +24/-5
#[Out]# 5633   f84bb2e1cc3a  Jim Hague <jim.hague@acm.org>     1: +1/-1
#[Out]# 5509   5133e9f61700  Jim Hague <jim.hague@acm.org>     1: +1/-1
#[Out]# 5503   777996744942  Jim Hague <jim.hague@acm.org>     1: +1/-1
#[Out]# 5471   5b81c1cc6ebe  Jim Hague <jim.hague@acm.org>     1: +2/-2), ('Jim Meyering <list+hg@meyering.net>',               node                               author  changestr
#[Out]# n                                                                 
#[Out]# 2115  fd77b7ee4aac  Jim Meyering <list+hg@meyering.net>  3: +43/-0), ('Joel Rosdahl <joel@rosdahl.net>',                node                           author    changestr
#[Out]# n                                                                
#[Out]# 11529  efbc09fdefd8  Joel Rosdahl <joel@rosdahl.net>    2: +61/-0
#[Out]# 9728   acb1c59b4514  Joel Rosdahl <joel@rosdahl.net>     2: +9/-0
#[Out]# 7262   4ba89b6d0e05  Joel Rosdahl <joel@rosdahl.net>   2: +169/-0
#[Out]# 7261   eb91b9ce2c19  Joel Rosdahl <joel@rosdahl.net>     1: +1/-0
#[Out]# 7260   18c23375861f  Joel Rosdahl <joel@rosdahl.net>     1: +2/-2
#[Out]# 7259   9bd051efbdd6  Joel Rosdahl <joel@rosdahl.net>     1: +2/-0
#[Out]# 7258   7fb0e130cf14  Joel Rosdahl <joel@rosdahl.net>     1: +4/-4
#[Out]# 7257   df800e004077  Joel Rosdahl <joel@rosdahl.net>     1: +3/-1
#[Out]# 7256   69e431ea124d  Joel Rosdahl <joel@rosdahl.net>     1: +6/-6
#[Out]# 7255   d892211d670e  Joel Rosdahl <joel@rosdahl.net>     1: +2/-0
#[Out]# 7254   8b81d1e2dc04  Joel Rosdahl <joel@rosdahl.net>     1: +2/-1
#[Out]# 7253   104a8324798e  Joel Rosdahl <joel@rosdahl.net>   1: +21/-17
#[Out]# 7252   444d88175e33  Joel Rosdahl <joel@rosdahl.net>     1: +4/-4
#[Out]# 7251   352627bcafc3  Joel Rosdahl <joel@rosdahl.net>   1: +10/-10
#[Out]# 6217   fe8dbbe9520d  Joel Rosdahl <joel@rosdahl.net>  11: +63/-54
#[Out]# 6216   a88259018f79  Joel Rosdahl <joel@rosdahl.net>     1: +1/-1
#[Out]# 6215   cb0434795fcd  Joel Rosdahl <joel@rosdahl.net>     1: +0/-7
#[Out]# 6214   0f76c7dc8484  Joel Rosdahl <joel@rosdahl.net>     1: +1/-2
#[Out]# 6213   5c5e45766224  Joel Rosdahl <joel@rosdahl.net>    3: +11/-3
#[Out]# 6212   e75aab656f46  Joel Rosdahl <joel@rosdahl.net>  40: +31/-52
#[Out]# 6211   f89fd07fc51d  Joel Rosdahl <joel@rosdahl.net>  33: +38/-36
#[Out]# 5964   00dfc810dae4  Joel Rosdahl <joel@rosdahl.net>     1: +8/-6
#[Out]# 4514   0ca5ef554987  Joel Rosdahl <joel@rosdahl.net>     1: +3/-3
#[Out]# 4513   c68e6486f295  Joel Rosdahl <joel@rosdahl.net>    2: +15/-0
#[Out]# 4428   f4af7960d578  Joel Rosdahl <joel@rosdahl.net>     1: +1/-1
#[Out]# 4401   345ed833854d  Joel Rosdahl <joel@rosdahl.net>   4: +720/-0), ('Johan Euphrosine <proppy@google.com>',                node                                author changestr
#[Out]# n                                                                  
#[Out]# 14201  1a919c3271bf  Johan Euphrosine <proppy@google.com>  1: +2/-0), ('Johan Samyn <johan.samyn@gmail.com>',                node                               author changestr
#[Out]# n                                                                 
#[Out]# 16140  3d26d69ef822  Johan Samyn <johan.samyn@gmail.com>  1: +1/-1
#[Out]# 9940   daec0f64656e  Johan Samyn <johan.samyn@gmail.com>  1: +1/-1), ('Johannes Stezenbach <js@linuxtv.org>',               node                                author  changestr
#[Out]# n                                                                  
#[Out]# 1705  4b5725a4a0a6  Johannes Stezenbach <js@linuxtv.org>   1: +4/-0
#[Out]# 1704  c2755eba8631  Johannes Stezenbach <js@linuxtv.org>   1: +1/-1
#[Out]# 1703  41d884f741ca  Johannes Stezenbach <js@linuxtv.org>  1: +12/-6
#[Out]# 1702  e291d9a30bef  Johannes Stezenbach <js@linuxtv.org>  1: +19/-3), ('Johannes Stezenbach <js@sig21.net>',               node                              author   changestr
#[Out]# n                                                                 
#[Out]# 6740  ab798a37b846  Johannes Stezenbach <js@sig21.net>  3: +54/-50
#[Out]# 6739  2713e42dcf4e  Johannes Stezenbach <js@sig21.net>  3: +56/-57
#[Out]# 6738  a78d8edaeedd  Johannes Stezenbach <js@sig21.net>   2: +15/-0
#[Out]# 6737  ffcf8e82f647  Johannes Stezenbach <js@sig21.net>    1: +8/-1), ('John Arbash Meinel <john@arbash-meinel.com>',               node                                       author changestr
#[Out]# n                                                                        
#[Out]# 2310  d01eac5968c6  John Arbash Meinel <john@arbash-meinel.com>  1: +4/-0), ('John Coomes <john.coomes@oracle.com>',                node                                author   changestr
#[Out]# n                                                                    
#[Out]# 13266  c046978cc0a9  John Coomes <john.coomes@oracle.com>  1: +117/-0), ('John Coomes <john.coomes@sun.com>',               node                             author   changestr
#[Out]# n                                                                
#[Out]# 7951  490e40816cbd  John Coomes <john.coomes@sun.com>  6: +11/-11
#[Out]# 6321  55ba3bc5b8fd  John Coomes <john.coomes@sun.com>  7: +92/-53
#[Out]# 5795  f75ca1b0c81e  John Coomes <john.coomes@sun.com>    2: +1/-2
#[Out]# 5524  1b230f506346  John Coomes <john.coomes@sun.com>    2: +1/-2), ('John Goerzen <jgoerzen@complete.org>',               node                                author   changestr
#[Out]# n                                                                   
#[Out]# 4366  a04141f51056  John Goerzen <jgoerzen@complete.org>    1: +2/-0
#[Out]# 4365  8625504f507c  John Goerzen <jgoerzen@complete.org>    1: +5/-4
#[Out]# 4362  a9336520a4ee  John Goerzen <jgoerzen@complete.org>   1: +26/-2
#[Out]# 4361  126d1967a3f8  John Goerzen <jgoerzen@complete.org>   1: +10/-4
#[Out]# 4360  cfe886c14ddf  John Goerzen <jgoerzen@complete.org>  1: +90/-48), ('John Mulligan <phlogistonjohn@asynchrono.us>',                node                                        author   changestr
#[Out]# n                                                                            
#[Out]# 13972  3259a067c102  John Mulligan <phlogistonjohn@asynchrono.us>  1: +560/-0
#[Out]# 8796   2bcef677a6c3  John Mulligan <phlogistonjohn@asynchrono.us>  6: +87/-28
#[Out]# 8698   9a89253a32e6  John Mulligan <phlogistonjohn@asynchrono.us>   3: +11/-4
#[Out]# 8697   ca8d05e1f1d1  John Mulligan <phlogistonjohn@asynchrono.us>   3: +70/-2
#[Out]# 7937   5ac1a72e5b74  John Mulligan <phlogistonjohn@asynchrono.us>    1: +4/-1
#[Out]# 7730   dd08e1e0cea1  John Mulligan <phlogistonjohn@asynchrono.us>    1: +4/-1
#[Out]# 7729   b7ac53f7b061  John Mulligan <phlogistonjohn@asynchrono.us>    1: +0/-2
#[Out]# 7665   405cacb06745  John Mulligan <phlogistonjohn@asynchrono.us>  3: +134/-7
#[Out]# 7664   6a24fb994701  John Mulligan <phlogistonjohn@asynchrono.us>  2: +40/-10
#[Out]# 7663   cce37dab7ad6  John Mulligan <phlogistonjohn@asynchrono.us>   2: +12/-2
#[Out]# 7662   816b708f23af  John Mulligan <phlogistonjohn@asynchrono.us>  5: +34/-52
#[Out]# 7149   8d1bdaf842de  John Mulligan <phlogistonjohn@asynchrono.us>   3: +22/-0
#[Out]# 6316   ad5baedeee02  John Mulligan <phlogistonjohn@asynchrono.us>   2: +24/-0
#[Out]# 6314   9a1c59283ad3  John Mulligan <phlogistonjohn@asynchrono.us>   1: +11/-3
#[Out]# 6311   a079cf630065  John Mulligan <phlogistonjohn@asynchrono.us>    1: +7/-0), ('John Mulligan <phlogistonjohn@yahoo.com>',               node                                    author  changestr
#[Out]# n                                                                      
#[Out]# 6171  73b1de288801  John Mulligan <phlogistonjohn@yahoo.com>  3: +15/-5), ('John Peberdy <john@peberdy.ca>',                node                          author changestr
#[Out]# n                                                            
#[Out]# 13000  aa72ff5abf5f  John Peberdy <john@peberdy.ca>  1: +3/-2), ('Jon M. Dugan <jdugan@x1024.net>',                node                           author changestr
#[Out]# n                                                             
#[Out]# 13560  4bfff063aed6  Jon M. Dugan <jdugan@x1024.net>  1: +7/-3), ('Jonas Diemer <diemer@gmx.de>',               node                        author changestr
#[Out]# n                                                         
#[Out]# 6232  59200a2de7bf  Jonas Diemer <diemer@gmx.de>  1: +1/-0), ('Jonathan Kotta <jpkotta@packetdigital.com>',               node                                      author changestr
#[Out]# n                                                                       
#[Out]# 8381  45ed015b524e  Jonathan Kotta <jpkotta@packetdigital.com>  1: +2/-1), ('Jonathan Nieder <jrnieder@gmail.com>',                node                                author   changestr
#[Out]# n                                                                    
#[Out]# 13473  bbdd858e3229  Jonathan Nieder <jrnieder@gmail.com>    1: +4/-4
#[Out]# 13046  02aa06a021a0  Jonathan Nieder <jrnieder@gmail.com>  1: +16/-20), ('Jonathan Smith <https://issues.rpath.com/>',               node                                      author changestr
#[Out]# n                                                                       
#[Out]# 4206  c9160748c094  Jonathan Smith <https://issues.rpath.com/>  1: +1/-1
#[Out]# 4205  15b2528239e4  Jonathan Smith <https://issues.rpath.com/>  1: +1/-1
#[Out]# 4204  a48971ae1387  Jonathan Smith <https://issues.rpath.com/>  1: +1/-1), ('Jordi Guti\xc3\xa9rrez Hermoso <jordigh@octave.org>',                node                                        author   changestr
#[Out]# n                                                                            
#[Out]# 15894  44fa047cef57  Jordi Gutiérrez Hermoso <jordigh@octave.org>  3: +11/-4
#[Out]# 15158  510184e5a09e  Jordi Gutiérrez Hermoso <jordigh@octave.org>   1: +6/-1), ('Jose M. Prieto <jmprieto@gmx.net>',               node                             author  changestr
#[Out]# n                                                               
#[Out]# 3252  c9cd63a6fce9  Jose M. Prieto <jmprieto@gmx.net>  4: +43/-5
#[Out]# 3251  e5c9a084ffe3  Jose M. Prieto <jmprieto@gmx.net>  3: +13/-7
#[Out]# 3250  e96d2956eb4a  Jose M. Prieto <jmprieto@gmx.net>  3: +27/-3
#[Out]# 2522  85f796baab10  Jose M. Prieto <jmprieto@gmx.net>  4: +62/-6), ('Josef "Jeff" Sipek <jeff@josefsipek.net>',               node                                    author   changestr
#[Out]# n                                                                       
#[Out]# 3043  2a4d4aecb2b4  Josef "Jeff" Sipek <jeff@josefsipek.net>    1: +1/-1
#[Out]# 3041  a10adb6a9c9c  Josef "Jeff" Sipek <jeff@josefsipek.net>    1: +1/-1
#[Out]# 3037  f74077473b36  Josef "Jeff" Sipek <jeff@josefsipek.net>  1: +161/-0), ('Josef "Jeff" Sipek <jeffpc@josefsipek.net>',               node                                      author         changestr
#[Out]# n                                                                               
#[Out]# 4547  4272ae760bb1  Josef "Jeff" Sipek <jeffpc@josefsipek.net>        6: +49/-13
#[Out]# 4488  8af65bc092b0  Josef "Jeff" Sipek <jeffpc@josefsipek.net>        2: +22/-16
#[Out]# 4487  d189b19936ec  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +8/-0
#[Out]# 4486  faf2fa0f3fff  Josef "Jeff" Sipek <jeffpc@josefsipek.net>         2: +7/-12
#[Out]# 4485  0ed59f0076e0  Josef "Jeff" Sipek <jeffpc@josefsipek.net>        2: +13/-16
#[Out]# 4484  e8da331a860f  Josef "Jeff" Sipek <jeffpc@josefsipek.net>        2: +13/-16
#[Out]# 4483  3f444b82df9e  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +0/-1
#[Out]# 4480  3e679426dd7f  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +4/-0
#[Out]# 4479  717b96751431  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +4/-0
#[Out]# 4478  2ee0e935f86d  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +2/-3
#[Out]# 4477  e19d9b1223ee  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          3: +3/-2
#[Out]# 4476  7b2e808984e0  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +1/-1
#[Out]# 4475  907dd9157ccb  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +1/-0
#[Out]# 4474  1cddffbbc61a  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +1/-1
#[Out]# 4473  28778dc77a4b  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +2/-2
#[Out]# 4472  862dc0c020ad  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +1/-1
#[Out]# 4471  94a167c3c116  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +2/-2
#[Out]# 3291  0b5d626b354e  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +8/-3
#[Out]# 3049  51083c31db04  Josef "Jeff" Sipek <jeffpc@josefsipek.net>      2: +179/-179
#[Out]# 3048  7ffaf5aba4d8  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +2/-1
#[Out]# 3047  dd1a142988d3  Josef "Jeff" Sipek <jeffpc@josefsipek.net>         1: +20/-6
#[Out]# 3046  461573aa02ef  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +5/-1
#[Out]# 3045  8d344bc72e68  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +1/-1
#[Out]# 3044  fcadf7a32425  Josef "Jeff" Sipek <jeffpc@josefsipek.net>  151: +6043/-2449
#[Out]# 3040  fe0e3508ec6e  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +1/-1
#[Out]# 3039  2d35d7c6f251  Josef "Jeff" Sipek <jeffpc@josefsipek.net>         1: +7/-11
#[Out]# 3038  45942bb49194  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +4/-5
#[Out]# 2893  2497fa1c6b76  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          1: +3/-2
#[Out]# 2687  46b19175fec6  Josef "Jeff" Sipek <jeffpc@josefsipek.net>        10: +10/-0
#[Out]# 2686  d98eebc48d5e  Josef "Jeff" Sipek <jeffpc@josefsipek.net>         4: +53/-0
#[Out]# 2684  783220e5d2d1  Josef "Jeff" Sipek <jeffpc@josefsipek.net>       12: +53/-19
#[Out]# 2683  8a798185809d  Josef "Jeff" Sipek <jeffpc@josefsipek.net>          4: +7/-4), ('Josef "Jeff" Sipek <jeffpc@optonline.net>',               node                                     author      changestr
#[Out]# n                                                                           
#[Out]# 1790  88f0345d82e9  Josef "Jeff" Sipek <jeffpc@optonline.net>       3: +2/-0
#[Out]# 1779  a1e6e02e9d05  Josef "Jeff" Sipek <jeffpc@optonline.net>  17: +533/-121
#[Out]# 1778  b08b87cecc37  Josef "Jeff" Sipek <jeffpc@optonline.net>   4: +120/-123
#[Out]# 1777  a2316878f19d  Josef "Jeff" Sipek <jeffpc@optonline.net>      2: +38/-1
#[Out]# 1776  686bf56c17d0  Josef "Jeff" Sipek <jeffpc@optonline.net>      1: +12/-2
#[Out]# 1668  586b50294ea8  Josef "Jeff" Sipek <jeffpc@optonline.net>       4: +7/-4
#[Out]# 1579  85803ec2daab  Josef "Jeff" Sipek <jeffpc@optonline.net>     1: +12/-12
#[Out]# 1578  4a14edbda3ca  Josef "Jeff" Sipek <jeffpc@optonline.net>       1: +0/-1
#[Out]# 1577  4b0f6a9a6dd4  Josef "Jeff" Sipek <jeffpc@optonline.net>       1: +1/-1
#[Out]# 1576  145cc9f68c05  Josef "Jeff" Sipek <jeffpc@optonline.net>      2: +17/-5
#[Out]# 1575  0a1cca912fda  Josef "Jeff" Sipek <jeffpc@optonline.net>     5: +31/-11
#[Out]# 1574  32b091ce4026  Josef "Jeff" Sipek <jeffpc@optonline.net>       3: +3/-2
#[Out]# 1573  28305666f4c9  Josef "Jeff" Sipek <jeffpc@optonline.net>       3: +8/-9
#[Out]# 1572  385b8872b8e3  Josef "Jeff" Sipek <jeffpc@optonline.net>    16: +470/-0
#[Out]# 980   5197fb9d65d5  Josef "Jeff" Sipek <jeffpc@optonline.net>       3: +7/-4
#[Out]# 979   87d40e085e08  Josef "Jeff" Sipek <jeffpc@optonline.net>     2: +28/-15
#[Out]# 978   ea67e5b37043  Josef "Jeff" Sipek <jeffpc@optonline.net>     2: +11/-12
#[Out]# 977   289975641886  Josef "Jeff" Sipek <jeffpc@optonline.net>       2: +7/-8
#[Out]# 976   5d5ab159d197  Josef "Jeff" Sipek <jeffpc@optonline.net>       2: +4/-4
#[Out]# 975   bdd7c53fca00  Josef "Jeff" Sipek <jeffpc@optonline.net>     2: +18/-19
#[Out]# 974   aedb47764f29  Josef "Jeff" Sipek <jeffpc@optonline.net>     2: +35/-25), ('Juan Pablo Aroztegi <juanpablo.aroztegi@openbravo.com>',                node                                             author  changestr
#[Out]# n                                                                                
#[Out]# 12597  19dabc8a3236  Juan Pablo Aroztegi <juanpablo.aroztegi@openbravo  1: +25/-0), ('Julian Cowley <julian@lava.net>',                node                           author changestr
#[Out]# n                                                             
#[Out]# 11500  488a80c840ac  Julian Cowley <julian@lava.net>  1: +1/-1
#[Out]# 11450  6bca9801c92a  Julian Cowley <julian@lava.net>  1: +1/-1
#[Out]# 11449  05af334bac05  Julian Cowley <julian@lava.net>  1: +1/-1
#[Out]# 11446  0f623839a5cc  Julian Cowley <julian@lava.net>  1: +0/-1
#[Out]# 11332  716e176a4e01  Julian Cowley <julian@lava.net>  1: +3/-1), ('Julien Cristau <julien.cristau@logilab.fr>',                node                                      author changestr
#[Out]# n                                                                        
#[Out]# 16205  8614f8e0dd7a  Julien Cristau <julien.cristau@logilab.fr>  1: +1/-0), ('Jun Inoue <jun.lambda@gmail.com>',               node                            author  changestr
#[Out]# n                                                              
#[Out]# 3941  cc8a52229620  Jun Inoue <jun.lambda@gmail.com>  3: +13/-0), ('Justin Peng <justin.peng.sw@gmail.com>',               node                                  author   changestr
#[Out]# n                                                                     
#[Out]# 7999  8c6f823efcc9  Justin Peng <justin.peng.sw@gmail.com>  3: +147/-0), ('Kevin Berridge <kevin.w.berridge@gmail.com>',                node                                       author  changestr
#[Out]# n                                                                          
#[Out]# 13882  7dc2bd4c0dc8  Kevin Berridge <kevin.w.berridge@gmail.com>  2: +53/-3
#[Out]# 13881  e380964d53f8  Kevin Berridge <kevin.w.berridge@gmail.com>  2: +31/-1), ('Kevin Bullock <kbullock@ringworld.org>',                node                                  author    changestr
#[Out]# n                                                                       
#[Out]# 16646  6e578e77cbe6  Kevin Bullock <kbullock@ringworld.org>     1: +4/-4
#[Out]# 16485  83622954b64d  Kevin Bullock <kbullock@ringworld.org>     1: +3/-4
#[Out]# 16204  c14898df3b92  Kevin Bullock <kbullock@ringworld.org>     1: +1/-1
#[Out]# 16152  6b16ded5c810  Kevin Bullock <kbullock@ringworld.org>    3: +13/-2
#[Out]# 16013  c7811ca6fb94  Kevin Bullock <kbullock@ringworld.org>     2: +3/-1
#[Out]# 15957  12a1c9e92d66  Kevin Bullock <kbullock@ringworld.org>     1: +2/-1
#[Out]# 15939  f57f891eb88e  Kevin Bullock <kbullock@ringworld.org>     1: +5/-0
#[Out]# 15676  013688350c7d  Kevin Bullock <kbullock@ringworld.org>     1: +3/-2
#[Out]# 15675  73faa2664909  Kevin Bullock <kbullock@ringworld.org>     1: +4/-4
#[Out]# 15674  6c8573dd1b6b  Kevin Bullock <kbullock@ringworld.org>   6: +21/-14
#[Out]# 15673  0aca2695a110  Kevin Bullock <kbullock@ringworld.org>     1: +1/-1
#[Out]# 15605  c0e42b47ec1a  Kevin Bullock <kbullock@ringworld.org>     1: +2/-2
#[Out]# 15604  875bb46e35ea  Kevin Bullock <kbullock@ringworld.org>   1: +11/-11
#[Out]# 15495  32a6e00e4cfe  Kevin Bullock <kbullock@ringworld.org>     1: +3/-3
#[Out]# 15327  67e92d29ecb5  Kevin Bullock <kbullock@ringworld.org>    2: +10/-1
#[Out]# 14829  95ced9f5bf29  Kevin Bullock <kbullock@ringworld.org>    2: +15/-0
#[Out]# 14709  88a53081fb21  Kevin Bullock <kbullock@ringworld.org>     3: +3/-3
#[Out]# 14217  328422b0380d  Kevin Bullock <kbullock@ringworld.org>    3: +23/-1
#[Out]# 14216  9029b1a38c30  Kevin Bullock <kbullock@ringworld.org>    2: +14/-5
#[Out]# 13642  31ec4d7eb63f  Kevin Bullock <kbullock@ringworld.org>    2: +9/-11
#[Out]# 13622  3c753f9a2fbc  Kevin Bullock <kbullock@ringworld.org>     1: +4/-4
#[Out]# 13509  8aea95ec128f  Kevin Bullock <kbullock@ringworld.org>   1: +24/-20
#[Out]# 13477  0fb2ff949790  Kevin Bullock <kbullock@ringworld.org>   5: +42/-11
#[Out]# 13476  b85a09f368bd  Kevin Bullock <kbullock@ringworld.org>     1: +6/-0
#[Out]# 13428  5ef29e0dd418  Kevin Bullock <kbullock@ringworld.org>     2: +4/-4
#[Out]# 13407  354f304152ad  Kevin Bullock <kbullock@ringworld.org>     1: +3/-2
#[Out]# 13334  535a891284da  Kevin Bullock <kbullock@ringworld.org>     1: +1/-1
#[Out]# 13333  7ebdfa37842e  Kevin Bullock <kbullock@ringworld.org>     1: +2/-2
#[Out]# 13324  23bbb5b888ea  Kevin Bullock <kbullock@ringworld.org>   2: +52/-41
#[Out]# 13271  a8cef95cea88  Kevin Bullock <kbullock@ringworld.org>    2: +40/-1
#[Out]# 13245  592998ba3466  Kevin Bullock <kbullock@ringworld.org>    1: +2/-12
#[Out]# 13244  f14cfcc488fb  Kevin Bullock <kbullock@ringworld.org>   1: +14/-11
#[Out]# 13227  be7e8e9bc5e5  Kevin Bullock <kbullock@ringworld.org>  3: +379/-12
#[Out]# 13226  9b46dd253052  Kevin Bullock <kbullock@ringworld.org>    2: +0/-80
#[Out]# 13108  efbee27415ab  Kevin Bullock <kbullock@ringworld.org>     1: +2/-2
#[Out]# 13065  515c2786e1cf  Kevin Bullock <kbullock@ringworld.org>    2: +12/-2
#[Out]# 13064  a5f7f1e9340e  Kevin Bullock <kbullock@ringworld.org>    2: +56/-4
#[Out]# 12990  1c1ca9d393f4  Kevin Bullock <kbullock@ringworld.org>   3: +57/-11
#[Out]# 12989  ea3c93b53fdb  Kevin Bullock <kbullock@ringworld.org>    2: +36/-3
#[Out]# 12988  c1492615cdee  Kevin Bullock <kbullock@ringworld.org>    2: +17/-4
#[Out]# 12968  487b5787fe01  Kevin Bullock <kbullock@ringworld.org>     1: +1/-3
#[Out]# 12953  f08df4d38442  Kevin Bullock <kbullock@ringworld.org>    2: +82/-0
#[Out]# 12892  919c440868d9  Kevin Bullock <kbullock@ringworld.org>     1: +1/-1
#[Out]# 12847  b00eda50ad2b  Kevin Bullock <kbullock@ringworld.org>   26: +1/-84
#[Out]# 12773  4212fdc4db18  Kevin Bullock <kbullock@ringworld.org>     1: +4/-0
#[Out]# 12691  8c034a825cfe  Kevin Bullock <kbullock@ringworld.org>    1: +11/-6
#[Out]# 9563   3e698434b990  Kevin Bullock <kbullock@ringworld.org>   1: +17/-15
#[Out]# 9536   33033af09308  Kevin Bullock <kbullock@ringworld.org>    1: +17/-0
#[Out]# 9151   bcc27ee3a37b  Kevin Bullock <kbullock@ringworld.org>     1: +2/-3), ('Kevin Christen <kevin.christen@gmail.com>',               node                                     author    changestr
#[Out]# n                                                                         
#[Out]# 6500  c6890cfc2253  Kevin Christen <kevin.christen@gmail.com>     1: +2/-1
#[Out]# 6499  09db2b8236ec  Kevin Christen <kevin.christen@gmail.com>     1: +9/-5
#[Out]# 5877  5e7a8ea375a6  Kevin Christen <kevin.christen@gmail.com>     1: +4/-4
#[Out]# 5863  3a1ffc1da32c  Kevin Christen <kevin.christen@gmail.com>  15: +39/-44
#[Out]# 5838  956e01c31914  Kevin Christen <kevin.christen@gmail.com>     1: +4/-5
#[Out]# 5833  b7b22a2ade2e  Kevin Christen <kevin.christen@gmail.com>   1: +220/-0
#[Out]# 5830  d17e57592909  Kevin Christen <kevin.christen@gmail.com>     3: +6/-3), ('Kevin Gessner <kevin@fogcreek.com>',                node                              author   changestr
#[Out]# n                                                                  
#[Out]# 15791  f15c646bffc7  Kevin Gessner <kevin@fogcreek.com>   2: +29/-5
#[Out]# 15477  971c55ce03b8  Kevin Gessner <kevin@fogcreek.com>   1: +15/-7
#[Out]# 14890  c208dcd0f709  Kevin Gessner <kevin@fogcreek.com>    1: +6/-1
#[Out]# 13922  1209e1d52b68  Kevin Gessner <kevin@fogcreek.com>  5: +15/-17), ('Kevin Gessner <kevin@kevingessner.com>',                node                                  author   changestr
#[Out]# n                                                                      
#[Out]# 14117  debe5083a84e  Kevin Gessner <kevin@kevingessner.com>    1: +8/-0
#[Out]# 14116  08fde203a600  Kevin Gessner <kevin@kevingessner.com>  3: +1/-202
#[Out]# 14109  2e4d79dcc0a0  Kevin Gessner <kevin@kevingessner.com>    1: +1/-1
#[Out]# 14107  305c97670d7a  Kevin Gessner <kevin@kevingessner.com>   3: +94/-2
#[Out]# 14105  04ce8fa1015d  Kevin Gessner <kevin@kevingessner.com>   3: +46/-0
#[Out]# 14104  e88a4958a6b7  Kevin Gessner <kevin@kevingessner.com>   1: +26/-8), ('Kirill Elagin <kirelagin@gmail.com>',                node                               author   changestr
#[Out]# n                                                                   
#[Out]# 15201  2c4fdee4d1a8  Kirill Elagin <kirelagin@gmail.com>  1: +22/-13), ('Kirill Smelkov <kirr@landau.phys.spbu.ru>',               node                                     author   changestr
#[Out]# n                                                                        
#[Out]# 5462  91a522a69c13  Kirill Smelkov <kirr@landau.phys.spbu.ru>  3: +145/-9
#[Out]# 5461  ab4d2e9f3b97  Kirill Smelkov <kirr@landau.phys.spbu.ru>    1: +3/-2), ('Kirill Smelkov <kirr@mns.spb.ru>',               node                            author   changestr
#[Out]# n                                                               
#[Out]# 6398  ecde0baee570  Kirill Smelkov <kirr@mns.spb.ru>    1: +1/-1
#[Out]# 5963  28a79c259fcf  Kirill Smelkov <kirr@mns.spb.ru>  2: +298/-0
#[Out]# 5962  b014ff3fdaeb  Kirill Smelkov <kirr@mns.spb.ru>    1: +9/-7
#[Out]# 5873  c32d41affb68  Kirill Smelkov <kirr@mns.spb.ru>   1: +45/-7
#[Out]# 5872  784073457a0f  Kirill Smelkov <kirr@mns.spb.ru>    1: +4/-1
#[Out]# 5871  863e237b58fb  Kirill Smelkov <kirr@mns.spb.ru>    1: +9/-0
#[Out]# 5870  0c29977bd7db  Kirill Smelkov <kirr@mns.spb.ru>   1: +37/-2
#[Out]# 5869  cc43d9f36ff2  Kirill Smelkov <kirr@mns.spb.ru>   1: +38/-3
#[Out]# 5799  bc475d1f74ca  Kirill Smelkov <kirr@mns.spb.ru>    2: +8/-4
#[Out]# 5741  5d0b94d3ad0c  Kirill Smelkov <kirr@mns.spb.ru>    1: +2/-0
#[Out]# 5710  b940260c4291  Kirill Smelkov <kirr@mns.spb.ru>    1: +2/-1
#[Out]# 5566  37cc79a5727a  Kirill Smelkov <kirr@mns.spb.ru>    1: +2/-1), ('Klaus Koch <kuk42@gmx.net>',                node                      author  changestr
#[Out]# n                                                         
#[Out]# 13557  29c800ee54cf  Klaus Koch <kuk42@gmx.net>  2: +10/-1
#[Out]# 12929  ff083040a555  Klaus Koch <kuk42@gmx.net>   2: +6/-0), ('Konstantin Zemlyak <zart@zartsoft.ru>',                node                                 author changestr
#[Out]# n                                                                   
#[Out]# 10640  a1cb8ca051c0  Konstantin Zemlyak <zart@zartsoft.ru>  1: +6/-2), ('Kostantinos Koukopoulos <kouk@noc.uoa.gr>',               node                                     author changestr
#[Out]# n                                                                      
#[Out]# 5900  493632bb171c  Kostantinos Koukopoulos <kouk@noc.uoa.gr>  1: +1/-1), ('Kyle Moffett <mrmacman_g4@mac.com>',              node                              author changestr
#[Out]# n                                                              
#[Out]# 826  16700cdd9055  Kyle Moffett <mrmacman_g4@mac.com>  1: +1/-1), ('L. David Baron <dbaron@dbaron.org>',                node                              author changestr
#[Out]# n                                                                
#[Out]# 12805  cae1c187abd4  L. David Baron <dbaron@dbaron.org>  1: +2/-1), ('LUO Zheng <xmuluo@gmail.com>',                node                        author changestr
#[Out]# n                                                          
#[Out]# 14559  e29821ca94cf  LUO Zheng <xmuluo@gmail.com>  1: +1/-1), ('Laurens Holst <laurens.hg@grauw.nl>',                node                               author changestr
#[Out]# n                                                                 
#[Out]# 15766  e86dd8dfdea0  Laurens Holst <laurens.hg@grauw.nl>  2: +7/-7
#[Out]# 15733  64a80204433f  Laurens Holst <laurens.hg@grauw.nl>  1: +5/-0), ('Lee Cantey <lcantey@embarcadero.com>',                node                                author changestr
#[Out]# n                                                                  
#[Out]# 13320  5dda6c708138  Lee Cantey <lcantey@embarcadero.com>  1: +1/-1), ('Lee Cantey <lcantey@gmail.com>',                node                          author   changestr
#[Out]# n                                                              
#[Out]# 15092  3bccc15b201f  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 15003  4c01478991a3  Lee Cantey <lcantey@gmail.com>    1: +1/-3
#[Out]# 14833  58f97dcbd550  Lee Cantey <lcantey@gmail.com>  1: +19/-18
#[Out]# 13832  366e014a1ded  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 11862  ca6ede0988d5  Lee Cantey <lcantey@gmail.com>    2: +3/-3
#[Out]# 11601  71dab6955be0  Lee Cantey <lcantey@gmail.com>    2: +3/-3
#[Out]# 11378  2bb6dbf04757  Lee Cantey <lcantey@gmail.com>    1: +1/-0
#[Out]# 10595  47f9868d8dcf  Lee Cantey <lcantey@gmail.com>    1: +2/-2
#[Out]# 9596   a41f2840f9c6  Lee Cantey <lcantey@gmail.com>    1: +0/-1
#[Out]# 9595   6219401643d1  Lee Cantey <lcantey@gmail.com>    2: +4/-0
#[Out]# 7918   e945e012d5d1  Lee Cantey <lcantey@gmail.com>    1: +3/-3
#[Out]# 6726   5868d0b8509f  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 6464   1afb186d2934  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 6031   26ef792f834e  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 6028   e45de0f47215  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 5734   5d14d71148b8  Lee Cantey <lcantey@gmail.com>    1: +8/-6
#[Out]# 5512   cd893635b542  Lee Cantey <lcantey@gmail.com>   1: +2/-11
#[Out]# 5000   01ba62729c60  Lee Cantey <lcantey@gmail.com>    1: +1/-0
#[Out]# 4998   8c5aca855b5d  Lee Cantey <lcantey@gmail.com>  1: +45/-45
#[Out]# 4997   30762680fcd2  Lee Cantey <lcantey@gmail.com>  1: +45/-28
#[Out]# 4946   4bd0b2f862ba  Lee Cantey <lcantey@gmail.com>    1: +7/-3
#[Out]# 4909   778bab992732  Lee Cantey <lcantey@gmail.com>  1: +41/-41
#[Out]# 4752   4da2149b63a1  Lee Cantey <lcantey@gmail.com>    1: +2/-1
#[Out]# 4634   a04b5f37eda7  Lee Cantey <lcantey@gmail.com>   1: +14/-4
#[Out]# 4633   02956be66a58  Lee Cantey <lcantey@gmail.com>    1: +2/-1
#[Out]# 4632   d4e4d0f4fba4  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 4631   eb99af2d845e  Lee Cantey <lcantey@gmail.com>    1: +2/-0
#[Out]# 4433   1386a9cffc88  Lee Cantey <lcantey@gmail.com>    1: +9/-2
#[Out]# 4432   1bcf38111877  Lee Cantey <lcantey@gmail.com>    1: +2/-2
#[Out]# 4046   d1dd16256114  Lee Cantey <lcantey@gmail.com>   1: +33/-9
#[Out]# 3617   638193139ba8  Lee Cantey <lcantey@gmail.com>    1: +0/-2
#[Out]# 3422   2300632a3bc8  Lee Cantey <lcantey@gmail.com>    2: +4/-1
#[Out]# 3421   846bf33bf140  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 3012   fa4229c60dd7  Lee Cantey <lcantey@gmail.com>    5: +5/-5
#[Out]# 2970   12d1475b48df  Lee Cantey <lcantey@gmail.com>    1: +1/-0
#[Out]# 2969   7827bc82ebc5  Lee Cantey <lcantey@gmail.com>    2: +2/-2
#[Out]# 2681   259acfb963d1  Lee Cantey <lcantey@gmail.com>  4: +122/-6
#[Out]# 2611   1b4eb1f92433  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 2610   7a87aebd848e  Lee Cantey <lcantey@gmail.com>    1: +2/-1
#[Out]# 2575   7289d20b18cd  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 2516   4716a58c8cd5  Lee Cantey <lcantey@gmail.com>    2: +4/-7
#[Out]# 2321   d9ca698e3c5a  Lee Cantey <lcantey@gmail.com>    1: +8/-2
#[Out]# 2307   5b3a3e35f084  Lee Cantey <lcantey@gmail.com>    1: +4/-0
#[Out]# 2276   766c3c852786  Lee Cantey <lcantey@gmail.com>   3: +42/-5
#[Out]# 2216   1cbd10cfcb7c  Lee Cantey <lcantey@gmail.com>   3: +23/-7
#[Out]# 2091   fb8b35b0def9  Lee Cantey <lcantey@gmail.com>   1: +15/-2
#[Out]# 2024   6328445b0e71  Lee Cantey <lcantey@gmail.com>   1: +15/-7
#[Out]# 2001   a439b7b51530  Lee Cantey <lcantey@gmail.com>    1: +6/-5
#[Out]# 1992   ea8345a7a29d  Lee Cantey <lcantey@gmail.com>    1: +1/-0
#[Out]# 1864   7a09785d3237  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 1845   cfe689ab3f06  Lee Cantey <lcantey@gmail.com>  1: +23/-22
#[Out]# 1844   b768f3ae0c2c  Lee Cantey <lcantey@gmail.com>  1: +12/-13
#[Out]# 1834   24881eaebee3  Lee Cantey <lcantey@gmail.com>    1: +4/-0
#[Out]# 1795   36e19e3da12d  Lee Cantey <lcantey@gmail.com>    1: +1/-1
#[Out]# 1315   32f6cae83db7  Lee Cantey <lcantey@gmail.com>    1: +4/-3), ('Levi Bard <levi@unity3d.com>',                node                        author   changestr
#[Out]# n                                                            
#[Out]# 16598  265daefc00b2  Levi Bard <levi@unity3d.com>    1: +2/-0
#[Out]# 15818  b9886dde3649  Levi Bard <levi@unity3d.com>  1: +72/-83
#[Out]# 15817  3d11da212e30  Levi Bard <levi@unity3d.com>   1: +27/-0
#[Out]# 15816  884946c002b8  Levi Bard <levi@unity3d.com>   1: +18/-3
#[Out]# 15815  62098aeb1e15  Levi Bard <levi@unity3d.com>    1: +3/-1
#[Out]# 15805  8bed8551d535  Levi Bard <levi@unity3d.com>  1: +81/-21
#[Out]# 15804  0d91211dd12f  Levi Bard <levi@unity3d.com>  4: +36/-44
#[Out]# 15799  2c10ea43c801  Levi Bard <levi@unity3d.com>    1: +3/-2), ('Luke Plant <L.Plant.98@cantab.net>',                node                              author  changestr
#[Out]# n                                                                 
#[Out]# 13869  7e5031180c0f  Luke Plant <L.Plant.98@cantab.net>  2: +17/-0
#[Out]# 13709  3cbb3c57a50e  Luke Plant <L.Plant.98@cantab.net>  2: +26/-4), ('Mads Kiilerich <mads at kiilerich.com>',                node                                  author   changestr
#[Out]# n                                                                      
#[Out]# 11633  84a09639d9f1  Mads Kiilerich <mads at kiilerich.com>  2: +55/-12), ('Mads Kiilerich <mads@kiilerich.com>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 365 entries, 16613 to 6541
#[Out]# Data columns:
#[Out]# node         365  non-null values
#[Out]# author       365  non-null values
#[Out]# changestr    365  non-null values
#[Out]# dtypes: object(3)), ('Manpreet Singh <junkblocker@yahoo.com>',                node                                  author     changestr
#[Out]# n                                                                        
#[Out]# 10550  8036bc1871c2  Manpreet Singh <junkblocker@yahoo.com>   2: +47/-128
#[Out]# 10545  b9e4a67329cd  Manpreet Singh <junkblocker@yahoo.com>  2: +848/-231
#[Out]# 2350   091d555653a4  Manpreet Singh <junkblocker@yahoo.com>    2: +429/-0
#[Out]# 2278   3711e23ab10a  Manpreet Singh <junkblocker@yahoo.com>      1: +1/-1
#[Out]# 2271   90b122730d32  Manpreet Singh <junkblocker@yahoo.com>      1: +2/-0), ('Manuel Holtgrewe <purestorm@ggnore.net>',               node                                   author  changestr
#[Out]# n                                                                     
#[Out]# 5499  dcbda0c4c3eb  Manuel Holtgrewe <purestorm@ggnore.net>  3: +38/-4), ('Marc Simpson <marc@0branch.com>',                node                           author changestr
#[Out]# n                                                             
#[Out]# 15081  2f0a3977c939  Marc Simpson <marc@0branch.com>  1: +6/-1
#[Out]# 15080  ef43610a4cce  Marc Simpson <marc@0branch.com>  1: +5/-2), ('Marc-Antoine Ruel <maruel@google.com>',                node                                 author changestr
#[Out]# n                                                                   
#[Out]# 15613  7ee7b7426aad  Marc-Antoine Ruel <maruel@google.com>  1: +2/-4
#[Out]# 15426  58f96703a9ab  Marc-Antoine Ruel <maruel@google.com>  1: +2/-4), ('Marco Barisione <marco@barisione.org>',               node                                 author   changestr
#[Out]# n                                                                    
#[Out]# 2385  5d895018ef42  Marco Barisione <marco@barisione.org>    1: +1/-1
#[Out]# 2384  068b32d06873  Marco Barisione <marco@barisione.org>  3: +13/-46
#[Out]# 2383  dec7aa404dcf  Marco Barisione <marco@barisione.org>    1: +1/-0
#[Out]# 2378  6e5d40ec862d  Marco Barisione <marco@barisione.org>   1: +16/-6
#[Out]# 2377  626779aba9bb  Marco Barisione <marco@barisione.org>  1: +11/-11
#[Out]# 2376  52cfb9864257  Marco Barisione <marco@barisione.org>    1: +9/-6
#[Out]# 2375  9f4f77693890  Marco Barisione <marco@barisione.org>   1: +17/-2), ('Marco Beck <mbeck@miamod.de>',               node                        author changestr
#[Out]# n                                                         
#[Out]# 8700  3d53820381cb  Marco Beck <mbeck@miamod.de>  1: +1/-0), ('Marcos Chaves <marcos.nospam@gmail.com>',               node                                   author   changestr
#[Out]# n                                                                      
#[Out]# 4672  272c0a09b203  Marcos Chaves <marcos.nospam@gmail.com>   3: +13/-0
#[Out]# 3679  2956948b81f3  Marcos Chaves <marcos.nospam@gmail.com>  4: +16/-16), ('Marek Kubica <marek@xivilization.net>',               node                                 author    changestr
#[Out]# n                                                                     
#[Out]# 7614  d65671beee7f  Marek Kubica <marek@xivilization.net>     1: +2/-0
#[Out]# 7065  209ef5f3534c  Marek Kubica <marek@xivilization.net>  16: +663/-0), ('Mark Determann <qwerty360@gmail.com>',                node                                author changestr
#[Out]# n                                                                  
#[Out]# 10716  5dc09507b90e  Mark Determann <qwerty360@gmail.com>  1: +2/-0), ('Mark Drago <markdrago@gmail.com>',                node                            author  changestr
#[Out]# n                                                               
#[Out]# 13701  0b79cf616e65  Mark Drago <markdrago@gmail.com>  2: +17/-1), ('Mark Edgington <edgimar@gmail.com>',                node                              author   changestr
#[Out]# n                                                                  
#[Out]# 11599  53fdc0989047  Mark Edgington <edgimar@gmail.com>  1: +30/-26
#[Out]# 7503   bbcd2dea19fe  Mark Edgington <edgimar@gmail.com>    2: +3/-3
#[Out]# 7502   b663b5563de7  Mark Edgington <edgimar@gmail.com>    1: +3/-2
#[Out]# 7337   2dc868712dcc  Mark Edgington <edgimar@gmail.com>   3: +65/-5), ('Mark Round <hg@markround.com>',                node                         author changestr
#[Out]# n                                                           
#[Out]# 16615  7002bb17cc5e  Mark Round <hg@markround.com>  1: +7/-4), ('Markus F.X.J. Oberhumer <markus@oberhumer.com>',                node                                          author   changestr
#[Out]# n                                                                              
#[Out]# 13815  afe9269dccec  Markus F.X.J. Oberhumer <markus@oberhumer.com>  1: +10/-10
#[Out]# 13814  5d0cdf4ec338  Markus F.X.J. Oberhumer <markus@oberhumer.com>    1: +4/-2
#[Out]# 13813  df978f28a259  Markus F.X.J. Oberhumer <markus@oberhumer.com>    1: +1/-1
#[Out]# 13812  4a9c09239ba1  Markus F.X.J. Oberhumer <markus@oberhumer.com>    1: +2/-2
#[Out]# 13775  15b97a1cd60b  Markus F.X.J. Oberhumer <markus@oberhumer.com>    1: +4/-6
#[Out]# 13774  12f60626d817  Markus F.X.J. Oberhumer <markus@oberhumer.com>    1: +1/-0
#[Out]# 13773  9a41af6b9f29  Markus F.X.J. Oberhumer <markus@oberhumer.com>    1: +3/-3
#[Out]# 4710   1aba0b752847  Markus F.X.J. Oberhumer <markus@oberhumer.com>    1: +2/-2
#[Out]# 4709   53eca35c3aeb  Markus F.X.J. Oberhumer <markus@oberhumer.com>    2: +5/-0
#[Out]# 4708   01f9ee4de1ad  Markus F.X.J. Oberhumer <markus@oberhumer.com>    1: +1/-0
#[Out]# 4707   3fd4dde37628  Markus F.X.J. Oberhumer <markus@oberhumer.com>    1: +1/-1
#[Out]# 4706   f0aa759b8f93  Markus F.X.J. Oberhumer <markus@oberhumer.com>    1: +3/-1
#[Out]# 2388   74d569332f8b  Markus F.X.J. Oberhumer <markus@oberhumer.com>  1: +12/-16
#[Out]# 2387   62ce297f214f  Markus F.X.J. Oberhumer <markus@oberhumer.com>   2: +12/-1), ('Markus Zapke-Gr\xc3\xbcndemann <info@keimlink.de>',                node                                      author  changestr
#[Out]# n                                                                         
#[Out]# 15862  44a371823f83  Markus Zapke-Gründemann <info@keimlink.de>  2: +7/-1
#[Out]# 15860  58dcb837f193  Markus Zapke-Gründemann <info@keimlink.de>  1: +1/-1), ('Marti Raudsepp <marti@juffo.org>',                node                            author   changestr
#[Out]# n                                                                
#[Out]# 10056  e5b44a7986d0  Marti Raudsepp <marti@juffo.org>   1: +21/-5
#[Out]# 10055  4600e6222efb  Marti Raudsepp <marti@juffo.org>  3: +50/-11
#[Out]# 9730   732fc0e9d411  Marti Raudsepp <marti@juffo.org>    1: +1/-1
#[Out]# 9715   f0e99a2eac76  Marti Raudsepp <marti@juffo.org>   3: +38/-1
#[Out]# 8452   e1f4343db740  Marti Raudsepp <marti@juffo.org>    4: +3/-2
#[Out]# 8014   43b70a964e0d  Marti Raudsepp <marti@juffo.org>    2: +3/-1
#[Out]# 8008   62154415821f  Marti Raudsepp <marti@juffo.org>  3: +22/-14
#[Out]# 8007   52e442fe43f4  Marti Raudsepp <marti@juffo.org>   2: +59/-0
#[Out]# 6187   531f3e78c6f2  Marti Raudsepp <marti@juffo.org>    1: +1/-1
#[Out]# 6186   aae4eb2f40b0  Marti Raudsepp <marti@juffo.org>    1: +3/-2
#[Out]# 6185   c48d778d7c23  Marti Raudsepp <marti@juffo.org>    1: +2/-2
#[Out]# 6184   9d13e7129423  Marti Raudsepp <marti@juffo.org>    1: +2/-0), ('Martijn Pieters <mj@zopatista.com>',               node                              author   changestr
#[Out]# n                                                                 
#[Out]# 8261  0eade101f762  Martijn Pieters <mj@zopatista.com>    1: +2/-2
#[Out]# 8260  99d7e2db8da8  Martijn Pieters <mj@zopatista.com>  1: +33/-33
#[Out]# 8258  dd1b47e17d7e  Martijn Pieters <mj@zopatista.com>   3: +10/-1
#[Out]# 8192  29bc5d18714a  Martijn Pieters <mj@zopatista.com>   3: +18/-1
#[Out]# 7887  aee8455ee8ec  Martijn Pieters <mj@zopatista.com>   3: +10/-1), ('Martin Geisler <martin@geisler.net>',                node                               author  changestr
#[Out]# n                                                                  
#[Out]# 16607  48b1674ac1e7  Martin Geisler <martin@geisler.net>  2: +13/-1), ('Martin Geisler <mg...@daimi.au.dk>',               node                              author changestr
#[Out]# n                                                               
#[Out]# 7533  31f70804f1b1  Martin Geisler <mg...@daimi.au.dk>  1: +9/-0), ('Martin Geisler <mg@aragost.com>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 298 entries, 16571 to 10761
#[Out]# Data columns:
#[Out]# node         298  non-null values
#[Out]# author       298  non-null values
#[Out]# changestr    298  non-null values
#[Out]# dtypes: object(3)), ('Martin Geisler <mg@daimi.au.dk>',               node                           author       changestr
#[Out]# n                                                                  
#[Out]# 8062  af49e2d15e51  Martin Geisler <mg@daimi.au.dk>      1: +18/-10
#[Out]# 8061  8985e1daa7f5  Martin Geisler <mg@daimi.au.dk>        2: +2/-2
#[Out]# 8054  58ba4b86ae13  Martin Geisler <mg@daimi.au.dk>        2: +8/-8
#[Out]# 8050  36a1219a13ab  Martin Geisler <mg@daimi.au.dk>   1: +1006/-938
#[Out]# 8049  595baa7c726f  Martin Geisler <mg@daimi.au.dk>      1: +84/-77
#[Out]# 8048  d5b1b846f277  Martin Geisler <mg@daimi.au.dk>    3: +139/-123
#[Out]# 8047  14f27921932a  Martin Geisler <mg@daimi.au.dk>        1: +7/-6
#[Out]# 8046  36a23a18b999  Martin Geisler <mg@daimi.au.dk>        1: +4/-3
#[Out]# 8045  c0e3aca616de  Martin Geisler <mg@daimi.au.dk>      1: +13/-11
#[Out]# 8044  83d7c9cfb065  Martin Geisler <mg@daimi.au.dk>      1: +14/-12
#[Out]# 8043  b25110140573  Martin Geisler <mg@daimi.au.dk>      2: +27/-26
#[Out]# 8042  e2c55c4a25e2  Martin Geisler <mg@daimi.au.dk>        1: +8/-7
#[Out]# 8041  8eb9f495e150  Martin Geisler <mg@daimi.au.dk>      1: +31/-29
#[Out]# 8040  a999dbc915f2  Martin Geisler <mg@daimi.au.dk>        1: +2/-2
#[Out]# 8039  b8e5d9487504  Martin Geisler <mg@daimi.au.dk>        1: +8/-8
#[Out]# 8038  3c22fdc741d8  Martin Geisler <mg@daimi.au.dk>      1: +78/-64
#[Out]# 8037  b83a11536fc6  Martin Geisler <mg@daimi.au.dk>      2: +43/-39
#[Out]# 8036  0e7f02eaa63b  Martin Geisler <mg@daimi.au.dk>        1: +7/-7
#[Out]# 8035  675a5a1ab0ee  Martin Geisler <mg@daimi.au.dk>        1: +4/-3
#[Out]# 8034  cdb848e8c4b5  Martin Geisler <mg@daimi.au.dk>      1: +12/-12
#[Out]# 8033  468ab22785aa  Martin Geisler <mg@daimi.au.dk>    2: +121/-109
#[Out]# 8032  0447939b4b97  Martin Geisler <mg@daimi.au.dk>        1: +9/-8
#[Out]# 8031  17147b465a9d  Martin Geisler <mg@daimi.au.dk>        1: +3/-3
#[Out]# 8030  c756e695012a  Martin Geisler <mg@daimi.au.dk>        1: +5/-5
#[Out]# 8029  0edca606c0f1  Martin Geisler <mg@daimi.au.dk>      1: +44/-37
#[Out]# 8028  5c61c75c2384  Martin Geisler <mg@daimi.au.dk>        1: +7/-6
#[Out]# 8027  7b813bdbd5d0  Martin Geisler <mg@daimi.au.dk>     12: +52/-52
#[Out]# 8026  cab4a521a3fd  Martin Geisler <mg@daimi.au.dk>        1: +6/-1
#[Out]# 8025  20df260ae301  Martin Geisler <mg@daimi.au.dk>        1: +6/-6
#[Out]# 8024  3d8252430e17  Martin Geisler <mg@daimi.au.dk>        1: +4/-1
#[Out]# 8023  6b04f12d2831  Martin Geisler <mg@daimi.au.dk>      4: +10/-10
#[Out]# 8022  aa512a03f6d3  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 8021  1cd3775e097c  Martin Geisler <mg@daimi.au.dk>        1: +7/-4
#[Out]# 8020  a62fc8fe882f  Martin Geisler <mg@daimi.au.dk>        1: +2/-5
#[Out]# 8019  fc4a3931e608  Martin Geisler <mg@daimi.au.dk>        1: +3/-1
#[Out]# 8018  a8a719ff150a  Martin Geisler <mg@daimi.au.dk>        2: +3/-3
#[Out]# 7980  ec4784bb7d75  Martin Geisler <mg@daimi.au.dk>        1: +3/-3
#[Out]# 7976  072df47d84c1  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 7975  0796c8862bee  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 7972  c84df11bf721  Martin Geisler <mg@daimi.au.dk>        1: +7/-7
#[Out]# 7971  6809f47603f6  Martin Geisler <mg@daimi.au.dk>  2: +9258/-9258
#[Out]# 7970  016d6357646d  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 7942  caef5fdf1375  Martin Geisler <mg@daimi.au.dk>        1: +4/-2
#[Out]# 7912  a536b9a43227  Martin Geisler <mg@daimi.au.dk>      1: +43/-43
#[Out]# 7911  b2e38a85b33b  Martin Geisler <mg@daimi.au.dk>        1: +9/-8
#[Out]# 7910  9c5c9a764199  Martin Geisler <mg@daimi.au.dk>      1: +305/-1
#[Out]# 7909  b43d7fc6923a  Martin Geisler <mg@daimi.au.dk>       1: +7/-11
#[Out]# 7908  161484deaf30  Martin Geisler <mg@daimi.au.dk>     1: +127/-73
#[Out]# 7802  e5627562b9f2  Martin Geisler <mg@daimi.au.dk>        1: +1/-0
#[Out]# 7795  57ce4da29310  Martin Geisler <mg@daimi.au.dk>      1: +40/-40
#[Out]# 7791  1817e45c2212  Martin Geisler <mg@daimi.au.dk>        1: +3/-2
#[Out]# 7790  e8d62d6133c2  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 7777  34ff1a1b5dd7  Martin Geisler <mg@daimi.au.dk>       1: +28/-0
#[Out]# 7776  5280c39778b6  Martin Geisler <mg@daimi.au.dk>       1: +20/-7
#[Out]# 7762  1e70db1825d2  Martin Geisler <mg@daimi.au.dk>     1: +648/-44
#[Out]# 7757  db6a03225177  Martin Geisler <mg@daimi.au.dk>    1: +267/-311
#[Out]# 7745  b44dbb95f07f  Martin Geisler <mg@daimi.au.dk>      1: +28/-17
#[Out]# 7744  ec9b726a9428  Martin Geisler <mg@daimi.au.dk>        1: +4/-3
#[Out]# 7738  26bdb7109170  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 7737  fb0776fe3e38  Martin Geisler <mg@daimi.au.dk>        1: +3/-3
#[Out]# 7736  2e48668b51f0  Martin Geisler <mg@daimi.au.dk>        1: +2/-2
#[Out]# 7735  9f73bddb9d0b  Martin Geisler <mg@daimi.au.dk>       3: +38/-0
#[Out]# 7725  fff6e253e1f6  Martin Geisler <mg@daimi.au.dk>     1: +87/-104
#[Out]# 7724  a343cd25e425  Martin Geisler <mg@daimi.au.dk>        1: +5/-2
#[Out]# 7723  103127a8cbdb  Martin Geisler <mg@daimi.au.dk>       1: +30/-1
#[Out]# 7722  a1138f437640  Martin Geisler <mg@daimi.au.dk>        1: +8/-1
#[Out]# 7721  b6c2cb40e664  Martin Geisler <mg@daimi.au.dk>        1: +5/-2
#[Out]# 7713  9f9bbd33f71e  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 7712  a0de99db7cdc  Martin Geisler <mg@daimi.au.dk>     1: +704/-64
#[Out]# 7711  88326ee85a1b  Martin Geisler <mg@daimi.au.dk>       1: +11/-5
#[Out]# 7708  0ae7f0b312ea  Martin Geisler <mg@daimi.au.dk>       2: +13/-6
#[Out]# 7706  30d1d313370b  Martin Geisler <mg@daimi.au.dk>      2: +42/-42
#[Out]# 7705  9044d3567f6d  Martin Geisler <mg@daimi.au.dk>       1: +69/-0
#[Out]# 7704  f6bb40554e34  Martin Geisler <mg@daimi.au.dk>       1: +56/-0
#[Out]# 7702  f410c552fa15  Martin Geisler <mg@daimi.au.dk>       1: +81/-0
#[Out]# 7701  fac054f84600  Martin Geisler <mg@daimi.au.dk>      1: +103/-0
#[Out]# 7700  934f0667f6fa  Martin Geisler <mg@daimi.au.dk>    1: +811/-802
#[Out]# 7699  9bb33d4610b6  Martin Geisler <mg@daimi.au.dk>    1: +13/-1827
#[Out]# 7694  a55de9e2726f  Martin Geisler <mg@daimi.au.dk>      1: +81/-77
#[Out]# 7690  1ac4dc64cf2a  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 7688  161412a3341c  Martin Geisler <mg@daimi.au.dk>        1: +2/-2
#[Out]# 7661  0641fd8a4bb4  Martin Geisler <mg@daimi.au.dk>        1: +1/-0
#[Out]# 7660  2605b2ef3f07  Martin Geisler <mg@daimi.au.dk>    1: +10005/-0
#[Out]# 7659  5b5036ef847a  Martin Geisler <mg@daimi.au.dk>       1: +26/-1
#[Out]# 7658  85ae7aaf08e9  Martin Geisler <mg@daimi.au.dk>       1: +15/-2
#[Out]# 7657  a489e3a94443  Martin Geisler <mg@daimi.au.dk>       2: +35/-1
#[Out]# 7656  02e358a3a8a7  Martin Geisler <mg@daimi.au.dk>       3: +18/-4
#[Out]# 7636  fb32ae9c76e7  Martin Geisler <mg@daimi.au.dk>   21: +147/-148
#[Out]# 7635  551afd4a4691  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 7612  f7739cf3833c  Martin Geisler <mg@daimi.au.dk>        2: +2/-2
#[Out]# 7611  7bf7c073375e  Martin Geisler <mg@daimi.au.dk>      7: +22/-22
#[Out]# 7610  26adfaccdf73  Martin Geisler <mg@daimi.au.dk>      9: +25/-25
#[Out]# 7609  81f68565281c  Martin Geisler <mg@daimi.au.dk>        1: +8/-8
#[Out]# 7608  0be97ee2309d  Martin Geisler <mg@daimi.au.dk>        1: +0/-2
#[Out]# 7582  e05aa73ce2b7  Martin Geisler <mg@daimi.au.dk>        4: +5/-8
#[Out]# 7227  59b4ae211584  Martin Geisler <mg@daimi.au.dk>        5: +5/-5
#[Out]# 7137  7e6a3bae0e8e  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 7063  5f201f711932  Martin Geisler <mg@daimi.au.dk>        1: +2/-2
#[Out]# 7040  6651de7176a0  Martin Geisler <mg@daimi.au.dk>      1: +16/-14
#[Out]# 7039  46456a51e247  Martin Geisler <mg@daimi.au.dk>        1: +3/-3
#[Out]# 7038  f56e788fa292  Martin Geisler <mg@daimi.au.dk>      2: +22/-19
#[Out]# 7037  78341ea65d16  Martin Geisler <mg@daimi.au.dk>      3: +12/-19
#[Out]# 7030  7739b61897df  Martin Geisler <mg@daimi.au.dk>       3: +13/-0
#[Out]# 7028  2365c6d4c330  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 7027  07c8396fa001  Martin Geisler <mg@daimi.au.dk>        1: +5/-5
#[Out]# 7026  9a32b8a6868e  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 7025  af694c6a888c  Martin Geisler <mg@daimi.au.dk>      1: +20/-20
#[Out]# 7024  f1546aa94362  Martin Geisler <mg@daimi.au.dk>        1: +9/-8
#[Out]# 7000  057ced2b8543  Martin Geisler <mg@daimi.au.dk>        1: +1/-1
#[Out]# 6999  98abbcf9fbdf  Martin Geisler <mg@daimi.au.dk>        1: +3/-3
#[Out]# 6998  b3239badc711  Martin Geisler <mg@daimi.au.dk>        1: +5/-5
#[Out]# 6997  71da881b259e  Martin Geisler <mg@daimi.au.dk>        1: +3/-3
#[Out]# 6996  2af657eafeba  Martin Geisler <mg@daimi.au.dk>        1: +3/-2
#[Out]# 6995  12163fb21fce  Martin Geisler <mg@daimi.au.dk>      1: +12/-12
#[Out]# 6994  46da38eef1b0  Martin Geisler <mg@daimi.au.dk>      1: +41/-40
#[Out]# 6993  56c643bb562d  Martin Geisler <mg@daimi.au.dk>      1: +10/-10
#[Out]# 6992  e01ed40a31a2  Martin Geisler <mg@daimi.au.dk>        1: +4/-3
#[Out]# 6991  bd979854a388  Martin Geisler <mg@daimi.au.dk>        1: +3/-3
#[Out]# 6990  12472a240398  Martin Geisler <mg@daimi.au.dk>      7: +44/-44
#[Out]# 6989  a9411e29773f  Martin Geisler <mg@daimi.au.dk>        1: +2/-2
#[Out]# 6988  f7d545a866e8  Martin Geisler <mg@daimi.au.dk>        1: +5/-4
#[Out]# 6987  63b5f4c73c98  Martin Geisler <mg@daimi.au.dk>     10: +17/-15
#[Out]# 6986  3fffba1c87d0  Martin Geisler <mg@daimi.au.dk>       4: +6/-10
#[Out]# 6976  05ec27530d04  Martin Geisler <mg@daimi.au.dk>        3: +8/-2
#[Out]# 6973  3aa8ad0e03ba  Martin Geisler <mg@daimi.au.dk>        1: +4/-3
#[Out]# 6956  95f35b553ae6  Martin Geisler <mg@daimi.au.dk>        1: +0/-1
#[Out]# 6955  580d5e6bfc1f  Martin Geisler <mg@daimi.au.dk>      4: +14/-14
#[Out]# 6954  b92baef99ebf  Martin Geisler <mg@daimi.au.dk>        1: +2/-2
#[Out]# 6953  1a14608bdeff  Martin Geisler <mg@daimi.au.dk>        1: +1/-0
#[Out]# 6923  13fe85fe396b  Martin Geisler <mg@daimi.au.dk>        1: +1/-4
#[Out]# 6539  e3f9feb9ab7e  Martin Geisler <mg@daimi.au.dk>        1: +2/-1), ('Martin Geisler <mg@lazybytes.net>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 955 entries, 16450 to 7893
#[Out]# Data columns:
#[Out]# node         955  non-null values
#[Out]# author       955  non-null values
#[Out]# changestr    955  non-null values
#[Out]# dtypes: object(3)), ('Martin Kr\xc3\xbcger <martin.krueger@gmx.com>',                node                                  author  changestr
#[Out]# n                                                                     
#[Out]# 13624  676643eece79  Martin Krüger <martin.krueger@gmx.com>  1: +2/-2), ('Martin OConnor <martinoc@gmail.com>',               node                               author changestr
#[Out]# n                                                                
#[Out]# 6486  e1d8e79d7c8f  Martin OConnor <martinoc@gmail.com>  1: +1/-1
#[Out]# 6483  24b2e213d84b  Martin OConnor <martinoc@gmail.com>  1: +2/-2), ('Martin Roppelt <m.p.roppelt@web.de>',                node                               author     changestr
#[Out]# n                                                                     
#[Out]# 12582  038369eb8730  Martin Roppelt <m.p.roppelt@web.de>   1: +4/-1096
#[Out]# 12577  252d616bc2c0  Martin Roppelt <m.p.roppelt@web.de>      1: +1/-3
#[Out]# 12576  6a6e0e2f19aa  Martin Roppelt <m.p.roppelt@web.de>    1: +16/-11
#[Out]# 12575  7b51cce70a37  Martin Roppelt <m.p.roppelt@web.de>    1: +6/-182
#[Out]# 12574  6d539d0e2230  Martin Roppelt <m.p.roppelt@web.de>  1: +150/-932
#[Out]# 12573  8426cf23696e  Martin Roppelt <m.p.roppelt@web.de>      1: +9/-5), ('Martin Schr\xc3\xb6der <martinschroeder@vcp-sh.de>',                node                                       author       changestr
#[Out]# n                                                                               
#[Out]# 16658  01eb88248937  Martin Schröder <martinschroeder@vcp-sh.de>   1: +294/-139
#[Out]# 16657  ccde69ab6a7a  Martin Schröder <martinschroeder@vcp-sh.de>     1: +96/-74
#[Out]# 16656  a63f8502d7e6  Martin Schröder <martinschroeder@vcp-sh.de>  1: +1848/-780
#[Out]# 15725  42248609edd9  Martin Schröder <martinschroeder@vcp-sh.de>     1: +75/-29), ('Mathieu Clabaut <mathieu.clabaut@gmail.com>',               node                                       author   changestr
#[Out]# n                                                                          
#[Out]# 4074  afa1f57ae484  Mathieu Clabaut <mathieu.clabaut@gmail.com>    3: +8/-2
#[Out]# 3857  f6f16f871049  Mathieu Clabaut <mathieu.clabaut@gmail.com>  2: +21/-26
#[Out]# 3690  97d2c1909f98  Mathieu Clabaut <mathieu.clabaut@gmail.com>    1: +3/-3
#[Out]# 3685  193e9c6d1a6d  Mathieu Clabaut <mathieu.clabaut@gmail.com>   3: +18/-1), ('Mathieu Clabaut <mathieu.clabaut@systerel.fr>',                node                                         author  changestr
#[Out]# n                                                                            
#[Out]# 10621  b4b16e90712f  Mathieu Clabaut <mathieu.clabaut@systerel.fr>  3: +37/-2
#[Out]# 3094   8e8deb8035a4  Mathieu Clabaut <mathieu.clabaut@systerel.fr>   1: +7/-1), ('Matt Doar <matt@xensource.com>',               node                          author   changestr
#[Out]# n                                                             
#[Out]# 3093  f422c8265ae5  Matt Doar <matt@xensource.com>  3: +29/-25), ('Matt Harbison <matt_harbison@yahoo.com>',                node                                   author  changestr
#[Out]# n                                                                      
#[Out]# 16617  47b8ec0eb7fb  Matt Harbison <matt_harbison@yahoo.com>   1: +5/-1
#[Out]# 16516  597ddcb41b32  Matt Harbison <matt_harbison@yahoo.com>  3: +36/-4
#[Out]# 16515  12dabc22de77  Matt Harbison <matt_harbison@yahoo.com>  3: +38/-1), ('Matt Mackall <mpm@selenic.com>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 3083 entries, 16652 to 608
#[Out]# Data columns:
#[Out]# node         3083  non-null values
#[Out]# author       3083  non-null values
#[Out]# changestr    3083  non-null values
#[Out]# dtypes: object(3)), ('Matt Zuba <matt.zuba@goodwillaz.org>',                node                                author  changestr
#[Out]# n                                                                   
#[Out]# 15896  30c34fde40cc  Matt Zuba <matt.zuba@goodwillaz.org>  3: +31/-2), ('Matteo Capobianco <m.capobianco@gmail.com>',                node                                      author  changestr
#[Out]# n                                                                         
#[Out]# 16371  e5788269741a  Matteo Capobianco <m.capobianco@gmail.com>  2: +17/-1), ('Matthew Elder <sseses@gmail.com>',               node                            author  changestr
#[Out]# n                                                              
#[Out]# 1408  5010207c3527  Matthew Elder <sseses@gmail.com>  2: +28/-0), ('Maxim Dounin <mdounin@mdounin.ru>',               node                             author   changestr
#[Out]# n                                                                
#[Out]# 6473  7f0dd352fb4d  Maxim Dounin <mdounin@mdounin.ru>   3: +29/-2
#[Out]# 6091  e1f11b8a1e9e  Maxim Dounin <mdounin@mdounin.ru>    1: +3/-3
#[Out]# 6086  4baad19c4801  Maxim Dounin <mdounin@mdounin.ru>    2: +6/-6
#[Out]# 5875  2192ed187319  Maxim Dounin <mdounin@mdounin.ru>  2: +51/-32
#[Out]# 5865  38b592536a58  Maxim Dounin <mdounin@mdounin.ru>   4: +2/-10
#[Out]# 5854  180a3eee4b75  Maxim Dounin <mdounin@mdounin.ru>  7: +64/-30
#[Out]# 5853  124577de40a7  Maxim Dounin <mdounin@mdounin.ru>   2: +12/-8
#[Out]# 5746  b63ef7b1441c  Maxim Dounin <mdounin@mdounin.ru>  3: +110/-7
#[Out]# 5745  98f45e141567  Maxim Dounin <mdounin@mdounin.ru>    1: +1/-0
#[Out]# 5742  e9f1a1ccd51b  Maxim Dounin <mdounin@mdounin.ru>    1: +1/-0
#[Out]# 5490  f252ba975925  Maxim Dounin <mdounin@mdounin.ru>  3: +40/-20
#[Out]# 5486  7a64931e2d76  Maxim Dounin <mdounin@mdounin.ru>  5: +158/-9), ('Maxim Khitrov <mkhitrov@gmail.com>',                node                              author  changestr
#[Out]# n                                                                 
#[Out]# 11469  c37f35d7f2f5  Maxim Khitrov <mkhitrov@gmail.com>  4: +22/-9), ('Md. O. Shayan <mdoshayan@gmail.com>',                node                               author  changestr
#[Out]# n                                                                  
#[Out]# 13986  c3372529247f  Md. O. Shayan <mdoshayan@gmail.com>   1: +8/-4
#[Out]# 13975  332e400764e5  Md. O. Shayan <mdoshayan@gmail.com>  3: +20/-4
#[Out]# 13614  08d49b6b8d32  Md. O. Shayan <mdoshayan@gmail.com>   1: +5/-1), ('Michael Bacarella <mbacarella@janestreet.com>',                node                                         author changestr
#[Out]# n                                                                           
#[Out]# 16139  b9c4302310e5  Michael Bacarella <mbacarella@janestreet.com>  1: +6/-5), ('Michael Gebetsroither <michael.geb@gmx.at>',               node                                      author  changestr
#[Out]# n                                                                        
#[Out]# 4438  722417b3d7fa  Michael Gebetsroither <michael.geb@gmx.at>  1: +47/-0
#[Out]# 4287  5c1e18bb804c  Michael Gebetsroither <michael.geb@gmx.at>   1: +7/-4
#[Out]# 4222  022056263354  Michael Gebetsroither <michael.geb@gmx.at>   1: +5/-2
#[Out]# 1544  b3184bea3eb3  Michael Gebetsroither <michael.geb@gmx.at>   1: +1/-1), ('Michael Glassford <glassfordmjg@gmail.com>',                node                                      author  changestr
#[Out]# n                                                                         
#[Out]# 10734  e4f911ce21de  Michael Glassford <glassfordmjg@gmail.com>  1: +13/-2
#[Out]# 10664  ce2ae8bf3ae3  Michael Glassford <glassfordmjg@gmail.com>   1: +2/-1), ('Michael J. Pedersen <m.pedersen@icelus.org>',               node                                       author  changestr
#[Out]# n                                                                         
#[Out]# 8388  29f4f0d66cd5  Michael J. Pedersen <m.pedersen@icelus.org>  5: +33/-4), ('Michael Sommerville <msommerville@gmail.com>',               node                                        author  changestr
#[Out]# n                                                                          
#[Out]# 7057  aafe12bd7174  Michael Sommerville <msommerville@gmail.com>  1: +25/-3), ('Michael Springmann <michael.springmann@unibas.ch>',               node                                             author changestr
#[Out]# n                                                                              
#[Out]# 7840  a8dccbed54ef  Michael Springmann <michael.springmann@unibas.ch>  1: +1/-1), ('Michael Tj\xc3\xb8rnemark <michael@tjornemark.dk>',                node                                      author  changestr
#[Out]# n                                                                         
#[Out]# 16557  9dba55369cd8  Michael Tjørnemark <michael@tjornemark.dk>  1: +1/-1), ('Michal Kvasnica <kvasnica@gmail.com>',               node                                author  changestr
#[Out]# n                                                                  
#[Out]# 1439  65cbe22b03fa  Michal Kvasnica <kvasnica@gmail.com>  1: +10/-4), ('Michal Sznajder <michalsznajder@gmail.com>',                node                                      author     changestr
#[Out]# n                                                                            
#[Out]# 16260  dbf64594a3c3  Michal Sznajder <michalsznajder@gmail.com>  1: +152/-152
#[Out]# 15767  be55285470cf  Michal Sznajder <michalsznajder@gmail.com>      1: +1/-1
#[Out]# 15499  6266b1b970a5  Michal Sznajder <michalsznajder@gmail.com>      1: +6/-0), ('Michele Cella <michele.cella@gmail.com>',               node                                   author  changestr
#[Out]# n                                                                     
#[Out]# 6052  588ad9227b63  Michele Cella <michele.cella@gmail.com>   1: +1/-1
#[Out]# 6000  d83020d0466f  Michele Cella <michele.cella@gmail.com>   1: +2/-0
#[Out]# 5999  6d5ecf824a65  Michele Cella <michele.cella@gmail.com>  2: +36/-0
#[Out]# 5998  f25070ecf334  Michele Cella <michele.cella@gmail.com>  3: +13/-5
#[Out]# 5878  bd34f0ac3cb0  Michele Cella <michele.cella@gmail.com>   3: +8/-4), ('Mikael Berthe <mikael@lilotux.net>',               node                              author changestr
#[Out]# n                                                               
#[Out]# 1365  74cf45f8bc19  Mikael Berthe <mikael@lilotux.net>  1: +1/-1
#[Out]# 1242  4a6efec8b698  Mikael Berthe <mikael@lilotux.net>  1: +5/-2
#[Out]# 675   49de76abc4da  Mikael Berthe <mikael@lilotux.net>  1: +3/-0), ('Mike Sperber <sperber@deinprogramm.de>',                node                                  author changestr
#[Out]# n                                                                    
#[Out]# 12891  b69fd38a034e  Mike Sperber <sperber@deinprogramm.de>  1: +1/-2), ('Mikhail Sobolev <mss@mawhrin.net>',               node                             author changestr
#[Out]# n                                                              
#[Out]# 3059  5e39ad2c8b52  Mikhail Sobolev <mss@mawhrin.net>  1: +2/-2), ('Mikkel Fahn\xc3\xb8e J\xc3\xb8rgensen <mikkel@dvide.com>',               node                                      author     changestr
#[Out]# n                                                                           
#[Out]# 6307  6840668e3bf6  Mikkel Fahnøe Jørgensen <mikkel@dvide.com>  1: +56/-77
#[Out]# 6306  2f9de4aaea9e  Mikkel Fahnøe Jørgensen <mikkel@dvide.com>  3: +217/-0), ('Mikkel Kr\xc3\xb8igaard <mk@cs.au.dk>',               node                          author  changestr
#[Out]# n                                                            
#[Out]# 8378  7cf3d20f5967  Mikkel Krøigaard <mk@cs.au.dk>  1: +1/-1), ('Milo\xc5\xa1 Had\xc5\xbei\xc4\x87 <milos.hadzic@gmail.com>',                node                                 author    changestr
#[Out]# n                                                                      
#[Out]# 13583  adf3c4401c5d  Miloš Hadžić <milos.hadzic@gmail.com>  3: +3/-2), ('Mirko Friedenhagen <mirko-lists@friedenhagen.de>',               node                                            author  changestr
#[Out]# n                                                                              
#[Out]# 5738  1b365c5723bc  Mirko Friedenhagen <mirko-lists@friedenhagen.de>  3: +11/-2), ('Muli Ben-Yehuda <mulix@mulix.org>',               node                             author    changestr
#[Out]# n                                                                 
#[Out]# 1607  d72d27ee72b9  Muli Ben-Yehuda <mulix@mulix.org>     1: +3/-3
#[Out]# 1606  ba625c8083d8  Muli Ben-Yehuda <mulix@mulix.org>  13: +44/-13
#[Out]# 1602  fb4149eebdd4  Muli Ben-Yehuda <mulix@mulix.org>   1: +55/-28
#[Out]# 1600  728fd9584993  Muli Ben-Yehuda <mulix@mulix.org>     1: +7/-3
#[Out]# 751   0b245edec124  Muli Ben-Yehuda <mulix@mulix.org>    2: +22/-9), ('NIIMI Satoshi <sa2c@sa2c.net>',               node                         author     changestr
#[Out]# n                                                              
#[Out]# 5468  24eb1bf8dd83  NIIMI Satoshi <sa2c@sa2c.net>    1: +24/-20
#[Out]# 5467  521284cdbcb4  NIIMI Satoshi <sa2c@sa2c.net>      1: +5/-1
#[Out]# 5466  87860c62e003  NIIMI Satoshi <sa2c@sa2c.net>      1: +3/-0
#[Out]# 5465  9873cbb134b2  NIIMI Satoshi <sa2c@sa2c.net>      2: +3/-2
#[Out]# 4694  6bf58c9400e2  NIIMI Satoshi <sa2c@sa2c.net>      1: +5/-4
#[Out]# 4693  3f484688c702  NIIMI Satoshi <sa2c@sa2c.net>      1: +6/-8
#[Out]# 4456  ba22e867cb23  NIIMI Satoshi <sa2c@sa2c.net>  1: +126/-119
#[Out]# 4451  b008deae9910  NIIMI Satoshi <sa2c@sa2c.net>      1: +3/-2
#[Out]# 4450  189a8ca52bfc  NIIMI Satoshi <sa2c@sa2c.net>    1: +12/-12), ("Na'Tosha Bard <natosha@unity3d.com>",                node                               author     changestr
#[Out]# n                                                                     
#[Out]# 16599  29fe533fe447  Na'Tosha Bard <natosha@unity3d.com>      1: +2/-1
#[Out]# 16597  b371056ae353  Na'Tosha Bard <natosha@unity3d.com>      1: +2/-0
#[Out]# 16566  1ff42ee98446  Na'Tosha Bard <natosha@unity3d.com>      1: +0/-4
#[Out]# 16440  290850e7aa43  Na'Tosha Bard <natosha@unity3d.com>     4: +40/-1
#[Out]# 16320  51e6f318bdf1  Na'Tosha Bard <natosha@unity3d.com>      3: +4/-9
#[Out]# 16319  d87d9d8a8e03  Na'Tosha Bard <natosha@unity3d.com>  7: +154/-154
#[Out]# 16318  169525f8ffbb  Na'Tosha Bard <natosha@unity3d.com>      2: +7/-2
#[Out]# 16317  a18ad914aa21  Na'Tosha Bard <natosha@unity3d.com>    2: +10/-10
#[Out]# 16244  47ee41fcf42b  Na'Tosha Bard <natosha@unity3d.com>     2: +21/-1
#[Out]# 16074  3e1efb458e8b  Na'Tosha Bard <natosha@unity3d.com>     2: +14/-6
#[Out]# 15983  32b9aee3602c  Na'Tosha Bard <natosha@unity3d.com>      2: +4/-0
#[Out]# 15982  bf502ccc46d7  Na'Tosha Bard <natosha@unity3d.com>    3: +15/-14
#[Out]# 15967  295f8aeab363  Na'Tosha Bard <natosha@unity3d.com>      1: +4/-3
#[Out]# 15944  f19d5c852f9b  Na'Tosha Bard <natosha@unity3d.com>     3: +18/-1
#[Out]# 15943  f9efb325ea32  Na'Tosha Bard <natosha@unity3d.com>      1: +5/-2
#[Out]# 15916  c96148346af8  Na'Tosha Bard <natosha@unity3d.com>     3: +31/-3
#[Out]# 15914  264087940d5b  Na'Tosha Bard <natosha@unity3d.com>      1: +4/-0
#[Out]# 15913  c35dcde25174  Na'Tosha Bard <natosha@unity3d.com>      1: +3/-3
#[Out]# 15905  634d49a8b6db  Na'Tosha Bard <natosha@unity3d.com>      1: +2/-1
#[Out]# 15863  3ecce805ac13  Na'Tosha Bard <natosha@unity3d.com>     2: +18/-3
#[Out]# 15803  3ef07ecdb0d5  Na'Tosha Bard <natosha@unity3d.com>     3: +19/-7
#[Out]# 15802  7cbba3adabc7  Na'Tosha Bard <natosha@unity3d.com>    2: +72/-41
#[Out]# 15797  acb0a40fa14d  Na'Tosha Bard <natosha@unity3d.com>      1: +0/-1
#[Out]# 15796  3fe39d6d2bd8  Na'Tosha Bard <natosha@unity3d.com>   1: +22/-104
#[Out]# 15703  93c77d5b9752  Na'Tosha Bard <natosha@unity3d.com>     1: +12/-1
#[Out]# 15672  74e691b141c4  Na'Tosha Bard <natosha@unity3d.com>     1: +33/-9
#[Out]# 15516  0c7b83a057aa  Na'Tosha Bard <natosha@unity3d.com>     2: +20/-2
#[Out]# 15515  aca0f2b3c7e3  Na'Tosha Bard <natosha@unity3d.com>     2: +15/-5
#[Out]# 15460  a77ce45584ef  Na'Tosha Bard <natosha@unity3d.com>     2: +29/-9
#[Out]# 15384  bf55991af17e  Na'Tosha Bard <natosha@unity3d.com>   1: +36/-168
#[Out]# 15383  155d0f8fb7e5  Na'Tosha Bard <natosha@unity3d.com>     3: +94/-0
#[Out]# 15382  b59e6b1e0c95  Na'Tosha Bard <natosha@unity3d.com>      1: +8/-0
#[Out]# 15298  54c581d98636  Na'Tosha Bard <natosha@unity3d.com>     1: +44/-0
#[Out]# 15297  3ef434028416  Na'Tosha Bard <natosha@unity3d.com>    1: +174/-0
#[Out]# 15251  173b00827279  Na'Tosha Bard <natosha@unity3d.com>    1: +318/-0
#[Out]# 15250  f172292cd416  Na'Tosha Bard <natosha@unity3d.com>    1: +26/-13
#[Out]# 15226  2223ea21c98f  Na'Tosha Bard <natosha@unity3d.com>      1: +1/-6
#[Out]# 15225  b450a4d427ef  Na'Tosha Bard <natosha@unity3d.com>      1: +6/-1
#[Out]# 15224  7c604d8c7e83  Na'Tosha Bard <natosha@unity3d.com>   5: +57/-211
#[Out]# 15216  7678790279da  Na'Tosha Bard <natosha@unity3d.com>    1: +121/-0
#[Out]# 15215  c41078b9d0b8  Na'Tosha Bard <natosha@unity3d.com>      1: +2/-1
#[Out]# 15206  f85c76b16f27  Na'Tosha Bard <natosha@unity3d.com>      1: +1/-5), ('Nathan Jones <nathanj@insightbb.com>',               node                                author changestr
#[Out]# n                                                                 
#[Out]# 4749  7549cd526b7f  Nathan Jones <nathanj@insightbb.com>  2: +7/-1), ('Neal Becker <ndbecker2@gmail.com>',               node                             author changestr
#[Out]# n                                                              
#[Out]# 6671  8b67211d9140  Neal Becker <ndbecker2@gmail.com>  1: +1/-1
#[Out]# 6447  90ec0e8fa4d0  Neal Becker <ndbecker2@gmail.com>  1: +1/-1), ('Nicholas Riley <njriley@illinois.edu>',                node                                 author changestr
#[Out]# n                                                                   
#[Out]# 14815  abf915f537be  Nicholas Riley <njriley@illinois.edu>  1: +4/-1), ('Nicholas Riley <njriley@uiuc.edu>',               node                             author  changestr
#[Out]# n                                                               
#[Out]# 5908  838fa52abcc1  Nicholas Riley <njriley@uiuc.edu>  1: +14/-5), ('Nicolas Bareil <nico@chdir.org>',                node                           author  changestr
#[Out]# n                                                              
#[Out]# 14666  27b080aa880a  Nicolas Bareil <nico@chdir.org>  2: +11/-6), ('Nicolas Dumazet <nicdumz.commits@gmail.com>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 278 entries, 14155 to 7931
#[Out]# Data columns:
#[Out]# node         278  non-null values
#[Out]# author       278  non-null values
#[Out]# changestr    278  non-null values
#[Out]# dtypes: object(3)), ('Nicolas Venegas <nvenegas@atlassian.com>',                node                                    author    changestr
#[Out]# n                                                                         
#[Out]# 15410  2b1ec74c961f  Nicolas Venegas <nvenegas@atlassian.com>  4: +108/-25), ('Nikolaj Sjujskij <sterkrig@myopera.com>',                node                                   author changestr
#[Out]# n                                                                     
#[Out]# 16619  040ae0d48d76  Nikolaj Sjujskij <sterkrig@myopera.com>  1: +3/-2
#[Out]# 16588  462dd183bd73  Nikolaj Sjujskij <sterkrig@myopera.com>  1: +4/-1
#[Out]# 16005  384f7521c791  Nikolaj Sjujskij <sterkrig@myopera.com>  1: +2/-2
#[Out]# 15162  0d4f6e843b05  Nikolaj Sjujskij <sterkrig@myopera.com>  3: +3/-3
#[Out]# 14892  f4bc0b9e03a4  Nikolaj Sjujskij <sterkrig@myopera.com>  3: +3/-3), ('Nikolaus Schueler <nikolaus.schueler@lantiq.com>',                node                                            author   changestr
#[Out]# n                                                                                
#[Out]# 15704  2a7fa7c641d8  Nikolaus Schueler <nikolaus.schueler@lantiq.com>  3: +105/-0), ('Nils Adermann <naderman@naderman.de>',                node                                author   changestr
#[Out]# n                                                                    
#[Out]# 13754  7e6c2f58ad56  Nils Adermann <naderman@naderman.de>  2: +23/-15), ('Nils Decker <mercurial@ndecker.de>',               node                              author changestr
#[Out]# n                                                               
#[Out]# 2585  5ec2dded1bda  Nils Decker <mercurial@ndecker.de>  1: +4/-3), ('OHASHI Hideya <ohachige at gmail.com>',               node                                 author changestr
#[Out]# n                                                                  
#[Out]# 4690  ecea4de3104e  OHASHI Hideya <ohachige at gmail.com>  2: +5/-1), ('OHASHI Hideya <ohachige@gmail.com>',               node                              author    changestr
#[Out]# n                                                                  
#[Out]# 6621  e837dded56c7  OHASHI Hideya <ohachige@gmail.com>  3: +357/-14
#[Out]# 4973  0ac6b537893f  OHASHI Hideya <ohachige@gmail.com>    1: +64/-0), ('Olav Reinert <seroton10@gmail.com>',                node                              author     changestr
#[Out]# n                                                                    
#[Out]# 15865  d0f2a89c8cfa  Olav Reinert <seroton10@gmail.com>  8: +541/-541
#[Out]# 15864  ee8f5e4ce7b8  Olav Reinert <seroton10@gmail.com>    6: +77/-83
#[Out]# 15517  e6c44dbe902f  Olav Reinert <seroton10@gmail.com>      1: +3/-2
#[Out]# 15471  05e522d3f186  Olav Reinert <seroton10@gmail.com>    1: +28/-10), ('Oleg Stepanov <oleg.stepanov@jetbrains.com>',                node                                       author  changestr
#[Out]# n                                                                          
#[Out]# 13437  6169493ac3f9  Oleg Stepanov <oleg.stepanov@jetbrains.com>  2: +30/-0
#[Out]# 13018  0b30e6148ec5  Oleg Stepanov <oleg.stepanov@jetbrains.com>  2: +20/-1), ('Oli Thissen <oli@tonick.net>',                node                        author changestr
#[Out]# n                                                          
#[Out]# 13248  a38df1250945  Oli Thissen <oli@tonick.net>  1: +2/-1), ('Ollie Rutherfurd <orutherfurd@gmail.com>',                node                                    author changestr
#[Out]# n                                                                      
#[Out]# 14698  848a6658069e  Ollie Rutherfurd <orutherfurd@gmail.com>  1: +1/-1), ('Ollivier Robert <roberto@keltia.freenix.fr>',               node                                       author   changestr
#[Out]# n                                                                          
#[Out]# 1277  0bf11906df28  Ollivier Robert <roberto@keltia.freenix.fr>    1: +0/-0
#[Out]# 1137  c54d03bdf2dc  Ollivier Robert <roberto@keltia.freenix.fr>    1: +1/-1
#[Out]# 1125  a33a7a543803  Ollivier Robert <roberto@keltia.freenix.fr>    2: +2/-1
#[Out]# 1124  725204f67d92  Ollivier Robert <roberto@keltia.freenix.fr>   1: +12/-0
#[Out]# 1123  457c23af92bd  Ollivier Robert <roberto@keltia.freenix.fr>  2: +19/-22
#[Out]# 1122  fb008a1a0a32  Ollivier Robert <roberto@keltia.freenix.fr>    1: +2/-2
#[Out]# 1121  14a69c4988cd  Ollivier Robert <roberto@keltia.freenix.fr>    1: +1/-1
#[Out]# 1120  df25ee778ac2  Ollivier Robert <roberto@keltia.freenix.fr>   1: +12/-3), ('Ori Avtalion <ori@avtalion.name>',                node                            author changestr
#[Out]# n                                                              
#[Out]# 11208  4b02fc71bbba  Ori Avtalion <ori@avtalion.name>  1: +1/-1
#[Out]# 11207  aad0c319b96e  Ori Avtalion <ori@avtalion.name>  1: +1/-1
#[Out]# 8550   a33d19dcf906  Ori Avtalion <ori@avtalion.name>  1: +1/-1
#[Out]# 8548   48dd8a93d6db  Ori Avtalion <ori@avtalion.name>  1: +1/-1), ('Osku Salerma <osku@iki.fi>',               node                      author   changestr
#[Out]# n                                                         
#[Out]# 5714  3c80ecdc1bcd  Osku Salerma <osku@iki.fi>  4: +33/-19
#[Out]# 5712  ae3089cefaab  Osku Salerma <osku@iki.fi>   3: +19/-5
#[Out]# 5711  47915bf68c44  Osku Salerma <osku@iki.fi>   4: +52/-4), ('Pang Yan Han <pangyanhan@gmail.com>',                node                               author changestr
#[Out]# n                                                                 
#[Out]# 14863  5e7f03cfeeb9  Pang Yan Han <pangyanhan@gmail.com>  1: +1/-1), ('Paolo Giarrusso <p.giarrusso@gmail.com>',                node                                   author       changestr
#[Out]# n                                                                           
#[Out]# 11675  5aa9f0f0257a  Paolo Giarrusso <p.giarrusso@gmail.com>      1: +63/-71
#[Out]# 11674  0392a605bbce  Paolo Giarrusso <p.giarrusso@gmail.com>      1: +29/-46
#[Out]# 11673  bc2d0027043d  Paolo Giarrusso <p.giarrusso@gmail.com>      1: +10/-13
#[Out]# 11672  c80467f0265f  Paolo Giarrusso <p.giarrusso@gmail.com>    1: +166/-163
#[Out]# 11671  0bd15f88e8eb  Paolo Giarrusso <p.giarrusso@gmail.com>      1: +10/-44
#[Out]# 11670  11ab9982d249  Paolo Giarrusso <p.giarrusso@gmail.com>       1: +6/-12
#[Out]# 11669  03c7c1907f25  Paolo Giarrusso <p.giarrusso@gmail.com>      1: +38/-39
#[Out]# 11668  f62d06598fa9  Paolo Giarrusso <p.giarrusso@gmail.com>        1: +8/-8
#[Out]# 11667  adeab1fb16b4  Paolo Giarrusso <p.giarrusso@gmail.com>    1: +106/-129
#[Out]# 11666  218bd2a056f5  Paolo Giarrusso <p.giarrusso@gmail.com>  1: +5811/-2629
#[Out]# 11595  41ec53065611  Paolo Giarrusso <p.giarrusso@gmail.com>    1: +113/-151
#[Out]# 11594  cbf24762958a  Paolo Giarrusso <p.giarrusso@gmail.com>      1: +17/-17
#[Out]# 11593  3742046d3729  Paolo Giarrusso <p.giarrusso@gmail.com>        1: +3/-3), ('Pascal Quantin <pascal.quantin@gmail.com>',                node                                     author    changestr
#[Out]# n                                                                          
#[Out]# 15620  9926aab3d0b5  Pascal Quantin <pascal.quantin@gmail.com>     1: +2/-0
#[Out]# 14190  a4049424cb51  Pascal Quantin <pascal.quantin@gmail.com>     1: +0/-2
#[Out]# 13019  a01c52b08c5f  Pascal Quantin <pascal.quantin@gmail.com>     2: +7/-2
#[Out]# 12363  8afbf44cfe86  Pascal Quantin <pascal.quantin@gmail.com>   1: +10/-10
#[Out]# 12320  5f19416056b4  Pascal Quantin <pascal.quantin@gmail.com>    2: +39/-8
#[Out]# 12319  df5386ae41b9  Pascal Quantin <pascal.quantin@gmail.com>   2: +35/-35
#[Out]# 11650  787a5a71e524  Pascal Quantin <pascal.quantin@gmail.com>     1: +2/-0
#[Out]# 11649  eb7ddba6046a  Pascal Quantin <pascal.quantin@gmail.com>     1: +2/-0
#[Out]# 10474  601a9d67825a  Pascal Quantin <pascal.quantin@gmail.com>     1: +1/-0
#[Out]# 10269  318d58fe4ceb  Pascal Quantin <pascal.quantin@gmail.com>     1: +2/-0
#[Out]# 10236  eb0665db0c5c  Pascal Quantin <pascal.quantin@gmail.com>     1: +1/-0
#[Out]# 10118  c0fa62259d06  Pascal Quantin <pascal.quantin@gmail.com>     1: +2/-0
#[Out]# 10098  08bbed8ac9b8  Pascal Quantin <pascal.quantin@gmail.com>     1: +2/-1
#[Out]# 10092  66f3b8c95b62  Pascal Quantin <pascal.quantin@gmail.com>     1: +2/-2
#[Out]# 9957   c9194a7d7d3e  Pascal Quantin <pascal.quantin@gmail.com>  15: +22/-22
#[Out]# 9886   58bdcab55bdc  Pascal Quantin <pascal.quantin@gmail.com>     1: +1/-0
#[Out]# 9633   82a4c54d51e1  Pascal Quantin <pascal.quantin@gmail.com>     1: +1/-0
#[Out]# 8093   a0555ae394b3  Pascal Quantin <pascal.quantin@gmail.com>    2: +27/-4
#[Out]# 8092   2a4cb1d509ec  Pascal Quantin <pascal.quantin@gmail.com>     1: +1/-0
#[Out]# 8091   f614f11a96ca  Pascal Quantin <pascal.quantin@gmail.com>     1: +2/-0
#[Out]# 7851   01bd0efef1b5  Pascal Quantin <pascal.quantin@gmail.com>     1: +1/-1
#[Out]# 7798   e48cc2315fe6  Pascal Quantin <pascal.quantin@gmail.com>     1: +1/-1
#[Out]# 7686   39ae4fb8cf17  Pascal Quantin <pascal.quantin@gmail.com>     1: +2/-1
#[Out]# 7671   950484f05f16  Pascal Quantin <pascal.quantin@gmail.com>    1: +12/-1
#[Out]# 7511   bcbe8446bf2b  Pascal Quantin <pascal.quantin@gmail.com>     1: +1/-1
#[Out]# 7495   e8b818029ed6  Pascal Quantin <pascal.quantin@gmail.com>     1: +3/-1), ('Pascal Quantin <pascal.quantin@wavecom.com>',               node                                       author  changestr
#[Out]# n                                                                         
#[Out]# 7669  b0a0eb28a933  Pascal Quantin <pascal.quantin@wavecom.com>   2: +5/-0
#[Out]# 7668  8aa338cd0df3  Pascal Quantin <pascal.quantin@wavecom.com>  2: +38/-6
#[Out]# 7514  25ac72ca68f6  Pascal Quantin <pascal.quantin@wavecom.com>   2: +1/-1), ('Patrick Mezard <patrick@mezard.eu>',                node                              author     changestr
#[Out]# n                                                                    
#[Out]# 16636  6d42c797ca6e  Patrick Mezard <patrick@mezard.eu>     2: +58/-2
#[Out]# 16628  30e46d7138de  Patrick Mezard <patrick@mezard.eu>     2: +24/-4
#[Out]# 16627  2f3317d53d51  Patrick Mezard <patrick@mezard.eu>     2: +46/-6
#[Out]# 16601  592e0beee8b0  Patrick Mezard <patrick@mezard.eu>      2: +7/-5
#[Out]# 16596  9d76320d8b99  Patrick Mezard <patrick@mezard.eu>    3: +62/-14
#[Out]# 16595  435375cc0ca0  Patrick Mezard <patrick@mezard.eu>     3: +83/-9
#[Out]# 16594  b2ca2f40c9c1  Patrick Mezard <patrick@mezard.eu>     2: +55/-2
#[Out]# 16587  d36a384bec87  Patrick Mezard <patrick@mezard.eu>     2: +24/-4
#[Out]# 16581  20a9d823f242  Patrick Mezard <patrick@mezard.eu>      2: +3/-5
#[Out]# 16579  95ca6c8b38da  Patrick Mezard <patrick@mezard.eu>     2: +16/-2
#[Out]# 16578  2de6ac4ac17c  Patrick Mezard <patrick@mezard.eu>     2: +10/-0
#[Out]# 16574  ebd2ead59f1c  Patrick Mezard <patrick@mezard.eu>     2: +32/-8
#[Out]# 16555  4955e7bf085c  Patrick Mezard <patrick@mezard.eu>      1: +4/-3
#[Out]# 16554  ae2664ee0223  Patrick Mezard <patrick@mezard.eu>     2: +52/-2
#[Out]# 16553  9224cc2e99cc  Patrick Mezard <patrick@mezard.eu>     2: +25/-9
#[Out]# 16552  90ca344a7c55  Patrick Mezard <patrick@mezard.eu>     1: +12/-0
#[Out]# 16551  ebf6d38c9063  Patrick Mezard <patrick@mezard.eu>  12: +115/-13
#[Out]# 16550  0d494a38c586  Patrick Mezard <patrick@mezard.eu>     1: +39/-2
#[Out]# 16542  e596a631210e  Patrick Mezard <patrick@mezard.eu>    3: +74/-17
#[Out]# 16536  63c817ea4a70  Patrick Mezard <patrick@mezard.eu>      2: +8/-0
#[Out]# 16531  b9f51f49bf2a  Patrick Mezard <patrick@mezard.eu>    2: +40/-19
#[Out]# 16530  e37199a1f9d4  Patrick Mezard <patrick@mezard.eu>     2: +16/-9
#[Out]# 16529  3d5d204a08c7  Patrick Mezard <patrick@mezard.eu>     2: +15/-0
#[Out]# 16527  17a1f7690b49  Patrick Mezard <patrick@mezard.eu>     3: +13/-1
#[Out]# 16526  f2cc0ffb09de  Patrick Mezard <patrick@mezard.eu>      1: +3/-3
#[Out]# 16525  b12b65d2cbe4  Patrick Mezard <patrick@mezard.eu>      1: +2/-2
#[Out]# 16524  ed6a74312176  Patrick Mezard <patrick@mezard.eu>    2: +32/-10
#[Out]# 16523  727068417b95  Patrick Mezard <patrick@mezard.eu>     2: +41/-8
#[Out]# 16522  a8065323c003  Patrick Mezard <patrick@mezard.eu>     3: +27/-4
#[Out]# 16521  592701c8eac6  Patrick Mezard <patrick@mezard.eu>     2: +17/-7
#[Out]# 16513  aa252059a98f  Patrick Mezard <patrick@mezard.eu>      1: +9/-3
#[Out]# 16512  c58bdecdb800  Patrick Mezard <patrick@mezard.eu>  2: +138/-230
#[Out]# 16511  ecd2fbe68b25  Patrick Mezard <patrick@mezard.eu>     1: +34/-7
#[Out]# 16509  eab9119c5dee  Patrick Mezard <patrick@mezard.eu>    4: +21/-46
#[Out]# 16508  475de53c08f4  Patrick Mezard <patrick@mezard.eu>     3: +24/-1
#[Out]# 16507  1f020021adfa  Patrick Mezard <patrick@mezard.eu>    2: +56/-16
#[Out]# 16506  fc4e0fecf403  Patrick Mezard <patrick@mezard.eu>    2: +50/-14
#[Out]# 16492  774e2dcd0a65  Patrick Mezard <patrick@mezard.eu>      2: +7/-6
#[Out]# 16491  bfe89d65d651  Patrick Mezard <patrick@mezard.eu>    3: +40/-14
#[Out]# 16490  c8ee34917045  Patrick Mezard <patrick@mezard.eu>      1: +1/-1
#[Out]# 16484  1f75c1decdeb  Patrick Mezard <patrick@mezard.eu>     2: +15/-1
#[Out]# 16466  c53a49c345e1  Patrick Mezard <patrick@mezard.eu>    4: +218/-2
#[Out]# 16465  ad38b96c88f9  Patrick Mezard <patrick@mezard.eu>    1: +25/-21
#[Out]# 16464  0e1329d905df  Patrick Mezard <patrick@mezard.eu>      1: +8/-6
#[Out]# 16453  d2a865d4b963  Patrick Mezard <patrick@mezard.eu>      1: +2/-2
#[Out]# 16436  df347129305d  Patrick Mezard <patrick@mezard.eu>      2: +6/-2
#[Out]# 16435  8b62a77d0895  Patrick Mezard <patrick@mezard.eu>     2: +17/-1
#[Out]# 16434  e38b29937118  Patrick Mezard <patrick@mezard.eu>     1: +8/-17
#[Out]# 16433  365bb0fa73a4  Patrick Mezard <patrick@mezard.eu>     1: +21/-8
#[Out]# 16432  c85098cdd7df  Patrick Mezard <patrick@mezard.eu>     2: +23/-0
#[Out]# 16414  1a10bee86e33  Patrick Mezard <patrick@mezard.eu>    1: +13/-14
#[Out]# 16413  4c2edcd84175  Patrick Mezard <patrick@mezard.eu>    4: +43/-10
#[Out]# 16412  80b3d574881f  Patrick Mezard <patrick@mezard.eu>      1: +2/-3
#[Out]# 16411  2cbd7dd0cc1f  Patrick Mezard <patrick@mezard.eu>    3: +95/-26
#[Out]# 16410  d74099ac2ac1  Patrick Mezard <patrick@mezard.eu>     2: +71/-9
#[Out]# 16409  49ef1c382965  Patrick Mezard <patrick@mezard.eu>      2: +2/-1
#[Out]# 16408  4aa4f50c52b9  Patrick Mezard <patrick@mezard.eu>      1: +5/-1
#[Out]# 16407  17deb6bbfbab  Patrick Mezard <patrick@mezard.eu>    2: +34/-25
#[Out]# 16370  d23197e08d05  Patrick Mezard <patrick@mezard.eu>      1: +0/-1
#[Out]# 16351  0f1e621d3d3b  Patrick Mezard <patrick@mezard.eu>    2: +91/-72
#[Out]# 16350  f89284d72a61  Patrick Mezard <patrick@mezard.eu>   1: +197/-27
#[Out]# 16349  16ec050490fc  Patrick Mezard <patrick@mezard.eu>      1: +1/-3
#[Out]# 16300  81a1a00f5738  Patrick Mezard <patrick@mezard.eu>   4: +168/-32
#[Out]# 16292  af3e67354beb  Patrick Mezard <patrick@mezard.eu>    2: +148/-7
#[Out]# 16291  352053e6cd8e  Patrick Mezard <patrick@mezard.eu>    2: +34/-50
#[Out]# 16290  6863caf01daa  Patrick Mezard <patrick@mezard.eu>     2: +11/-3
#[Out]# 16289  112a70c56d6a  Patrick Mezard <patrick@mezard.eu>     1: +6/-29
#[Out]# 16288  bd12ef347680  Patrick Mezard <patrick@mezard.eu>      2: +3/-1
#[Out]# 16287  1fd352aa08fc  Patrick Mezard <patrick@mezard.eu>     3: +28/-7
#[Out]# 16286  46a96cc830c2  Patrick Mezard <patrick@mezard.eu>     2: +36/-5
#[Out]# 16282  0a73c4bd9f47  Patrick Mezard <patrick@mezard.eu>    3: +87/-17
#[Out]# 16281  9178d284b880  Patrick Mezard <patrick@mezard.eu>    2: +92/-12
#[Out]# 16280  db75321c7a0e  Patrick Mezard <patrick@mezard.eu>      1: +2/-9
#[Out]# 16279  336e61875335  Patrick Mezard <patrick@mezard.eu>     3: +23/-3
#[Out]# 16278  ef2373ea3d24  Patrick Mezard <patrick@mezard.eu>     1: +17/-0
#[Out]# 16273  5a627b49b4d9  Patrick Mezard <patrick@mezard.eu>    3: +63/-19
#[Out]# 16272  1bfc7ba8b404  Patrick Mezard <patrick@mezard.eu>     2: +26/-4
#[Out]# 16271  ec33539b61f6  Patrick Mezard <patrick@mezard.eu>     2: +38/-4
#[Out]# 16270  e04cc21b01b2  Patrick Mezard <patrick@mezard.eu>    2: +14/-38
#[Out]# 16269  4a828d3bc04a  Patrick Mezard <patrick@mezard.eu>      2: +9/-6
#[Out]# 16266  0424f3c7d7ac  Patrick Mezard <patrick@mezard.eu>      2: +3/-3
#[Out]# 16265  6acbbb0c7381  Patrick Mezard <patrick@mezard.eu>     2: +12/-5
#[Out]# 16264  184cc3c3e0a6  Patrick Mezard <patrick@mezard.eu>     2: +12/-2
#[Out]# 16263  5607d829bf17  Patrick Mezard <patrick@mezard.eu>    2: +21/-20
#[Out]# 16262  267cebac84c3  Patrick Mezard <patrick@mezard.eu>     1: +20/-1
#[Out]# 16259  461a59e2765a  Patrick Mezard <patrick@mezard.eu>    1: +16/-14
#[Out]# 16258  6e4de55a41a4  Patrick Mezard <patrick@mezard.eu>    3: +37/-28
#[Out]# 16257  8fd18eb8aab7  Patrick Mezard <patrick@mezard.eu>    7: +10/-60
#[Out]# 16242  5535e66b3016  Patrick Mezard <patrick@mezard.eu>      1: +5/-1
#[Out]# 16240  4e4c416a0b1f  Patrick Mezard <patrick@mezard.eu>     2: +28/-4
#[Out]# 16239  8dc573a9c5e5  Patrick Mezard <patrick@mezard.eu>     2: +44/-2
#[Out]# 16238  b8be450638f6  Patrick Mezard <patrick@mezard.eu>   2: +113/-33
#[Out]# 16212  c9c8c9053119  Patrick Mezard <patrick@mezard.eu>     2: +26/-4
#[Out]# 16211  c3aedd526d53  Patrick Mezard <patrick@mezard.eu>      2: +2/-2
#[Out]# 16210  03e408a122c4  Patrick Mezard <patrick@mezard.eu>      1: +3/-4
#[Out]# 16209  c3fd35f88fbb  Patrick Mezard <patrick@mezard.eu>      1: +2/-1
#[Out]# 16208  f3df7d34791e  Patrick Mezard <patrick@mezard.eu>      2: +7/-5
#[Out]# 16206  e14d7805845d  Patrick Mezard <patrick@mezard.eu>      1: +0/-1
#[Out]# 16202  16b75661828e  Patrick Mezard <patrick@mezard.eu>    2: +61/-10
#[Out]# 16201  a1b6a63f9f39  Patrick Mezard <patrick@mezard.eu>      2: +9/-1
#[Out]# 16110  9479c28a22bf  Patrick Mezard <patrick@mezard.eu>     3: +14/-2
#[Out]# 16108  6b52963ced73  Patrick Mezard <patrick@mezard.eu>      2: +3/-3
#[Out]# 16105  280e834c9d15  Patrick Mezard <patrick@mezard.eu>      1: +6/-5
#[Out]# 16104  60101427d618  Patrick Mezard <patrick@mezard.eu>     3: +27/-2
#[Out]# 16103  18743c4d1989  Patrick Mezard <patrick@mezard.eu>    1: +51/-43
#[Out]# 16100  e7746fefd1ef  Patrick Mezard <patrick@mezard.eu>      1: +1/-2
#[Out]# 16092  0e0060bf2f44  Patrick Mezard <patrick@mezard.eu>    4: +41/-22
#[Out]# 16091  b0c7525f826d  Patrick Mezard <patrick@mezard.eu>     2: +85/-8
#[Out]# 16090  9ef3a4a2c6c0  Patrick Mezard <patrick@mezard.eu>    1: +19/-13
#[Out]# 16089  ccba74472af2  Patrick Mezard <patrick@mezard.eu>    1: +11/-15
#[Out]# 16088  5de83d9ca79c  Patrick Mezard <patrick@mezard.eu>    2: +40/-15
#[Out]# 16087  d554a3dcae5a  Patrick Mezard <patrick@mezard.eu>      2: +3/-3
#[Out]# 16081  d7829b2ecf32  Patrick Mezard <patrick@mezard.eu>     3: +25/-4
#[Out]# 16080  131d1a09108a  Patrick Mezard <patrick@mezard.eu>      1: +3/-3
#[Out]# 16076  d75aa756149b  Patrick Mezard <patrick@mezard.eu>    5: +192/-8
#[Out]# 16075  ebaa0aa749e2  Patrick Mezard <patrick@mezard.eu>     3: +26/-4
#[Out]# 16073  20ad8f0512a2  Patrick Mezard <patrick@mezard.eu>    3: +25/-20
#[Out]# 16072  24df9338aa01  Patrick Mezard <patrick@mezard.eu>    1: +19/-21
#[Out]# 16069  2e8f4b82c551  Patrick Mezard <patrick@mezard.eu>     3: +54/-2), ('Patrick Mezard <pmezard@gmail.com>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 981 entries, 16220 to 3920
#[Out]# Data columns:
#[Out]# node         981  non-null values
#[Out]# author       981  non-null values
#[Out]# changestr    981  non-null values
#[Out]# dtypes: object(3)), ('Patrick Mezard <pmezard@gmail.com> ',               node                               author  changestr
#[Out]# n                                                                 
#[Out]# 5575  f0a3918abd42  Patrick Mezard <pmezard@gmail.com>   4: +17/-3), ('Paul Aurich <paul@darkrain42.org>',               node                             author changestr
#[Out]# n                                                              
#[Out]# 7875  da9f3866c637  Paul Aurich <paul@darkrain42.org>  1: +2/-1
#[Out]# 7872  d8229670710f  Paul Aurich <paul@darkrain42.org>  1: +2/-0), ('Paul Boddie <paul@boddie.org.uk>',                node                            author    changestr
#[Out]# n                                                                 
#[Out]# 16565  63f10a163017  Paul Boddie <paul@boddie.org.uk>     1: +9/-0
#[Out]# 16346  2695aaf4eb72  Paul Boddie <paul@boddie.org.uk>    3: +54/-8
#[Out]# 16314  287f76b3f502  Paul Boddie <paul@boddie.org.uk>  2: +390/-13), ('Paul Bx <pb@e-scribe.com>',               node                     author changestr
#[Out]# n                                                      
#[Out]# 4890  121f961b358c  Paul Bx <pb@e-scribe.com>  1: +1/-1), ('Paul Molodowitch <pm@stanfordalumni.org>',                node                                    author changestr
#[Out]# n                                                                      
#[Out]# 14457  96f1c1b14154  Paul Molodowitch <pm@stanfordalumni.org>  1: +6/-1
#[Out]# 12748  175fb1b193f4  Paul Molodowitch <pm@stanfordalumni.org>  1: +4/-8
#[Out]# 10597  153d688cdd06  Paul Molodowitch <pm@stanfordalumni.org>  1: +7/-0), ('Paul Moore <p.f.moore@gmail.com>',               node                            author  changestr
#[Out]# n                                                              
#[Out]# 6878  482581431dcd  Paul Moore <p.f.moore@gmail.com>  2: +13/-2
#[Out]# 6760  9865e15febd0  Paul Moore <p.f.moore@gmail.com>  1: +25/-2
#[Out]# 6759  33045179d079  Paul Moore <p.f.moore@gmail.com>  1: +47/-0
#[Out]# 6758  03a836ca6fde  Paul Moore <p.f.moore@gmail.com>   1: +6/-0
#[Out]# 6646  66e87c11447d  Paul Moore <p.f.moore@gmail.com>  2: +16/-1
#[Out]# 6612  fb502719c75c  Paul Moore <p.f.moore@gmail.com>  2: +15/-0
#[Out]# 6482  c1c202e2d45d  Paul Moore <p.f.moore@gmail.com>   1: +1/-1), ('Pavel Boldin <boldin.pavel@gmail.com>',                node                                 author   changestr
#[Out]# n                                                                     
#[Out]# 13494  3178aca36b0f  Pavel Boldin <boldin.pavel@gmail.com>  4: +24/-14), ('Pavel Volkovitskiy <int@mtx.ru>',               node                           author  changestr
#[Out]# n                                                             
#[Out]# 8003  88a2687fbd38  Pavel Volkovitskiy <int@mtx.ru>  2: +25/-3), ('Peer Stritzinger <peer@stritzinger.com>',                node                                   author changestr
#[Out]# n                                                                     
#[Out]# 15373  9a2582e325a5  Peer Stritzinger <peer@stritzinger.com>  1: +8/-9), ('Peter Arrenbrecht <peter.arrenbrecht@gmail.com>',                node                                           author       changestr
#[Out]# n                                                                                   
#[Out]# 15090  73307643a09f  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +11/-12
#[Out]# 14873  c20688b7c061  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       2: +59/-1
#[Out]# 14867  06c3667c259c  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        2: +2/-2
#[Out]# 14717  b6dc362b051c  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +2/-2
#[Out]# 14696  df902fe3d79e  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      2: +175/-1
#[Out]# 14694  e4d3370fa234  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +1/-1
#[Out]# 14624  f03c82d1f50a  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      5: +67/-55
#[Out]# 14623  e7c9fdbbb902  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +35/-19
#[Out]# 14622  bd88561afb4b  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      4: +110/-2
#[Out]# 14621  84094c0d2724  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      3: +311/-0
#[Out]# 14553  d976542986d2  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      6: +13/-13
#[Out]# 14552  3417954c42e9  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +1/-1
#[Out]# 14537  3c7907dc95ca  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +1/-1
#[Out]# 14508  ad6ad51cc0dd  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +48/-35
#[Out]# 14453  5adb52524779  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +2/-2
#[Out]# 14429  9ac479758d3b  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +6/-7
#[Out]# 14428  0c35514734e7  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +310/-0
#[Out]# 14427  afeb14a8128a  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       1: +42/-0
#[Out]# 14426  9ff996ba00b4  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +1/-1
#[Out]# 14337  a389dd285282  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       2: +18/-3
#[Out]# 14247  c5db85676c38  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +8/-4
#[Out]# 14246  30273f0c776b  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      4: +36/-13
#[Out]# 14227  e3dd3dcd6059  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      2: +282/-4
#[Out]# 14218  8aab5a82685f  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +3/-2
#[Out]# 14195  cb98fed52495  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>  15: +1005/-159
#[Out]# 14194  38184a72d793  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>    4: +289/-280
#[Out]# 14193  301725c3df9a  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>   18: +267/-261
#[Out]# 14192  8a0fca925992  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      4: +78/-38
#[Out]# 14110  72c84f24b420  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>    12: +54/-149
#[Out]# 14087  58e58406ed19  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      4: +22/-12
#[Out]# 13822  7abab875e647  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>     12: +51/-25
#[Out]# 13821  b51bf961b3cb  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>     8: +361/-16
#[Out]# 13808  fe57046e9448  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       3: +82/-1
#[Out]# 13807  e615765fdcc7  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       6: +75/-5
#[Out]# 13806  f4a85acef50c  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +3/-1
#[Out]# 13805  3458c15ab2f0  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       5: +55/-8
#[Out]# 13804  9c4e04fe267e  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       5: +83/-1
#[Out]# 13803  cc9bf81382f5  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +0/-1
#[Out]# 13726  395a84f78736  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      3: +16/-12
#[Out]# 12409  6f0d9d79111f  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       2: +15/-7
#[Out]# 12395  7340b0fa049a  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +3/-3
#[Out]# 12365  2912881c2a98  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       1: +14/-9
#[Out]# 11454  9b0406b23be0  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +9/-4
#[Out]# 11453  2ee26044d846  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +6/-2
#[Out]# 11409  7a6ac83a15b0  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       2: +62/-0
#[Out]# 11337  0f3c8a47960e  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      5: +470/-1
#[Out]# 11336  3dfbe26cfded  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       2: +65/-1
#[Out]# 11335  3201ff1459dd  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      2: +476/-0
#[Out]# 11319  9d1cf337a78d  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +5/-5
#[Out]# 11242  0d09f2244805  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       3: +17/-1
#[Out]# 10983  dc097666de01  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +11/-29
#[Out]# 10695  29a83fb8c067  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       2: +81/-0
#[Out]# 10688  196908117c27  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       3: +30/-0
#[Out]# 10407  2d30d66a89ad  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        2: +2/-2
#[Out]# 10004  6e8a16dd3e30  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +6/-0
#[Out]# 9821   7d2e9121ef4f  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      2: +137/-0
#[Out]# 9820   0b999aec64e8  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      4: +55/-18
#[Out]# 9631   1c34fca5d785  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       1: +12/-8
#[Out]# 9150   0d3c1aa9d5de  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +5/-5
#[Out]# 8842   acd03a6e2426  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      2: +19/-29
#[Out]# 8841   94ac080e7af9  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +24/-24
#[Out]# 8840   d9acbe7b0049  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      2: +44/-27
#[Out]# 8839   bbfa21b6f18a  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +12/-12
#[Out]# 8838   e89b05308d69  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +13/-12
#[Out]# 8837   d8e3a98018cb  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      2: +13/-11
#[Out]# 8836   11ff34956ee7  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      2: +37/-37
#[Out]# 8835   ec5483efc31f  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +2/-5
#[Out]# 8639   7aa1526d4fc5  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +1/-1
#[Out]# 8638   aaaf4af1c173  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       2: +39/-0
#[Out]# 8405   850b5a7c210d  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        2: +5/-1
#[Out]# 8404   59160ca338f7  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +6/-6
#[Out]# 8403   7e5cbb09515b  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +5/-5
#[Out]# 8402   27bffd81d265  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +5/-4
#[Out]# 8401   beae42f3d93b  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       8: +7/-11
#[Out]# 8400   4b798b100c32  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        2: +7/-7
#[Out]# 8236   21cf74ff2deb  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        2: +3/-3
#[Out]# 7926   eba7f12b0c51  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>    5: +117/-119
#[Out]# 7925   53c72ba36c2b  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        2: +2/-2
#[Out]# 7924   553aa0cbeab6  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>     15: +14/-25
#[Out]# 7923   d812029cda85  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>     13: +27/-28
#[Out]# 7922   4a4c7f6a5912  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>     21: +26/-29
#[Out]# 7852   2b901f9b37aa  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +1/-1
#[Out]# 7598   e9d3a11eacad  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        3: +8/-1
#[Out]# 7497   11a4eb81fb4f  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       3: +40/-0
#[Out]# 7383   b501c7f3c2ad  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       3: +26/-1
#[Out]# 7371   7bc62ebe7693  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>     1: +73/-114
#[Out]# 7360   b0fa5dbd9cdd  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        2: +4/-4
#[Out]# 7359   3c2ed7c2dcb4  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      2: +535/-0
#[Out]# 7358   6eb38b2dca6c  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +8/-8
#[Out]# 7357   eee5b7b9c5d2  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +1/-0
#[Out]# 7356   fac7e9070a19  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +0/-1
#[Out]# 7354   982b55ec80be  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +29/-22
#[Out]# 7353   6c336e7dc145  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +14/-10
#[Out]# 7326   f9985108d4e4  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +53/-29
#[Out]# 7325   3a2cbf68e2f1  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +9/-9
#[Out]# 7324   1c9f7aa7c8a5  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       1: +9/-10
#[Out]# 7323   b05834d6be3c  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +3/-3
#[Out]# 7322   e016b65fd284  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +13/-14
#[Out]# 7321   8dca507e56ce  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       3: +11/-1
#[Out]# 6735   602f7c1ab954  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        3: +3/-5
#[Out]# 6517   ef14c773b3d6  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       1: +10/-8
#[Out]# 6410   c1b47c0fd2b6  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      7: +49/-24
#[Out]# 6310   1a13a5bbbbc1  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      1: +35/-22
#[Out]# 6219   d43c94414ba1  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       2: +14/-3
#[Out]# 6208   c88b9e597588  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +8/-4
#[Out]# 6205   b193a6e59131  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       2: +67/-0
#[Out]# 6166   f857eac30cd5  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +3/-0
#[Out]# 6164   0c2b443fb3c3  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +2/-0
#[Out]# 6129   3d666e8e6398  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        2: +5/-3
#[Out]# 6128   b3286a92f4bc  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       2: +20/-0
#[Out]# 5834   4107e823dc2c  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>     3: +484/-16
#[Out]# 5718   da72b4d24797  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>      6: +193/-2
#[Out]# 5717   99fdef2e6793  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>       2: +36/-0
#[Out]# 5699   1f044b04fa0a  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +1/-1
#[Out]# 5585   bb417470d62a  Peter Arrenbrecht <peter.arrenbrecht@gmail.com>        1: +9/-0), ('Peter Ingebretson <pingebre@yahoo.com>',               node                                  author changestr
#[Out]# n                                                                   
#[Out]# 9123  6ea653272c09  Peter Ingebretson <pingebre@yahoo.com>  1: +4/-4), ('Peter Meerwald <pmeerw@pmeerw.net>',               node                              author changestr
#[Out]# n                                                               
#[Out]# 4850  942c0827dc5b  Peter Meerwald <pmeerw@pmeerw.net>  1: +1/-1), ('Peter Ruibal <peter.ruibal@intel.com>',               node                                 author   changestr
#[Out]# n                                                                    
#[Out]# 7033  8fee8ff13d37  Peter Ruibal <peter.ruibal@intel.com>  7: +14/-14), ('Peter van Dijk <mercurial-bugs@selenic.com>',               node                                       author changestr
#[Out]# n                                                                        
#[Out]# 7771  fd3e5ff53a31  Peter van Dijk <mercurial-bugs@selenic.com>  1: +1/-0), ('Peter van Dijk <peter@dataloss.nl>',               node                              author        changestr
#[Out]# n                                                                      
#[Out]# 1931  819a2508f2c6  Peter van Dijk <peter@dataloss.nl>      7: +106/-49
#[Out]# 1930  70be74899338  Peter van Dijk <peter@dataloss.nl>  51: +2657/-1057
#[Out]# 1928  50e1c90b0fcf  Peter van Dijk <peter@dataloss.nl>         1: +7/-0
#[Out]# 1927  397b62d5dd13  Peter van Dijk <peter@dataloss.nl>         2: +2/-2
#[Out]# 1926  ba198d17eea9  Peter van Dijk <peter@dataloss.nl>         5: +7/-7
#[Out]# 1925  c71420b186b0  Peter van Dijk <peter@dataloss.nl>         3: +7/-4
#[Out]# 1924  46fb38ef9a91  Peter van Dijk <peter@dataloss.nl>        1: +25/-0
#[Out]# 1923  7d83a351a936  Peter van Dijk <peter@dataloss.nl>        6: +10/-7
#[Out]# 1768  f79afc26ae3b  Peter van Dijk <peter@dataloss.nl>         1: +3/-0
#[Out]# 1767  adbc392dfd9e  Peter van Dijk <peter@dataloss.nl>         2: +5/-3
#[Out]# 1766  93f54a2b3864  Peter van Dijk <peter@dataloss.nl>        3: +14/-0
#[Out]# 1695  4b1e0dc913bf  Peter van Dijk <peter@dataloss.nl>         1: +1/-1
#[Out]# 1652  f910437af806  Peter van Dijk <peter@dataloss.nl>         1: +1/-1
#[Out]# 1650  f2ebd5251e88  Peter van Dijk <peter@dataloss.nl>      21: +89/-86), ('Petr Kodl <petrkodl@gmail.com>',               node                          author   changestr
#[Out]# n                                                             
#[Out]# 7126  619ebf82cef2  Petr Kodl <petrkodl@gmail.com>  2: +51/-11
#[Out]# 7080  852f39691a0a  Petr Kodl <petrkodl@gmail.com>    1: +2/-2
#[Out]# 7079  57377fa7eda2  Petr Kodl <petrkodl@gmail.com>   1: +11/-8
#[Out]# 7071  6a76cf980999  Petr Kodl <petrkodl@gmail.com>    1: +5/-8
#[Out]# 7068  2c1f18b88b6a  Petr Kodl <petrkodl@gmail.com>  2: +176/-0), ('Petr Mazanec <petr.mazanec@tiscali.cz>',               node                                  author changestr
#[Out]# n                                                                   
#[Out]# 1648  80640ef93aec  Petr Mazanec <petr.mazanec@tiscali.cz>  1: +1/-1), ('Pierre-Yves David <pierre-yves.david@ens-lyon.org>',                node                                             author     changestr
#[Out]# n                                                                                   
#[Out]# 16532  9eba72cdde34  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +1/-1
#[Out]# 16216  db4b0532dbf2  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +8/-7
#[Out]# 16163  9518cb55c822  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +19/-2
#[Out]# 15968  bf87b6b95ce5  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +1/-1
#[Out]# 15956  5653f2d166ea  Pierre-Yves David <pierre-yves.david@ens-lyon.org    3: +58/-25
#[Out]# 15951  bd84fc0b5f64  Pierre-Yves David <pierre-yves.david@ens-lyon.org      2: +2/-2
#[Out]# 15927  2eec74d7ce95  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +18/-8
#[Out]# 15907  51fc43253a52  Pierre-Yves David <pierre-yves.david@ens-lyon.org    5: +114/-1
#[Out]# 15906  aad565319fa3  Pierre-Yves David <pierre-yves.david@ens-lyon.org     1: +14/-0
#[Out]# 15893  eb6867b98223  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +3/-5
#[Out]# 15892  592b3d1742a1  Pierre-Yves David <pierre-yves.david@ens-lyon.org    3: +39/-72
#[Out]# 15891  249d3420ec9c  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +49/-4
#[Out]# 15890  e234eda20984  Pierre-Yves David <pierre-yves.david@ens-lyon.org      2: +7/-4
#[Out]# 15889  816209eaf963  Pierre-Yves David <pierre-yves.david@ens-lyon.org    2: +131/-4
#[Out]# 15844  7299e09a85a2  Pierre-Yves David <pierre-yves.david@ens-lyon.org    3: +67/-22
#[Out]# 15843  cd956049fc14  Pierre-Yves David <pierre-yves.david@ens-lyon.org    5: +74/-27
#[Out]# 15842  926c9ee8d4be  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +2/-2
#[Out]# 15841  fa15869bf95c  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +3/-6
#[Out]# 15831  94a4748db392  Pierre-Yves David <pierre-yves.david@ens-lyon.org  1: +503/-252
#[Out]# 15830  a1f818a2b50d  Pierre-Yves David <pierre-yves.david@ens-lyon.org      3: +8/-3
#[Out]# 15829  d523b6e7ad26  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +2/-0
#[Out]# 15828  e3ee8bf5d0cc  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +1/-0
#[Out]# 15827  2673006f7989  Pierre-Yves David <pierre-yves.david@ens-lyon.org    3: +68/-25
#[Out]# 15826  33ca11b010e2  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +38/-1
#[Out]# 15825  57241845a4bb  Pierre-Yves David <pierre-yves.david@ens-lyon.org    3: +14/-13
#[Out]# 15770  65df60a3f96b  Pierre-Yves David <pierre-yves.david@ens-lyon.org    16: +62/-2
#[Out]# 15769  60344b83e442  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +21/-0
#[Out]# 15768  62aa9305399d  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +23/-2
#[Out]# 15765  8edd9f2c7b57  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +1/-1
#[Out]# 15764  306e84e8bbe9  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +1/-1
#[Out]# 15744  cff25e4b37d2  Pierre-Yves David <pierre-yves.david@ens-lyon.org    5: +131/-5
#[Out]# 15743  06b8b74720d6  Pierre-Yves David <pierre-yves.david@ens-lyon.org     1: +52/-1
#[Out]# 15738  dc3eefe0c80e  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +9/-0
#[Out]# 15737  ebaefd8c6028  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +9/-2
#[Out]# 15736  e34f4d1f0dbb  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +3/-0
#[Out]# 15735  8857e150bec0  Pierre-Yves David <pierre-yves.david@ens-lyon.org      2: +9/-0
#[Out]# 15734  2a48422e27f6  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +2/-0
#[Out]# 15730  0cb45fef99ba  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +1/-1
#[Out]# 15728  1e4e49c58b94  Pierre-Yves David <pierre-yves.david@ens-lyon.org     1: +33/-4
#[Out]# 15708  7fba5a245acc  Pierre-Yves David <pierre-yves.david@ens-lyon.org   4: +131/-17
#[Out]# 15699  ca7c4254a21a  Pierre-Yves David <pierre-yves.david@ens-lyon.org     1: +27/-0
#[Out]# 15656  a348739da8f0  Pierre-Yves David <pierre-yves.david@ens-lyon.org     4: +7/-15
#[Out]# 15655  9df9444e96ec  Pierre-Yves David <pierre-yves.david@ens-lyon.org    1: +14/-11
#[Out]# 15654  926a06f7a353  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +16/-0
#[Out]# 15593  1eefa4451c56  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +31/-0
#[Out]# 15592  fa47291b3f1f  Pierre-Yves David <pierre-yves.david@ens-lyon.org    3: +68/-26
#[Out]# 15591  a44446ff9ad8  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +63/-3
#[Out]# 15590  9ae766f2f452  Pierre-Yves David <pierre-yves.david@ens-lyon.org     5: +11/-1
#[Out]# 15589  a667c89e49b3  Pierre-Yves David <pierre-yves.david@ens-lyon.org     1: +21/-2
#[Out]# 15588  0b7ce2f739fb  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +1/-1
#[Out]# 15587  7d4f364c980b  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +2/-2
#[Out]# 15574  abcaaf51d568  Pierre-Yves David <pierre-yves.david@ens-lyon.org     3: +25/-4
#[Out]# 15573  c6f87bdab2a1  Pierre-Yves David <pierre-yves.david@ens-lyon.org     5: +21/-2
#[Out]# 15572  5a7dde5adec8  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +29/-0
#[Out]# 15571  cff509500a24  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +5/-0
#[Out]# 15549  ea5b346024e1  Pierre-Yves David <pierre-yves.david@ens-lyon.org     1: +10/-0
#[Out]# 15548  042e11c4e416  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +5/-0
#[Out]# 15546  e80d0d3198f0  Pierre-Yves David <pierre-yves.david@ens-lyon.org     1: +12/-0
#[Out]# 15544  cf729af26963  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +33/-1
#[Out]# 15543  5261140d9322  Pierre-Yves David <pierre-yves.david@ens-lyon.org     1: +11/-0
#[Out]# 15518  e43c140eb08f  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +4/-1
#[Out]# 15270  6cb6064f1d50  Pierre-Yves David <pierre-yves.david@ens-lyon.org    4: +269/-8
#[Out]# 15267  3bfdfefea2fc  Pierre-Yves David <pierre-yves.david@ens-lyon.org    4: +59/-63
#[Out]# 14751  1a9256cdf10f  Pierre-Yves David <pierre-yves.david@ens-lyon.org      2: +5/-1
#[Out]# 14738  72e4fcb43227  Pierre-Yves David <pierre-yves.david@ens-lyon.org     4: +14/-6
#[Out]# 14645  e4cfdff6d3f4  Pierre-Yves David <pierre-yves.david@ens-lyon.org     3: +22/-1
#[Out]# 14644  f3a40fd7008c  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +2/-0
#[Out]# 14643  7e295dd10d40  Pierre-Yves David <pierre-yves.david@ens-lyon.org      1: +2/-0
#[Out]# 14055  d7b4d421b56c  Pierre-Yves David <pierre-yves.david@ens-lyon.org     2: +50/-2
#[Out]# 10643  bdb60057f905  Pierre-Yves David <pierre-yves.david@ens-lyon.org      2: +2/-5), ('Pierre-Yves David <pierre-yves.david@logilab.fr>',                node                                            author     changestr
#[Out]# n                                                                                  
#[Out]# 16611  0128cdb846d9  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +3/-4
#[Out]# 16535  39d1f83eb05d  Pierre-Yves David <pierre-yves.david@logilab.fr>     5: +69/-3
#[Out]# 16114  40cc20042fb4  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +33/-0
#[Out]# 16048  140b6282ac79  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +38/-1
#[Out]# 16030  308406677e9d  Pierre-Yves David <pierre-yves.david@logilab.fr>     3: +19/-3
#[Out]# 16029  ee1c8385e5b0  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +24/-1
#[Out]# 16028  922c0e9b40be  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +21/-2
#[Out]# 16027  29ea059be33c  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +32/-8
#[Out]# 16026  31c02546e6de  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +31/-2
#[Out]# 16025  6697498bdd83  Pierre-Yves David <pierre-yves.david@logilab.fr>      2: +2/-0
#[Out]# 16024  7c967c4a6144  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +5/-2
#[Out]# 15986  ba959f6e10f8  Pierre-Yves David <pierre-yves.david@logilab.fr>      2: +5/-4
#[Out]# 15955  5a14f48d6b9a  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +1/-2
#[Out]# 15954  b345f851d056  Pierre-Yves David <pierre-yves.david@logilab.fr>     1: +10/-3
#[Out]# 15953  52dc2b33d0be  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +4/-4
#[Out]# 15952  ec8a9e06cf05  Pierre-Yves David <pierre-yves.david@logilab.fr>    4: +41/-21
#[Out]# 15933  b8696a6676be  Pierre-Yves David <pierre-yves.david@logilab.fr>    2: +11/-13
#[Out]# 15932  4154338f0bc0  Pierre-Yves David <pierre-yves.david@logilab.fr>  3: +136/-148
#[Out]# 15931  44b5de2d1876  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +1/-1
#[Out]# 15928  3a51eb88046a  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +9/-0
#[Out]# 15926  f94513971767  Pierre-Yves David <pierre-yves.david@logilab.fr>     4: +39/-9
#[Out]# 15922  23921c17299a  Pierre-Yves David <pierre-yves.david@logilab.fr>      3: +7/-1
#[Out]# 15921  92e455f2866c  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +8/-0
#[Out]# 15920  885e0c71db9b  Pierre-Yves David <pierre-yves.david@logilab.fr>     1: +17/-5
#[Out]# 15919  69e792cf7851  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +36/-0
#[Out]# 15888  2072e4031994  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +15/-0
#[Out]# 15836  8ed112ed774a  Pierre-Yves David <pierre-yves.david@logilab.fr>    8: +178/-1
#[Out]# 15731  21eb048edc19  Pierre-Yves David <pierre-yves.david@logilab.fr>     1: +15/-0
#[Out]# 15729  1b9dcf2eb011  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +7/-0
#[Out]# 15702  ca6accdad79c  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +3/-0
#[Out]# 15701  e69a3cdad37e  Pierre-Yves David <pierre-yves.david@logilab.fr>    4: +255/-4
#[Out]# 15700  5b26667fc4d3  Pierre-Yves David <pierre-yves.david@logilab.fr>    5: +159/-2
#[Out]# 15698  79cc89de5be1  Pierre-Yves David <pierre-yves.david@logilab.fr>     4: +47/-2
#[Out]# 15697  ce193147f492  Pierre-Yves David <pierre-yves.david@logilab.fr>    1: +43/-42
#[Out]# 15696  218ec96c45d7  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +32/-2
#[Out]# 15547  405ca90df2b1  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +2/-0
#[Out]# 15326  8ae2900d6d9b  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +3/-2
#[Out]# 15292  7fa471248185  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +3/-2
#[Out]# 15232  5d9a5b919863  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +2/-1
#[Out]# 15142  81f76098211e  Pierre-Yves David <pierre-yves.david@logilab.fr>     4: +52/-5
#[Out]# 14934  5097d8b5078c  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +11/-0
#[Out]# 14933  677339529a53  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +11/-0
#[Out]# 13507  375ba42f3cda  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +29/-4
#[Out]# 10886  fbcccf9ec58f  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +5/-0
#[Out]# 10885  3be9ae49b628  Pierre-Yves David <pierre-yves.david@logilab.fr>     1: +35/-8
#[Out]# 10884  f18c37fd624f  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +3/-3
#[Out]# 10883  b1f4fcef99b3  Pierre-Yves David <pierre-yves.david@logilab.fr>    1: +31/-27
#[Out]# 10882  5f92bde72eef  Pierre-Yves David <pierre-yves.david@logilab.fr>    1: +32/-31
#[Out]# 10881  83dce0f817f4  Pierre-Yves David <pierre-yves.david@logilab.fr>     2: +26/-0
#[Out]# 10559  9134725caf1d  Pierre-Yves David <pierre-yves.david@logilab.fr>      1: +1/-0), ('Pradeepkumar Gayam <in3xes@gmail.com>',                node                                 author     changestr
#[Out]# n                                                                       
#[Out]# 12846  4b334f8c941b  Pradeepkumar Gayam <in3xes@gmail.com>     6: +4/-12
#[Out]# 12102  27649cf258e3  Pradeepkumar Gayam <in3xes@gmail.com>    3: +51/-52
#[Out]# 12101  56d9b73487ff  Pradeepkumar Gayam <in3xes@gmail.com>   3: +90/-100
#[Out]# 12100  518b90d66fad  Pradeepkumar Gayam <in3xes@gmail.com>    3: +27/-29
#[Out]# 12099  c443e95d295b  Pradeepkumar Gayam <in3xes@gmail.com>  3: +143/-145
#[Out]# 12098  39fb1e4c079f  Pradeepkumar Gayam <in3xes@gmail.com>    3: +69/-73
#[Out]# 12097  ef4a1ffbf519  Pradeepkumar Gayam <in3xes@gmail.com>    3: +29/-32
#[Out]# 12096  db2a291e25e9  Pradeepkumar Gayam <in3xes@gmail.com>    3: +20/-21
#[Out]# 12095  b28fc3b3efd6  Pradeepkumar Gayam <in3xes@gmail.com>    3: +53/-55
#[Out]# 12094  21884b433c51  Pradeepkumar Gayam <in3xes@gmail.com>  3: +165/-172
#[Out]# 12093  ccd581c66284  Pradeepkumar Gayam <in3xes@gmail.com>  3: +101/-113
#[Out]# 12092  b773ca489fd3  Pradeepkumar Gayam <in3xes@gmail.com>    3: +65/-68
#[Out]# 12091  b708cadc6e8f  Pradeepkumar Gayam <in3xes@gmail.com>    3: +63/-65
#[Out]# 12090  71105dd7d4df  Pradeepkumar Gayam <in3xes@gmail.com>   3: +84/-103
#[Out]# 12066  106311e7740f  Pradeepkumar Gayam <in3xes@gmail.com>  3: +103/-122
#[Out]# 12060  cf858e76e992  Pradeepkumar Gayam <in3xes@gmail.com>      1: +2/-0
#[Out]# 12059  293afcfb66a8  Pradeepkumar Gayam <in3xes@gmail.com>     1: +57/-0
#[Out]# 12058  01778673aab7  Pradeepkumar Gayam <in3xes@gmail.com>      1: +5/-1
#[Out]# 12057  6051db1327f8  Pradeepkumar Gayam <in3xes@gmail.com>      1: +7/-2
#[Out]# 12056  12547cedc264  Pradeepkumar Gayam <in3xes@gmail.com>      1: +9/-7
#[Out]# 12055  1839a7518b0d  Pradeepkumar Gayam <in3xes@gmail.com>     1: +22/-0
#[Out]# 12054  b69899dbad40  Pradeepkumar Gayam <in3xes@gmail.com>      1: +6/-1
#[Out]# 12051  487152f29db2  Pradeepkumar Gayam <in3xes@gmail.com>  3: +250/-237
#[Out]# 12050  be74ba87acaf  Pradeepkumar Gayam <in3xes@gmail.com>    3: +23/-25
#[Out]# 12049  3e59059b2785  Pradeepkumar Gayam <in3xes@gmail.com>  3: +321/-326
#[Out]# 12048  650d8a023249  Pradeepkumar Gayam <in3xes@gmail.com>    3: +40/-38
#[Out]# 12047  d0a7e700b5d1  Pradeepkumar Gayam <in3xes@gmail.com>  3: +123/-133
#[Out]# 12046  67fb33eb3add  Pradeepkumar Gayam <in3xes@gmail.com>    3: +21/-21
#[Out]# 12045  f21ecd091970  Pradeepkumar Gayam <in3xes@gmail.com>    3: +33/-39
#[Out]# 12044  b03cf2349a80  Pradeepkumar Gayam <in3xes@gmail.com>    3: +23/-28
#[Out]# 11888  bf49d48e4602  Pradeepkumar Gayam <in3xes@gmail.com>     1: +11/-0
#[Out]# 11887  ff33f937a7da  Pradeepkumar Gayam <in3xes@gmail.com>      1: +4/-2
#[Out]# 11300  3e46d76eaabf  Pradeepkumar Gayam <in3xes@gmail.com>      1: +1/-1), ('Radomir Dopieralski <sheep@stxnext.pl>',                node                                  author  changestr
#[Out]# n                                                                     
#[Out]# 13766  ee349e228835  Radomir Dopieralski <sheep@stxnext.pl>  2: +51/-5), ('Radoslaw "AstralStorm" Szkodzinski <astralstorm@gorzow.mm.pl>',              node                                             author changestr
#[Out]# n                                                                             
#[Out]# 666  0100a43788ca  Radoslaw "AstralStorm" Szkodzinski <astralstorm@g  1: +3/-1
#[Out]# 665  40fd5722c669  Radoslaw "AstralStorm" Szkodzinski <astralstorm@g  1: +2/-0
#[Out]# 664  e1fbc1982372  Radoslaw "AstralStorm" Szkodzinski <astralstorm@g  1: +5/-3
#[Out]# 663  562404de61fb  Radoslaw "AstralStorm" Szkodzinski <astralstorm@g  1: +3/-3
#[Out]# 662  b55a78595ef6  Radoslaw "AstralStorm" Szkodzinski <astralstorm@g  1: +3/-0), ('Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>',               node                                           author   changestr
#[Out]# n                                                                              
#[Out]# 2051  6a03cff2b0f5  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>    1: +9/-4
#[Out]# 1798  d610fe0e6893  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>    1: +2/-2
#[Out]# 1774  ac7b91bcbd8d  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>   1: +14/-1
#[Out]# 1773  aae93c3bffb4  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>    1: +5/-1
#[Out]# 1772  b1a7fd503a29  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>   1: +8/-20
#[Out]# 1771  e22bbca2e82b  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>  1: +13/-10
#[Out]# 1770  4eea6a747c27  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>  1: +36/-35
#[Out]# 1701  4ba8fe499df2  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>  1: +30/-33
#[Out]# 1700  e2f91e0acbb8  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>  1: +46/-30
#[Out]# 1699  83e8cd97b9f9  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>  1: +22/-11
#[Out]# 1505  27f08094cfe0  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>    1: +4/-1
#[Out]# 631   a287f6cd9c6b  Radoslaw Szkodzinski <astralstorm@gorzow.mm.pl>   3: +11/-8), ('Rafael Villar Burke <pachi@mmn-arquitectos.com>',               node                                           author   changestr
#[Out]# n                                                                              
#[Out]# 2615  b075216da118  Rafael Villar Burke <pachi@mmn-arquitectos.com>  1: +123/-0), ('Rafael Villar Burke <pachi@rvburke.com>',               node                                   author changestr
#[Out]# n                                                                    
#[Out]# 5421  6d1bd20ae14d  Rafael Villar Burke <pachi@rvburke.com>  1: +7/-3), ('Ralf Schmitt <schmir@gmail.com>',               node                           author changestr
#[Out]# n                                                            
#[Out]# 6237  4a85a9077136  Ralf Schmitt <schmir@gmail.com>  1: +1/-2), ('Raoul Bhatia [IPAX] <r.bhatia@ipax.at>',               node                                  author   changestr
#[Out]# n                                                                     
#[Out]# 9587  3b93032516b3  Raoul Bhatia [IPAX] <r.bhatia@ipax.at>  6: +14/-14), ('Raphael Marmier <raphael@marmier.net>',               node                                 author changestr
#[Out]# n                                                                  
#[Out]# 2550  45235e492cc6  Raphael Marmier <raphael@marmier.net>  1: +4/-2), ('Regis Desgroppes <regis.desgroppes@nokia.com>',                node                                         author changestr
#[Out]# n                                                                           
#[Out]# 14501  278a4e0fdfed  Regis Desgroppes <regis.desgroppes@nokia.com>  1: +4/-2
#[Out]# 13667  90ef40bf97e3  Regis Desgroppes <regis.desgroppes@nokia.com>  1: +4/-2), ('Remy Roy <remyroy@remyroy.com>',               node                          author changestr
#[Out]# n                                                           
#[Out]# 6514  d2375bbee6d4  Remy Roy <remyroy@remyroy.com>  1: +2/-1), ('Renato Cunha <renato@renatocunha.com>',                node                                 author changestr
#[Out]# n                                                                   
#[Out]# 15474  cfc15cbecc5e  Renato Cunha <renato@renatocunha.com>  1: +8/-2), ('Renato Cunha <renatoc@gmail.com>',                node                            author   changestr
#[Out]# n                                                                
#[Out]# 14882  02734d2baa79  Renato Cunha <renatoc@gmail.com>    1: +9/-7
#[Out]# 12075  626fe5c99231  Renato Cunha <renatoc@gmail.com>  1: +108/-0
#[Out]# 12074  88d4911930bf  Renato Cunha <renatoc@gmail.com>  1: +374/-0
#[Out]# 12073  59ec12093261  Renato Cunha <renatoc@gmail.com>    1: +8/-0
#[Out]# 12016  e3526634d5a3  Renato Cunha <renatoc@gmail.com>   1: +19/-2
#[Out]# 12014  8bb1481cf08f  Renato Cunha <renatoc@gmail.com>    1: +7/-0
#[Out]# 11921  16723af520b0  Renato Cunha <renatoc@gmail.com>    1: +1/-0
#[Out]# 11920  69e0bcf36961  Renato Cunha <renatoc@gmail.com>    1: +1/-1
#[Out]# 11913  e627fef94604  Renato Cunha <renatoc@gmail.com>   1: +63/-0
#[Out]# 11912  37a70a784397  Renato Cunha <renatoc@gmail.com>   2: +66/-0
#[Out]# 11911  40d5633889bb  Renato Cunha <renatoc@gmail.com>   1: +96/-0
#[Out]# 11781  f8576644a222  Renato Cunha <renatoc@gmail.com>    1: +1/-0
#[Out]# 11780  d5d4e6a30613  Renato Cunha <renatoc@gmail.com>    1: +4/-0
#[Out]# 11779  34cc8b84407f  Renato Cunha <renatoc@gmail.com>  5: +14/-14
#[Out]# 11778  4d11fde55cc5  Renato Cunha <renatoc@gmail.com>    1: +6/-2
#[Out]# 11777  7546d4a272c8  Renato Cunha <renatoc@gmail.com>    1: +3/-1
#[Out]# 11776  9bbfeba33aa3  Renato Cunha <renatoc@gmail.com>    1: +2/-1
#[Out]# 11764  935c83ce9172  Renato Cunha <renatoc@gmail.com>   1: +33/-2
#[Out]# 11763  dd2f356e1f6f  Renato Cunha <renatoc@gmail.com>  1: +48/-30
#[Out]# 11762  36a6aeb679da  Renato Cunha <renatoc@gmail.com>    1: +1/-1
#[Out]# 11761  09cb56b760b4  Renato Cunha <renatoc@gmail.com>   1: +41/-0
#[Out]# 11760  9777a3b19efe  Renato Cunha <renatoc@gmail.com>    1: +1/-0
#[Out]# 11759  5be8760d2fb3  Renato Cunha <renatoc@gmail.com>    1: +2/-1
#[Out]# 11758  f3732ab1149f  Renato Cunha <renatoc@gmail.com>   1: +13/-2
#[Out]# 11750  deb5d02ae91c  Renato Cunha <renatoc@gmail.com>    1: +2/-1
#[Out]# 11749  b782a7eb9037  Renato Cunha <renatoc@gmail.com>    1: +3/-3
#[Out]# 11748  324cd681fa47  Renato Cunha <renatoc@gmail.com>    1: +2/-1
#[Out]# 11747  8fa85378c527  Renato Cunha <renatoc@gmail.com>    1: +2/-3
#[Out]# 11746  f5a8d85df06a  Renato Cunha <renatoc@gmail.com>    1: +3/-3
#[Out]# 11521  db9d16233787  Renato Cunha <renatoc@gmail.com>   2: +16/-1
#[Out]# 11499  9d905b9769af  Renato Cunha <renatoc@gmail.com>    1: +1/-1
#[Out]# 11364  0044193a1c45  Renato Cunha <renatoc@gmail.com>   1: +23/-4
#[Out]# 11363  f50103035c38  Renato Cunha <renatoc@gmail.com>  1: +39/-10
#[Out]# 11362  f42ef9493fa9  Renato Cunha <renatoc@gmail.com>   1: +24/-5
#[Out]# 11361  3de3d670d2b6  Renato Cunha <renatoc@gmail.com>   1: +30/-8
#[Out]# 11360  2ac98313b26c  Renato Cunha <renatoc@gmail.com>   1: +29/-3
#[Out]# 11359  4eaacccbb2ca  Renato Cunha <renatoc@gmail.com>   1: +29/-4
#[Out]# 11358  4494fb02d549  Renato Cunha <renatoc@gmail.com>   1: +63/-0
#[Out]# 11340  938fefb57db5  Renato Cunha <renatoc@gmail.com>    1: +3/-1), ('Richard Hopkins',                node           author changestr
#[Out]# n                                             
#[Out]# 12930  0d4fb319974b  Richard Hopkins  2: +2/-2), ('Richard Lowe <richlowe@richlowe.net>',               node                                author changestr
#[Out]# n                                                                 
#[Out]# 5946  2296ecefa223  Richard Lowe <richlowe@richlowe.net>  1: +1/-1), ('Richard Quirk <richard.quirk@gmail.com>',               node                                   author  changestr
#[Out]# n                                                                     
#[Out]# 8282  e3d3dad805f9  Richard Quirk <richard.quirk@gmail.com>  3: +52/-6), ('Robert Bachmann <rbach@rbach.priv.at>',               node                                 author     changestr
#[Out]# n                                                                      
#[Out]# 5302  b962f82cfd61  Robert Bachmann <rbach@rbach.priv.at>      2: +4/-4
#[Out]# 5301  46c5e1ee8aaa  Robert Bachmann <rbach@rbach.priv.at>  35: +144/-13), ('Robert Bachmann <rbachm@gmail.com>',                node                              author   changestr
#[Out]# n                                                                  
#[Out]# 10221  3acfb69a4729  Robert Bachmann <rbachm@gmail.com>   1: +41/-0
#[Out]# 10220  48653dea23dd  Robert Bachmann <rbachm@gmail.com>  3: +269/-1
#[Out]# 10219  182416227722  Robert Bachmann <rbachm@gmail.com>    1: +2/-0
#[Out]# 10214  000546ec7ced  Robert Bachmann <rbachm@gmail.com>   1: +17/-0
#[Out]# 10213  56284451a22c  Robert Bachmann <rbachm@gmail.com>   4: +23/-3), ('Robert Bauck Hamar <r.b.hamar@usit.uio.no>',                node                                      author  changestr
#[Out]# n                                                                         
#[Out]# 11502  cc982ff2dcf8  Robert Bauck Hamar <r.b.hamar@usit.uio.no>   1: +1/-1
#[Out]# 7748   5f7512f680cb  Robert Bauck Hamar <r.b.hamar@usit.uio.no>   1: +2/-0
#[Out]# 7747   59815cef38f0  Robert Bauck Hamar <r.b.hamar@usit.uio.no>  1: +34/-6
#[Out]# 7746   8bfe47e726fe  Robert Bauck Hamar <r.b.hamar@usit.uio.no>  1: +12/-4
#[Out]# 7739   db366ec8d0a4  Robert Bauck Hamar <r.b.hamar@usit.uio.no>   1: +9/-7), ('Robert Jones <rob@redshirtsoftware.com>',                node                                   author changestr
#[Out]# n                                                                     
#[Out]# 15085  8413916df816  Robert Jones <rob@redshirtsoftware.com>  1: +3/-1), ('Robin Farine <robin.farine@terminus.org>',               node                                    author    changestr
#[Out]# n                                                                        
#[Out]# 1822  64df4220b349  Robin Farine <robin.farine@terminus.org>   3: +42/-12
#[Out]# 1747  91c56c427171  Robin Farine <robin.farine@terminus.org>   5: +34/-11
#[Out]# 1634  f49f602fae92  Robin Farine <robin.farine@terminus.org>    3: +22/-1
#[Out]# 1633  94c179a92f4a  Robin Farine <robin.farine@terminus.org>  3: +101/-31
#[Out]# 1565  4bcbc126b80b  Robin Farine <robin.farine@terminus.org>  3: +203/-27
#[Out]# 1563  cc2a2e12f4ad  Robin Farine <robin.farine@terminus.org>     1: +7/-5
#[Out]# 1558  651690fe6be3  Robin Farine <robin.farine@terminus.org>    1: +4/-10
#[Out]# 1514  faf46d810a85  Robin Farine <robin.farine@terminus.org>    3: +26/-1
#[Out]# 1513  5c3b93b244aa  Robin Farine <robin.farine@terminus.org>    3: +36/-5
#[Out]# 1512  53ad6ee6ede4  Robin Farine <robin.farine@terminus.org>  3: +210/-68
#[Out]# 1455  407bd229f003  Robin Farine <robin.farine@terminus.org>    1: +15/-2
#[Out]# 1371  68e84563c540  Robin Farine <robin.farine@terminus.org>     1: +1/-1), ('Rocco Rutte <pdmef@gmx.net>',               node                       author    changestr
#[Out]# n                                                           
#[Out]# 8890  c487719cccef  Rocco Rutte <pdmef@gmx.net>     1: +3/-1
#[Out]# 8380  93a811ef3ac0  Rocco Rutte <pdmef@gmx.net>   5: +16/-16
#[Out]# 8362  f28c2f8b9969  Rocco Rutte <pdmef@gmx.net>   1: +23/-20
#[Out]# 8343  3e544c074459  Rocco Rutte <pdmef@gmx.net>  3: +344/-31
#[Out]# 8252  89bc3946c8f3  Rocco Rutte <pdmef@gmx.net>  31: +53/-38
#[Out]# 8251  27dbe534397b  Rocco Rutte <pdmef@gmx.net>     1: +4/-0
#[Out]# 8015  a969b1470987  Rocco Rutte <pdmef@gmx.net>     1: +3/-2
#[Out]# 7958  14ec64d41dad  Rocco Rutte <pdmef@gmx.net>   3: +20/-16
#[Out]# 7957  179fac5c10d8  Rocco Rutte <pdmef@gmx.net>     4: +5/-5
#[Out]# 7954  c0dc1f15b30d  Rocco Rutte <pdmef@gmx.net>     1: +1/-1
#[Out]# 7051  b84d27386285  Rocco Rutte <pdmef@gmx.net>    4: +54/-4
#[Out]# 7050  93746cbf15b5  Rocco Rutte <pdmef@gmx.net>     1: +1/-1
#[Out]# 7018  d09e813b21e3  Rocco Rutte <pdmef@gmx.net>    3: +51/-9
#[Out]# 7014  029a54423a96  Rocco Rutte <pdmef@gmx.net>     1: +2/-2
#[Out]# 6982  0061498f8ab8  Rocco Rutte <pdmef@gmx.net>     1: +1/-0
#[Out]# 6947  248e54a9456e  Rocco Rutte <pdmef@gmx.net>  15: +30/-31
#[Out]# 5485  48c22c719f8c  Rocco Rutte <pdmef@gmx.net>     1: +3/-3), ('Roman Sokolov <sokolov.r.v@gmail.com>',                node                                 author  changestr
#[Out]# n                                                                    
#[Out]# 13394  30e103dacd5f  Roman Sokolov <sokolov.r.v@gmail.com>   1: +1/-1
#[Out]# 13393  d38d500deb08  Roman Sokolov <sokolov.r.v@gmail.com>   1: +3/-0
#[Out]# 13392  777cef34a890  Roman Sokolov <sokolov.r.v@gmail.com>  2: +18/-5), ('Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>',                node                                          author      changestr
#[Out]# n                                                                                 
#[Out]# 13055  0071c8fc2fa6  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +1/-2
#[Out]# 12912  9bb180abc4d0  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       2: +6/-1
#[Out]# 11647  2e7647d25458  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       2: +3/-0
#[Out]# 11248  5116a077c3da  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>      3: +14/-4
#[Out]# 10912  afbcea270bb8  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +1/-1
#[Out]# 10911  fd31a3237498  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +2/-1
#[Out]# 10909  2ed667a9dfcb  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +9/-3
#[Out]# 10908  ab3782458827  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +2/-1
#[Out]# 10907  cb681cc59a8d  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +7/-0
#[Out]# 10677  07dbafd3a0e2  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>      2: +37/-0
#[Out]# 10520  4bab7c3db4e1  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +1/-1
#[Out]# 10489  f2618cacb485  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>  31: +280/-280
#[Out]# 10156  89617aacb495  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +7/-1
#[Out]# 8238   f35b933044cc  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +5/-0
#[Out]# 8237   6e6ebeb52899  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +1/-1
#[Out]# 8138   87a1605979e4  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +5/-0
#[Out]# 8137   6ee71f78497c  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>     6: +22/-16
#[Out]# 8136   dbf20df40eb1  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +2/-0
#[Out]# 8135   b616f328af9f  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>       1: +3/-2
#[Out]# 8134   496ae1ea4698  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>     9: +52/-47
#[Out]# 8133   a26d33749bd8  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>      2: +24/-5
#[Out]# 7320   eae1767cc6a8  Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>      4: +17/-3), ('Ross Lagerwall <rosslagerwall@gmail.com>',                node                                    author changestr
#[Out]# n                                                                      
#[Out]# 16299  df5ecb813426  Ross Lagerwall <rosslagerwall@gmail.com>  1: +5/-0), ('Ry4an Brase <ry4an-hg@ry4an.org>',                node                            author    changestr
#[Out]# n                                                                 
#[Out]# 13493  95b0d4c1c9e1  Ry4an Brase <ry4an-hg@ry4an.org>    3: +30/-3
#[Out]# 11721  a72c5ff1260c  Ry4an Brase <ry4an-hg@ry4an.org>     1: +2/-2
#[Out]# 10693  26d1d23e5a2b  Ry4an Brase <ry4an-hg@ry4an.org>     1: +1/-0
#[Out]# 7306   c21d236ca897  Ry4an Brase <ry4an-hg@ry4an.org>  7: +111/-19), ('Ryan Phillips <ryan@trolocsis.com>',                node                              author changestr
#[Out]# n                                                                
#[Out]# 11699  0c2c969e032b  Ryan Phillips <ryan@trolocsis.com>  2: +4/-0), ('Saint Germain <saintger@gmail.com>',                node                              author  changestr
#[Out]# n                                                                 
#[Out]# 10519  b07d487009b2  Saint Germain <saintger@gmail.com>  3: +35/-2
#[Out]# 10382  e1401c74572f  Saint Germain <saintger@gmail.com>  3: +36/-1), ('Samuel Masham <samuel.masham@gmail.com>',               node                                   author changestr
#[Out]# n                                                                    
#[Out]# 2287  3f18d1eea370  Samuel Masham <samuel.masham@gmail.com>  1: +5/-4), ('Samuel Tardieu <sam@rfc1149.net>',              node                            author   changestr
#[Out]# n                                                              
#[Out]# 968  4a9a753e8232  Samuel Tardieu <sam@rfc1149.net>    1: +6/-1
#[Out]# 967  1f3710636b45  Samuel Tardieu <sam@rfc1149.net>  9: +28/-26
#[Out]# 852  1df0983eb589  Samuel Tardieu <sam@rfc1149.net>    1: +1/-0
#[Out]# 850  d2bf8b9534b1  Samuel Tardieu <sam@rfc1149.net>    1: +2/-1
#[Out]# 825  0108c602feb9  Samuel Tardieu <sam@rfc1149.net>   3: +15/-7), ('Sascha Wilde <wilde@sha-bang.de>',               node                            author  changestr
#[Out]# n                                                              
#[Out]# 5234  f53d97d651f4  Sascha Wilde <wilde@sha-bang.de>   1: +8/-1
#[Out]# 2529  9419855309cd  Sascha Wilde <wilde@sha-bang.de>   1: +1/-1
#[Out]# 2528  049f930f18c1  Sascha Wilde <wilde@sha-bang.de>   1: +1/-1
#[Out]# 2527  c51fad25e59e  Sascha Wilde <wilde@sha-bang.de>  1: +12/-4
#[Out]# 2163  278f9b13c39a  Sascha Wilde <wilde@sha-bang.de>   1: +1/-1
#[Out]# 2059  a4c271765415  Sascha Wilde <wilde@sha-bang.de>  1: +12/-2), ('Satish Balay <balay@fastmail.fm>',                node                            author changestr
#[Out]# n                                                              
#[Out]# 14633  cdda48c93676  Satish Balay <balay@fastmail.fm>  1: +7/-1), ('Scott McCreary <scottmc2@gmail.com>',               node                               author changestr
#[Out]# n                                                                
#[Out]# 6538  bfad9865b1dc  Scott McCreary <scottmc2@gmail.com>  2: +2/-2), ('Sean Dague <sean@dague.net>',               node                       author changestr
#[Out]# n                                                        
#[Out]# 3937  1305ba7dee88  Sean Dague <sean@dague.net>  1: +3/-1), ('Sean Meiners <sean.meiners@linspire.com>',               node                                    author   changestr
#[Out]# n                                                                       
#[Out]# 2549  e1831f06eef1  Sean Meiners <sean.meiners@linspire.com>  4: +72/-32), ('Sebastian Hauer <sebastian.hauer@gmail.com>',               node                                       author changestr
#[Out]# n                                                                        
#[Out]# 5475  b3afa6725082  Sebastian Hauer <sebastian.hauer@gmail.com>  1: +3/-0), ('Sebastien Binet <binet@cern.ch>',               node                           author changestr
#[Out]# n                                                            
#[Out]# 9093  3ac42ca1f3e6  Sebastien Binet <binet@cern.ch>  1: +1/-1), ('Shane Holloway <shane.holloway@ieee.org>',               node                                    author  changestr
#[Out]# n                                                                      
#[Out]# 4239  403c4ddd74bb  Shane Holloway <shane.holloway@ieee.org>  1: +7/-14
#[Out]# 4235  33c369afec94  Shane Holloway <shane.holloway@ieee.org>  1: +16/-7), ('Shuhei Takahashi <takahashi.shuhei@gmail.com>',                node                                         author  changestr
#[Out]# n                                                                            
#[Out]# 13995  88f0e41d8802  Shuhei Takahashi <takahashi.shuhei@gmail.com>  3: +44/-4), ('Shun-ichi GOTO <shunichi.goto@gmail.com>',                node                                    author   changestr
#[Out]# n                                                                        
#[Out]# 14862  a494b54b6ed3  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-1
#[Out]# 14808  6990340c57a8  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +2/-1
#[Out]# 12971  9696954415db  Shun-ichi GOTO <shunichi.goto@gmail.com>   1: +10/-5
#[Out]# 10134  dd37f044f1fa  Shun-ichi GOTO <shunichi.goto@gmail.com>  1: +22/-13
#[Out]# 9508   bd017f359c08  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-1
#[Out]# 9120   661bc51f09b7  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-1
#[Out]# 9115   25c41ddb3978  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-1
#[Out]# 9048   b47d7b440c5c  Shun-ichi GOTO <shunichi.goto@gmail.com>   1: +24/-5
#[Out]# 9047   2bbb8419720d  Shun-ichi GOTO <shunichi.goto@gmail.com>   1: +11/-5
#[Out]# 9027   623f96ae3a26  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-1
#[Out]# 9026   3d456bf32f18  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +3/-5
#[Out]# 8717   505a96cbc923  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-1
#[Out]# 7697   deec6628e62b  Shun-ichi GOTO <shunichi.goto@gmail.com>   2: +14/-6
#[Out]# 5889   02884e56c217  Shun-ichi GOTO <shunichi.goto@gmail.com>  1: +158/-0
#[Out]# 5888   5924a11aa419  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +4/-3
#[Out]# 5887   07d8eb78dd68  Shun-ichi GOTO <shunichi.goto@gmail.com>   1: +11/-3
#[Out]# 5886   83c354c4d529  Shun-ichi GOTO <shunichi.goto@gmail.com>    3: +8/-4
#[Out]# 5885   111ed8c871bf  Shun-ichi GOTO <shunichi.goto@gmail.com>    3: +4/-4
#[Out]# 5849   a3a380af8fb5  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +2/-2
#[Out]# 5840   4c16020d1172  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +8/-0
#[Out]# 5839   68f5bf9aa582  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +4/-1
#[Out]# 5836   f85c0034a062  Shun-ichi GOTO <shunichi.goto@gmail.com>   1: +32/-7
#[Out]# 5835   2baa786c7843  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-0
#[Out]# 5701   165cda754d9e  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +9/-1
#[Out]# 5459   b0e5f44fdeb3  Shun-ichi GOTO <shunichi.goto@gmail.com>   1: +12/-2
#[Out]# 5112   81f8ff2a9bf2  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-1
#[Out]# 4807   edfe69548e2a  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-1
#[Out]# 3057   50e0392d51df  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-1
#[Out]# 2979   985594e891b8  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +3/-0
#[Out]# 2483   5583d5ef257e  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-1
#[Out]# 2261   20cf545b4725  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-1
#[Out]# 1970   119165543ce6  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +1/-0
#[Out]# 1955   2f500a4b6e99  Shun-ichi GOTO <shunichi.goto@gmail.com>    1: +5/-1), ('Shun-ichi Goto <shunichi.goto@gmail.com>',               node                                    author    changestr
#[Out]# n                                                                        
#[Out]# 6929  304484c7e0ba  Shun-ichi Goto <shunichi.goto@gmail.com>  1: +97/-133
#[Out]# 1975  6e1a8ea5d717  Shun-ichi Goto <shunichi.goto@gmail.com>     1: +1/-1), ('Siddharth Agarwal <sid.bugzilla@gmail.com>',               node                                      author   changestr
#[Out]# n                                                                         
#[Out]# 9961  750b7a4f01f6  Siddharth Agarwal <sid.bugzilla@gmail.com>  5: +74/-16), ("Simon 'corecode' Schubert <corecode@fs.ei.tum.de>",               node                                             author changestr
#[Out]# n                                                                              
#[Out]# 4198  dbf250b80cc2  Simon 'corecode' Schubert <corecode@fs.ei.tum.de>  1: +2/-0
#[Out]# 4197  c3864dfb7812  Simon 'corecode' Schubert <corecode@fs.ei.tum.de>  1: +3/-0), ('Simon Heimberg <simohe@besonet.ch>',                node                              author    changestr
#[Out]# n                                                                   
#[Out]# 15609  d5abe76da61e  Simon Heimberg <simohe@besonet.ch>     1: +2/-1
#[Out]# 15608  7a7a1c594daf  Simon Heimberg <simohe@besonet.ch>    1: +23/-1
#[Out]# 15607  8504699d1aa6  Simon Heimberg <simohe@besonet.ch>     1: +7/-1
#[Out]# 15606  36f076d03b34  Simon Heimberg <simohe@besonet.ch>     1: +1/-1
#[Out]# 15578  f9f0731dbc56  Simon Heimberg <simohe@besonet.ch>     1: +8/-5
#[Out]# 15577  434c48e981b8  Simon Heimberg <simohe@besonet.ch>     1: +5/-0
#[Out]# 15576  c3a6ec304055  Simon Heimberg <simohe@besonet.ch>     1: +8/-3
#[Out]# 15116  76cd1964519c  Simon Heimberg <simohe@besonet.ch>     1: +3/-2
#[Out]# 15109  b1f49efeab65  Simon Heimberg <simohe@besonet.ch>     1: +8/-2
#[Out]# 15106  868282fa29d8  Simon Heimberg <simohe@besonet.ch>    1: +11/-8
#[Out]# 15097  574dc5d74f9b  Simon Heimberg <simohe@besonet.ch>    1: +18/-0
#[Out]# 15096  ea96bdda593c  Simon Heimberg <simohe@besonet.ch>    1: +38/-1
#[Out]# 15095  193e7018dc8c  Simon Heimberg <simohe@besonet.ch>   1: +31/-18
#[Out]# 15094  89d9f92f6fdd  Simon Heimberg <simohe@besonet.ch>     1: +2/-0
#[Out]# 14986  545e00279670  Simon Heimberg <simohe@besonet.ch>     1: +1/-1
#[Out]# 14985  351624f8f523  Simon Heimberg <simohe@besonet.ch>     1: +2/-0
#[Out]# 14984  1bc970a77977  Simon Heimberg <simohe@besonet.ch>     1: +1/-1
#[Out]# 14885  31c9e2a702d1  Simon Heimberg <simohe@besonet.ch>     1: +2/-2
#[Out]# 13349  31fdb04cb5e8  Simon Heimberg <simohe@besonet.ch>     1: +2/-1
#[Out]# 13348  ce07defe7d9f  Simon Heimberg <simohe@besonet.ch>     1: +2/-1
#[Out]# 13347  91fe769ac84e  Simon Heimberg <simohe@besonet.ch>     1: +2/-0
#[Out]# 10717  6c2c766afefe  Simon Heimberg <simohe@besonet.ch>     1: +7/-4
#[Out]# 9469   8e6019b16a7d  Simon Heimberg <simohe@besonet.ch>     1: +6/-1
#[Out]# 9457   5b117c90f036  Simon Heimberg <simohe@besonet.ch>     1: +2/-1
#[Out]# 9456   5cd14e1e8385  Simon Heimberg <simohe@besonet.ch>     1: +3/-0
#[Out]# 9455   163e79e2ed5f  Simon Heimberg <simohe@besonet.ch>     1: +1/-1
#[Out]# 9405   567648eab1dd  Simon Heimberg <simohe@besonet.ch>     1: +3/-0
#[Out]# 9247   54eb3782d32f  Simon Heimberg <simohe@besonet.ch>     1: +3/-5
#[Out]# 9196   86b4a9b0ddda  Simon Heimberg <simohe@besonet.ch>   5: +59/-49
#[Out]# 9049   996c1cd8f530  Simon Heimberg <simohe@besonet.ch>     1: +7/-6
#[Out]# 8952   7c7a672e9db7  Simon Heimberg <simohe@besonet.ch>     1: +6/-0
#[Out]# 8891   5fe8dc75aa4a  Simon Heimberg <simohe@besonet.ch>     1: +1/-1
#[Out]# 8649   60f9e574b6eb  Simon Heimberg <simohe@besonet.ch>   1: +14/-16
#[Out]# 8595   cc22b4168879  Simon Heimberg <simohe@besonet.ch>     1: +3/-0
#[Out]# 8592   3edf133dcb5a  Simon Heimberg <simohe@besonet.ch>    1: +25/-5
#[Out]# 8591   2624f485b9bc  Simon Heimberg <simohe@besonet.ch>    1: +10/-2
#[Out]# 8530   b169ba60eebe  Simon Heimberg <simohe@besonet.ch>     1: +9/-0
#[Out]# 8529   21c87b299a04  Simon Heimberg <simohe@besonet.ch>    1: +24/-8
#[Out]# 8527   39fd67552297  Simon Heimberg <simohe@besonet.ch>     1: +1/-1
#[Out]# 8526   9fe16b1a1786  Simon Heimberg <simohe@besonet.ch>     1: +1/-1
#[Out]# 8521   8e2c0ab94432  Simon Heimberg <simohe@besonet.ch>     1: +1/-1
#[Out]# 8391   a00a4db76a15  Simon Heimberg <simohe@besonet.ch>     1: +5/-5
#[Out]# 8323   b87a50b7125c  Simon Heimberg <simohe@besonet.ch>  33: +72/-46
#[Out]# 8321   8417d82d3969  Simon Heimberg <simohe@besonet.ch>     1: +1/-1
#[Out]# 8320   4ff63d699256  Simon Heimberg <simohe@besonet.ch>     1: +2/-2
#[Out]# 8299   9de088320e9a  Simon Heimberg <simohe@besonet.ch>     1: +3/-4
#[Out]# 8180   1bb8a75fceb3  Simon Heimberg <simohe@besonet.ch>     1: +3/-4
#[Out]# 8141   c11636f0609e  Simon Heimberg <simohe@besonet.ch>     1: +2/-2
#[Out]# 7855   47b0a881638f  Simon Heimberg <simohe@besonet.ch>     1: +1/-1
#[Out]# 7774   607de5bd3578  Simon Heimberg <simohe@besonet.ch>     1: +1/-1
#[Out]# 7766   da9acc68b1dd  Simon Heimberg <simohe@besonet.ch>     1: +2/-1), ('Simon Howkins <simonh@symbian.org>',                node                              author  changestr
#[Out]# n                                                                 
#[Out]# 11465  ace5bd98bee3  Simon Howkins <simonh@symbian.org>  3: +22/-3
#[Out]# 11441  d74fe370ab04  Simon Howkins <simonh@symbian.org>   1: +4/-1), ('Soh Tk-r28629 <tksoh@freescale.com>',               node                               author  changestr
#[Out]# n                                                                 
#[Out]# 1949  d2c2e77826c0  Soh Tk-r28629 <tksoh@freescale.com>   1: +1/-1
#[Out]# 1483  a4ba63e04134  Soh Tk-r28629 <tksoh@freescale.com>  2: +13/-5), ('Sol Jerome <sol.jerome@gmail.com>',                node                             author changestr
#[Out]# n                                                               
#[Out]# 12072  851161f07068  Sol Jerome <sol.jerome@gmail.com>  1: +2/-2
#[Out]# 11641  ff5cec76b1c5  Sol Jerome <sol.jerome@gmail.com>  1: +2/-2), ('Stanimir Stamenkov <s7an10@netscape.net>',                node                                    author changestr
#[Out]# n                                                                      
#[Out]# 11159  24f904ae5a26  Stanimir Stamenkov <s7an10@netscape.net>  1: +3/-0), ('Stefan Rank <strank(AT)strank(DOT)info>',               node                                   author changestr
#[Out]# n                                                                    
#[Out]# 6153  09a8be3e5bfb  Stefan Rank <strank(AT)strank(DOT)info>  2: +7/-4), ('Stefan Ring <stefan@complang.tuwien.ac.at>',               node                                      author  changestr
#[Out]# n                                                                        
#[Out]# 7633  f2fa1a9eede6  Stefan Ring <stefan@complang.tuwien.ac.at>  2: +42/-3), ('Stefan Rusek <stefan@rusek.org>',               node                           author   changestr
#[Out]# n                                                              
#[Out]# 7809  dcdda2f59513  Stefan Rusek <stefan@rusek.org>    1: +1/-0
#[Out]# 7775  3b8f2750efcf  Stefan Rusek <stefan@rusek.org>    1: +1/-1
#[Out]# 7531  4c3e0ad58c5b  Stefan Rusek <stefan@rusek.org>   1: +19/-0
#[Out]# 7474  fe0e02f952b0  Stefan Rusek <stefan@rusek.org>  1: +11/-10), ('Stefan Simek <simek@triaxis.sk>',                node                           author changestr
#[Out]# n                                                             
#[Out]# 10010  2dd700a35fd1  Stefan Simek <simek@triaxis.sk>  1: +2/-2), ('Stefano Mioli <jstevie@gmail.com>',               node                             author changestr
#[Out]# n                                                              
#[Out]# 8958  8358cf63f612  Stefano Mioli <jstevie@gmail.com>  1: +2/-2), ('Stefano Tortarolo <stefano.tortarolo@gmail.com>',                node                                           author       changestr
#[Out]# n                                                                                   
#[Out]# 15430  00276525e2b7  Stefano Tortarolo <stefano.tortarolo@gmail.com>       2: +40/-1
#[Out]# 15429  7186b54b07c6  Stefano Tortarolo <stefano.tortarolo@gmail.com>      1: +13/-13
#[Out]# 15428  dc9fb7015d7f  Stefano Tortarolo <stefano.tortarolo@gmail.com>       2: +34/-1
#[Out]# 15415  ad336e093a59  Stefano Tortarolo <stefano.tortarolo@gmail.com>       2: +56/-3
#[Out]# 15412  3411a83e232a  Stefano Tortarolo <stefano.tortarolo@gmail.com>       2: +46/-2
#[Out]# 15411  e1005da0ae04  Stefano Tortarolo <stefano.tortarolo@gmail.com>        1: +1/-1
#[Out]# 15368  872f06c342ff  Stefano Tortarolo <stefano.tortarolo@gmail.com>        1: +1/-1
#[Out]# 14828  b9daa5b7a3af  Stefano Tortarolo <stefano.tortarolo@gmail.com>       2: +46/-0
#[Out]# 14825  c0ccd70df52c  Stefano Tortarolo <stefano.tortarolo@gmail.com>      2: +111/-1
#[Out]# 13926  0995eee8ffe4  Stefano Tortarolo <stefano.tortarolo@gmail.com>       2: +71/-4
#[Out]# 13858  46c3043253fb  Stefano Tortarolo <stefano.tortarolo@gmail.com>       2: +50/-1
#[Out]# 13846  627e50e9e316  Stefano Tortarolo <stefano.tortarolo@gmail.com>       2: +81/-0
#[Out]# 13816  4e2690a764c1  Stefano Tortarolo <stefano.tortarolo@gmail.com>      2: +173/-1
#[Out]# 13659  ea585f2b1adc  Stefano Tortarolo <stefano.tortarolo@gmail.com>       2: +81/-0
#[Out]# 13610  14c0988c314d  Stefano Tortarolo <stefano.tortarolo@gmail.com>       2: +50/-1
#[Out]# 13588  8c3e0542e153  Stefano Tortarolo <stefano.tortarolo@gmail.com>  1: +4251/-3115
#[Out]# 13587  6783f47d90dd  Stefano Tortarolo <stefano.tortarolo@gmail.com>        1: +1/-1
#[Out]# 11316  7fa3968004c1  Stefano Tortarolo <stefano.tortarolo@gmail.com>      3: +96/-23
#[Out]# 10853  f2558a8228be  Stefano Tortarolo <stefano.tortarolo@gmail.com>        1: +4/-1
#[Out]# 10430  6cebf27287de  Stefano Tortarolo <stefano.tortarolo@gmail.com>        1: +2/-2
#[Out]# 10356  66d954e76ffb  Stefano Tortarolo <stefano.tortarolo@gmail.com>     4: +252/-16
#[Out]# 10355  38fe86fb16e3  Stefano Tortarolo <stefano.tortarolo@gmail.com>    1: +119/-120
#[Out]# 8906   bb255fe7c27e  Stefano Tortarolo <stefano.tortarolo@gmail.com>        1: +1/-1
#[Out]# 8905   68decbcb12cf  Stefano Tortarolo <stefano.tortarolo@gmail.com>        1: +1/-1
#[Out]# 8001   c3d4ff03ec72  Stefano Tortarolo <stefano.tortarolo@gmail.com>      3: +100/-5
#[Out]# 8000   b969611064ae  Stefano Tortarolo <stefano.tortarolo@gmail.com>      3: +112/-2
#[Out]# 7998   b214066b7e1d  Stefano Tortarolo <stefano.tortarolo@gmail.com>     3: +167/-12
#[Out]# 7997   4d9e8efb7326  Stefano Tortarolo <stefano.tortarolo@gmail.com>      2: +16/-16
#[Out]# 7987   f5d4f59a9996  Stefano Tortarolo <stefano.tortarolo@gmail.com>     1: +101/-57
#[Out]# 7939   3e0c28145e6a  Stefano Tortarolo <stefano.tortarolo@gmail.com>        1: +0/-1
#[Out]# 7933   38de4b36bcdd  Stefano Tortarolo <stefano.tortarolo@gmail.com>      1: +71/-24
#[Out]# 7811   864ad81b4e24  Stefano Tortarolo <stefano.tortarolo@gmail.com>  1: +3610/-2867
#[Out]# 7787   92455c1d6f83  Stefano Tortarolo <stefano.tortarolo@gmail.com>       3: +42/-5
#[Out]# 7756   9f9137cd83f5  Stefano Tortarolo <stefano.tortarolo@gmail.com>     1: +8720/-0
#[Out]# 7279   45495d784ad6  Stefano Tortarolo <stefano.tortarolo@gmail.com>     5: +298/-18
#[Out]# 7138   204c7850c158  Stefano Tortarolo <stefano.tortarolo@gmail.com>        3: +7/-0
#[Out]# 6975   40cacb049ef6  Stefano Tortarolo <stefano.tortarolo@gmail.com>        1: +8/-8
#[Out]# 6948   808f03f61ebe  Stefano Tortarolo <stefano.tortarolo@gmail.com>    21: +1890/-0
#[Out]# 6930   7c36a4fb05a3  Stefano Tortarolo <stefano.tortarolo@gmail.com>       6: +63/-0
#[Out]# 6924   c7cc40fd74f6  Stefano Tortarolo <stefano.tortarolo@gmail.com>      3: +108/-0
#[Out]# 6487   88804fad71bc  Stefano Tortarolo <stefano.tortarolo@gmail.com>        1: +2/-2
#[Out]# 6466   a2b13cac0922  Stefano Tortarolo <stefano.tortarolo@gmail.com>      4: +28/-24), ('Steffen Daode Nurpmeso <sdaoden@googlemail.com>',                node                                           author changestr
#[Out]# n                                                                             
#[Out]# 14891  7ce7177e029a  Steffen Daode Nurpmeso <sdaoden@googlemail.com>  1: +1/-1), ('Stepan Koltsov <stepancheg@yandex-team.ru>',                node                                      author  changestr
#[Out]# n                                                                         
#[Out]# 14940  f33579435378  Stepan Koltsov <stepancheg@yandex-team.ru>  2: +61/-0
#[Out]# 14939  23c2d7d25329  Stepan Koltsov <stepancheg@yandex-team.ru>  2: +27/-2), ('Stepan Koltsov <yozh@mx1.ru>',               node                        author   changestr
#[Out]# n                                                           
#[Out]# 7637  9c6ae2e09e11  Stepan Koltsov <yozh@mx1.ru>  4: +103/-2
#[Out]# 7516  876de22b70b8  Stepan Koltsov <yozh@mx1.ru>    4: +4/-4), ('Stephen Darnell',               node           author   changestr
#[Out]# n                                              
#[Out]# 1241  3b4f05ff3130  Stephen Darnell  2: +50/-12
#[Out]# 1114  58371c4c2c8f  Stephen Darnell    1: +6/-4
#[Out]# 783   4b06fc1c0f26  Stephen Darnell   1: +16/-1), ('Stephen Darnell <stephen@darnell.plus.com>',               node                                      author    changestr
#[Out]# n                                                                          
#[Out]# 3193  367a009c2acb  Stephen Darnell <stephen@darnell.plus.com>     2: +3/-3
#[Out]# 3192  096f1c73cdc3  Stephen Darnell <stephen@darnell.plus.com>  13: +33/-45
#[Out]# 2207  8a2a7f7d9df6  Stephen Darnell <stephen@darnell.plus.com>   4: +4/-201
#[Out]# 2206  c74e91e81f70  Stephen Darnell <stephen@darnell.plus.com>     1: +2/-1
#[Out]# 2144  d3bddedfdbd0  Stephen Darnell <stephen@darnell.plus.com>    2: +56/-6
#[Out]# 2133  4334be196f8d  Stephen Darnell <stephen@darnell.plus.com>   1: +70/-61
#[Out]# 2110  25a8d116ab6a  Stephen Darnell <stephen@darnell.plus.com>   1: +192/-0), ('Stephen Deasey <sdeasey@gmail.com>',               node                              author   changestr
#[Out]# n                                                                 
#[Out]# 6262  de7256c82fad  Stephen Deasey <sdeasey@gmail.com>  6: +37/-32
#[Out]# 6223  bab6c8f2bb1a  Stephen Deasey <sdeasey@gmail.com>  1: +13/-11), ('Stephen Rasku <mercurial@srasku.net>',               node                                author changestr
#[Out]# n                                                                 
#[Out]# 9162  a9d1e7c8160e  Stephen Rasku <mercurial@srasku.net>  1: +1/-1), ('Stephen Thorne <stephen@thorne.id.au>',                node                                 author changestr
#[Out]# n                                                                   
#[Out]# 14616  64dfbe576455  Stephen Thorne <stephen@thorne.id.au>  1: +2/-0
#[Out]# 14558  2ce7dfe17bc5  Stephen Thorne <stephen@thorne.id.au>  1: +6/-6), ('Steve Borho <steve@ageia.com>',               node                         author changestr
#[Out]# n                                                          
#[Out]# 4905  1df76921aab3  Steve Borho <steve@ageia.com>  1: +2/-2), ('Steve Borho <steve@borho.org>',                node                         author      changestr
#[Out]# n                                                                
#[Out]# 16132  939f043ab5ed  Steve Borho <steve@borho.org>       3: +4/-3
#[Out]# 15511  c8cd3c4bf9a4  Steve Borho <steve@borho.org>       2: +2/-1
#[Out]# 14814  6ed2a449cb5b  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 14795  b30c889584ef  Steve Borho <steve@borho.org>      3: +13/-5
#[Out]# 14662  2b30124c7d8a  Steve Borho <steve@borho.org>       1: +4/-1
#[Out]# 14115  80b8c0b59178  Steve Borho <steve@borho.org>       2: +2/-2
#[Out]# 13782  136854393eed  Steve Borho <steve@borho.org>       2: +2/-1
#[Out]# 13749  595dba23d337  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 13741  8aec2516602b  Steve Borho <steve@borho.org>       1: +2/-2
#[Out]# 13739  fd09c3aeae20  Steve Borho <steve@borho.org>      1: +0/-16
#[Out]# 13700  cc27c31ebc28  Steve Borho <steve@borho.org>      3: +18/-2
#[Out]# 13699  c1ae4ecda8da  Steve Borho <steve@borho.org>       2: +1/-8
#[Out]# 13678  d931cce7f207  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 13647  3c65cdcf3ba6  Steve Borho <steve@borho.org>      2: +10/-7
#[Out]# 13584  a083c6e62acb  Steve Borho <steve@borho.org>       2: +2/-1
#[Out]# 13554  78cc35e75ecc  Steve Borho <steve@borho.org>       1: +2/-2
#[Out]# 13537  a87a0fcb412f  Steve Borho <steve@borho.org>       1: +8/-0
#[Out]# 13536  984175605311  Steve Borho <steve@borho.org>      2: +10/-2
#[Out]# 13535  391948925b67  Steve Borho <steve@borho.org>       2: +1/-8
#[Out]# 13519  8ac1260941c0  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 13441  b366a5e021c6  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 13373  900a92862a7b  Steve Borho <steve@borho.org>      2: +53/-5
#[Out]# 13372  5bced0d28a39  Steve Borho <steve@borho.org>      1: +13/-8
#[Out]# 13371  c691cfdc6b4d  Steve Borho <steve@borho.org>     1: +33/-30
#[Out]# 13370  d13a533a0b11  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 13311  189edd1b15fb  Steve Borho <steve@borho.org>       1: +2/-0
#[Out]# 13275  af50a62e9c20  Steve Borho <steve@borho.org>       2: +7/-2
#[Out]# 13262  f3058dd05281  Steve Borho <steve@borho.org>      1: +12/-0
#[Out]# 13260  1f4721de2ca9  Steve Borho <steve@borho.org>      2: +21/-1
#[Out]# 13259  637d07d8e377  Steve Borho <steve@borho.org>      2: +13/-0
#[Out]# 13240  5314cbb775f6  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 13239  f5be619663f9  Steve Borho <steve@borho.org>       2: +5/-6
#[Out]# 13214  82f840109f76  Steve Borho <steve@borho.org>      1: +11/-6
#[Out]# 13189  873c032c81b5  Steve Borho <steve@borho.org>       1: +2/-1
#[Out]# 13134  1b1cbc246377  Steve Borho <steve@borho.org>       1: +0/-5
#[Out]# 13133  cc40e4f49559  Steve Borho <steve@borho.org>   11: +127/-36
#[Out]# 13132  44b26a87f73e  Steve Borho <steve@borho.org>       1: +4/-4
#[Out]# 13054  5c3e5cd141ea  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 13049  0e0a52bd58f9  Steve Borho <steve@borho.org>      2: +15/-1
#[Out]# 13022  2ef915184ff2  Steve Borho <steve@borho.org>       1: +2/-0
#[Out]# 13005  e5c2338d76b5  Steve Borho <steve@borho.org>      2: +13/-0
#[Out]# 12997  6c9345f9edca  Steve Borho <steve@borho.org>       2: +5/-6
#[Out]# 12987  dbc546811dd6  Steve Borho <steve@borho.org>       1: +2/-1
#[Out]# 12958  db1433e4bf5f  Steve Borho <steve@borho.org>       1: +0/-5
#[Out]# 12957  bd9bc4123920  Steve Borho <steve@borho.org>     9: +69/-37
#[Out]# 12956  79388a8325dc  Steve Borho <steve@borho.org>      4: +62/-3
#[Out]# 12896  b19b4c1df066  Steve Borho <steve@borho.org>     7: +13/-13
#[Out]# 12838  830be2c57626  Steve Borho <steve@borho.org>       1: +5/-4
#[Out]# 12837  c82056f2509f  Steve Borho <steve@borho.org>       1: +4/-0
#[Out]# 12830  d8205dacf9a3  Steve Borho <steve@borho.org>       2: +2/-1
#[Out]# 12810  a68ccfd9c7be  Steve Borho <steve@borho.org>     3: +23/-15
#[Out]# 12801  cddea24aafed  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 12793  0c6c600c03fd  Steve Borho <steve@borho.org>       2: +2/-1
#[Out]# 12792  2c177bda512d  Steve Borho <steve@borho.org>       2: +9/-3
#[Out]# 12791  6c619c2e8778  Steve Borho <steve@borho.org>       2: +2/-1
#[Out]# 12790  24999db620cd  Steve Borho <steve@borho.org>     9: +36/-13
#[Out]# 12786  de793925862e  Steve Borho <steve@borho.org>     6: +70/-21
#[Out]# 12766  5eed9ceebd64  Steve Borho <steve@borho.org>       1: +2/-2
#[Out]# 12751  05bd2658bbb3  Steve Borho <steve@borho.org>      2: +27/-5
#[Out]# 12369  d643ae555a4d  Steve Borho <steve@borho.org>       1: +4/-4
#[Out]# 12339  2ae4d6c31dcc  Steve Borho <steve@borho.org>       1: +1/-0
#[Out]# 12161  a8b1cb0b0ddb  Steve Borho <steve@borho.org>       1: +3/-1
#[Out]# 11690  ed639917c825  Steve Borho <steve@borho.org>       1: +4/-4
#[Out]# 11686  0852da25a31b  Steve Borho <steve@borho.org>       1: +1/-0
#[Out]# 11492  239f3210c970  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 11491  159233cc9c14  Steve Borho <steve@borho.org>       1: +3/-0
#[Out]# 11311  fcd06ecd4cb7  Steve Borho <steve@borho.org>     5: +20/-31
#[Out]# 11310  ac873ecfc3c2  Steve Borho <steve@borho.org>     5: +20/-31
#[Out]# 11308  16277f8aca1a  Steve Borho <steve@borho.org>       1: +9/-0
#[Out]# 11303  e1dde7363601  Steve Borho <steve@borho.org>     5: +31/-20
#[Out]# 11211  7d99edddbaea  Steve Borho <steve@borho.org>      2: +55/-2
#[Out]# 11147  213ca9ffcddb  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 11146  6f4543842795  Steve Borho <steve@borho.org>       1: +4/-2
#[Out]# 11142  a68bd3b7c040  Steve Borho <steve@borho.org>      1: +17/-6
#[Out]# 11141  380ab78dbd69  Steve Borho <steve@borho.org>      1: +15/-2
#[Out]# 11140  9651fa5a3cbf  Steve Borho <steve@borho.org>       1: +9/-1
#[Out]# 11128  4a8d4179362b  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 11074  6d9ff3374a81  Steve Borho <steve@borho.org>       1: +2/-2
#[Out]# 11006  6ced27d3168a  Steve Borho <steve@borho.org>       1: +4/-4
#[Out]# 10988  f0bfe42c7b1f  Steve Borho <steve@borho.org>    21: +54/-42
#[Out]# 10987  a685011ed38e  Steve Borho <steve@borho.org>      6: +13/-7
#[Out]# 10981  3f30190781a3  Steve Borho <steve@borho.org>       1: +2/-0
#[Out]# 10980  a4944b430417  Steve Borho <steve@borho.org>      1: +95/-1
#[Out]# 10979  2d57be56c500  Steve Borho <steve@borho.org>       1: +0/-1
#[Out]# 10805  eea2db5f56ba  Steve Borho <steve@borho.org>       1: +3/-0
#[Out]# 10580  3fb2f7cb5ea5  Steve Borho <steve@borho.org>       2: +2/-2
#[Out]# 10539  261cc6b0f15c  Steve Borho <steve@borho.org>  28: +1700/-97
#[Out]# 10535  dd9d057465c1  Steve Borho <steve@borho.org>       1: +4/-0
#[Out]# 10500  1e022c88a0a5  Steve Borho <steve@borho.org>    8: +1538/-0
#[Out]# 10485  6b354a763617  Steve Borho <steve@borho.org>      1: +25/-2
#[Out]# 10484  677fee0a0604  Steve Borho <steve@borho.org>       1: +2/-1
#[Out]# 10393  935ef1836b2f  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 10390  07bd7608a0ea  Steve Borho <steve@borho.org>      2: +14/-3
#[Out]# 10321  d117089386e2  Steve Borho <steve@borho.org>       1: +3/-2
#[Out]# 10254  37c4ce51a12d  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 10215  c31ac3f7fd8f  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 9997   be324d31b6c5  Steve Borho <steve@borho.org>       1: +3/-2
#[Out]# 9935   fb890a546d44  Steve Borho <steve@borho.org>       1: +4/-2
#[Out]# 9666   71e081b88f3e  Steve Borho <steve@borho.org>       1: +3/-3
#[Out]# 9556   b6b0c42739e9  Steve Borho <steve@borho.org>       1: +8/-1
#[Out]# 9503   ffeaf5ba25d8  Steve Borho <steve@borho.org>       1: +2/-0
#[Out]# 9497   812b812ce8cf  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 9427   baebf028f505  Steve Borho <steve@borho.org>     2: +32/-10
#[Out]# 9398   81900431589f  Steve Borho <steve@borho.org>     1: +88/-17
#[Out]# 9117   bc6b0fef9495  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 9095   7ee67a037dcb  Steve Borho <steve@borho.org>       1: +2/-2
#[Out]# 9094   9488a4d64fb5  Steve Borho <steve@borho.org>      2: +30/-8
#[Out]# 9089   872d49dd577a  Steve Borho <steve@borho.org>      1: +11/-3
#[Out]# 9031   78e54b9f3a62  Steve Borho <steve@borho.org>       1: +4/-1
#[Out]# 8549   3682a19bb637  Steve Borho <steve@borho.org>       4: +6/-5
#[Out]# 8280   bb9f13974d8e  Steve Borho <steve@borho.org>      3: +7/-12
#[Out]# 8273   98acfd1d2b08  Steve Borho <steve@borho.org>     4: +27/-13
#[Out]# 7981   39566bb99a9c  Steve Borho <steve@borho.org>      3: +22/-1
#[Out]# 7974   a218ba5f60df  Steve Borho <steve@borho.org>      5: +25/-3
#[Out]# 7962   48661519913f  Steve Borho <steve@borho.org>       1: +2/-1
#[Out]# 7961   1b1b3dd630a5  Steve Borho <steve@borho.org>     2: +13/-14
#[Out]# 7863   976170068286  Steve Borho <steve@borho.org>       1: +4/-3
#[Out]# 7846   2bc14da14992  Steve Borho <steve@borho.org>       1: +1/-0
#[Out]# 7830   2dfe5cf92ad3  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 7799   57fee79e5588  Steve Borho <steve@borho.org>       1: +4/-1
#[Out]# 7753   998fc8f62539  Steve Borho <steve@borho.org>       1: +6/-0
#[Out]# 7719   6fa7b6fb90a9  Steve Borho <steve@borho.org>     3: +110/-1
#[Out]# 6175   7f9f3233a2c6  Steve Borho <steve@borho.org>       1: +4/-0
#[Out]# 6082   0ee885fea464  Steve Borho <steve@borho.org>       1: +6/-2
#[Out]# 6081   63e0e57ab157  Steve Borho <steve@borho.org>      3: +13/-1
#[Out]# 6039   f2335246e5c7  Steve Borho <steve@borho.org>      1: +11/-8
#[Out]# 6027   15a53af36a89  Steve Borho <steve@borho.org>       1: +2/-1
#[Out]# 6026   83d193a513c8  Steve Borho <steve@borho.org>      1: +84/-1
#[Out]# 5996   6dcc190ffc36  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 5967   56e8a54bf71d  Steve Borho <steve@borho.org>      2: +13/-2
#[Out]# 5966   9ed100559851  Steve Borho <steve@borho.org>      1: +65/-4
#[Out]# 5716   ab5a455cb67c  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 5700   c722bd73c948  Steve Borho <steve@borho.org>       1: +2/-2
#[Out]# 5698   e2e8e977a6cb  Steve Borho <steve@borho.org>      2: +13/-3
#[Out]# 5686   44482de04767  Steve Borho <steve@borho.org>       1: +0/-1
#[Out]# 5684   71179daf6941  Steve Borho <steve@borho.org>       1: +1/-0
#[Out]# 5683   382e336098ed  Steve Borho <steve@borho.org>       1: +1/-0
#[Out]# 5682   28899bf513cc  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 5681   876acbe2f856  Steve Borho <steve@borho.org>       2: +2/-2
#[Out]# 5680   3da5ff2a9b11  Steve Borho <steve@borho.org>       1: +0/-1
#[Out]# 5679   f22708f50213  Steve Borho <steve@borho.org>       1: +5/-1
#[Out]# 5678   ea2625655baf  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 5676   55d3e845736a  Steve Borho <steve@borho.org>      1: +12/-8
#[Out]# 5672   2e76e5a23c2b  Steve Borho <steve@borho.org>       1: +6/-1
#[Out]# 5644   1b5b81d9039b  Steve Borho <steve@borho.org>      2: +20/-1
#[Out]# 5634   9c7f543405c1  Steve Borho <steve@borho.org>       1: +2/-1
#[Out]# 5469   b12432b1c2c7  Steve Borho <steve@borho.org>       1: +2/-0
#[Out]# 5316   f8c36b215281  Steve Borho <steve@borho.org>       1: +2/-0
#[Out]# 3875   729f354f3f09  Steve Borho <steve@borho.org>       1: +1/-0
#[Out]# 3806   45a751d73080  Steve Borho <steve@borho.org>       1: +1/-1
#[Out]# 3805   248a952c0d17  Steve Borho <steve@borho.org>       1: +0/-1
#[Out]# 1486   d7809d6e9db2  Steve Borho <steve@borho.org>       1: +2/-0
#[Out]# 1484   840808c57969  Steve Borho <steve@borho.org>       1: +4/-4
#[Out]# 1442   d32dbf86b88d  Steve Borho <steve@borho.org>       1: +4/-0
#[Out]# 1438   c22da894e4cc  Steve Borho <steve@borho.org>   1: +334/-227
#[Out]# 1414   32fde51910c0  Steve Borho <steve@borho.org>      1: +93/-0
#[Out]# 1368   d1d605d1e839  Steve Borho <steve@borho.org>   1: +122/-122
#[Out]# 1362   246e1a00af6f  Steve Borho <steve@borho.org>     1: +312/-0), ('Steve Losh <steve@stevelosh.com>',                node                            author       changestr
#[Out]# n                                                                    
#[Out]# 13434  b5cc838dd999  Steve Losh <steve@stevelosh.com>       1: +17/-0
#[Out]# 13128  026053f691a4  Steve Losh <steve@stevelosh.com>      2: +307/-3
#[Out]# 12913  ab93029ab622  Steve Losh <steve@stevelosh.com>       2: +35/-1
#[Out]# 12749  d10369fefd01  Steve Losh <steve@stevelosh.com>       2: +87/-1
#[Out]# 12636  301d7626e0ff  Steve Losh <steve@stevelosh.com>        1: +3/-0
#[Out]# 12563  208fc9ad6a48  Steve Losh <steve@stevelosh.com>     2: +115/-16
#[Out]# 12536  4746a2e4b239  Steve Losh <steve@stevelosh.com>       1: +41/-0
#[Out]# 12106  f853873fc66d  Steve Losh <steve@stevelosh.com>       2: +50/-6
#[Out]# 12105  8380ed691df8  Steve Losh <steve@stevelosh.com>       2: +17/-2
#[Out]# 11756  24965bb270b7  Steve Losh <steve@stevelosh.com>       4: +17/-1
#[Out]# 11535  0e789549271d  Steve Losh <steve@stevelosh.com>        1: +2/-2
#[Out]# 11212  6d7cf82453be  Steve Losh <steve@stevelosh.com>       4: +18/-1
#[Out]# 11186  e8d10d085f47  Steve Losh <steve@stevelosh.com>       5: +18/-0
#[Out]# 11034  ca739acf1a98  Steve Losh <steve@stevelosh.com>       4: +90/-0
#[Out]# 11031  0d5f139b23c1  Steve Losh <steve@stevelosh.com>      4: +100/-4
#[Out]# 10486  7a6b5f85c3ab  Steve Losh <steve@stevelosh.com>      1: +13/-10
#[Out]# 10438  e6dc44147234  Steve Losh <steve@stevelosh.com>       1: +12/-0
#[Out]# 10399  8cb81d75730c  Steve Losh <steve@stevelosh.com>  18: +1506/-314
#[Out]# 10337  6ae4f390ec61  Steve Losh <steve@stevelosh.com>        1: +2/-1
#[Out]# 10336  3d75c691b77d  Steve Losh <steve@stevelosh.com>        1: +1/-1
#[Out]# 9505   552c5a5a3502  Steve Losh <steve@stevelosh.com>       1: +16/-0
#[Out]# 9504   3b283adcc720  Steve Losh <steve@stevelosh.com>        1: +5/-2
#[Out]# 8902   b9a8b616521d  Steve Losh <steve@stevelosh.com>       8: +59/-3
#[Out]# 8722   b5e9ed63913b  Steve Losh <steve@stevelosh.com>       1: +17/-0
#[Out]# 8721   3463b28681ee  Steve Losh <steve@stevelosh.com>        1: +3/-0), ('Steve Streeting <steve@stevestreeting.com>',                node                                      author changestr
#[Out]# n                                                                        
#[Out]# 14887  258eee414ab7  Steve Streeting <steve@stevestreeting.com>  1: +2/-2), ('Steven Brown <StevenGBrown@gmail.com>',                node                                 author     changestr
#[Out]# n                                                                       
#[Out]# 15845  43317af36d28  Steven Brown <StevenGBrown@gmail.com>     1: +14/-4
#[Out]# 15833  1dacf7672556  Steven Brown <StevenGBrown@gmail.com>      1: +1/-1
#[Out]# 15519  e4fc0f0b4f7e  Steven Brown <StevenGBrown@gmail.com>   2: +146/-13
#[Out]# 14571  17c0cb1045e5  Steven Brown <StevenGBrown@gmail.com>    5: +131/-0
#[Out]# 14570  9f908ef5a595  Steven Brown <StevenGBrown@gmail.com>     2: +20/-3
#[Out]# 14563  81fc9678b018  Steven Brown <StevenGBrown@gmail.com>     5: +52/-0
#[Out]# 14562  fccd3b966da7  Steven Brown <StevenGBrown@gmail.com>      1: +3/-1
#[Out]# 14561  925d9f2b188b  Steven Brown <StevenGBrown@gmail.com>    1: +12/-13
#[Out]# 14514  175e4b9d8a96  Steven Brown <StevenGBrown@gmail.com>      1: +1/-1
#[Out]# 14503  1d3e2349304a  Steven Brown <StevenGBrown@gmail.com>     2: +27/-2
#[Out]# 14454  cbe13e6bdc34  Steven Brown <StevenGBrown@gmail.com>    3: +15/-11
#[Out]# 14331  d5a65e3ee6b1  Steven Brown <StevenGBrown@gmail.com>      1: +3/-1
#[Out]# 14233  2bf60f158ecb  Steven Brown <StevenGBrown@gmail.com>     2: +14/-8
#[Out]# 14130  ce99d887585f  Steven Brown <StevenGBrown@gmail.com>  11: +120/-17
#[Out]# 14056  b69471bdb678  Steven Brown <StevenGBrown@gmail.com>    2: +21/-11
#[Out]# 13999  3c2f9f611ef6  Steven Brown <StevenGBrown@gmail.com>     2: +41/-1
#[Out]# 13694  970150ddaaf8  Steven Brown <StevenGBrown@gmail.com>      2: +6/-7
#[Out]# 13397  6f9616a46f7c  Steven Brown <StevenGBrown@gmail.com>     1: +74/-0), ('Steven Stallion <sstallion@gmail.com>',                node                                 author     changestr
#[Out]# n                                                                       
#[Out]# 16603  822e75386c16  Steven Stallion <sstallion@gmail.com>      1: +4/-2
#[Out]# 16572  cbb916e2d7c5  Steven Stallion <sstallion@gmail.com>      1: +5/-5
#[Out]# 16556  f9262456fb01  Steven Stallion <sstallion@gmail.com>      2: +7/-7
#[Out]# 16489  cf137319c6cd  Steven Stallion <sstallion@gmail.com>      1: +2/-1
#[Out]# 16463  cef755f86d5c  Steven Stallion <sstallion@gmail.com>    1: +11/-11
#[Out]# 16457  91196ebcaeed  Steven Stallion <sstallion@gmail.com>      1: +1/-1
#[Out]# 16443  9181188ffb5b  Steven Stallion <sstallion@gmail.com>      3: +8/-1
#[Out]# 16439  28a90cdf0ca0  Steven Stallion <sstallion@gmail.com>      0: +0/-0
#[Out]# 16403  c292bbbcf10c  Steven Stallion <sstallion@gmail.com>      0: +0/-0
#[Out]# 16402  f2ba409dbb0f  Steven Stallion <sstallion@gmail.com>     2: +87/-6
#[Out]# 16396  9cf7c9d529d0  Steven Stallion <sstallion@gmail.com>      2: +7/-2
#[Out]# 16388  f5dd179bfa4a  Steven Stallion <sstallion@gmail.com>  14: +328/-28
#[Out]# 14084  1c38777f7b8a  Steven Stallion <sstallion@gmail.com>      1: +4/-2
#[Out]# 14014  a1c31c64bcd3  Steven Stallion <sstallion@gmail.com>      2: +4/-1
#[Out]# 14012  616ad3f6fd33  Steven Stallion <sstallion@gmail.com>   42: +46/-38), ('StevenGBrown',                node        author    changestr
#[Out]# n                                             
#[Out]# 13295  aa3f726a2bdb  StevenGBrown  5: +33/-119), ('Stuart W Marks <smarks@smarks.org>',               node                              author    changestr
#[Out]# n                                                                  
#[Out]# 9831  9ebad1b93456  Stuart W Marks <smarks@smarks.org>     1: +7/-5
#[Out]# 9718  fe1b19bfe75b  Stuart W Marks <smarks@smarks.org>   1: +26/-24
#[Out]# 9717  68a1b9d0663e  Stuart W Marks <smarks@smarks.org>   4: +24/-28
#[Out]# 9716  ea8c207a0f78  Stuart W Marks <smarks@smarks.org>   3: +164/-0
#[Out]# 9512  b2310903c462  Stuart W Marks <smarks@smarks.org>  12: +27/-27
#[Out]# 9118  e78967d3dd6f  Stuart W Marks <smarks@smarks.org>     1: +4/-1
#[Out]# 9085  73bec717b825  Stuart W Marks <smarks@smarks.org>     1: +7/-8), ('Sune Foldager <cryo@cyanite.org>',                node                            author       changestr
#[Out]# n                                                                    
#[Out]# 16618  025b3b763ba9  Sune Foldager <cryo@cyanite.org>      4: +50/-22
#[Out]# 15901  4252d9f08d7e  Sune Foldager <cryo@cyanite.org>        2: +5/-3
#[Out]# 15459  bc0778f5619a  Sune Foldager <cryo@cyanite.org>        1: +4/-0
#[Out]# 15105  2ca855126091  Sune Foldager <cryo@cyanite.org>        1: +2/-1
#[Out]# 15104  cbba7fca7c4d  Sune Foldager <cryo@cyanite.org>        1: +1/-1
#[Out]# 14900  b1880474e3ad  Sune Foldager <cryo@cyanite.org>        2: +4/-1
#[Out]# 14886  106f89299da6  Sune Foldager <cryo@cyanite.org>        1: +2/-1
#[Out]# 14695  5fb3cb7266e5  Sune Foldager <cryo@cyanite.org>        1: +3/-0
#[Out]# 14523  b4175b72bbd8  Sune Foldager <cryo@cyanite.org>        1: +5/-5
#[Out]# 14522  5ca61ef6ff00  Sune Foldager <cryo@cyanite.org>     3: +97/-104
#[Out]# 14521  d27f669bad7c  Sune Foldager <cryo@cyanite.org>        1: +3/-6
#[Out]# 14520  9d8d2fecb72e  Sune Foldager <cryo@cyanite.org>      3: +88/-86
#[Out]# 14449  0969d91fad5c  Sune Foldager <cryo@cyanite.org>        1: +1/-1
#[Out]# 14383  a8e3931e3fb5  Sune Foldager <cryo@cyanite.org>       2: +27/-9
#[Out]# 14382  a3b9f1bddab1  Sune Foldager <cryo@cyanite.org>       1: +28/-0
#[Out]# 14375  077cdf172580  Sune Foldager <cryo@cyanite.org>        1: +0/-1
#[Out]# 14357  85c82ebc96a3  Sune Foldager <cryo@cyanite.org>        2: +6/-0
#[Out]# 14356  31a5973fcf96  Sune Foldager <cryo@cyanite.org>       2: +8/-10
#[Out]# 14353  473d0aaf7655  Sune Foldager <cryo@cyanite.org>        1: +2/-2
#[Out]# 14347  a79fea6b3e77  Sune Foldager <cryo@cyanite.org>      7: +66/-41
#[Out]# 14329  32a548776b65  Sune Foldager <cryo@cyanite.org>      1: +81/-38
#[Out]# 14328  64c22db0bc38  Sune Foldager <cryo@cyanite.org>       2: +99/-0
#[Out]# 14327  e2be0bba0d83  Sune Foldager <cryo@cyanite.org>        1: +1/-1
#[Out]# 14326  b0f97b2589cc  Sune Foldager <cryo@cyanite.org>    1: +294/-294
#[Out]# 14325  f94993769c87  Sune Foldager <cryo@cyanite.org>        1: +6/-1
#[Out]# 14320  62e25c63fb3a  Sune Foldager <cryo@cyanite.org>        1: +8/-8
#[Out]# 14316  c97d8485b5fa  Sune Foldager <cryo@cyanite.org>        1: +6/-0
#[Out]# 14311  7c231754a621  Sune Foldager <cryo@cyanite.org>        2: +9/-2
#[Out]# 14288  d6907a5674a2  Sune Foldager <cryo@cyanite.org>       2: +23/-9
#[Out]# 14287  66257848c154  Sune Foldager <cryo@cyanite.org>        1: +2/-2
#[Out]# 14280  d6a762d93b77  Sune Foldager <cryo@cyanite.org>       1: +14/-4
#[Out]# 14279  c28d5200374c  Sune Foldager <cryo@cyanite.org>       1: +12/-3
#[Out]# 14278  19067884c5f5  Sune Foldager <cryo@cyanite.org>       2: +20/-7
#[Out]# 14277  258fbccf22f5  Sune Foldager <cryo@cyanite.org>        1: +2/-8
#[Out]# 14235  d62d597b8974  Sune Foldager <cryo@cyanite.org>        2: +7/-3
#[Out]# 14224  e7483ec3c374  Sune Foldager <cryo@cyanite.org>       1: +7/-29
#[Out]# 14223  0013d3eeb826  Sune Foldager <cryo@cyanite.org>       2: +5/-27
#[Out]# 14212  4ab6e2d597cc  Sune Foldager <cryo@cyanite.org>        2: +2/-2
#[Out]# 14189  ec5886db9dc6  Sune Foldager <cryo@cyanite.org>     16: +49/-47
#[Out]# 14188  fa2b596db182  Sune Foldager <cryo@cyanite.org>       4: +85/-5
#[Out]# 14183  497493b777ad  Sune Foldager <cryo@cyanite.org>   17: +264/-151
#[Out]# 14112  bc101902a68d  Sune Foldager <cryo@cyanite.org>        1: +4/-1
#[Out]# 14111  e8271159c8c2  Sune Foldager <cryo@cyanite.org>      1: +21/-11
#[Out]# 12338  d7fff529d85d  Sune Foldager <cryo@cyanite.org>       2: +26/-4
#[Out]# 12337  3388ab21d768  Sune Foldager <cryo@cyanite.org>       1: +17/-8
#[Out]# 12336  6ee719f56f01  Sune Foldager <cryo@cyanite.org>        0: +0/-0
#[Out]# 12334  c4c2ba553401  Sune Foldager <cryo@cyanite.org>       1: +21/-7
#[Out]# 12218  c061f9882ff7  Sune Foldager <cryo@cyanite.org>       1: +11/-4
#[Out]# 11685  a7d3147bd4b3  Sune Foldager <cryo@cyanite.org>       1: +19/-7
#[Out]# 11322  3d6915f5a2bb  Sune Foldager <cryo@cyanite.org>      4: +37/-16
#[Out]# 11301  24eeca1f2791  Sune Foldager <cryo@cyanite.org>        2: +7/-6
#[Out]# 11233  e43c23d189a5  Sune Foldager <cryo@cyanite.org>      6: +49/-19
#[Out]# 11017  4d81cbd8a851  Sune Foldager <cryo@cyanite.org>      3: +99/-96
#[Out]# 11014  39c69b5dc258  Sune Foldager <cryo@cyanite.org>        1: +2/-4
#[Out]# 11010  3d7c20986027  Sune Foldager <cryo@cyanite.org>     3: +102/-11
#[Out]# 11009  4327409c1303  Sune Foldager <cryo@cyanite.org>      1: +29/-11
#[Out]# 11008  78db9b7d9f65  Sune Foldager <cryo@cyanite.org>      1: +29/-11
#[Out]# 10982  24ed7a541f23  Sune Foldager <cryo@cyanite.org>      7: +197/-4
#[Out]# 10917  bd36e5c0ccb1  Sune Foldager <cryo@cyanite.org>      4: +51/-25
#[Out]# 10820  6227c8d669d5  Sune Foldager <cryo@cyanite.org>       2: +11/-5
#[Out]# 10793  deaeb2d84d8a  Sune Foldager <cryo@cyanite.org>       3: +30/-4
#[Out]# 10792  05ac42e56452  Sune Foldager <cryo@cyanite.org>        2: +7/-6
#[Out]# 10702  a101a743c570  Sune Foldager <cryo@cyanite.org>      3: +99/-96
#[Out]# 10694  816bac2f9452  Sune Foldager <cryo@cyanite.org>      3: +21/-11
#[Out]# 10686  a9702c47a19f  Sune Foldager <cryo@cyanite.org>      3: +157/-1
#[Out]# 10649  1e819576e926  Sune Foldager <cryo@cyanite.org>       1: +5/-13
#[Out]# 10648  01f097c4ae66  Sune Foldager <cryo@cyanite.org>       3: +38/-6
#[Out]# 10647  fe39f0160c74  Sune Foldager <cryo@cyanite.org>        2: +8/-6
#[Out]# 10629  4a70178f9bde  Sune Foldager <cryo@cyanite.org>        1: +1/-0
#[Out]# 10590  5faf3566c96d  Sune Foldager <cryo@cyanite.org>        1: +1/-0
#[Out]# 10589  92b8c79b34c2  Sune Foldager <cryo@cyanite.org>        3: +3/-2
#[Out]# 10588  b0b19d61d79a  Sune Foldager <cryo@cyanite.org>        3: +8/-1
#[Out]# 10587  a48d256cc7d9  Sune Foldager <cryo@cyanite.org>      1: +16/-13
#[Out]# 10586  efd3b71fc293  Sune Foldager <cryo@cyanite.org>      1: +13/-13
#[Out]# 10579  612c142b7a82  Sune Foldager <cryo@cyanite.org>       3: +22/-1
#[Out]# 10574  b3db23a124ad  Sune Foldager <cryo@cyanite.org>       1: +92/-0
#[Out]# 10573  321a2aeb79a3  Sune Foldager <cryo@cyanite.org>  17: +230/-1861
#[Out]# 10572  704af22f4907  Sune Foldager <cryo@cyanite.org>       1: +92/-0
#[Out]# 10544  2e1a9b811d13  Sune Foldager <cryo@cyanite.org>        2: +7/-6
#[Out]# 10527  e3eff76552f1  Sune Foldager <cryo@cyanite.org>        1: +1/-4
#[Out]# 10526  ed87b6c60e0b  Sune Foldager <cryo@cyanite.org>        1: +2/-3
#[Out]# 10523  72d3a02c62e6  Sune Foldager <cryo@cyanite.org>        1: +1/-1
#[Out]# 10522  cc2d296c1d4c  Sune Foldager <cryo@cyanite.org>        1: +1/-1
#[Out]# 10491  0e64d814d7d0  Sune Foldager <cryo@cyanite.org>      5: +39/-27
#[Out]# 10391  6dc25b01e170  Sune Foldager <cryo@cyanite.org>        1: +4/-4
#[Out]# 10381  ee72d89c0d9f  Sune Foldager <cryo@cyanite.org>        1: +4/-1
#[Out]# 10380  a78bfaf988e1  Sune Foldager <cryo@cyanite.org>      6: +39/-18
#[Out]# 10369  d757bc0c7865  Sune Foldager <cryo@cyanite.org>     8: +147/-38
#[Out]# 10362  d42821cd5c96  Sune Foldager <cryo@cyanite.org>       3: +11/-3
#[Out]# 10176  e533fc8a058b  Sune Foldager <cryo@cyanite.org>        1: +5/-5
#[Out]# 10111  15fbbc939373  Sune Foldager <cryo@cyanite.org>      3: +269/-4
#[Out]# 10108  4e3a8f3e9dc2  Sune Foldager <cryo@cyanite.org>       3: +43/-0
#[Out]# 10087  c08583734fc5  Sune Foldager <cryo@cyanite.org>       8: +44/-7
#[Out]# 10061  ad44e1f8b3f3  Sune Foldager <cryo@cyanite.org>       3: +13/-1
#[Out]# 10026  806e6b6cb8d8  Sune Foldager <cryo@cyanite.org>        1: +4/-3
#[Out]# 10023  6f92997dbdca  Sune Foldager <cryo@cyanite.org>      2: +55/-40
#[Out]# 10013  38170eeed18c  Sune Foldager <cryo@cyanite.org>        2: +7/-2
#[Out]# 9930   37679dbf2ee3  Sune Foldager <cryo@cyanite.org>        1: +5/-5
#[Out]# 9914   585f51f8b5f0  Sune Foldager <cryo@cyanite.org>      3: +269/-4
#[Out]# 9913   4ddfad7ebd98  Sune Foldager <cryo@cyanite.org>       3: +43/-0
#[Out]# 9912   2770d03ae49f  Sune Foldager <cryo@cyanite.org>       5: +23/-4
#[Out]# 9911   eba6c8687fd2  Sune Foldager <cryo@cyanite.org>       3: +21/-3
#[Out]# 9898   6045a8c4dbbc  Sune Foldager <cryo@cyanite.org>       3: +13/-1
#[Out]# 9897   d6a307719ccb  Sune Foldager <cryo@cyanite.org>       3: +33/-6
#[Out]# 9875   7e7d56fe4833  Sune Foldager <cryo@cyanite.org>       2: +10/-4
#[Out]# 9709   5858117a0077  Sune Foldager <cryo@cyanite.org>        1: +1/-0
#[Out]# 9694   8269fe2d48f6  Sune Foldager <cryo@cyanite.org>      3: +11/-10
#[Out]# 9693   c40a1ee20aa5  Sune Foldager <cryo@cyanite.org>       3: +17/-4
#[Out]# 9692   807633f1e3c2  Sune Foldager <cryo@cyanite.org>        2: +3/-3
#[Out]# 9691   f8e1456e1c2c  Sune Foldager <cryo@cyanite.org>        2: +2/-2
#[Out]# 9690   b33d70849a20  Sune Foldager <cryo@cyanite.org>       4: +20/-0
#[Out]# 9658   852b1f3032d2  Sune Foldager <cryo@cyanite.org>        1: +9/-5
#[Out]# 9650   1ad02c04356c  Sune Foldager <cryo@cyanite.org>        1: +1/-1
#[Out]# 9584   341182ac95e4  Sune Foldager <cryo@cyanite.org>       3: +23/-2
#[Out]# 9583   b91960aed018  Sune Foldager <cryo@cyanite.org>        2: +6/-6
#[Out]# 9537   e7bde4680eec  Sune Foldager <cryo@cyanite.org>      1: +71/-28
#[Out]# 9125   f3569d95c2ab  Sune Foldager <cryo@cyanite.org>      3: +44/-11
#[Out]# 9124   c295a82a020b  Sune Foldager <cryo@cyanite.org>       2: +11/-4
#[Out]# 8911   62e3b9466700  Sune Foldager <cryo@cyanite.org>    2: +103/-101
#[Out]# 8568   268d16b2ec25  Sune Foldager <cryo@cyanite.org>      2: +108/-0
#[Out]# 8567   6b9ec23b09fc  Sune Foldager <cryo@cyanite.org>      2: +84/-25
#[Out]# 8431   b6d0fa8c7685  Sune Foldager <cryo@cyanite.org>     3: +13/-125
#[Out]# 8368   d974a32b59dc  Sune Foldager <cryo@cyanite.org>      14: +40/-0
#[Out]# 8367   439663cd043a  Sune Foldager <cryo@cyanite.org>      14: +52/-2
#[Out]# 8366   5ba798f339c8  Sune Foldager <cryo@cyanite.org>      16: +53/-2
#[Out]# 8364   6058d291abdf  Sune Foldager <cryo@cyanite.org>      21: +81/-0
#[Out]# 8363   eefcb59d44d6  Sune Foldager <cryo@cyanite.org>       1: +22/-2
#[Out]# 8355   873429914ec5  Sune Foldager <cryo@cyanite.org>        1: +2/-1
#[Out]# 8344   89c80c3dc584  Sune Foldager <cryo@cyanite.org>     4: +283/-10
#[Out]# 8306   1ea7e7d90007  Sune Foldager <cryo@cyanite.org>        1: +2/-4
#[Out]# 8055   25b63941b17b  Sune Foldager <cryo@cyanite.org>      1: +13/-13
#[Out]# 7979   5325596c354c  Sune Foldager <cryo@cyanite.org>        1: +1/-0
#[Out]# 7978   96501a4abbec  Sune Foldager <cryo@cyanite.org>        1: +1/-1
#[Out]# 7889   ea82a23cf887  Sune Foldager <cryo@cyanite.org>       1: +20/-5
#[Out]# 7751   b03416194895  Sune Foldager <cryo@cyanite.org>        2: +2/-1
#[Out]# 7750   f32af51aaee5  Sune Foldager <cryo@cyanite.org>       2: +18/-0
#[Out]# 7749   09bec6fd747c  Sune Foldager <cryo@cyanite.org>       2: +10/-0
#[Out]# 7742   a3d7f99c23c0  Sune Foldager <cryo@cyanite.org>        2: +3/-1
#[Out]# 7074   efc579fdaf69  Sune Foldager <cryo@cyanite.org>        3: +6/-1
#[Out]# 7061   6489ee64b522  Sune Foldager <cryo@cyanite.org>       3: +24/-2
#[Out]# 7032   a6b74fbb5ce0  Sune Foldager <cryo@cyanite.org>     3: +206/-16
#[Out]# 7031   92d44ec32430  Sune Foldager <cryo@cyanite.org>      3: +40/-21), ('Sune Foldager <sune.foldager@edlund.dk>',                node                                   author  changestr
#[Out]# n                                                                      
#[Out]# 12219  8a0e5b0c0ba9  Sune Foldager <sune.foldager@edlund.dk>  1: +18/-7), ('Sverre Rabbelier <sverre@rabbelier.nl>',               node                                  author changestr
#[Out]# n                                                                   
#[Out]# 8324  b695392491e7  Sverre Rabbelier <sverre@rabbelier.nl>  2: +2/-2), ('S\xc3\xa9bastien Pierre <sebastien@xprima.com>',               node                                   author    changestr
#[Out]# n                                                                       
#[Out]# 2749  d13e4ffaa79d  Sébastien Pierre <sebastien@xprima.com>    1: +4/-3
#[Out]# 2587  fe3e87358b47  Sébastien Pierre <sebastien@xprima.com>  1: +73/-26
#[Out]# 2586  bb63d29ce03d  Sébastien Pierre <sebastien@xprima.com>  1: +13/-10
#[Out]# 2349  88c881bda888  Sébastien Pierre <sebastien@xprima.com>  1: +124/-0), ('TK Soh <teekaysoh@gmail.com>',               node                        author changestr
#[Out]# n                                                         
#[Out]# 9562  3bcb28131bab  TK Soh <teekaysoh@gmail.com>  1: +7/-0), ('TK Soh <teekaysoh@yahoo.com>',               node                        author   changestr
#[Out]# n                                                           
#[Out]# 6518  75b8c8b92e92  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 5418  b8872655f951  TK Soh <teekaysoh@yahoo.com>    1: +2/-2
#[Out]# 4650  15e22b483adc  TK Soh <teekaysoh@yahoo.com>    1: +2/-0
#[Out]# 4083  1774c037fbd2  TK Soh <teekaysoh@yahoo.com>    1: +2/-3
#[Out]# 4076  50a46ae14efb  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 4039  5e857d72d3ac  TK Soh <teekaysoh@yahoo.com>  2: +129/-4
#[Out]# 4031  66a3fe30f9fc  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 4022  cd650cd61b06  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 4021  7843528a7922  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 4020  38922a13101e  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 3173  eb0906ebba81  TK Soh <teekaysoh@yahoo.com>    1: +4/-2
#[Out]# 3160  36ab673f66a5  TK Soh <teekaysoh@yahoo.com>    1: +2/-1
#[Out]# 3124  f145d04899d2  TK Soh <teekaysoh@yahoo.com>    1: +6/-2
#[Out]# 3071  be98c5ce4022  TK Soh <teekaysoh@yahoo.com>    1: +1/-2
#[Out]# 3065  15526271eafb  TK Soh <teekaysoh@yahoo.com>    1: +2/-2
#[Out]# 3056  3dab573a4330  TK Soh <teekaysoh@yahoo.com>  2: +22/-17
#[Out]# 3036  77637938d43d  TK Soh <teekaysoh@yahoo.com>   1: +15/-0
#[Out]# 3030  892eb1b4f973  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 3029  cef3e7071443  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 3021  b41cd423e5a3  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 3020  a7d93a22f28c  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 3019  d5cdf25bab74  TK Soh <teekaysoh@yahoo.com>    2: +6/-5
#[Out]# 3013  2b255c3478dc  TK Soh <teekaysoh@yahoo.com>    1: +2/-2
#[Out]# 2959  7f5fc4b347de  TK Soh <teekaysoh@yahoo.com>    1: +2/-2
#[Out]# 2360  25ec4981883e  TK Soh <teekaysoh@yahoo.com>    1: +2/-0
#[Out]# 2358  8819fc1dcf4b  TK Soh <teekaysoh@yahoo.com>   3: +16/-8
#[Out]# 2352  61909dfb316d  TK Soh <teekaysoh@yahoo.com>  1: +16/-10
#[Out]# 2195  f027bc2d3f4a  TK Soh <teekaysoh@yahoo.com>    3: +6/-6
#[Out]# 2187  09d3eebdd9b2  TK Soh <teekaysoh@yahoo.com>    1: +2/-2
#[Out]# 2186  1092533fd11c  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 2012  d07c322e0033  TK Soh <teekaysoh@yahoo.com>    1: +2/-0
#[Out]# 2011  b4df4687a78a  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 2007  2ffa36dc3423  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 1993  fb6ca9801d04  TK Soh <teekaysoh@yahoo.com>    1: +1/-0
#[Out]# 1978  10606ee61107  TK Soh <teekaysoh@yahoo.com>    2: +7/-6
#[Out]# 1962  2a676ad52c22  TK Soh <teekaysoh@yahoo.com>    4: +4/-4
#[Out]# 1953  379ab45b91b7  TK Soh <teekaysoh@yahoo.com>    3: +7/-7
#[Out]# 1952  f4df34b6987f  TK Soh <teekaysoh@yahoo.com>    1: +9/-3
#[Out]# 1886  d4a3a8a332ab  TK Soh <teekaysoh@yahoo.com>    2: +2/-2
#[Out]# 1848  bb70ffebe77b  TK Soh <teekaysoh@yahoo.com>   1: +10/-9
#[Out]# 1567  b4956bbbadc9  TK Soh <teekaysoh@yahoo.com>    1: +2/-3
#[Out]# 1547  4dea10839201  TK Soh <teekaysoh@yahoo.com>    1: +1/-0
#[Out]# 1526  c230939283c3  TK Soh <teekaysoh@yahoo.com>    1: +1/-8
#[Out]# 1524  0d47bb884330  TK Soh <teekaysoh@yahoo.com>    1: +4/-1
#[Out]# 1511  a91bfbbe88d3  TK Soh <teekaysoh@yahoo.com>    3: +2/-3
#[Out]# 1470  fb9b84c91222  TK Soh <teekaysoh@yahoo.com>    1: +2/-2
#[Out]# 1453  6fbb13b7a59f  TK Soh <teekaysoh@yahoo.com>   1: +13/-2
#[Out]# 1445  56281e086f38  TK Soh <teekaysoh@yahoo.com>   6: +10/-8
#[Out]# 1441  cbc36ad70945  TK Soh <teekaysoh@yahoo.com>    1: +5/-1
#[Out]# 1433  70a3b6a505c6  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 1432  612f3eba73ee  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 1430  c91966c3bbf5  TK Soh <teekaysoh@yahoo.com>    1: +4/-1
#[Out]# 1425  8fe4116b3253  TK Soh <teekaysoh@yahoo.com>    2: +8/-2
#[Out]# 1405  6fd6527f95eb  TK Soh <teekaysoh@yahoo.com>    1: +3/-3
#[Out]# 1404  67e20e27d8df  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 1381  c29c36745c6e  TK Soh <teekaysoh@yahoo.com>    1: +3/-0
#[Out]# 1361  f6d73b26dbdb  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 1336  8c094fb47b59  TK Soh <teekaysoh@yahoo.com>    2: +3/-2
#[Out]# 1334  0843e1bf2b97  TK Soh <teekaysoh@yahoo.com>    2: +3/-3
#[Out]# 1311  db8bebb08f8f  TK Soh <teekaysoh@yahoo.com>    1: +2/-0
#[Out]# 1221  89f899caecb5  TK Soh <teekaysoh@yahoo.com>    1: +2/-1
#[Out]# 1192  6e165de907c5  TK Soh <teekaysoh@yahoo.com>   2: +24/-6
#[Out]# 1156  1d5996d39c9d  TK Soh <teekaysoh@yahoo.com>   1: +33/-0
#[Out]# 1155  92697ad28f08  TK Soh <teekaysoh@yahoo.com>   1: +74/-0
#[Out]# 1113  6130de75bb2a  TK Soh <teekaysoh@yahoo.com>    3: +5/-5
#[Out]# 1088  39b916b1d8e4  TK Soh <teekaysoh@yahoo.com>    1: +2/-0
#[Out]# 1085  6f94688b81b6  TK Soh <teekaysoh@yahoo.com>   1: +10/-1
#[Out]# 1084  069b4311a81b  TK Soh <teekaysoh@yahoo.com>   1: +29/-4
#[Out]# 952   dbfabfcb485e  TK Soh <teekaysoh@yahoo.com>    1: +1/-1
#[Out]# 949   d997148155f2  TK Soh <teekaysoh@yahoo.com>   3: +10/-7
#[Out]# 924   ab681ea2857e  TK Soh <teekaysoh@yahoo.com>   2: +10/-2
#[Out]# 913   46581ad4bd27  TK Soh <teekaysoh@yahoo.com>    1: +8/-8
#[Out]# 779   b3c7cb74d325  TK Soh <teekaysoh@yahoo.com>   1: +14/-0), ('TK Soh <tksoh@freescale.com>',               node                        author  changestr
#[Out]# n                                                          
#[Out]# 1158  4650ec7ef690  TK Soh <tksoh@freescale.com>  1: +11/-4
#[Out]# 1157  6e66235084d9  TK Soh <tksoh@freescale.com>   1: +3/-4), ('Takumi IINO <trot.thunder@gmail.com>',                node                                author changestr
#[Out]# n                                                                  
#[Out]# 16348  8ac2c91855cf  Takumi IINO <trot.thunder@gmail.com>  1: +2/-0
#[Out]# 16184  740f20e252bd  Takumi IINO <trot.thunder@gmail.com>  1: +2/-0), ('Terry Smith <terry@t11e.com>',               node                        author  changestr
#[Out]# n                                                          
#[Out]# 5353  bd706eb8bc25  Terry Smith <terry@t11e.com>  1: +19/-2
#[Out]# 5352  ad8783fe20f7  Terry Smith <terry@t11e.com>   1: +5/-0
#[Out]# 5351  b62a59fa9d26  Terry Smith <terry@t11e.com>  1: +51/-1), ('Thomas Arendsen Hein <thomas@intevation.de>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 1018 entries, 16650 to 233
#[Out]# Data columns:
#[Out]# node         1018  non-null values
#[Out]# author       1018  non-null values
#[Out]# changestr    1018  non-null values
#[Out]# dtypes: object(3)), ('Thomas Arendsen Hein <thomas@jtah.de>',                node                                 author changestr
#[Out]# n                                                                   
#[Out]# 13148  6b8d2ee24ce2  Thomas Arendsen Hein <thomas@jtah.de>  2: +2/-2
#[Out]# 13147  a861c7155f09  Thomas Arendsen Hein <thomas@jtah.de>  1: +2/-5
#[Out]# 13146  d73c3034deee  Thomas Arendsen Hein <thomas@jtah.de>  3: +6/-6
#[Out]# 13145  637627f31c74  Thomas Arendsen Hein <thomas@jtah.de>  1: +3/-0), ('Thomas De Schampheleire <thomas.de.schampheleire@gmail.com>',                node                                             author changestr
#[Out]# n                                                                               
#[Out]# 15433  8b011ededfb2  Thomas De Schampheleire <thomas.de.schampheleire@  1: +1/-0), ('Tobias Bell <tobias.bell@gmail.com>',               node                               author      changestr
#[Out]# n                                                                     
#[Out]# 8759  1060cb231595  Tobias Bell <tobias.bell@gmail.com>  1: +727/-1163
#[Out]# 8100  28a72f620cde  Tobias Bell <tobias.bell@gmail.com>   1: +944/-870
#[Out]# 8051  a4defdc4f5dc  Tobias Bell <tobias.bell@gmail.com>       1: +1/-1
#[Out]# 8011  8503adbd9d49  Tobias Bell <tobias.bell@gmail.com>     1: +60/-21
#[Out]# 8010  4946ecb3c6fa  Tobias Bell <tobias.bell@gmail.com>     1: +13/-13
#[Out]# 7985  d77960ae81a9  Tobias Bell <tobias.bell@gmail.com>     1: +18/-17
#[Out]# 7984  b08be68bbc4f  Tobias Bell <tobias.bell@gmail.com>      1: +15/-7
#[Out]# 7983  32658c155522  Tobias Bell <tobias.bell@gmail.com>     1: +40/-32
#[Out]# 7982  0e95d41939c3  Tobias Bell <tobias.bell@gmail.com>      1: +20/-1
#[Out]# 7960  28b5cc18baa2  Tobias Bell <tobias.bell@gmail.com>   1: +246/-135
#[Out]# 7949  ccc6531e6db8  Tobias Bell <tobias.bell@gmail.com>       1: +2/-2
#[Out]# 7948  5c9c87ec4693  Tobias Bell <tobias.bell@gmail.com>       1: +7/-8
#[Out]# 7947  a5460b2425e3  Tobias Bell <tobias.bell@gmail.com>       1: +4/-4
#[Out]# 7946  78c9996fb7ee  Tobias Bell <tobias.bell@gmail.com>     1: +25/-25
#[Out]# 7941  606723f4a327  Tobias Bell <tobias.bell@gmail.com>       1: +8/-2
#[Out]# 7935  c2ecaf63bade  Tobias Bell <tobias.bell@gmail.com>    1: +9626/-0), ('Tristan Wibberley <tristan@wibberley.org>',              node                                     author changestr
#[Out]# n                                                                     
#[Out]# 854  473c030d34a6  Tristan Wibberley <tristan@wibberley.org>  1: +2/-2), ('Vadim Gelfer <vadim.gelfer@gmail.com>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 476 entries, 3008 to 1398
#[Out]# Data columns:
#[Out]# node         476  non-null values
#[Out]# author       476  non-null values
#[Out]# changestr    476  non-null values
#[Out]# dtypes: object(3)), ('Vadim Gelfer <vadim.gelger@gmail.com>',               node                                 author    changestr
#[Out]# n                                                                     
#[Out]# 1827  26dd4ae77b7b  Vadim Gelfer <vadim.gelger@gmail.com>    1: +9/-18
#[Out]# 1826  f3abe0bdccdd  Vadim Gelfer <vadim.gelger@gmail.com>  1: +121/-11), ('Valentino Volonghi aka dialtone <dialtone@divmod.com>',               node                                             author changestr
#[Out]# n                                                                              
#[Out]# 2583  6e5427447f4c  Valentino Volonghi aka dialtone <dialtone@divmod.  2: +5/-1), ('Vasily Titskiy <qehgt0@gmail.com>',                node                             author changestr
#[Out]# n                                                               
#[Out]# 14845  a115b5ee9c63  Vasily Titskiy <qehgt0@gmail.com>  1: +1/-1), ('Vincent Danjean',               node           author changestr
#[Out]# n                                            
#[Out]# 1341  3ab6e55ee361  Vincent Danjean  2: +2/-2
#[Out]# 1340  faa62c7685fb  Vincent Danjean  1: +1/-3
#[Out]# 1339  f351d1a07d75  Vincent Danjean  1: +0/-2), ('Vincent Danjean <Vincent.Danjean@ens-lyon.org>',               node                                          author changestr
#[Out]# n                                                                           
#[Out]# 1614  0952d164030e  Vincent Danjean <Vincent.Danjean@ens-lyon.org>  1: +0/-2), ('Vincent Danjean <vdanjean@free.fr>',               node                              author changestr
#[Out]# n                                                               
#[Out]# 2149  43ce1c17e644  Vincent Danjean <vdanjean@free.fr>  1: +2/-1), ('Vincent Wagelaar <vincent@ricardis.tudelft.nl>',               node                                          author   changestr
#[Out]# n                                                                             
#[Out]# 1181  4f5001f5b4c3  Vincent Wagelaar <vincent@ricardis.tudelft.nl>    1: +7/-4
#[Out]# 1180  fe3eb1628c40  Vincent Wagelaar <vincent@ricardis.tudelft.nl>   1: +3/-10
#[Out]# 1163  dacd3463ee3f  Vincent Wagelaar <vincent@ricardis.tudelft.nl>    1: +2/-2
#[Out]# 1162  91db1c90b20d  Vincent Wagelaar <vincent@ricardis.tudelft.nl>    1: +1/-3
#[Out]# 1161  7654d8f2ccf6  Vincent Wagelaar <vincent@ricardis.tudelft.nl>    1: +2/-3
#[Out]# 1160  0da98529a476  Vincent Wagelaar <vincent@ricardis.tudelft.nl>    1: +2/-0
#[Out]# 1159  b6f5a947e62e  Vincent Wagelaar <vincent@ricardis.tudelft.nl>  1: +96/-83), ('Vishakh H <vsh426@gmail.com>',                node                        author  changestr
#[Out]# n                                                           
#[Out]# 12114  3361075816f8  Vishakh H <vsh426@gmail.com>  1: +20/-3
#[Out]# 12113  62e2bbf523f2  Vishakh H <vsh426@gmail.com>  1: +13/-6
#[Out]# 11910  46ac30b17978  Vishakh H <vsh426@gmail.com>  1: +11/-3
#[Out]# 11909  138c055ec57d  Vishakh H <vsh426@gmail.com>   1: +9/-4
#[Out]# 11837  6b7b99867ada  Vishakh H <vsh426@gmail.com>  1: +21/-0
#[Out]# 11539  64f284da1278  Vishakh H <vsh426@gmail.com>  4: +43/-3
#[Out]# 11462  1b82a26635d7  Vishakh H <vsh426@gmail.com>  3: +55/-9), ('Volker Kleinfeld <Volker.Kleinfeld@gmx.de>',               node                                      author   changestr
#[Out]# n                                                                         
#[Out]# 2981  0171a5432621  Volker Kleinfeld <Volker.Kleinfeld@gmx.de>    1: +7/-1
#[Out]# 2443  bd9c39e8f38b  Volker Kleinfeld <Volker.Kleinfeld@gmx.de>   1: +10/-2
#[Out]# 2323  c58a403aa830  Volker Kleinfeld <Volker.Kleinfeld@gmx.de>  2: +18/-12
#[Out]# 2322  685597676a13  Volker Kleinfeld <Volker.Kleinfeld@gmx.de>   1: +34/-7
#[Out]# 2314  e9b5749e4de3  Volker Kleinfeld <Volker.Kleinfeld@gmx.de>    1: +1/-1
#[Out]# 2285  0912f807b7ff  Volker Kleinfeld <Volker.Kleinfeld@gmx.de>    1: +5/-1
#[Out]# 2284  d6392a7c03dd  Volker Kleinfeld <Volker.Kleinfeld@gmx.de>   2: +17/-2
#[Out]# 1422  a7e8408ac79c  Volker Kleinfeld <Volker.Kleinfeld@gmx.de>   1: +15/-0
#[Out]# 1421  a7631cf1326a  Volker Kleinfeld <Volker.Kleinfeld@gmx.de>    1: +2/-0
#[Out]# 1285  1546c2aa6b30  Volker Kleinfeld <Volker.Kleinfeld@gmx.de>  2: +28/-12), ('Volker.Kleinfeld@gmx.de',               node                   author   changestr
#[Out]# n                                                      
#[Out]# 1283  f5faab34f32e  Volker.Kleinfeld@gmx.de  2: +106/-2
#[Out]# 1075  e254bcbfe636  Volker.Kleinfeld@gmx.de    1: +2/-0), ('Vsevolod Solovyov <vsevolod.solovyov@gmail.com>',                node                                           author  changestr
#[Out]# n                                                                              
#[Out]# 10326  d9a2bc2f776b  Vsevolod Solovyov <vsevolod.solovyov@gmail.com>   2: +4/-3
#[Out]# 7882   6ea0318daf75  Vsevolod Solovyov <vsevolod.solovyov@gmail.com>  3: +22/-1), ('Wagner Bruna <wbruna@softwareexpress.com.br>', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 219 entries, 16655 to 8147
#[Out]# Data columns:
#[Out]# node         219  non-null values
#[Out]# author       219  non-null values
#[Out]# changestr    219  non-null values
#[Out]# dtypes: object(3)), ('Wagner Bruna <wbruna@yahoo.com>',                node                           author        changestr
#[Out]# n                                                                    
#[Out]# 16638  4cf41c333e74  Wagner Bruna <wbruna@yahoo.com>         1: +3/-0
#[Out]# 16631  b748106fe616  Wagner Bruna <wbruna@yahoo.com>       1: +37/-25
#[Out]# 16560  f2a3ce017355  Wagner Bruna <wbruna@yahoo.com>       1: +32/-18
#[Out]# 16545  4b093c30a5f0  Wagner Bruna <wbruna@yahoo.com>       1: +83/-40
#[Out]# 16544  3d81780deb78  Wagner Bruna <wbruna@yahoo.com>    1: +1501/-711
#[Out]# 16519  9c196f38f9f5  Wagner Bruna <wbruna@yahoo.com>       1: +48/-17
#[Out]# 16518  80d940066176  Wagner Bruna <wbruna@yahoo.com>    1: +1221/-649
#[Out]# 16517  63e24ec0ef8b  Wagner Bruna <wbruna@yahoo.com>    1: +1221/-649
#[Out]# 16230  94aa8a41f1d9  Wagner Bruna <wbruna@yahoo.com>         1: +2/-2
#[Out]# 16229  fb022810bf16  Wagner Bruna <wbruna@yahoo.com>         3: +9/-8
#[Out]# 16228  e6c87c46c795  Wagner Bruna <wbruna@yahoo.com>       1: +13/-12
#[Out]# 16227  f45e7f09c0b1  Wagner Bruna <wbruna@yahoo.com>         1: +3/-2
#[Out]# 16067  bf798234f983  Wagner Bruna <wbruna@yahoo.com>         1: +3/-3
#[Out]# 16066  eee86643037c  Wagner Bruna <wbruna@yahoo.com>         1: +5/-4
#[Out]# 16065  da8e7da0b198  Wagner Bruna <wbruna@yahoo.com>         1: +1/-1
#[Out]# 16064  d151c5d9f5fd  Wagner Bruna <wbruna@yahoo.com>       1: +13/-12
#[Out]# 16063  a27aab28047c  Wagner Bruna <wbruna@yahoo.com>         1: +2/-2
#[Out]# 16015  2494a8b42dfb  Wagner Bruna <wbruna@yahoo.com>      1: +234/-10
#[Out]# 15506  be3173353094  Wagner Bruna <wbruna@yahoo.com>       1: +49/-17
#[Out]# 14866  c004d5550243  Wagner Bruna <wbruna@yahoo.com>        1: +32/-8
#[Out]# 14865  7f504202cb5c  Wagner Bruna <wbruna@yahoo.com>         1: +1/-1
#[Out]# 14747  fdcf6f09b68d  Wagner Bruna <wbruna@yahoo.com>         1: +1/-1
#[Out]# 13595  2347feb35691  Wagner Bruna <wbruna@yahoo.com>         1: +4/-4
#[Out]# 13512  0a6bca3d5273  Wagner Bruna <wbruna@yahoo.com>        1: +18/-2
#[Out]# 13499  28cc153cb033  Wagner Bruna <wbruna@yahoo.com>       1: +40/-23
#[Out]# 13095  318872681e5e  Wagner Bruna <wbruna@yahoo.com>        1: +2/-36
#[Out]# 13094  bf3e019938ec  Wagner Bruna <wbruna@yahoo.com>       1: +38/-36
#[Out]# 13039  a6c855c32ea0  Wagner Bruna <wbruna@yahoo.com>     1: +307/-292
#[Out]# 12976  acebcefa86d4  Wagner Bruna <wbruna@yahoo.com>        1: +26/-7
#[Out]# 12938  062ae1aeb84d  Wagner Bruna <wbruna@yahoo.com>        1: +2/-36
#[Out]# 12901  80076785e150  Wagner Bruna <wbruna@yahoo.com>       1: +31/-21
#[Out]# 12883  6f6f6a9c2a41  Wagner Bruna <wbruna@yahoo.com>     1: +316/-264
#[Out]# 12859  76066903ae08  Wagner Bruna <wbruna@yahoo.com>         1: +1/-1
#[Out]# 12858  6eec9d7c6e0f  Wagner Bruna <wbruna@yahoo.com>         1: +1/-1
#[Out]# 12855  d01c21002e82  Wagner Bruna <wbruna@yahoo.com>         1: +3/-2
#[Out]# 12854  5d3f3d577218  Wagner Bruna <wbruna@yahoo.com>         1: +2/-1
#[Out]# 12788  9aae04f4fcf6  Wagner Bruna <wbruna@yahoo.com>        2: +21/-4
#[Out]# 12571  a2577df1e163  Wagner Bruna <wbruna@yahoo.com>  2: +8711/-12221
#[Out]# 11734  34a9a71d586c  Wagner Bruna <wbruna@yahoo.com>        1: +32/-2
#[Out]# 11720  1717df90da17  Wagner Bruna <wbruna@yahoo.com>       1: +21/-21
#[Out]# 11719  82120bc66577  Wagner Bruna <wbruna@yahoo.com>         1: +3/-3
#[Out]# 11718  b4b0c63a2ed6  Wagner Bruna <wbruna@yahoo.com>         1: +9/-9
#[Out]# 11715  cf1df979956e  Wagner Bruna <wbruna@yahoo.com>       1: +6/-182
#[Out]# 11682  7853a550a61b  Wagner Bruna <wbruna@yahoo.com>         1: +5/-5
#[Out]# 11681  01ef7949691e  Wagner Bruna <wbruna@yahoo.com>       1: +228/-0
#[Out]# 11575  c00f03a4982e  Wagner Bruna <wbruna@yahoo.com>         1: +2/-2
#[Out]# 11574  c28081fa920c  Wagner Bruna <wbruna@yahoo.com>        1: +24/-8
#[Out]# 11567  bf1774d95bde  Wagner Bruna <wbruna@yahoo.com>        1: +19/-3
#[Out]# 11566  0b8d17bb8b2d  Wagner Bruna <wbruna@yahoo.com>    38: +333/-144
#[Out]# 11565  281a812297cc  Wagner Bruna <wbruna@yahoo.com>        1: +19/-4
#[Out]# 11525  6f44bd4cc4f2  Wagner Bruna <wbruna@yahoo.com>       1: +35/-23
#[Out]# 11524  89ef60af92e9  Wagner Bruna <wbruna@yahoo.com>       5: +45/-18
#[Out]# 11478  13d02d6677f2  Wagner Bruna <wbruna@yahoo.com>       1: +13/-16
#[Out]# 11477  9374e3c214f9  Wagner Bruna <wbruna@yahoo.com>       9: +60/-34
#[Out]# 11390  11cd65611f3f  Wagner Bruna <wbruna@yahoo.com>         2: +2/-1
#[Out]# 11389  4fd49329a1b5  Wagner Bruna <wbruna@yahoo.com>        1: +56/-0
#[Out]# 11387  181936ec9bfb  Wagner Bruna <wbruna@yahoo.com>      2: +1695/-0
#[Out]# 11255  1893867231d1  Wagner Bruna <wbruna@yahoo.com>       1: +46/-17
#[Out]# 11126  23295cedf7f1  Wagner Bruna <wbruna@yahoo.com>       1: +55/-17
#[Out]# 11093  d02b5c528dca  Wagner Bruna <wbruna@yahoo.com>       1: +64/-47
#[Out]# 11092  08e6048592a8  Wagner Bruna <wbruna@yahoo.com>     1: +179/-135
#[Out]# 10781  f4a8478dcd3f  Wagner Bruna <wbruna@yahoo.com>       1: +46/-17
#[Out]# 10747  39f725929f0c  Wagner Bruna <wbruna@yahoo.com>       1: +55/-17
#[Out]# 10731  0425f1fdf3a8  Wagner Bruna <wbruna@yahoo.com>       1: +64/-47
#[Out]# 10730  d16315e811de  Wagner Bruna <wbruna@yahoo.com>       1: +56/-41
#[Out]# 10472  9126d13bad7a  Wagner Bruna <wbruna@yahoo.com>         1: +2/-2
#[Out]# 9864   6feb002417e9  Wagner Bruna <wbruna@yahoo.com>      1: +31/-398
#[Out]# 9566   b9995b9c0d63  Wagner Bruna <wbruna@yahoo.com>   1: +2090/-1947
#[Out]# 9565   125958a03630  Wagner Bruna <wbruna@yahoo.com>       1: +18/-20
#[Out]# 9415   c47693630e72  Wagner Bruna <wbruna@yahoo.com>       1: +49/-54
#[Out]# 9138   02c27a451cbf  Wagner Bruna <wbruna@yahoo.com>       1: +18/-20
#[Out]# 9091   e15bc0433897  Wagner Bruna <wbruna@yahoo.com>       1: +30/-27
#[Out]# 8978   2656a5b40c7b  Wagner Bruna <wbruna@yahoo.com>       1: +61/-36
#[Out]# 8119   388bb482024e  Wagner Bruna <wbruna@yahoo.com>         1: +5/-4
#[Out]# 8118   67efe5e3b0fb  Wagner Bruna <wbruna@yahoo.com>         1: +5/-2
#[Out]# 8117   bdeb380a10de  Wagner Bruna <wbruna@yahoo.com>        1: +10/-4
#[Out]# 8116   6dcf425cc2a6  Wagner Bruna <wbruna@yahoo.com>         1: +1/-1
#[Out]# 8115   89b6450148d0  Wagner Bruna <wbruna@yahoo.com>         1: +1/-1
#[Out]# 8053   76e4c08a48ad  Wagner Bruna <wbruna@yahoo.com>         2: +2/-2
#[Out]# 8052   36924a4711e9  Wagner Bruna <wbruna@yahoo.com>         1: +4/-2
#[Out]# 7973   edf2d83a11aa  Wagner Bruna <wbruna@yahoo.com>         1: +4/-3), ('Walter Doerwald <walter@livinglogic.de>',               node                                   author changestr
#[Out]# n                                                                    
#[Out]# 6140  47e6d5d5913a  Walter Doerwald <walter@livinglogic.de>  1: +3/-5), ('Waqas Hussain <waqas20@gmail.com>',                node                             author changestr
#[Out]# n                                                               
#[Out]# 13467  31aa2e5b0750  Waqas Hussain <waqas20@gmail.com>  1: +2/-1), ('Weijun Wang <weijun.wang@sun.com>',               node                             author changestr
#[Out]# n                                                              
#[Out]# 6471  2519976a998b  Weijun Wang <weijun.wang@sun.com>  1: +8/-4), ('Wes Turner <wes@wrd.nu>',                node                   author    changestr
#[Out]# n                                                        
#[Out]# 16663  43c6b542c85c  Wes Turner <wes@wrd.nu>     0: +0/-0
#[Out]# 16662  e78ebfbbd72d  Wes Turner <wes@wrd.nu>    2: +71/-0
#[Out]# 16661  51064efff902  Wes Turner <wes@wrd.nu>  20: +67/-25
#[Out]# 16660  ba5d77da40df  Wes Turner <wes@wrd.nu>    2: +12/-1
#[Out]# 16659  000d427d9340  Wes Turner <wes@wrd.nu>     1: +7/-1), ('Wesley J. Landaker <wjl@icecavern.net>',               node                                  author changestr
#[Out]# n                                                                   
#[Out]# 5011  419a6f715c6a  Wesley J. Landaker <wjl@icecavern.net>  1: +3/-2
#[Out]# 5009  8f430b1b3025  Wesley J. Landaker <wjl@icecavern.net>  1: +7/-1
#[Out]# 5008  be591b740e0f  Wesley J. Landaker <wjl@icecavern.net>  1: +1/-1
#[Out]# 5006  8be7ba425621  Wesley J. Landaker <wjl@icecavern.net>  1: +9/-2), ('Will <will@glozer.net>',               node                  author changestr
#[Out]# n                                                   
#[Out]# 1548  18f3224da392  Will <will@glozer.net>  1: +1/-1), ('Will Maier <willmaier@ml1.net>',                node                          author   changestr
#[Out]# n                                                              
#[Out]# 12358  4ab87473029d  Will Maier <willmaier@ml1.net>   1: +65/-0
#[Out]# 12357  6ad36bca3a8a  Will Maier <willmaier@ml1.net>    1: +4/-2
#[Out]# 8724   2816239e0020  Will Maier <willmaier@ml1.net>  2: +26/-36
#[Out]# 8723   da1b93583855  Will Maier <willmaier@ml1.net>    1: +1/-1
#[Out]# 7768   b2410ed2cbe9  Will Maier <willmaier@ml1.net>    1: +2/-2
#[Out]# 5882   59fba5caa94b  Will Maier <willmaier@ml1.net>    1: +2/-2
#[Out]# 3022   d9b8d28c0b94  Will Maier <willmaier@ml1.net>    1: +4/-2
#[Out]# 2672   118b198c9423  Will Maier <willmaier@ml1.net>    1: +1/-1), ('Wojciech Milkowski <wmilkowski@interia.pl>',               node                                      author   changestr
#[Out]# n                                                                         
#[Out]# 3244  f045b049a704  Wojciech Milkowski <wmilkowski@interia.pl>    1: +1/-1
#[Out]# 1077  b87aeccf73d9  Wojciech Milkowski <wmilkowski@interia.pl>  3: +64/-67
#[Out]# 1076  01db658cc78a  Wojciech Milkowski <wmilkowski@interia.pl>   2: +88/-3), ('Wojciech Mi\xc5\x82kowski <wmilkowski@interia.pl>',               node                                      author  changestr
#[Out]# n                                                                        
#[Out]# 6668  f2abfca4beb8  Wojciech Miłkowski <wmilkowski@interia.pl>  1: +1/-1), ('Wolfgang Treutterer <Wolfgang.Treutterer@ipp.mpg.de>',                node                                             author changestr
#[Out]# n                                                                               
#[Out]# 16437  e98460f6089d  Wolfgang Treutterer <Wolfgang.Treutterer@ipp.mpg.  1: +3/-3), ('Xavier ALT <dex@phoenix-ind.net>',               node                            author changestr
#[Out]# n                                                             
#[Out]# 7857  cb77c0fbec39  Xavier ALT <dex@phoenix-ind.net>  1: +1/-0), ('Xavier Snelgrove <xs@wxs.ca>',                node                        author changestr
#[Out]# n                                                          
#[Out]# 12067  4532c44bb62d  Xavier Snelgrove <xs@wxs.ca>  1: +2/-2), ('Xiaofeng Ling <xiaofeng.ling@intel.com>',               node                                   author changestr
#[Out]# n                                                                    
#[Out]# 1890  d4545f1b8bfa  Xiaofeng Ling <xiaofeng.ling@intel.com>  1: +3/-0), ('Yann E. MORIN <yann.morin.1998@anciens.enib.fr>',               node                                           author  changestr
#[Out]# n                                                                             
#[Out]# 9413  4cc0815a0dd4  Yann E. MORIN <yann.morin.1998@anciens.enib.fr>   1: +4/-4
#[Out]# 9412  2b1260436f83  Yann E. MORIN <yann.morin.1998@anciens.enib.fr>  2: +23/-4
#[Out]# 9411  dd6f605b15c0  Yann E. MORIN <yann.morin.1998@anciens.enib.fr>  3: +13/-5
#[Out]# 9410  6eaadd777bc4  Yann E. MORIN <yann.morin.1998@anciens.enib.fr>   1: +8/-0
#[Out]# 9409  08f59f7916f9  Yann E. MORIN <yann.morin.1998@anciens.enib.fr>   1: +1/-1), ('Yannick Gingras <ygingras@ygingras.net>',               node                                   author  changestr
#[Out]# n                                                                     
#[Out]# 9725  3f522d2fa633  Yannick Gingras <ygingras@ygingras.net>  9: +77/-5), ('Yun Lee <yun.lee.bj@gmail.com>',                node                          author       changestr
#[Out]# n                                                                  
#[Out]# 14473  ff4126ce9301  Yun Lee <yun.lee.bj@gmail.com>  2: +1158/-1154
#[Out]# 14472  59853c30e31e  Yun Lee <yun.lee.bj@gmail.com>       1: +11/-0
#[Out]# 14083  0528b69f8db4  Yun Lee <yun.lee.bj@gmail.com>      5: +93/-78), ('Yun Lee <yunlee.bj@gmail.com>',                node                         author   changestr
#[Out]# n                                                             
#[Out]# 13950  9a96efc4af8a  Yun Lee <yunlee.bj@gmail.com>    2: +8/-0
#[Out]# 13949  9e5407a67dea  Yun Lee <yunlee.bj@gmail.com>  3: +46/-42
#[Out]# 13929  28f557e8b419  Yun Lee <yunlee.bj@gmail.com>   2: +16/-0), ('Yuya Nishihara <yuya@tcha.org>',                node                          author     changestr
#[Out]# n                                                                
#[Out]# 16604  fcb97d9a26cd  Yuya Nishihara <yuya@tcha.org>     2: +22/-2
#[Out]# 16575  46e9ed223d2c  Yuya Nishihara <yuya@tcha.org>      4: +8/-9
#[Out]# 15523  012b285cf643  Yuya Nishihara <yuya@tcha.org>     2: +28/-1
#[Out]# 15388  eb6c0d47c3d5  Yuya Nishihara <yuya@tcha.org>    1: +14/-13
#[Out]# 14620  2b9c32929e62  Yuya Nishihara <yuya@tcha.org>     1: +14/-6
#[Out]# 14539  558ec14ba6be  Yuya Nishihara <yuya@tcha.org>     1: +17/-0
#[Out]# 14538  3818c67a501e  Yuya Nishihara <yuya@tcha.org>     2: +34/-2
#[Out]# 14530  cd31a1cc1521  Yuya Nishihara <yuya@tcha.org>      1: +2/-4
#[Out]# 14186  a8f136f430da  Yuya Nishihara <yuya@tcha.org>      1: +1/-1
#[Out]# 13979  ea726c97c1b6  Yuya Nishihara <yuya@tcha.org>     4: +48/-0
#[Out]# 13978  2176c5babd53  Yuya Nishihara <yuya@tcha.org>      1: +3/-6
#[Out]# 13977  b8dd2e95b0ca  Yuya Nishihara <yuya@tcha.org>      2: +9/-8
#[Out]# 13976  4788923a2b33  Yuya Nishihara <yuya@tcha.org>      2: +6/-0
#[Out]# 13608  e33ebe67657a  Yuya Nishihara <yuya@tcha.org>     1: +13/-0
#[Out]# 13607  fd8a6ca3a750  Yuya Nishihara <yuya@tcha.org>    19: +61/-0
#[Out]# 13606  b602ac02f1ba  Yuya Nishihara <yuya@tcha.org>     8: +28/-7
#[Out]# 13605  4d0a7d70866b  Yuya Nishihara <yuya@tcha.org>      1: +8/-1
#[Out]# 13604  e8f50febc2d4  Yuya Nishihara <yuya@tcha.org>      2: +5/-4
#[Out]# 13603  b5b84dd43613  Yuya Nishihara <yuya@tcha.org>    19: +66/-0
#[Out]# 13602  78acaca60243  Yuya Nishihara <yuya@tcha.org>      2: +2/-2
#[Out]# 13601  1046cb663776  Yuya Nishihara <yuya@tcha.org>     6: +35/-0
#[Out]# 13592  5c18a0bca26f  Yuya Nishihara <yuya@tcha.org>     7: +21/-5
#[Out]# 13034  a939f08fae9c  Yuya Nishihara <yuya@tcha.org>    6: +34/-10
#[Out]# 13021  75d0c38a0bca  Yuya Nishihara <yuya@tcha.org>     2: +29/-5
#[Out]# 13020  00411a4fa1bb  Yuya Nishihara <yuya@tcha.org>      2: +9/-1
#[Out]# 13012  e3bf16703e26  Yuya Nishihara <yuya@tcha.org>     2: +61/-4
#[Out]# 12999  d83566f4453b  Yuya Nishihara <yuya@tcha.org>      1: +2/-2
#[Out]# 12931  5f80f44d23c5  Yuya Nishihara <yuya@tcha.org>      1: +1/-6
#[Out]# 12902  a63902f98942  Yuya Nishihara <yuya@tcha.org>  1: +604/-604
#[Out]# 12845  685d884fd2b6  Yuya Nishihara <yuya@tcha.org>      1: +4/-2
#[Out]# 12724  22f45e53bb21  Yuya Nishihara <yuya@tcha.org>    1: +12/-12
#[Out]# 12723  d4e21a9de8bc  Yuya Nishihara <yuya@tcha.org>      1: +2/-0
#[Out]# 12322  1ed2dc9d4368  Yuya Nishihara <yuya@tcha.org>      1: +6/-1
#[Out]# 11917  46039b2af349  Yuya Nishihara <yuya@tcha.org>      1: +1/-0
#[Out]# 11635  9617803b1acb  Yuya Nishihara <yuya@tcha.org>     3: +61/-0
#[Out]# 11611  9dac951d0185  Yuya Nishihara <yuya@tcha.org>     2: +10/-4
#[Out]# 11585  aff419e260f9  Yuya Nishihara <yuya@tcha.org>     3: +20/-2
#[Out]# 11501  0c944b7af564  Yuya Nishihara <yuya@tcha.org>     5: +22/-0
#[Out]# 11497  fbab0875fd09  Yuya Nishihara <yuya@tcha.org>     3: +51/-1
#[Out]# 11414  0fa4474bdc2f  Yuya Nishihara <yuya@tcha.org>      1: +3/-0
#[Out]# 11234  4d8db9676171  Yuya Nishihara <yuya@tcha.org>      1: +1/-1
#[Out]# 11232  0c0088881562  Yuya Nishihara <yuya@tcha.org>      1: +1/-0
#[Out]# 11230  2313dc4d9817  Yuya Nishihara <yuya@tcha.org>   20: +20/-20
#[Out]# 11229  1d714c1546b5  Yuya Nishihara <yuya@tcha.org>      1: +5/-1
#[Out]# 11210  b25464e9b448  Yuya Nishihara <yuya@tcha.org>      1: +1/-1
#[Out]# 11118  51d0387523c6  Yuya Nishihara <yuya@tcha.org>     5: +22/-8
#[Out]# 11109  5d35f7d93514  Yuya Nishihara <yuya@tcha.org>    3: +27/-33
#[Out]# 11108  a84f14228b1d  Yuya Nishihara <yuya@tcha.org>      3: +6/-2
#[Out]# 11079  45351e65230b  Yuya Nishihara <yuya@tcha.org>      1: +0/-1
#[Out]# 10718  f1250e2e8fd1  Yuya Nishihara <yuya@tcha.org>      1: +4/-3
#[Out]# 10617  3c05ecffe20d  Yuya Nishihara <yuya@tcha.org>      1: +1/-3
#[Out]# 10616  6d87c20cd7a8  Yuya Nishihara <yuya@tcha.org>     3: +68/-6
#[Out]# 10615  9848b39a1472  Yuya Nishihara <yuya@tcha.org>      1: +6/-4
#[Out]# 10596  7648f32713f2  Yuya Nishihara <yuya@tcha.org>      2: +2/-2
#[Out]# 10566  992723445a29  Yuya Nishihara <yuya@tcha.org>      3: +7/-2
#[Out]# 10563  6ded6243bde2  Yuya Nishihara <yuya@tcha.org>      2: +3/-2
#[Out]# 9832   42ced358cbba  Yuya Nishihara <yuya@tcha.org>      1: +1/-2
#[Out]# 9793   ec8533806e27  Yuya Nishihara <yuya@tcha.org>   1: +77/-135
#[Out]# 9661   c4f6c02e33c4  Yuya Nishihara <yuya@tcha.org>     2: +25/-0
#[Out]# 9660   e0eae93e6c67  Yuya Nishihara <yuya@tcha.org>    2: +11/-11
#[Out]# 9651   bd3af545c7c6  Yuya Nishihara <yuya@tcha.org>      1: +2/-2
#[Out]# 9108   799373ff2554  Yuya Nishihara <yuya@tcha.org>     3: +47/-8), ('Zachary Gramana <zgramana@pottsconsultinggroup.com>',                node                                             author  changestr
#[Out]# n                                                                                
#[Out]# 14319  bb7e3b3e6e11  Zachary Gramana <zgramana@pottsconsultinggroup.co  1: +14/-4
#[Out]# 14234  c1cca38818b9  Zachary Gramana <zgramana@pottsconsultinggroup.co   1: +3/-1), ('Zbynek Winkler <zwin@users.sourceforge.net>',               node                                       author  changestr
#[Out]# n                                                                         
#[Out]# 1399  9a70776e355e  Zbynek Winkler <zwin@users.sourceforge.net>  1: +10/-1), ('Zhigang Wang <w1z2g3@gmail.com>',                node                           author changestr
#[Out]# n                                                             
#[Out]# 10008  b3b57ecbda50  Zhigang Wang <w1z2g3@gmail.com>  3: +3/-0), ('Zhigang Wang <zhigang.x.wang@oracle.com>',                node                                    author  changestr
#[Out]# n                                                                       
#[Out]# 13250  f05250572467  Zhigang Wang <zhigang.x.wang@oracle.com>  2: +15/-8), ('Zoran Bosnjak <zoran.bosnjak@via.si>',               node                                author  changestr
#[Out]# n                                                                  
#[Out]# 6200  acc40572da5b  Zoran Bosnjak <zoran.bosnjak@via.si>  4: +64/-0), ('anatoly techtonik <techtonik@gmail.com>',                node                                   author changestr
#[Out]# n                                                                     
#[Out]# 10714  d703906d02ab  anatoly techtonik <techtonik@gmail.com>  1: +4/-0), ('andrea@suse.de',               node          author  changestr
#[Out]# n                                            
#[Out]# 2482  818ebebc4554  andrea@suse.de   1: +1/-1
#[Out]# 2460  605e26a2e96e  andrea@suse.de  1: +17/-6), ('bdowning@lavos.net',               node              author changestr
#[Out]# n                                               
#[Out]# 5584  be20a42f27a1  bdowning@lavos.net  1: +3/-3), ('benoit.boissinot@ens-lyon.fr',               node                        author     changestr
#[Out]# n                                                             
#[Out]# 1062  6d5a62a549fa  benoit.boissinot@ens-lyon.fr  8: +100/-100), ('bos@eng-25.internal.keyresearch.com',               node                               author    changestr
#[Out]# n                                                                   
#[Out]# 1038  5f191561a061  bos@eng-25.internal.keyresearch.com     1: +6/-8
#[Out]# 1002  254ab35709e6  bos@eng-25.internal.keyresearch.com  2: +307/-26), ('bos@serpentine.internal.keyresearch.com',               node                                   author     changestr
#[Out]# n                                                                        
#[Out]# 1194  c165cbf56bb1  bos@serpentine.internal.keyresearch.com      1: +1/-0
#[Out]# 1193  04d1ca8ae9ec  bos@serpentine.internal.keyresearch.com      1: +3/-2
#[Out]# 1191  77a0c7528c2f  bos@serpentine.internal.keyresearch.com     2: +6/-24
#[Out]# 1190  737f9b90c571  bos@serpentine.internal.keyresearch.com     2: +15/-1
#[Out]# 1187  120aa5fc7ced  bos@serpentine.internal.keyresearch.com     2: +24/-6
#[Out]# 1186  508c7d1b3e1c  bos@serpentine.internal.keyresearch.com   3: +145/-87
#[Out]# 1184  9462df772bc8  bos@serpentine.internal.keyresearch.com    2: +17/-17
#[Out]# 1154  c3cb9f39a91f  bos@serpentine.internal.keyresearch.com      1: +7/-5
#[Out]# 1148  fad2d091c74f  bos@serpentine.internal.keyresearch.com     1: +10/-0
#[Out]# 1147  d32b91ebad5d  bos@serpentine.internal.keyresearch.com   12: +78/-93
#[Out]# 1146  9061f79c6c6f  bos@serpentine.internal.keyresearch.com   3: +149/-47
#[Out]# 1059  4eab07ef66e2  bos@serpentine.internal.keyresearch.com     1: +11/-7
#[Out]# 1037  c0a1abf562eb  bos@serpentine.internal.keyresearch.com      1: +6/-1
#[Out]# 1024  5b257e419816  bos@serpentine.internal.keyresearch.com     1: +14/-2
#[Out]# 1011  d06420c90d8b  bos@serpentine.internal.keyresearch.com      1: +4/-5
#[Out]# 1004  ad6fcceaf59b  bos@serpentine.internal.keyresearch.com    1: +32/-17
#[Out]# 1003  6dfc9cc71f42  bos@serpentine.internal.keyresearch.com  1: +197/-127), ('bttfmcf <bttf.mcf@gmail.com>',                node                        author     changestr
#[Out]# n                                                              
#[Out]# 10929  318da45f907c  bttfmcf <bttf.mcf@gmail.com>  1: +129/-208), ('byron@base2.cc',               node          author changestr
#[Out]# n                                           
#[Out]# 6877  694223a29ad4  byron@base2.cc  1: +5/-2), ('chad.netzer@gmail.com',              node                 author   changestr
#[Out]# n                                                   
#[Out]# 674  6513ba7d858a  chad.netzer@gmail.com  3: +10/-10), ('csaba.henk@creo.hu',               node              author   changestr
#[Out]# n                                                 
#[Out]# 4731  1d5a2ee683b0  csaba.henk@creo.hu    1: +1/-1
#[Out]# 4652  06de65673ec2  csaba.henk@creo.hu   1: +42/-2
#[Out]# 4218  705d0792dbf2  csaba.henk@creo.hu  1: +52/-17), ('demian@gaudron.lan',               node              author   changestr
#[Out]# n                                                 
#[Out]# 2374  ffc2ed61061b  demian@gaudron.lan    1: +2/-1
#[Out]# 2373  61976a27aa2b  demian@gaudron.lan    1: +3/-3
#[Out]# 2372  449906e17576  demian@gaudron.lan    1: +1/-1
#[Out]# 2371  e39300cdb8ff  demian@gaudron.lan    1: +2/-4
#[Out]# 2370  de893ad6bd17  demian@gaudron.lan    1: +2/-8
#[Out]# 2369  9da3dd62c827  demian@gaudron.lan  1: +33/-38
#[Out]# 2368  eb1ec13e3b0d  demian@gaudron.lan    1: +5/-2
#[Out]# 2367  8c893af1154a  demian@gaudron.lan    1: +3/-0
#[Out]# 2366  f9f53c7e1875  demian@gaudron.lan    1: +4/-0
#[Out]# 2365  a5d2e5490ac7  demian@gaudron.lan   1: +12/-5
#[Out]# 2364  f368a1c302d5  demian@gaudron.lan  4: +559/-0), ('desgropp <regis.desgroppes@nokia.com>',                node                                 author changestr
#[Out]# n                                                                   
#[Out]# 14500  37901cf0680b  desgropp <regis.desgroppes@nokia.com>  0: +0/-0), ('dhruva <dhruvakm@gmail.com>',               node                       author changestr
#[Out]# n                                                        
#[Out]# 6032  288ec2f6faa2  dhruva <dhruvakm@gmail.com>  1: +1/-1), ('divy@chelsio.com',               node            author changestr
#[Out]# n                                             
#[Out]# 7012  a3fd4aa154af  divy@chelsio.com  1: +4/-2), ('efiring@manini.soest.hawaii.edu',               node                           author changestr
#[Out]# n                                                            
#[Out]# 1635  ae61937c61c5  efiring@manini.soest.hawaii.edu  1: +3/-1), ('eric@localhost.localdomain',               node                      author  changestr
#[Out]# n                                                        
#[Out]# 1279  8ab1c07d4e0b  eric@localhost.localdomain  1: +21/-0), ('etienne <etienne.desautels@gmail.com>',                node                                 author changestr
#[Out]# n                                                                   
#[Out]# 15117  2433525a9e1e  etienne <etienne.desautels@gmail.com>  1: +3/-0), ('greg@maptuit.com',               node            author  changestr
#[Out]# n                                              
#[Out]# 4382  05d15c456fb2  greg@maptuit.com  3: +28/-2), ('hlian',                node author  changestr
#[Out]# n                                    
#[Out]# 16577  5516fdf3fe24  hlian  2: +29/-2), ('jake@edge2.net',              node          author     changestr
#[Out]# n                                              
#[Out]# 196  48827121af7e  jake@edge2.net     4: +49/-1
#[Out]# 181  038e4d8602bd  jake@edge2.net     3: +27/-8
#[Out]# 177  91055f795d88  jake@edge2.net    4: +838/-0
#[Out]# 154  1d5f799ebe1e  jake@edge2.net   10: +51/-54
#[Out]# 153  e8a360cd5a9f  jake@edge2.net    7: +23/-23
#[Out]# 152  67b8d24d2dbe  jake@edge2.net      1: +1/-1
#[Out]# 136  0e8d60d2bb2b  jake@edge2.net     3: +46/-7
#[Out]# 135  c0faf50822ea  jake@edge2.net    1: +22/-16
#[Out]# 134  13d609f8d830  jake@edge2.net      1: +3/-2
#[Out]# 133  fb84d3e71042  jake@edge2.net  8: +189/-117
#[Out]# 132  210eeb6f5197  jake@edge2.net    1: +93/-83
#[Out]# 131  c9d51742471c  jake@edge2.net  2: +377/-377
#[Out]# 103  33500fe7d56c  jake@edge2.net     1: +21/-3
#[Out]# 101  6da5cf0c4193  jake@edge2.net    1: +119/-6
#[Out]# 100  526722d24ee5  jake@edge2.net  1: +179/-145
#[Out]# 99   db5eb6a86179  jake@edge2.net     1: +12/-9), ('jakob krainz <jakob@hawo-net.de>',                node                            author changestr
#[Out]# n                                                              
#[Out]# 15205  4e5b7d130e76  jakob krainz <jakob@hawo-net.de>  1: +8/-2), ('jdc@uwo.ca',               node      author changestr
#[Out]# n                                       
#[Out]# 1179  8acf62f579d8  jdc@uwo.ca  1: +3/-3
#[Out]# 1178  a7abffa4b19f  jdc@uwo.ca  1: +4/-4
#[Out]# 718   7dae73778114  jdc@uwo.ca  1: +4/-4), ('jfh <jason@jasonfharris.com>',                node                        author   changestr
#[Out]# n                                                            
#[Out]# 14196  78bdfc756908  jfh <jason@jasonfharris.com>    1: +3/-1
#[Out]# 13838  5c0e1222e7c0  jfh <jason@jasonfharris.com>    1: +4/-4
#[Out]# 13406  5e57c199848d  jfh <jason@jasonfharris.com>    1: +4/-1
#[Out]# 13396  3e66eec9a814  jfh <jason@jasonfharris.com>   4: +19/-8
#[Out]# 13298  5ccdca7df211  jfh <jason@jasonfharris.com>  9: +30/-26), ('john.levon@sun.com',               node              author  changestr
#[Out]# n                                                
#[Out]# 3082  240ec0e61290  john.levon@sun.com   1: +1/-1
#[Out]# 2267  d812d91c5a84  john.levon@sun.com  2: +14/-4), ('jon.christopher@Rigaku.com',               node                      author  changestr
#[Out]# n                                                        
#[Out]# 5014  97dbf330069a  jon.christopher@Rigaku.com  1: +16/-3), ('jorendorff@mozilla.com',               node                  author changestr
#[Out]# n                                                   
#[Out]# 6047  dd714452c26e  jorendorff@mozilla.com  1: +3/-2
#[Out]# 6046  1d0bfa4c75c0  jorendorff@mozilla.com  3: +5/-1), ('julian@lava.net',               node           author  changestr
#[Out]# n                                             
#[Out]# 4911  2f2d8c5e7a5c  julian@lava.net  1: +11/-0), ('kreijack@inwind.REMOVEME.it',              node                       author    changestr
#[Out]# n                                                          
#[Out]# 847  f1555f48f884  kreijack@inwind.REMOVEME.it  2: +108/-53
#[Out]# 846  a30f7ee30914  kreijack@inwind.REMOVEME.it     1: +6/-5
#[Out]# 845  52576cf969f2  kreijack@inwind.REMOVEME.it     1: +3/-3
#[Out]# 844  5a717cfa7406  kreijack@inwind.REMOVEME.it     1: +7/-1
#[Out]# 843  859e7ea530bd  kreijack@inwind.REMOVEME.it    1: +14/-0
#[Out]# 661  148f642d1f8e  kreijack@inwind.REMOVEME.it     2: +7/-2
#[Out]# 645  a55048b2ae3a  kreijack@inwind.REMOVEME.it     2: +3/-3), ('kyle@zeus.moffetthome.net',              node                     author changestr
#[Out]# n                                                     
#[Out]# 463  ea93402b81b9  kyle@zeus.moffetthome.net  2: +2/-0), ('lcantey@gmail.com',               node             author  changestr
#[Out]# n                                               
#[Out]# 1690  58894621c87a  lcantey@gmail.com  3: +25/-4), ('levon@movementarian.org',               node                   author  changestr
#[Out]# n                                                     
#[Out]# 1434  696851b1bba9  levon@movementarian.org  1: +33/-8
#[Out]# 1423  76239f0cb0dc  levon@movementarian.org   1: +2/-2), ('lupus@debian.org',               node            author  changestr
#[Out]# n                                              
#[Out]# 1522  d07d729ce306  lupus@debian.org  2: +13/-3), ('madhu@madhu',               node       author  changestr
#[Out]# n                                         
#[Out]# 7879  7bcce39e8f07  madhu@madhu  3: +21/-9), ('maf46@burn.cl.cam.ac.uk',              node                   author   changestr
#[Out]# n                                                     
#[Out]# 616  d45d1c90032e  maf46@burn.cl.cam.ac.uk  4: +110/-8), ('mark.williamson@cl.cam.ac.uk',               node                        author changestr
#[Out]# n                                                         
#[Out]# 5879  c5c9a022bd9a  mark.williamson@cl.cam.ac.uk  1: +1/-1
#[Out]# 912   302f83b85054  mark.williamson@cl.cam.ac.uk  1: +1/-1
#[Out]# 899   aa5b726e9619  mark.williamson@cl.cam.ac.uk  1: +4/-1
#[Out]# 667   31a9aa890016  mark.williamson@cl.cam.ac.uk  5: +6/-7), ('mason@suse.com',               node          author      changestr
#[Out]# n                                                
#[Out]# 2255  3f38e872f39a  mason@suse.com     1: +39/-17
#[Out]# 2222  c9e264b115e6  mason@suse.com      3: +14/-5
#[Out]# 2082  856f0ba200bc  mason@suse.com      3: +10/-9
#[Out]# 2080  1cbb14c048cb  mason@suse.com      1: +13/-8
#[Out]# 2079  ee96ca273f32  mason@suse.com    1: +145/-40
#[Out]# 2078  441ea218414e  mason@suse.com      3: +74/-4
#[Out]# 2077  4d0700ae0991  mason@suse.com       1: +2/-0
#[Out]# 2076  d007df6daf8e  mason@suse.com      2: +25/-8
#[Out]# 2075  343aeefb553b  mason@suse.com      3: +35/-8
#[Out]# 2074  01ee43dda681  mason@suse.com       1: +6/-4
#[Out]# 2073  1e6745f78989  mason@suse.com    2: +139/-28
#[Out]# 2072  74d3f5336b66  mason@suse.com   8: +201/-103
#[Out]# 1808  7036cd7f770d  mason@suse.com    1: +1286/-0
#[Out]# 1807  f1f43ea22cbf  mason@suse.com       1: +3/-2
#[Out]# 1806  a2c69737e65e  mason@suse.com      2: +33/-7
#[Out]# 1712  21dcf38e5d7d  mason@suse.com     2: +38/-25
#[Out]# 1711  8959700c2b19  mason@suse.com       1: +1/-0
#[Out]# 1644  e7e6504c4989  mason@suse.com     1: +1/-121
#[Out]# 1637  3b1b44b917f4  mason@suse.com    6: +171/-14
#[Out]# 1535  7ae0ce7a3dc4  mason@suse.com      1: +39/-0
#[Out]# 1534  80a3d6a0af71  mason@suse.com     1: +91/-76
#[Out]# 1533  3d11f81c9145  mason@suse.com     1: +17/-11
#[Out]# 1240  cc756ffd4d04  mason@suse.com  1: +2779/-576
#[Out]# 1239  29f17e083e84  mason@suse.com    1: +176/-96
#[Out]# 1238  6a4f181497c9  mason@suse.com       1: +5/-1
#[Out]# 1237  227cfbe34109  mason@suse.com       1: +1/-3
#[Out]# 1183  d9e85a75dbda  mason@suse.com    1: +128/-70
#[Out]# 1074  55bf5cfde69e  mason@suse.com      1: +22/-0
#[Out]# 1071  8f0ac653f85e  mason@suse.com      2: +31/-5
#[Out]# 904   969647d5100a  mason@suse.com       1: +5/-2
#[Out]# 903   71be6dd282d1  mason@suse.com       1: +3/-0
#[Out]# 902   c749ca37aed1  mason@suse.com       1: +9/-1
#[Out]# 901   120cba94d5aa  mason@suse.com       1: +5/-5
#[Out]# 900   ba8cf1f2210c  mason@suse.com       1: +2/-2
#[Out]# 898   3616c0d7ab88  mason@suse.com     2: +140/-7
#[Out]# 880   409a9a7b0da2  mason@suse.com       1: +4/-5
#[Out]# 879   953ccddd57bd  mason@suse.com     2: +53/-11
#[Out]# 873   4480e035d838  mason@suse.com       1: +4/-5
#[Out]# 872   9a0af739cf55  mason@suse.com     2: +53/-11
#[Out]# 720   095dd8c757e0  mason@suse.com       1: +7/-7
#[Out]# 719   dda258572847  mason@suse.com       1: +5/-8
#[Out]# 644   6ebe118280bd  mason@suse.com    2: +113/-12), ('mcmillen@cs.cmu.edu',               node               author   changestr
#[Out]# n                                                  
#[Out]# 2005  bc47af2d3693  mcmillen@cs.cmu.edu   1: +13/-9
#[Out]# 2004  7dd6317ab4fd  mcmillen@cs.cmu.edu    1: +5/-2
#[Out]# 2003  62647394e368  mcmillen@cs.cmu.edu  3: +49/-22
#[Out]# 1995  2da2d46862fb  mcmillen@cs.cmu.edu    4: +5/-5), ('michael.w.dales@intel.com',               node                     author changestr
#[Out]# n                                                      
#[Out]# 1427  0980d77f5e9a  michael.w.dales@intel.com  1: +1/-1), ('mpm@selenic.com', <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 768 entries, 1348 to 0
#[Out]# Data columns:
#[Out]# node         768  non-null values
#[Out]# author       768  non-null values
#[Out]# changestr    768  non-null values
#[Out]# dtypes: object(3)), ('mwilli2@localhost.localdomain',              node                         author changestr
#[Out]# n                                                         
#[Out]# 669  8aa2a282eda4  mwilli2@localhost.localdomain  1: +8/-1), ('olivier.maquelin@intel.com',               node                      author  changestr
#[Out]# n                                                        
#[Out]# 1420  b32b3509c7ab  olivier.maquelin@intel.com  2: +11/-0), ('oxymoron@cinder.waste.org',             node                     author changestr
#[Out]# n                                                    
#[Out]# 11  7f16aaeed62f  oxymoron@cinder.waste.org  1: +9/-4
#[Out]# 10  e76ed1e480ef  oxymoron@cinder.waste.org  1: +5/-4), ('paul sorenson <sf@metrak.com>',               node                         author changestr
#[Out]# n                                                          
#[Out]# 4692  c135c6cddbec  paul sorenson <sf@metrak.com>  1: +2/-1), ('peter.arrenbrecht@gmail.com',               node                       author   changestr
#[Out]# n                                                          
#[Out]# 5721  dd3ce7515f4d  peter.arrenbrecht@gmail.com  3: +333/-4), ('py4fun',                node  author changestr
#[Out]# n                                    
#[Out]# 15048  8d928799dab5  py4fun  1: +1/-3), ('roberto@keltia.freenix.fr',               node                     author changestr
#[Out]# n                                                      
#[Out]# 1119  7fca9752d945  roberto@keltia.freenix.fr  1: +5/-4), ('root@coffee.suse.com',               node                author changestr
#[Out]# n                                                 
#[Out]# 1243  9d10f89b75a5  root@coffee.suse.com  1: +2/-2), ('rubik <ribik@sina.com>',               node                  author  changestr
#[Out]# n                                                    
#[Out]# 6919  105d8676a688  rubik <ribik@sina.com>  2: +19/-0), ('rupert.thurner@gmail.com',               node                    author changestr
#[Out]# n                                                     
#[Out]# 5260  ce4e67533723  rupert.thurner@gmail.com  1: +4/-2), ('shaleh@speakeasy.net',              node                author changestr
#[Out]# n                                                
#[Out]# 611  48c3eb2bf844  shaleh@speakeasy.net  1: +8/-4
#[Out]# 610  4c02464cb9f0  shaleh@speakeasy.net  1: +3/-0), ('tailgunner@smtp.ru',               node              author changestr
#[Out]# n                                               
#[Out]# 3951  544838cc1158  tailgunner@smtp.ru  1: +6/-1), ('teki321@gmail.com',               node             author changestr
#[Out]# n                                              
#[Out]# 6462  d9266e48cd27  teki321@gmail.com  1: +1/-1), ('thananck@yahoo.com',              node              author   changestr
#[Out]# n                                                
#[Out]# 782  cdb9e95b2fab  thananck@yahoo.com  1: +16/-13
#[Out]# 632  8b8f710bb658  thananck@yahoo.com  1: +50/-28
#[Out]# 617  285965ddca41  thananck@yahoo.com    1: +1/-1
#[Out]# 615  ad2999fad721  thananck@yahoo.com    1: +1/-1), ('thron7 <thron7@users.sourceforge.net>',                node                                 author  changestr
#[Out]# n                                                                    
#[Out]# 13576  a93312c8f7b7  thron7 <thron7@users.sourceforge.net>  1: +15/-3
#[Out]# 13575  8496b36403c1  thron7 <thron7@users.sourceforge.net>   1: +9/-5
#[Out]# 13574  2b8c5fc7dc1d  thron7 <thron7@users.sourceforge.net>  1: +24/-0
#[Out]# 13573  e415680ee1c5  thron7 <thron7@users.sourceforge.net>   1: +6/-0
#[Out]# 13572  5472d888d80d  thron7 <thron7@users.sourceforge.net>  1: +20/-2
#[Out]# 13571  a7ba079bbaa0  thron7 <thron7@users.sourceforge.net>  1: +19/-2
#[Out]# 13570  7803827ca94e  thron7 <thron7@users.sourceforge.net>  1: +11/-0
#[Out]# 13569  37987e22bf03  thron7 <thron7@users.sourceforge.net>   1: +8/-2
#[Out]# 13568  07129cc45abc  thron7 <thron7@users.sourceforge.net>  1: +28/-1
#[Out]# 13567  871242b0283a  thron7 <thron7@users.sourceforge.net>   1: +9/-0
#[Out]# 13566  47f11b52021b  thron7 <thron7@users.sourceforge.net>  1: +14/-3), ('timeless',                node    author changestr
#[Out]# n                                      
#[Out]# 10058  af5f99d8195e  timeless  1: +2/-1), ('timeless <timeless@gmail.com>',                node                         author     changestr
#[Out]# n                                                               
#[Out]# 13772  8cbb59124e67  timeless <timeless@gmail.com>      1: +4/-1
#[Out]# 13771  c49cddce0a81  timeless <timeless@gmail.com>     2: +12/-6
#[Out]# 13524  66d65bccbf06  timeless <timeless@gmail.com>     2: +11/-1
#[Out]# 13523  c17e4d881722  timeless <timeless@gmail.com>      1: +1/-1
#[Out]# 13265  3f299f5d9a29  timeless <timeless@gmail.com>     2: +40/-2
#[Out]# 13191  c9ae7e096994  timeless <timeless@gmail.com>     1: +30/-3
#[Out]# 13119  3e2281b85990  timeless <timeless@gmail.com>      2: +2/-2
#[Out]# 13118  3fd4e4e81382  timeless <timeless@gmail.com>      2: +7/-6
#[Out]# 12926  27e4146d9241  timeless <timeless@gmail.com>      1: +1/-1
#[Out]# 12862  9d6adddc8eea  timeless <timeless@gmail.com>      1: +2/-2
#[Out]# 12861  1c57a66bf985  timeless <timeless@gmail.com>      1: +1/-1
#[Out]# 12851  765c98f068d3  timeless <timeless@gmail.com>      1: +2/-2
#[Out]# 12848  f7f1a146f407  timeless <timeless@gmail.com>      1: +1/-1
#[Out]# 12774  98aaf58a1d7c  timeless <timeless@gmail.com>      1: +1/-1
#[Out]# 12770  daa8dc6e1f66  timeless <timeless@gmail.com>      1: +1/-1
#[Out]# 12769  c6b55be14461  timeless <timeless@gmail.com>      1: +2/-2
#[Out]# 12750  338b4b615d33  timeless <timeless@gmail.com>    1: +29/-32
#[Out]# 12747  8b438cb84c57  timeless <timeless@gmail.com>      1: +3/-2
#[Out]# 12746  5a1912b5aa42  timeless <timeless@gmail.com>      1: +4/-4
#[Out]# 12745  0793d763e413  timeless <timeless@gmail.com>      3: +6/-6
#[Out]# 11900  c91b86a291b0  timeless <timeless@gmail.com>      1: +7/-2
#[Out]# 11899  226a328a7ff3  timeless <timeless@gmail.com>      3: +9/-9
#[Out]# 11571  87dcf758309d  timeless <timeless@gmail.com>    2: +13/-13
#[Out]# 11563  db426935fa94  timeless <timeless@gmail.com>   14: +91/-91
#[Out]# 11408  534c69494918  timeless <timeless@gmail.com>     1: +13/-0
#[Out]# 11355  9011036ba79d  timeless <timeless@gmail.com>     2: +22/-1
#[Out]# 11354  412a6e749f8d  timeless <timeless@gmail.com>      2: +7/-0
#[Out]# 10602  7ce62865d72a  timeless <timeless@gmail.com>   3: +169/-16
#[Out]# 9646   5b001f534452  timeless <timeless@gmail.com>     2: +10/-5
#[Out]# 8780   708938509732  timeless <timeless@gmail.com>  6: +124/-118
#[Out]# 8764   fccdf5ca5065  timeless <timeless@gmail.com>      2: +5/-5
#[Out]# 8763   545dfd502e69  timeless <timeless@gmail.com>      1: +2/-2
#[Out]# 8762   0289f384e1e5  timeless <timeless@gmail.com>   12: +20/-20
#[Out]# 8761   bf17aeafb869  timeless <timeless@gmail.com>      6: +8/-8
#[Out]# 8729   1b713f72c91a  timeless <timeless@gmail.com>    1: +14/-15
#[Out]# 7807   bd8f44638847  timeless <timeless@gmail.com>    5: +20/-20
#[Out]# 7804   06afe0f9dbf8  timeless <timeless@gmail.com>    1: +43/-38
#[Out]# 7765   14a42208d8af  timeless <timeless@gmail.com>      1: +3/-3), ('timeless <timeless@mozdev.org>',                node                          author   changestr
#[Out]# n                                                              
#[Out]# 14206  fc004d16633f  timeless <timeless@mozdev.org>    1: +1/-1
#[Out]# 14205  dea68bddfb87  timeless <timeless@mozdev.org>    2: +5/-0
#[Out]# 14204  b452abffcb15  timeless <timeless@mozdev.org>    1: +5/-1
#[Out]# 14203  bab267e7fc1a  timeless <timeless@mozdev.org>    2: +2/-2
#[Out]# 14202  419539ea79cb  timeless <timeless@mozdev.org>   2: +17/-2
#[Out]# 14177  82f0412ef7de  timeless <timeless@mozdev.org>   3: +29/-0
#[Out]# 14176  4e5a36eeefd1  timeless <timeless@mozdev.org>    4: +3/-4
#[Out]# 14174  83a94c2fe6f4  timeless <timeless@mozdev.org>   1: +20/-0
#[Out]# 14173  eebf196a8bbe  timeless <timeless@mozdev.org>    1: +0/-1
#[Out]# 14172  673abd432104  timeless <timeless@mozdev.org>   1: +18/-3
#[Out]# 13991  f4e4faa92939  timeless <timeless@mozdev.org>  2: +36/-22
#[Out]# 13990  6e6d19738df9  timeless <timeless@mozdev.org>   1: +55/-0
#[Out]# 10524  9c0ba837dc65  timeless <timeless@mozdev.org>    2: +4/-4
#[Out]# 10517  75361931884d  timeless <timeless@mozdev.org>    2: +8/-2
#[Out]# 10450  b4fd900569b1  timeless <timeless@mozdev.org>    1: +2/-2
#[Out]# 10378  a2950e053614  timeless <timeless@mozdev.org>  3: +13/-13
#[Out]# 9932   3e7663b2f3fc  timeless <timeless@mozdev.org>   3: +30/-0), ('timeless@gmail.com',                node              author changestr
#[Out]# n                                                
#[Out]# 13874  6337149fc07c  timeless@gmail.com  1: +3/-0
#[Out]# 13591  794f4476b974  timeless@gmail.com  1: +2/-2), ('timeless@mozdev.org',                node               author   changestr
#[Out]# n                                                   
#[Out]# 10377  adf9505e8888  timeless@mozdev.org  3: +17/-17
#[Out]# 9896   5b149c88d9e8  timeless@mozdev.org    1: +7/-7
#[Out]# 9747   85a3285860d3  timeless@mozdev.org    1: +5/-3
#[Out]# 9649   20b91f91f9ca  timeless@mozdev.org    2: +3/-2
#[Out]# 9645   02f40b2ece3f  timeless@mozdev.org    1: +2/-0
#[Out]# 9644   c6b721da201b  timeless@mozdev.org    1: +2/-2
#[Out]# 9506   cec9fb4e07a1  timeless@mozdev.org  3: +65/-65
#[Out]# 9383   9219037fc0a6  timeless@mozdev.org    2: +2/-2
#[Out]# 9163   fdf0c375cdbf  timeless@mozdev.org  2: +15/-15), ('tksoh@users.sf.net',              node              author changestr
#[Out]# n                                              
#[Out]# 933  9c43d68ad59f  tksoh@users.sf.net  1: +1/-1), ('tksoh@users.sourceforge.net',              node                       author   changestr
#[Out]# n                                                         
#[Out]# 867  0cd2ee61b10a  tksoh@users.sourceforge.net    1: +5/-0
#[Out]# 840  141744605b51  tksoh@users.sourceforge.net  2: +24/-12), ('tonfa@arakou.lan',               node            author changestr
#[Out]# n                                             
#[Out]# 1440  bf109779f48b  tonfa@arakou.lan  2: +9/-6), ('trbs <trbs@trbs.net>',                node                author  changestr
#[Out]# n                                                   
#[Out]# 13045  22167be007ed  trbs <trbs@trbs.net>  2: +13/-1), ('twaldmann@thinkmo.de',               node                author   changestr
#[Out]# n                                                   
#[Out]# 1542  8e80eefb3de6  twaldmann@thinkmo.de    1: +5/-4
#[Out]# 1541  bf4e7ef08741  twaldmann@thinkmo.de  9: +17/-17
#[Out]# 1540  8ca9f5b17257  twaldmann@thinkmo.de    2: +3/-3), ('various',                node   author     changestr
#[Out]# n                                         
#[Out]# 15174  cfccd3bee7b3  various  14: +3135/-0), ('wilde@trapperkeeper.sha-bang.de',               node                           author  changestr
#[Out]# n                                                             
#[Out]# 2233  3840cefa5222  wilde@trapperkeeper.sha-bang.de  2: +15/-3), ('wujek',                node author changestr
#[Out]# n                                   
#[Out]# 14850  dd74cd1e5d49  wujek  1: +4/-1), ('wujek srujek <wujek.srujek@googlemail.com>',                node                                      author changestr
#[Out]# n                                                                        
#[Out]# 16642  a7ba57b10530  wujek srujek <wujek.srujek@googlemail.com>  1: +2/-1), ('zbynek@alex.kolej.mff.cuni.cz',               node                         author changestr
#[Out]# n                                                          
#[Out]# 1357  94586af53d2f  zbynek@alex.kolej.mff.cuni.cz  1: +4/-5)]
df['fileschanged'] = df['changestr'].split(':')[0]
df['fileschanged'] = df['changestr'].apply(lambda x: x.split(':')[0])
df['fileschanged']
#[Out]# n
#[Out]# 16663     0
#[Out]# 16662     2
#[Out]# 16661    20
#[Out]# 16660     2
#[Out]# 16659     1
#[Out]# 16658     1
#[Out]# 16657     1
#[Out]# 16656     1
#[Out]# 16655     1
#[Out]# 16654     1
#[Out]# 16653     2
#[Out]# 16652     2
#[Out]# 16651     1
#[Out]# 16650     2
#[Out]# 16649     1
#[Out]# ...
#[Out]# 14     1
#[Out]# 13     1
#[Out]# 12     1
#[Out]# 11     1
#[Out]# 10     1
#[Out]# 9      1
#[Out]# 8      1
#[Out]# 7      1
#[Out]# 6      1
#[Out]# 5      1
#[Out]# 4      1
#[Out]# 3      1
#[Out]# 2      1
#[Out]# 1      2
#[Out]# 0     12
#[Out]# Name: fileschanged, Length: 16664
#df['added'] = df['changestr'].apply(lambda x: x.split(':')[1].split()
get_ipython().magic(u'pinfo2 read_csv')
get_ipython().magic(u'pinfo read_csv')
df['added'] = df['changestr'].apply(lambda x: x.split(':')[1].split('/')[0].strip()[1:])
df['added']
#[Out]# n
#[Out]# 16663       0
#[Out]# 16662      71
#[Out]# 16661      67
#[Out]# 16660      12
#[Out]# 16659       7
#[Out]# 16658     294
#[Out]# 16657      96
#[Out]# 16656    1848
#[Out]# 16655      83
#[Out]# 16654       0
#[Out]# 16653      82
#[Out]# 16652      14
#[Out]# 16651       2
#[Out]# 16650      14
#[Out]# 16649       4
#[Out]# ...
#[Out]# 14       4
#[Out]# 13       2
#[Out]# 12       1
#[Out]# 11       9
#[Out]# 10       5
#[Out]# 9        2
#[Out]# 8        2
#[Out]# 7        5
#[Out]# 6        1
#[Out]# 5        3
#[Out]# 4        6
#[Out]# 3        3
#[Out]# 2        4
#[Out]# 1       11
#[Out]# 0     1937
#[Out]# Name: added, Length: 16664
df['removed'] = df['changestr'].apply(lambda x: x.split(':')[1].split('/')[1].strip()[1:])
df
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 16663 to 0
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df['added'].mean()
#[Out]# inf
df['added']
#[Out]# n
#[Out]# 16663       0
#[Out]# 16662      71
#[Out]# 16661      67
#[Out]# 16660      12
#[Out]# 16659       7
#[Out]# 16658     294
#[Out]# 16657      96
#[Out]# 16656    1848
#[Out]# 16655      83
#[Out]# 16654       0
#[Out]# 16653      82
#[Out]# 16652      14
#[Out]# 16651       2
#[Out]# 16650      14
#[Out]# 16649       4
#[Out]# ...
#[Out]# 14       4
#[Out]# 13       2
#[Out]# 12       1
#[Out]# 11       9
#[Out]# 10       5
#[Out]# 9        2
#[Out]# 8        2
#[Out]# 7        5
#[Out]# 6        1
#[Out]# 5        3
#[Out]# 4        6
#[Out]# 3        3
#[Out]# 2        4
#[Out]# 1       11
#[Out]# 0     1937
#[Out]# Name: added, Length: 16664
df['added'] = df['changestr'].apply(lambda x: int(x.split(':')[1].split('/')[0].strip()[1:]))
df['removed'] = df['changestr'].apply(lambda x: int(x.split(':')[1].split('/')[1].strip()[1:]))
df['added'].mean()
#[Out]# 126.73049687950072
col=df['added']
col.median()
#[Out]# 9.0
df
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 16663 to 0
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df['fileschanged'].mean()
#[Out]# inf
df['fileschanged'] = df['fileschanged'].apply(int)
df['fileschanged'].mean()
#[Out]# 2.8861617858857418
df['fileschanged'].max()
#[Out]# 1293
df['fileschanged'].argmax()
#[Out]# 3868
df[df['fileschanged'].argmax()]
df.ix[0]
#[Out]# node               9117c6561b0b
#[Out]# author          mpm@selenic.com
#[Out]# changestr          12: +1937/-0
#[Out]# fileschanged                 12
#[Out]# added                      1937
#[Out]# removed                       0
#[Out]# Name: 0
df.ix[1]
#[Out]# node               273ce12ad8f1
#[Out]# author          mpm@selenic.com
#[Out]# changestr             2: +11/-1
#[Out]# fileschanged                  2
#[Out]# added                        11
#[Out]# removed                       1
#[Out]# Name: 1
df.ix[df['fileschanged'].argmax()]
#[Out]# node                                           6033d9f28052
#[Out]# author          Thomas Arendsen Hein <thomas@intevation.de>
#[Out]# changestr                                        2: +26/-16
#[Out]# fileschanged                                              2
#[Out]# added                                                    26
#[Out]# removed                                                  16
#[Out]# Name: 3868
get_ipython().magic(u'pinfo col.argmax')
df.ix[df['fileschanged'].ma()]
df.ix[df['fileschanged'].max()]
#[Out]# node                                     a6ffcebd3315
#[Out]# author          Bryan O'Sullivan <bos@serpentine.com>
#[Out]# changestr                                   2: +81/-9
#[Out]# fileschanged                                        2
#[Out]# added                                              81
#[Out]# removed                                             9
#[Out]# Name: 1293
df['fileschanged'].max()
#[Out]# 1293
df['fileschanged'].argmax()
#[Out]# 3868
get_ipython().magic(u'pinfo df.xs')
df.xs(df['fileschanged'].argmax())
#[Out]# node                                           6033d9f28052
#[Out]# author          Thomas Arendsen Hein <thomas@intevation.de>
#[Out]# changestr                                        2: +26/-16
#[Out]# fileschanged                                              2
#[Out]# added                                                    26
#[Out]# removed                                                  16
#[Out]# Name: 3868
df[0]
df.index
#[Out]# Int64Index([16663, 16662, 16661, ...,     2,     1,     0], dtype=int64)
get_ipython().magic(u'pinfo df.sort')
df.sort()
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 0 to 16663
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df[0]
df[1]
df.ix[0]
#[Out]# node               9117c6561b0b
#[Out]# author          mpm@selenic.com
#[Out]# changestr          12: +1937/-0
#[Out]# fileschanged                 12
#[Out]# added                      1937
#[Out]# removed                       0
#[Out]# Name: 0
df.ix[1]
#[Out]# node               273ce12ad8f1
#[Out]# author          mpm@selenic.com
#[Out]# changestr             2: +11/-1
#[Out]# fileschanged                  2
#[Out]# added                        11
#[Out]# removed                       1
#[Out]# Name: 1
df.ix[-1]
df
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 16663 to 0
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df.ix[16664]
df.ix
#[Out]# <pandas.core.indexing._NDFrameIndexer object at 0x9cc942c>
df.ix.ndim
#[Out]# 2
df.ix.obj
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 16663 to 0
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df.indesx
df.index
#[Out]# Int64Index([16663, 16662, 16661, ...,     2,     1,     0], dtype=int64)
get_ipython().magic(u'pinfo df.reindex')
df.reindex(index=df.index[::-1])
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 0 to 16663
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 16663 to 0
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df[0]
df.ix[0]
#[Out]# node               9117c6561b0b
#[Out]# author          mpm@selenic.com
#[Out]# changestr          12: +1937/-0
#[Out]# fileschanged                 12
#[Out]# added                      1937
#[Out]# removed                       0
#[Out]# Name: 0
df
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 16663 to 0
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df['0']
df.ix['0']
df
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 16663 to 0
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
get_ipython().magic(u'pinfo df')
import numpy as np
df3 = DataFrame(np.random.randn(10, 5),
                 columns=['a', 'b', 'c', 'd', 'e'])
df3
#[Out]#           a         b         c         d         e
#[Out]# 0  0.144199 -1.033453 -1.515417  0.365670  1.278047
#[Out]# 1 -0.164493  1.552385  1.763152 -1.317428 -1.240592
#[Out]# 2 -0.915401  0.538293  0.186137 -0.310534  1.466384
#[Out]# 3 -0.245401 -2.272524 -0.091289 -0.147050 -0.013532
#[Out]# 4 -0.830598 -1.372792 -1.759492  0.057304 -0.561801
#[Out]# 5 -1.457285  0.323503 -0.654238 -0.917850 -0.278945
#[Out]# 6  1.839205  0.648414 -1.993186 -1.198790 -0.610247
#[Out]# 7 -1.282671 -0.811091 -0.059240  1.425815 -1.834416
#[Out]# 8  0.607595  0.540417 -1.421721  0.519813 -1.053572
#[Out]# 9 -0.458529 -1.867968  0.085734  1.654514 -0.975314
df3[0]
df3
#[Out]#           a         b         c         d         e
#[Out]# 0  0.144199 -1.033453 -1.515417  0.365670  1.278047
#[Out]# 1 -0.164493  1.552385  1.763152 -1.317428 -1.240592
#[Out]# 2 -0.915401  0.538293  0.186137 -0.310534  1.466384
#[Out]# 3 -0.245401 -2.272524 -0.091289 -0.147050 -0.013532
#[Out]# 4 -0.830598 -1.372792 -1.759492  0.057304 -0.561801
#[Out]# 5 -1.457285  0.323503 -0.654238 -0.917850 -0.278945
#[Out]# 6  1.839205  0.648414 -1.993186 -1.198790 -0.610247
#[Out]# 7 -1.282671 -0.811091 -0.059240  1.425815 -1.834416
#[Out]# 8  0.607595  0.540417 -1.421721  0.519813 -1.053572
#[Out]# 9 -0.458529 -1.867968  0.085734  1.654514 -0.975314
df3.ix[0]
#[Out]# a    0.144199
#[Out]# b   -1.033453
#[Out]# c   -1.515417
#[Out]# d    0.365670
#[Out]# e    1.278047
#[Out]# Name: 0
df3['a'].argmax()
#[Out]# 6
df3.ix[df3['a'].argmax()]
#[Out]# a    1.839205
#[Out]# b    0.648414
#[Out]# c   -1.993186
#[Out]# d   -1.198790
#[Out]# e   -0.610247
#[Out]# Name: 6
df.ix(df['fileschanged'].argmax())
df.ix[df['fileschanged'].argmax()]
#[Out]# node                                           6033d9f28052
#[Out]# author          Thomas Arendsen Hein <thomas@intevation.de>
#[Out]# changestr                                        2: +26/-16
#[Out]# fileschanged                                              2
#[Out]# added                                                    26
#[Out]# removed                                                  16
#[Out]# Name: 3868
df.ix[df['fileschanged'].argmax()]['fileschanged']
#[Out]# 2
df.ix[df['fileschanged'].argmax()]['fileschanged'] == df['fileschanged'].max()
#[Out]# False
df.ix[df['fileschanged'].argmax()+1]['fileschanged'] == df['fileschanged'].max()
#[Out]# False
df.ix[df['fileschanged'].argmax()-1]['fileschanged'] == df['fileschanged'].max()
#[Out]# False
df['fileschanged'].max()
#[Out]# 1293
get_ipython().system(u'less ./log.txt')
df
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 16663 to 0
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df.ix[16664-df['fileschanged'].argmax()]['fileschanged'] == df['fileschanged'].max()
#[Out]# False
df.ix[16664-df['fileschanged'].argmax()]['fileschanged']
#[Out]# 1
df.ix[16663-df['fileschanged'].argmax()]['fileschanged']
#[Out]# 1293
df.ix[16663-df['fileschanged'].argmax()]['fileschanged'] == df['fileschanged'].max()
#[Out]# True
get_ipython().magic(u'pinfo df.ix')
get_ipython().magic(u'pinfo df.xs')
df.xs[df['fileschanged'].argmax()]['fileschanged'] == df['fileschanged'].max()
df.xs(df['fileschanged'].argmax())
#[Out]# node                                           6033d9f28052
#[Out]# author          Thomas Arendsen Hein <thomas@intevation.de>
#[Out]# changestr                                        2: +26/-16
#[Out]# fileschanged                                              2
#[Out]# added                                                    26
#[Out]# removed                                                  16
#[Out]# Name: 3868
df.ix[16663-df['fileschanged'].argmax()]
#[Out]# node                              3cb0559e44d0
#[Out]# author          Matt Mackall <mpm@selenic.com>
#[Out]# changestr                  1293: +94880/-81039
#[Out]# fileschanged                              1293
#[Out]# added                                    94880
#[Out]# removed                                  81039
#[Out]# Name: 12795
df.index[0]
#[Out]# 16663
df.index[1]
#[Out]# 16662
df.index[::-1]
#[Out]# Int64Index([    0,     1,     2, ..., 16661, 16662, 16663], dtype=int64)
df.index
#[Out]# Int64Index([16663, 16662, 16661, ...,     2,     1,     0], dtype=int64)
get_ipython().magic(u'pinfo df.reindex')
df.reindex(index=df.index[::-1])
#[Out]# <class 'pandas.core.frame.DataFrame'>
#[Out]# Int64Index: 16664 entries, 0 to 16663
#[Out]# Data columns:
#[Out]# node            16664  non-null values
#[Out]# author          16664  non-null values
#[Out]# changestr       16664  non-null values
#[Out]# fileschanged    16664  non-null values
#[Out]# added           16664  non-null values
#[Out]# removed         16664  non-null values
#[Out]# dtypes: int64(3), object(3)
df = df.reindex(index=df.index[::-1])
df.xs[df['fileschanged'].argmax()]['fileschanged'] == df['fileschanged'].max()
df.ix[df['fileschanged'].argmax()]['fileschanged'] == df['fileschanged'].max()
#[Out]# True
df.ix[df['fileschanged'].argmax()]
#[Out]# node                              3cb0559e44d0
#[Out]# author          Matt Mackall <mpm@selenic.com>
#[Out]# changestr                  1293: +94880/-81039
#[Out]# fileschanged                              1293
#[Out]# added                                    94880
#[Out]# removed                                  81039
#[Out]# Name: 12795
df.ix[df['added'].argmax()]
#[Out]# node                              3cb0559e44d0
#[Out]# author          Matt Mackall <mpm@selenic.com>
#[Out]# changestr                  1293: +94880/-81039
#[Out]# fileschanged                              1293
#[Out]# added                                    94880
#[Out]# removed                                  81039
#[Out]# Name: 12795
df.ix[df['removed'].argmax()]
#[Out]# node                              3cb0559e44d0
#[Out]# author          Matt Mackall <mpm@selenic.com>
#[Out]# changestr                  1293: +94880/-81039
#[Out]# fileschanged                              1293
#[Out]# added                                    94880
#[Out]# removed                                  81039
#[Out]# Name: 12795
get_ipython().magic(u'logstart hglog.py')
