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
    URL='https://www.infojobs.net/jobsearch/search-results/list.xhtml#f1=1&item_showFilters=false&item_showExtraFilters=false&f2=20&{0}&f4=&f5=&f6=49&f7=&f8=0&f9=0&f10=0&f11=1&f12=&f13=true&f14=true&f15=10&f16=false&f17=&f18=&f19=&f20=0&f21=3012&f22=0&f23=-2147483648&f24=&f25=&f26=&f27=false&f28=&f29=1&f30=&f31=-2147483648&f32=-2147483648&f34=&item_vieneUrlExecutive=false&item_id_push=&f35=false&ajax=true&formId=form_relaunch'
    def __init__(self):
        super().__init__()

    def search(self, terms):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        }
        payload = {'f3': terms}
        result = urlencode(payload, quote_via=quote_plus)
        r = requests.get(self.URL.format(result), headers=headers)

        soup = BeautifulSoup(r.text, 'html.parser')

        #offer_list = soup.find(id="offer-list")
        #for child in offer_list.children:
        #    print(child)

        return r.text
