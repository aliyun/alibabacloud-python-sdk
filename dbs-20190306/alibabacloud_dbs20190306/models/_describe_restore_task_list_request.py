# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRestoreTaskListRequest(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        end_timestamp: int = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        restore_task_id: str = None,
        start_timestamp: int = None,
    ):
        # The ID of the backup plan.
        # 
        # > Specify either BackupPlanId or RestoreTaskId.
        self.backup_plan_id = backup_plan_id
        # A client token that is used to ensure the idempotence of the request. This prevents duplicate requests.
        self.client_token = client_token
        # The end time of the backup.
        self.end_timestamp = end_timestamp
        self.owner_id = owner_id
        # The page number. The value must be greater than or equal to 0 and not exceed the maximum value of the integer data type. Default value: 0.
        self.page_num = page_num
        # The number of entries to return on each page. Valid values: 1 to 100.
        # 
        # > Default value: 30.
        self.page_size = page_size
        # The ID of the restore job. You can specify multiple IDs. Separate them with commas (,). Call the [CreateRestoreTask](https://help.aliyun.com/document_detail/2869836.html) operation to obtain this parameter.
        # 
        # > Specify either RestoreTaskId or BackupPlanId. An error occurs if you specify both parameters.
        self.restore_task_id = restore_task_id
        # The start time of the backup.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        return self

