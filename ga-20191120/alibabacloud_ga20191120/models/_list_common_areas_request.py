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
        # The IP version used to connect to the GA instance. Valid values:
        # 
        # *   **IPv4** (default)
        # *   **IPv6**
        self.ip_version = ip_version
        # Specifies whether to query regions where endpoint groups of GA can be deployed. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.is_epg = is_epg
        # Specifies whether to query regions supported by GA. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
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

