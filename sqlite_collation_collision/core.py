import sqlite3
from .common import identifier
def run(data):
 keys=data['keys']
 if not isinstance(keys,list)or len(keys)>1000 or any(v is not None and(not isinstance(v,str)or len(v)>1000)for v in keys):raise ValueError('keys')
 out={}
 with sqlite3.connect(':memory:')as db:
  for coll in ['BINARY','NOCASE','RTRIM']:
   db.execute('create table t_'+coll+'(v text collate '+coll+' unique)');accepted=[];rejected=[]
   for i,key in enumerate(keys):
    try:db.execute('insert into t_'+coll+' values(?)',(key,));accepted.append(i)
    except sqlite3.IntegrityError:rejected.append(i)
   out[coll]={'accepted_indices':accepted,'rejected_indices':rejected}
 return {'collations':out,'nocase_scope':'SQLite built-in ASCII case folding; not Unicode normalization'}
