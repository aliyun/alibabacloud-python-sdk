# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTicketRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        content: str = None,
        email: str = None,
        language: str = None,
        notify_time_range: str = None,
        phone: str = None,
        product_code: str = None,
        secret_content: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.category = category
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.email = email
        self.language = language
        self.notify_time_range = notify_time_range
        self.phone = phone
        # This parameter is required.
        self.product_code = product_code
        self.secret_content = secret_content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.content is not None:
            result['Content'] = self.content

        if self.email is not None:
            result['Email'] = self.email

        if self.language is not None:
            result['Language'] = self.language

        if self.notify_time_range is not None:
            result['NotifyTimeRange'] = self.notify_time_range

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.secret_content is not None:
            result['SecretContent'] = self.secret_content

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('NotifyTimeRange') is not None:
            self.notify_time_range = m.get('NotifyTimeRange')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SecretContent') is not None:
            self.secret_content = m.get('SecretContent')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

