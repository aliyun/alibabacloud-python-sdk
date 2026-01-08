# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDomainResolveRealtimeTaskRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        firewall_type: str = None,
        region_no: str = None,
    ):
        self.domain_name = domain_name
        self.firewall_type = firewall_type
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

