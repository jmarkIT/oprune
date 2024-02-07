import os
import platform

from dataclasses import dataclass

extentions_to_ignore = ["md", "canvas"]


@dataclass
class VaultFile:
    full_path: str
    extension: str

    def is_attachment(self) -> bool:
        return self.extension not in extentions_to_ignore

    def scan_for_attachments(self):
        # No reason to look for attachments in attachments
        if self.is_attachment():
            return

        print(self.full_path)

        with open(self.full_path, encoding="utf8") as f:
            lines = f.readlines()
            for line in lines:
                print(line)


def crawl_dir(path: str) -> list[VaultFile]:
    files = []
    slash = "/"
    if platform.system() == "Windows":
        slash = "\\"
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
