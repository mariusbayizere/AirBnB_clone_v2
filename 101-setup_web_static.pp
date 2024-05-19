# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Create web_static directory
file { '/data/web_static':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create releases and shared directories
file { ['/data/web_static/releases', '/data/web_static/shared']:
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

# Create symbolic link 'current'
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'root',
  group  => 'root',
  mode   => '0777',
}

# Create index.html in releases/test directory
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Configure nginx to serve the content
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}
",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable the configuration and restart nginx
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Restart nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}
