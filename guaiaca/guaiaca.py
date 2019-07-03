# -*- coding: utf-8 -*-


import os
import boto3
from cmd import Cmd

from guaiaca.config import VERIFY
from guaiaca.services.s3 import create_bucket, upload_file, list_files


class MyPrompt(Cmd):
    prompt = 'guaiaca> '
    intro = "Welcome to Guaiaca! Type ? to list commands"

    def do_exit(self, inp):
        print("Bye")
        return True

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def do_login(self, inp):
        access_key = input('Enter the AWS Access Key: ')
        os.environ["GUAIACA_AWS_ACCESS_KEY"] = access_key

        secret_key = input('Enter the AWS Secret Key: ')
        os.environ["GUAIACA_AWS_SECRET_KEY"] = secret_key

        account_name = boto3.client('iam', verify=VERIFY).list_account_aliases()['AccountAliases'][0]
        print("Logged in AWS Account: {}".format(account_name))

    def help_login(self):
        print("Login on AWS Account")

    def do_configure(self, inp):
        certificate_path = input('Enter the PATH of the certificate: ')
        os.environ["GUAIACA_CERTIFICATE_PATH"] = certificate_path

    def do_create_bucket(self, inp):
        bucket_name = input('Enter the bucket name: ')
        create_bucket(bucket_name)

    def do_add(self, inp):
        print("adding '{}'".format(inp))

    def help_add(self):
        print("Add a new entry to the system.")

    def do_list(self, inp):
        s3 = boto3.resource('s3', verify=VERIFY)
        for bucket in s3.buckets.all():
            print(bucket.name)

    def do_upload_file(self, inp):
        file_name = input('Enter file name: ')
        upload_file(file_name)

    def do_list_files(self, inp):
        list_files()

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        print("Default: {}".format(inp))

    do_EOF = do_exit
    help_EOF = help_exit


def main():
    MyPrompt().cmdloop()
