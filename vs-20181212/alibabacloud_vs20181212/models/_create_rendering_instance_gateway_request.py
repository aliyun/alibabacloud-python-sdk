# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRenderingInstanceGatewayRequest(DaraModel):
    def __init__(
        self,
        gateway_instance_id: str = None,
        rendering_instance_id: str = None,
    ):
        # This parameter is required.
        self.gateway_instance_id = gateway_instance_id
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_instance_id is not None:
            result['GatewayInstanceId'] = self.gateway_instance_id

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayInstanceId') is not None:
            self.gateway_instance_id = m.get('GatewayInstanceId')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

