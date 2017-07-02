
##TODO I'm not certain that this allows puppet to update ssh_config(6.3)
##I'm also not certain that this is how you add ssh keys(6.4) further testing needed

class sshd {
	
	package { 'openssh-server':
		ensure => latest
	}

	service { 'sshd':
		subscribe => File[sshdconfig],
		require => Package['openssh-server'],
		ensure => 'running',
		enable => true
	}
	
	file { 'sshdconfig':
		name => 'etc/ssh/sshd_config',
		owner => root,
		group => root,
		mode => 644,
		source => 'puppet:///modules/sshd/sshd_config',
		require => Package['openssh-server'],
		notify => Service[sshd]
	}
	
	ssh_authorized_key { 'jdolan':
		user => 'ec2-user',
		key => 'AAAAB3NzaC1yc2EAAAADAQABAAABAQCzQ9y1oCy32mSQNuxr6ti9aE02mf1TV4DnWAMkHrBhrgzwF6ycLrqkTqUA0gOaWX9AlvgotVNMVgpHicM0QM5BCD1eLai1MKBewhqTzw9hnpaf9OugdWCSQtC7Jc9M0sYFCp6kdLCRHyvUvnb74jQXFA4EiXO1bLfnIbTCcHNvQDdymyEnfHD/Q5JeNm+DqaN4ZqcMqzlnWM27+/m312nn1KEIWpRANWJBJSBIFvXWS4YmrbFZN7WkRYy1GJisGRhk4PaHFQOZJJ26Im8URBhKhPlQwJljIU8kuboQ/2ASrboBPSYOV3Cmoh1PETjeu2OXag1shUlUaSatqBb/t+uF'
	}

	ssh_authorized_key { 'houllette':
		user => 'ec2-user',
		key => 'AAAAB3NzaC1yc2EAAAADAQABAAABAQCVs/6140OKWU4CBCR8H/eDSxeAOhlyQzuv6X4xv4PxW0425s5Rz/pXKPv5OfZdA0WTBEBCHkrxC2Kn2n7IId25kqhckI5T6W0F3LLcmFXkE5kxzbGICgeXRHAewozv8TrK3pbMIJCbnTEnkqXkf72FFuog36GbbHuKE60qCYrF5h4oQ6gfXvBfhjxusfb4hdi3H84dQrG4IK9yyr5o2U1b5cV4kP/jt9wjiZapWSxcvbvsgftRdTrRx5Bru0Jfn+bKcPH9UKFplDQTC0HbCzPQ5242J9vt/wBubPPdevw1SukvdOAIE8tXSZhmJodNkmBLOZy+NXjK7cXxFcdGeCwd'
	}
}
