# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigEndpointProbeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        enable: str = None,
        endpoint: str = None,
        endpoint_group_id: str = None,
        endpoint_type: str = None,
        probe_port: str = None,
        probe_protocol: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to enable latency monitoring. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # This parameter is required.
        self.enable = enable
        # The endpoint.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The endpoint group ID.
        # 
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id
        # The type of the endpoint. Valid values:
        # 
        # *   **Ip:** a custom IP address.
        # *   **Domain:** a custom domain name.
        # *   **EIP:** an Alibaba Cloud elastic IP address (EIP).
        # *   **PublicIp:** an Alibaba Cloud public IP address.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The port that is used to monitor latency. Valid values: **0** to **65535**.
        self.probe_port = probe_port
        # The protocol that is used to monitor latency. Valid values:
        # 
        # *   **tcp:** TCP.
        # *   **icmp:** ICMP.
        self.probe_protocol = probe_protocol
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.probe_port is not None:
            result['ProbePort'] = self.probe_port

        if self.probe_protocol is not None:
            result['ProbeProtocol'] = self.probe_protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('ProbePort') is not None:
            self.probe_port = m.get('ProbePort')

        if m.get('ProbeProtocol') is not None:
            self.probe_protocol = m.get('ProbeProtocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

