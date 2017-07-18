class html {
	
	file { '/var/www/html':
		owner => root,
		group => root,
		mode => 644,
		source => 'puppet:///modules/html/html',
		ensure => directory,
		recurse => remote,
	}
}
