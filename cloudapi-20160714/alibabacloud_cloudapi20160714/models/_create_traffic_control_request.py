# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTrafficControlRequest(DaraModel):
    def __init__(
        self,
        api_default: int = None,
        app_default: int = None,
        description: str = None,
        security_token: str = None,
        traffic_control_name: str = None,
        traffic_control_unit: str = None,
        user_default: int = None,
    ):
        # The default throttling value for each API.
        # 
        # This parameter is required.
        self.api_default = api_default
        # The default throttling value for each app.
        self.app_default = app_default
        # The description of the throttling policy.
        self.description = description
        # The security token included in the WebSocket request header. The system uses this token to authenticate the request.
        self.security_token = security_token
        # The name of the throttling policy. The name must be 4 to 50 characters in length and can contain letters, digits, and underscores (_). It cannot start with an underscore.
        # 
        # This parameter is required.
        self.traffic_control_name = traffic_control_name
        # The unit to be used in the throttling policy. Valid values:
        # 
        # *   **SECOND**
        # *   **MINUTE**
        # *   **HOUR**
        # *   **DAY**
        # 
        # This parameter is required.
        self.traffic_control_unit = traffic_control_unit
        # The default throttling value for each user.
        self.user_default = user_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_default is not None:
            result['ApiDefault'] = self.api_default

        if self.app_default is not None:
            result['AppDefault'] = self.app_default

        if self.description is not None:
            result['Description'] = self.description

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name

        if self.traffic_control_unit is not None:
            result['TrafficControlUnit'] = self.traffic_control_unit

        if self.user_default is not None:
            result['UserDefault'] = self.user_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDefault') is not None:
            self.api_default = m.get('ApiDefault')

        if m.get('AppDefault') is not None:
            self.app_default = m.get('AppDefault')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')

        if m.get('TrafficControlUnit') is not None:
            self.traffic_control_unit = m.get('TrafficControlUnit')

        if m.get('UserDefault') is not None:
            self.user_default = m.get('UserDefault')

        return self

