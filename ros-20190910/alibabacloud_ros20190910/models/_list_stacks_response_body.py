# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListStacksResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stacks: List[main_models.ListStacksResponseBodyStacks] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Details of the stacks.
        self.stacks = stacks
        # The total number of stacks.
        self.total_count = total_count

    def validate(self):
        if self.stacks:
            for v1 in self.stacks:
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

        result['Stacks'] = []
        if self.stacks is not None:
            for k1 in self.stacks:
                result['Stacks'].append(k1.to_map() if k1 else None)

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

        self.stacks = []
        if m.get('Stacks') is not None:
            for k1 in m.get('Stacks'):
                temp_model = main_models.ListStacksResponseBodyStacks()
                self.stacks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListStacksResponseBodyStacks(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_protection: str = None,
        disable_rollback: bool = None,
        drift_detection_time: str = None,
        operation_info: main_models.ListStacksResponseBodyStacksOperationInfo = None,
        parent_stack_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_managed: bool = None,
        service_name: str = None,
        stack_drift_status: str = None,
        stack_id: str = None,
        stack_name: str = None,
        stack_type: str = None,
        status: str = None,
        status_reason: str = None,
        tags: List[main_models.ListStacksResponseBodyStacksTags] = None,
        timeout_in_minutes: int = None,
        update_time: str = None,
    ):
        # The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # Indicates whether deletion protection is enabled for the stack. Valid values:
        # 
        # *   Enabled: Deletion protection is enabled for the stack.
        # *   Disabled: Deletion protection is disabled for the stack. In this case, you can delete the stack by using the console or calling the [DeleteStack](https://help.aliyun.com/document_detail/610812.html) operation.
        # 
        # >  Deletion protection of a nested stack is the same as that of its root stack.
        self.deletion_protection = deletion_protection
        # Indicates whether rollback is disabled when the stack fails to be created. Valid values:
        # 
        # *   true
        # *   false (default)
        self.disable_rollback = disable_rollback
        # The time when the most recent successful drift detection was performed on the stack.
        self.drift_detection_time = drift_detection_time
        # The supplementary information that is returned if an error occurs on a stack operation.
        # 
        # >  This parameter is returned only under specific conditions, and is returned together with at least one sub-parameter. For example, an error occurred when an API operation of another Alibaba Cloud service was called.
        self.operation_info = operation_info
        # The ID of the parent stack.
        self.parent_stack_id = parent_stack_id
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether the stack is a managed stack. Valid values:
        # 
        # *   true
        # *   false
        self.service_managed = service_managed
        # The name of the service to which the managed stack belongs.
        self.service_name = service_name
        # The state of the stack on which the most recent successful drift detection was performed. Valid values:
        # 
        # *   DRIFTED: The stack has drifted.
        # *   NOT_CHECKED: No successful drift detection is performed on the stack.
        # *   IN_SYNC: The stack is being synchronized.
        self.stack_drift_status = stack_drift_status
        # The stack ID.
        self.stack_id = stack_id
        # The stack name.
        self.stack_name = stack_name
        # The stack type. Valid values:
        # 
        # *   ROS: ROS stack. The stack is created by using a ROS template.
        # *   Terraform: Terraform stack. The stack is created by using a Terraform template.
        self.stack_type = stack_type
        # The state of the stack.
        self.status = status
        # The reason why the stack is in its current state.
        self.status_reason = status_reason
        # The tags of the stack.
        self.tags = tags
        # The timeout period for creating the stack. Unit: minutes.
        self.timeout_in_minutes = timeout_in_minutes
        # The time when the stack was updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        if self.operation_info:
            self.operation_info.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback

        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time

        if self.operation_info is not None:
            result['OperationInfo'] = self.operation_info.to_map()

        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.stack_name is not None:
            result['StackName'] = self.stack_name

        if self.stack_type is not None:
            result['StackType'] = self.stack_type

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')

        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')

        if m.get('OperationInfo') is not None:
            temp_model = main_models.ListStacksResponseBodyStacksOperationInfo()
            self.operation_info = temp_model.from_map(m.get('OperationInfo'))

        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')

        if m.get('StackType') is not None:
            self.stack_type = m.get('StackType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListStacksResponseBodyStacksTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListStacksResponseBodyStacksTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the stack.
        self.key = key
        # The tag value of the stack.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListStacksResponseBodyStacksOperationInfo(DaraModel):
    def __init__(
        self,
        action: str = None,
        code: str = None,
        logical_resource_id: str = None,
        message: str = None,
        request_id: str = None,
        resource_type: str = None,
    ):
        # The name of the API operation that belongs to another Alibaba Cloud service.
        self.action = action
        # The error code.
        self.code = code
        # The logical ID of the resource on which the operation error occurred.
        self.logical_resource_id = logical_resource_id
        # The error message.
        self.message = message
        # The ID of the request that is initiated to call the API operation of another Alibaba Cloud service.
        self.request_id = request_id
        # The type of the resource on which the operation error occurred.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.code is not None:
            result['Code'] = self.code

        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

