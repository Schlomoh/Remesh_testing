import argparse
import os, sys

from modules.remeshing import Remesher



class Meshlab:

    def __init__(self, args):
     
        self.input_file = args.input
        self.action = args.action

        if args.output_dir != None:
            self.output_dir = args.output_dir
        else:
            self.output_dir = ''

        if args.decimation_amount != None:
            self.amount = args.decimation_amount
        else:
            self.amount = 50


    def remesh(self):
        
        '''Calling remesher module'''

        remesher = Remesher(
            self.input_file,
            self.output_file,
            self.amount
            )

        remesher.start()


    def select(self):
        
        '''Select action from argument'''

        print('Input_file:', self.input_file)

        if self.output_dir == '':
            self.output_dir = os.path.dirname(os.path.abspath(self.input_file))

    #   making output file name
        base = os.path.basename(self.input_file)
        name = os.path.splitext(base)[0]
        ext = os.path.splitext(base)[1]
        print('amount:', self.amount)
        new_file = self.output_dir + name + '_remsh_' + str(self.amount) + ext
        print('new file', new_file)

        self.output_file = new_file

        action = self.action

        if action == 'remesh':
            self.remesh()
    
    #   Future actions
    #   ...
    #   ...
    #   ...


def main():

    '''Argument handling'''
    
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument('input', type=str, help='set the input file to be edited')
    parser.add_argument('action', type=str, help='The action to be applied onto the input file')
    parser.add_argument('-d', '--decimation_amount', type=int, help='percentage by which to decimate mesh')
    parser.add_argument('-o', '--output_dir', type=str, help='If not set the output file will be saved next to the original.')
    
    args = parser.parse_args()

    meshlab = Meshlab(args)

    meshlab.select()


if __name__ == "__main__":
    main()