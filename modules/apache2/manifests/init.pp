class apache2 {
	
	package { 'apache2':
		ensure => latest,
	}
	
	service { 'apache2':
		subscribe => File[apacheconfig],
		require => Package[apache2],
		ensure => 'running',
		enable => 'true',
	}

	file { 'apacheconfig':
		name => '/etc/apache2/apache2.conf',
		owner => root,
		group => root,
		mode => 644,
		source => 'puppet://modules/apache2/apache2.conf,
		require => Package[apache2],
		notify => Service[apache2],
	}
}
