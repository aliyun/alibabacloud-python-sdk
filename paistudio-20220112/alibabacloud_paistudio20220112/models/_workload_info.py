# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class WorkloadInfo(DaraModel):
    def __init__(
        self,
        is_scheduled: str = None,
        priority: int = None,
        queue_metas: List[main_models.QueueMeta] = None,
        tenant_id: str = None,
        user_id: str = None,
        user_name: str = None,
        workload_created_time: str = None,
        workload_id: str = None,
        workload_name: str = None,
        workload_status: str = None,
        workload_type: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.is_scheduled = is_scheduled
        self.priority = priority
        self.queue_metas = queue_metas
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.user_name = user_name
        self.workload_created_time = workload_created_time
        self.workload_id = workload_id
        self.workload_name = workload_name
        self.workload_status = workload_status
        self.workload_type = workload_type
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        if self.queue_metas:
            for v1 in self.queue_metas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_scheduled is not None:
            result['IsScheduled'] = self.is_scheduled

        if self.priority is not None:
            result['Priority'] = self.priority

        result['QueueMetas'] = []
        if self.queue_metas is not None:
            for k1 in self.queue_metas:
                result['QueueMetas'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.workload_created_time is not None:
            result['WorkloadCreatedTime'] = self.workload_created_time

        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id

        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name

        if self.workload_status is not None:
            result['WorkloadStatus'] = self.workload_status

        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsScheduled') is not None:
            self.is_scheduled = m.get('IsScheduled')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.queue_metas = []
        if m.get('QueueMetas') is not None:
            for k1 in m.get('QueueMetas'):
                temp_model = main_models.QueueMeta()
                self.queue_metas.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('WorkloadCreatedTime') is not None:
            self.workload_created_time = m.get('WorkloadCreatedTime')

        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')

        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')

        if m.get('WorkloadStatus') is not None:
            self.workload_status = m.get('WorkloadStatus')

        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

