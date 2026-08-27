# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScheduledTaskExecutionRecordsRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        initiator_user_id: str = None,
        page: int = None,
        page_size: int = None,
        status: str = None,
        task_id: str = None,
        tenant_id: str = None,
    ):
        # The ID of the collaboration group to which the task belongs (such as cg_101). If specified, a group space task is created (the caller must be a valid group member). If left empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # Filters by initiator (platform user ID). The scope is the executor of the record (manual execution = the person who triggered it, automatic execution = the task creator). To view only tasks initiated by yourself, pass the current user ID.
        self.initiator_user_id = initiator_user_id
        # The page number. Default value: 1. Minimum value: 1. Maximum value: 200.
        self.page = page
        # The number of records per page.
        self.page_size = page_size
        # Filters by execution status (lowercase). Valid values:
        # - pending: queued.
        # - running: in progress.
        # - success: succeeded.
        # - failed: failed.
        # - timeout: timed out.
        # - cancelled: terminated.
        # 
        # If not specified, no status filter is applied. If specified, future planned items are no longer generated.
        self.status = status
        # Filters by a single task ID. If not specified, execution records of all visible tasks are returned.
        self.task_id = task_id
        # The ID of the effective tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

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
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

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

