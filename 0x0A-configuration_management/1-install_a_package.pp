#Install flask "a python web application library" and pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['/usr/bin'],
  environment => [],
  require     => Package['python3-pip'],
}
