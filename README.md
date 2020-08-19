# POSCO-GANgineer
- POSCO AI/BigData 청년 아카데미 10기 B4조 AI 프로젝트
- GAN 기반 anomaly detection 기술을 활용해 미세조직의 특성(마르텐사이트 분율/ 기공 분산도/ 티타늄 상대밀도)를 측정하는 프로그램


## Demonstration Video


## Getting Started

### Prerequisites
- torch
- torchvision
- os
- numpy
- matplotlib

### Prepare Dataset

### Installing
- git clone https://github.com/ehdgus6876/POSCO-GANgineer.git

## Running with Pretrained
- open Final/source/model/[model_name]/[model_name].ipynb
- run after "모델 저장 및 읽기"

### Networks
#### why GAN based anomaly detection?
- GANgineer의 최종목표는 미세조직 특성 파악을 통한 신소재 연구개발 기간의 축소입니다.
- 현재 미세조직 특성 파악을 위한 딥러닝 접근은 대부분이 FCN이 활용되고 있습니다.
- 하지만 CNN기반의 모델을 활용하기 위해서는 많은 양의 데이터셋과 라벨링이 요구됩니다.
- 우리는 실험 환경에 맞춰 간단히 구할 수 있는 정상 이미지들 만으로 이상치를 추출하는 GAN based anomaly detection 모델을 활용하기로 했습니다. 

#### Unsupervised Learning Model
- AnoGAN
- fAnoGAN
#### Semi-Supervised Learning Model
- GANomaly
https://github.com/YeongHyeon/GANomaly-PyTorch/raw/master/figures/ganomaly.png

## Training with Custom Dataset

## References
[1] T Schlegl, et al. (2017). AnoGAN: Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide Marker Discovery.. arXiv:1703.05921.
[2] T Schlegl, et al. (2019). f-AnoGAN: Fast unsupervised anomaly detection with generative adversarial networks.. dio:10.1016.
[3] S Akcay, et al. (2018). GANomaly: Semi-supervised anomaly detection via adversarial training.. arXiv preprint arXiv:1805.06725.
