from tensorflow.keras.layers import Input, Conv2D, Concatenate
from tensorflow.keras.models import Model

# HYPER PARAMS
n_hidden = 6

def _conv(n_filters):
    x = Conv2D(n_filters, (2,2), 2, padding='same', activation='relu')
    return x

def _convblock(input_layer):
    x = _conv(32)(input_layer)
    x = _conv(64)(x)

    return x

def PixelEncoder():
    # maps ((MxN)t, (MxN)t+1) to (4x4x32) latent representation of (p,q)

    input_1 = Input(shape=(32,32, 1))
    input_2 = Input(shape=(32,32, 1))

    encoder_branch_1 = _convblock(input_1)
    encoder_branch_2 = _convblock(input_2)

    concatenate_1 = Concatenate()([encoder_branch_1, encoder_branch_2])

    conv_1 = _conv(32)(concatenate_1)

    model = Model(inputs=[input_1, input_2], outputs=conv_1)

    return model

def HamiltionianNN():

    r
