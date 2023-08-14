#!/usr/bin/python3
import argparse
import subprocess
import sys
import requests

SESSION = '53616c7465645f5f92bb9b25843fe8f6156bd64c0a98fdb8caa39d9e9970bc37d54d4ec9b4c8cec9933fce4a177abdd8bb091a6e627ceb507ec1ba3b7d32a8ea'

agent = 'https://github.com/necr0mancer/advent-of-code-2022/blob/main/fetch_input.py by robm@librem.one'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2022)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}" -A {agent}'
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)

