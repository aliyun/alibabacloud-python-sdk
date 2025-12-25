# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        dbname: str = None,
        dbstatus: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The name of the database.
        self.dbname = dbname
        # The status of the database. Valid values:
        # 
        # *   **Creating**
        # *   **Running**
        # *   **Deleting**
        self.dbstatus = dbstatus
        # The ID of the request.
        self.request_id = request_id
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.dbstatus is not None:
            result['DBStatus'] = self.dbstatus

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DBStatus') is not None:
            self.dbstatus = m.get('DBStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

