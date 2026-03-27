# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class MergeContact(DaraModel):
    def __init__(
        self,
        email: str = None,
        email_verify: bool = None,
        extend: Dict[str, Any] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        identifier: str = None,
        lang: str = None,
        name: str = None,
        phone: str = None,
        phone_code: str = None,
        phone_verify: bool = None,
        source: str = None,
    ):
        self.email = email
        self.email_verify = email_verify
        self.extend = extend
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.identifier = identifier
        self.lang = lang
        self.name = name
        self.phone = phone
        self.phone_code = phone_code
        self.phone_verify = phone_verify
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['email'] = self.email

        if self.email_verify is not None:
            result['emailVerify'] = self.email_verify

        if self.extend is not None:
            result['extend'] = self.extend

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.identifier is not None:
            result['identifier'] = self.identifier

        if self.lang is not None:
            result['lang'] = self.lang

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.phone_code is not None:
            result['phoneCode'] = self.phone_code

        if self.phone_verify is not None:
            result['phoneVerify'] = self.phone_verify

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('emailVerify') is not None:
            self.email_verify = m.get('emailVerify')

        if m.get('extend') is not None:
            self.extend = m.get('extend')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('phoneCode') is not None:
            self.phone_code = m.get('phoneCode')

        if m.get('phoneVerify') is not None:
            self.phone_verify = m.get('phoneVerify')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

