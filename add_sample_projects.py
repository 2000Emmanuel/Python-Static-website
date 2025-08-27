#!/usr/bin/env python3
"""
Script to add sample projects with images to the portfolio
"""
import os
import django
from django.core.files import File
from django.core.files.images import ImageFile

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Project, Skill, Experience, Education

def add_sample_projects():
    """Add sample projects to the database"""
    
    # Sample projects data
    projects_data = [
        {
            'title': 'E-Commerce Website',
            'description': 'A full-featured e-commerce platform built with Django and React. Features include user authentication, product catalog, shopping cart, payment integration with Stripe, order management, and admin dashboard. Responsive design with modern UI/UX.',
            'technologies': 'Django, React, PostgreSQL, Stripe API, Bootstrap, JavaScript',
            'github_url': 'https://github.com/yourusername/ecommerce-site',
            'live_url': 'https://your-ecommerce-demo.com',
            'featured': True,
            'image_name': 'project1.jpg'
        },
        {
            'title': 'Task Manager App',
            'description': 'A collaborative task management application with real-time updates. Users can create projects, assign tasks, set deadlines, and track progress. Features drag-and-drop interface, notifications, and team collaboration tools.',
            'technologies': 'Django, WebSockets, JavaScript, Bootstrap, SQLite',
            'github_url': 'https://github.com/yourusername/task-manager',
            'live_url': 'https://your-taskmanager-demo.com',
            'featured': True,
            'image_name': 'project2.jpg'
        },
        {
            'title': 'Weather Dashboard',
            'description': 'A responsive weather application that displays current weather conditions and forecasts. Features location-based weather data, interactive maps, weather alerts, and historical data visualization with charts and graphs.',
            'technologies': 'JavaScript, Chart.js, OpenWeather API, HTML5, CSS3',
            'github_url': 'https://github.com/yourusername/weather-dashboard',
            'live_url': 'https://your-weather-demo.com',
            'featured': False,
            'image_name': 'project3.jpg'
        },
        {
            'title': 'Blog Platform',
            'description': 'A modern blogging platform with rich text editor, comment system, and social sharing. Features include user profiles, post categories, search functionality, SEO optimization, and responsive design.',
            'technologies': 'Django, TinyMCE, PostgreSQL, Bootstrap, JavaScript',
            'github_url': 'https://github.com/yourusername/blog-platform',
            'live_url': 'https://your-blog-demo.com',
            'featured': True,
            'image_name': 'project4.jpg'
        },
        {
            'title': 'Portfolio Website',
            'description': 'This very portfolio website you\'re viewing! Built with Django and Bootstrap, featuring responsive design, admin panel for content management, contact form with email notifications, and optimized for deployment on AWS EC2.',
            'technologies': 'Django, Bootstrap, JavaScript, AWS EC2, Nginx, Gunicorn',
            'github_url': 'https://github.com/yourusername/portfolio-website',
            'live_url': 'https://your-portfolio.com',
            'featured': False,
            'image_name': 'project5.jpg'
        },
        {
            'title': 'Chat Application',
            'description': 'Real-time chat application with multiple rooms, private messaging, file sharing, and emoji support. Built with WebSockets for instant messaging and includes user authentication and message history.',
            'technologies': 'Django Channels, WebSockets, Redis, JavaScript, Bootstrap',
            'github_url': 'https://github.com/yourusername/chat-app',
            'live_url': 'https://your-chat-demo.com',
            'featured': False,
            'image_name': 'project6.jpg'
        }
    ]
    
    # Clear existing projects
    Project.objects.all().delete()
    print("Cleared existing projects")
    
    # Add new projects
    for project_data in projects_data:
        image_name = project_data.pop('image_name')
        image_path = f'static/images/{image_name}'
        
        project = Project.objects.create(**project_data)
        
        # Add image if it exists
        if os.path.exists(image_path):
            with open(image_path, 'rb') as img_file:
                project.image.save(
                    image_name,
                    File(img_file),
                    save=True
                )
        
        print(f"Created project: {project.title}")
    
    print(f"\nAdded {len(projects_data)} sample projects successfully!")

def add_sample_skills():
    """Add sample skills to the database"""
    
    skills_data = [
        # Programming Languages
        {'name': 'Python', 'proficiency': 90, 'category': 'Programming Languages'},
        {'name': 'JavaScript', 'proficiency': 85, 'category': 'Programming Languages'},
        {'name': 'HTML5', 'proficiency': 95, 'category': 'Programming Languages'},
        {'name': 'CSS3', 'proficiency': 90, 'category': 'Programming Languages'},
        {'name': 'SQL', 'proficiency': 80, 'category': 'Programming Languages'},
        
        # Frameworks
        {'name': 'Django', 'proficiency': 90, 'category': 'Frameworks'},
        {'name': 'React', 'proficiency': 75, 'category': 'Frameworks'},
        {'name': 'Bootstrap', 'proficiency': 85, 'category': 'Frameworks'},
        {'name': 'jQuery', 'proficiency': 80, 'category': 'Frameworks'},
        
        # Databases
        {'name': 'PostgreSQL', 'proficiency': 80, 'category': 'Databases'},
        {'name': 'MySQL', 'proficiency': 75, 'category': 'Databases'},
        {'name': 'SQLite', 'proficiency': 85, 'category': 'Databases'},
        {'name': 'Redis', 'proficiency': 70, 'category': 'Databases'},
        
        # Tools & Technologies
        {'name': 'Git', 'proficiency': 85, 'category': 'Tools & Technologies'},
        {'name': 'AWS', 'proficiency': 75, 'category': 'Tools & Technologies'},
        {'name': 'Docker', 'proficiency': 70, 'category': 'Tools & Technologies'},
        {'name': 'Nginx', 'proficiency': 75, 'category': 'Tools & Technologies'},
        {'name': 'Linux', 'proficiency': 80, 'category': 'Tools & Technologies'},
    ]
    
    # Clear existing skills
    Skill.objects.all().delete()
    print("Cleared existing skills")
    
    # Add new skills
    for skill_data in skills_data:
        skill = Skill.objects.create(**skill_data)
        print(f"Created skill: {skill.name}")
    
    print(f"\nAdded {len(skills_data)} sample skills successfully!")

def add_sample_experience():
    """Add sample work experience"""
    
    experience_data = [
        {
            'company': 'Tech Solutions Inc.',
            'position': 'Senior Full Stack Developer',
            'description': 'Led development of web applications using Django and React. Managed a team of 3 developers, implemented CI/CD pipelines, and improved application performance by 40%. Collaborated with product managers and designers to deliver high-quality solutions.',
            'start_date': '2022-01-01',
            'end_date': None,  # Current position
            'location': 'San Francisco, CA'
        },
        {
            'company': 'Digital Innovations LLC',
            'position': 'Full Stack Developer',
            'description': 'Developed and maintained multiple client websites and web applications. Worked with Django, JavaScript, and various APIs. Implemented responsive designs and optimized database queries for better performance.',
            'start_date': '2020-06-01',
            'end_date': '2021-12-31',
            'location': 'Remote'
        },
        {
            'company': 'StartupXYZ',
            'position': 'Junior Web Developer',
            'description': 'Built frontend components using HTML, CSS, and JavaScript. Assisted in backend development with Python and Django. Participated in code reviews and learned best practices for web development.',
            'start_date': '2019-03-01',
            'end_date': '2020-05-31',
            'location': 'New York, NY'
        }
    ]
    
    # Clear existing experience
    Experience.objects.all().delete()
    print("Cleared existing experience")
    
    # Add new experience
    for exp_data in experience_data:
        experience = Experience.objects.create(**exp_data)
        print(f"Created experience: {experience.position} at {experience.company}")
    
    print(f"\nAdded {len(experience_data)} sample work experiences successfully!")

def add_sample_education():
    """Add sample education"""
    
    education_data = [
        {
            'institution': 'University of Technology',
            'degree': 'Bachelor of Science',
            'field_of_study': 'Computer Science',
            'start_date': '2015-09-01',
            'end_date': '2019-05-31',
            'gpa': 3.75
        },
        {
            'institution': 'Online Learning Platform',
            'degree': 'Certificate',
            'field_of_study': 'Full Stack Web Development',
            'start_date': '2018-01-01',
            'end_date': '2018-12-31',
            'gpa': None
        }
    ]
    
    # Clear existing education
    Education.objects.all().delete()
    print("Cleared existing education")
    
    # Add new education
    for edu_data in education_data:
        education = Education.objects.create(**edu_data)
        print(f"Created education: {education.degree} from {education.institution}")
    
    print(f"\nAdded {len(education_data)} sample education records successfully!")

if __name__ == "__main__":
    print("Adding sample data to portfolio...")
    print("=" * 50)
    
    add_sample_projects()
    print()
    add_sample_skills()
    print()
    add_sample_experience()
    print()
    add_sample_education()
    
    print("=" * 50)
    print("All sample data added successfully!")
    print("You can now view your portfolio with sample content.")
    print("Remember to update the personal information in the templates!")
