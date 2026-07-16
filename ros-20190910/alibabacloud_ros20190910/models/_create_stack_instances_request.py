# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class CreateStackInstancesRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        client_token: str = None,
        deployment_options: List[str] = None,
        deployment_targets: main_models.CreateStackInstancesRequestDeploymentTargets = None,
        disable_rollback: bool = None,
        operation_description: str = None,
        operation_preferences: Dict[str, Any] = None,
        parameter_overrides: List[main_models.CreateStackInstancesRequestParameterOverrides] = None,
        region_id: str = None,
        region_ids: List[str] = None,
        stack_group_name: str = None,
        timeout_in_minutes: int = None,
    ):
        # The IDs of the execution accounts within which you want to deploy stacks in self-managed mode. You can specify up to 20 execution account IDs.
        # 
        # > You must specify one of the following parameters: `AccountIds` and `DeploymentTargets`.
        self.account_ids = account_ids
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\\
        # The token can contain letters, digits, hyphens (-), and underscores (_), and cannot exceed 64 characters in length.\\
        # For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        self.deployment_options = deployment_options
        # The folders in which ROS deploy stacks in service-managed permission model.
        # 
        # > You must specify one of the following parameters: `AccountIds` and `DeploymentTargets`.
        self.deployment_targets = deployment_targets
        # Specifies whether to disable rollback when the stack fails to be created.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (default)
        self.disable_rollback = disable_rollback
        # The description of the stack creation operation.
        # 
        # The description must be 1 to 256 characters in length.
        self.operation_description = operation_description
        # The preference settings of the stack creation operation.
        # 
        # The following parameters are available:
        # 
        # -  {"FailureToleranceCount": N}
        # 
        #     The number of accounts within which stack operation failures are allowed in each region. If the value of this parameter is exceeded in a region, Resource Orchestration Service (ROS) stops the operation in the region. If ROS stops the operation in one region, ROS stops the operation in other regions.
        # 
        #     Valid values of N: 0 to 20.
        # 
        #     If you do not specify FailureToleranceCount, 0 is used as the default value.
        # 
        # -  {"FailureTolerancePercentage": N}
        # 
        #     The percentage of the number of accounts within which stack operation failures are allowed to the total number of accounts in each region. If the value of this parameter is exceeded, ROS stops the operation in the region.
        # 
        #     Valid values of N: 0 to 100. If the numeric value in the percentage is not an integer, ROS rounds the value down to the nearest integer.
        # 
        #     If you do not specify FailureTolerancePercentage, 0 is used as the default value.
        # 
        # -  {"MaxConcurrentCount": N}
        # 
        #    The maximum number of accounts within which multiple stacks are deployed at the same time in each region.
        # 
        #    Valid values of N: 1 to 20.
        # 
        #    If you do not specify MaxConcurrentCount, 1 is used as the default value.
        # 
        # -  {"MaxConcurrentPercentage": N}
        # 
        #     The percentage of the maximum number of accounts within which multiple stacks are deployed at the same time to the total number of accounts in each region.
        # 
        #     Valid values: 1 to 100. If the numeric value in the percentage is not an integer, ROS rounds the number down to the nearest integer.
        # 
        #     If you do not specify MaxConcurrentPercentage, 1 is used as the default value.
        # 
        # -  {"RegionConcurrencyType": N}\\
        #     The mode that you want to use to deploy stacks across regions. Valid values: 
        #    - SEQUENTIAL (default): deploys stacks in each specified region based on the specified sequence of regions. ROS deploys stacks in one region at a time. 
        #    - PARALLEL: deploys stacks in parallel across all specified regions.
        # 
        # Separate multiple parameters with commas (,).
        # 
        # >-  You can specify only one of the following parameters: MaxConcurrentCount and MaxConcurrentPercentage.
        # >-  You can specify only one of the following parameters: FailureToleranceCount and FailureTolerancePercentage.
        self.operation_preferences = operation_preferences
        # The parameters that are used to override specific parameters.
        self.parameter_overrides = parameter_overrides
        # The region ID of the stack group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the regions where you want to create the stacks. You can specify up to 20 region IDs.
        # 
        # This parameter is required.
        self.region_ids = region_ids
        # The name of the stack group. The name must be unique within a region.\\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or a letter.
        # 
        # This parameter is required.
        self.stack_group_name = stack_group_name
        # The timeout period within which you can create the stack.
        # 
        # *   Default value: 60.
        # *   Unit: minutes.
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        if self.deployment_targets:
            self.deployment_targets.validate()
        if self.parameter_overrides:
            for v1 in self.parameter_overrides:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deployment_options is not None:
            result['DeploymentOptions'] = self.deployment_options

        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()

        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback

        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description

        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences

        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k1 in self.parameter_overrides:
                result['ParameterOverrides'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeploymentOptions') is not None:
            self.deployment_options = m.get('DeploymentOptions')

        if m.get('DeploymentTargets') is not None:
            temp_model = main_models.CreateStackInstancesRequestDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m.get('DeploymentTargets'))

        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')

        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')

        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')

        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k1 in m.get('ParameterOverrides'):
                temp_model = main_models.CreateStackInstancesRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')

        return self

class CreateStackInstancesRequestParameterOverrides(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The key of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the name that you specified when you created the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # >-   ParameterOverrides is optional.
        # >-   If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The value of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the value that you specify when you create the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # >-  ParameterOverrides is optional.
        # >-  If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
        # 
        # This parameter is required.
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

class CreateStackInstancesRequestDeploymentTargets(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        rd_folder_ids: List[str] = None,
    ):
        self.account_ids = account_ids
        # The folder IDs of the resource directory. You can add up to five folder IDs.
        # 
        # You can create stacks within all the member accounts in the specified folders. If you create stacks in the Root folder, the stacks are created within all member accounts in the resource directory.
        # 
        # > To view the folder IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the basic information about a folder](https://help.aliyun.com/document_detail/111223.html).
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

