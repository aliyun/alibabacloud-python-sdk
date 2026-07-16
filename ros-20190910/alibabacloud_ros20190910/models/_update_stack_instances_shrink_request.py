# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class UpdateStackInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        client_token: str = None,
        deployment_targets_shrink: str = None,
        operation_description: str = None,
        operation_preferences_shrink: str = None,
        parameter_overrides: List[main_models.UpdateStackInstancesShrinkRequestParameterOverrides] = None,
        region_id: str = None,
        region_ids_shrink: str = None,
        stack_group_name: str = None,
        timeout_in_minutes: int = None,
    ):
        # The IDs of the execution accounts within which you want to deploy stacks in self-managed mode. You can specify up to 20 execution account IDs.
        # 
        # > If you want to update stacks in self-managed permission mode, you must specify this parameter.
        self.account_ids_shrink = account_ids_shrink
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\\
        # The token can contain letters, digits, hyphens (-), and underscores (_), and cannot exceed 64 characters in length.\\
        # For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The folders in which you want to deploy stacks in service-managed mode.
        # 
        # > If you want to update stacks in service-managed permission mode, you must specify this parameter.
        self.deployment_targets_shrink = deployment_targets_shrink
        # The description of the update operation.
        # 
        # The description must be 1 to 256 characters in length.
        self.operation_description = operation_description
        # The preference settings of the update operation.
        # 
        # The following parameters are available:
        # -  {"FailureToleranceCount": N}
        # 
        #     The number of accounts within which stack operation failures are allowed in each region. If the value of this parameter is exceeded in a region, ROS stops the operation in the region. If ROS stops the operation in one region, ROS stops the operation in other regions.
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
        #     The maximum number of accounts within which multiple stacks are deployed at the same time in each region.
        # 
        #     Valid values of N: 1 to 20.
        # 
        #     If you do not specify MaxConcurrentCount, 1 is used as the default value.
        # 
        # - {"MaxConcurrentPercentage": N}
        # 
        #     The percentage of the maximum number of accounts within which stacks are deployed at the same time to the total number of accounts in each region.
        # 
        #     Valid values: 1 to 100. If the numeric value in the percentage is not an integer, ROS rounds the value down to the nearest integer.
        # 
        #     If you do not specify MaxConcurrentPercentage, 1 is used as the default value.
        # 
        # - {"RegionConcurrencyType": N}
        # 
        #   The mode that you want to use to deploy stacks across regions. Valid values:
        #   - SEQUENTIAL (default): deploys stacks in the specified regions one by one in sequence. This way, ROS deploys stacks in only one region at a time. 
        # 
        #    - PARALLEL: deploys stacks in all the specified regions in parallel. 
        # 
        # Separate multiple parameters with commas (,).
        # 
        # > - You can specify only one of the following parameters: MaxConcurrentCount and MaxConcurrentPercentage.
        # > - You can specify only one of the following parameters: FailureToleranceCount and FailureTolerancePercentage.
        self.operation_preferences_shrink = operation_preferences_shrink
        # The parameters that are used to override specific parameters.
        self.parameter_overrides = parameter_overrides
        # The region ID of the stack group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the regions where you want to update the stacks. You can specify up to 20 region IDs.
        # 
        # This parameter is required.
        self.region_ids_shrink = region_ids_shrink
        # The name of the stack group. The name must be unique within a region.\\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or a letter.
        # 
        # This parameter is required.
        self.stack_group_name = stack_group_name
        # The timeout period for the update operation.
        # 
        # *   Default value: 60.
        # *   Unit: minutes.
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        if self.parameter_overrides:
            for v1 in self.parameter_overrides:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deployment_targets_shrink is not None:
            result['DeploymentTargets'] = self.deployment_targets_shrink

        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description

        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink

        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k1 in self.parameter_overrides:
                result['ParameterOverrides'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeploymentTargets') is not None:
            self.deployment_targets_shrink = m.get('DeploymentTargets')

        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')

        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')

        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k1 in m.get('ParameterOverrides'):
                temp_model = main_models.UpdateStackInstancesShrinkRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')

        return self

class UpdateStackInstancesShrinkRequestParameterOverrides(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The key of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the name that you specified when you created the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # > -  ParameterOverrides is optional.
        # > - If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The value of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the value that you specified when you created the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # > -  ParameterOverrides is optional.
        # > - If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
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

