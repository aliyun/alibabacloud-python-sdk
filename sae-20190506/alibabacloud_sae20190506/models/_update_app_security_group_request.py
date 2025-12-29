# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppSecurityGroupRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        security_group_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

