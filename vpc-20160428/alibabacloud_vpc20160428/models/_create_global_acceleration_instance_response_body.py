# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGlobalAccelerationInstanceResponseBody(DaraModel):
    def __init__(
        self,
        global_acceleration_instance_id: str = None,
        ip_address: str = None,
        request_id: str = None,
    ):
        # The ID of the GA instance.
        self.global_acceleration_instance_id = global_acceleration_instance_id
        # The public IP address of the GA instance.
        # 
        # If **BandwidthType** is set to **Sharing**, this parameter is not returned.
        self.ip_address = ip_address
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.global_acceleration_instance_id is not None:
            result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalAccelerationInstanceId') is not None:
            self.global_acceleration_instance_id = m.get('GlobalAccelerationInstanceId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

