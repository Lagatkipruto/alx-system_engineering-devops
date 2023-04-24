# installing puppet-lint -v 2.1.0
# First installing python3

# Declare the pip3 package provider
Package { provider => pip3 }

# Install Flask version 2.1.0
package { 'flask':
  ensure => '2.1.0',
}
