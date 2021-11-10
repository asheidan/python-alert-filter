#!/usr/bin/env python3

import argparse
import sys

import exchangelib


def main() -> None:
    username: str = ""
    password: str = ""
    server: str = "outlook.office365.com"

    credentials = exchangelib.Credentials(username=username, password=password)
    config = exchangelib.Configuration(server=server, credentials=credentials)
    account = exchangelib.Account(
        primary_smtp_address=username,
        config=config,
        autodiscover=False,
        access_type=exchangelib.DELEGATE,
    )

    alert_folder = account.root / "Top of Information Store" / "Alerts"
    for message in alert_folder.all():
        print(message.subject)


if __name__ == "__main__":
    main()
