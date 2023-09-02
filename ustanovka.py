import os
  
install_httpd = """
sudo yes y | yum install httpd
sudo systemctl start httpd
sudo systemctl enable httpd.service
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload
systemctl status httpd
"""
os.system(install_httpd)

# os.system("yes y | yum install httpd")

# os.system("yes y | yum install mysql")
