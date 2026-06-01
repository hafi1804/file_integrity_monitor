import hashlib
import os

print("=== File Integrity Monitor ===")

file_path = input("Enter file path: ")

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()

try:
    current_hash = calculate_hash(file_path)

    hash_file = file_path + ".hash"

    if not os.path.exists(hash_file):

        with open(hash_file, "w") as f:
            f.write(current_hash)

        print("\nBaseline hash created.")
        print("Hash:", current_hash)

    else:

        with open(hash_file, "r") as f:
            original_hash = f.read()

        print("\nOriginal Hash :", original_hash)
        print("Current Hash  :", current_hash)

        if original_hash == current_hash:
            print("\n[OK] File integrity maintained.")
        else:
            print("\n[ALERT] File has been modified!")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)