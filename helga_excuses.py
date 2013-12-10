import requests
from BeautifulSoup import BeautifulSoup

from helga.plugins import command


@command('excuses', aliases=['excuse'],
         help='Show something from developer excuses. Usage: helga (excuses|excuse)')
def excuses(client, channel, nick, message, cmd, args):
    response = requests.get('http://developerexcuses.com/')
    return BeautifulSoup(response.text).find('a').text.encode('ascii', 'ignore')
