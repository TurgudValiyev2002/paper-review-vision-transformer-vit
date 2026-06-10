# Dosovitskiy et al. 2020: Vision Transformer

Paper: "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"  
Link: https://arxiv.org/abs/2010.11929

This paper introduced the Vision Transformer approach for image classification. The central idea is simple and powerful: split an image into fixed-size patches, turn each patch into a token, add position embeddings, and process the token sequence with a standard Transformer encoder.

The paper challenged the assumption that convolution is necessary for high-performing image recognition. Instead of building locality directly into the architecture, ViT lets self-attention learn relationships between patch tokens.

The main lesson is that attention can work for vision, but scale matters. ViT performs best when pretrained on large datasets and then transferred to smaller benchmarks. This is important because it shows both the strength and weakness of the method.

What we learn is that ViT changes image modeling from grid processing to sequence processing. This connects computer vision more closely with NLP transformer methods.

The limitation is data hunger. A plain ViT has weaker built-in image bias than CNNs, so it often needs large pretraining data or strong training recipes to perform well.
