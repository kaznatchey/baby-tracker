import os

install_httpd = """
sudo yes y | sudo yum install httpd
sudo systemctl start httpd
sudo systemctl enable httpd.service
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload
echo 'finished firewall'
sudo chmod -R 775 /var/www/html/
sudo chown -R cloud_user:cloud_user /var/www/html/
sudo chown -R cloud_user:cloud_user /var/www/
echo 'finished chown -R cloud_user:cloud_user /var/www/'
ls -al /var/www/html/
sudo yes y | sudo yum install php
echo 'installed php'
chcon -R -t httpd_sys_content_t /var/www/html
chcon -R -t httpd_sys_rw_content_t /var/www/html
chmod 777 newfile.txt
chmod 777 welcome.php
"""
return_value = os.system(install_httpd)
print(return_value)

configFile = open("/etc/httpd/conf/httpd.conf", "a")  # append mode
configFile.write("# PHP 7 specific configuration \n")
configFile.close()
