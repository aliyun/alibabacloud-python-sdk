# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTrafficSpecialControlRequest(DaraModel):
    def __init__(
        self,
        security_token: str = None,
        special_key: str = None,
        special_type: str = None,
        traffic_control_id: str = None,
    ):
        # The security token included in the WebSocket request header. The system uses this token to authenticate the request.
        self.security_token = security_token
        # The ID of the app or Alibaba Cloud account. You can view your account ID on the [Account Management](https://account.console.aliyun.com/?spm=a2c4g.11186623.2.15.343130a8sDi8cO#/secure) page.
        # 
        # This parameter is required.
        self.special_key = special_key
        # The type of the special throttling policy. Valid values:
        # 
        # *   **APP**
        # *   **USER**
        # 
        # This parameter is required.
        self.special_type = special_type
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

        if self.special_key is not None:
            result['SpecialKey'] = self.special_key

        if self.special_type is not None:
            result['SpecialType'] = self.special_type

        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SpecialKey') is not None:
            self.special_key = m.get('SpecialKey')

        if m.get('SpecialType') is not None:
            self.special_type = m.get('SpecialType')

        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')

        return self

