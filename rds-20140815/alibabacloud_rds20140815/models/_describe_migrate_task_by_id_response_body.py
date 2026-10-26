# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMigrateTaskByIdResponseBody(DaraModel):
    def __init__(
        self,
        backup_mode: str = None,
        create_time: str = None,
        dbinstance_name: str = None,
        dbname: str = None,
        description: str = None,
        end_time: str = None,
        is_dbreplaced: str = None,
        migrate_task_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The type of the OSS backup migration task. Valid values:
        # 
        # - **FULL**: restores data by using a full log file.
        # - **UPDF**: restores incremental data by using differential or log log files.
        self.backup_mode = backup_mode
        # The time when the OSS backup migration task was created. The time follows the ISO 8601 standard in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The instance ID.
        self.dbinstance_name = dbinstance_name
        # The name of the database.
        self.dbname = dbname
        # The description of the OSS backup migration task.
        self.description = description
        # The time when the OSS backup migration task ended. The time follows the ISO 8601 standard in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is displayed in UTC.
        self.end_time = end_time
        # Specifies whether the import overwrites the existing database. Valid values: 
        # 
        # - **False**: no
        # - **True**: yes
        self.is_dbreplaced = is_dbreplaced
        # The ID of the OSS backup migration task.
        self.migrate_task_id = migrate_task_id
        # The ID of the request.
        self.request_id = request_id
        # The status of the OSS backup migration task. Valid values:
        # 
        # - **NoStart**: The task is not started.
        # - **Running**: The task is running.
        # - **Success**: The task is successful.
        # - **Failed**: The task failed.
        # - **Waiting**: The task is waiting for the import of incremental backup files.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_dbreplaced is not None:
            result['IsDBReplaced'] = self.is_dbreplaced

        if self.migrate_task_id is not None:
            result['MigrateTaskId'] = self.migrate_task_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsDBReplaced') is not None:
            self.is_dbreplaced = m.get('IsDBReplaced')

        if m.get('MigrateTaskId') is not None:
            self.migrate_task_id = m.get('MigrateTaskId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

