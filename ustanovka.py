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

php_config = """
# PHP 7 specific configuration
<IfModule php7_module>
    AddType application/x-httpd-php .php
    AddType application/x-httpd-php-source .phps
    <IfModule dir_module>
        DirectoryIndex index.html index.php
    </IfModule>
</IfModule>
"""

configFile = open("/etc/httpd/conf/httpd.conf", "a")  # append mode
configFile.write(php_config)
# configFile.write("# PHP 7 specific configuration \n")
# configFile.write("<IfModule php7_module> \n")
# configFile.write("    AddType application/x-httpd-php .php \n")
# configFile.write("    AddType application/x-httpd-php-source .phps \n")
# configFile.write("    <IfModule dir_module> \n")
# configFile.write("        DirectoryIndex index.html index.php \n")
# configFile.write("    </IfModule> \n")
# configFile.write("</IfModule> \n")
configFile.close()
