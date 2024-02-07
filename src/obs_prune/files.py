import os
import pathlib
import re

from dataclasses import dataclass

extentions_to_ignore = ["md", "canvas"]


@dataclass
class VaultFile:
    full_path: str
    extension: str

    def is_attachment(self) -> bool:
        return self.extension not in extentions_to_ignore

    def scan_for_attachments(self) -> list[str]:
        attachments = []
        # No reason to look for attachments in attachments
        if self.is_attachment():
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


def crawl_dir(path: str, slash: str) -> list[VaultFile]:
    files = []
    for root, _, file_names in os.walk(path):
        for f in file_names:
            # files.append({"directory": root, "files": file_names})
            full_path = root + slash + f
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
    file = pathlib.Path(path)
    confirmation = input(f"Are you sure you would like to delete {file}? y/N\n> ")
    if confirmation.lower() == "y":
        file.unlink()
    else:
        print(f"Skipping file {file}")
