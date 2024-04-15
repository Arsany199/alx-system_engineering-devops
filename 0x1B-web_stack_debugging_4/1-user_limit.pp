# holberton user can login without any errors
exec { 'increase hard limit':
  command => "sed -i "s/5/2000" /etc/security/limits.conf",
  path    => "/bin"
}

exec { 'increase soft limit':
  command => "sed -i "s/4/2000" /etc/security/limits.conf",
  path    => "/bin"
}
