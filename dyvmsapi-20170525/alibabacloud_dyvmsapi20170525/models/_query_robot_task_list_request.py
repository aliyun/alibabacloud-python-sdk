# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRobotTaskListRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        task_name: str = None,
        time: str = None,
    ):
        self.owner_id = owner_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task state. Valid values:
        # 
        # *   **INIT**: The task is not started.
        # *   **READY**: The task is ready to start.
        # *   **DISPATCH**: The task is being parsed.
        # *   **EXCUTING**: The task is being executed.
        # *   **MANUAL_STOP**: The task is manually suspended.
        # *   **SYSTEM_STOP**: The task is suspended by the system.
        # *   **ARREARS_STOP**: The task is suspended due to overdue payments.
        # *   **CANCEL**: The task is manually canceled.
        # *   **SYSTEM_CANCEL**: The task is canceled by the system.
        # *   **FINISH**: The task is complete.
        self.status = status
        # The task name.
        self.task_name = task_name
        # The date when the task is created, in the yyyy-MM-dd format.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

