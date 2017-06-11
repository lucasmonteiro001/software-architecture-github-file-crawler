php:
  build: containers/php/.
  volumes_from:
    - source
{{#PRODUCTION}}
  restart: always
{{/PRODUCTION}}
nginx:
  build: containers/nginx/.
  links:
    - php
  volumes_from:
    - source
  environment:
    - VIRTUAL_HOST={{PROJECT_NGINX_PROXY_VIRTUAL_HOSTS}}
{{#PRODUCTION}}
  restart: always
{{/PRODUCTION}}
# Data containers
source:
  build: containers/source/.
  volumes:
    - {{#DEVELOPMENT}}./containers/source/http:{{/DEVELOPMENT}}/srv/http/source
  command: "true"

# vim:syntax=yaml
