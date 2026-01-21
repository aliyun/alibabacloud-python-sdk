# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSiteMonitorISPCityListRequest(DaraModel):
    def __init__(
        self,
        city: str = None,
        ipv4: bool = None,
        ipv6: bool = None,
        isp: str = None,
        region_id: str = None,
        view_all: bool = None,
    ):
        # The name or ID of the city.
        # 
        # > City names support fuzzy match.
        self.city = city
        # Specifies whether to query IPv4 probes. Valid values:
        # 
        # *   true (default): IPv4 probes are queried.
        # *   false: IPv4 probes are not queried.
        self.ipv4 = ipv4
        # Specifies whether to query IPv6 probes. Valid values:
        # 
        # *   true (default): IPv6 probes are queried.
        # *   false: IPv6 probes are not queried.
        self.ipv6 = ipv6
        # The name or ID of the carrier.
        # 
        # > Carrier names support fuzzy match.
        self.isp = isp
        self.region_id = region_id
        # Specifies whether to return all detection points. Valid values:
        # 
        # *   true (default): returns all detection points.
        # *   false: returns only available detection points.
        self.view_all = view_all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.ipv4 is not None:
            result['IPV4'] = self.ipv4

        if self.ipv6 is not None:
            result['IPV6'] = self.ipv6

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.view_all is not None:
            result['ViewAll'] = self.view_all

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('IPV4') is not None:
            self.ipv4 = m.get('IPV4')

        if m.get('IPV6') is not None:
            self.ipv6 = m.get('IPV6')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ViewAll') is not None:
            self.view_all = m.get('ViewAll')

        return self

