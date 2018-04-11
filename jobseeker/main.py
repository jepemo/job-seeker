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

import json
import time
import smtplib
from email.message import EmailMessage
from jobseeker.providers import create_providers

all_offers = []

def get_new_offers(offers):
    new_offers = []
    for offer in offers:
        exists = False
        for all_offer in all_offers:
            if all_offer["link"] == offer["link"]:
                exists = True
                break

        if not exists:
            new_offers.append(offer)

    # Update global dict
    all_offers.extend(new_offers)

    return new_offers

def send_offers(mail_info, to_send, offers):
    data = ""

    for offer in offers:
        data += "Title: %s\n" % offer["title"]
        data += "City: %s\n" % offer["city"]
        data += "Link: %s\n\n\n" % offer["link"]

    print(">> Content mail:\n", data)

    msg = EmailMessage()
    msg.set_content(data)

    msg['Subject'] = '[JOBSEEKER] Job Digest (%s)' % time.strftime("%c")
    msg['From'] = mail_info["smtp_from"]
    msg['To'] = to_send

    s = smtplib.SMTP(mail_info["smtp_host"], mail_info["smtp_port"])
    s.ehlo()
    s.starttls()
    s.login(mail_info["smtp_user"], mail_info["smtp_pass"])
    s.send_message(msg)
    s.quit()

def load_config(config_path):
    with open(config_path) as cin:
        content = cin.read()
        print("Conf. content:", content)
        return json.loads(content)

def main():
    print("[*] Start job seeker")

    config = load_config("./config.json")
    providers = create_providers(config["providers"])
    mail_info = config["mail_info"]

    offers = []

    job_lists = config["job_list"]

    while True:
        for job_list in job_lists:
            print("> Downloading offers for", job_list["name"])
            for provider_name in job_list["providers"]:
                print(">> For provider", provider_name)
                provider = providers[provider_name]
                for term in job_list["search_terms"]:
                    print(">>> Searching", term)
                    offers_result = provider.search(term)
                    print(">>>>", len(offers_result), "results")
                    offers.extend(offers_result)
                    time.sleep(5)

            new_offers = get_new_offers(offers)

            if len(new_offers) > 0:
                to_send = job_list["send_mail"]
                print("> Send offers to", to_send)
                send_offers(mail_info, to_send, new_offers)
            else:
                print("> Nothing to send...")

        print(">> Waiting....")
        time.sleep(300)
