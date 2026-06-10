from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import FancyArrowPatch, Rectangle


RESULTS = Path("results")


def save_vit_architecture() -> None:
    blocks = [
        ("Image", "224x224"),
        ("Patchify", "16x16 patches"),
        ("Linear\nprojection", "patch tokens"),
        ("Add position\nembedding", "order signal"),
        ("Transformer\nencoder", "MSA + MLP"),
        ("Class token", "image summary"),
        ("Classifier", "class scores"),
    ]
    fig, ax = plt.subplots(figsize=(12, 3.8))
    ax.axis("off")
    x = 0.03
    for i, (title, detail) in enumerate(blocks):
        width = 0.12
        rect = Rectangle((x, 0.38), width, 0.28, facecolor="#efe6f7", edgecolor="#674b8f", linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + width / 2, 0.55, title, ha="center", va="center", fontsize=10, weight="bold")
        ax.text(x + width / 2, 0.44, detail, ha="center", va="center", fontsize=8)
        if i < len(blocks) - 1:
            ax.add_patch(FancyArrowPatch((x + width, 0.52), (x + width + 0.035, 0.52), arrowstyle="->", mutation_scale=15, linewidth=1.3))
        x += width + 0.045
    ax.set_title("Vision Transformer Architecture Flow", fontsize=15, weight="bold")
    plt.tight_layout()
    plt.savefig(RESULTS / "vit_architecture_flow.png", dpi=180)
    plt.close()


def save_attention_sketch() -> None:
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    positions = [(0.25, 0.75), (0.5, 0.75), (0.75, 0.75), (0.25, 0.5), (0.5, 0.5), (0.75, 0.5), (0.25, 0.25), (0.5, 0.25), (0.75, 0.25)]
    for idx, (x, y) in enumerate(positions):
        rect = Rectangle((x - 0.055, y - 0.055), 0.11, 0.11, facecolor="#dce9f8", edgecolor="#2f5f9f")
        ax.add_patch(rect)
        ax.text(x, y, f"p{idx+1}", ha="center", va="center", fontsize=9)
    center = positions[4]
    for pos in positions:
        if pos != center:
            ax.add_patch(FancyArrowPatch(center, pos, arrowstyle="->", mutation_scale=9, linewidth=0.9, alpha=0.55))
    ax.set_title("Self-Attention Connects Patch Tokens", fontsize=13, weight="bold")
    plt.tight_layout()
    plt.savefig(RESULTS / "patch_attention_sketch.png", dpi=180)
    plt.close()


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    papers = pd.DataFrame(
        [
            {
                "paper": "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale",
                "authors": "Dosovitskiy et al.",
                "year": 2020,
                "url": "https://arxiv.org/abs/2010.11929",
                "what_they_did": "Introduced ViT by splitting images into patches and processing them with a standard Transformer encoder.",
                "main_result_or_claim": "Pure Transformers can perform very well for image classification when pretrained on large datasets.",
                "lesson": "Attention can replace convolution, but scale is critical.",
            },
            {
                "paper": "Training Data-Efficient Image Transformers & Distillation through Attention",
                "authors": "Touvron et al.",
                "year": 2020,
                "url": "https://arxiv.org/abs/2012.12877",
                "what_they_did": "Introduced DeiT, using strong training recipes and distillation to train ViTs on ImageNet without huge private datasets.",
                "main_result_or_claim": "A ViT-style model can be competitive using ImageNet-only training and teacher-student distillation.",
                "lesson": "Training strategy can reduce ViT's data hunger.",
            },
            {
                "paper": "Swin Transformer: Hierarchical Vision Transformer using Shifted Windows",
                "authors": "Liu et al.",
                "year": 2021,
                "url": "https://arxiv.org/abs/2103.14030",
                "what_they_did": "Proposed hierarchical shifted-window attention for efficient vision backbones.",
                "main_result_or_claim": "Swin works well for classification and dense prediction tasks such as detection and segmentation.",
                "lesson": "Local windows and hierarchy bring back useful image priors.",
            },
            {
                "paper": "Masked Autoencoders Are Scalable Vision Learners",
                "authors": "He et al.",
                "year": 2021,
                "url": "https://arxiv.org/abs/2111.06377",
                "what_they_did": "Used masked patch reconstruction as a self-supervised pretraining task for ViT models.",
                "main_result_or_claim": "High masking ratios and asymmetric encoder-decoder design make scalable visual pretraining effective.",
                "lesson": "Self-supervised pretraining is a major path for strong vision transformers.",
            },
        ]
    )
    papers.to_csv(RESULTS / "reviewed_papers.csv", index=False)

    comparison = pd.DataFrame(
        [
            ("ViT", "global attention over fixed image patches", "needs large-scale pretraining", "simple architecture"),
            ("DeiT", "ViT plus data-efficient training and distillation", "depends on teacher/training recipe", "ImageNet-only training becomes stronger"),
            ("Swin", "shifted local-window attention with hierarchy", "more complex architecture", "better fit for dense vision tasks"),
            ("MAE", "masked patch reconstruction pretraining", "pretraining objective, not classifier alone", "scalable self-supervised learning"),
        ],
        columns=["method", "core_idea", "limitation", "why_it_matters"],
    )
    comparison.to_csv(RESULTS / "paper_comparison.csv", index=False)

    architecture = pd.DataFrame(
        [
            ("Image", "Input image is split into patches."),
            ("Patch embedding", "Each patch becomes a token vector."),
            ("Position embedding", "Location information is added to token vectors."),
            ("Transformer encoder", "Self-attention and MLP blocks mix patch information."),
            ("Class token", "A learned token summarizes image-level information."),
            ("Classifier", "The final representation is mapped to class scores."),
        ],
        columns=["stage", "purpose"],
    )
    architecture.to_csv(RESULTS / "vit_architecture_table.csv", index=False)
    save_vit_architecture()
    save_attention_sketch()
    print(papers[["year", "paper", "lesson"]].to_string(index=False))


if __name__ == "__main__":
    main()
