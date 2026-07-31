# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class UserSummaryModel(DaraModel):
    def __init__(
        self,
        access_tokens: List[main_models.AccessTokenModel] = None,
        host: str = None,
        ram_user: str = None,
        status: str = None,
        user_name: str = None,
    ):
        self.access_tokens = access_tokens
        self.host = host
        self.ram_user = ram_user
        self.status = status
        self.user_name = user_name

    def validate(self):
        if self.access_tokens:
            for v1 in self.access_tokens:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessTokens'] = []
        if self.access_tokens is not None:
            for k1 in self.access_tokens:
                result['AccessTokens'].append(k1.to_map() if k1 else None)

        if self.host is not None:
            result['Host'] = self.host

        if self.ram_user is not None:
            result['RamUser'] = self.ram_user

        if self.status is not None:
            result['Status'] = self.status

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_tokens = []
        if m.get('AccessTokens') is not None:
            for k1 in m.get('AccessTokens'):
                temp_model = main_models.AccessTokenModel()
                self.access_tokens.append(temp_model.from_map(k1))

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('RamUser') is not None:
            self.ram_user = m.get('RamUser')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

