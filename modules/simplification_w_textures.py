import pymeshlab as ml
import os



class Simplification:

    def __init__(
        self,
        ms,
        amount
        ):

        self.ms = ms
        self.amount = amount


    def start(self):
        ms = self.ms

        ms.apply_filter(
            'simplification_quadric_edge_collapse_decimation_with_texture',
            targetperc = self.amount * 0.01,
            preservenormal = True,
            planarquadric = True
            )
            
        return ms