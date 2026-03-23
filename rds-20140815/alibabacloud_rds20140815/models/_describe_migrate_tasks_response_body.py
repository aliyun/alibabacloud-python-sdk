# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeMigrateTasksResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        items: main_models.DescribeMigrateTasksResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeMigrateTasksResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeMigrateTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        migrate_task: List[main_models.DescribeMigrateTasksResponseBodyItemsMigrateTask] = None,
    ):
        self.migrate_task = migrate_task

    def validate(self):
        if self.migrate_task:
            for v1 in self.migrate_task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MigrateTask'] = []
        if self.migrate_task is not None:
            for k1 in self.migrate_task:
                result['MigrateTask'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.migrate_task = []
        if m.get('MigrateTask') is not None:
            for k1 in m.get('MigrateTask'):
                temp_model = main_models.DescribeMigrateTasksResponseBodyItemsMigrateTask()
                self.migrate_task.append(temp_model.from_map(k1))

        return self

class DescribeMigrateTasksResponseBodyItemsMigrateTask(DaraModel):
    def __init__(
        self,
        backup_mode: str = None,
        create_time: str = None,
        dbname: str = None,
        description: str = None,
        end_time: str = None,
        is_dbreplaced: str = None,
        migrate_task_id: str = None,
        status: str = None,
    ):
        self.backup_mode = backup_mode
        self.create_time = create_time
        self.dbname = dbname
        self.description = description
        self.end_time = end_time
        self.is_dbreplaced = is_dbreplaced
        self.migrate_task_id = migrate_task_id
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

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

