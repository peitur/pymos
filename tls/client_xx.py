#!/usr/bin/env python3

import os, re, sys
import argparse
import threading

import socket
import ssl
import pathlib

from pprint import pprint

if __name__ == "__main__":
    options = dict()
