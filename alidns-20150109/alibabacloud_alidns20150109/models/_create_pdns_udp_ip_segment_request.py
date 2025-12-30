# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePdnsUdpIpSegmentRequest(DaraModel):
    def __init__(
        self,
        ip: str = None,
        ip_token: str = None,
        lang: str = None,
        name: str = None,
    ):
        self.ip = ip
        self.ip_token = ip_token
        self.lang = lang
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ip_token is not None:
            result['IpToken'] = self.ip_token

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IpToken') is not None:
            self.ip_token = m.get('IpToken')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

