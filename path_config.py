from pathlib import Path
# =========================================================
# MODEL
# =========================================================

WIDTH = 16


# =========================================================
# TASK
# =========================================================

TASK = 'water'

DIFFICULTIES = [
    'easy',
    'medium',
    'hard'
]

# =========================================================
# ROOT
# =========================================================

EXPERIMENT_ROOT = Path(
    r'C:\DNN\deepLearning\NAFNet\experiments'
)

YML_ROOT = Path(
    r'C:\DNN\deepLearning\sidl_options\test'
)

# =========================================================
# MODEL PATH
# =========================================================

def get_experiment_dir(task, difficulty):

    return (
        EXPERIMENT_ROOT /
        f'NAFNet-{task}-{difficulty}-w{WIDTH}'
    )


def get_model_dir(task, difficulty):

    return (
        get_experiment_dir(task, difficulty) /
        'models'
    )