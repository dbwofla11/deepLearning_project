from pathlib import Path

from dataset_config import (
    get_valid_root
)

# =========================================================
# TEST YML
# =========================================================

def build_test_yml(
    task,
    difficulty,
    ckpt_path,
    width=16
):

    valid_root = get_valid_root(task)

    valid_gt = (
        valid_root /
        difficulty /
        'target'
    ).as_posix()

    valid_lq = (
        valid_root /
        difficulty /
        'input'
    ).as_posix()

    ckpt_name = Path(ckpt_path).stem

    return f"""
path:
  root: C:/DNN/deepLearning/NAFNet

  pretrain_network_g: {ckpt_path}

  strict_load_g: true

name: TEST-{task}-{difficulty}-{ckpt_name}

model_type: ImageRestorationModel

scale: 1
num_gpu: 1

datasets:

  test:
    name: sidl-{task}-{difficulty}-test

    type: PairedImageDataset

    dataroot_gt: {valid_gt}

    dataroot_lq: {valid_lq}

    io_backend:
      type: disk

network_g:
  type: NAFNetLocal

  width: {width}

  enc_blk_nums: [1, 1, 1, 8]

  middle_blk_num: 1

  dec_blk_nums: [1, 1, 1, 1]

val:

  save_img: true

  metrics:

    psnr:
      type: calculate_psnr
      crop_border: 0
      test_y_channel: false

    ssim:
      type: calculate_ssim
      crop_border: 0
      test_y_channel: false
"""