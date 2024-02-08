"""A package to delete unreferenced attachments in an Obsidian vault"""
import os

from oprune.files import crawl_dir, delete_file
from oprune.args import set_args


def main():
    """Looks for unreferenced attachments in the given Obsidian Vault"""
    ags = set_args()
    path = ags.vault
    all_files = crawl_dir(path)
    attachments = []
    for file in all_files:
        attachments += file.scan_for_attachments()

    for file in all_files:
        if file.is_attachment():
            file_name = file.full_path.split(os.sep)[-1]
            if file_name not in attachments:
                delete_file(file.full_path)


if __name__ == "__main__":
    main()
