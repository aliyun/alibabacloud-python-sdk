# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDnsGtmAddrAttributeInfoRequest(DaraModel):
    def __init__(
        self,
        addrs: str = None,
        lang: str = None,
        type: str = None,
    ):
        # The addresses.
        # 
        # This parameter is required.
        self.addrs = addrs
        # The language of the values for specific response parameters. Default value: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The type of addresses. Valid values:
        # 
        # *   IPV4: IPv4 address
        # *   IPv6: IPv6 address
        # *   DOMAIN: domain name
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addrs is not None:
            result['Addrs'] = self.addrs

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addrs') is not None:
            self.addrs = m.get('Addrs')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

