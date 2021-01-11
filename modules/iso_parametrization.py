import pymeshlab as ml
import os



class Iso_para:

    def __init__(
        self,
        mesh
        ):

        self.ms = mesh


    def start(self):
        ms = self.ms

        ms.apply_filter(
            ' iso_parametrization_main'
            )

        return ms