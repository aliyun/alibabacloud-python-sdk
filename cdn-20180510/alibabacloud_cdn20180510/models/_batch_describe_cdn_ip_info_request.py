# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchDescribeCdnIpInfoRequest(DaraModel):
    def __init__(
        self,
        ip_addr_list: str = None,
        language: str = None,
    ):
        # The list of IP addresses to query. Separate IP addresses with commas (,). You can specify up to 20 IP addresses at a time.
        # 
        # > *   Example of an IPv4 address: 192.0.2.1
        # >*   Example of an IPv6 address: 2001:db8:ffff:ffff:ffff:\\*\\*\\*\\*:ffff.
        # 
        # This parameter is required.
        self.ip_addr_list = ip_addr_list
        # The language of the query results. Valid values:
        # 
        # *   **zh** (default): Simplified Chinese.
        # *   **en**: English.
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_addr_list is not None:
            result['IpAddrList'] = self.ip_addr_list

        if self.language is not None:
            result['Language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddrList') is not None:
            self.ip_addr_list = m.get('IpAddrList')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        return self

