# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBackupResponseBody(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        create_time: str = None,
        description: str = None,
        end_time: str = None,
        modified_time: str = None,
        request_id: str = None,
        service_instance_id: str = None,
        start_time: str = None,
        status: str = None,
        status_detail: str = None,
    ):
        # The backup ID.
        self.backup_id = backup_id
        # The creation time of the backup task.
        self.create_time = create_time
        # The description of the backup task.
        self.description = description
        # The end time of the backup task.
        self.end_time = end_time
        # The update time of the backup task.
        self.modified_time = modified_time
        # The request ID.
        self.request_id = request_id
        # The request ID.
        self.service_instance_id = service_instance_id
        # The start time of the backup task.
        self.start_time = start_time
        # The status of the backup task.
        # 
        # *   Creating
        # *   Created
        # *   CreateFailed
        # *   Deleting
        # *   Deleted
        # *   DeleteFailed
        self.status = status
        # The description of the deployment instance status.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')

        return self

