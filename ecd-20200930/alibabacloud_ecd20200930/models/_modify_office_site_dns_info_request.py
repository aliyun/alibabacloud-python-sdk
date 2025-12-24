# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyOfficeSiteDnsInfoRequest(DaraModel):
    def __init__(
        self,
        dns_address: List[str] = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        # The IP addresses of the custom DNS servers. Up to 2 IP addresses can be specified.
        self.dns_address = dns_address
        # The office network ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

