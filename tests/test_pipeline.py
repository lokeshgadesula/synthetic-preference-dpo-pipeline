from preference_dpo.generator import make_pair
from preference_dpo.validators import schema_score,total_score
from preference_dpo.evaluate import adherence
def test_pair_order():p=make_pair(0);assert p["chosen_score"]>p["rejected_score"]
def test_schema():assert schema_score(make_pair(1)["chosen"])==1
def test_adherence():assert adherence([make_pair(0)["chosen"],make_pair(1)["chosen"]])==1
def test_bad_lower():p=make_pair(2);assert total_score(p["chosen"])>total_score(p["rejected"])
