# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRenderingInstanceBandwidthRequest(DaraModel):
    def __init__(
        self,
        max_egress_bandwidth: int = None,
        max_ingress_bandwidth: int = None,
        rendering_instance_id: str = None,
    ):
        self.max_egress_bandwidth = max_egress_bandwidth
        self.max_ingress_bandwidth = max_ingress_bandwidth
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_egress_bandwidth is not None:
            result['MaxEgressBandwidth'] = self.max_egress_bandwidth

        if self.max_ingress_bandwidth is not None:
            result['MaxIngressBandwidth'] = self.max_ingress_bandwidth

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxEgressBandwidth') is not None:
            self.max_egress_bandwidth = m.get('MaxEgressBandwidth')

        if m.get('MaxIngressBandwidth') is not None:
            self.max_ingress_bandwidth = m.get('MaxIngressBandwidth')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

