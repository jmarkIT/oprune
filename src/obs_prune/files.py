import os
from dataclasses import dataclass


@dataclass
class VaultFile:
    full_path: str
    extension: str

    def is_attachment(self) -> bool:
        return self.extension != "md" or self.extension != "canvas"


def crawl_dir(path: str) -> list[VaultFile]:
    files = []
    for root, _, file_names in os.walk(path):
        for f in file_names:
            # files.append({"directory": root, "files": file_names})
            full_path = root + "/" + f
            extension = f.split(".")[-1]
            files.append(VaultFile(full_path, extension))

    return files
