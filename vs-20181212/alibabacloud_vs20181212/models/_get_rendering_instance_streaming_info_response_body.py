# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRenderingInstanceStreamingInfoResponseBody(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        gateway: str = None,
        hostname: str = None,
        port: str = None,
        rendering_instance_id: str = None,
        request_id: str = None,
    ):
        # Token for this connection
        self.flow_id = flow_id
        # Domain name of the cloud application service instance streaming gateway
        self.gateway = gateway
        # Hostname or IP address of the cloud application service instance stream
        self.hostname = hostname
        # Streaming connection port
        self.port = port
        # Cloud application service instance ID
        self.rendering_instance_id = rendering_instance_id
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.port is not None:
            result['Port'] = self.port

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

