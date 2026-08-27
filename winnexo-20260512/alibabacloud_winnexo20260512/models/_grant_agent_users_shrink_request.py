# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantAgentUsersShrinkRequest(DaraModel):
    def __init__(
        self,
        expire_date: int = None,
        operating_object_name: str = None,
        permissions_shrink: str = None,
        tenant_id: str = None,
        user_group_ids_shrink: str = None,
        user_ids_shrink: str = None,
    ):
        # The authorization expiration timestamp in milliseconds. If this parameter is not specified, the authorization never expires.
        self.expire_date = expire_date
        # The name of the digital human.
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # The permission items.
        self.permissions_shrink = permissions_shrink
        # The tenant ID.
        self.tenant_id = tenant_id
        # The list of user group IDs.
        self.user_group_ids_shrink = user_group_ids_shrink
        # The list of user IDs to be authorized.
        self.user_ids_shrink = user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_date is not None:
            result['expireDate'] = self.expire_date

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.permissions_shrink is not None:
            result['permissions'] = self.permissions_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_ids_shrink is not None:
            result['userGroupIds'] = self.user_group_ids_shrink

        if self.user_ids_shrink is not None:
            result['userIds'] = self.user_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireDate') is not None:
            self.expire_date = m.get('expireDate')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('permissions') is not None:
            self.permissions_shrink = m.get('permissions')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupIds') is not None:
            self.user_group_ids_shrink = m.get('userGroupIds')

        if m.get('userIds') is not None:
            self.user_ids_shrink = m.get('userIds')

        return self

