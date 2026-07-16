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
        # The maximum outbound bandwidth for rate limiting. Unit: Mbit/s. You must specify at least one of MaxIngressBandwidth and MaxEgressBandwidth.
        # 
        # - By default, no rate limit is configured for the instance.
        # 
        # - If you do not specify this parameter or set it to 0, the last configuration is retained.
        # 
        # - If you set this parameter to a value less than 0, the rate limit is reset to unlimited.
        self.max_egress_bandwidth = max_egress_bandwidth
        # The maximum inbound bandwidth for rate limiting. Unit: Mbit/s. You must specify at least one of MaxIngressBandwidth and MaxEgressBandwidth.
        # 
        # - By default, no rate limit is configured for the instance.
        # 
        # - If you do not specify this parameter or set it to 0, the last configuration is retained.
        # 
        # - If you set this parameter to a value less than 0, the rate limit is reset to unlimited.
        self.max_ingress_bandwidth = max_ingress_bandwidth
        # The ID of the cloud application service instance.
        # 
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

