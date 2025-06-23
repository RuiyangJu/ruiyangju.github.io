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

I am currently pursuing a Master of Science (M.S.) at the [Graduate Institute of Networking and Multimedia](https://www.inm.ntu.edu.tw/), [National Taiwan University](https://www.ntu.edu.tw/), Taipei City, Taiwan. 
I am a member of [NTU imLab](https://ntuimlab.tw/), advised by Prof. [Yi-Ping Hung](https://scholar.google.com/citations?user=gUYquw0AAAAJ), and my current research focuses on 3D Gaussian Splatting (3DGS).

I received my Bachelor of Science (B.S.) degree in [Electrical and Computer Engineering](http://www.ee.tku.edu.tw/) from [Tamkang University](https://www.tku.edu.tw/), New Taipei City, Taiwan, in 2023, where I ranked first in my department.
From 2020 to 2023, I conducted research in the Advanced Mixed-Operation System Laboratory (AMOS Lab.) at Tamkang University, focusing on deep learning and computer vision under the supervision of Prof. [Jen-Shiun Chiang](https://scholar.google.com/citations?user=vb5-3aQAAAAJ).

My primary research areas include Deep Learning (DL), Neural Networks (NN), Computer Vision (CV), and Image Processing (IP). In addition, I have contributed to some projects in other fields, such as Natural Language Processing (NLP), and Speech & Audio. I have published 10+ papers <a href='https://scholar.google.com/citations?user=r8F35p8AAAAJ'><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fruiyangju%2Fruiyangju.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> at the international journals or conferences.

Further details about my background are available in <a href='https://ruiyangju.github.io/images/CV_English.pdf'><img src='https://img.shields.io/badge/Resume-English-white?color=green'></a> (updated in June 2025).

# News
- *2025.01*: One paper is accepted by <strong>ICRA 2025</strong> ([Project](https://www.neiljin.site/projects/orbsfm/)).
- *2025.01*: Our split GRAZPEDWRI-DX dataset is now available ([Project](https://ruiyangju.github.io/GRAZPEDWRI-DX_JU/)).
- *2024.09*: One paper is accepted by <strong>Knowledge-Based Systems</strong> (IF=7.2) ([GitHub](https://github.com/abcpp12383/ThreeStageBinarization)).

# Research
## 3D stylized Head Avatar
<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img  src='https://ruiyangju.github.io/images/Figure/ToonifyGB.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ToonifyGB: StyleGAN-based Gaussian Blendshapes for 3D Stylized Head Avatars](https://arxiv.org/abs/2505.10072) \\
**Rui-Yang Ju**, Sheng-Yen Huang, Yi-Ping Hung
- <details>
  <summary>Abstract</summary>
  The introduction of 3D Gaussian blendshapes has enabled the real-time reconstruction of animatable head avatars from monocular video. Toonify, a StyleGAN-based framework, has become widely used for facial image stylization. To extend Toonify for synthesizing diverse stylized 3D head avatars using Gaussian blendshapes, we propose an efficient two-stage framework, ToonifyGB. In Stage 1 (stylized video generation), we employ an improved StyleGAN to generate the stylized video from the input video frames, which addresses the limitation of cropping aligned faces at a fixed resolution as preprocessing for normal StyleGAN. This process provides a more stable video, which enables Gaussian blendshapes to better capture the high-frequency details of the video frames, and efficiently generate high-quality animation in the next stage. In Stage 2 (Gaussian blendshapes synthesis), we learn a stylized neutral head model and a set of expression blendshapes from the generated video. By combining the neutral head model with expression blendshapes, ToonifyGB can efficiently render stylized avatars with arbitrary expressions. We validate the effectiveness of ToonifyGB on the benchmark dataset using two styles: Arcane and Pixar.
  </details>

</div>
</div>

## Document Binarization
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Knowledge-Based Systems 2024</div><img  src='https://ruiyangju.github.io/images/Figure/document-binarization.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Three-stage Binarization of Color Document Images Based on Discrete Wavelet Transform and Generative Adversarial Networks](https://doi.org/10.1016/j.knosys.2024.112542) \\
**Rui-Yang Ju**, Yu-Shian Lin, Yanlin Jin, Chih-Chia Chen, Chun-Tse Chien, Jen-Shiun Chiang
- <details>
  <summary>Abstract</summary>
  The efficient extraction of text information from the background in degraded color document images is an important challenge in the preservation of ancient manuscripts. The imperfect preservation of ancient manuscripts has led to different types of degradation over time, such as page yellowing, staining, and ink bleeding, seriously affecting the results of document image binarization. This work proposes an effective three-stage network method to image enhancement and binarization of degraded documents using generative adversarial networks (GANs). Specifically, in Stage-1, we first split the input images into multiple patches, and then split these patches into four single-channel patch images (gray, red, green, and blue). Then, three single-channel patch images (red, green, and blue) are processed by the discrete wavelet transform (DWT) with normalization. In Stage-2, we use four independent generators to separately train GAN models based on the four channels on the processed patch images to extract color foreground information. Finally, in Stage-3, we train two independent GAN models on the outputs of Stage-2 and the resized original input images (512 × 512) as the local and global predictions to obtain the final outputs. The experimental results show that the Avg-Score metrics of the proposed method are 77.64, 77.95, 79.05, 76.38, 75.34, and 77.00 on the (H)-DIBCO 2011, 2013, 2014, 2016, 2017, and 2018 datasets, which are at the state-of-the-art level.
  </details>
- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/three-stage-binarization-of-color-document/binarization-on-h-dibco-2018)](https://paperswithcode.com/sota/binarization-on-h-dibco-2018?p=three-stage-binarization-of-color-document)
- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/three-stage-binarization-of-color-document/binarization-on-h-dibco-2014)](https://paperswithcode.com/sota/binarization-on-h-dibco-2014?p=three-stage-binarization-of-color-document)
</div>
</div>

## Fracture Detection
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Scientific Reports 2023</div><img src='https://ruiyangju.github.io/images/Figure/fracture-detection.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Hospital emergency departments frequently receive lots of bone fracture cases, with pediatric wrist trauma fracture accounting for the majority of them. Before pediatric surgeons perform surgery, they need to ask patients how the fracture occurred and analyze the fracture situation by interpreting X-ray images. The interpretation of X-ray images often requires a combination of techniques from radiologists and surgeons, which requires time-consuming specialized training. With the rise of deep learning in the field of computer vision, network models applying for fracture detection has become an important research topic. 

- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/fce-yolov8-yolov8-with-feature-context/fracture-detection-on-grazpedwri-dx)](https://paperswithcode.com/sota/fracture-detection-on-grazpedwri-dx?p=fce-yolov8-yolov8-with-feature-context)
- [Our split dataset](https://ruiyangju.github.io/GRAZPEDWRI-DX_JU/)
- [Our web application](https://fracture-detection-yolo.streamlit.app/)
</div>
</div>

## ORB-SfMLearner
<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='https://ruiyangju.github.io/images/Figure/ORB.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
  
Deep visual odometry, despite extensive research, still faces limitations in accuracy and generalizability that prevent its broader application. To address these challenges, we propose an Oriented FAST and Rotated BRIEF (ORB)-guided visual odometry with selective online adaptation named ORB-SfMLearner. We present a novel use of ORB features for learning-based ego-motion estimation, leading to more robust and accurate results. 
  
- [Project](https://www.neiljin.site/projects/orbsfm/)
</div>
</div>

# Publications
## 2025
<details>
<summary>View more</summary>
<h3>Journal</h3>
<ul>
  <li>Chun-Tse Chien, <u>Rui-Yang Ju</u>, Kuang-Yi Chou, Enkaer Xieerke, Jen-Shiun Chiang, <a href="https://ieeexplore.ieee.org/document/10918980">“YOLOv8-AM: YOLOv8 Based on Effective Attention Mechanisms for Pediatric Wrist Fracture Detection”</a>, <strong>IEEE Access</strong>, 2025.</li>
</ul>
<h3>Conference</h3>
<ul>
  <li>Yanlin Jin, <u>Rui-Yang Ju</u>, Haojun Liu, Yuzhong Zhong, “ORB-SfMLearner: ORB-Guided Self-supervised Visual Odometry with Selective Online Adaptation”, <strong>IEEE International Conference on Robotics and Automation (ICRA)</strong>, Atlanta, USA, 2025.</li>
</ul>
</details>

## 2024
<details>
<summary>View more</summary>
<h3>Journal</h3>
<ul>
  <li>Chun-Tse Chien, <u>Rui-Yang Ju</u>, Kuang-Yi Chou, Jen-Shiun Chiang, <a href="http://dx.doi.org/10.1049/ell2.13248">“YOLOv9 for Fracture Detection in Pediatric Wrist Trauma X-ray Images”</a>, <strong>Electronics Letters</strong>, 2024.</li>
</ul>

<h3>Conference</h3>
<ul>
  <li><u>Rui-Yang Ju</u>, Chun-Tse Chien, Jen-Shiun Chiang, “YOLOv8-ResCBAM: YOLOv8 Based on An Effective Attention Module for Pediatric Wrist Fracture Detection”, <strong>International Conference on Neural Information Processing (ICONIP)</strong>, Auckland, New Zealand, 2024.</li>
  <li><u>Rui-Yang Ju</u>, Chun-Tse Chien, Chia-Min Lin, Jen-Shiun Chiang, <a href="https://doi.org/10.1109/ISPACS62486.2024.10869064">“Global Context Modeling in YOLOv8 for Pediatric Wrist Fracture Detection”</a>, <strong>International Symposium on Intelligent Signal Processing and Communication Systems (ISPACS)</strong>, Kaohsiung, Taiwan, 2024.</li>
  <li>Yanbing Bai, Siao Li, <u>Rui-Yang Ju</u>, Zihao Yang, Jinze Yu, Jen-Shiun Chiang, <a href="https://doi.org/10.1109/ISPACS62486.2024.10869003">“FAD-SAR: A Novel Fishing Activity Detection System via Synthetic Aperture Radar Images Based on Deep Learning Method”</a>, <strong>International Symposium on Intelligent Signal Processing and Communication Systems (ISPACS)</strong>, Kaohsiung, Taiwan, 2024.</li>
</ul>
</details>

## 2023
<details>
<summary>View more</summary>
<h3>Journal</h3>
<ul>
  <li><u>Rui-Yang Ju</u>, Weiming Cai, <a href="https://doi.org/10.1038/s41598-023-47460-7">“Fracture Detection in Pediatric Wrist Trauma X-ray Images Using YOLOv8 Algorithm”</a>, <strong>Scientific Reports</strong>, 2023.</li>
  <li><u>Rui-Yang Ju</u>* , Chih-Chia Chen* , Jen-Shiun Chiang, Yu-Shian Lin, Wei-Han Chen (*=equal contribution), <a href="https://doi.org/10.1007/s11042-023-16088-0">“Resolution Enhancement Processing on Low Quality Images Using Swin Transformer Based on Interval Dense Connection Strategy”</a>, <strong>Multimedia Tools and Applications (MTA)</strong>, 2023.</li>
  <li><u>Rui-Yang Ju</u>, Ting-Yu Lin, Jia-Hao Jian, Jen-Shiun Chiang, <a href="https://doi.org/10.1007/s11554-023-01271-1">“Efficient Convolutional Neural Networks on Raspberry Pi for Image Classification”</a>, <strong>Journal of Real-Time Image Processing (JRTIP)</strong>, 2023.</li>
</ul>

<h3>Conference</h3>
<ul>
  <li><u>Rui-Yang Ju</u>, Yu-Shian Lin, Jen-Shiun Chiang, Chih-Chia Chen, Wei-Han Chen, Chun-Tse Chien, <a href="https://doi.org/10.1007/978-981-99-7019-3_19">“CCDWT-GAN: Generative Adversarial Networks Based on Color Channel Using Discrete Wavelet Transform for Document Image Binarization”</a>, <strong>Pacific Rim International Conferences on Artificial Intelligence (PRICAI)</strong>, Jakarta, Indonesia, 2023.</li>
</ul>
</details>

# Professional Services
## Journal Reviewer
<details>
<summary>View more</summary>
<ul>
  <li>Pattern Recognition.</li>
  <li>Knowledge-based Systems.</li>
  <li>IEEE Signal Processing Letters.</li>
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

# Honors and Scholarships
<span class='anchor' id='honors-and-scholarships'></span>
## Honors
<details>
<summary>View more</summary>
<ul>
  <li>Silver Medal (Top 4%), Google Universal Image Embedding Challenge, ECCV 2022 Competition, 2022.10.</li>
  <li>Excellent Academic Performance Award, Tamkang University, 2022.05.</li>
  <li>The Innovation and Entrepreneurship Competition Excellent Award, Tamkang University, 2021.05.</li>
</ul>
</details>

## Scholarships
<details>
<summary>View more</summary>
<ul>
  <li>National Taiwan University Scholarship, 2023 – 2025, Total: NT$32,000</li>
  <li>National Taiwan University (imLab) Scholarship, 2024, Total: NT$36,000</li>
  <li>Sino International Business Innovation Association (SIBIA) Scholarship, 2021, 2022, 2024, Total: US$900</li>
  <li>Tamkang University Research Scholarship, 2021 – 2022, Total: NT$48,000</li>
  <li>Tamkang University Scholarship (Top 1%), 2021, 2022, Total: NT$20,000</li>
</ul>
</details>

# Educations
- *2023.09 - 2025.06*, Graduate Institute of Networking and Multimedia, National Taiwan University, Taipei City
- *2019.09 - 2023.06*, Electrical and Computer Engineering, Tamkang University, New Taipei City
