from obs_prune.files import crawl_dir, delete_file
from obs_prune.args import set_args
import platform


def main():
    # Set appropriate slash for operating system
    operating_system = platform.system()
    slash = "/"
    if operating_system == "Windows":
        slash = "\\"
    ags = set_args()
    path = ags.vault
    all_files = crawl_dir(path, slash)
    attachments = []
    for file in all_files:
        attachments += file.scan_for_attachments()

    for file in all_files:
        if file.is_attachment():
            file_name = file.full_path.split(slash)[-1]
            if file_name not in attachments:
                delete_file(file.full_path)


if __name__ == "__main__":
    main()
