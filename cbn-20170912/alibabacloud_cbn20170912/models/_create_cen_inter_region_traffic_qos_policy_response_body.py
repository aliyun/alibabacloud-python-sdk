# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCenInterRegionTrafficQosPolicyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_qos_policy_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the QoS policy.
        self.traffic_qos_policy_id = traffic_qos_policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.traffic_qos_policy_id is not None:
            result['TrafficQosPolicyId'] = self.traffic_qos_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrafficQosPolicyId') is not None:
            self.traffic_qos_policy_id = m.get('TrafficQosPolicyId')

        return self

