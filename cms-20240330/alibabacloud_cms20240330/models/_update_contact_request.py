# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class UpdateContactRequest(DaraModel):
    def __init__(
        self,
        email: str = None,
        im_user_ids: Dict[str, str] = None,
        lang: str = None,
        name: str = None,
        phone: str = None,
        phone_code: str = None,
    ):
        # The email address of the contact.
        self.email = email
        # The instant messaging (IM) user ID mappings. Multiple IM tools are supported.
        self.im_user_ids = im_user_ids
        # The language.
        self.lang = lang
        # The name of the contact.
        self.name = name
        # The mobile phone number of the contact. Only Chinese mobile phone numbers are supported.
        self.phone = phone
        # The country code for the mobile phone number, typically +86 for China.
        self.phone_code = phone_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['email'] = self.email

        if self.im_user_ids is not None:
            result['imUserIds'] = self.im_user_ids

        if self.lang is not None:
            result['lang'] = self.lang

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.phone_code is not None:
            result['phoneCode'] = self.phone_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('imUserIds') is not None:
            self.im_user_ids = m.get('imUserIds')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('phoneCode') is not None:
            self.phone_code = m.get('phoneCode')

        return self

