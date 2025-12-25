# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMigrateTaskResponseBody(DaraModel):
    def __init__(
        self,
        backup_mode: str = None,
        dbinstance_id: str = None,
        dbname: str = None,
        migrate_task_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The type of the migration task. Valid values:
        # 
        # *   **FULL**: The migration task migrates full backup files.
        # *   **UPDF**: The migration task migrates incremental or log backup files.
        self.backup_mode = backup_mode
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.dbname = dbname
        # The ID of the migration task.
        self.migrate_task_id = migrate_task_id
        # The ID of the request.
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
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.migrate_task_id is not None:
            result['MigrateTaskId'] = self.migrate_task_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('MigrateTaskId') is not None:
            self.migrate_task_id = m.get('MigrateTaskId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

