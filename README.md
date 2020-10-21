# GANgineer

포스코 청년 AI/Big Data 아카데미 10기 AI 프로젝트

---

## Demonstration Video



---

## Getting Started

### Prerequisites

```
torch
torchvision
os
numpy
matplotlib
```

### Prepare Dataset

```
please Contact us via Google Drive link.
```

#### Google Drive link

https://drive.google.com/drive/folders/14IapfDIzIbPIXa1ynzSLbD96BaogyReP?usp=sharing


### Installing

```
https://github.com/POSCO-B4/GANgineer.git
```

### Running with Pretrained

```
open "sorce/model/{dataset_name}/{model_name_*}.ipynb"

dataset_name == [DualPhaseSteel | CFRP | Ti64]
model_name == [fanogan_* | ganomaly_*]
```

```
run after "모델 저장 및 읽기"
```

---

## Networks

### why GAN based anomaly detection?

```
GANgineer의 최종목표는 미세조직 특성 파악을 통한 신소재 연구개발 기간의 축소입니다.

현재 딥러닝을 활용한 미세조직 특성파악은 대부분이 FCN(Fully Connected Network)를 사용하고 있습니다.
... 이런 CNN기반의 모델은 많은 양의 데이터셋과 라벨링을 요구함에 프로젝트의 진행방향과 맞지 않았습니다.
... 최근 1~2년 내 GAN을 활용한 신소재 연구개발이 활발해짐에 따라 GAN based anomaly detection을 활용해 보았습니다.

수행 결과.
... 공정과 같이 결과물의 형태가 일정한 환경에서 기대값의 오차범위를 벗어나는 불량을 찾는데 특히 효과적인 모델임을 확인했습니다.
... 신소재의 경우, 일반적인 철(DualPhaseSteel), 탄소 소재(CFRP)의 특성 예측에 효과적임을 확인했습니다.
... 티타늄 소재(Ti64)의 경우 미세조직의 3D 구조를 학습하여 단면의 분율보다 높은 분율을 추출했습니다.
... 즉 3D 구조의 미세조직에 있어서는 또다른 Anomaly GAN 모델을 탐색할 필요가 있었습니다.
```

### Unsupervised Learning Model

![AnoGAN](https://github.com/yjucho1/anoGAN)

![fAnoGAN](https://github.com/tSchlegl/f-AnoGAN)

### Semi-Supervised Learning Model

![GANomaly](https://github.com/YeongHyeon/GANomaly)

---

## Training with Custom Dataset

```
crawl at least 50 SEM images for each of your dataset and set datapath. 
```

---

## References

```
[1] T Schlegl, et al. (2017). AnoGAN: Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide Marker Discovery.. arXiv:1703.05921.
[2] T Schlegl, et al. (2019). f-AnoGAN: Fast unsupervised anomaly detection with generative adversarial networks.. dio:10.1016.
[3] S Akcay, et al. (2018). GANomaly: Semi-supervised anomaly detection via adversarial training.. arXiv preprint arXiv:1805.06725.
```