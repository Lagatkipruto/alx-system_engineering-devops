# Manifest that kills the process named killmenow using pkill.

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
  user    => 'root',
}
