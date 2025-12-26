import os

def read_token(file_path:str):
    token = None
    with open(file_path) as f:
        lines = f.readlines()
        if len(lines) < 1:
            raise ValueError("File is empty.")
        token = lines[0]
    return token