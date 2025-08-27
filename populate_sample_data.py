#!/usr/bin/env python
"""
Sample data population script for Portfolio Django App
Run this script to populate your portfolio with sample data for testing
"""

import os
import sys
import django
from datetime import date, datetime

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Project, Skill, Experience, Education

def create_sample_projects():
    """Create sample projects"""
    projects_data = [
        {
            'title': 'E-Commerce Platform',
            'description': '''A full-stack e-commerce platform built with Django and React. Features include user authentication, product catalog, shopping cart, payment integration with Stripe, order management, and admin dashboard.

Key Features:
• User registration and authentication
• Product catalog with search and filtering
• Shopping cart and checkout process
• Payment processing with Stripe
• Order tracking and management
• Admin dashboard for inventory management
• Responsive design for mobile and desktop''',
            'technologies': 'Django, React, PostgreSQL, Redis, Stripe API, Docker, AWS',
            'github_url': 'https://github.com/yourusername/ecommerce-platform',
            'live_url': 'https://your-ecommerce-demo.com',
            'featured': True
        },
        {
            'title': 'Task Management API',
            'description': '''RESTful API for task management application built with Django REST Framework. Includes user authentication, CRUD operations for tasks, team collaboration features, and real-time notifications.

Key Features:
• JWT-based authentication
• CRUD operations for tasks and projects
• Team collaboration and permissions
• Real-time notifications with WebSockets
• File attachments and comments
• API documentation with Swagger
• Comprehensive test coverage''',
            'technologies': 'Django REST Framework, PostgreSQL, Celery, Redis, WebSockets',
            'github_url': 'https://github.com/yourusername/task-api',
            'live_url': 'https://task-api-demo.herokuapp.com',
            'featured': True
        },
        {
            'title': 'Weather Dashboard',
            'description': '''Interactive weather dashboard built with React and Django. Displays current weather conditions, forecasts, and historical data with beautiful visualizations.

Key Features:
• Current weather conditions for any location
• 7-day weather forecast
• Interactive charts and graphs
• Location-based weather alerts
• Historical weather data
• Responsive design
• Dark/light theme toggle''',
            'technologies': 'React, Django, Chart.js, OpenWeather API, Bootstrap',
            'github_url': 'https://github.com/yourusername/weather-dashboard',
            'live_url': 'https://weather-dashboard-demo.netlify.app',
            'featured': True
        },
        {
            'title': 'Blog Platform',
            'description': '''A modern blog platform with content management system. Features include rich text editor, comment system, social sharing, and SEO optimization.

Key Features:
• Rich text editor for content creation
• Comment system with moderation
• Social media sharing integration
• SEO optimization
• Tag and category system
• User profiles and author pages
• Search functionality''',
            'technologies': 'Django, TinyMCE, PostgreSQL, Bootstrap, jQuery',
            'github_url': 'https://github.com/yourusername/blog-platform',
            'featured': False
        },
        {
            'title': 'Portfolio Website',
            'description': '''This very portfolio website you\'re viewing! Built with Django and Bootstrap, featuring a responsive design, admin panel for content management, and optimized for deployment on AWS EC2.

Key Features:
• Responsive design with Bootstrap 5
• Admin panel for content management
• Contact form with email notifications
• Project showcase with filtering
• Skills and experience sections
• SEO optimized
• Production-ready deployment configuration''',
            'technologies': 'Django, Bootstrap, JavaScript, Nginx, Gunicorn, AWS EC2',
            'github_url': 'https://github.com/yourusername/portfolio-website',
            'featured': False
        }
    ]
    
    for project_data in projects_data:
        project, created = Project.objects.get_or_create(
            title=project_data['title'],
            defaults=project_data
        )
        if created:
            print(f"Created project: {project.title}")
        else:
            print(f"Project already exists: {project.title}")

def create_sample_skills():
    """Create sample skills"""
    skills_data = [
        # Programming Languages
        {'name': 'Python', 'proficiency': 90, 'category': 'Programming Languages'},
        {'name': 'JavaScript', 'proficiency': 85, 'category': 'Programming Languages'},
        {'name': 'TypeScript', 'proficiency': 75, 'category': 'Programming Languages'},
        {'name': 'Java', 'proficiency': 70, 'category': 'Programming Languages'},
        {'name': 'SQL', 'proficiency': 80, 'category': 'Programming Languages'},
        
        # Frameworks & Libraries
        {'name': 'Django', 'proficiency': 90, 'category': 'Frameworks & Libraries'},
        {'name': 'Django REST Framework', 'proficiency': 85, 'category': 'Frameworks & Libraries'},
        {'name': 'React', 'proficiency': 80, 'category': 'Frameworks & Libraries'},
        {'name': 'Vue.js', 'proficiency': 70, 'category': 'Frameworks & Libraries'},
        {'name': 'Bootstrap', 'proficiency': 85, 'category': 'Frameworks & Libraries'},
        {'name': 'jQuery', 'proficiency': 75, 'category': 'Frameworks & Libraries'},
        
        # Databases
        {'name': 'PostgreSQL', 'proficiency': 85, 'category': 'Databases'},
        {'name': 'MySQL', 'proficiency': 80, 'category': 'Databases'},
        {'name': 'SQLite', 'proficiency': 90, 'category': 'Databases'},
        {'name': 'Redis', 'proficiency': 70, 'category': 'Databases'},
        {'name': 'MongoDB', 'proficiency': 65, 'category': 'Databases'},
        
        # Tools & Technologies
        {'name': 'Git', 'proficiency': 90, 'category': 'Tools & Technologies'},
        {'name': 'Docker', 'proficiency': 75, 'category': 'Tools & Technologies'},
        {'name': 'AWS', 'proficiency': 70, 'category': 'Tools & Technologies'},
        {'name': 'Nginx', 'proficiency': 75, 'category': 'Tools & Technologies'},
        {'name': 'Linux', 'proficiency': 80, 'category': 'Tools & Technologies'},
        {'name': 'Postman', 'proficiency': 85, 'category': 'Tools & Technologies'},
    ]
    
    for skill_data in skills_data:
        skill, created = Skill.objects.get_or_create(
            name=skill_data['name'],
            defaults=skill_data
        )
        if created:
            print(f"Created skill: {skill.name}")
        else:
            print(f"Skill already exists: {skill.name}")

def create_sample_experience():
    """Create sample work experience"""
    experience_data = [
        {
            'company': 'Tech Solutions Inc.',
            'position': 'Senior Full Stack Developer',
            'description': '''Lead developer responsible for designing and implementing scalable web applications using Django and React. Collaborated with cross-functional teams to deliver high-quality software solutions.

Key Responsibilities:
• Developed and maintained multiple Django-based web applications
• Built responsive frontend interfaces using React and modern JavaScript
• Designed and optimized database schemas for improved performance
• Implemented RESTful APIs and integrated third-party services
• Mentored junior developers and conducted code reviews
• Participated in agile development processes and sprint planning''',
            'start_date': date(2022, 1, 15),
            'end_date': None,  # Current position
            'location': 'San Francisco, CA (Remote)'
        },
        {
            'company': 'Digital Innovations LLC',
            'position': 'Full Stack Developer',
            'description': '''Developed and maintained web applications for various clients using Django, React, and PostgreSQL. Worked closely with designers and project managers to deliver projects on time and within budget.

Key Responsibilities:
• Built custom web applications from requirements to deployment
• Integrated payment gateways and third-party APIs
• Optimized application performance and database queries
• Implemented automated testing and CI/CD pipelines
• Provided technical support and maintenance for existing applications''',
            'start_date': date(2020, 6, 1),
            'end_date': date(2021, 12, 31),
            'location': 'Austin, TX'
        },
        {
            'company': 'StartupXYZ',
            'position': 'Junior Web Developer',
            'description': '''Entry-level position where I gained hands-on experience with web development technologies. Contributed to the development of the company\'s main product and learned best practices in software development.

Key Responsibilities:
• Assisted in developing features for the main web application
• Fixed bugs and implemented minor enhancements
• Wrote unit tests and participated in code reviews
• Collaborated with senior developers on complex features
• Learned and applied modern web development practices''',
            'start_date': date(2019, 8, 1),
            'end_date': date(2020, 5, 31),
            'location': 'New York, NY'
        }
    ]
    
    for exp_data in experience_data:
        experience, created = Experience.objects.get_or_create(
            company=exp_data['company'],
            position=exp_data['position'],
            defaults=exp_data
        )
        if created:
            print(f"Created experience: {experience.position} at {experience.company}")
        else:
            print(f"Experience already exists: {experience.position} at {experience.company}")

def create_sample_education():
    """Create sample education records"""
    education_data = [
        {
            'institution': 'University of Technology',
            'degree': 'Bachelor of Science',
            'field_of_study': 'Computer Science',
            'start_date': date(2015, 9, 1),
            'end_date': date(2019, 5, 31),
            'gpa': 3.75
        },
        {
            'institution': 'Online Learning Platform',
            'degree': 'Certificate',
            'field_of_study': 'Full Stack Web Development',
            'start_date': date(2019, 1, 1),
            'end_date': date(2019, 6, 30),
            'gpa': None
        },
        {
            'institution': 'AWS Training Center',
            'degree': 'AWS Certified Solutions Architect',
            'field_of_study': 'Cloud Computing',
            'start_date': date(2021, 3, 1),
            'end_date': date(2021, 4, 30),
            'gpa': None
        }
    ]
    
    for edu_data in education_data:
        education, created = Education.objects.get_or_create(
            institution=edu_data['institution'],
            degree=edu_data['degree'],
            field_of_study=edu_data['field_of_study'],
            defaults=edu_data
        )
        if created:
            print(f"Created education: {education.degree} from {education.institution}")
        else:
            print(f"Education already exists: {education.degree} from {education.institution}")

def main():
    """Main function to populate all sample data"""
    print("Populating sample data for Portfolio Django App...")
    print("=" * 50)
    
    print("\nCreating sample projects...")
    create_sample_projects()
    
    print("\nCreating sample skills...")
    create_sample_skills()
    
    print("\nCreating sample experience...")
    create_sample_experience()
    
    print("\nCreating sample education...")
    create_sample_education()
    
    print("\n" + "=" * 50)
    print("Sample data population completed!")
    print("\nYou can now:")
    print("1. Visit the admin panel to modify the data")
    print("2. Run the development server to see your portfolio")
    print("3. Add your own images and customize the content")
    print("\nAdmin panel: http://127.0.0.1:8000/admin/")
    print("Username: admin")
    print("Password: admin123")

if __name__ == '__main__':
    main()
