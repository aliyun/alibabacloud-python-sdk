# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppPoliciesForIdentityRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        identity_name: str = None,
        identity_type: str = None,
    ):
        # The ID of the application. Default value: **app-1000000**. For more information, see [Overview](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The name of the identity.
        # 
        # *   Specifies the ID of the RAM user when the IdentityType parameter is set to RamUser.
        # *   Specifies the name of the RAM role when the IdentityType parameter is set to RamRole.
        self.identity_name = identity_name
        # The type of the identity. Valid values:
        # 
        # *   **RamUser**: a RAM user.
        # *   **RamRole**: a RAM role.
        self.identity_type = identity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        return self

