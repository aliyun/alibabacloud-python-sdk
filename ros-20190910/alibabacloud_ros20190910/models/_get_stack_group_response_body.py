# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetStackGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stack_group: main_models.GetStackGroupResponseBodyStackGroup = None,
    ):
        # The details of the stack group.
        self.request_id = request_id
        # Details of the stack group.
        self.stack_group = stack_group

    def validate(self):
        if self.stack_group:
            self.stack_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stack_group is not None:
            result['StackGroup'] = self.stack_group.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StackGroup') is not None:
            temp_model = main_models.GetStackGroupResponseBodyStackGroup()
            self.stack_group = temp_model.from_map(m.get('StackGroup'))

        return self

class GetStackGroupResponseBodyStackGroup(DaraModel):
    def __init__(
        self,
        administration_role_name: str = None,
        auto_deployment: main_models.GetStackGroupResponseBodyStackGroupAutoDeployment = None,
        create_time: str = None,
        description: str = None,
        execution_role_name: str = None,
        parameters: List[main_models.GetStackGroupResponseBodyStackGroupParameters] = None,
        permission_model: str = None,
        rd_folder_ids: List[str] = None,
        resource_group_id: str = None,
        stack_group_drift_detection_detail: main_models.GetStackGroupResponseBodyStackGroupStackGroupDriftDetectionDetail = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
        status: str = None,
        template_body: str = None,
        template_content: str = None,
        update_time: str = None,
    ):
        # The parameters of the stack group.
        self.administration_role_name = administration_role_name
        # Indicates whether automatic deployment is enabled.
        # 
        # Valid values:
        # 
        # *   true: Automatic deployment is enabled. If a member account is added to the folder to which the stack group belongs after automatic deployment is enabled, the stack group deploys its stack instances in the specified region where the added account is deployed. If the account is deleted from the folder, the stack instances in the specified region are deleted from the stack group.
        # *   false: Automatic deployment is disabled. After automatic deployment is disabled, the stack instances remain unchanged when the member account in the folder is changed.
        self.auto_deployment = auto_deployment
        self.create_time = create_time
        # The name of the stack group.
        self.description = description
        # The template body.
        self.execution_role_name = execution_role_name
        # The key of the parameter.
        self.parameters = parameters
        # The information about automatic deployment settings.
        # 
        # >  This parameter is returned only when the PermissionModel parameter is set to SERVICE_MANAGED.
        self.permission_model = permission_model
        # The folder IDs of the resource directory. This parameter is used to deploy stack instances within all the accounts in the folders.
        # 
        # >  This parameter is returned only when the PermissionModel parameter is set to SERVICE_MANAGED.
        self.rd_folder_ids = rd_folder_ids
        # The permission model.
        # 
        # Valid values:
        # 
        # *   SELF_MANAGED: the self-managed permission model
        # *   SERVICE_MANAGED: the service-managed permission model
        # 
        # >  For more information about the permission models of stack groups, see [Overview](https://help.aliyun.com/document_detail/154578.html).
        self.resource_group_id = resource_group_id
        # The time when drift detection was performed on the stack group.
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail
        # The status of the stack group.
        # 
        # Valid values:
        # 
        # *   ACTIVE
        # *   DELETED
        self.stack_group_id = stack_group_id
        # The name of the RAM role that is specified for the execution account when you create the self-managed stack group. The administrator role AliyunROSStackGroupAdministrationRole assumes the execution role. If this parameter is not specified, the default value AliyunROSStackGroupExecutionRole is returned.
        self.stack_group_name = stack_group_name
        # The name of the RAM role that is specified for the administrator account in Resource Orchestration Service (ROS) when you create the self-managed stack group. If this parameter is not specified, the default value AliyunROSStackGroupAdministrationRole is returned.
        self.status = status
        # The structure that contains the template body.
        # 
        # > We recommend that you use TemplateContent instead of TemplateBody.
        self.template_body = template_body
        # The JSON-formatted structure that contains the template body. For more information, see [Template syntax](https://help.aliyun.com/document_detail/28857.html).
        self.template_content = template_content
        self.update_time = update_time

    def validate(self):
        if self.auto_deployment:
            self.auto_deployment.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.stack_group_drift_detection_detail:
            self.stack_group_drift_detection_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name

        if self.auto_deployment is not None:
            result['AutoDeployment'] = self.auto_deployment.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model

        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.stack_group_drift_detection_detail is not None:
            result['StackGroupDriftDetectionDetail'] = self.stack_group_drift_detection_detail.to_map()

        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        if self.status is not None:
            result['Status'] = self.status

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')

        if m.get('AutoDeployment') is not None:
            temp_model = main_models.GetStackGroupResponseBodyStackGroupAutoDeployment()
            self.auto_deployment = temp_model.from_map(m.get('AutoDeployment'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GetStackGroupResponseBodyStackGroupParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')

        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StackGroupDriftDetectionDetail') is not None:
            temp_model = main_models.GetStackGroupResponseBodyStackGroupStackGroupDriftDetectionDetail()
            self.stack_group_drift_detection_detail = temp_model.from_map(m.get('StackGroupDriftDetectionDetail'))

        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetStackGroupResponseBodyStackGroupStackGroupDriftDetectionDetail(DaraModel):
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
        # The number of stack instances that have drifted.
        self.cancelled_stack_instances_count = cancelled_stack_instances_count
        # The drift status of the stack group.
        # 
        # Valid values:
        # 
        # *   DRIFTED: At least one stack instance in the stack group has drifted.
        # *   NOT_CHECKED: No drift detection is completed on the stack group.
        # *   IN_SYNC: All the stack instances in the stack group are being synchronized.
        self.drift_detection_status = drift_detection_status
        # The number of stack instances.
        self.drift_detection_time = drift_detection_time
        # The ID of the resource group. This parameter is specified when you create the stack group.
        self.drifted_stack_instances_count = drifted_stack_instances_count
        # The status of drift detection on the stack group.
        # 
        # Valid values:
        # 
        # *   COMPLETED: Drift detection is performed and completed on all stack instances.
        # *   FAILED: Drift detection is performed. The number of stack instances that failed the drift detection exceeds the specified threshold.
        # *   PARTIAL_SUCCESS: Drift detection is performed. The number of stack instances that failed the drift detection does not exceed the specified threshold.
        # *   IN_PROGRESS: Drift detection is being performed on the stack group.
        # *   STOPPED: Drift detection is canceled for the stack group.
        self.failed_stack_instances_count = failed_stack_instances_count
        # The number of stack instances that were being synchronized.
        self.in_progress_stack_instances_count = in_progress_stack_instances_count
        # The number of stack instances for which drift detection was canceled.
        self.in_sync_stack_instances_count = in_sync_stack_instances_count
        # The number of stack instances on which drift detection was being performed.
        self.stack_group_drift_status = stack_group_drift_status
        # The number of stack instances that failed drift detection.
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

class GetStackGroupResponseBodyStackGroupParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the parameter.
        self.parameter_key = parameter_key
        # The value of the parameter.
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

class GetStackGroupResponseBodyStackGroupAutoDeployment(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        retain_stacks_on_account_removal: bool = None,
    ):
        # Indicates whether stacks in the member account are retained when the member account is deleted from the folder.
        # 
        # Valid values:
        # 
        # *   true: The stacks are retained.
        # *   false: The stacks are deleted.
        # 
        # >  This parameter is returned only when the Enabled parameter is set to true.
        self.enabled = enabled
        # The folder IDs of the resource directory. This parameter is used to deploy stack instances within all the accounts in the folders.
        # 
        # >  This parameter is returned only when the PermissionModel parameter is set to SERVICE_MANAGED.
        self.retain_stacks_on_account_removal = retain_stacks_on_account_removal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.retain_stacks_on_account_removal is not None:
            result['RetainStacksOnAccountRemoval'] = self.retain_stacks_on_account_removal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('RetainStacksOnAccountRemoval') is not None:
            self.retain_stacks_on_account_removal = m.get('RetainStacksOnAccountRemoval')

        return self

