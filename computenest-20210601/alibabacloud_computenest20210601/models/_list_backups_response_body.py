# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListBackupsResponseBody(DaraModel):
    def __init__(
        self,
        backups: List[main_models.ListBackupsResponseBodyBackups] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the backup.
        self.backups = backups
        # The maximum number of records returned in this request.
        self.max_results = max_results
        # Indicates the read position returned by the current call. An empty value means all data has been read.
        # 
        # This parameter is required.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # Total data count under the current request conditions (optional; not returned by default).
        self.total_count = total_count

    def validate(self):
        if self.backups:
            for v1 in self.backups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Backups'] = []
        if self.backups is not None:
            for k1 in self.backups:
                result['Backups'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backups = []
        if m.get('Backups') is not None:
            for k1 in m.get('Backups'):
                temp_model = main_models.ListBackupsResponseBodyBackups()
                self.backups.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBackupsResponseBodyBackups(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_mode: str = None,
        create_time: str = None,
        description: str = None,
        end_time: str = None,
        modified_time: str = None,
        retention_days: int = None,
        service_instance_id: str = None,
        start_time: str = None,
        status: str = None,
        status_detail: str = None,
    ):
        # The backup ID.
        self.backup_id = backup_id
        # The backup mode. Valid values:
        # 
        # *   **Manual**: manual backup
        self.backup_mode = backup_mode
        # The creation time.
        self.create_time = create_time
        # The description of the backup task.
        self.description = description
        # The end time of the backup task.
        self.end_time = end_time
        # The update time.
        self.modified_time = modified_time
        # Retention Days. Resources will be cleared upon expiration. Defaults to no expiration if left blank.
        self.retention_days = retention_days
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The start time of the backup task.
        self.start_time = start_time
        # The status of the backup task. Valid values:
        # 
        # *   Creating
        # *   Created
        # *   CreateFailed
        # *   Deleting
        # *   Deleted
        # *   DeleteFailed
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

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

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

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')

        return self

