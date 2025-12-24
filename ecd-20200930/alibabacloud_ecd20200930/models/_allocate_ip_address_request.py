# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateIpAddressRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        internet_charge_type: str = None,
        name: str = None,
        network_interface_id: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.internet_charge_type = internet_charge_type
        self.name = name
        self.network_interface_id = network_interface_id
        self.office_site_id = office_site_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.name is not None:
            result['Name'] = self.name

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

