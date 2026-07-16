# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetStackGroupOperationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stack_group_operation: main_models.GetStackGroupOperationResponseBodyStackGroupOperation = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the stack group operation.
        self.stack_group_operation = stack_group_operation

    def validate(self):
        if self.stack_group_operation:
            self.stack_group_operation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stack_group_operation is not None:
            result['StackGroupOperation'] = self.stack_group_operation.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StackGroupOperation') is not None:
            temp_model = main_models.GetStackGroupOperationResponseBodyStackGroupOperation()
            self.stack_group_operation = temp_model.from_map(m.get('StackGroupOperation'))

        return self

class GetStackGroupOperationResponseBodyStackGroupOperation(DaraModel):
    def __init__(
        self,
        action: str = None,
        administration_role_name: str = None,
        create_time: str = None,
        deployment_targets: main_models.GetStackGroupOperationResponseBodyStackGroupOperationDeploymentTargets = None,
        end_time: str = None,
        execution_role_name: str = None,
        operation_description: str = None,
        operation_id: str = None,
        operation_preferences: main_models.GetStackGroupOperationResponseBodyStackGroupOperationOperationPreferences = None,
        retain_stacks: bool = None,
        stack_group_drift_detection_detail: main_models.GetStackGroupOperationResponseBodyStackGroupOperationStackGroupDriftDetectionDetail = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
        status: str = None,
    ):
        # The operation type.
        # 
        # Valid values:
        # 
        # *   CREATE
        # *   UPDATE
        # *   DELETE
        # *   DETECT_DRIFT
        self.action = action
        # The name of the RAM role that you specify for the administrator account when you create the self-managed stack group. ROS assumes the administrator role to perform operations. If this parameter is not specified, the default value AliyunROSStackGroupAdministrationRole is returned.
        self.administration_role_name = administration_role_name
        # The time when the operation was initiated.
        self.create_time = create_time
        # The destinations to deploy stack instances when the stack is granted service-managed permissions.
        self.deployment_targets = deployment_targets
        # The time when the operation ended.
        self.end_time = end_time
        # The name of the RAM role that you specify for the execution account when you create the self-managed stack group. The administrator role AliyunROSStackGroupAdministrationRole assumes the execution role to perform operations. If this parameter is not specified, the default value AliyunROSStackGroupExecutionRole is returned.
        self.execution_role_name = execution_role_name
        # The description of the operation.
        # 
        # > This parameter is returned only if OperationDescription is specified when the [CreateStackInstances](https://help.aliyun.com/document_detail/151338.html) operation is called to create stack instances.
        self.operation_description = operation_description
        # The operation ID.
        self.operation_id = operation_id
        # The operation settings.
        self.operation_preferences = operation_preferences
        # Indicates whether stacks are retained when the associated stack instances are deleted. When you delete a stack instance, you can choose to delete or retain the stack with which the stack instance is associated.
        # 
        # Valid values:
        # 
        # *   true: Stacks are retained when the associated stack instances are deleted.
        # *   false: Stacks are deleted when the associated stack instances are deleted. Proceed with caution.
        # 
        # > This parameter is returned only if you delete stack instances.
        self.retain_stacks = retain_stacks
        # The information about drift detection.
        # 
        # > This parameter is returned only if drift detection is performed.
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail
        # The ID of the stack group.
        self.stack_group_id = stack_group_id
        # The name of the stack group.
        self.stack_group_name = stack_group_name
        # The state of the operation.
        # 
        # Valid values:
        # 
        # *   RUNNING
        # *   SUCCEEDED
        # *   FAILED
        # *   STOPPING
        # *   STOPPED
        self.status = status

    def validate(self):
        if self.deployment_targets:
            self.deployment_targets.validate()
        if self.operation_preferences:
            self.operation_preferences.validate()
        if self.stack_group_drift_detection_detail:
            self.stack_group_drift_detection_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name

        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences.to_map()

        if self.retain_stacks is not None:
            result['RetainStacks'] = self.retain_stacks

        if self.stack_group_drift_detection_detail is not None:
            result['StackGroupDriftDetectionDetail'] = self.stack_group_drift_detection_detail.to_map()

        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeploymentTargets') is not None:
            temp_model = main_models.GetStackGroupOperationResponseBodyStackGroupOperationDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m.get('DeploymentTargets'))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')

        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('OperationPreferences') is not None:
            temp_model = main_models.GetStackGroupOperationResponseBodyStackGroupOperationOperationPreferences()
            self.operation_preferences = temp_model.from_map(m.get('OperationPreferences'))

        if m.get('RetainStacks') is not None:
            self.retain_stacks = m.get('RetainStacks')

        if m.get('StackGroupDriftDetectionDetail') is not None:
            temp_model = main_models.GetStackGroupOperationResponseBodyStackGroupOperationStackGroupDriftDetectionDetail()
            self.stack_group_drift_detection_detail = temp_model.from_map(m.get('StackGroupDriftDetectionDetail'))

        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetStackGroupOperationResponseBodyStackGroupOperationStackGroupDriftDetectionDetail(DaraModel):
    def __init__(
        self,
        cancelled_stack_instances_count: int = None,
        drift_detection_status: str = None,
        drift_detection_time: str = None,
        drifted_stack_instances_count: int = None,
        failed_stack_instances_count: int = None,
        in_progress_stack_instances_count: int = None,
        in_sync_stack_instances_count: int = None,
        stack_group_drift_status: str = None,
        total_stack_instances_count: int = None,
    ):
        # The number of stack instances for which drift detection was canceled.
        self.cancelled_stack_instances_count = cancelled_stack_instances_count
        # The drift detection state.
        # 
        # Valid values:
        # 
        # *   COMPLETED: Drift detection is performed on the stack group and all stack instances passed the drift detection.
        # *   FAILED: Drift detection is performed on the stack group. The number of stack instances that failed the drift detection exceeds the specified threshold.
        # *   PARTIAL_SUCCESS: Drift detection is performed on the stack group. The number of stack instances that failed the drift detection does not exceed the specified threshold.
        # *   IN_PROGRESS: Drift detection is being performed on the stack group.
        # *   STOPPED: Drift detection is canceled for the stack group.
        self.drift_detection_status = drift_detection_status
        # The time when drift detection was performed.
        self.drift_detection_time = drift_detection_time
        # The number of stack instances that have drifted.
        self.drifted_stack_instances_count = drifted_stack_instances_count
        # The number of stack instances that failed drift detection.
        self.failed_stack_instances_count = failed_stack_instances_count
        # The number of stack instances on which drift detection was being performed.
        self.in_progress_stack_instances_count = in_progress_stack_instances_count
        # The number of stack instances that were being synchronized.
        self.in_sync_stack_instances_count = in_sync_stack_instances_count
        # The drift state of the stack group.
        # 
        # Valid values:
        # 
        # *   DRIFTED: At least one stack instance in the stack group has drifted.
        # *   NOT_CHECKED: No successful drift detection is performed in the stack group.
        # *   IN_SYNC: All the stack instances in the stack group are being synchronized.
        self.stack_group_drift_status = stack_group_drift_status
        # The number of stack instances.
        self.total_stack_instances_count = total_stack_instances_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancelled_stack_instances_count is not None:
            result['CancelledStackInstancesCount'] = self.cancelled_stack_instances_count

        if self.drift_detection_status is not None:
            result['DriftDetectionStatus'] = self.drift_detection_status

        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time

        if self.drifted_stack_instances_count is not None:
            result['DriftedStackInstancesCount'] = self.drifted_stack_instances_count

        if self.failed_stack_instances_count is not None:
            result['FailedStackInstancesCount'] = self.failed_stack_instances_count

        if self.in_progress_stack_instances_count is not None:
            result['InProgressStackInstancesCount'] = self.in_progress_stack_instances_count

        if self.in_sync_stack_instances_count is not None:
            result['InSyncStackInstancesCount'] = self.in_sync_stack_instances_count

        if self.stack_group_drift_status is not None:
            result['StackGroupDriftStatus'] = self.stack_group_drift_status

        if self.total_stack_instances_count is not None:
            result['TotalStackInstancesCount'] = self.total_stack_instances_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelledStackInstancesCount') is not None:
            self.cancelled_stack_instances_count = m.get('CancelledStackInstancesCount')

        if m.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = m.get('DriftDetectionStatus')

        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')

        if m.get('DriftedStackInstancesCount') is not None:
            self.drifted_stack_instances_count = m.get('DriftedStackInstancesCount')

        if m.get('FailedStackInstancesCount') is not None:
            self.failed_stack_instances_count = m.get('FailedStackInstancesCount')

        if m.get('InProgressStackInstancesCount') is not None:
            self.in_progress_stack_instances_count = m.get('InProgressStackInstancesCount')

        if m.get('InSyncStackInstancesCount') is not None:
            self.in_sync_stack_instances_count = m.get('InSyncStackInstancesCount')

        if m.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = m.get('StackGroupDriftStatus')

        if m.get('TotalStackInstancesCount') is not None:
            self.total_stack_instances_count = m.get('TotalStackInstancesCount')

        return self

class GetStackGroupOperationResponseBodyStackGroupOperationOperationPreferences(DaraModel):
    def __init__(
        self,
        failure_tolerance_count: int = None,
        failure_tolerance_percentage: int = None,
        max_concurrent_count: int = None,
        max_concurrent_percentage: int = None,
        region_ids_order: List[str] = None,
    ):
        # The number of accounts within which stack operation failures are allowed to occur in each region. If the value of this parameter is exceeded in a region, Resource Orchestration Service (ROS) stops the operation in the region. If the operation is stopped in one region, the operation is no longer performed in other regions.
        # 
        # Valid values: 0 to 20.
        # 
        # > Only one of FailureToleranceCount and FailureTolerancePercentage can be returned.
        self.failure_tolerance_count = failure_tolerance_count
        # The percentage of the number of accounts within which stack operation failures are allowed to occur to the total number of accounts in each region. If the value of this parameter is exceeded in a region, ROS stops the operation in the region.
        # 
        # Valid values: 0 to 100.
        # 
        # > Only one of FailureToleranceCount and FailureTolerancePercentage can be returned.
        self.failure_tolerance_percentage = failure_tolerance_percentage
        # The maximum number of accounts within which stacks are deployed at the same time in each region.
        # 
        # Valid values: 1 to 20.
        # 
        # > Only one of MaxConcurrentCount and MaxConcurrentPercentage can be returned.
        self.max_concurrent_count = max_concurrent_count
        # The percentage of the maximum number of accounts within which stacks are deployed at the same time to the total number of accounts in each region.
        # 
        # Valid values: 1 to 100.
        # 
        # > Only one of MaxConcurrentCount and MaxConcurrentPercentage can be returned.
        self.max_concurrent_percentage = max_concurrent_percentage
        # The regions in the order of operation execution.
        self.region_ids_order = region_ids_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_tolerance_count is not None:
            result['FailureToleranceCount'] = self.failure_tolerance_count

        if self.failure_tolerance_percentage is not None:
            result['FailureTolerancePercentage'] = self.failure_tolerance_percentage

        if self.max_concurrent_count is not None:
            result['MaxConcurrentCount'] = self.max_concurrent_count

        if self.max_concurrent_percentage is not None:
            result['MaxConcurrentPercentage'] = self.max_concurrent_percentage

        if self.region_ids_order is not None:
            result['RegionIdsOrder'] = self.region_ids_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureToleranceCount') is not None:
            self.failure_tolerance_count = m.get('FailureToleranceCount')

        if m.get('FailureTolerancePercentage') is not None:
            self.failure_tolerance_percentage = m.get('FailureTolerancePercentage')

        if m.get('MaxConcurrentCount') is not None:
            self.max_concurrent_count = m.get('MaxConcurrentCount')

        if m.get('MaxConcurrentPercentage') is not None:
            self.max_concurrent_percentage = m.get('MaxConcurrentPercentage')

        if m.get('RegionIdsOrder') is not None:
            self.region_ids_order = m.get('RegionIdsOrder')

        return self

class GetStackGroupOperationResponseBodyStackGroupOperationDeploymentTargets(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        rd_folder_ids: List[str] = None,
    ):
        # The IDs of the members in the resource directory.
        # 
        # > This parameter is returned only if AccountIds is specified when the [UpdateStackInstances](https://help.aliyun.com/document_detail/151716.html) operation is called to update stack instances.
        self.account_ids = account_ids
        # The IDs of the folders in the resource directory.
        self.rd_folder_ids = rd_folder_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')

        return self

