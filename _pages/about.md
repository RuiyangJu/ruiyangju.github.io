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

I am currently pursuing the M.S. degree at the [Graduate Institute of Networking and Multimedia](https://www.inm.ntu.edu.tw/), [National Taiwan University](https://www.ntu.edu.tw/), Taipei City, Taiwan. 
I am now a member of [NTU imLab](https://ntuimlab.tw/), and advised by Prof. [Yi-Ping Hung](https://scholar.google.com/citations?user=gUYquw0AAAAJ).

I received my B.S. degree in the Department of [Electrical and Computer Engineering](http://www.ee.tku.edu.tw/) from [Tamkang University](https://www.tku.edu.tw/), New Taipei City, Taiwan, in 2023. 
From 2020 to 2023, I conducted research in the Advanced Mixed-Operation System Laboratory (AMOS Lab.) at Tamkang University, focusing on deep learning and computer vision under the supervision of Prof. [Jen-Shiun Chiang](https://scholar.google.com/citations?user=vb5-3aQAAAAJ).

My primary research areas include Deep Learning (DL), Neural Networks (NN), Computer Vision (CV), and Image Processing (IP). In addition, I have contributed to some projects in other fields, such as Natural Language Processing (NLP), and Speech & Audio. I have published 10+ papers <a href='https://scholar.google.com/citations?user=r8F35p8AAAAJ'><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fruiyangju%2Fruiyangju.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> at the international journals or conferences.

Further details about my background can be found in my resume (available in both 
<a href='https://ruiyangju.github.io/images/CV_English.pdf'><img src='https://img.shields.io/badge/Resume-English-white?color=green'></a> and <a href='https://ruiyangju.github.io/images/CV_Chinese.pdf'><img src='https://img.shields.io/badge/Resume-Chinese-white?color=blue'></a>).

# News
- *2025.01*: One paper is accepted by <strong>ICRA 2025</strong> ([Webpage](https://www.neiljin.site/projects/orbsfm/)).
- *2025.01*: Our split GRAZPEDWRI-DX dataset is now [avaliable](https://ruiyangju.github.io/GRAZPEDWRI-DX_JU/).
- *2024.09*: One paper is accepted by <strong>Knowledge-Based Systems</strong> (IF=7.2).

# Research
## Document Binarization
<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img  src='https://ruiyangju.github.io/images/Figure/document-binarization.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
  
The efficient extraction of text information from the background in degraded color document images is an important challenge. The imperfect preservation of some manuscripts has led to different types of degradation over time, such as page yellowing, staining, and ink bleeding, seriously affecting the results of document image binarization. 
We propose a three-stage network method based on generative adversarial networks (GANs) to perform document image enhancement and binarization.

- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/three-stage-binarization-of-color-document/binarization-on-h-dibco-2018)](https://paperswithcode.com/sota/binarization-on-h-dibco-2018?p=three-stage-binarization-of-color-document)
- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/three-stage-binarization-of-color-document/binarization-on-h-dibco-2014)](https://paperswithcode.com/sota/binarization-on-h-dibco-2014?p=three-stage-binarization-of-color-document)
</div>
</div>

## Fracture Detection
<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='https://ruiyangju.github.io/images/Figure/fracture-detection.gif' alt="sym" width="100%"></div></div>
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
  
- [Webpage](https://www.neiljin.site/projects/orbsfm/)
</div>
</div>

# Publications
## 2025
### Conference
- Yanlin Jin, <u>Rui-Yang Ju</u>, Haojun Liu, Yuzhong Zhong, “[ORB-SfMLearner: ORB-Guided Self-supervised Visual Odometry with Selective Online Adaptation](https://arxiv.org/abs/2409.11692)”, **IEEE International Conference on Robotics and Automation (ICRA)**, Atlanta, USA, 2025.

<details>
<summary>View more</summary>
  
## 2024
### Journal
- <u>Rui-Yang Ju</u>, Yu-Shian Lin, Yanlin Jin, Chih-Chia Chen, Chun-Tse Chien, Jen-Shiun Chiang, “[Three-stage Binarization of Color Document Images Based on Discrete Wavelet Transform and Generative Adversarial Networks](https://doi.org/10.1016/j.knosys.2024.112542)”, **Knowledge-Based Systems**, 2024.
- Chun-Tse Chien, <u>Rui-Yang Ju</u>, Kuang-Yi Chou, Jen-Shiun Chiang, “[YOLOv9 for Fracture Detection in Pediatric Wrist Trauma X-ray Images](http://dx.doi.org/10.1049/ell2.13248)”, **Electronics Letters**, 2024.

### Conference
- <u>Rui-Yang Ju</u>, Chun-Tse Chien, Jen-Shiun Chiang, “YOLOv8-ResCBAM: YOLOv8 Based on An Effective Attention Module for Pediatric Wrist Fracture Detection”, **International Conference on Neural Information Processing (ICONIP)**, Auckland, New Zealand, 2024.
- <u>Rui-Yang Ju</u>, Chun-Tse Chien, Chia-Min Lin, Jen-Shiun Chiang, “[Global Context Modeling in YOLOv8 for Pediatric Wrist Fracture Detection](https://doi.org/10.1109/ISPACS62486.2024.10869064)”, **International Symposium on Intelligent Signal Processing and Communication Systems (ISPACS)**, Kaohsiung, Taiwan, 2024.
- Yanbing Bai, Siao Li, <u>Rui-Yang Ju</u>, Zihao Yang, Jinze Yu, Jen-Shiun Chiang, “[FAD-SAR: A Novel Fishing Activity Detection System via Synthetic Aperture Radar Images Based on Deep Learning Method](https://doi.org/10.1109/ISPACS62486.2024.10869003)”, **International Symposium on Intelligent Signal Processing and Communication Systems (ISPACS)**, Kaohsiung, Taiwan, 2024.

### arXiv
- <u>Rui-Yang Ju</u>, KokSheik Wong, Jen-Shiun Chiang, “Efficient GANs for Document Image Binarization Based on DWT and Normalization”, arXiv preprint, 2024.
- <u>Rui-Yang Ju</u>, Chun-Tse Chien, Enkaer Xieerke, Jen-Shiun Chiang, “Pediatric Wrist Fracture Detection Using Feature Context Excitation Modules in X-ray Images”, arXiv preprint, 2024.
- Chun-Tse Chien, <u>Rui-Yang Ju</u>, Kuang-Yi Chou, Enkaer Xieerke, Jen-Shiun Chiang, “YOLOv8-AM: YOLOv8 Based on Effective Attention Mechanisms for Pediatric Wrist Fracture Detection”, arXiv preprint, 2024.
- Yanbing Bai, Zihao Yang, Jinze Yu, <u>Rui-Yang Ju</u>, Bin Yang, Erick Mas, Shunichi Koshimura, “Flood Data Analysis on SpaceNet 8 Using Apache Sedona”, arXiv preprint, 2024.

</details>

# Professional Services
## Conference Committee
- International Joint Conference on Neural Networks (IJCNN), Rome, Italy, 2025, **Reviewer**.
- IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Hyderabad, India, 2025, **Reviewer**.
- Pacific Rim International Conference on Artificial Intelligence (PRICAI), Kyoto, Japan, 2024, **Program Committee**.
- Pacific Rim International Conference on Artificial Intelligence (PRICAI), Jakarta, Indonesia, 2023, **Program Committee**.

# Honors
- *2024.11*: NTU Scholarship, TWD9,000
- *2024.05*: NTU Scholarship, TWD8,000
- *2023.11*: NTU Scholarship, TWD8,000
- *2022.12*: TKU Scholarship (Top 1%), TWD10,000
- *2022.05*: TKU Academic Award (Top 5%, College of Engineer)
- *2021.05*: TKU Scholarship (Top 1%), TWD10,000

# Educations
- *2023.09 - 2025.06*, Graduate Institute of Networking and Multimedia, National Taiwan University, Taipei City
- *2019.09 - 2023.06*, Electrical and Computer Engineering, Tamkang University, New Taipei City
