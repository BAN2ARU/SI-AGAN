import tensorflow as tf

import cyclegan_datasets
import model


def _load_samples(csv_name, image_type):

    # filename_queue = tf.train.string_input_producer([csv_name], shuffle=False, num_epochs=1)
    filename_queue = tf.train.string_input_producer([csv_name], shuffle=False)

    reader = tf.TextLineReader()
    _, csv_filename = reader.read(filename_queue)

    record_defaults = [tf.constant([], dtype=tf.string),
                       tf.constant([], dtype=tf.string)]

    filename_i, filename_j = tf.decode_csv(
        csv_filename, record_defaults=record_defaults)

    file_contents_i = tf.read_file(filename_i)
    file_contents_j = tf.read_file(filename_j)

    if image_type == '.jpg':
        image_decoded_A = tf.image.decode_jpeg(
            file_contents_i, channels=model.IMG_CHANNELS)
        image_decoded_B = tf.image.decode_jpeg(
            file_contents_j, channels=model.IMG_CHANNELS)
    elif image_type == '.png':
        image_decoded_A = tf.image.decode_png(
            file_contents_i, channels=model.IMG_CHANNELS, dtype=tf.uint8)
        image_decoded_B = tf.image.decode_png(
            file_contents_j, channels=model.IMG_CHANNELS, dtype=tf.uint8)

    return image_decoded_A, image_decoded_B, filename_i, filename_j


def load_data(dataset_name, h, w,
              do_shuffle, do_flipping):
    """

    :param dataset_name: The name of the dataset.
    :param image_size_before_crop: Resize to this size before random cropping.
    :param do_shuffle: Shuffle switch.
    :param do_flipping: Flip switch.
    :return:
    """
    if dataset_name not in cyclegan_datasets.DATASET_TO_SIZES:
        raise ValueError('split name %s was not recognized.'
                         % dataset_name)

    csv_name = cyclegan_datasets.PATH_TO_CSV[dataset_name]

    image_i, image_j, name_i, name_j = _load_samples(
        csv_name, cyclegan_datasets.DATASET_TO_IMAGETYPE[dataset_name])

    inputs = {
        'image_i': image_i,
        'image_j': image_j
    }
    # Preprocessing:
    inputs['image_i'] = tf.image.resize_images(
        inputs['image_i'], [h, w])
    inputs['image_j'] = tf.image.resize_images(
        inputs['image_j'], [h, w])

    if do_flipping is True:
        inputs['image_i'] = tf.image.random_flip_left_right(inputs['image_i'], seed=1)
        inputs['image_j'] = tf.image.random_flip_left_right(inputs['image_j'], seed=1)

    inputs['image_i'] = tf.random_crop(
        inputs['image_i'], [model.IMG_HEIGHT, model.IMG_WIDTH, 3], seed=1)
    inputs['image_j'] = tf.random_crop(
        inputs['image_j'], [model.IMG_HEIGHT, model.IMG_WIDTH, 3], seed=1)

    inputs['image_i'] = tf.subtract(tf.div(inputs['image_i'], 127.5), 1)
    inputs['image_j'] = tf.subtract(tf.div(inputs['image_j'], 127.5), 1)

    # Batch
    if do_shuffle is True:
        inputs['images_i'], inputs['images_j'] = tf.train.shuffle_batch(
            [inputs['image_i'], inputs['image_j']], 1, 5000, 100, seed=1)
    else:
        inputs['images_i'], inputs['images_j'] = tf.train.batch(
            [inputs['image_i'], inputs['image_j']], 1, num_threads=1)
    return inputs
