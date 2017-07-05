class apache2 {
	
	package { 'httpd':
		ensure => latest,
	}
	
	service { 'httpd':
		subscribe => File["apacheconfig"],
		require => Package["httpd"],
		ensure => 'running',
		enable => 'true',
	}

	file { 'apacheconfig':
		name => '/etc/httpd/conf/httpd.conf',
		owner => root,
		group => root,
		mode => 644,
		source => 'puppet://modules/apache2/httpd.conf',
		require => Package["httpd"],
		notify => Service["httpd"],
	}
}
