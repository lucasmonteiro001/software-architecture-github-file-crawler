openvpn:
  image: dperson/openvpn-client
  cap_add:
    - NET_ADMIN
  devices:
    - "/dev/net/tun"
  dns:
    - 8.8.4.4
    - 8.8.8.8
  restart: always
  log_driver: journald
  volumes:
    - ./vpn:/vpn
{{#PROJECT_OPENVPN_COMMAND}}
  command: {{PROJECT_OPENVPN_COMMAND}}
{{/PROJECT_OPENVPN_COMMAND}}
transmission:
  image: dperson/transmission  
  log_driver: journald
  net: "container:openvpn"
  restart: always
  volumes:
    - {{PROJECT_DOWNLOAD_DIR}}:/var/lib/transmission-daemon/downloads
    - {{PROJECT_INCOMPLETE_DOWNLOAD_DIR}}:/var/lib/transmission-daemon/incomplete
    - {{PROJECT_TRANSMISSION_CONFIG_DIR}}:/var/lib/transmission-daemon
  environment:
    - USERID={{PROJECT_USERID}}
    - GROUPID={{PROJECT_GROUPID}}
transmission-proxy:
  image: dperson/nginx
  log_driver: journald
  links:
    - transmission
  command: -w "http://transmission:9091/transmission;/transmission"
  ports:
    - "{{PROJECT_PROXY_PORT}}:80"
  restart: always

# vi: set tabstop=2 expandtab syntax=yaml:
