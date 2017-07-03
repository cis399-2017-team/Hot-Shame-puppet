node ip-10-0-4-70 {
    cron { "puppet update":
	command => "cd /etc/puppet && git pull -q origin master",
	user    => root,
	minute  => "*/5",
    }
    include sshd,
}

node ip-10-0-4-10 {
    include sshd,
    include apache2,
}

node ip-10-0-4-8 {
    include sshd,
    include apache2,
}
