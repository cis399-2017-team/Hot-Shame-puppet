node ip-10-0-4-70 {
    include sshd
    cron { "puppet update":
	command => "cd /etc/puppet && git pull -q origin master",
	user    => root,
	minute  => "*/5",
    }
}

node ip-10-0-4-10 {
    #dead server
    include sshd
    include apache2
}

node ip-10-0-4-8 {
    include sshd
    include apache2
    include html
}

node ip-10-0-4-84 {
    include sshd
    include apache2
    include html
}
