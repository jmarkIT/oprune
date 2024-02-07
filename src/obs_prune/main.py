from files import crawl_dir, delete_file
from args import set_args
import platform


def main():
    # Set appropriate slash for operating system
    operating_system = platform.system()
    slash = "/"
    if operating_system == "Windows":
        slash = "\\"
    args = set_args()
    path = args.vault
    files = crawl_dir(path, slash)
    attachments = []
    for file in files:
        attachments += file.scan_for_attachments()

    for file in files:
        if file.is_attachment():
            file_name = file.full_path.split(slash)[-1]
            if file_name not in attachments:
                delete_file(file.full_path)


if __name__ == "__main__":
    main()
