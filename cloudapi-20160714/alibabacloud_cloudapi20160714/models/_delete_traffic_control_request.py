# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTrafficControlRequest(DaraModel):
    def __init__(
        self,
        security_token: str = None,
        traffic_control_id: str = None,
    ):
        self.security_token = security_token
        # The ID of the throttling policy.
        # 
        # This parameter is required.
        self.traffic_control_id = traffic_control_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')

        return self

