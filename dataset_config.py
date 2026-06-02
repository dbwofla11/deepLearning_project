from pathlib import Path

# =========================================================
# Train Dataset Paths
# =========================================================

TRAIN_ROOTS = {
    "dust": Path(
        r"G:\.shortcut-targets-by-id\1m0K_qS3tHhvbNzWSoCD29_tWj31WpbZk\dust"
    ),

    "finger": Path(
        r"G:\.shortcut-targets-by-id\1y03rtui6h1LD8SRDg0Vo9Tz_ASCNehnp\finger"
    ),

    "scratch": Path(
        r"G:\.shortcut-targets-by-id\19ozuLRNk-PdJTknrJR58Bq_aWyLatEEH\scratch"
    ),

    "water": Path(
        r"G:\.shortcut-targets-by-id\1EEFsAOy22ywrq7X8hbG_yng8rxLpRcoh\water"
    ),

    "mixed": Path(
        r"G:\.shortcut-targets-by-id\1rmr4AHuOKBYVcTFWdTOrfmNqHNMQRXzT\mixed"
    )
}


# =========================================================
# Validation Dataset Paths
# =========================================================

VALID_ROOTS = {
    "dust": Path(
        r"G:\.shortcut-targets-by-id\1Qj7pFgGOGDo5oSRr4v7-H6Ui2jUMrpg3\dust"
    ),

    "finger": Path(
        r"G:\.shortcut-targets-by-id\1PQ6cYxt1UbNuYSFXo0MZmeVFiptKLPNn\finger"
    ),

    "mixed": Path(
        r"G:\.shortcut-targets-by-id\15heQpPoDquJ_skh0A0Sw0H7XTqAVciCY\mixed"
    ),

    "scratch": Path(
        r"G:\.shortcut-targets-by-id\1lzZPHko2q1I5Ory_mF1AygiZk2D4XxQb\scratch"
    ),

    "water": Path(
        r"G:\.shortcut-targets-by-id\1BsFgeHgPmT1UOKl78ikwUNLB7YjXVRpF\water"
    )
}


# =========================================================
# Test Dataset Paths
# =========================================================

TEST_ROOTS = {
    "dust": Path(
        r"G:\.shortcut-targets-by-id\1Dm3ejpjEbAU-X5tpel5OrgzojpeNRaIA\dust"
    ),

    "finger": Path(
        r"G:\.shortcut-targets-by-id\1BBtDIX64_7qLi-Ua46xOpD-RY1p4Ginm\finger"
    ),

    "mixed": Path(
        r"G:\.shortcut-targets-by-id\16M_VTZyM-1-mp0UmdTs2kbK0_ro4GkE9\mixed"
    ),

    "scratch": Path(
        r"G:\.shortcut-targets-by-id\19aT9ee2LhOUE8wI7CNxE9Fr765YSETmy\scratch"
    ),

    "water": Path(
        r"G:\.shortcut-targets-by-id\1oZXf6Nq0R5ucEyqzpSvQVwI1wMO5xmAj\water"
    )
}


# =========================================================
# Difficulty Levels
# =========================================================

DIFFICULTIES = [
    "easy",
    "medium",
    "hard"
]


# =========================================================
# Utility Functions
# =========================================================

def get_train_root(noise_type: str) -> Path:
    return TRAIN_ROOTS[noise_type]


def get_valid_root(noise_type: str) -> Path:
    return VALID_ROOTS[noise_type]


def get_test_root(noise_type: str) -> Path:
    return TEST_ROOTS[noise_type]