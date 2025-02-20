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
<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img  src='https://ruiyangju.github.io/images/Figure/document-binarization.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
  
The efficient extraction of text information from the background in degraded color document images is an important challenge. 
The imperfect preservation of some manuscripts has led to different types of degradation over time, such as page yellowing, staining, and ink bleeding, seriously affecting the results of document image binarization. 
We propose a three-stage network method based on generative adversarial networks (GANs) to perform document image enhancement and binarization.

- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/three-stage-binarization-of-color-document/binarization-on-h-dibco-2018)](https://paperswithcode.com/sota/binarization-on-h-dibco-2018?p=three-stage-binarization-of-color-document)
- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/three-stage-binarization-of-color-document/binarization-on-dibco-2017)](https://paperswithcode.com/sota/binarization-on-dibco-2017?p=three-stage-binarization-of-color-document)
</div>
</div>


## Fracture Detection
<!--
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISPACS'24</div><img src='https://ruiyangju.github.io/images/Figure/FCE-YOLOv8.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Global Context Modeling in YOLOv8 for Pediatric Wrist Fracture Detection](https://arxiv.org/pdf/2407.03163)

**Rui-Yang Ju**, Chun-Tse Chien, et al.

International Symposium on Intelligent Signal Processing and Communication Systems, Kaohsiung, Taiwan, 2024

[**GitHub**](https://github.com/RuiyangJu/FCE-YOLOv8)

- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/fce-yolov8-yolov8-with-feature-context/object-detection-on-grazpedwri-dx)](https://paperswithcode.com/sota/object-detection-on-grazpedwri-dx?p=fce-yolov8-yolov8-with-feature-context)
- Journal Version: [Pediatric Wrist Fracture Detection Using Feature Context Excitation Modules in X-ray Images](https://arxiv.org/pdf/2410.01031), Under Review
- Integrate feature context excitation module into YOLOv8
</div>
</div>
-->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICONIP'24</div><img src='https://ruiyangju.github.io/images/Figure/YOLOv8-AM.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[YOLOv8-ResCBAM: YOLOv8 Based on An Effective Attention Module for Pediatric Wrist Fracture Detection](https://arxiv.org/pdf/2409.18826)

**Rui-Yang Ju**, Chun-Tse Chien, Jen-Shiun Chiang

International Conference on Neural Information Processing, Auckland, New Zealand, 2024

[**GitHub**](https://github.com/RuiyangJu/Fracture_Detection_Improved_YOLOv8)

- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/yolov8-rescbam-yolov8-based-on-an-effective/fracture-detection-on-grazpedwri-dx)](https://paperswithcode.com/sota/fracture-detection-on-grazpedwri-dx?p=yolov8-rescbam-yolov8-based-on-an-effective)
- Integrate attention modules into YOLOv8
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SR'23</div><img src='https://ruiyangju.github.io/images/Figure/YOLOv8.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Fracture Detection in Pediatric Wrist Trauma X-ray Images Using YOLOv8 Algorithm](https://arxiv.org/pdf/2304.05071)

**Rui-Yang Ju**, Weiming Cai

Scientific Reports, 2023

[**GitHub**](https://github.com/RuiyangJu/Bone_Fracture_Detection_YOLOv8) [**Journal**](https://www.nature.com/articles/s41598-023-47460-7) [**Dataset**](https://ruiyangju.github.io/GRAZPEDWRI-DX_JU/)
- First to use YOLOv8 for pediatric wrist fracture detection
- Our split GRAZPEDWRI-DX dataset can be downloaded [here](https://1drv.ms/u/s!Ap6uuRvdVcJWbXtfIFYUvzOMKXQ)
- Perform as Computer-assisted diagnosis (CAD) tools
</div>
</div>

- ``Electronics Letters'24`` [YOLOv9 for Fracture Detection in Pediatric Wrist Trauma X-ray Images](https://arxiv.org/pdf/2403.11249), Chun-Tse Chien, **Rui-Yang Ju**, Kuang-Yi Chou, et al., Electronics Letters, 2024

## Layer & Block Connection Strategy
- ``MTA'23`` [Resolution Enhancement Processing on Low Quality Images Using Swin Transformer Based on Interval Dense Connection Strategy](https://arxiv.org/pdf/2303.09190), **Rui-Yang Ju**, Chih-Chia Chen, Jen-Shiun Chiang, et al., Multimedia Tools and Applications, 2023
- ``JRTIP'23`` [Efficient Convolutional Neural Networks on Raspberry Pi for Image Classification](https://arxiv.org/pdf/2204.00943), **Rui-Yang Ju**, Ting-Yu Lin, Jia-Hao Jian, et al., Journal of Real-Time Image Processing, 2023
- ``IEEE Access'22`` [ThreshNet: An Efficient DenseNet Using Threshold Mechanism to Reduce Connections](https://arxiv.org/pdf/2201.03013), **Rui-Yang Ju**, Ting-Yu Lin, Jia-Hao Jian, et al., IEEE Access, 2022

# Publications
123

# Professional Services
123

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
