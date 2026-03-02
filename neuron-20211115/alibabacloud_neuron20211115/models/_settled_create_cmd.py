# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SettledCreateCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        application: str = None,
        developer_name: str = None,
        email: str = None,
        enterprise_name: str = None,
        phone: str = None,
        usage: str = None,
    ):
        self.account_id = account_id
        self.application = application
        self.developer_name = developer_name
        self.email = email
        self.enterprise_name = enterprise_name
        self.phone = phone
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.application is not None:
            result['application'] = self.application

        if self.developer_name is not None:
            result['developerName'] = self.developer_name

        if self.email is not None:
            result['email'] = self.email

        if self.enterprise_name is not None:
            result['enterpriseName'] = self.enterprise_name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('application') is not None:
            self.application = m.get('application')

        if m.get('developerName') is not None:
            self.developer_name = m.get('developerName')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('enterpriseName') is not None:
            self.enterprise_name = m.get('enterpriseName')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

