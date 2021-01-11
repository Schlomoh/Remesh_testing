import argparse
import os

import pymeshlab as ml

from modules.simplification_w_textures import Simplification
from modules.iso_parametrization import Iso_para



class OBJ_PL:

    def __init__(
        self,
        input = '',
        output_dir = '',
        target_sizes = [],
        iso_para = False,
        
    ):
        self.input_file = input
        self.output_dir = output_dir
        self.target_sizes = target_sizes
        self.iso_para = iso_para

        self.mesh = ml.MeshSet()
        self.mesh.load_new_mesh(input)


    def fs_estimation(self, file, target_sizes ):

        '''Estimates a percentage by which to decimate the mesh according to the set target filesize'''

        stats = os.stat(file)

        orig_file_size = int(round(stats.st_size / (1024 * 1024)))
        
        target_percentages = []

        for size in target_sizes:
            size += 2

            target_perc = round(size / orig_file_size, 2)

            target_percentages.append(target_perc)

        return target_percentages


    def simplify(self, mesh, amount):
        
        '''Calling simplifier module'''

        simplifier = Simplification(
            mesh,
            amount
            )

        return simplifier.start()


    def iso_parametrization(self, mesh):

        '''Calling module for iso parametrization'''

        iso = Iso_para(mesh)

        return iso.start()



    def start(self):
        
        '''Select action from argument'''

        print('Input_file:', self.input_file)


        if self.output_dir == '':
            self.output_dir = os.path.dirname(os.path.abspath(self.input_file))

        input_file = self.input_file
        target_percentages = self.fs_estimation(input_file, self.target_sizes)

        for amount in target_percentages:
            mesh = self.mesh

        #   making output file name
            base = os.path.basename(self.input_file)
            name = os.path.splitext(base)[0]
        #   ext = os.path.splitext(base)[1]

            output_file = self.output_dir + name + '_remsh_' + str(amount)
            print('new file', output_file)
            print('resizing percentage:', amount)

            if self.iso_para:
                mesh = self.iso_parametrization(mesh)
            
            mesh = self.simplify(mesh, amount)

            mesh.save_current_mesh(output_file)



def main():

    '''Argument handling'''
    
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument('input_file', type=str, help='Set the input file')
    parser.add_argument('-d', '--decimation_perc', type=int, help='Percentage by which to decimate mesh.')
    parser.add_argument('-o', '--output_dir', type=str, help='If not set the output file will be saved next to the original.')
    parser.add_argument('-p', '--iso_parametrization', action='store_true', help='Set to activate iso_parametrization')

    args = parser.parse_args()
    decimation = []
    decimation.append(args.decimation_perc)

    pipeline = OBJ_PL(
        input=args.input_file,
        output_dir=args.output_dir,
        target_sizes=decimation,
        iso_para=args.iso_parametrization
    )

    pipeline.start()


if __name__ == "__main__":
    main()