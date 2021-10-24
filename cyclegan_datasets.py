"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
    'summer2winter_yosemite_train': 1231,
    'summer2winter_yosemite_test': 309,
    'NIR2VIS_train': 3310,
    'DAT2SYSU_F1_train': 3310,
    'NIR2VIS_test': 810,
    'VIS2NIR_F5_train': 3310,
    'VIS2NIR_F5_test': 810,
    'SYSU_F1_train': 7724,
    'SYSU_F1_test': 7771,
    'SYSU_F2_train': 7771,
    'SYSU_F2_test': 7724,
    'VIS2NIR_ALL_TRAIN': 4120,
    'VIS2NIR_ALL_TEST': 7771,
    'SYSU_REVISED_F1_train': 7724,
    'SYSU_REVISED_F1_test': 7771,
    'SYSU_train': 9819,
    'SYSU_val': 1949

}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
    'summer2winter_yosemite_train': '.jpg',
    'summer2winter_yosemite_test': '.jpg',
    'NIR2VIS_train': '.jpg',
    'DAT2SYSU_F1_train': '.jpg',
    'NIR2VIS_test': '.jpg',
    'VIS2NIR_F5_train': '.jpg',
    'VIS2NIR_F5_test': '.jpg',
    'SYSU_F1_train': '.jpg',
    'SYSU_F1_test': '.jpg',
    'SYSU_F2_train': '.jpg',
    'SYSU_F2_test': '.jpg',
    'VIS2NIR_ALL_TRAIN': '.jpg',
    'VIS2NIR_ALL_TEST': '.jpg',
    'SYSU_REVISED_F1_train': '.jpg',
    'SYSU_REVISED_F1_test': '.jpg',
    'SYSU_train': '.jpg',
    'SYSU_val': '.jpg'
}

"""The path to the output csv file."""
PATH_TO_CSV = {
    'summer2winter_yosemite_train': './input/summer2winter_yosemite/summer2winter_yosemite_train.csv',
    'summer2winter_yosemite_test': './input/summer2winter_yosemite/summer2winter_yosemite_test.csv',
    'NIR2VIS_train': './input/NIR2VIS/NIR2VIS_train.csv',
    'DAT2SYSU_F1_train': './input/Dat2SYSU_F1/DAT2SYSU_F1_train.csv',
    'NIR2VIS_test': './input/NIR2VIS/NIR2VIS_test.csv',
    'VIS2NIR_F5_train': './input/VIS2NIR_F5/VIS2NIR_F5_train.csv',
    'VIS2NIR_F5_test': './input/VIS2NIR_F5/VIS2NIR_F5_test.csv',
    'SYSU_F1_train': './input/SYSU_F1/SYSU_F1_train.csv',
    'SYSU_F1_test': './input/SYSU_F1/SYSU_F1_test.csv',
    'SYSU_F2_train': './input/SYSU_F2/SYSU_F2_train.csv',
    'SYSU_F2_test': './input/SYSU_F2/SYSU_F2_test.csv',
    'VIS2NIR_ALL_TRAIN': './input/VIS2NIR_ALL/VIS2NIR_ALL_TRAIN.csv',
    'VIS2NIR_ALL_TEST': './input/VIS2NIR_ALL/VIS2NIR_ALL_TEST.csv',
    'SYSU_REVISED_F1_train': './input/SYSU_REVISED_F1/SYSU_REVISED_F1_train.csv',
    'SYSU_REVISED_F1_test': './input/SYSU_REVISED_F1/SYSU_REVISED_F1_test.csv',
    'SYSU_train': './input/SYSU/SYSU_train.csv',
    'SYSU_val': './input/SYSU/SYSU_val.csv'

}
