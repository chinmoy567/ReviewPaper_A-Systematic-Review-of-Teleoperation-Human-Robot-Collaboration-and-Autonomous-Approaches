import pandas as pd,re,csv,collections
import os
os.chdir(r"C:\Users\chinmoy\Downloads\review paper")
x=pd.read_excel('assets/docs/paperlinks.xlsx')
x['route']=x['How it was found'].str.lower().map(lambda s:'pub' if any(k in s for k in['mdpi','elsevier','scientific reports','plos','ieee','frontiers','wiley']) else ('gs' if 'scholer' in s else 'ai'))
x['pre']=x.DOI.map(lambda d:re.search(r'doi.org/(10\.\d+)',str(d)).group(1))
x['doi']=x.DOI.str.lower().str.replace(r'^https?://(dx\.)?doi\.org/','',regex=True).str.strip()
print(x.route.value_counts().to_dict())
pubname={'10.3390':'MDPI','10.1016':'Elsevier','10.1109':'IEEE','10.1007':'Springer','10.1038':'SciRep','10.1371':'PLOS','10.3389':'Frontiers','10.32604':'TSP','10.31763':'ASCEE','10.1002':'Wiley'}
x['pub']=x.pre.map(pubname)
print(pd.crosstab(x.pub,x.route,margins=True))
# platform-search by search site vs DOI prefix (TSP via ScienceDirect)
d=x[x.doi.duplicated(keep=False)].sort_values('doi'); print(d[['No','doi','route']].to_string())
log=list(csv.DictReader(open('supplementary/screening_log.csv',encoding='utf-8')))
ids=set(int(r['record_id']) for r in log); allno=set(x.No)
rem=sorted(allno-ids); print('not in log',rem, 'in log not in xlsx',ids-allno)
print(x[x.No.isin(rem)][['No','route','doi']])
# route of screened
x['inlog']=x.No.isin(ids)
print('screened by route',x[x.inlog].route.value_counts().to_dict())
inc={int(r['record_id']) for r in log if r['decision']=='INCLUDED'}
x['inc']=x.No.isin(inc)
print('included by route',x[x.inc].route.value_counts().to_dict(), x.inc.sum())
# exclusions
ex=[r for r in log if r['decision']=='EXCLUDED']
c=collections.Counter()
for r in ex:
    for k in r['criteria_violated'].split('/'): c[k]+=1
print(len(ex),c,collections.Counter(r['criteria_violated'] for r in ex))
print('multi',sum('/' in r['criteria_violated'] for r in ex), 'sum',sum(c.values()))
# removed dup not in 125; also check whether pubs with route for Table II
