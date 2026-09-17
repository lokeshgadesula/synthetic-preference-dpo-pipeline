from .validators import schema_score
def adherence(outputs):
 if not outputs:return 0.0
 return sum(schema_score(x)==1.0 for x in outputs)/len(outputs)
def compare(before,after):
 return {"before_adherence":adherence(before),"after_adherence":adherence(after),
         "absolute_gain":adherence(after)-adherence(before)}
