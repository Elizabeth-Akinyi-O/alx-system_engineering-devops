# Using Puppet to configure SSH configuration file so that you can connect to a server without typing a password
# Requirements:
#   Your SSH client configuration must be configured to use the private key ~/.ssh/school
#   Your SSH client configuration must be configured to refuse to authenticate using a password

file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
