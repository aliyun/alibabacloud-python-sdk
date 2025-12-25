# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RebuildDBInstanceResponseBody(DaraModel):
    def __init__(
        self,
        migration_id: int = None,
        request_id: str = None,
        task_id: int = None,
    ):
        # The serial number of the task in the rebuild task queue. When the serial number becomes 0, the system starts to rebuild the secondary instance.
        self.migration_id = migration_id
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
        if self.migration_id is not None:
            result['MigrationId'] = self.migration_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationId') is not None:
            self.migration_id = m.get('MigrationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

