# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WhoisProtectionRequest(DaraModel):
    def __init__(
        self,
        data_content: str = None,
        data_source: int = None,
        lang: str = None,
        user_client_ip: str = None,
        whois_protect: bool = None,
    ):
        # This parameter is required.
        self.data_content = data_content
        # This parameter is required.
        self.data_source = data_source
        self.lang = lang
        self.user_client_ip = user_client_ip
        # This parameter is required.
        self.whois_protect = whois_protect

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_content is not None:
            result['DataContent'] = self.data_content

        if self.data_source is not None:
            result['DataSource'] = self.data_source

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.whois_protect is not None:
            result['WhoisProtect'] = self.whois_protect

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataContent') is not None:
            self.data_content = m.get('DataContent')

        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('WhoisProtect') is not None:
            self.whois_protect = m.get('WhoisProtect')

        return self

