# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TimedResidentResourcePoolApplication(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        content: str = None,
        created_time: str = None,
        last_modified_time: str = None,
        operation_type: str = None,
        status: str = None,
        timed_pool_id: str = None,
    ):
        self.account_id = account_id
        self.content = content
        self.created_time = created_time
        self.last_modified_time = last_modified_time
        self.operation_type = operation_type
        self.status = status
        self.timed_pool_id = timed_pool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.content is not None:
            result['content'] = self.content

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.operation_type is not None:
            result['operationType'] = self.operation_type

        if self.status is not None:
            result['status'] = self.status

        if self.timed_pool_id is not None:
            result['timedPoolId'] = self.timed_pool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('timedPoolId') is not None:
            self.timed_pool_id = m.get('timedPoolId')

        return self

