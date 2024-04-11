# this code fix a 500 error returning from apache

exec { 'fix my error':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => 'shell'
}
