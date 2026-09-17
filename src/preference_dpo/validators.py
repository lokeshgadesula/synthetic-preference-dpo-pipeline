import json,re
REQUIRED={"component","title","items"}
def parse_candidate(text):
    try:return json.loads(text)
    except json.JSONDecodeError:return None
def schema_score(text):
    x=parse_candidate(text)
    if not isinstance(x,dict):return 0.0
    present=sum(k in x for k in REQUIRED)/len(REQUIRED)
    types=(isinstance(x.get("component"),str)+isinstance(x.get("title"),str)+isinstance(x.get("items"),list))/3
    return .6*present+.4*types
def aesthetic_score(text):
    x=parse_candidate(text)
    if not isinstance(x,dict):return 0.0
    title=x.get("title","")
    items=x.get("items",[])
    concise=1.0 if 1<=len(title)<=60 else .3
    bounded=1.0 if 1<=len(items)<=8 else .4
    labels=1.0 if all(isinstance(i,dict) and isinstance(i.get("label"),str) for i in items) else .2
    return (concise+bounded+labels)/3
def total_score(text):return .7*schema_score(text)+.3*aesthetic_score(text)
