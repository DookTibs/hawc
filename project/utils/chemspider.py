import re
import logging
import xml.etree.ElementTree as ET

from django.conf import settings

import requests


logger = logging.getLogger(__name__)


def fetch_chemspider(cas_number):
    d = {}
    try:
        # get chemspider chem id
        url = 'https://www.chemspider.com/Search.asmx/SimpleSearch'
        payload = {
            'query': cas_number,
            'token': settings.CHEMSPIDER_TOKEN,
        }
        r = requests.post(url, data=payload)
        id_val = re.search(r'\<int\>(\d+)\</int\>', r.text).group(1)

        # get details
        url = 'https://www.chemspider.com/MassSpecAPI.asmx/GetExtendedCompoundInfo'  # noqa
        payload = {
            'CSID': id_val,
            'token': settings.CHEMSPIDER_TOKEN,
        }
        r = requests.post(url, data=payload)
        xml = ET.fromstring(r.text)
        namespace = '{http://www.chemspider.com/}'
        d['CommonName'] = xml.find('{}CommonName'.format(namespace)).text
        d['SMILES'] = xml.find('{}SMILES'.format(namespace)).text
        d['MW'] = xml.find('{}MolecularWeight'.format(namespace)).text

        # get image
        url = 'https://www.chemspider.com/Search.asmx/GetCompoundThumbnail'
        payload = {
            'id': id_val,
            'token': settings.CHEMSPIDER_TOKEN,
        }
        r = requests.post(url, data=payload)
        xml = ET.fromstring(r.text)
        d['image'] = xml.text

        # call it a success if we made it here
        d['status'] = 'success'

    except AttributeError as e:
        logger.error(f"Request failed: {r.text}", exc_info=True)

    except Exception as e:
        logger.error(str(e), exc_info=True)

    return d
