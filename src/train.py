"""
A very fake training module for demo purposes
"""
import os

def train():
    """
    An extremely useless training function for demo purposes
    """
    print('Current training mode is {}'.format(os.environ['TRAINING_MODE']))


if __name__ == '__main__':
    train()
