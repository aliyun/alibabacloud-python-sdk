# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRegionsRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        security_token: str = None,
    ):
        # The language in which you want to return the descriptions of the access control policies. Valid values:
        # 
        # *   zh-CN (default value): Chinese
        # *   en: English
        # *   ja: Japanese
        self.language = language
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

