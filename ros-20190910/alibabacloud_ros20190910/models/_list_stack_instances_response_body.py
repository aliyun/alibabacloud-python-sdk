# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListStackInstancesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stack_instances: List[main_models.ListStackInstancesResponseBodyStackInstances] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The stacks.
        self.stack_instances = stack_instances
        # The total number of stacks.
        self.total_count = total_count

    def validate(self):
        if self.stack_instances:
            for v1 in self.stack_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StackInstances'] = []
        if self.stack_instances is not None:
            for k1 in self.stack_instances:
                result['StackInstances'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stack_instances = []
        if m.get('StackInstances') is not None:
            for k1 in m.get('StackInstances'):
                temp_model = main_models.ListStackInstancesResponseBodyStackInstances()
                self.stack_instances.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListStackInstancesResponseBodyStackInstances(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        drift_detection_time: str = None,
        rd_folder_id: str = None,
        region_id: str = None,
        stack_drift_status: str = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
        stack_id: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        # The ID of the destination account to which the stack belongs.
        self.account_id = account_id
        # The time when the last successful drift detection was performed on the stack.
        # 
        # > This parameter is returned only if drift detection is performed on the stack group.
        self.drift_detection_time = drift_detection_time
        # The ID of the folder in the resource directory.
        # 
        # > This parameter is returned only if the stack group is granted service-managed permissions.
        self.rd_folder_id = rd_folder_id
        # The region ID of the stack.
        self.region_id = region_id
        # The state of the stack when the last successful drift detection was performed on the stack group.
        # 
        # Valid values:
        # 
        # *   DRIFTED: The stack has drifted.
        # *   NOT_CHECKED: No successful drift detection is performed on the stack.
        # *   IN_SYNC: The stack is being synchronized.
        # 
        # > This parameter is returned only if drift detection is performed on the stack group.
        self.stack_drift_status = stack_drift_status
        # The ID of the stack group.
        self.stack_group_id = stack_group_id
        # The name of the stack group.
        self.stack_group_name = stack_group_name
        # The stack ID.
        # 
        # > This parameter is returned only if the stack is in the CURRENT state.
        self.stack_id = stack_id
        # The state of the stack.
        # 
        # Valid values:
        # 
        # *   CURRENT: The stack is up-to-date with the stack group.
        # 
        # *   OUTDATED: The stack is not up-to-date with the stack group. Stacks are in the OUTDATED state due to the following possible reasons:
        # 
        #     *   When the CreateStackInstances operation is called to create stacks, the stacks fail to be created.
        #     *   When the UpdateStackInstances or UpdateStackGroup operation is called to update stacks, the stacks fail to be updated, or only specific stacks are updated.
        #     *   The creation or update operation is not complete.
        self.status = status
        # The reason why the stack instance is in the OUTDATED state.
        # 
        # > This parameter is returned only if the stack instance is in the OUTDATED state.
        self.status_reason = status_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time

        if self.rd_folder_id is not None:
            result['RdFolderId'] = self.rd_folder_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status

        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')

        if m.get('RdFolderId') is not None:
            self.rd_folder_id = m.get('RdFolderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')

        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        return self

