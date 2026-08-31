# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQualityWatchTaskRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        watch_task_id: int = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id
        # The quality watchtask ID.
        # 
        # This parameter is required.
        self.watch_task_id = watch_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.watch_task_id is not None:
            result['WatchTaskId'] = self.watch_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('WatchTaskId') is not None:
            self.watch_task_id = m.get('WatchTaskId')

        return self

