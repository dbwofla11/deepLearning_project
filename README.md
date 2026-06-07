# Residual Prediction based NAFNet for Image Restoration

## Motivation

기존 이미지 복원 모델은 일반적으로 오염된 이미지를 입력받아 복원된 이미지를 직접 예측한다.

```text
Input Image
    ↓
 Network
    ↓
Restored Image
```

하지만 복원 문제의 본질은 "깨끗한 이미지를 생성하는 것"이 아니라 "오염된 부분을 제거하는 것"에 가깝다.

이에 따라 다음과 같은 의문에서 본 연구를 시작하였다.

> 복원 이미지를 직접 예측하는 대신 제거해야 할 오염 성분(Residual)만 예측하면 학습 문제가 더 단순해질 수 있지 않을까?

특히 Water, Mixed와 같은 이미지 복원 문제에서는 실제로 변경되어야 하는 영역이 전체 이미지 중 일부에 불과하므로, 오염 성분만을 학습하는 것이 더 효율적인 최적화를 가능하게 할 것이라는 가설을 세웠다.

---

## Baseline: Direct Restoration

기존 NAFNet은 복원 이미지를 직접 예측하는 방식으로 동작한다.

```text
Input Image
    ↓
   NAFNet
    ↓
Restored Image
```

학습 시 모델 출력과 Ground Truth 간의 오차를 최소화한다.

```python
Loss(pred, gt)
```

또한 NAFNet은 마지막 단계에서 Global Residual Connection을 사용한다.

```python
x = self.ending(x)
x = x + inp
```

즉 입력 이미지에 대한 보정값을 학습하는 구조를 가진다.

---

## Proposed Method: Residual Prediction

본 실험에서는 최종 Global Residual Connection을 제거하고 모델이 오염 성분 자체를 예측하도록 변경하였다.

```python
x = self.ending(x)
return x
```

Residual Target은 다음과 같이 정의하였다.

```python
target_residual = lq - gt
```

즉 모델은 복원 이미지를 생성하는 대신 제거해야 할 오염 성분을 직접 예측한다.

```text
Input Image
    ↓
   NAFNet
    ↓
Predicted Residual
```

추론 시에는 예측된 Residual을 입력 이미지에서 제거하여 최종 복원 이미지를 생성한다.

```python
restored = input - predicted_residual
```

```text
Input Image
      -
Predicted Residual
      ↓
 Restored Image
```

---

## Research Question

본 실험은 단순한 성능 향상 실험이 아니라 다음 질문에 대한 검증을 목표로 한다.

1. Residual Prediction이 더 효율적인 학습 목표가 될 수 있는가?
2. Direct Restoration보다 더 빠르게 수렴할 수 있는가?
3. 동일한 모델 구조에서 성능 향상을 얻을 수 있는가?
4. 추가적인 계산 비용 없이 성능 개선이 가능한가?

---

## Benchmark Results

구조 자체는 변경하지 않았기 때문에 파라미터 수와 연산량은 동일하다.

| Model                      | Params(M) | FLOPs(G) | GMACs(G) | Latency(ms) |
| -------------------------- | --------: | -------: | -------: | ----------: |
| Baseline NAFNet            |    1.9696 |  18.5265 |   9.1703 |     17.6578 |
| Residual Prediction NAFNet |    1.9696 |  18.5265 |   9.1703 |     17.3561 |

### Observation

* Params 변화 없음
* FLOPs 변화 없음
* GMACs 변화 없음
* Latency 차이는 측정 오차 범위 수준

즉 Residual Prediction은 추가적인 계산 비용 없이 구현되었다.

---

## Validation Results

### Water Dataset

| Difficulty | Baseline PSNR | Residual PSNR |
| ---------- | ------------: | ------------: |
| Easy       |       27.2620 |       26.7445 |
| Medium     |       23.8838 |       23.7588 |
| Hard       |       19.7782 |       19.6677 |

Baseline이 전반적으로 더 높은 성능을 보였다.

---

### Mixed Dataset

| Difficulty | Baseline PSNR | Residual PSNR |
| ---------- | ------------: | ------------: |
| Easy       |       22.6261 |       22.7542 |
| Medium     |       23.9262 |       24.2283 |
| Hard       |       16.8692 |       16.9411 |

Residual Prediction 방식이 모든 난이도에서 더 높은 성능을 기록하였다.

---

## Training Analysis

초기 가설은 Residual Prediction이 더 단순한 학습 목표를 제공하여 학습 안정성과 수렴 속도를 향상시킬 것이라는 것이었다.

그러나 실제 학습 과정에서는 예상과 다른 현상이 관찰되었다.

### Baseline

* Train Loss 감소 추세가 비교적 명확
* Validation Curve가 상대적으로 안정적

### Residual Prediction

* Train Loss 변동성이 더 크게 관찰됨
* 특정 구간에서 Validation 성능 급등 및 급락 발생
* Mixed-Medium에서는 6000 iteration 부근에서 최고 성능을 기록한 후 빠르게 감소

이는 Residual Prediction이 항상 더 안정적인 최적화를 제공하는 것은 아님을 시사한다.

---

## Insights

본 실험을 통해 다음과 같은 인사이트를 얻을 수 있었다.

### 1. Residual Prediction은 공짜 성능 향상을 제공할 수 있다.

추가적인 파라미터나 연산량 증가 없이 일부 데이터셋에서 성능 향상을 달성하였다.

### 2. 데이터 특성에 따라 효과가 달라진다.

Water Dataset에서는 Baseline이 우세하였으나 Mixed Dataset에서는 Residual Prediction이 우세하였다.

이는 Residual Prediction이 복잡하고 다양한 오염 환경에서 더 효과적일 가능성을 시사한다.

### 3. 학습 문제를 단순화한다고 해서 최적화가 항상 쉬워지는 것은 아니다.

Residual Prediction은 제거해야 할 오염 성분 전체를 직접 예측해야 하므로 학습 과정에서 더 큰 변동성을 보일 수 있다.

### 4. 문제 정의 자체가 성능에 영향을 줄 수 있다.

본 실험은 모델 구조를 변경하지 않고 학습 목표만 변경하였다.

그럼에도 불구하고 성능 차이가 발생하였으며, 이는 이미지 복원 문제에서 네트워크 구조뿐 아니라 학습 목표의 정의 또한 중요한 요소임을 보여준다.

---

## Conclusion

본 연구에서는 NAFNet의 구조를 변경하지 않고 Direct Restoration을 Residual Prediction으로 재정의하였다.

실험 결과 Residual Prediction은 추가적인 계산 비용 없이 Mixed Dataset에서 일관된 성능 향상을 보였으며, 학습 목표의 변경만으로도 복원 성능에 영향을 줄 수 있음을 확인하였다.

반면 학습 안정성 측면에서는 예상했던 이점을 명확히 확인하지 못하였으며, 데이터 특성에 따라 성능 차이가 크게 나타남을 확인하였다.

향후에는 Test Set 및 Leaderboard 결과를 통해 일반화 성능을 추가적으로 검증할 예정이다.
