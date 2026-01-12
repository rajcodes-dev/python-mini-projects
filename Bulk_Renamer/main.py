"""Just a simple files renamer project."""
import os 


def rename_file(files, ext):
    """Rename the files."""

    files_with_ext = []
    for file in files:
        if file.endswith(ext):
            files_with_ext.append(file)

    for idx, file in enumerate(files_with_ext):
        os.rename(file, f"image_{idx+1}{ext}")


if __name__ == "__main__":
    files = os.listdir()
    rename_file(files, ".jpg")
