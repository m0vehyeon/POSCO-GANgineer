# POSCO-GANgineer

## Model

```
AnoGAN
f-AnoGAN
GANomaly
```

---

## Fine Tuning Hyper Parameter

### Dual Phase Steel

```
train dataset : Aug Ferrite Steel
learning G per D = 1
lr = 4e-1
```

---

### CFRP

```
train dataset : Origin Ferrite Steel
learning G per D = 5
lr = 3e-5
```

### Ti64

```
Train Dataset : Aug Ferrite Steel
learning G per D = 20
lr = 2e-1
```

---

## Fined Tuned Model's Accuracy

```
we define model accuracy as 'row error-rate compare with real fraction of the certain microstructure'.
```

---

### Dual Phase Steel

```
Mean error-rate overall test dataset: 1.48%
```

---

### CFRP

```
Mean error-rate overall test dataset: 3.24%
```

---

### Ti64

```
Mean error-rate overall test dataset: 10.37%
```

---