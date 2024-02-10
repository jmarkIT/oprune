"""Contains classes and functions to interact with files
"""
import os
import pathlib
import re

from dataclasses import dataclass


@dataclass
class VaultFile:
    """Class to represent a file in an Obsidian vault"""

    full_path: str
    extension: str

    EXTENSIONS_TO_IGNORE = ("md", "canvas")

    @property
    def is_attachment(self) -> bool:
        """Checks if the file is an attachments, and returns a bool

        Returns:
            bool: Is this file an attachment
        """
        return self.extension not in self.EXTENSIONS_TO_IGNORE

    def scan_for_attachments(self) -> list[str]:
        """Looks for attachments referenced in the file

        Returns:
            list[str]: list of all attachments referenced in the file
        """
        attachments = []  # type: list[str]
        # No reason to look for attachments in attachments
        if self.is_attachment:
            return attachments

        regex = re.compile(r"!\[{2}([^\]]+)\]]")

        with open(self.full_path, encoding="utf8") as f:
            lines = f.readlines()
            for line in lines:
                matches = regex.findall(line)
                if not matches:
                    continue
                for match in matches:
                    match = match.strip("[")
                    match = match.strip("]")
                    attachments.append(match)

        return attachments


def crawl_dir(path: str) -> list[VaultFile]:
    """Crawls the provided path returning a list of all files found
    Ignores files in .obsidian and .DS_Store files

    Args:
        path (str): path to directory to crawl
        slash (str): which slash to use in the path '/' for posix systems, '\\' for Windows

    Returns:
        list[VaultFile]: list of all files found as ObsidianFile type
    """
    files = []
    for root, _, file_names in os.walk(path):
        for f in file_names:
            # files.append({"directory": root, "files": file_names})
            full_path = root + os.sep + f
            extension = f.split(".")[-1]
            # Throw away any .DS_Store files we find
            if extension == "DS_Store":
                continue
            # We don't want to accidentally delete anything in Obsidian's configuration directory
            if ".obsidian" in root:
                continue
            files.append(VaultFile(full_path, extension))

    return files


def delete_file(path: str):
    """Deletes file at the provided path after recieving user confirmation

    Args:
        path (str): path of the file to delete
    """
    file = pathlib.Path(path)
    confirmation = input(f"Are you sure you would like to delete {file}? y/N\n> ")
    if confirmation.lower() == "y":
        file.unlink()
    else:
        print(f"Skipping file {file}")
