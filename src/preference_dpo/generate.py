import argparse,json
from pathlib import Path
from .generator import make_pair
def main():
 p=argparse.ArgumentParser();p.add_argument("--count",type=int,default=100);p.add_argument("--out",default="data/preferences.jsonl");a=p.parse_args()
 out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text("\n".join(json.dumps(make_pair(i)) for i in range(a.count))+"\n")
 print(f"wrote {a.count} preference pairs to {out}")
if __name__=="__main__":main()
