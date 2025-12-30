# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePdnsAppKeyRequest(DaraModel):
    def __init__(
        self,
        app_key_id: str = None,
        auth_code: str = None,
        lang: str = None,
    ):
        self.app_key_id = app_key_id
        self.auth_code = auth_code
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key_id is not None:
            result['AppKeyId'] = self.app_key_id

        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKeyId') is not None:
            self.app_key_id = m.get('AppKeyId')

        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

