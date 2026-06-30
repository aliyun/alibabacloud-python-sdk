# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCommonAreasRequest(DaraModel):
    def __init__(
        self,
        ip_version: str = None,
        is_epg: bool = None,
        is_ip_set: bool = None,
    ):
        # The IP address protocol used to connect to Global Accelerator (GA). Valid values:
        # - **IPv4** (default): IPv4 address protocol. Queries regions that support IPv4.
        # - **IPv6**: IPv6 address protocol. Queries regions that support IPv6.
        self.ip_version = ip_version
        # Specifies whether the region is an endpoint group region supported by Global Accelerator.
        # - **true**: Yes.
        # - **false** (default): No.
        self.is_epg = is_epg
        # Specifies whether the region is an acceleration area supported by Global Accelerator.
        # - **true**: Yes.
        # - **false** (default): No.
        self.is_ip_set = is_ip_set

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.is_epg is not None:
            result['IsEpg'] = self.is_epg

        if self.is_ip_set is not None:
            result['IsIpSet'] = self.is_ip_set

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IsEpg') is not None:
            self.is_epg = m.get('IsEpg')

        if m.get('IsIpSet') is not None:
            self.is_ip_set = m.get('IsIpSet')

        return self

