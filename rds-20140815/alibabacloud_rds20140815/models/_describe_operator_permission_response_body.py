# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOperatorPermissionResponseBody(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        expired_time: str = None,
        privileges: str = None,
        request_id: str = None,
    ):
        # The effective period of the authorization. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        self.created_time = created_time
        # The time when the authorization expires. Format: yyyy-MM-ddTHH:mm:ssZ (UTC).
        self.expired_time = expired_time
        # The types of permissions that are granted. Valid values:
        # - **Control**: configuration permissions. Allows you to view and modify instance configurations.
        # - **Data**: database permissions. Allows you to view table schemas, indexes, and SQL statements.
        self.privileges = privileges
        # The ID of the request.
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

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Privileges') is not None:
            self.privileges = m.get('Privileges')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

