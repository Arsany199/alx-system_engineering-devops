#!/usr/bin/pup
# Installing an especific version of flask
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
