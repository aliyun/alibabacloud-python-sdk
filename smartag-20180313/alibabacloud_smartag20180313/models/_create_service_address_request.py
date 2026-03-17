# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceAddressRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_type: str = None,
        region_id: str = None,
        sag_id: str = None,
        sn: str = None,
    ):
        # The service address. Example: **192.168.1.1**.
        # 
        # This parameter is required.
        self.address = address
        # The type of service address. Set the value to **ProbeTask**.
        # 
        # This parameter is required.
        self.address_type = address_type
        # The region ID of the SAG instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.sag_id = sag_id
        # The serial number of the SAG device.
        # 
        # This parameter is required.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sag_id is not None:
            result['SagId'] = self.sag_id

        if self.sn is not None:
            result['Sn'] = self.sn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SagId') is not None:
            self.sag_id = m.get('SagId')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        return self

