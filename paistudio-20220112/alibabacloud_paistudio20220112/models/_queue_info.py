# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class QueueInfo(DaraModel):
    def __init__(
        self,
        code: str = None,
        code_type: str = None,
        gmt_created_time: str = None,
        gmt_dequeued_time: str = None,
        gmt_enqueued_time: str = None,
        gmt_position_modified_time: str = None,
        name: str = None,
        position: int = None,
        priority: int = None,
        queue_strategy: str = None,
        quota_id: str = None,
        reason: str = None,
        resource: main_models.ResourceAmount = None,
        status: str = None,
        use_oversold_resource: bool = None,
        user_id: str = None,
        user_name: str = None,
        workload_id: str = None,
        workload_name: str = None,
        workload_status: str = None,
        workload_type: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.code = code
        self.code_type = code_type
        self.gmt_created_time = gmt_created_time
        self.gmt_dequeued_time = gmt_dequeued_time
        self.gmt_enqueued_time = gmt_enqueued_time
        self.gmt_position_modified_time = gmt_position_modified_time
        self.name = name
        self.position = position
        self.priority = priority
        self.queue_strategy = queue_strategy
        self.quota_id = quota_id
        self.reason = reason
        self.resource = resource
        self.status = status
        self.use_oversold_resource = use_oversold_resource
        self.user_id = user_id
        self.user_name = user_name
        self.workload_id = workload_id
        self.workload_name = workload_name
        self.workload_status = workload_status
        self.workload_type = workload_type
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.code_type is not None:
            result['CodeType'] = self.code_type

        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time

        if self.gmt_dequeued_time is not None:
            result['GmtDequeuedTime'] = self.gmt_dequeued_time

        if self.gmt_enqueued_time is not None:
            result['GmtEnqueuedTime'] = self.gmt_enqueued_time

        if self.gmt_position_modified_time is not None:
            result['GmtPositionModifiedTime'] = self.gmt_position_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.position is not None:
            result['Position'] = self.position

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.queue_strategy is not None:
            result['QueueStrategy'] = self.queue_strategy

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.use_oversold_resource is not None:
            result['UseOversoldResource'] = self.use_oversold_resource

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeType') is not None:
            self.code_type = m.get('CodeType')

        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')

        if m.get('GmtDequeuedTime') is not None:
            self.gmt_dequeued_time = m.get('GmtDequeuedTime')

        if m.get('GmtEnqueuedTime') is not None:
            self.gmt_enqueued_time = m.get('GmtEnqueuedTime')

        if m.get('GmtPositionModifiedTime') is not None:
            self.gmt_position_modified_time = m.get('GmtPositionModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('QueueStrategy') is not None:
            self.queue_strategy = m.get('QueueStrategy')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Resource') is not None:
            temp_model = main_models.ResourceAmount()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UseOversoldResource') is not None:
            self.use_oversold_resource = m.get('UseOversoldResource')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

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

