# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddFaceDeviceGroupRequest(DaraModel):
    def __init__(
        self,
        device_group_name: str = None,
        isolation_id: str = None,
    ):
        # The name of the device group. You can customize the value. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.device_group_name = device_group_name
        # The business isolation ID. It is used to isolate data between different business applications under the same Alibaba Cloud account. It supports uppercase and lowercase English letters and digits.
        # 
        # For example, if you have face recognition businesses in Region A and Region B, you can set different business isolation IDs to distinguish the face recognition businesses in Region A and Region B.
        # 
        # >Notice: 
        # Save the business isolation ID properly for use when you call other API operations in this business isolation zone.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name

        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')

        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        return self

