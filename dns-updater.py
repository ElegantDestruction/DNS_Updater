#!/usr/bin/env python3

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import socket
import boto3
import os

# Function to update .jackhil.de subdomains
# subdomain must be full domain name (ie `books.jackhil.de`)
# ip can be more than one ip. comma seperated but don't?
def update_dns(subdomain, ip):
  client = boto3.client('route53')
  print(ip)
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
    ip_address = str(urlopen('http://ip.42.pl/raw').read()).replace("'", '').replace('b','')
    current_ip = "127.0.0.1"
    try:
        current_file = open('/var/lib/dns-update/current_address','r')
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
    overwrite = open('/var/lib/dns-update/current_address','w')
    overwrite.write(ip_address)
    overwrite.close()


def main():
    config = open('/etc/dns-update/config', 'r')
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
