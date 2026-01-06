# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOperatorPermissionResponseBody(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        dbcluster_id: str = None,
        expired_time: str = None,
        privileges: str = None,
        request_id: str = None,
    ):
        # The time when the permissions take effect.
        self.created_time = created_time
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The time when the permissions expire.
        self.expired_time = expired_time
        # The queried permissions.
        self.privileges = privileges
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.privileges is not None:
            result['Privileges'] = self.privileges

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Privileges') is not None:
            self.privileges = m.get('Privileges')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

