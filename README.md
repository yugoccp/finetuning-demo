# LoRA Fine-tuning DEMO

This project aim to demonstrate how to fine-tune LLM for specific task and domain using LoRA technique.

## What is LoRA?
LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that inserts trainable rank-decomposition matrices into transformer layers, enabling model adaptation with minimal computational resources and memory overhead.

## Why should I consider fine-tuning a model?
Fine-tuning tailors a pre-trained model to your specific task or dataset, improving accuracy and relevance. It saves time, resources, and enhances performance without training an entirely new model.

## Getting started

Follow the steps below to getting started with fine-tuning process using LoRA and experiment generating your own fine-tuned models :)

### 0. Install

Activate Python virtual environment and install dependencies:
```
python -m venv .venv

# Activate virtual environment on Windows
./.venv/Scripts/Activate.ps1

# Activate virtual environment on Linux/MacOS
source ./.venv/bin/activate

pip install -r requirements.txt
```

### 1. Defining Goal and Base Model

For this example, I've decided to generate a Q&A assistant to answer questions regarding to Yu-Gi-Oh! Card Game rules, exclusively extracted from the official rulebook in `./data/yugioh_rulebook.pdf`.

I've decided to use Meta's Llama 3.2 with 1B parameters (`meta-llama/llama-3.2-1B-Instruct`) for this task, since it's a small and relatively good for response quality.

### 2. Preparing Dataset

For this example, I've generated `yugioh_rulebook_qa.json` with Q&A samples from `yugioh_rulebook.pdf` using ChatGPT.
You can do the same with any other document and any powerful models services such as OpenAI's, Anthropic's or Google's services using the prompt below:

```
Exclusively based on the attached file content, generate 100 unique and high quality Q&A pairs that explores all the document content details.
Follow the structure below for the output format:
[
    {
        "question": "...",
        "answer": "..."
    },
    ...
]
```

With the Q&A dataset onpen the `./src/_01_prepare_dataset.ipynb` Notebook and follow the instructions to generate a ChatML structured dataset.

### 3. Fine-tuning the model

With ChatML dataset in your hands, you're ready to run the fine-tuning process using LoRA! Open the `./src/_02_finetune_model.ipynb` Notebook and follow the instructions to fine-tune a model, based on Llama 3.2 1B model.

This step should generate a new LoRA adapter for the model.

### 4. Evaluate model result

Now, use the generated adapter to evaluate your fine-tune results. I've separated a few questions that is not present in the training dataset, and usually tricky to correctly respond!

Here we're using ROUGE metrics to evaluate the model performance. Open the `./src/_03_evaluate_model.ipynb` Notebook to try it yourself :).
