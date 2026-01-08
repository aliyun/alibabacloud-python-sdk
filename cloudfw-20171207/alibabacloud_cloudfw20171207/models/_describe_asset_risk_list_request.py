# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAssetRiskListRequest(DaraModel):
    def __init__(
        self,
        ip_addr_list: List[str] = None,
        ip_version: int = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The IP addresses to query. Separate the IP addresses with commas (,). You can specify up to 20 IP addresses at a time.
        # 
        # > 
        # 
        # *   Example IPv4 address: 47.97.XX.XX.
        # 
        # *   Example IPv6 address: 2001:db8:ffff:ffff:ffff:XXXX:ffff.
        self.ip_addr_list = ip_addr_list
        # The IP version of the asset that is protected by Cloud Firewall.
        # 
        # Valid values:
        # 
        # *   **4** (default): IPv4
        # *   **6**: IPv6
        # 
        # This parameter is required.
        self.ip_version = ip_version
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_addr_list is not None:
            result['IpAddrList'] = self.ip_addr_list

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddrList') is not None:
            self.ip_addr_list = m.get('IpAddrList')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

