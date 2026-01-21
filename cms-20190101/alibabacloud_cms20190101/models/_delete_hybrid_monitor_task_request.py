# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHybridMonitorTaskRequest(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        region_id: str = None,
        target_user_id: str = None,
        task_id: str = None,
    ):
        # The name of the namespace.
        # 
        # The name can contain uppercase letters, lowercase letters, digits, and hyphens (-).
        # 
        # > This parameter is required only if you call this operation to delete metric import tasks for Alibaba Cloud services. In this case, the `TaskType` parameter is set to `aliyun_fc`.
        self.namespace = namespace
        self.region_id = region_id
        # The ID of the member account.
        # 
        # > This parameter is required only if you use a management account to call this operation to query metric import tasks that belong to a member in a resource directory. In this case, the `TaskType` parameter is set to `aliyun_fc`.
        self.target_user_id = target_user_id
        # The ID of the metric import task.
        # 
        # For information about how to obtain the ID of a metric import task, see [DescribeHybridMonitorTaskList](https://help.aliyun.com/document_detail/428624.html).
        # 
        # > This parameter is required only if you call this operation to delete metrics for the logs that are imported from Log Service. In this case, the `TaskType` parameter is set to `aliyun_sls`.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

