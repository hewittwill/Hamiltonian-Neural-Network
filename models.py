from tensorflow.keras.layers import Input, Conv2D
from tensorflow.keras.models import Model


class PixelEncoder(Model):
    # maps (Xt, Xt+1) to a latent representation of S0 = (p, q) 

    def _conv(self, n_filters):
        x = Conv2D(n_filters, (2,2), 2, padding='same', activation='relu')
        return x

    def _convblock(self):

        self.conv1_1 = self._conv(32)
        self.conv1_2 = self._conv(64)
        self.conv1_3 = self._conv(64)
        self.conv1_4 = self._conv(64)
        self.conv1_5 = self._conv(64)
        self.conv1_6 = self._conv(64)
        self.conv1_7 = self._conv(64)
        self.conv1_8 = self._conv(48)

        return 


    def __init__(self):
        super(PixelEncoder, self).__init__()

        self.input1_1 = Input()
        self.input1_2 = Input()



    def call(self, inputs):

        x = self.input1_1:
        x =

        return x

class HamiltonianNetwork(Model):
    # Maps latent representation of S0 = (p, q) to scalar R (Hamiltonian of the system)

    def __init__(self):
        super(HamiltonianNetwork, self).__init__()
