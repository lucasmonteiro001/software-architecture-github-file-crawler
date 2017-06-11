web:
  build: containers/web/.
  environment:
    - VIRTUAL_HOST={{PROJECT_NGINX_PROXY_VIRTUAL_HOSTS}}
{{#PRODUCTION}}
    - LETSENCRYPT_HOST={{PROJECT_NGINX_PROXY_VIRTUAL_HOSTS}}
    - LETSENCRYPT_EMAIL={{PROJECT_LETSENCRYPT_EMAIL}}
{{/PRODUCTION}}
  {{#DEVELOPMENT}}volumes:
    - ./containers/web/html:/usr/share/nginx/html{{/DEVELOPMENT}}
  log_driver: {{PROJECT_DOCKER_LOG_DRIVER}}
{{#PRODUCTION}}
  restart: always
{{/PRODUCTION}}

# vim:syntax=yaml
