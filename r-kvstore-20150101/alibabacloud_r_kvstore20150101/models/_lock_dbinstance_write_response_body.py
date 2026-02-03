# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LockDBInstanceWriteResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        lock_reason: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        # The instance ID.
        self.dbinstance_name = dbinstance_name
        # The reason why write operations on the instance are locked.
        self.lock_reason = lock_reason
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

