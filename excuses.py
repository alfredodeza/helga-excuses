from helga.extensions.base import (CommandExtension,
                                   ContextualExtension)
from helga.log import setup_logger
from BeautifulSoup import BeautifulSoup
import requests


logger = setup_logger(__name__)


class ExcusesExtension(CommandExtension):

    NAME = 'excuses'

    usage = '[BOTNICK] excuses'

    allow_many = True

    def handle_message(self, opts, message):
        response = requests.get('http://developerexcuses.com/')
        soup = BeautifulSoup(response.text)
        elem = soup.find('a')
        message.response = elem.text.encode('ascii', 'ignore')
