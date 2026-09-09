---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
.paper-box {
  border-bottom: none !important;
}
</style>

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

I am currently pursuing a Ph.D. degree (JST DoGS SPRING Fellowship) at the [Graduate School of Informatics](https://www.i.kyoto-u.ac.jp/), [Kyoto University](https://www.kyoto-u.ac.jp/), Japan. 
I am a member of the [LSTA Lab.](https://www.lsta.media.kyoto-u.ac.jp/), where my current research focuses on the processing and analysis of Japanese historical document images, particularly Kuzushiji character recognition (Kuzushiji OCR).
If you are interested in any form of academic collaboration, please feel free to [email](mailto:jryjry1094791442@gmail.com) me.

I received my Master of Science (M.S.) degree in 2025 from the [Graduate Institute of Networking and Multimedia](https://www.inm.ntu.edu.tw/), [National Taiwan University](https://www.ntu.edu.tw/), Taipei, Taiwan.
I was a member of [NTU imLab](https://ntuimlab.tw/), and my master’s thesis focused on 3D Gaussian Splatting (3DGS) and 3D head reconstruction.

I obtained my Bachelor of Science (B.S.) degree in 2023 in [Electrical and Computer Engineering](http://www.ee.tku.edu.tw/) from [Tamkang University](https://www.tku.edu.tw/), New Taipei City, Taiwan, where I graduated first in my department (1/68). 
I conducted my undergraduate research at the Advanced Mixed-Operation System Laboratory (AMOS Lab.) at Tamkang University, focusing on object detection, document image binarization, and image super-resolution.

My primary research interests include Multimodal Learning (Vision-Language Models), Computer Vision (Optical Character Recognition, Object Detection, Document Understanding), Image Processing (Document Image Enhancement and Binarization, Image Super-Resolution), Natural Language Processing (Large Language Models), and Computer Graphics (3D Gaussian Reconstruction and Blendshapes).
I have published numerous papers in international journals and conferences <a href='https://scholar.google.com/citations?user=r8F35p8AAAAJ'><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fruiyangju%2Fruiyangju.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=Citations"></a>.

# News
<span class="anchor" id="News"></span>
- 2025.11: I am the recipient of the <a href="https://www.kugd.k.kyoto-u.ac.jp/en/support/recruitlist" target="_blank">Kyoto University DoGS SPRING Fellowship</a>. Thanks Kyoto University.
- 2025.06: I receive an offer for a PhD student at Kyoto University, Kyoto, Japan.

# Publications
<span class="anchor" id="Publications"></span>
## 🔥🔥🔥 Japanese Historical Document Processing
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img  src='https://ruiyangju.github.io/images/Figure/Seal-Robust-KCR.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Seal-Robust KCR: A Robust Kuzushiji Character Recognition Framework under Seal Interference](https://arxiv.org/abs/2602.19086) \\
**Rui-Yang Ju**, Kohei Yamashita, Hirotaka Kameko, Shinsuke Mori \\
[![](https://img.shields.io/badge/Project-white?logo=googlechrome&logoColor=black&labelColor=white&color=white)](https://ruiyangju.github.io/Seal-Robust-KCR)
[![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/Seal-Robust-KCR)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJDAR 2026</div><img  src='https://ruiyangju.github.io/images/Figure/DKDS.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[DKDS: A Benchmark Dataset of Degraded Kuzushiji Documents with Seals for Detection and Binarization](https://arxiv.org/abs/2511.09117) \\
**Rui-Yang Ju**, Kohei Yamashita, Hirotaka Kameko, Shinsuke Mori \\
[![](https://img.shields.io/badge/Project-white?logo=googlechrome&logoColor=black&labelColor=white&color=white)](https://ruiyangju.github.io/DKDS)
[![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/DKDS)
</div>
</div>

<hr style="margin-top: 20px; margin-bottom: 20px;">

## 🔥🔥🔥 Degraded Document Image Binarization
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Knowledge-Based Systems 2024</div><img  src='https://ruiyangju.github.io/images/Figure/document-binarization.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Three-stage Binarization of Color Document Images Based on Discrete Wavelet Transform and Generative Adversarial Networks](https://doi.org/10.1016/j.knosys.2024.112542) \\
**Rui-Yang Ju**, Yu-Shian Lin, Yanlin Jin, Chih-Chia Chen, Chun-Tse Chien, Jen-Shiun Chiang \\
[![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/abcpp12383/ThreeStageBinarization)
</div>
</div>

<div class="paper-box-related" markdown="1">
- ``Under Review`` [MFE-GAN: Efficient GAN-based Framework for Document Image Enhancement and Binarization with Multi-scale Feature Extraction](https://arxiv.org/abs/2512.14114), **Rui-Yang Ju**, KokSheik Wong, Yanlin Jin, Jen-Shiun Chiang. [![](https://img.shields.io/badge/Project-white?logo=googlechrome&logoColor=black&labelColor=white&color=white)](https://ruiyangju.github.io/MFE-GAN) [![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/Efficient_Document_Image_Binarization)
- ``APSIPA ASC 2025`` [Efficient Generative Adversarial Networks for Color Document Image Enhancement and Binarization Using Multi-scale Feature Extraction](https://ieeexplore.ieee.org/document/11249173), **Rui-Yang Ju**, KokSheik Wong, Jen-Shiun Chiang. [![](https://img.shields.io/badge/Project-white?logo=googlechrome&logoColor=black&labelColor=white&color=white)](https://ruiyangju.github.io/MFE-GAN) [![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/Efficient_Document_Image_Binarization)
- ``PRICAI 2023`` [CCDWT-GAN: Generative Adversarial Networks Based on Color Channel Using Discrete Wavelet Transform for Document Image Binarization](https://doi.org/10.1007/978-981-99-7019-3_19), **Rui-Yang Ju**, Yu-Shian Lin, Jen-Shiun Chiang, Chih-Chia Chen, Wei-Han Chen, Chun-Tse Chien. 
</div>

<hr style="margin-top: 20px; margin-bottom: 20px;">

## 🔥🔥 Subtitle Recognition and Translation for Short Dramas
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICASSP 2026</div><img  src='https://ruiyangju.github.io/images/Figure/CN-JP-translation.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[An End-to-End Multimodal System for Subtitle Recognition and Chinese-Japanese Translation in Short Dramas](https://doi.org/10.1109/ICASSP55912.2026.11464228) \\
Jing An, Haofei Chang, **Rui-Yang Ju**, Jinhua Su, Yanbing Bai, Xin Qu
</div>
</div>

<hr style="margin-top: 20px; margin-bottom: 20px;">

## 🔥🔥 3D Gaussian Head Avatar Creation
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE VR 2026 Poster</div><img  src='https://ruiyangju.github.io/images/Figure/ToonifyGB.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[ToonifyGB: StyleGAN-based Gaussian Blendshapes for 3D Stylized Head Avatars](https://doi.org/10.1109/VRW70859.2026.00201) \\
**Rui-Yang Ju**, Sheng-Yen Huang, Yi-Ping Hung \\
[![](https://img.shields.io/badge/Project-white?logo=googlechrome&logoColor=black&labelColor=white&color=white)](https://ruiyangju.github.io/ToonifyGB)
[![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/ToonifyGB)
</div>
</div>

<div class="paper-box-related" markdown="1">
- ``IEEE VR 2026 Poster`` [GlassesGB: Controllable 2D GAN-Based Eyewear Personalization for 3D Gaussian Blendshapes Head Avatars](https://doi.org/10.1109/VRW70859.2026.00215), **Rui-Yang Ju**, Jen-Shiun Chiang. [![](https://img.shields.io/badge/Project-white?logo=googlechrome&logoColor=black&labelColor=white&color=white)](https://ruiyangju.github.io/GlassesGB)
</div>

<hr style="margin-top: 20px; margin-bottom: 20px;">

## 🔥🔥 Pediatric Wrist Fracture Detection
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Scientific Reports 2023</div><img src='https://ruiyangju.github.io/images/Figure/fracture-detection.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Fracture Detection in Pediatric Wrist Trauma X-ray Images Using YOLOv8 Algorithm](https://doi.org/10.1038/s41598-023-47460-7) \\
**Rui-Yang Ju**, Weiming Cai \\
[![](https://img.shields.io/badge/Project-white?logo=googlechrome&logoColor=black&labelColor=white&color=white)](https://ruiyangju.github.io/GRAZPEDWRI-DX_JU)
[![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/Bone_Fracture_Detection_YOLOv8)
</div>
</div>

<div class="paper-box-related" markdown="1">
- ``IET Image Processing 2025`` [Pediatric Wrist Fracture Detection Using Feature Context Excitation Modules in X-ray Images](https://doi.org/10.1049/ipr2.70269), **Rui-Yang Ju**, Chun-Tse Chien, Enkaer Xieerke, Jen-Shiun Chiang. [![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/FCE-YOLOv8)
- ``IEEE Access 2025`` [YOLOv8-AM: YOLOv8 Based on Effective Attention Mechanisms for Pediatric Wrist Fracture Detection](https://ieeexplore.ieee.org/document/10918980), Chun-Tse Chien, **Rui-Yang Ju**, Kuang-Yi Chou, Enkaer Xieerke, Jen-Shiun Chiang. [![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/Fracture_Detection_Improved_YOLOv8)
- ``Electronics Letters 2024`` [YOLOv9 for Fracture Detection in Pediatric Wrist Trauma X-ray Images](http://dx.doi.org/10.1049/ell2.13248), Chun-Tse Chien, **Rui-Yang Ju**, Kuang-Yi Chou, Jen-Shiun Chiang. [![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/YOLOv9-Fracture-Detection)
- ``ICONIP 2024`` [YOLOv8-ResCBAM: YOLOv8 Based on An Effective Attention Module for Pediatric Wrist Fracture Detection](https://doi.org/10.1007/978-981-96-6972-1_28), **Rui-Yang Ju**, Chun-Tse Chien, Jen-Shiun Chiang. [![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/Fracture_Detection_Improved_YOLOv8)
</div>

<hr style="margin-top: 20px; margin-bottom: 20px;">

## 🔥 Other
<div class="paper-box-related" markdown="1">
  
- ``J-STARS 2026`` [Two-Stage Framework for Efficient UAV-Based Wildfire Video Analysis with Adaptive Compression and Fire Source Detection](https://doi.org/10.1109/JSTARS.2026.3685660), Yanbing Bai, **Rui-Yang Ju**, Lemeng Zhao, Junjie Hu, Jianchao Bi, Erick Mas, Shunichi Koshimura.

- ``ADMA  2025`` [From Roads to Lights: Satellite Evidence on Smart City Planning](https://doi.org/10.1007/978-981-95-3459-3_24), Yang Yang, Tianzhi Wu, Lize Zheng, **Rui-Yang Ju**, Yanbing Bai.

- ``ICRA 2025`` [ORB-SfMLearner: ORB-Guided Self-supervised Visual Odometry with Selective Online Adaptation](https://doi.org/10.1109/ICRA55743.2025.11127848), Yanlin Jin, **Rui-Yang Ju**, Haojun Liu, Yuzhong Zhong. [![](https://img.shields.io/badge/Project-white?logo=googlechrome&logoColor=black&labelColor=white&color=white)](https://www.neiljin.site/projects/orbsfm) [![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/PeaceNeil/ORB-SfMLearner)

- ``MTA 2023`` [Resolution enhancement processing on low quality images using swin transformer based on interval dense connection strategy](https://doi.org/10.1007/s11042-023-16088-0), **Rui-Yang Ju**, Chih-Chia Chen, Jen-Shiun Chiang, Yu-Shian Lin, Wei-Han Chen, Chun-Tse Chien. [![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/Rubbbbbbbbby/SwinOIR)

- ``JRTIP 2023`` [Efficient Convolutional Neural Networks on Raspberry Pi for Image Classification](https://doi.org/10.1007/s11554-023-01271-1), **Rui-Yang Ju**, Ting-Yu Lin, Jia-Hao Jian, Jen-Shiun Chiang. [![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/TripleNet)

- ``IEEE Access 2022`` [ThreshNet: An Efficient DenseNet Using Threshold Mechanism to Reduce Connections](https://doi.org/10.1109/ACCESS.2022.3196492), **Rui-Yang Ju**, Ting-Yu Lin, Jia-Hao Jian, Jen-Shiun Chiang, Wei-Bin Yang. [![](https://img.shields.io/badge/GitHub-white?logo=github&logoColor=black&labelColor=white&color=white)](https://github.com/RuiyangJu/ThreshNet)

</div>

# Awards
<span class='anchor' id='Awards'></span>

- Japan Science and Technology Agency (JST), DoGS SPRING Fellowship, Oct. 2025.
- National Taiwan University, Graduate Research Assistantship, Feb. 2024.
- National Taiwan University, Postgraduate Scholarship, Jan. 2024; Jul. 2024; Jan. 2025.
- Sino International Business Innovation Association (SIBIA), Gratitude and Heritage Scholarship, Mar. 2021; Mar. 2022; May 2024.
- Tamkang University, Undergraduate Research Fellowship, Aug. 2021.
- Tamkang University, Excellent Academic Performance Award (Top 1% Ranking), May 2021; Dec. 2022.

# Services
<span class="anchor" id="Services"></span>

I currently serve as a reviewer for several international journals and conferences. 
A detailed record of my reviewing activities is available on my ORCID profile <a href="https://orcid.org/0000-0003-2240-1377"><img src="https://img.shields.io/endpoint?url=https://cdn.jsdelivr.net/gh/ruiyangju/ruiyangju.github.io@main/orcid_peer_review_shieldsio.json&logo=ORCID&labelColor=f6f6f6&color=9cf&style=flat&label=Peer%20Reviews"></a>.

### Selected Journal Review Service
- IEEE Transactions on Visualization and Computer Graphics (TVCG), Pattern Recognition (PR), Knowledge-Based Systems (KBS), Neural Networks (NN), Neurocomputing, IEEE Signal Processing Letters, and Engineering Applications of Artificial Intelligence (EAAI).

### Conference Committee and Review Service
- AAAI 2027, IJCNN 2027, PRIMA 2026, PRICAI 2026, SMC 2026, CHI 2026, IJCNN 2026, ICASSP 2026, AAAI 2026, PRICAI 2025, IJCNN 2025, ICASSP 2025, PRICAI 2024, PRICAI 2023.

<hr style="margin-top: 40px; margin-bottom: 20px;">
<div style="text-align: center; font-size: 13px; color: #888; line-height: 1.8;">
  © Copyright 2026 RuiYang Ju.  
</div>
