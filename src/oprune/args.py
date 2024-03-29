"""Returns parsed arguments for use by main
"""
import argparse


def set_args():
    """Parses args for use at CLI, returns parsed args

    Returns:
        Namespace: parsed arguments
    """
    parser = argparse.ArgumentParser(description="Delete unused Obsidian attachments")
    parser.add_argument("vault", type=str, help="The full path to your Obsidian vault")
    args = parser.parse_args()
    return args
