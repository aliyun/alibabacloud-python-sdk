# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveUserGroupMembersRequest(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
        user_group_id: str = None,
        user_ids: List[int] = None,
    ):
        # The tenant ID. This is a common parameter. You can explicitly pass this parameter in winnexo-cli by using `--tenant-id`.
        self.tenant_id = tenant_id
        # The ID of the target user group.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id
        # The list of platform user IDs to be removed. You can specify one or more IDs.
        # 
        # This parameter is required.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_id is not None:
            result['userGroupId'] = self.user_group_id

        if self.user_ids is not None:
            result['userIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupId') is not None:
            self.user_group_id = m.get('userGroupId')

        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')

        return self

