# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeReplicationLinkLogsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        task_id: int = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The task ID. You must set this parameter to the ID of the task that you create by calling the **CreateReplicationLink** operation for the disaster recovery instance.
        self.task_id = task_id
        # The task name. You must set this parameter to the name of the task that you create by calling the **CreateReplicationLink** operation for the disaster recovery instance.
        self.task_name = task_name
        # The type of the task. Valid values:
        # 
        # *   **create**: creates a synchronization link.
        # *   **create-dryrun**: performs a precheck before a synchronization link is created.
        # 
        # Valid values:
        # 
        # *   create: creates a replication link.
        # *   create-dryrun: performs a precheck before a replication link is created.
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

