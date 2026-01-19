# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyIpControlRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        ip_control_id: str = None,
        ip_control_name: str = None,
        security_token: str = None,
    ):
        # The description. The description can be up to 200 characters in length.
        self.description = description
        # The ID of the ACL. The ID is unique.
        # 
        # This parameter is required.
        self.ip_control_id = ip_control_id
        # The name of the ACL. The name must be 4 to 50 characters in length, and can contain letters, digits, and underscores (_). The name cannot start with an underscore (_).
        self.ip_control_name = ip_control_name
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id

        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')

        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

