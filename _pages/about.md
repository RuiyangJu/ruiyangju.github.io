---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

<!--
I am currently pursuing a Ph.D. at the [Graduate School of Informatics](https://www.i.kyoto-u.ac.jp/), [Kyoto University](https://www.kyoto-u.ac.jp/), Japan. I am working at the [LSTA Lab.](https://www.lsta.media.kyoto-u.ac.jp/), where I conduct research on document and text analysis, recognition, and processing. If you are interested in any form of academic collaboration, please feel free to email me.
-->

I graduated from the [Graduate Institute of Networking and Multimedia](https://www.inm.ntu.edu.tw/), [National Taiwan University](https://www.ntu.edu.tw/), Taipei, Taiwan, with a Master of Science (M.S.) degree. I was a member of [NTU imLab](https://ntuimlab.tw/), and my master’s thesis focused on 3D Gaussian Splatting (3DGS).

I received my Bachelor of Science (B.S.) degree in [Electrical and Computer Engineering](http://www.ee.tku.edu.tw/) from [Tamkang University](https://www.tku.edu.tw/), New Taipei City, Taiwan, where I ranked first in my department. I conducted research in the Advanced Mixed-Operation System Laboratory (AMOS Lab.) at Tamkang University, focusing on Image Processing and Computer Vision.

My primary research interests include Natural Language Processing (Large Language Models), Computer Vision (Document Binarization, Image Generation, Super-Resolution, Object Detection, Optical Character Recognition), Computer Graphics (3D Gaussian Blendshapes). I have published 20+ papers <a href='https://scholar.google.com/citations?user=r8F35p8AAAAJ'><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fruiyangju%2Fruiyangju.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> at the international journals or conferences.

<!--
Further details about my background are available in <a href='https://ruiyangju.github.io/images/CV_English.pdf'><img src='https://img.shields.io/badge/Resume-English-white?color=green'></a> (updated in July 2025).
-->

# News
- 2025.06: I receive an offer for a PhD student at Kyoto University, Japan.
- 2025.06: My master's thesis project, ToonifyGB, is now available ([Project](https://ruiyangju.github.io/ToonifyGB)).
- 2025.01: One paper is accepted by <strong>ICRA 2025</strong> ([Project](https://www.neiljin.site/projects/orbsfm/)).
- 2025.01: Our split GRAZPEDWRI-DX dataset is now available ([Project](https://ruiyangju.github.io/GRAZPEDWRI-DX_JU/)).
- 2024.09: One paper is accepted by <strong>Knowledge-Based Systems</strong> (IF=7.2) ([GitHub](https://github.com/abcpp12383/ThreeStageBinarization)).

# Publication
## 3D stylized Head Avatar
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img  src='https://ruiyangju.github.io/images/Figure/ToonifyGB.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ToonifyGB: StyleGAN-based Gaussian Blendshapes for 3D Stylized Head Avatars](https://arxiv.org/abs/2505.10072) \\
**Rui-Yang Ju**, Sheng-Yen Huang, Yi-Ping Hung \\
[Project](https://ruiyangju.github.io/ToonifyGB)｜[GitHub](https://github.com/RuiyangJu/ToonifyGB)
<details>
<summary>Abstract</summary>
The introduction of 3D Gaussian blendshapes has enabled the real-time reconstruction of animatable head avatars from monocular video. Toonify, a StyleGAN-based framework, has become widely used for facial image stylization. To extend Toonify for synthesizing diverse stylized 3D head avatars using Gaussian blendshapes, we propose an efficient two-stage framework, ToonifyGB. In Stage 1 (stylized video generation), we employ an improved StyleGAN to generate the stylized video from the input video frames, which addresses the limitation of cropping aligned faces at a fixed resolution as preprocessing for normal StyleGAN. This process provides a more stable video, which enables Gaussian blendshapes to better capture the high-frequency details of the video frames, and efficiently generate high-quality animation in the next stage. In Stage 2 (Gaussian blendshapes synthesis), we learn a stylized neutral head model and a set of expression blendshapes from the generated video. By combining the neutral head model with expression blendshapes, ToonifyGB can efficiently render stylized avatars with arbitrary expressions. We validate the effectiveness of ToonifyGB on the benchmark dataset using two styles: Arcane and Pixar.
</details>

</div>
</div>

## Document Binarization
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Knowledge-Based Systems 2024</div><img  src='https://ruiyangju.github.io/images/Figure/document-binarization.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Three-stage Binarization of Color Document Images Based on Discrete Wavelet Transform and Generative Adversarial Networks](https://doi.org/10.1016/j.knosys.2024.112542) \\
**Rui-Yang Ju**, Yu-Shian Lin, Yanlin Jin, Chih-Chia Chen, Chun-Tse Chien, Jen-Shiun Chiang \\
[GitHub](https://github.com/abcpp12383/ThreeStageBinarization)
<details>
<summary>Abstract</summary>
The efficient extraction of text information from the background in degraded color document images is an important challenge in the preservation of ancient manuscripts. The imperfect preservation of ancient manuscripts has led to different types of degradation over time, such as page yellowing, staining, and ink bleeding, seriously affecting the results of document image binarization. This work proposes an effective three-stage network method to image enhancement and binarization of degraded documents using generative adversarial networks (GANs). Specifically, in Stage-1, we first split the input images into multiple patches, and then split these patches into four single-channel patch images (gray, red, green, and blue). Then, three single-channel patch images (red, green, and blue) are processed by the discrete wavelet transform (DWT) with normalization. In Stage-2, we use four independent generators to separately train GAN models based on the four channels on the processed patch images to extract color foreground information. Finally, in Stage-3, we train two independent GAN models on the outputs of Stage-2 and the resized original input images (512 × 512) as the local and global predictions to obtain the final outputs. The experimental results show that the Avg-Score metrics of the proposed method are 77.64, 77.95, 79.05, 76.38, 75.34, and 77.00 on the (H)-DIBCO 2011, 2013, 2014, 2016, 2017, and 2018 datasets, which are at the state-of-the-art level.
</details>

</div>
</div>

- ``PRICAI 2023`` [CCDWT-GAN: Generative Adversarial Networks Based on Color Channel Using Discrete Wavelet Transform for Document Image Binarization](https://doi.org/10.1007/978-981-99-7019-3_19), **Rui-Yang Ju**, Yu-Shian Lin, Jen-Shiun Chiang, Chih-Chia Chen, Wei-Han Chen, Chun-Tse Chien.

## Fracture Detection
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Scientific Reports 2023</div><img src='https://ruiyangju.github.io/images/Figure/fracture-detection.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Fracture Detection in Pediatric Wrist Trauma X-ray Images Using YOLOv8 Algorithm](https://doi.org/10.1038/s41598-023-47460-7) \\
**Rui-Yang Ju**, Weiming Cai \\
[Project](https://ruiyangju.github.io/GRAZPEDWRI-DX_JU/)|[Application](https://fracture-detection-yolo.streamlit.app/)
<details>
<summary>Abstract</summary>
Hospital emergency departments frequently receive lots of bone fracture cases, with pediatric wrist trauma fracture accounting for the majority of them. Before pediatric surgeons perform surgery, they need to ask patients how the fracture occurred and analyze the fracture situation by interpreting X-ray images. The interpretation of X-ray images often requires a combination of techniques from radiologists and surgeons, which requires time-consuming specialized training. With the rise of deep learning in the field of computer vision, network models applying for fracture detection has become an important research topic. In this paper, we use data augmentation to improve the model performance of YOLOv8 algorithm (the latest version of You Only Look Once) on a pediatric wrist trauma X-ray dataset (GRAZPEDWRI-DX), which is a public dataset. The experimental results show that our model has reached the state-of-the-art (SOTA) mean average precision (mAP 50). Specifically, mAP 50 of our model is 0.638, which is significantly higher than the 0.634 and 0.636 of the improved YOLOv7 and original YOLOv8 models. To enable surgeons to use our model for fracture detection on pediatric wrist trauma X-ray images, we have designed the application “Fracture Detection Using YOLOv8 App” to assist surgeons in diagnosing fractures, reducing the probability of error analysis, and providing more useful information for surgery.
</details>

</div>
</div>

- ``IEEE Access 2025`` [YOLOv8-AM: YOLOv8 Based on Effective Attention Mechanisms for Pediatric Wrist Fracture Detection](https://ieeexplore.ieee.org/document/10918980), Chun-Tse Chien, **Rui-Yang Ju**, Kuang-Yi Chou, Enkaer Xieerke, Jen-Shiun Chiang.
- ``Electronics Letters 2024`` [YOLOv9 for Fracture Detection in Pediatric Wrist Trauma X-ray Images](http://dx.doi.org/10.1049/ell2.13248), Chun-Tse Chien, **Rui-Yang Ju**, Kuang-Yi Chou, Jen-Shiun Chiang.
- ``ICONIP 2024`` [YOLOv8-ResCBAM: YOLOv8 Based on An Effective Attention Module for Pediatric Wrist Fracture Detection](https://doi.org/10.1007/978-981-96-6972-1_28), **Rui-Yang Ju**, Chun-Tse Chien, Jen-Shiun Chiang.

## ORB-SfMLearner
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICRA 2025</div><img src='https://ruiyangju.github.io/images/Figure/ORB.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ORB-SfMLearner: ORB-Guided Self-supervised Visual Odometry with Selective Online Adaptation](https://arxiv.org/abs/2409.11692) \\
Yanlin Jin, **Rui-Yang Ju**, Haojun Liu, Yuzhong Zhong \\
[Project](https://www.neiljin.site/projects/orbsfm/)
<details>
<summary>Abstract</summary>
Deep visual odometry, despite extensive research, still faces limitations in accuracy and generalizability that prevent its broader application. To address these challenges, we propose an Oriented FAST and Rotated BRIEF (ORB)-guided visual odometry with selective online adaptation named ORB-SfMLearner. We present a novel use of ORB features for learning-based ego-motion estimation, leading to more robust and accurate results. We also introduce the cross-attention mechanism to enhance the explainability of PoseNet and have revealed that driving direction of the vehicle can be explained through the attention weights. To improve generalizability, our selective online adaptation allows the network to rapidly and selectively adjust to the optimal parameters across different domains. Experimental results on KITTI and vKITTI datasets show that our method outperforms previous state-of-the-art deep visual odometry methods in terms of ego-motion accuracy and generalizability.
</details>

</div>
</div>

## Super Resolution 
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Multimedia Tools and Applications 2023</div><img src='https://ruiyangju.github.io/images/Figure/SwinOIR.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Resolution enhancement processing on low quality images using swin transformer based on interval dense connection strategy](https://doi.org/10.1007/s11042-023-16088-0) \\
**Rui-Yang Ju**, Chih-Chia Chen, Jen-Shiun Chiang, Yu-Shian Lin, Wei-Han Chen, Chun-Tse Chien \\
[GitHub](https://github.com/Rubbbbbbbbby/SwinOIR)
<details>
<summary>Abstract</summary>
The Transformer-based method has demonstrated remarkable performance for image super-resolution in comparison to the method based on the convolutional neural networks (CNNs). However, using the self-attention mechanism like SwinIR (Image Restoration Using Swin Transformer) to extract feature information from images needs a significant amount of computational resources, which limits its application on low computing power platforms. To improve the model feature reuse, this research work proposes the Interval Dense Connection Strategy, which connects different blocks according to the newly designed algorithm. We apply this strategy to SwinIR and present a new model, which named SwinOIR (Object Image Restoration Using Swin Transformer). For image super-resolution, an ablation study is conducted to demonstrate the positive effect of the Interval Dense Connection Strategy on the model performance. Furthermore, we evaluate our model on various popular benchmark datasets, and compare it with other state-of-the-art (SOTA) lightweight models. For example, SwinOIR obtains a PSNR of 26.62 dB for x4 upscaling image super-resolution on Urban100 dataset, which is 0.15 dB higher than the SOTA model SwinIR. For real-life application, this work applies the lastest version of You Only Look Once (YOLOv8) model and the proposed model to perform object detection and real-life image super-resolution on low-quality images.
</details>

</div>
</div>

# Professional Service
## Journal Reviewer
<details>
<summary>View more</summary>
<ul>
  <li>Pattern Recognition.</li>
  <li>Knowledge-based Systems.</li>
  <li>Neurocomputing.</li>
  <li>Alexandria Engineering Journal.</li>
  <li>Neural Networks.</li>
  <li>IEEE Signal Processing Letters.</li>
  <li>Engineering Applications of Artificial Intelligence.</li>
  <li>Multimedia Tools and Applications.</li>
  <li>Scientific Reports.</li>
  <li>Cognitive Computation.</li>
  <li>International Journal of Multimedia Information Retrieval.</li>
  <li>International Journal of Machine Learning and Cybernetics.</li>
  <li>Plos One.</li>
  <li>Journal of Real-Time Image Processing.</li>
  <li>International Journal of Computational Intelligence Systems.</li>
  <li>The Journal of Supercomputing.</li>
  <li>Frontiers in Computer Science.</li>
  <li>Signal, Image and Video Processing.</li>
  <li>Telecommunication Systems.</li>
  <li>Journal of Engineering.</li>
  <li>Computer Methods in Biomechanics and Biomedical Engineering: Imaging & Visualization.</li>
</ul>
</details>

## Conference Committee and Reviewer
<details>
<summary>View more</summary>
<ul>
  <li>Pacific Rim International Conference on Artificial Intelligence (PRICAI), Wellington, New Zealand, 2025, Program Committee.</li>
  <li>International Joint Conference on Neural Networks (IJCNN), Rome, Italy, 2025, Reviewer.</li>
  <li>IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Hyderabad, India, 2025, Reviewer.</li>
  <li>Pacific Rim International Conference on Artificial Intelligence (PRICAI), Kyoto, Japan, 2024, Program Committee.</li>
  <li>Pacific Rim International Conference on Artificial Intelligence (PRICAI), Jakarta, Indonesia, 2023, Program Committee.</li>
</ul>
</details>

# Scholarship
<span class='anchor' id='scholarship'></span>
- National Taiwan University Academic Scholarship, Total: NT$32,000, 2023 – 2025.
- National Taiwan University Research Scholarship, Total: NT$36,000, 2024.
- Sino International Business Innovation Association (SIBIA) Scholarship, Total: US$900, 2021, 2022, 2024.
- Tamkang University Research Scholarship, Total: NT$48,000, 2021 – 2022.
- Tamkang University Academic Scholarship (Top 1%), Total: NT$20,000, 2021, 2022.

# Education
<!--
- 2025.10 - 2028.09, Graduate School of Informatics, Kyoto University, Kyoto, Japan.
-->
- 2023.09 - 2025.06, Graduate Institute of Networking and Multimedia, National Taiwan University, Taipei, Taiwan.
- 2019.09 - 2023.06, Electrical and Computer Engineering, Tamkang University, New Taipei, Taiwan.
