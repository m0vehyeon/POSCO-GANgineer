# Anogan정리

## DualPhaseSteel

- 분율

  ```python
  diff_cnts = np.array(diff_cnts)
  
  diff_fraction = diff_cnts / img_size ** 2
  
  print(diff_fraction)
  ```

  

## Ti64

- 상대밀도

  ```python
  Ti64_density = 4.43
  
  Ti64_rel_densitys = np.array([])
  
  Ti64_rel_densitys = diff_fraction * Ti64_density
  
  print(Ti64_rel_densitys)
  ```



### Aug vs Origin

| File_name           | Aug                                                          | Origin                                                       | 참고                                      |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | :---------------------------------------- |
| angoan_gen_Ti64_aug | [0.36206055 0.20947266 0.24902344 0.18603516 0.21948242 0.06616211  0.04785156 0.09692383 0.1237793  0.70336914] | [0.36254883 0.2097168  0.2512207  0.1875     0.21972656 0.06640625  0.0480957  0.09960938 0.12451172 0.7019043 ] | 사진상 빨간색 부분은 Aug데이터가 더 많음. |
|                     |                                                              |                                                              |                                           |





## CFRP

- 분산

  ```python
  from scipy import stats
  from extended_int import int_inf
  
  corr_coeffis = []
  corr_p_vals = []
  
  def cal_corr_coeffis():
      for idx in range(len(test_data_loader)):
          x_points = diff_points[idx][0]
          y_points = diff_points[idx][1]
          
          
          if len(x_points) > 0:
              corr_coeffi, corr_p_val = stats.pearsonr(x_points, y_points)
          else:
              corr_coeffi, corr_p_val = -int_inf, -int_inf
          
          corr_coeffis.append(corr_coeffi)
          corr_p_vals.append(corr_p_val)
  ```

  ```python
  cal_corr_coeffis()
  
  print(corr_coeffis)
  ```

  

  ### CFRP - Aug vs Origin

  | File_name | Aug  | Origin | 참고 |
  | --------- | ---- | ------ | ---- |
  |           |      |        |      |

  



### 참고

# AnoGAN
- 2020.08.11 : Genrator 학습 수 ... 4

# 개발일지
- 2020.08.14 : 분율 추출 구현
- 2020.08.15 : 이상치 상관계수 추출 구현 / 모델 save, load 구현
- 2020.08.16 : anomaly detect 이미지 저장 구현 / 티티늄(Ti64) 상대 밀도 계산 구현





### !!!

#### parameter
- 2020.08.16
> latent_size = 100  
> workers = 4 
> img_size = 64  
> channel = 1  
> epochs = 100  
> batch_size = 64  
> **learning_rate = 2e-1  
> learning_G_per_D = 1**

