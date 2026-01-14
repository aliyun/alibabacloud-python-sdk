# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBasicAccelerateIpResponseBody(DaraModel):
    def __init__(
        self,
        accelerate_ip_address: str = None,
        accelerate_ip_id: str = None,
        accelerator_id: str = None,
        ip_set_id: str = None,
        request_id: str = None,
        state: str = None,
    ):
        # The accelerated IP address of the basic GA instance.
        self.accelerate_ip_address = accelerate_ip_address
        # The ID of the accelerated IP address.
        self.accelerate_ip_id = accelerate_ip_id
        # The ID of the basic GA instance to which the queried accelerated IP address belongs.
        self.accelerator_id = accelerator_id
        # The ID of the acceleration region of the basic GA instance.
        self.ip_set_id = ip_set_id
        # The request ID.
        self.request_id = request_id
        # The status of the accelerated IP address. Valid values:
        # 
        # *   **active**: The accelerated IP address is available.
        # *   **binding**: The accelerated IP address is being associated.
        # *   **bound**: The accelerated IP address is associated.
        # *   **unbinding**: The accelerated IP address is being disassociated.
        # *   **deleting**: The GA instance is being deleted.
        # 
        # >  If the accelerated IP address is being created, this parameter is not returned.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_ip_address is not None:
            result['AccelerateIpAddress'] = self.accelerate_ip_address

        if self.accelerate_ip_id is not None:
            result['AccelerateIpId'] = self.accelerate_ip_id

        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateIpAddress') is not None:
            self.accelerate_ip_address = m.get('AccelerateIpAddress')

        if m.get('AccelerateIpId') is not None:
            self.accelerate_ip_id = m.get('AccelerateIpId')

        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

