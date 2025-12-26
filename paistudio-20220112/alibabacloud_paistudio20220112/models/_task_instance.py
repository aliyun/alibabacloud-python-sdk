# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TaskInstance(DaraModel):
    def __init__(
        self,
        gmt_created_time: str = None,
        gmt_end_time: str = None,
        status: str = None,
        task_id: str = None,
        task_instance_id: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        self.gmt_created_time = gmt_created_time
        self.gmt_end_time = gmt_end_time
        self.status = status
        self.task_id = task_id
        self.task_instance_id = task_instance_id
        self.tenant_id = tenant_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time

        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')

        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

