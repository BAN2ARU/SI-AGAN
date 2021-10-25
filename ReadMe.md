# SI-AGAN

Attention-guided gan for synthesizing IR images

This repository contains the Tensorflow code for "[Pedestrian Gender Recognition by Style Transfer of Visible-Light Image to Infrared-Light Image Based on an Attention-Guided Generative Adversarial Network](https://www.mdpi.com/2227-7390/9/20/2535)". This code is based on the TensorFlow implementation of AGGAN provide by [AlamiMejjati](https://github.com/AlamiMejjati/Unsupervised-Attention-guided-Image-to-Image-Translation).

I am working on updating to Tensorflow 2.0, and when it is updated, I will add a link to the new repository.

### Dataset

1. [ReGDB Database](https://github.com/bismex/HiCMD)
2. [SYSU-MM01 Database](https://github.com/wuancong/SYSU-MM01)

 

### Training

1. revise .json file in configs folder
2. make .csv file using create_cyclegan_dataaset.py
3. start training
    
`python main.py --to_train=1 --log_dir=./output/##/## --config_filename=./configs/##.json`
    

Also, you can check the tensorbaord

`tensorboard --port=#### --logdir=./output/##/##/#timestamp#`

### Testing

`python main.py --to_train=0 --log_dir=./output/##/## --config_filename=./configs/##.json --checkpoint_dir=./output/##/##/#timestamp#`
