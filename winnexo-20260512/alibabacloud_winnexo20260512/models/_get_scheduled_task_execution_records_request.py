# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScheduledTaskExecutionRecordsRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        collaboration_group_id: str = None,
        initiator_user_id: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        page: int = None,
        page_size: int = None,
        status: str = None,
        task_id: str = None,
        tenant_id: str = None,
    ):
        # The platform application token issued by the console. If this parameter is passed, the operation is executed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The ID of the collaboration group to which the task belongs, such as cg_101. If this parameter is passed, a group space task is created, and the caller must be a valid group member. If this parameter is left empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The business status code. A value of 200 indicates success. A failure is indicated by a backend error code such as ERR.* or InvalidParameter.*.
        self.initiator_user_id = initiator_user_id
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The page number. Default value: 1. Minimum value: 1. Maximum value: 200.
        self.page = page
        # The number of records per page.
        self.page_size = page_size
        # Filters records by the initiator platform user ID. The scope is the executor of the record. For manual execution, the executor is the trigger user. For automatic execution, the executor is the task creator. To view only the tasks that you initiated, pass the current user ID.
        self.status = status
        # The execution status filter in lowercase. Valid values: pending (queued), running (executing), success (succeeded), failed (failed), timeout (timed out), and cancelled (cancelled). If this parameter is not passed, no filtering is applied. If this parameter is passed, future plan items are not generated.
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
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.initiator_user_id is not None:
            result['initiatorUserId'] = self.initiator_user_id

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

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
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('initiatorUserId') is not None:
            self.initiator_user_id = m.get('initiatorUserId')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

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

