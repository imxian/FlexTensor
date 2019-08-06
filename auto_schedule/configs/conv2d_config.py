import copy


def copy_change_batch(batch, x):
    ret = copy.deepcopy(x[1:])
    ret = (batch,) + ret
    return ret


yolo_shapes_b1 = [
    # batch, in_channel, height, width, out_channel, _, k_h, k_w, _, stride, padding, dilation, groups = shape
    # yolo
    (1, 3, 448, 448, 64, 3, 7, 7, 1, 2, 3, 1, 1),  # conv1  0
    (1, 64, 112, 112, 192, 64, 3, 3, 1, 1, 1, 1, 1),  # conv2   1
    (1, 192, 56, 56, 128, 192, 1, 1, 1, 1, 0, 1, 1),  # conv3   2
    (1, 128, 56, 56, 256, 128, 3, 3, 1, 1, 1, 1, 1),  # conv4   3
    (1, 256, 56, 56, 256, 256, 1, 1, 1, 1, 0, 1, 1),  # conv5   4
    (1, 256, 56, 56, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv6   5
    (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),  # conv7   6
    (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv8   7
    # # (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),  # conv9
    # # (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv10
    # # (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),  # conv11
    # # (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv12
    # # (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),  # conv13
    # # (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv14
    (1, 512, 28, 28, 512, 512, 1, 1, 1, 1, 0, 1, 1),  # conv15      8
    (1, 512, 28, 28, 1024, 512, 3, 3, 1, 1, 1, 1, 1),  # conv16     9
    (1, 1024, 14, 14, 512, 1024, 1, 1, 1, 1, 0, 1, 1),  # conv17    10
    (1, 512, 14, 14, 1024, 512, 3, 3, 1, 1, 1, 1, 1),  # conv18     11
    # # (1, 1024, 14, 14, 512, 1024, 1, 1, 1, 1, 0, 1, 1),  # conv19
    # # (1, 512, 14, 14, 1024, 512, 3, 3, 1, 1, 1, 1, 1),  # conv20
    (1, 1024, 14, 14, 1024, 1024, 3, 3, 1, 1, 1, 1, 1),  # conv21   12
    (1, 1024, 14, 14, 1024, 1024, 3, 3, 1, 2, 1, 1, 1),  # conv22   13
    (1, 1024, 7, 7, 1024, 1024, 3, 3, 1, 1, 1, 1, 1),  # conv23     14
    # (1, 1024, 7, 7, 1024, 1024, 3, 3, 1, 1, 1, 1, 1),  # conv24
]


yolo_shapes_b8 = [copy_change_batch(8, x) for x in yolo_shapes_b1]
yolo_shapes_b16 = [copy_change_batch(16, x) for x in yolo_shapes_b1]
yolo_shapes_b32 = [copy_change_batch(32, x) for x in yolo_shapes_b1]
yolo_shapes_b64 = [copy_change_batch(64, x) for x in yolo_shapes_b1]
yolo_shapes_b128 = [copy_change_batch(128, x) for x in yolo_shapes_b1]


yolo_shapes = yolo_shapes_b1


mobilev2_shapes_b1 = [
    (1, 32, 112, 112, 32, 32, 3, 3, 1, 1, 1, 1, 32),
    (1, 16, 112, 112, 16 * 6, 16, 3, 3, 1, 2, 1, 1, 16),
    (1, 24, 56, 56, 24 * 6, 24, 3, 3, 1, 2, 1, 1, 24),
    (1, 32, 28, 28, 32 * 6, 32, 3, 3, 1, 2, 1, 1, 32),
    (1, 64, 14, 14, 64 * 6, 64, 3, 3, 1, 1, 1, 1, 64),
    (1, 96, 14, 14, 96 * 6, 96, 3, 3, 1, 2, 1, 1, 96),
    (1, 160, 7, 7, 160 * 6, 160, 3, 3, 1, 1, 1, 1, 160),
]


mobilev2_shapes_b8 = [
    (8, 32, 112, 112, 32, 32, 3, 3, 1, 1, 1, 1, 32),
    (8, 16, 112, 112, 16 * 6, 16, 3, 3, 1, 2, 1, 1, 16),
    (8, 24, 56, 56, 24 * 6, 24, 3, 3, 1, 2, 1, 1, 24),
    (8, 32, 28, 28, 32 * 6, 32, 3, 3, 1, 2, 1, 1, 32),
    (8, 64, 14, 14, 64 * 6, 64, 3, 3, 1, 1, 1, 1, 64),
    (8, 96, 14, 14, 96 * 6, 96, 3, 3, 1, 2, 1, 1, 96),
    (8, 160, 7, 7, 160 * 6, 160, 3, 3, 1, 1, 1, 1, 160),
]


mobilev2_shapes = mobilev2_shapes_b1


google_shapes = [
    # google-net
    (1, 3, 224, 224, 64, 3, 7, 7, 1, 2, 3, 1, 1),  # conv1
    (1, 64, 56, 56, 64, 64, 1, 1, 1, 1, 0, 1, 1),  # conv2_3x3_reduce
    (1, 64, 56, 56, 192, 64, 3, 3, 1, 1, 1, 1, 1),  # conv2_3x3
    (1, 192, 28, 28, 64, 192, 1, 1, 1, 1, 0, 1, 1),  # inception3a_branch1
    (1, 192, 28, 28, 96, 192, 1, 1, 1, 1, 0, 1, 1),  # inception3a_branch2a
    (1, 96, 28, 28, 128, 96, 3, 3, 1, 1, 1, 1, 1),  # inception3a_branch2b
    (1, 192, 28, 28, 16, 192, 1, 1, 1, 1, 0, 1, 1),  # inception3a_branch3a
    (1, 16, 28, 28, 32, 16, 5, 5, 1, 1, 2, 1, 1),  # inception3a_branch3b
    (1, 192, 28, 28, 32, 192, 1, 1, 1, 1, 0, 1, 1),  # inception3a_branch4
    (1, 256, 28, 28, 128, 256, 1, 1, 1, 1, 0, 1, 1),  # inception3b_branch1
    # (1, 256, 28, 28, 128, 256, 1, 1, 1, 1, 0, 1, 1),  # inception3b_branch2a
    (1, 128, 28, 28, 192, 128, 3, 3, 1, 1, 1, 1, 1),  # inception3b_branch2b
    (1, 256, 28, 28, 32, 256, 1, 1, 1, 1, 0, 1, 1),  # inception3b_branch3a
    (1, 32, 28, 28, 96, 32, 5, 5, 1, 1, 2, 1, 1),  # inception3b_branch3b
    (1, 256, 28, 28, 64, 256, 1, 1, 1, 1, 0, 1, 1),  # inception3b_branch4
    (1, 480, 14, 14, 192, 480, 1, 1, 1, 1, 0, 1, 1),  # inception4a_branch1
    (1, 480, 14, 14, 96, 480, 1, 1, 1, 1, 0, 1, 1),  # inception4a_branch2a
    (1, 96, 14, 14, 208, 96, 3, 3, 1, 1, 1, 1, 1),  # inception4a_branch2b
    (1, 480, 14, 14, 16, 480, 1, 1, 1, 1, 0, 1, 1),  # inception4a_branch3a
    (1, 16, 14, 14, 48, 16, 5, 5, 1, 1, 2, 1, 1),  # inception4a_branch3b
    (1, 480, 14, 14, 64, 480, 1, 1, 1, 1, 0, 1, 1),  # inception4a_branch4
    (1, 512, 14, 14, 160, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4b_branch1
    (1, 512, 14, 14, 112, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4b_branch2a
    (1, 112, 14, 14, 224, 112, 3, 3, 1, 1, 1, 1, 1),  # inception4b_branch2b
    (1, 512, 14, 14, 24, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4b_branch3a
    (1, 24, 14, 14, 64, 24, 5, 5, 1, 1, 2, 1, 1),  # inception4b_branch3b
    (1, 512, 14, 14, 64, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4b_branch4
    (1, 512, 14, 14, 128, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4c_branch1
    # (1, 512, 14, 14, 128, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4c_branch2a
    (1, 128, 14, 14, 256, 128, 3, 3, 1, 1, 1, 1, 1),  # inception4c_branch2b
    # (1, 512, 14, 14, 24, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4c_branch3a
    # (1, 24, 14, 14, 64, 24, 5, 5, 1, 1, 2, 1, 1),  # inception4c_branch3b
    # (1, 512, 14, 14, 64, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4c_branch4
    # (1, 512, 14, 14, 112, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4d_branch1
    (1, 512, 14, 14, 144, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4d_branch2a
    (1, 144, 14, 14, 288, 144, 3, 3, 1, 1, 1, 1, 1),  # inception4d_branch2b
    (1, 512, 14, 14, 32, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4d_branch3a
    (1, 32, 14, 14, 64, 32, 5, 5, 1, 1, 2, 1, 1),  # inception4d_branch3b
    # (1, 512, 14, 14, 64, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4d_branch4
    (1, 528, 14, 14, 256, 528, 1, 1, 1, 1, 0, 1, 1),  # inception4e_branch1
    (1, 528, 14, 14, 160, 528, 1, 1, 1, 1, 0, 1, 1),  # inception4e_branch2a
    (1, 160, 14, 14, 320, 160, 3, 3, 1, 1, 1, 1, 1),  # inception4e_branch2b
    (1, 528, 14, 14, 32, 528, 1, 1, 1, 1, 0, 1, 1),  # inception4e_branch3a
    (1, 32, 14, 14, 128, 32, 5, 5, 1, 1, 2, 1, 1),  # inception4e_branch3b
    (1, 528, 14, 14, 128, 528, 1, 1, 1, 1, 0, 1, 1),  # inception4e_branch4
    (1, 832, 7, 7, 256, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5a_branch1
    (1, 832, 7, 7, 160, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5a_branch2a
    (1, 160, 7, 7, 320, 160, 3, 3, 1, 1, 1, 1, 1),  # inception5a_branch2b
    (1, 832, 7, 7, 32, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5a_branch3a
    (1, 32, 7, 7, 128, 32, 5, 5, 1, 1, 2, 1, 1),  # inception5a_branch3b
    (1, 832, 7, 7, 128, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5a_branch4
    (1, 832, 7, 7, 384, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5b_branch1
    (1, 832, 7, 7, 192, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5b_branch2a
    (1, 192, 7, 7, 384, 192, 3, 3, 1, 1, 1, 1, 1),  # inception5b_branch2b
    (1, 832, 7, 7, 48, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5b_branch3a
    (1, 48, 7, 7, 128, 48, 5, 5, 1, 1, 2, 1, 1),  # inception5b_branch3b
    # (1, 832, 7, 7, 128, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5b_branch4
]

squeeze_shapes = [
    # squeeze-net
    (1, 3, 227, 227, 96, 3, 7, 7, 1, 2, 0, 1, 1),  # conv1
    (1, 96, 55, 55, 16, 96, 1, 1, 1, 1, 0, 1, 1),  # fire2
    (1, 16, 55, 55, 64, 16, 1, 1, 1, 1, 0, 1, 1),  # fire2_1
    (1, 16, 55, 55, 64, 16, 3, 3, 1, 1, 1, 1, 1),  # fire2_2
    (1, 128, 55, 55, 16, 128, 1, 1, 1, 1, 0, 1, 1),  # fire3
    # (1, 16, 55, 55, 64, 16, 1, 1, 1, 1, 0, 1, 1),  # fire3_1
    # (1, 16, 55, 55, 64, 16, 3, 3, 1, 1, 1, 1, 1),  # fire3_2
    (1, 128, 55, 55, 32, 128, 1, 1, 1, 1, 0, 1, 1),  # fire4
    (1, 32, 55, 55, 128, 32, 1, 1, 1, 1, 0, 1, 1),  # fire4_1
    (1, 32, 55, 55, 128, 32, 3, 3, 1, 1, 1, 1, 1),  # fire4_2
    (1, 256, 27, 27, 32, 256, 1, 1, 1, 1, 0, 1, 1),  # fire5
    (1, 32, 27, 27, 128, 32, 1, 1, 1, 1, 0, 1, 1),  # fire5_1
    (1, 32, 27, 27, 128, 32, 3, 3, 1, 1, 1, 1, 1),  # fire5_2
    (1, 256, 27, 27, 48, 256, 1, 1, 1, 1, 0, 1, 1),  # fire6
    (1, 48, 27, 27, 192, 48, 1, 1, 1, 1, 0, 1, 1),  # fire6_1
    (1, 48, 27, 27, 192, 48, 3, 3, 1, 1, 1, 1, 1),  # fire6_2
    (1, 384, 27, 27, 48, 384, 1, 1, 1, 1, 0, 1, 1),  # fire7
    # (1, 48, 27, 27, 192, 48, 1, 1, 1, 1, 0, 1, 1),  # fire7_1
    # (1, 48, 27, 27, 192, 48, 3, 3, 1, 1, 1, 1, 1),  # fire7_2
    (1, 384, 27, 27, 64, 384, 1, 1, 1, 1, 0, 1, 1),  # fire8
    (1, 64, 27, 27, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # fire8_1
    (1, 64, 27, 27, 256, 64, 3, 3, 1, 1, 1, 1, 1),  # fire8_2
    (1, 512, 13, 13, 64, 512, 1, 1, 1, 1, 0, 1, 1),  # fire9
    (1, 64, 13, 13, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # fire9_1
    (1, 64, 13, 13, 256, 64, 3, 3, 1, 1, 1, 1, 1),  # fire9_2
    (1, 512, 13, 13, 1000, 512, 1, 1, 1, 1, 0, 1, 1),  # conv10
]

res_shapes_b1 = [
    # resnet-50
    (1, 3, 224, 224, 64, 3, 7, 7, 1, 2, 3, 1, 1),  # conv1
    (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # res2a_branch1
    (1, 64, 56, 56, 64, 64, 1, 1, 1, 1, 0, 1, 1),  # res2a_branch2a
    (1, 64, 56, 56, 64, 64, 3, 3, 1, 1, 1, 1, 1),  # res2a_branch2b
    # (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # res2a_branch2c
    (1, 256, 56, 56, 64, 256, 1, 1, 1, 1, 0, 1, 1),  # res2b_branch2a
    # (1, 64, 56, 56, 64, 64, 3, 3, 1, 1, 1, 1, 1),  # res2b_branch2b
    # (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # res2b_branch2c
    # (1, 256, 56, 56, 64, 256, 1, 1, 1, 1, 0, 1, 1),  # res2c_branch2a
    # (1, 64, 56, 56, 64, 64, 3, 3, 1, 1, 1, 1, 1),  # res2c_branch2b
    # (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # res2c_branch2c
    (1, 256, 56, 56, 512, 256, 1, 1, 1, 2, 0, 1, 1),  # res3a_branch1
    (1, 256, 56, 56, 128, 256, 1, 1, 1, 2, 0, 1, 1),  # res3a_branch2a
    (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # res3a_branch2b
    (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),  # res3a_branch2c
    (1, 512, 28, 28, 128, 512, 1, 1, 1, 1, 0, 1, 1),  # res3b_branch2a
    # (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # res3b_branch2b
    # (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),  # res3b_branch2c
    # (1, 512, 28, 28, 128, 512, 1, 1, 1, 1, 0, 1, 1),  # res3c_branch2a
    # (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # res3c_branch2b
    # (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),  # res3c_branch2c
    # (1, 512, 28, 28, 128, 512, 1, 1, 1, 1, 0, 1, 1),  # res3d_branch2a
    # (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # res3d_branch2b
    # (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),  # res3d_branch2c
    (1, 512, 28, 28, 1024, 512, 1, 1, 1, 2, 0, 1, 1),  # res4a_branch1
    (1, 512, 28, 28, 256, 512, 1, 1, 1, 2, 0, 1, 1),  # res4a_branch2a
    (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4a_branch2b
    (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4a_branch2c
    (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # res4b_branch2a
    # (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4b_branch2b
    # (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4b_branch2c
    # (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # res4c_branch2a
    # (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4c_branch2b
    # (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4c_branch2c
    # (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # res4d_branch2a
    # (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4d_branch2b
    # (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4d_branch2c
    # (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # res4e_branch2a
    # (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4e_branch2b
    # (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4e_branch2c
    # (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # res4f_branch2a
    # (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4f_branch2b
    # (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4f_branch2c
    (1, 1024, 14, 14, 2048, 1024, 1, 1, 1, 2, 0, 1, 1),  # res5a_branch1
    (1, 1024, 14, 14, 512, 1024, 1, 1, 1, 2, 0, 1, 1),  # res5a_branch2a
    (1, 512, 7, 7, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # res5a_branch2b
    (1, 512, 7, 7, 2048, 512, 1, 1, 1, 1, 0, 1, 1),  # res5a_branch2c
    (1, 2048, 7, 7, 512, 2048, 1, 1, 1, 1, 0, 1, 1),  # res5b_branch2a
    # (1, 512, 7, 7, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # res5b_branch2b
    # (1, 512, 7, 7, 2048, 512, 1, 1, 1, 1, 0, 1, 1),  # res5b_branch2c
    # (1, 2048, 7, 7, 512, 2048, 1, 1, 1, 1, 0, 1, 1),  # res5c_branch2a
    # (1, 512, 7, 7, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # res5c_branch2b
    # (1, 512, 7, 7, 2048, 512, 1, 1, 1, 1, 0, 1, 1),  # res5c_branch2c
]

res_shapes = [copy_change_batch(64, x) for x in res_shapes_b1]

vgg_16_shapes = [
    # vgg-16
    (1, 3, 224, 224, 64, 3, 3, 3, 1, 1, 1, 1, 1),  # conv1_1
    (1, 64, 224, 224, 64, 64, 3, 3, 1, 1, 1, 1, 1),  # conv1_2
    (1, 64, 112, 112, 128, 64, 3, 3, 1, 1, 1, 1, 1),  # conv2_1
    (1, 128, 112, 112, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # conv2_2
    (1, 128, 56, 56, 256, 128, 3, 3, 1, 1, 1, 1, 1),  # conv3_1
    (1, 256, 56, 56, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # conv3_2
    # (1, 256, 56, 56, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # conv3_3
    (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv4_1
    (1, 512, 28, 28, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv4_2
    # (1, 512, 28, 28, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv4_3
    (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_1
    # (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_2
    # (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_3
]

vgg_19_shapes = [
    # vgg-19
    # (1, 3, 224, 224, 64, 3, 3, 3, 1, 1, 1, 1, 1),  # conv1_1
    # (1, 64, 224, 224, 64, 64, 3, 3, 1, 1, 1, 1, 1),  # conv1_2
    # (1, 64, 112, 112, 128, 64, 3, 3, 1, 1, 1, 1, 1),  # conv2_1
    # (1, 128, 112, 112, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # conv2_2
    # (1, 128, 56, 56, 256, 128, 3, 3, 1, 1, 1, 1, 1),  # conv3_1
    # (1, 256, 56, 56, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # conv3_2
    # (1, 256, 56, 56, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # conv3_3
    # (1, 256, 56, 56, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # conv3_4
    # (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv4_1
    # (1, 512, 28, 28, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv4_2
    # (1, 512, 28, 28, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv4_3
    # (1, 512, 28, 28, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv4_4
    # (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_1
    # (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_2
    # (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_3
    # (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_4
]

test_conv_shapes = [
    # batch_size, 
    # in_channel, 
    # inputs_height, 
    # inputs_width, 
    # out_channel, 
    # channel_per_group, 
    # kernel_height, 
    # kernel_width, 
    # if_bias=0, 
    # stride=1, 
    # padding=0, 
    # dilation=1, 
    # groups=1, 
    # dtype="float32"

    # jlc
    (256, 256, 14, 14, 512, 256, 1, 1, 0, 1, 0, 1, 1),
    # open
    # (1, 1024, 7, 7, 1024, 1024, 3, 3, 0, 1, 1, 1, 1), # yolo 24
    # (1, 384, 27, 27, 64, 384, 1, 1, 1, 1, 0, 1, 1), # squeeze-net fire 8
    # (4, 112, 14, 14, 224, 112, 3, 3, 0, 1, 1, 2, 1), # google-net inception4b-branch2b
    # # confidential
    # (1, 64, 56, 56, 256, 64, 1, 1, 0, 1, 0, 1, 1), # resnet res2a_branch1
    # (1, 512, 28, 28, 512, 512, 3, 3, 0, 1, 1, 2, 1), # vgg-16 conv4_2
]

all_conv_shapes = [
    ###########################################################
    # fuck!!!! I should write these configs by hands!!!!!
    # I am a foolish!
    # # yolo
    # (1, 3, 448, 448, 64, 3, 7, 7, 1, 2, 3, 1, 1),       # 1
    # (1, 64, 112, 112, 192, 64, 3, 3, 1, 1, 1, 1, 1),    # 2
    # (1, 192, 56, 56, 128, 192, 1, 1, 1, 1, 0, 1, 1),    # 3
    # (1, 128, 56, 56, 256, 128, 3, 3, 1, 1, 1, 1, 1),    # 4
    # (1, 256, 56, 56, 256, 256, 1, 1, 1, 1, 0, 1, 1),    # 5
    # (1, 256, 56, 56, 512, 256, 3, 3, 1, 1, 1, 1, 1),    # 6
    # (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),    # 7
    # (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),    # 8
    # (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),    # 9
    # (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),    # 10
    # (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),    # 11
    # (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),    # 12
    # (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),    # 13
    # (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),    # 14
    # (1, 512, 28, 28, 512, 512, 1, 1, 1, 1, 0, 1, 1),    # 15
    # (1, 512, 28, 28, 1024, 512, 3, 3, 1, 1, 1, 1, 1),   # 16
    # (1, 1024, 14, 14, 512, 1024, 1, 1, 1, 1, 0, 1, 1),  # 17
    # (1, 512, 14, 14, 1024, 512, 3, 3, 1, 1, 1, 1, 1),   # 18
    # (1, 1024, 14, 14, 512, 1024, 1, 1, 1, 1, 0, 1, 1),  # 19
    # (1, 512, 14, 14, 1024, 512, 3, 3, 1, 1, 1, 1, 1),   # 20
    # (1, 1024, 14, 14, 1024, 1024, 3, 3, 1, 1, 1, 1, 1), # 21
    # (1, 1024, 14, 14, 1024, 1024, 3, 3, 1, 2, 1, 1, 1), # 22
    # (1, 1024, 7, 7, 1024, 1024, 3, 3, 1, 1, 1, 1, 1),   # 23
    # (1, 1024, 7, 7, 1024, 1024, 3, 3, 1, 1, 1, 1, 1),   # 24

    # # ResNet-50
    # (1, 3, 224, 224, 64, 3, 7, 7, 1, 2, 3, 1, 1),       # 1
    # (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),      # 2
    # (1, 64, 56, 56, 64, 64, 1, 1, 1, 1, 0, 1, 1),       # 3
    # (1, 64, 56, 56, 64, 64, 3, 3, 1, 1, 1, 1, 1),       # 4
    # (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),      # 5
    # (1, 256, 56, 56, 64, 256, 1, 1, 1, 1, 0, 1, 1),     # 6
    # (1, 64, 56, 56, 64, 64, 3, 3, 1, 1, 1, 1, 1),       # 7
    # (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),      # 8
    # (1, 256, 56, 56, 64, 256, 1, 1, 1, 1, 0, 1, 1),     # 9
    # (1, 64, 56, 56, 64, 64, 3, 3, 1, 1, 1, 1, 1),       # 10
    # (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),      # 11
    # (1, 256, 56, 56, 512, 256, 1, 1, 1, 2, 1, 1, 1),    # 12
    # (1, 256, 56, 56, 128, 256, 1, 1, 1, 2, 1, 1, 1),    # 13
    # (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),    # 14
    # (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),    # 15
    # (1, 512, 28, 28, 128, 512, 1, 1, 1, 1, 0, 1, 1),    # 16
    # (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),    # 17
    # (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),    # 18
    # (1, 512, 28, 28, 128, 512, 1, 1, 1, 1, 0, 1, 1),    # 19
    # (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),    # 20
    # (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),    # 21
    # (1, 512, 28, 28, 128, 512, 1, 1, 1, 1, 0, 1, 1),    # 22
    # (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),    # 23
    # (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),    # 24
    # (1, 512, 28, 28, 1024, 512, 1, 1, 1, 2, 0, 1, 1),   # 25
    # (1, 512, 28, 28, 256, 512, 1, 1, 1, 2, 0, 1, 1),    # 26
    # (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),    # 27
    # (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),   # 28
    # (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # 29
    # (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),    # 30
    # (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),   # 31
    # (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # 32
    # (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),    # 33
    # (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),   # 34
    # (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # 35
    # (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),    # 36
    # (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),   # 37
    # (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # 38
    # (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),    # 39
    # (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),   # 40
    # (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # 41
    # (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),    # 42
    # (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),   # 43
    # (1, 1024, 14, 14, 2048, 1024, 1, 1, 1, 2, 0, 1, 1), # 44
    # (1, 1024, 14, 14, 512, 1024, 1, 1, 1, 2, 0, 1, 1),  # 45
    # (1, 512, 7, 7, 512, 512, 3, 3, 1, 1, 1, 1, 1),      # 46
    # (1, 512, 7, 7, 2048, 512, 1, 1, 1, 1, 0, 1, 1),     # 47
    # (1, 2048, 7, 7, 512, 2048, 1, 1, 1, 1, 0, 1, 1),    # 48
    # (1, 512, 7, 7, 512, 512, 3, 3, 1, 1, 1, 1, 1),      # 49
    # (1, 512, 7, 7, 2048, 512, 1, 1, 1, 1, 0, 1, 1),     # 50
    # (1, 2048, 7, 7, 512, 2048, 1, 1, 1, 1, 0, 1, 1),    # 51
    # (1, 512, 7, 7, 512, 512, 3, 3, 1, 1, 1, 1, 1),      # 52
    # (1, 512, 7, 7, 2048, 512, 1, 1, 1, 1, 0, 1, 1),      # 53

    # # google-net
    # (1, 3, 224, 224, 64, 3, 7, 7, 1, 2, 3, 1, 1),
    # (1, 64, 56, 56, 64, 64, 1, 1, 1, 1, 0, 1, 1),
    # (1, 64, 56, 56, 192, 64, 3, 3, 1, 1, 1, 1, 1),
    # (1, 192, 28, 28, 64, 192, 1, 1, 1, 1, 0, 1, 1),
    # (1, 192, 28, 28, 96, 192, 1, 1, 1, 1, 0, 1, 1),
    # (1, 96, 28, 28, 128, 96, 3, 3, 1, 1, 1, 1, 1),
    # (1, 192, 28, 28, 16, 192, 1, 1, 1, 1, 0, 1, 1),
    # (1, 16, 28, 28, 32, 16, 5, 5, 1, 1, 2, 1, 1),
    # (1, 192, 28, 28, 32, 192, 1, 1, 1, 1, 0, 1, 1),
    # (1, 256, 28, 28, 128, 256, 1, 1, 1, 1, 0, 1, 1),
    # (1, 256, 28, 28, 128, 256, 1, 1, 1, 1, 0, 1, 1),
    # (1, 128, 28, 28, 192, 128, 3, 3, 1, 1, 1, 1, 1),
    # (1, 256, 28, 28, 32, 256, 1, 1, 1, 1, 0, 1, 1),
    # (1, 32, 28, 28, 96, 32, 5, 5, 1, 1, 2, 1, 1),
    # (1, 256, 28, 28, 64, 256, 1, 1, 1, 1, 0, 1, 1),
    # (1, 480, 14, 14, 192, 480, 1, 1, 1, 1, 0, 1, 1),
    # (1, 480, 14, 14, 96, 480, 1, 1, 1, 1, 0, 1, 1),
    # (1, 96, 14, 14, 208, 96, 3, 3, 1, 1, 1, 1, 1),
    # (1, 480, 14, 14, 16, 480, 1, 1, 1, 1, 0, 1, 1),
    # (1, 16, 14, 14, 48, 16, 5, 5, 1, 1, 2, 1, 1),
    # (1, 480, 14, 14, 64, 480, 1, 1, 1, 1, 0, 1, 1),
    # (1, 512, 14, 14, 160, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 512, 14, 14, 112, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 112, 14, 14, 224, 112, 3, 3, 1, 1, 1, 1, 1),
    # (1, 512, 14, 14, 24, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 24, 14, 14, 64, 24, 5, 5, 1, 1, 2, 1, 1),
    # (1, 512, 14, 14, 64, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 512, 14, 14, 128, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 512, 14, 14, 128, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 128, 14, 14, 256, 128, 3, 3, 1, 1, 1, 1, 1),
    # (1, 512, 14, 14, 24, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 24, 14, 14, 64, 24, 5, 5, 1, 1, 2, 1, 1),
    # (1, 512, 14, 14, 64, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 512, 14, 14, 112, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 512, 14, 14, 144, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 144, 14, 14, 288, 144, 3, 3, 1, 1, 1, 1, 1),
    # (1, 512, 14, 14, 32, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 32, 14, 14, 64, 32, 5, 5, 1, 1, 2, 1, 1),
    # (1, 512, 14, 14, 64, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 512, 14, 14, 256, 512, 1, 1, 1, 1, 0, 1, 1),
    # (1, 528, 14, 14, 160, 528, 1, 1, 1, 1, 0, 1, 1),
    # (1, 160, 14, 14, 320, 160, 3, 3, 1, 1, 1, 1, 1),
    # (1, 528, 14, 14, 32, 528, 1, 1, 1, 1, 0, 1, 1),
    # (1, 32, 14, 14, 128, 32, 5, 5, 1, 1, 2, 1, 1),
    # (1, 528, 14, 14, 128, 528, 1, 1, 1, 1, 0, 1, 1),
    # (1, 832, 7, 7, 256, 832, 1, 1, 1, 1, 0, 1, 1),
    # (1, 832, 7, 7, 160, 832, 1, 1, 1, 1, 0, 1, 1),
    # (1, 160, 7, 7, 320, 160, 3, 3, 1, 1, 1, 1, 1),
    # (1, 832, 7, 7, 32, 832, 1, 1, 1, 1, 0, 1, 1),
    # (1, 32, 7, 7, 128, 32, 5, 5, 1, 1, 2, 1, 1),
    # (1, 832, 7, 7, 128, 832, 1, 1, 1, 1, 0, 1, 1),
    # (1, 832, 7, 7, 384, 832, 1, 1, 1, 1, 0, 1, 1),
    # (1, 832, 7, 7, 192, 832, 1, 1, 1, 1, 0, 1, 1),
    # (1, 192, 7, 7, 384, 192, 3, 3, 1, 1, 1, 1, 1),
    # (1, 832, 7, 7, 48, 832, 1, 1, 1, 1, 0, 1, 1),
    # (1, 48, 7, 7, 128, 48, 5, 5, 1, 1, 2, 1, 1),
    # (1, 832, 7, 7, 128, 832, 1, 1, 1, 1, 0, 1, 1),

    # yolo
    (1, 3, 448, 448, 64, 3, 7, 7, 1, 2, 3, 1, 1),  # conv1
    (1, 64, 112, 112, 192, 64, 3, 3, 1, 1, 1, 1, 1),  # conv2
    (1, 192, 56, 56, 128, 192, 1, 1, 1, 1, 0, 1, 1),  # conv3
    (1, 128, 56, 56, 256, 128, 3, 3, 1, 1, 1, 1, 1),  # conv4
    (1, 256, 56, 56, 256, 256, 1, 1, 1, 1, 0, 1, 1),  # conv5
    (1, 256, 56, 56, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv6
    (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),  # conv7
    (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv8
    (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),  # conv9
    (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv10
    (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),  # conv11
    (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv12
    (1, 512, 28, 28, 256, 512, 1, 1, 1, 1, 0, 1, 1),  # conv13
    (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv14
    (1, 512, 28, 28, 512, 512, 1, 1, 1, 1, 0, 1, 1),  # conv15
    (1, 512, 28, 28, 1024, 512, 3, 3, 1, 1, 1, 1, 1),  # conv16
    (1, 1024, 14, 14, 512, 1024, 1, 1, 1, 1, 0, 1, 1),  # conv17
    (1, 512, 14, 14, 1024, 512, 3, 3, 1, 1, 1, 1, 1),  # conv18
    (1, 1024, 14, 14, 512, 1024, 1, 1, 1, 1, 0, 1, 1),  # conv19
    (1, 512, 14, 14, 1024, 512, 3, 3, 1, 1, 1, 1, 1),  # conv20
    (1, 1024, 14, 14, 1024, 1024, 3, 3, 1, 1, 1, 1, 1),  # conv21
    (1, 1024, 14, 14, 1024, 1024, 3, 3, 1, 2, 1, 1, 1),  # conv22
    (1, 1024, 7, 7, 1024, 1024, 3, 3, 1, 1, 1, 1, 1),  # conv23
    (1, 1024, 7, 7, 1024, 1024, 3, 3, 1, 1, 1, 1, 1),  # conv24

    # google-net
    (1, 3, 224, 224, 64, 3, 7, 7, 1, 2, 3, 1, 1),  # conv1
    (1, 64, 56, 56, 64, 64, 1, 1, 1, 1, 0, 1, 1),  # conv2_3x3_reduce
    (1, 64, 56, 56, 192, 64, 3, 3, 1, 1, 1, 1, 1),  # conv2_3x3
    (1, 192, 28, 28, 64, 192, 1, 1, 1, 1, 0, 1, 1),  # inception3a_branch1
    (1, 192, 28, 28, 96, 192, 1, 1, 1, 1, 0, 1, 1),  # inception3a_branch2a
    (1, 96, 28, 28, 128, 96, 3, 3, 1, 1, 1, 1, 1),  # inception3a_branch2b
    (1, 192, 28, 28, 16, 192, 1, 1, 1, 1, 0, 1, 1),  # inception3a_branch3a
    (1, 16, 28, 28, 32, 16, 5, 5, 1, 1, 2, 1, 1),  # inception3a_branch3b
    (1, 192, 28, 28, 32, 192, 1, 1, 1, 1, 0, 1, 1),  # inception3a_branch4
    (1, 256, 28, 28, 128, 256, 1, 1, 1, 1, 0, 1, 1),  # inception3b_branch1
    (1, 256, 28, 28, 128, 256, 1, 1, 1, 1, 0, 1, 1),  # inception3b_branch2a
    (1, 128, 28, 28, 192, 128, 3, 3, 1, 1, 1, 1, 1),  # inception3b_branch2b
    (1, 256, 28, 28, 32, 256, 1, 1, 1, 1, 0, 1, 1),  # inception3b_branch3a
    (1, 32, 28, 28, 96, 32, 5, 5, 1, 1, 2, 1, 1),  # inception3b_branch3b
    (1, 256, 28, 28, 64, 256, 1, 1, 1, 1, 0, 1, 1),  # inception3b_branch4
    (1, 480, 14, 14, 192, 480, 1, 1, 1, 1, 0, 1, 1),  # inception4a_branch1
    (1, 480, 14, 14, 96, 480, 1, 1, 1, 1, 0, 1, 1),  # inception4a_branch2a
    (1, 96, 14, 14, 208, 96, 3, 3, 1, 1, 1, 1, 1),  # inception4a_branch2b
    (1, 480, 14, 14, 16, 480, 1, 1, 1, 1, 0, 1, 1),  # inception4a_branch3a
    (1, 16, 14, 14, 48, 16, 5, 5, 1, 1, 2, 1, 1),  # inception4a_branch3b
    (1, 480, 14, 14, 64, 480, 1, 1, 1, 1, 0, 1, 1),  # inception4a_branch4
    (1, 512, 14, 14, 160, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4b_branch1
    (1, 512, 14, 14, 112, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4b_branch2a
    (1, 112, 14, 14, 224, 112, 3, 3, 1, 1, 1, 1, 1),  # inception4b_branch2b
    (1, 512, 14, 14, 24, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4b_branch3a
    (1, 24, 14, 14, 64, 24, 5, 5, 1, 1, 2, 1, 1),  # inception4b_branch3b
    (1, 512, 14, 14, 64, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4b_branch4
    (1, 512, 14, 14, 128, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4c_branch1
    (1, 512, 14, 14, 128, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4c_branch2a
    (1, 128, 14, 14, 256, 128, 3, 3, 1, 1, 1, 1, 1),  # inception4c_branch2b
    (1, 512, 14, 14, 24, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4c_branch3a
    (1, 24, 14, 14, 64, 24, 5, 5, 1, 1, 2, 1, 1),  # inception4c_branch3b
    (1, 512, 14, 14, 64, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4c_branch4
    (1, 512, 14, 14, 112, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4d_branch1
    (1, 512, 14, 14, 144, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4d_branch2a
    (1, 144, 14, 14, 288, 144, 3, 3, 1, 1, 1, 1, 1),  # inception4d_branch2b
    (1, 512, 14, 14, 32, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4d_branch3a
    (1, 32, 14, 14, 64, 32, 5, 5, 1, 1, 2, 1, 1),  # inception4d_branch3b
    (1, 512, 14, 14, 64, 512, 1, 1, 1, 1, 0, 1, 1),  # inception4d_branch4
    (1, 528, 14, 14, 256, 528, 1, 1, 1, 1, 0, 1, 1),  # inception4e_branch1
    (1, 528, 14, 14, 160, 528, 1, 1, 1, 1, 0, 1, 1),  # inception4e_branch2a
    (1, 160, 14, 14, 320, 160, 3, 3, 1, 1, 1, 1, 1),  # inception4e_branch2b
    (1, 528, 14, 14, 32, 528, 1, 1, 1, 1, 0, 1, 1),  # inception4e_branch3a
    (1, 32, 14, 14, 128, 32, 5, 5, 1, 1, 2, 1, 1),  # inception4e_branch3b
    (1, 528, 14, 14, 128, 528, 1, 1, 1, 1, 0, 1, 1),  # inception4e_branch4
    (1, 832, 7, 7, 256, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5a_branch1
    (1, 832, 7, 7, 160, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5a_branch2a
    (1, 160, 7, 7, 320, 160, 3, 3, 1, 1, 1, 1, 1),  # inception5a_branch2b
    (1, 832, 7, 7, 32, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5a_branch3a
    (1, 32, 7, 7, 128, 32, 5, 5, 1, 1, 2, 1, 1),  # inception5a_branch3b
    (1, 832, 7, 7, 128, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5a_branch4
    (1, 832, 7, 7, 384, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5b_branch1
    (1, 832, 7, 7, 192, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5b_branch2a
    (1, 192, 7, 7, 384, 192, 3, 3, 1, 1, 1, 1, 1),  # inception5b_branch2b
    (1, 832, 7, 7, 48, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5b_branch3a
    (1, 48, 7, 7, 128, 48, 5, 5, 1, 1, 2, 1, 1),  # inception5b_branch3b
    (1, 832, 7, 7, 128, 832, 1, 1, 1, 1, 0, 1, 1),  # inception5b_branch4

    # squeeze-net
    (1, 3, 227, 227, 96, 3, 7, 7, 1, 2, 0, 1, 1),  # conv1
    (1, 96, 55, 55, 16, 96, 1, 1, 1, 1, 0, 1, 1),  # fire2
    (1, 16, 55, 55, 64, 16, 1, 1, 1, 1, 0, 1, 1),  # fire2_1
    (1, 16, 55, 55, 64, 16, 3, 3, 1, 1, 1, 1, 1),  # fire2_2
    (1, 128, 55, 55, 16, 128, 1, 1, 1, 1, 0, 1, 1),  # fire3
    (1, 16, 55, 55, 64, 16, 1, 1, 1, 1, 0, 1, 1),  # fire3_1
    (1, 16, 55, 55, 64, 16, 3, 3, 1, 1, 1, 1, 1),  # fire3_2
    (1, 128, 55, 55, 32, 128, 1, 1, 1, 1, 0, 1, 1),  # fire4
    (1, 32, 55, 55, 128, 32, 1, 1, 1, 1, 0, 1, 1),  # fire4_1
    (1, 32, 55, 55, 128, 32, 3, 3, 1, 1, 1, 1, 1),  # fire4_2
    (1, 256, 27, 27, 32, 256, 1, 1, 1, 1, 0, 1, 1),  # fire5
    (1, 32, 27, 27, 128, 32, 1, 1, 1, 1, 0, 1, 1),  # fire5_1
    (1, 32, 27, 27, 128, 32, 3, 3, 1, 1, 1, 1, 1),  # fire5_2
    (1, 256, 27, 27, 48, 256, 1, 1, 1, 1, 0, 1, 1),  # fire6
    (1, 48, 27, 27, 192, 48, 1, 1, 1, 1, 0, 1, 1),  # fire6_1
    (1, 48, 27, 27, 192, 48, 3, 3, 1, 1, 1, 1, 1),  # fire6_2
    (1, 384, 27, 27, 48, 384, 1, 1, 1, 1, 0, 1, 1),  # fire7
    (1, 48, 27, 27, 192, 48, 1, 1, 1, 1, 0, 1, 1),  # fire7_1
    (1, 48, 27, 27, 192, 48, 3, 3, 1, 1, 1, 1, 1),  # fire7_2
    (1, 384, 27, 27, 64, 384, 1, 1, 1, 1, 0, 1, 1),  # fire8
    (1, 64, 27, 27, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # fire8_1
    (1, 64, 27, 27, 256, 64, 3, 3, 1, 1, 1, 1, 1),  # fire8_2
    (1, 512, 13, 13, 64, 512, 1, 1, 1, 1, 0, 1, 1),  # fire9
    (1, 64, 13, 13, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # fire9_1
    (1, 64, 13, 13, 256, 64, 3, 3, 1, 1, 1, 1, 1),  # fire9_2
    (1, 512, 13, 13, 1000, 512, 1, 1, 1, 1, 0, 1, 1),  # conv10

    # resnet-50
    (1, 3, 224, 224, 64, 3, 7, 7, 1, 2, 3, 1, 1),  # conv1
    (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # res2a_branch1
    (1, 64, 56, 56, 64, 64, 1, 1, 1, 1, 0, 1, 1),  # res2a_branch2a
    (1, 64, 56, 56, 64, 64, 3, 3, 1, 1, 1, 1, 1),  # res2a_branch2b
    (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # res2a_branch2c
    (1, 256, 56, 56, 64, 256, 1, 1, 1, 1, 0, 1, 1),  # res2b_branch2a
    (1, 64, 56, 56, 64, 64, 3, 3, 1, 1, 1, 1, 1),  # res2b_branch2b
    (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # res2b_branch2c
    (1, 256, 56, 56, 64, 256, 1, 1, 1, 1, 0, 1, 1),  # res2c_branch2a
    (1, 64, 56, 56, 64, 64, 3, 3, 1, 1, 1, 1, 1),  # res2c_branch2b
    (1, 64, 56, 56, 256, 64, 1, 1, 1, 1, 0, 1, 1),  # res2c_branch2c
    (1, 256, 56, 56, 512, 256, 1, 1, 1, 2, 0, 1, 1),  # res3a_branch1
    (1, 256, 56, 56, 128, 256, 1, 1, 1, 2, 0, 1, 1),  # res3a_branch2a
    (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # res3a_branch2b
    (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),  # res3a_branch2c
    (1, 512, 28, 28, 128, 512, 1, 1, 1, 1, 0, 1, 1),  # res3b_branch2a
    (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # res3b_branch2b
    (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),  # res3b_branch2c
    (1, 512, 28, 28, 128, 512, 1, 1, 1, 1, 0, 1, 1),  # res3c_branch2a
    (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # res3c_branch2b
    (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),  # res3c_branch2c
    (1, 512, 28, 28, 128, 512, 1, 1, 1, 1, 0, 1, 1),  # res3d_branch2a
    (1, 128, 28, 28, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # res3d_branch2b
    (1, 128, 28, 28, 512, 128, 1, 1, 1, 1, 0, 1, 1),  # res3d_branch2c
    (1, 512, 28, 28, 1024, 512, 1, 1, 1, 2, 0, 1, 1),  # res4a_branch1
    (1, 512, 28, 28, 256, 512, 1, 1, 1, 2, 0, 1, 1),  # res4a_branch2a
    (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4a_branch2b
    (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4a_branch2c
    (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # res4b_branch2a
    (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4b_branch2b
    (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4b_branch2c
    (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # res4c_branch2a
    (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4c_branch2b
    (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4c_branch2c
    (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # res4d_branch2a
    (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4d_branch2b
    (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4d_branch2c
    (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # res4e_branch2a
    (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4e_branch2b
    (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4e_branch2c
    (1, 1024, 14, 14, 256, 1024, 1, 1, 1, 1, 0, 1, 1),  # res4f_branch2a
    (1, 256, 14, 14, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # res4f_branch2b
    (1, 256, 14, 14, 1024, 256, 1, 1, 1, 1, 0, 1, 1),  # res4f_branch2c
    (1, 1024, 14, 14, 2048, 1024, 1, 1, 1, 2, 0, 1, 1),  # res5a_branch1
    (1, 1024, 14, 14, 512, 1024, 1, 1, 1, 2, 0, 1, 1),  # res5a_branch2a
    (1, 512, 7, 7, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # res5a_branch2b
    (1, 512, 7, 7, 2048, 512, 1, 1, 1, 1, 0, 1, 1),  # res5a_branch2c
    (1, 2048, 7, 7, 512, 2048, 1, 1, 1, 1, 0, 1, 1),  # res5b_branch2a
    (1, 512, 7, 7, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # res5b_branch2b
    (1, 512, 7, 7, 2048, 512, 1, 1, 1, 1, 0, 1, 1),  # res5b_branch2c
    (1, 2048, 7, 7, 512, 2048, 1, 1, 1, 1, 0, 1, 1),  # res5c_branch2a
    (1, 512, 7, 7, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # res5c_branch2b
    (1, 512, 7, 7, 2048, 512, 1, 1, 1, 1, 0, 1, 1),  # res5c_branch2c

    # vgg-16
    (1, 3, 224, 224, 64, 3, 3, 3, 1, 1, 1, 1, 1),  # conv1_1
    (1, 64, 224, 224, 64, 64, 3, 3, 1, 1, 1, 1, 1),  # conv1_2
    (1, 64, 112, 112, 128, 64, 3, 3, 1, 1, 1, 1, 1),  # conv2_1
    (1, 128, 112, 112, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # conv2_2
    (1, 128, 56, 56, 256, 128, 3, 3, 1, 1, 1, 1, 1),  # conv3_1
    (1, 256, 56, 56, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # conv3_2
    (1, 256, 56, 56, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # conv3_3
    (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv4_1
    (1, 512, 28, 28, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv4_2
    (1, 512, 28, 28, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv4_3
    (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_1
    (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_2
    (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_3

    # vgg-19
    (1, 3, 224, 224, 64, 3, 3, 3, 1, 1, 1, 1, 1),  # conv1_1
    (1, 64, 224, 224, 64, 64, 3, 3, 1, 1, 1, 1, 1),  # conv1_2
    (1, 64, 112, 112, 128, 64, 3, 3, 1, 1, 1, 1, 1),  # conv2_1
    (1, 128, 112, 112, 128, 128, 3, 3, 1, 1, 1, 1, 1),  # conv2_2
    (1, 128, 56, 56, 256, 128, 3, 3, 1, 1, 1, 1, 1),  # conv3_1
    (1, 256, 56, 56, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # conv3_2
    (1, 256, 56, 56, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # conv3_3
    (1, 256, 56, 56, 256, 256, 3, 3, 1, 1, 1, 1, 1),  # conv3_4
    (1, 256, 28, 28, 512, 256, 3, 3, 1, 1, 1, 1, 1),  # conv4_1
    (1, 512, 28, 28, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv4_2
    (1, 512, 28, 28, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv4_3
    (1, 512, 28, 28, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv4_4
    (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_1
    (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_2
    (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_3
    (1, 512, 14, 14, 512, 512, 3, 3, 1, 1, 1, 1, 1),  # conv5_4
]

# with open("config.txt", "r") as fin:
#     for line in fin:
#         name, batch, in_c, h, w, out_c, k_h, k_w, pad, stride = line.split()
#         print("(" + batch + ", " + in_c + ", " + h + ", " + w + ", " + out_c + ", " + 
#             in_c + ", " + k_h + ", " + k_w + ", 1, " + stride + ", " + pad + ", 1, 1),  # " + name)
