from files import crawl_dir
from args import set_args


def main():
    args = set_args()
    path = args.vault
    files = crawl_dir(path)
    # check_for_attachments(files)
    for file in files:
        if not file.is_attachment():
            print(file.full_path)


if __name__ == "__main__":
    main()
