# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DescribeRoleTagStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        role_tag_status: str = None,
        shard_role_tag_status: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.role_tag_status = role_tag_status
        self.shard_role_tag_status = shard_role_tag_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_tag_status is not None:
            result['RoleTagStatus'] = self.role_tag_status

        if self.shard_role_tag_status is not None:
            result['ShardRoleTagStatus'] = self.shard_role_tag_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleTagStatus') is not None:
            self.role_tag_status = m.get('RoleTagStatus')

        if m.get('ShardRoleTagStatus') is not None:
            self.shard_role_tag_status = m.get('ShardRoleTagStatus')

        return self

