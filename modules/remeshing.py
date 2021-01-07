import pymeshlab as ml
import os



class Remesher:

    def __init__(
        self,
        input_file,
        output_file,
        amount
        ):

        self.input_file = input_file
        self.output_file = output_file
        self.amount = amount


    def start(self):
        ms = ml.MeshSet()

        ms.load_new_mesh(self.input_file)
        ms.apply_filter(
            'simplification_quadric_edge_collapse_decimation_with_texture',
            targetperc = self.amount * 0.01,
            preservenormal = True,
            planarquadric = True
            )
        ms.save_current_mesh(self.output_file)