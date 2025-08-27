#!/usr/bin/env python3
"""
Script to create placeholder images for the portfolio website
"""
import os
from PIL import Image, ImageDraw, ImageFont

def create_placeholder_image(width, height, text, filename, bg_color='lightblue', text_color='darkblue'):
    """Create a placeholder image with text"""
    # Create image
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    except:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
        except:
            font = ImageFont.load_default()
    
    # Get text size and position
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save image
    img.save(filename, 'JPEG', quality=85)
    print(f"Created: {filename}")

def main():
    # Create static/images directory if it doesn't exist
    images_dir = 'static/images'
    os.makedirs(images_dir, exist_ok=True)
    
    # Create profile image
    create_placeholder_image(
        400, 400, 
        "Your Photo\nHere", 
        f"{images_dir}/profile.jpg",
        bg_color='#4a90e2',
        text_color='white'
    )
    
    # Create hero background image
    create_placeholder_image(
        1200, 600, 
        "Hero Background", 
        f"{images_dir}/hero-bg.jpg",
        bg_color='#2c3e50',
        text_color='white'
    )
    
    # Create project placeholder images
    project_images = [
        ("E-Commerce\nWebsite", "project1.jpg"),
        ("Task Manager\nApp", "project2.jpg"),
        ("Weather\nDashboard", "project3.jpg"),
        ("Blog\nPlatform", "project4.jpg"),
        ("Portfolio\nWebsite", "project5.jpg"),
        ("Chat\nApplication", "project6.jpg")
    ]
    
    colors = [
        ('#e74c3c', 'white'),  # Red
        ('#3498db', 'white'),  # Blue
        ('#2ecc71', 'white'),  # Green
        ('#f39c12', 'white'),  # Orange
        ('#9b59b6', 'white'),  # Purple
        ('#1abc9c', 'white')   # Teal
    ]
    
    for i, (text, filename) in enumerate(project_images):
        bg_color, text_color = colors[i % len(colors)]
        create_placeholder_image(
            600, 400, 
            text, 
            f"{images_dir}/{filename}",
            bg_color=bg_color,
            text_color=text_color
        )
    
    # Create about page image
    create_placeholder_image(
        500, 600, 
        "About Me\nImage", 
        f"{images_dir}/about-me.jpg",
        bg_color='#34495e',
        text_color='white'
    )
    
    # Create logo/favicon placeholder
    create_placeholder_image(
        64, 64, 
        "Logo", 
        f"{images_dir}/favicon.jpg",
        bg_color='#2c3e50',
        text_color='white'
    )
    
    print("\nAll placeholder images created successfully!")
    print("You can replace these with your actual images later.")

if __name__ == "__main__":
    main()
