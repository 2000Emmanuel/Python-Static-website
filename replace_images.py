#!/usr/bin/env python3
"""
Script to help replace placeholder images with your own images
"""
import os
import shutil
from pathlib import Path

def list_current_images():
    """List all current images in the static/images directory"""
    images_dir = Path('static/images')
    if not images_dir.exists():
        print("Images directory not found!")
        return
    
    print("Current images in static/images/:")
    print("=" * 40)
    
    for image_file in sorted(images_dir.glob('*.jpg')):
        size = image_file.stat().st_size
        size_kb = size / 1024
        print(f"  {image_file.name:<20} ({size_kb:.1f} KB)")
    
    print("\nImage descriptions:")
    print("-" * 40)
    descriptions = {
        'profile.jpg': 'Your profile photo (400x400px recommended)',
        'hero-bg.jpg': 'Hero section background (1200x600px recommended)',
        'about-me.jpg': 'About page image (500x600px recommended)',
        'favicon.jpg': 'Website favicon (64x64px)',
        'project1.jpg': 'E-Commerce Website project image',
        'project2.jpg': 'Task Manager App project image',
        'project3.jpg': 'Weather Dashboard project image',
        'project4.jpg': 'Blog Platform project image',
        'project5.jpg': 'Portfolio Website project image',
        'project6.jpg': 'Chat Application project image',
    }
    
    for filename, description in descriptions.items():
        print(f"  {filename:<15} - {description}")

def replace_image(old_filename, new_image_path):
    """Replace an existing image with a new one"""
    images_dir = Path('static/images')
    old_path = images_dir / old_filename
    new_path = Path(new_image_path)
    
    if not new_path.exists():
        print(f"Error: New image file '{new_image_path}' not found!")
        return False
    
    if not old_path.exists():
        print(f"Error: Target file '{old_filename}' not found in static/images/!")
        return False
    
    # Create backup
    backup_dir = images_dir / 'backups'
    backup_dir.mkdir(exist_ok=True)
    backup_path = backup_dir / f"backup_{old_filename}"
    shutil.copy2(old_path, backup_path)
    print(f"Created backup: {backup_path}")
    
    # Replace the image
    shutil.copy2(new_path, old_path)
    print(f"Successfully replaced {old_filename} with {new_image_path}")
    
    return True

def interactive_replace():
    """Interactive mode to replace images"""
    print("\nInteractive Image Replacement")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. List current images")
        print("2. Replace an image")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            list_current_images()
        
        elif choice == '2':
            print("\nAvailable images to replace:")
            images_dir = Path('static/images')
            image_files = sorted([f.name for f in images_dir.glob('*.jpg')])
            
            for i, filename in enumerate(image_files, 1):
                print(f"  {i}. {filename}")
            
            try:
                img_choice = int(input(f"\nSelect image to replace (1-{len(image_files)}): "))
                if 1 <= img_choice <= len(image_files):
                    old_filename = image_files[img_choice - 1]
                    new_image_path = input(f"Enter path to new image for {old_filename}: ").strip()
                    
                    if replace_image(old_filename, new_image_path):
                        print("Don't forget to run 'python manage.py collectstatic' after replacing images!")
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def main():
    """Main function"""
    print("Portfolio Image Management Tool")
    print("=" * 50)
    
    if not os.path.exists('static/images'):
        print("Error: static/images directory not found!")
        print("Make sure you're running this script from the portfolio root directory.")
        return
    
    if len(os.sys.argv) > 1:
        # Command line mode
        if os.sys.argv[1] == 'list':
            list_current_images()
        elif os.sys.argv[1] == 'replace' and len(os.sys.argv) == 4:
            old_filename = os.sys.argv[2]
            new_image_path = os.sys.argv[3]
            replace_image(old_filename, new_image_path)
        else:
            print("Usage:")
            print("  python replace_images.py list")
            print("  python replace_images.py replace <old_filename> <new_image_path>")
            print("  python replace_images.py  (for interactive mode)")
    else:
        # Interactive mode
        interactive_replace()

if __name__ == "__main__":
    main()
