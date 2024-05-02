import sys
import os
import zlib

def main():

    def run_cat_file(mode, file_hash):
        folder_name = file_hash[:2]
        file_name = file_hash[2:]
        file_path = f".git/objects/{folder_name}/{file_name}"
        with open(file_path, "rb") as file:
            data = file.read()
            data_decompressed = zlib.decompress(data)
            data_content = data_decompressed.split(b"\x00")[1]
            data_decoded = data_content.decode("utf-8")
            print(data_decoded, end="")


    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")
    elif command == "cat-file":
        mode = sys.argv[2]
        file_hash = sys.argv[3]
        run_cat_file(mode, file_hash)
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
