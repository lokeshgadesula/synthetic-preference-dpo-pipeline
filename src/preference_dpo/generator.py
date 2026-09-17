import json,random
from .validators import total_score
TASKS=["analytics dashboard","billing settings panel","project status card","support queue"]
def instruction(task):return f'Create JSON for a {task}. Required keys: component, title, items. Each item needs a label.'
def good(task,i):
 return json.dumps({"component":"panel","title":task.title(),"items":[{"label":f"Item {i+1}"},{"label":"Details"}]})
def bad(task,i):
 variants=[json.dumps({"title":task,"rows":["x"]}),"{bad json",json.dumps({"component":7,"title":"","items":"wrong"})]
 return variants[i%len(variants)]
def make_pair(i):
 task=TASKS[i%len(TASKS)];a,b=good(task,i),bad(task,i)
 return {"prompt":instruction(task),"chosen":a if total_score(a)>=total_score(b) else b,
         "rejected":b if total_score(a)>=total_score(b) else a,
         "chosen_score":max(total_score(a),total_score(b)),"rejected_score":min(total_score(a),total_score(b))}
