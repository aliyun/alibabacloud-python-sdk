# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnlockVirtualMFADeviceRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        serial_number: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The serial number of the virtual MFA device, which is a unique identifier.
        # 
        # You can call the [DescribeVirtualMFADevices](https://help.aliyun.com/document_detail/206210.html) operation to query the serial number of the virtual MFA device bound to Active Directory (AD) users.
        # 
        # This parameter is required.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        return self

