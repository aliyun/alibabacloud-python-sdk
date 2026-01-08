# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolicyPriorUsedRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        ip_version: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The direction of the traffic to which the access control policy applies.
        # 
        # Valid values:
        # 
        # *   **in**: inbound.
        # *   **out**: outbound.
        # 
        # This parameter is required.
        self.direction = direction
        # The IP version of the asset that is protected by Cloud Firewall.
        # 
        # Valid values:
        # 
        # *   **4** (default): IPv4.
        # *   **6**: IPv6.
        self.ip_version = ip_version
        # The language of the content within the request and response.
        # 
        # Valid values:
        # 
        # *   **zh** (default)
        # *   **en**
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
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

