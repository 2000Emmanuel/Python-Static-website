#!/bin/bash

# Portfolio Django App Deployment Script for AWS EC2
# Run this script on your EC2 instance after uploading your code

set -e

echo "Starting deployment of Portfolio Django App..."

# Update system packages
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install required system packages
echo "Installing system dependencies..."
sudo apt install -y python3 python3-pip python3-venv nginx supervisor git

# Create application directory
APP_DIR="/home/ubuntu/Python-Static-website"
echo "Setting up application directory: $APP_DIR"

# Create necessary directories
sudo mkdir -p /var/log/gunicorn
sudo mkdir -p /var/run/gunicorn

# Set up virtual environment
echo "Setting up Python virtual environment..."
cd $APP_DIR
python3 -m venv emma-venv
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Set environment variables
echo "Setting up environment variables..."
export SECRET_KEY="your-secret-key-here-change-this-in-production"
export DEBUG="False"

# Run Django setup
echo "Running Django setup..."
python manage.py collectstatic --noinput
python manage.py migrate

# Create superuser (optional - you can do this manually later)
# echo "Creating Django superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', '07061246263')" | python manage.py shell

# Set up Gunicorn service
echo "Setting up Gunicorn service..."
sudo cp portfolio.service /etc/systemd/system/
sudo systemctl daemon-reload 
sudo systemctl enable portfolio


# Set up Nginx
echo "Setting up Nginx..."
sudo cp nginx.conf /etc/nginx/sites-available/portfolio
sudo ln -sf /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

# Test Nginx configuration
sudo nginx -t

# Restart services
echo "Restarting services..."
sudo systemctl restart nginx
sudo systemctl restart portfolio

# Set proper permissions
echo "Setting file permissions..."
sudo chown -R www-data:www-data $APP_DIR
sudo chmod -R 755 $APP_DIR

# Create log directories
sudo mkdir -p /var/log/portfolio
sudo chown -R www-data:www-data /var/log/portfolio

echo "Deployment completed successfully!"
echo ""
echo "Your Django app should now be running on your EC2 instance."
echo "You can check the status with:"
echo "  sudo systemctl status portfolio"
echo "  sudo systemctl status nginx"
echo ""
echo "View logs with:"
echo "  sudo journalctl -u portfolio -f"
echo "  sudo tail -f /var/log/nginx/error.log"
echo ""
echo "Don't forget to:"
echo "1. Update your domain name in the Nginx configuration"
echo "2. Set up SSL with Let's Encrypt (certbot)"
echo "3. Configure your security groups to allow HTTP/HTTPS traffic"
echo "4. Update ALLOWED_HOSTS in Django settings with your domain"
