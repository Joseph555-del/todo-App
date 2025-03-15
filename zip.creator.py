import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_dir, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)


if __name__ == "__main__":
    make_archive(filepaths=["bonus4.py", "bonus5.py"], dest_dir="")