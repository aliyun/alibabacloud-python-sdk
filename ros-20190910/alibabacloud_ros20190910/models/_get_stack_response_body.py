# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetStackResponseBody(DaraModel):
    def __init__(
        self,
        checked_stack_resource_count: int = None,
        create_time: str = None,
        deletion_protection: str = None,
        description: str = None,
        disable_rollback: bool = None,
        drift_detection_time: str = None,
        interface: str = None,
        log: main_models.GetStackResponseBodyLog = None,
        not_checked_stack_resource_count: int = None,
        notification_urls: List[str] = None,
        operation_info: main_models.GetStackResponseBodyOperationInfo = None,
        order_ids: List[str] = None,
        outputs: List[Dict[str, Any]] = None,
        parameters: List[main_models.GetStackResponseBodyParameters] = None,
        parent_stack_id: str = None,
        ram_role_name: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resource_progress: main_models.GetStackResponseBodyResourceProgress = None,
        rollback_failed_root_reason: str = None,
        root_stack_id: str = None,
        service_managed: bool = None,
        service_name: str = None,
        stack_drift_status: str = None,
        stack_id: str = None,
        stack_name: str = None,
        stack_type: str = None,
        status: str = None,
        status_reason: str = None,
        tags: List[main_models.GetStackResponseBodyTags] = None,
        template_description: str = None,
        template_id: str = None,
        template_scratch_id: str = None,
        template_url: str = None,
        template_version: str = None,
        timeout_in_minutes: int = None,
        update_time: str = None,
    ):
        # The number of resources on which drift detection was performed.
        # 
        # >  This parameter is returned only if the most recent drift detection on the stack was successful.
        self.checked_stack_resource_count = checked_stack_resource_count
        # The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # Indicates whether deletion protection is enabled for the stack. Valid values:
        # 
        # *   Enabled: Deletion protection is enabled for the stack.
        # *   Disabled: Deletion protection is disabled for the stack. You can delete the stack by using the ROS console or by calling the DeleteStack operation.
        # 
        # >  Deletion protection of a nested stack is the same as deletion protection of its root stack.
        self.deletion_protection = deletion_protection
        # The description of the stack.
        self.description = description
        # Indicates whether rollback is disabled when the stack fails to be created. Valid values:
        # 
        # *   true
        # *   false (default)
        self.disable_rollback = disable_rollback
        # The time when the most recent successful drift detection was performed on the stack.
        self.drift_detection_time = drift_detection_time
        # The description of the console user interface (UI).
        self.interface = interface
        # The log of the stack.
        self.log = log
        # The number of resources on which drift detection was not performed.
        # 
        # >  This parameter is returned only if the most recent drift detection on the stack was successful.
        self.not_checked_stack_resource_count = not_checked_stack_resource_count
        # The callback URLs for receiving stack events.
        self.notification_urls = notification_urls
        # The supplementary information that is returned if an error occurs on a stack operation.
        # 
        # >  This parameter is returned together with at least one sub-parameter and only under specific conditions. For example, the supplementary information is returned when an API operation of another Alibaba Cloud service fails to be called.
        self.operation_info = operation_info
        # The order IDs. This parameter is returned only if you configured manual payment when you created a subscription stack.
        self.order_ids = order_ids
        # The outputs of the stack.
        self.outputs = outputs
        # The parameters of the stack.
        self.parameters = parameters
        # The ID of the parent stack.
        self.parent_stack_id = parent_stack_id
        # The name of the Resource Access Management (RAM) role. ROS assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.\\
        # ROS assumes the RAM role to perform operations on the stack. If you have permissions to perform operations on the stack, ROS assumes the RAM role even if you do not have permissions to use the RAM role. You must make sure that permissions are granted to the RAM role based on the principle of least privilege.\\
        # If this parameter is not specified, ROS uses the existing role that is associated with the stack. If no roles are available, ROS uses a temporary credential that is generated from the credentials of your account.\\
        # The RAM role name can be up to 64 characters in length.
        self.ram_role_name = ram_role_name
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The resource creation progress.
        self.resource_progress = resource_progress
        # 当资源栈状态为回滚失败时，该字段展示导致回滚的前一阶段执行失败的原因。
        self.rollback_failed_root_reason = rollback_failed_root_reason
        # The ID of the root stack. This parameter is returned if the specified stack is a nested stack.
        self.root_stack_id = root_stack_id
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
        # The stack name.\\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (_). The name must start with a digit or letter.
        self.stack_name = stack_name
        # The stack type. Valid values:
        # 
        # *   ROS: ROS stack. The stack is created by using a ROS template.
        # *   Terraform: Terraform stack. The stack is created by using a Terraform template.
        self.stack_type = stack_type
        # The state of the stack. Valid values:
        # 
        # *   CREATE_IN_PROGRESS: The stack is being created.
        # *   CREATE_FAILED: The stack failed to be created.
        # *   CREATE_COMPLETE: The stack is created.
        # *   UPDATE_IN_PROGRESS: The stack is being updated.
        # *   UPDATE_FAILED: The stack failed to be updated.
        # *   UPDATE_COMPLETE: The stack is updated.
        # *   DELETE_IN_PROGRESS: The stack is being deleted.
        # *   DELETE_FAILED: The stack failed to be deleted.
        # *   CREATE_ROLLBACK_IN_PROGRESS: The resources are being rolled back after the stack failed to be created.
        # *   CREATE_ROLLBACK_FAILED: The resources failed to be rolled back after the stack failed to be created.
        # *   CREATE_ROLLBACK_COMPLETE: The resources are rolled back after the stack failed to be created.
        # *   ROLLBACK_IN_PROGRESS: The resources of the stack are being rolled back.
        # *   ROLLBACK_FAILED: The resources of the stack failed to be rolled back.
        # *   ROLLBACK_COMPLETE: The resources of the stack are rolled back.
        # *   CHECK_IN_PROGRESS: The stack is being validated.
        # *   CHECK_FAILED: The stack failed to be validated.
        # *   CHECK_COMPLETE: The stack is validated.
        # *   REVIEW_IN_PROGRESS: The stack is being reviewed.
        # *   IMPORT_CREATE_IN_PROGRESS: The stack is being created by using imported resources.
        # *   IMPORT_CREATE_FAILED: The stack failed to be created by using imported resources.
        # *   IMPORT_CREATE_COMPLETE: The stack is created by using imported resources.
        # *   IMPORT_CREATE_ROLLBACK_IN_PROGRESS: The resources are being rolled back after the stack failed to be created by using imported resources.
        # *   IMPORT_CREATE_ROLLBACK_FAILED: The resources failed to be rolled back after the stack failed to be created by using imported resources.
        # *   IMPORT_CREATE_ROLLBACK_COMPLETE: The resources are rolled back after the stack failed to be created by using imported resources.
        # *   IMPORT_UPDATE_IN_PROGRESS: The stack is being updated by using imported resources.
        # *   IMPORT_UPDATE_FAILED: The stack failed to be updated by using imported resources.
        # *   IMPORT_UPDATE_COMPLETE: The stack is updated by using imported resources.
        # *   IMPORT_UPDATE_ROLLBACK_IN_PROGRESS: The resources are being rolled back after the stack failed to be updated by using imported resources.
        # *   IMPORT_UPDATE_ROLLBACK_FAILED: The resources failed to be rolled back after the stack failed to be updated by using imported resources.
        # *   IMPORT_UPDATE_ROLLBACK_COMPLETE: The resources are rolled back after the stack failed to be updated by using imported resources.
        self.status = status
        # The reason why the stack is in its current state.
        self.status_reason = status_reason
        # The tags of the stack.
        self.tags = tags
        # The description of the template.
        self.template_description = template_description
        # The template ID. This parameter is returned only if the current stack template is a custom template or shared template.
        # 
        # If the template is a shared template, the value of this parameter is the same as the value of TemplateARN.
        self.template_id = template_id
        # The ID of the resource scenario. This parameter is returned only if the current template of the stack is generated from a resource scenario.
        self.template_scratch_id = template_scratch_id
        # The URL of the file that contains the template body. This parameter is returned only if the current template of the stack is from a URL. The URL can point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket.
        self.template_url = template_url
        # The version of the template. This parameter is returned only if the current stack template is a custom template or shared template.
        # 
        # If the template is a shared template, this parameter is returned only if VersionOption is set to AllVersions.
        # 
        # Valid values: v1 to v100.
        self.template_version = template_version
        # The timeout period for creating the stack. Unit: minutes.
        self.timeout_in_minutes = timeout_in_minutes
        # The time when the stack was updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        if self.log:
            self.log.validate()
        if self.operation_info:
            self.operation_info.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.resource_progress:
            self.resource_progress.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checked_stack_resource_count is not None:
            result['CheckedStackResourceCount'] = self.checked_stack_resource_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.description is not None:
            result['Description'] = self.description

        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback

        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time

        if self.interface is not None:
            result['Interface'] = self.interface

        if self.log is not None:
            result['Log'] = self.log.to_map()

        if self.not_checked_stack_resource_count is not None:
            result['NotCheckedStackResourceCount'] = self.not_checked_stack_resource_count

        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls

        if self.operation_info is not None:
            result['OperationInfo'] = self.operation_info.to_map()

        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_progress is not None:
            result['ResourceProgress'] = self.resource_progress.to_map()

        if self.rollback_failed_root_reason is not None:
            result['RollbackFailedRootReason'] = self.rollback_failed_root_reason

        if self.root_stack_id is not None:
            result['RootStackId'] = self.root_stack_id

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

        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckedStackResourceCount') is not None:
            self.checked_stack_resource_count = m.get('CheckedStackResourceCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')

        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')

        if m.get('Interface') is not None:
            self.interface = m.get('Interface')

        if m.get('Log') is not None:
            temp_model = main_models.GetStackResponseBodyLog()
            self.log = temp_model.from_map(m.get('Log'))

        if m.get('NotCheckedStackResourceCount') is not None:
            self.not_checked_stack_resource_count = m.get('NotCheckedStackResourceCount')

        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')

        if m.get('OperationInfo') is not None:
            temp_model = main_models.GetStackResponseBodyOperationInfo()
            self.operation_info = temp_model.from_map(m.get('OperationInfo'))

        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GetStackResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceProgress') is not None:
            temp_model = main_models.GetStackResponseBodyResourceProgress()
            self.resource_progress = temp_model.from_map(m.get('ResourceProgress'))

        if m.get('RollbackFailedRootReason') is not None:
            self.rollback_failed_root_reason = m.get('RollbackFailedRootReason')

        if m.get('RootStackId') is not None:
            self.root_stack_id = m.get('RootStackId')

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
                temp_model = main_models.GetStackResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetStackResponseBodyTags(DaraModel):
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

class GetStackResponseBodyResourceProgress(DaraModel):
    def __init__(
        self,
        failed_resource_count: int = None,
        in_progress_resource_count: int = None,
        in_progress_resource_details: List[main_models.GetStackResponseBodyResourceProgressInProgressResourceDetails] = None,
        pending_resource_count: int = None,
        stack_action_progress: float = None,
        stack_operation_progress: float = None,
        success_resource_count: int = None,
        total_resource_count: int = None,
    ):
        # The number of resources that failed to be created.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
        self.failed_resource_count = failed_resource_count
        # The number of resources that are being created.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
        self.in_progress_resource_count = in_progress_resource_count
        # The progress details of resources that are being created.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
        self.in_progress_resource_details = in_progress_resource_details
        # The number of resources to be created.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
        self.pending_resource_count = pending_resource_count
        # The creation or rollback progress of the stack, in percentage. Valid values: 0 to 100.
        # 
        # The value progressively increases from 0 to 100 during a stack creation operation. If the stack is created, the value reaches 100. If the stack fails to be created, a rollback is started for the stack resources, and the value progressively increases from the percentage of the remaining progress (100 - Progress value generated when the stack fails to be created). The value increases to 100 when the stack resources are rolled back. This parameter indicates the creation progress during a stack creation operation and indicates the rollback progress during a stack rollback operation.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `PercentageOnly`.
        self.stack_action_progress = stack_action_progress
        # The overall creation progress of the stack, in percentage. Valid values: 0 to 100.
        # 
        # The value progressively increases from 0 to 100 during a stack creation operation. If the stack is created, the value reaches 100. If the stack fails to be created, a rollback is started for the stack resources, and the value progressively decreases. The value decreases to 0 when the stack resources are rolled back. This parameter indicates only the overall creation progress, regardless of whether during a stack creation or rollback operation.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `PercentageOnly`.
        self.stack_operation_progress = stack_operation_progress
        # The number of resources that are created.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
        self.success_resource_count = success_resource_count
        # The total number of resources.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
        self.total_resource_count = total_resource_count

    def validate(self):
        if self.in_progress_resource_details:
            for v1 in self.in_progress_resource_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_resource_count is not None:
            result['FailedResourceCount'] = self.failed_resource_count

        if self.in_progress_resource_count is not None:
            result['InProgressResourceCount'] = self.in_progress_resource_count

        result['InProgressResourceDetails'] = []
        if self.in_progress_resource_details is not None:
            for k1 in self.in_progress_resource_details:
                result['InProgressResourceDetails'].append(k1.to_map() if k1 else None)

        if self.pending_resource_count is not None:
            result['PendingResourceCount'] = self.pending_resource_count

        if self.stack_action_progress is not None:
            result['StackActionProgress'] = self.stack_action_progress

        if self.stack_operation_progress is not None:
            result['StackOperationProgress'] = self.stack_operation_progress

        if self.success_resource_count is not None:
            result['SuccessResourceCount'] = self.success_resource_count

        if self.total_resource_count is not None:
            result['TotalResourceCount'] = self.total_resource_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedResourceCount') is not None:
            self.failed_resource_count = m.get('FailedResourceCount')

        if m.get('InProgressResourceCount') is not None:
            self.in_progress_resource_count = m.get('InProgressResourceCount')

        self.in_progress_resource_details = []
        if m.get('InProgressResourceDetails') is not None:
            for k1 in m.get('InProgressResourceDetails'):
                temp_model = main_models.GetStackResponseBodyResourceProgressInProgressResourceDetails()
                self.in_progress_resource_details.append(temp_model.from_map(k1))

        if m.get('PendingResourceCount') is not None:
            self.pending_resource_count = m.get('PendingResourceCount')

        if m.get('StackActionProgress') is not None:
            self.stack_action_progress = m.get('StackActionProgress')

        if m.get('StackOperationProgress') is not None:
            self.stack_operation_progress = m.get('StackOperationProgress')

        if m.get('SuccessResourceCount') is not None:
            self.success_resource_count = m.get('SuccessResourceCount')

        if m.get('TotalResourceCount') is not None:
            self.total_resource_count = m.get('TotalResourceCount')

        return self

class GetStackResponseBodyResourceProgressInProgressResourceDetails(DaraModel):
    def __init__(
        self,
        progress_target_value: float = None,
        progress_value: float = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The desired progress value of the resource.
        self.progress_target_value = progress_target_value
        # The current progress value of the resource.
        self.progress_value = progress_value
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.progress_target_value is not None:
            result['ProgressTargetValue'] = self.progress_target_value

        if self.progress_value is not None:
            result['ProgressValue'] = self.progress_value

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProgressTargetValue') is not None:
            self.progress_target_value = m.get('ProgressTargetValue')

        if m.get('ProgressValue') is not None:
            self.progress_value = m.get('ProgressValue')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class GetStackResponseBodyParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The parameter name.
        self.parameter_key = parameter_key
        # The parameter value.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

class GetStackResponseBodyOperationInfo(DaraModel):
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
        # The logical ID of the resource on which the operation error occurs.
        self.logical_resource_id = logical_resource_id
        # The error message.
        self.message = message
        # The ID of the request that is initiated to call the API operation of another Alibaba Cloud service.
        self.request_id = request_id
        # The type of the resource on which the operation error occurs.
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

class GetStackResponseBodyLog(DaraModel):
    def __init__(
        self,
        resource_logs: List[main_models.GetStackResponseBodyLogResourceLogs] = None,
        terraform_logs: List[main_models.GetStackResponseBodyLogTerraformLogs] = None,
    ):
        # The logs of resources in the stack. This parameter is returned if LogOption is set to Resource or All.
        # 
        # >  The logs are returned only for resources of specific types, such as the `ALIYUN::ROS::ResourceCleaner` type.
        self.resource_logs = resource_logs
        # The logs generated when the Terraform stack is run. This parameter is returned only for a Terraform stack. This parameter is returned if LogOption is left empty or set to Stack or All.
        # 
        # >  This parameter is not returned for a running stack. The logs are generated from the most recent operation on the stack, such as the creation, resumed creation, update, or deletion operation.
        self.terraform_logs = terraform_logs

    def validate(self):
        if self.resource_logs:
            for v1 in self.resource_logs:
                 if v1:
                    v1.validate()
        if self.terraform_logs:
            for v1 in self.terraform_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourceLogs'] = []
        if self.resource_logs is not None:
            for k1 in self.resource_logs:
                result['ResourceLogs'].append(k1.to_map() if k1 else None)

        result['TerraformLogs'] = []
        if self.terraform_logs is not None:
            for k1 in self.terraform_logs:
                result['TerraformLogs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_logs = []
        if m.get('ResourceLogs') is not None:
            for k1 in m.get('ResourceLogs'):
                temp_model = main_models.GetStackResponseBodyLogResourceLogs()
                self.resource_logs.append(temp_model.from_map(k1))

        self.terraform_logs = []
        if m.get('TerraformLogs') is not None:
            for k1 in m.get('TerraformLogs'):
                temp_model = main_models.GetStackResponseBodyLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k1))

        return self

class GetStackResponseBodyLogTerraformLogs(DaraModel):
    def __init__(
        self,
        command: str = None,
        content: str = None,
        stream: str = None,
    ):
        # The name of the Terraform command that is run. Valid values:
        # 
        # *   apply
        # *   plan
        # *   destroy
        # *   version
        # 
        # For more information about Terraform commands, see [Basic CLI Features](https://www.terraform.io/cli/commands).
        self.command = command
        # The content of the output stream that is returned after the command is run.
        self.content = content
        # The output stream. Valid values:
        # 
        # *   stdout: standard output stream
        # *   stderr: standard error stream
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        if self.content is not None:
            result['Content'] = self.content

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

class GetStackResponseBodyLogResourceLogs(DaraModel):
    def __init__(
        self,
        logs: List[main_models.GetStackResponseBodyLogResourceLogsLogs] = None,
        resource_name: str = None,
    ):
        # All the logs that are associated with the resources.
        self.logs = logs
        # The name of the resource that is defined in the template.
        self.resource_name = resource_name

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.GetStackResponseBodyLogResourceLogsLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        return self

class GetStackResponseBodyLogResourceLogsLogs(DaraModel):
    def __init__(
        self,
        content: str = None,
        keys: List[str] = None,
    ):
        # The content of a resource log.
        self.content = content
        # The keywords of a resource log.
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.keys is not None:
            result['Keys'] = self.keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Keys') is not None:
            self.keys = m.get('Keys')

        return self

