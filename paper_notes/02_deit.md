# Touvron et al. 2020: DeiT

Paper: "Training Data-Efficient Image Transformers & Distillation through Attention"  
Link: https://arxiv.org/abs/2012.12877

DeiT addresses a practical problem in the original ViT paper: ViTs can need very large pretraining datasets. The authors asked whether a vision transformer can be trained effectively on ImageNet without massive private datasets.

The paper introduced a stronger training recipe and a distillation strategy. A teacher model helps the transformer student learn. The distillation token is an important design detail because it gives the model a dedicated path for learning from the teacher.

The main contribution is data efficiency. DeiT showed that transformer-based vision models can be competitive with better training, not only with huge data scale.

What we learn is that architecture alone is not the full story. Training recipe, augmentation, regularization, and distillation can change the practical value of a model.

The limitation is that the method depends on careful training and teacher-student setup. It reduces the data problem but does not completely remove the need for strong training design.
