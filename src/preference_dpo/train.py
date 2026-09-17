import argparse
def main():
 p=argparse.ArgumentParser();p.add_argument("--model",required=True);p.add_argument("--dataset",required=True);p.add_argument("--output",default="artifacts/dpo-model");a=p.parse_args()
 try:
  from datasets import load_dataset
  from transformers import AutoModelForCausalLM,AutoTokenizer
  from trl import DPOConfig,DPOTrainer
 except ImportError as e:raise RuntimeError('Install: pip install -e ".[train]"') from e
 ds=load_dataset("json",data_files=a.dataset,split="train")
 split=ds.train_test_split(test_size=.1,seed=42)
 tok=AutoTokenizer.from_pretrained(a.model)
 if tok.pad_token is None:tok.pad_token=tok.eos_token
 model=AutoModelForCausalLM.from_pretrained(a.model)
 cfg=DPOConfig(output_dir=a.output,num_train_epochs=1,per_device_train_batch_size=1,
               gradient_accumulation_steps=4,learning_rate=5e-6,logging_steps=5,save_strategy="epoch")
 trainer=DPOTrainer(model=model,args=cfg,processing_class=tok,train_dataset=split["train"],eval_dataset=split["test"])
 trainer.train();trainer.save_model(a.output)
if __name__=="__main__":main()
