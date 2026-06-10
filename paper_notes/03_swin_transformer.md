# Liu et al. 2021: Swin Transformer

Paper: "Swin Transformer: Hierarchical Vision Transformer using Shifted Windows"  
Link: https://arxiv.org/abs/2103.14030

Swin Transformer improves the practical architecture of vision transformers. The original ViT uses global attention over patch tokens, which can be expensive and less natural for dense vision tasks. Swin introduces local window attention and shifted windows.

The model also builds a hierarchy. As the network goes deeper, patch representations are merged, producing multi-scale features. This makes Swin more similar to CNN backbones in how it handles resolution and scale.

The main contribution is making transformers more useful as general-purpose vision backbones. Swin is not only for classification; it is also suitable for object detection and segmentation.

What we learn is that pure global attention is not always the most practical design. Vision benefits from locality, hierarchy, and multi-scale representation.

The limitation is architectural complexity. Swin is more engineered than the original ViT. That complexity is useful, but it makes the model less minimal and harder to explain than plain ViT.
