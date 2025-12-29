# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAuditLogFilterResponseBody(DaraModel):
    def __init__(
        self,
        filter: str = None,
        request_id: str = None,
        role_type: str = None,
    ):
        # The type of the audit log entries. Valid values:
        # 
        # *   **admin**: O\\&M and management operations
        # *   **slow**: slow query logs
        # *   **query**: query operations
        # *   **insert**: insert operations
        # *   **update**: update operations
        # *   **delete**: delete operations
        # *   **command**: protocol commands such as the aggregate method
        self.filter = filter
        # The ID of the request.
        self.request_id = request_id
        # The role of the node.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

