# Paper Review: Vision Transformer

## Motivation

Vision Transformer is important because it changed the assumption that image recognition must be built mainly around convolution. But the original ViT paper is only the starting point. To understand the topic properly, we also need to study data-efficient training, hierarchical attention, and self-supervised pretraining.

## Project Goal

We reviewed four papers:

1. ViT: images as patch tokens.
2. DeiT: data-efficient ViT training with distillation.
3. Swin Transformer: hierarchical shifted-window attention.
4. MAE: masked autoencoder pretraining for scalable vision learners.

The aim is to understand what ViT introduced, what problem it created, and how later papers improved it.

## Reviewed Papers

| Paper | Year | Main contribution |
|---|---:|---|
| [An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929) | 2020 | Introduced ViT: split images into patches and process them with a Transformer encoder. |
| [Training Data-Efficient Image Transformers & Distillation through Attention](https://arxiv.org/abs/2012.12877) | 2020 | Showed that ViTs can be trained more effectively on ImageNet using distillation and a strong recipe. |
| [Swin Transformer](https://arxiv.org/abs/2103.14030) | 2021 | Added hierarchy and shifted local windows for efficient vision backbones. |
| [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377) | 2021 | Used masked patch reconstruction for scalable self-supervised ViT pretraining. |

Short one-page notes for each paper are available in `paper_notes/`.

## What The Papers Did

The ViT paper treated an image as a sequence of fixed-size patch tokens. This made it possible to use the standard Transformer encoder for image classification. The main limitation was data scale: ViT worked best when pretrained on very large datasets.

DeiT addressed this data problem. It showed that better training recipes and distillation can make ViT-style models competitive without requiring enormous private pretraining datasets.

Swin Transformer changed the architecture. Instead of global attention everywhere, it used shifted local windows and a hierarchy. This made the transformer more efficient and more useful for dense prediction tasks such as object detection and segmentation.

MAE changed the training objective. It used masked patch reconstruction, showing that self-supervised pretraining can make large ViT models learn strong visual representations.

## Architecture Discussion

A basic ViT pipeline is:

Image -> patchify -> linear patch embedding -> position embedding -> Transformer encoder -> class token -> classifier.

The architecture is shown as a flow diagram because each stage transforms the representation.

## Review Artifacts

The repository includes:

- `results/reviewed_papers.csv`
- `results/paper_comparison.csv`
- `results/vit_architecture_table.csv`
- `results/vit_architecture_flow.png`
- `results/patch_attention_sketch.png`
- `paper_notes/01_vit.md`
- `paper_notes/02_deit.md`
- `paper_notes/03_swin_transformer.md`
- `paper_notes/04_masked_autoencoders.md`

## Interpretation

The main lesson is that ViT opened the door, but later papers made the idea more practical. DeiT improved data efficiency, Swin improved architectural efficiency and dense-task usability, and MAE improved pretraining.

## Conclusion

Vision Transformer should be studied as a research line, not as one isolated paper. The core idea is patch tokens plus self-attention, but practical success depends on training recipe, hierarchy, and pretraining strategy.

## How To Run

```bash
pip install -r requirements.txt
python 1_vit_review_tables.py
```
