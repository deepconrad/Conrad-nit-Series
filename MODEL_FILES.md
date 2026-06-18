# Model file checklist

This repository currently publishes the model card for `conrad-nit-8b`.

To make the repository loadable in common Transformers tooling, add the following files when they are available:

- `config.json`
- tokenizer files such as `tokenizer.json`, `tokenizer_config.json`, and `special_tokens_map.json`
- `generation_config.json` if needed
- weights such as `model.safetensors` or sharded safetensors files

If the model is being published as an adapter or LoRA-only repo, include the adapter files and the base model reference in the model card.
