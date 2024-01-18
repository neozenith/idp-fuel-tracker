import os
import sys
from pathlib import Path
import boto3

def discover_heic(start_dir: Path = Path("./data/HEIC/")):
    """Recursively walk and discover a list of HEIC files to process."""
    return [ start_dir /f for f in os.listdir(start_dir) if f.lower().endswith(".heic")]

def targeter(p: Path, suffix: str = "JPEG"):
    return (p.parent.parent / suffix / p.name).with_suffix(f".{suffix}")

def process_image(img_path: Path, type: str = "PNG"):
    """Given the path to a HEIC, convert it to a PNG."""
    from PIL import Image
    from pillow_heif import register_heif_opener

    register_heif_opener()
    target_path = targeter(img_path, type)
    image = Image.open(img_path)
    image.save(target_path,type)
    return target_path


def main(args):
    """Process HEIC images to PNG/JPG."""
    for f in discover_heic():
        print(f"Processing {f} --> ")
        print(process_image(f, "JPEG"))
    

if __name__ == "__main__":
    main(sys.argv)