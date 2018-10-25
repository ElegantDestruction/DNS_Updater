#!/usr/bin/env python3

import socket
import boto3
import os

HOME = os.getenv("HOME")

# Function to update .jackhil.de subdomains 
# subdomain must be full domain name (ie `books.jackhil.de`)
# ip can be more than one ip. comma seperated but don't?
def update_dns(subdomain, ip):
  client = boto3.client('route53')
  response = client.change_resource_record_sets(
      HostedZoneId='Z3MDEXKPR2M7K7',
      ChangeBatch={
          'Changes': [
              {
                  'Action': 'UPSERT',
                  'ResourceRecordSet': {
                      'Name': subdomain,
                      'Type': 'A',
                      'TTL': 300,
                      'ResourceRecords': [
                          {
                              'Value': ip
                          },
                      ]
                  }
              },
          ]
      }
    )


# Function to display hostname and
# IP address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    print('IP reported from google \'{}\'.'.format(ip_address))
    s.close()
    current_ip = "127.0.0.1"
    try:
        current_file = open(HOME + '/.config/dns-update/current_address','r')
        current_ip = current_file.read()
        current_ip = current_ip.strip()
        current_file.close()
    except:
        print("No previous ip.")

    if (ip_address != current_ip):
        return ip_address
    else:
        return 'null'


def save_ip(ip_address):
    overwrite = open(HOME + '/.config/dns-update/current_address','w')
    overwrite.write(ip_address)
    overwrite.close()


def main():
    config = open(HOME + '/.config/dns-update/config', 'r')
    ip = get_ip()
    
    if ip is not 'null':
        for domain in config:
            print('Updating {} with new IP {}.'.format(domain.strip(), ip))
            update_dns(domain.strip(), ip)
        save_ip(ip)
    else:
        print('No need to update. Bailling.') 
    config.close()


if __name__ == '__main__':
    main()

