# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListRestoreTasksResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        restore_tasks: List[main_models.ListRestoreTasksResponseBodyRestoreTasks] = None,
        total_count: int = None,
    ):
        # The maximum number of records returned in this request.
        self.max_results = max_results
        # Indicates the read position returned by the current call. An empty value means all data has been read.
        # 
        # This parameter is required.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The list of restore tasks.
        self.restore_tasks = restore_tasks
        # Total data count under the current request conditions (optional; not returned by default).
        self.total_count = total_count

    def validate(self):
        if self.restore_tasks:
            for v1 in self.restore_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RestoreTasks'] = []
        if self.restore_tasks is not None:
            for k1 in self.restore_tasks:
                result['RestoreTasks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.restore_tasks = []
        if m.get('RestoreTasks') is not None:
            for k1 in m.get('RestoreTasks'):
                temp_model = main_models.ListRestoreTasksResponseBodyRestoreTasks()
                self.restore_tasks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRestoreTasksResponseBodyRestoreTasks(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        create_time: str = None,
        end_time: str = None,
        modified_time: str = None,
        restore_task_id: str = None,
        service_instance_id: str = None,
        start_time: str = None,
        status: str = None,
        status_detail: str = None,
    ):
        # The backup ID.
        self.backup_id = backup_id
        # The creation time.
        self.create_time = create_time
        # The expiration time of the service instance.
        self.end_time = end_time
        # The update time.
        self.modified_time = modified_time
        # The ID of the restore task.
        self.restore_task_id = restore_task_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The time when the update started.
        self.start_time = start_time
        # The status of the service instance. Valid values:
        # 
        # *   Restoring
        # *   Restored
        # *   RestoreFailed
        self.status = status
        # The description of the service instance deployment information.
        self.status_detail = status_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')

        return self

