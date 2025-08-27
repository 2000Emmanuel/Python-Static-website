from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Experience, Education, Contact
from .forms import ContactForm

def home(request):
    """Home page view with featured projects and skills"""
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()
    recent_experience = Experience.objects.first()
    
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
        'recent_experience': recent_experience,
    }
    return render(request, 'main/home.html', context)

def about(request):
    """About page with experience and education"""
    experiences = Experience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'experiences': experiences,
        'education': education,
        'skills': skills,
    }
    return render(request, 'main/about.html', context)

def projects(request):
    """Projects page showing all projects"""
    all_projects = Project.objects.all()
    
    context = {
        'projects': all_projects,
    }
    return render(request, 'main/projects.html', context)

def project_detail(request, pk):
    """Individual project detail page"""
    project = get_object_or_404(Project, pk=pk)
    
    context = {
        'project': project,
    }
    return render(request, 'main/project_detail.html', context)

def contact(request):
    """Contact page with contact form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact_message = form.save()
            
            # Send email notification (optional)
            try:
                send_mail(
                    subject=f"Portfolio Contact: {contact_message.subject}",
                    message=f"From: {contact_message.name} ({contact_message.email})\n\n{contact_message.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['your-email@example.com'],  # Replace with your email
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
            
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'main/contact.html', context)
