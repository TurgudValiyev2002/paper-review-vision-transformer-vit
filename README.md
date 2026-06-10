# Paper Review: Vision Transformer

## Motivation

Vision Transformer changed computer vision by showing that a pure transformer architecture can work well for image classification when trained at sufficient scale. Understanding ViT is important because many modern vision-language and multimodal models build on this idea.

## Project Goal

We reviewed the main ViT idea: split an image into patches, treat patches like tokens, and process them with a transformer encoder.

## Paper / Problem

The reviewed work is the Vision Transformer approach for image recognition. The central problem is whether self-attention can replace convolution as the main operation for visual classification.

## Tools

Python, pandas, and matplotlib.

## Method

We summarized the ViT pipeline, compared CNNs and ViTs, and extracted key lessons into structured result tables.

## Hyperparameters

No model was trained in this review. Important ViT design settings include patch size, embedding dimension, number of transformer layers, number of attention heads, MLP size, and pretraining dataset size.

## Results

The result files are:

- `results/vit_pipeline.csv`
- `results/cnn_vs_vit.csv`
- `results/vit_key_lessons.csv`
- `results/vit_pipeline.png`

## Interpretation

ViT reduces image modeling to sequence modeling. This is powerful, but it also means the model has less built-in image structure than a CNN. Large-scale pretraining becomes very important.

## Conclusion

ViT is a foundation for modern vision models. Its key lesson is that attention can model images effectively, but data scale and pretraining are critical.

## How To Run

```bash
pip install -r requirements.txt
python 1_vit_review_tables.py
```
