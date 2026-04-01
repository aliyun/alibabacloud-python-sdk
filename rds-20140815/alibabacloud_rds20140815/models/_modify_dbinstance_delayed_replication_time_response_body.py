# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceDelayedReplicationTimeResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        read_sqlreplication_time: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The replication latency of the read-only instance. Unit: seconds.
        self.read_sqlreplication_time = read_sqlreplication_time
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.read_sqlreplication_time is not None:
            result['ReadSQLReplicationTime'] = self.read_sqlreplication_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ReadSQLReplicationTime') is not None:
            self.read_sqlreplication_time = m.get('ReadSQLReplicationTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

