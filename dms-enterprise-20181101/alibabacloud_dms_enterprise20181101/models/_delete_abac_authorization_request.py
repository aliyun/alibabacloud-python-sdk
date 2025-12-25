# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAbacAuthorizationRequest(DaraModel):
    def __init__(
        self,
        authorization_id: int = None,
        identity_type: str = None,
        tid: int = None,
    ):
        # The authorization ID.
        # 
        # This parameter is required.
        self.authorization_id = authorization_id
        # The type of object to which you want to attach the policy.********
        # 
        # Valid values:
        # 
        # *   USER
        # *   ROLE
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_id is not None:
            result['AuthorizationId'] = self.authorization_id

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationId') is not None:
            self.authorization_id = m.get('AuthorizationId')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

