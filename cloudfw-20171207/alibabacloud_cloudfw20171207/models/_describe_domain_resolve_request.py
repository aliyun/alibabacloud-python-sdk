# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainResolveRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        ip_version: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The domain name whose DNS record you want to query.
        # 
        # This parameter is required.
        self.domain = domain
        # The IP version of the asset that is protected by Cloud Firewall. Valid values:
        # 
        # *   **4**: IPv4 (default)
        # *   **6**: IPv6
        self.ip_version = ip_version
        # The language of the content within the response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
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
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

