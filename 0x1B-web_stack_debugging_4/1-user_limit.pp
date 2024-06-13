# Change the OS configuration so that it is possible to login
#   with the holberton user and open a file without any error message

exec { 'fix--reads-holbertonuser':
  path     =>  '/bin',
  provider =>  shell,
  command  =>  'sed -i \'/holberton/c\\\' /etc/security/limits.conf'
}
