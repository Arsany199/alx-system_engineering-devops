# this file increase the amount of traffic of a server can handle
exec { 'limit to 2000':
  command => "sed -i 's/15/2000' etc/default/nginx",
  path    => '/bin'
}

exec { 'nginx restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
