#Creates a manifest that kills a process named killmenow

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'], # Specify the path for the pkill command
  refreshonly => true,                # Only run the command when notified by another resource
}
