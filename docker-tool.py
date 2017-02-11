#!/usr/bin/python3

import argparse, subprocess

DOCKER_NAME_FORMAT='{}:{}'
DOCKER_IMG_NAME='zeenlym/dolibarr'

class Main:

    def __init__(self):
        self.initParser()

    def initParser(self):
        self.parser = argparse.ArgumentParser(description='Tool for building this docker image')
        subparsers = self.parser.add_subparsers(dest='command')
        parser_build = subparsers.add_parser('build', help='Build image')
        parser_push = subparsers.add_parser('push', help='Push image')

    def exec(self):
        self.args = self.parser.parse_args()
        command = self.args.command
        if (command == 'build'):
            self.build()
        elif (command == 'push'):
            self.push()
        else :
            self.parser.print_help()
            exit(1)

    def build(self):
        cmd = 'docker build -t {} .'.format(
            DOCKER_NAME_FORMAT.format(DOCKER_IMG_NAME, self.getTag())
        )
        print(cmd)
        try:
            subprocess.check_call(cmd, shell=True)
        except subprocess.CalledProcessError:
            print('Error while building')
            exit()
        return

    def push(self):
        pass

    def getTag(self):
        tag = 'latest'
        with open('docker-tag', 'r') as f:
            tag = f.read().strip()
        return tag

if __name__ == '__main__':
    try:
        main = Main()
        main.exec()
    except KeyboardInterrupt:
        exit(0)

