# Automated Synthetic Dataset Engine & DPO Alignment Pipeline

Runnable portfolio project for generating schema/design instruction examples, scoring candidates with deterministic validators, constructing **chosen/rejected preference pairs**, and training a causal LM with **Hugging Face TRL DPO**.

## Included
- synthetic instruction/task generator
- JSON schema validator
- deterministic design/aesthetic heuristics
- preference-pair builder
- JSONL export
- train/validation split
- TRL `DPOTrainer` training entry point
- post-training structural-adherence evaluation
- tests, Docker, CI

## Dataset generation
```bash
python -m preference_dpo.generate --count 100 --out data/preferences.jsonl
```

## Local tests
```bash
pip install -e ".[dev]"
pytest -q
```

## DPO training
```bash
pip install -e ".[train]"
python -m preference_dpo.train \
  --model <your-small-causal-lm> \
  --dataset data/preferences.jsonl \
  --output artifacts/dpo-model
```
