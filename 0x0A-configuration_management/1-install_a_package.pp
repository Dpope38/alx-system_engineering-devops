#Install flask "a python web application library" and pip3

class { 'python::pip':
  ensure  => 'present',
}

python::pip { 'flask':
  ensure  => '2.1.0',
  require => Class['python::pip'],
}
