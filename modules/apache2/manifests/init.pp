class apache2 {
	
	package { 'httpd':
		ensure => latest,
	}
	
	service { 'httpd':
		require => Package["httpd"],
		ensure => 'running',
		enable => 'true',
		#subscribe => File["/etc/httpd/conf/httpd.conf"],
	}

	file { '/etc/httpd/conf/httpd.conf':
		owner => root,
		group => root,
		mode => 644,
		source => 'puppet:///modules/apache2/httpd.conf',
		require => Package["httpd"],
		#notify => Service["httpd"],
	}
}
