import argparse
import os, sys

from modules.remeshing import Remesher



class Meshlab:

    def __init__(
        self,
        input_file,
        action,
        amount = 50,
        output_dir = ''
        ):

        self.input_file = input_file
        self.output_dir = output_dir
        self.action = action
        self.amount = amount


    def select(self):
        print(chr(10))
        print(self.input_file)
        print(self.action)

        action = self.action

        if action = 'remesh'


def main():
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument('input', type=str, help='set the input file to be edited')
    parser.add_argument('action', type=str, help='The action to be applied onto the input file')
    parser.add_argument('-d', '--decimation_amount', type=float, help='percentage by which to decimate mesh')
    parser.add_argument('-o', '--output_dir', type=str, help='If not set the output file will be saved next to the original.')
    args = parser.parse_args()

    meshlab = Meshlab(
        args.input,
        args.action,
        args.decimation_amount,
        args.output_dir
    )

    meshlab.select()


if __name__ == "__main__":
    main()
