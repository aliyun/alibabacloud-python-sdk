# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScheduledTaskConversationRecordsRequest(DaraModel):
    def __init__(
        self,
        initiator_user_id: str = None,
        page: int = None,
        page_size: int = None,
        status: str = None,
        task_id: str = None,
        tenant_id: str = None,
    ):
        # The user ID of the task initiator.
        self.initiator_user_id = initiator_user_id
        # The page number. Default value: 1.
        self.page = page
        # The maximum number of data records to return in this request.
        self.page_size = page_size
        # The running status of the task.
        self.status = status
        # The execution status filter in lowercase. Valid values: pending (queued), running (running), success (successful), failed (failed), timeout (timed out), and cancelled (cancelled). If you do not specify this parameter, no filtering is applied. If you specify this parameter, future scheduled items are not generated.
        self.task_id = task_id
        # The tenant ID. This is a common parameter. If you do not specify this parameter, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.initiator_user_id is not None:
            result['initiatorUserId'] = self.initiator_user_id

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('initiatorUserId') is not None:
            self.initiator_user_id = m.get('initiatorUserId')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

