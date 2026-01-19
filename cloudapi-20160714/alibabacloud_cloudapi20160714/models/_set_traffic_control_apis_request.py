# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetTrafficControlApisRequest(DaraModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
        traffic_control_id: str = None,
    ):
        # The API ID for the specified operation. Separate multiple API IDs with commas (,). A maximum of 100 API IDs can be entered.
        # 
        # This parameter is required.
        self.api_ids = api_ids
        # The ID of the API group containing the APIs to which you want to bind a specified throttling policy.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The security token included in the WebSocket request header. The system uses this token to authenticate the request.
        self.security_token = security_token
        # The name of the runtime environment. Valid values:
        # 
        # *   **RELEASE**
        # *   **TEST**
        # 
        # This parameter is required.
        self.stage_name = stage_name
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
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')

        return self

