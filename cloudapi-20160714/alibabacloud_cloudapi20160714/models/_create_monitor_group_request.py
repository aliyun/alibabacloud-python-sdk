# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMonitorGroupRequest(DaraModel):
    def __init__(
        self,
        auth: str = None,
        group_id: str = None,
        raw_monitor_group_id: int = None,
        security_token: str = None,
    ):
        # The caller authentication status of the API. Valid values: **ok**: The authentication is successful. **mismatch**: The request is redirected. **servicenotfound**: A request error occurred. **Unknown**: An unknown error occurred.
        # 
        # This parameter is required.
        self.auth = auth
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the monitoring group.
        self.raw_monitor_group_id = raw_monitor_group_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth is not None:
            result['Auth'] = self.auth

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.raw_monitor_group_id is not None:
            result['RawMonitorGroupId'] = self.raw_monitor_group_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('RawMonitorGroupId') is not None:
            self.raw_monitor_group_id = m.get('RawMonitorGroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

