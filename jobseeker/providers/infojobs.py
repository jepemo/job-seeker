# -*- coding: utf-8 -*-
# jobseeker - Basic job offer advisor
#
# Copyright (C) 2018-present Jeremies Pérez Morata
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
from bs4 import BeautifulSoup
from jobseeker.providers.provider import Provider
from urllib.parse import urlencode, quote_plus

class InfojobsProvider(Provider):
    URL='https://api.infojobs.net/api/1/offer?{0}'
    def __init__(self, client_id, client_secret):
        super().__init__()

        self.client_id = client_id
        self.client_secret = client_secret

    def search(self, terms):
        offers = []

        payload = {
            'q': terms,
            'province': 'valencia-valencia',
            'radius': '50',
            'order': 'updated-desc'
        }
        params = urlencode(payload, quote_via=quote_plus)

        r = requests.get(self.URL.format(params), auth=(self.client_id, self.client_secret))

        json_result = r.json()
        for offer in json_result["offers"]:
            offers.append({
                'title': offer['title'],
                'city': offer['city'],
                'link': offer['link'],
            })

        return offers
