# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConnectionTicketResponseBody(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        avatar_id: str = None,
        biz_region_id: str = None,
        os_type: str = None,
        request_id: str = None,
        task_id: str = None,
        task_status: str = None,
        tenant_id: int = None,
        ticket: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the application instance.
        self.app_instance_id = app_instance_id
        # The ID of the persistent session.
        self.app_instance_persistent_id = app_instance_persistent_id
        # The avatar ID.
        self.avatar_id = avatar_id
        # The region ID.
        self.biz_region_id = biz_region_id
        # The operating system.
        # 
        # Valid value:
        # 
        # *   Windows: the Windows operating system
        self.os_type = os_type
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id
        # The task status.
        # 
        # Valid values:
        # 
        # *   Finished: The task is complete.
        # *   Failed: The task failed.
        # *   Running: The task is being executed.
        self.task_status = task_status
        # The ID of the Alibaba Cloud account.
        self.tenant_id = tenant_id
        # The credential that is used to connect to App Streaming.
        # 
        # >  This parameter is displayed for calls other than the first call to this operation.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id

        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.ticket is not None:
            result['Ticket'] = self.ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')

        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')

        return self

