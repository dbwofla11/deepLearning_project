# deepLearning_project
딥러닝 기반 렌즈 노이즈 제거 실험

# 메모장 테스트 해볼리스트 
그리고 솔직히 지금 그래프 모양 보면

Water-Easy      -> 2000
Water-Medium    -> 12000
Water-Hard      -> 18000

Mixed-Easy      -> 5000
Mixed-Medium    -> 5000
Mixed-Hard      -> 14000

이 6개가 가장 유력한 제출 후보임. 20000은 혹시 모를 역전 확인용.


# 아키텍처 실험: Residual Learning 기반 NAFNet
실험 목적

기존 NAFNet은 손상 이미지를 입력받아 깨끗한 이미지를 직접 예측한다.

Input (Degraded)
      ↓
    NAFNet
      ↓
Output (Clean)

하지만 복원 문제에서는 전체 이미지를 생성하는 것보다 손상 성분(Residual)만 예측하는 방식이 효과적인 경우가 많다.

따라서 모델이 복원 이미지 대신 손상 성분만 학습하도록 변경하여 성능 변화를 확인한다.

Baseline

현재 구조

pred = model(lq)

loss = L1(pred, gt)
입력: 손상 이미지 (lq)
정답: 원본 이미지 (gt)
Residual Learning

Residual 정의

residual_gt = lq - gt

즉

Residual
=
손상 이미지
-
원본 이미지

학습 구조

Input (Degraded)
      ↓
    NAFNet
      ↓
Pred Residual

Loss

pred_residual = model(lq)

target_residual = lq - gt

loss = L1(
    pred_residual,
    target_residual
)
Inference

기존

output = model(lq)

Residual 방식

pred_residual = model(lq)

output = lq - pred_residual
기대 효과

모델이

이미지 전체

를 복원하는 대신

손상된 부분

만 학습하게 됨.

따라서

학습 목표 단순화
노이즈 제거 효율 향상
수렴 속도 향상

등을 기대할 수 있음.

예상 결과 해석
Case 1

PSNR 상승

Residual > Baseline

해석

손상 성분만 학습하도록 변경함으로써 복원 성능이 향상되었다.

Case 2

PSNR 유사

Residual ≈ Baseline

해석

Residual Prediction 역시 복원 문제에 효과적으로 적용 가능함을 확인하였다.

Case 3

PSNR 하락

Residual < Baseline

해석

Water Degradation은 단순 가산성 노이즈가 아닌 구조적 왜곡 특성이 강하여 Residual Learning의 효과가 제한적이었다.

구현 위치

NAFNet(BasicSR)

수정 파일

basicsr/models/image_restoration_model.py

수정 함수

optimize_parameters()

test()
실험 비교표
Model	Params	PSNR	SSIM
Baseline NAFNet	-	?	?
Residual NAFNet	동일	?	?
실험 의의

성능 향상 여부와 관계없이

Direct Reconstruction
Residual Reconstruction

두 접근법을 비교할 수 있으며,

Water 복원 문제에서 Residual Learning의 적용 가능성과 한계를 분석할 수 있다.