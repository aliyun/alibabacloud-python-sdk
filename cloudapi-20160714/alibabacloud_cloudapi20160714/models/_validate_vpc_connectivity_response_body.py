# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateVpcConnectivityResponseBody(DaraModel):
    def __init__(
        self,
        connected: bool = None,
        ip_type: str = None,
        request_id: str = None,
    ):
        # Indicates whether the API Gateway instance is connected to the port. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.connected = connected
        # Indicates whether the instance in the authorization is an ECS instance or an SLB instance when the instance ID in the authorization is an IP address. Valid values:
        # 
        # *   **ECS**
        # *   **SLB**
        # *   **INVALID**: The instance type corresponding to the IP address is invalid.
        self.ip_type = ip_type
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connected is not None:
            result['Connected'] = self.connected

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connected') is not None:
            self.connected = m.get('Connected')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

