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

class Provider(object):
    def __init__(self):
        pass

    def search(self, terms):
        raise Exception("Not implemented")



"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}
r = requests.get(self.URL.format(params), headers=headers)

print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
offer_list = soup.find(id="offer-list")
for child in offer_list.children:
    print(child)
"""
