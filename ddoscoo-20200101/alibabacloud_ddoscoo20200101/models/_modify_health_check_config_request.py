# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHealthCheckConfigRequest(DaraModel):
    def __init__(
        self,
        forward_protocol: str = None,
        frontend_port: int = None,
        health_check: str = None,
        instance_id: str = None,
    ):
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        # 
        # This parameter is required.
        self.forward_protocol = forward_protocol
        # The forwarding port.
        # 
        # This parameter is required.
        self.frontend_port = frontend_port
        # The details of the health check configuration. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **Type**: the protocol type. This field is required and must be of the STRING type. Valid values: **tcp** (Layer 4) and **http** (Layer 7).
        # 
        # *   **Domain**: the domain name, which must be of the STRING type.
        # 
        #     **
        # 
        #     **Note**This parameter is returned only when the Layer 7 health check configuration is queried.
        # 
        # *   **Uri**: the check path, which must be of the STRING type.
        # 
        #     **
        # 
        #     **Note**This parameter is returned only when the Layer 7 health check configuration is queried.
        # 
        # *   **Timeout**: the response timeout period, which must be of the INTEGER type. Valid values: **1** to **30**. Unit: seconds.
        # 
        # *   **Port**: the port on which you want to perform the health check, which must be of the INTEGER type.
        # 
        # *   **Interval**: the health check interval, which must be of the INTEGER type. Valid values: **1** to **30**. Unit: seconds.
        # 
        # *   **Up**: the number of consecutive successful health checks that must occur before declaring a port healthy, which must be of the INTEGER type. Valid values: **1** to **10**.
        # 
        # *   **Down**: the number of consecutive failed health checks that must occur before declaring a port unhealthy, which must be of the INTEGER type. Valid values: **1** to **10**.
        # 
        # This parameter is required.
        self.health_check = health_check
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol

        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

