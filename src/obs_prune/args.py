import argparse


def set_args():
    parser = argparse.ArgumentParser(description="Delete unused Obsidian attachments")
    parser.add_argument("vault", type=str, help="The full path to your Obsidian vault")
    args = parser.parse_args()
    return args
