# Installs and configures an Nginx server using Puppet
# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request (requesting a page) using curl,\
#      it must return a page that contains the string Hello World!
# The redirection must be a “301 Moved Permanently”
# Answer file should be a Puppet manifest containing commands to automatically \
#      configure an Ubuntu machine to respect above requirements

exec { 'update system':
  command => '/usr/bin/sudo apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'redirect_me':
  command  => 'sed -i "24i\     rewrite ^/redirect_me https://www.youtube.com/watch?v=vYqLz3GVN4Q&t=295s permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
