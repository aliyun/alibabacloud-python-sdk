# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RevokeAgentUsersRequest(DaraModel):
    def __init__(
        self,
        operating_object_name: str = None,
        tenant_id: str = None,
        user_group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # The name of the digital human.
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The list of user group IDs to be revoked (16-character hex strings).
        self.user_group_ids = user_group_ids
        # The list of user IDs to be revoked.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_ids is not None:
            result['userGroupIds'] = self.user_group_ids

        if self.user_ids is not None:
            result['userIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupIds') is not None:
            self.user_group_ids = m.get('userGroupIds')

        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')

        return self

