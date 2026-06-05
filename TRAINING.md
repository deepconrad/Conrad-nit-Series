# Training Conrad NIT 120B

This repository is set up for a Llama-based fine-tune path.

## Base model

`meta-llama/Meta-Llama-3.1-8B-Instruct`

## Dataset format

Use JSONL with a `messages` array:

```json
{"messages":[{"role":"system","content":"You are Conrad."},{"role":"user","content":"What is Deep Conrad?"},{"role":"assistant","content":"Deep Conrad is the company behind Conrad."}]}
```

## Train

Install training dependencies:

```bash
pip install -r requirements-train.txt
```

Run LoRA fine-tuning:

```bash
python train_lora.py --train_file data/sample_sft.jsonl --output_dir outputs/conrad-nit-120b-lora
```

## Output

The script saves LoRA adapter files and tokenizer files into the output directory.

If you merge adapters into the base model later, publish the merged checkpoint separately and update the model card accordingly.
