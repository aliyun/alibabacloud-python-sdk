# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDomainWebSocketStatusRequest(DaraModel):
    def __init__(
        self,
        action_value: str = None,
        domain_name: str = None,
        group_id: str = None,
        security_token: str = None,
        wssenable: str = None,
    ):
        # The action.
        # 
        # This parameter is required.
        self.action_value = action_value
        # The custom domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        self.security_token = security_token
        # If enable WSS.
        self.wssenable = wssenable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_value is not None:
            result['ActionValue'] = self.action_value

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.wssenable is not None:
            result['WSSEnable'] = self.wssenable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionValue') is not None:
            self.action_value = m.get('ActionValue')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('WSSEnable') is not None:
            self.wssenable = m.get('WSSEnable')

        return self

