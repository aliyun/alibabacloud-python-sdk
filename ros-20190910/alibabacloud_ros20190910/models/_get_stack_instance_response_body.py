# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetStackInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stack_instance: main_models.GetStackInstanceResponseBodyStackInstance = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the stack.
        self.stack_instance = stack_instance

    def validate(self):
        if self.stack_instance:
            self.stack_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stack_instance is not None:
            result['StackInstance'] = self.stack_instance.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StackInstance') is not None:
            temp_model = main_models.GetStackInstanceResponseBodyStackInstance()
            self.stack_instance = temp_model.from_map(m.get('StackInstance'))

        return self

class GetStackInstanceResponseBodyStackInstance(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        drift_detection_time: str = None,
        outputs: List[Dict[str, Any]] = None,
        parameter_overrides: List[main_models.GetStackInstanceResponseBodyStackInstanceParameterOverrides] = None,
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
        # The time when the most recent successful drift detection was performed on the stack group.
        # 
        # > This parameter is returned only if drift detection is performed on the stack group.
        self.drift_detection_time = drift_detection_time
        # The outputs of the stack.
        # 
        # >  This parameter is returned if OutputOption is set to Enabled.
        self.outputs = outputs
        # The parameters that are used to override specific parameters.
        self.parameter_overrides = parameter_overrides
        # The ID of the folder in the resource directory.
        # 
        # > This parameter is returned only if the stack group is granted service-managed permissions.
        self.rd_folder_id = rd_folder_id
        # The region ID of the stack.
        self.region_id = region_id
        # The state of the stack when the most recent successful drift detection was performed on the stack group.
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
        if self.parameter_overrides:
            for v1 in self.parameter_overrides:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k1 in self.parameter_overrides:
                result['ParameterOverrides'].append(k1.to_map() if k1 else None)

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

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k1 in m.get('ParameterOverrides'):
                temp_model = main_models.GetStackInstanceResponseBodyStackInstanceParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k1))

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

class GetStackInstanceResponseBodyStackInstanceParameterOverrides(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the parameter that is used to override a specific parameter.
        self.parameter_key = parameter_key
        # The value of the parameter that is used to override a specific parameter.
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

