file { '/path/to/configuration/file':
  ensure  => file,
  content => template('module_name/file.erb'),
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure => running,
  enable => true,
}
