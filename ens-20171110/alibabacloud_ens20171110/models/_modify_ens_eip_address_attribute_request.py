# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEnsEipAddressAttributeRequest(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        bandwidth: int = None,
        description: str = None,
        name: str = None,
    ):
        # The ID of the EIP.
        # 
        # This parameter is required.
        self.allocation_id = allocation_id
        # The peak bandwidth of the EIP. Default value: 5. Valid values: **5** to **10000**. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The new description of the EIP. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The new name of the EIP. The name must be 2 to 128 characters in length and cannot start with http:// or https://.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

