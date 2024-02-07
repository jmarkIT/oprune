from files import crawl_dir
from args import set_args


def main():
    args = set_args()
    path = args.vault
    files = crawl_dir(path)
    for file in files:
        file.scan_for_attachments()


if __name__ == "__main__":
    main()
