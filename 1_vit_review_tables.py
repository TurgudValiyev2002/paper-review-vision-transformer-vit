from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RESULTS = Path("results")

def main():
    RESULTS.mkdir(exist_ok=True)
    pipeline = pd.DataFrame([
        ("Image", "Input image is divided into fixed-size patches."),
        ("Patch embedding", "Each patch is flattened and projected into a vector."),
        ("Position embedding", "Position information is added because attention has no natural order."),
        ("Transformer encoder", "Self-attention mixes information across patches."),
        ("Class token", "A special token summarizes the image for classification."),
        ("MLP head", "The final representation is mapped to class scores."),
    ], columns=["stage", "explanation"])
    pipeline.to_csv(RESULTS / "vit_pipeline.csv", index=False)
    comparison = pd.DataFrame([
        ("CNN", "local convolution", "strong image prior", "efficient on smaller data"),
        ("ViT", "global self-attention over patches", "weaker image prior", "benefits strongly from large-scale pretraining"),
    ], columns=["model_family", "main_operation", "inductive_bias", "data_requirement"])
    comparison.to_csv(RESULTS / "cnn_vs_vit.csv", index=False)
    lessons = pd.DataFrame([
        ("patches as tokens", "Images can be processed like sequences."),
        ("scale matters", "ViT becomes strong when trained on large datasets."),
        ("less built-in locality", "The model learns spatial relations instead of hard-coding them."),
        ("transfer learning", "Pretraining is important for practical performance."),
    ], columns=["lesson", "interpretation"])
    lessons.to_csv(RESULTS / "vit_key_lessons.csv", index=False)
    plt.figure(figsize=(8,3))
    plt.bar(pipeline["stage"], range(1, len(pipeline)+1), color="#3d6fb6")
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Pipeline order")
    plt.title("Vision Transformer Pipeline")
    plt.tight_layout()
    plt.savefig(RESULTS / "vit_pipeline.png", dpi=160)
    print(pipeline.to_string(index=False))

if __name__ == "__main__":
    main()
