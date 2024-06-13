# Tests how well the web server setup featuring Nginx is doing under pressure
# Increments the ngix limit

exec {'fix--files-limit-setting':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  path    => '/bin',
}
