# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class UpdateStackResponseBody(DaraModel):
    def __init__(
        self,
        dry_run_result: main_models.UpdateStackResponseBodyDryRunResult = None,
        request_id: str = None,
        stack_id: str = None,
    ):
        # The dry run result. This parameter is returned only if DryRun is set to true.
        self.dry_run_result = dry_run_result
        # The ID of the request.
        self.request_id = request_id
        # The ID of the stack.
        self.stack_id = stack_id

    def validate(self):
        if self.dry_run_result:
            self.dry_run_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run_result is not None:
            result['DryRunResult'] = self.dry_run_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRunResult') is not None:
            temp_model = main_models.UpdateStackResponseBodyDryRunResult()
            self.dry_run_result = temp_model.from_map(m.get('DryRunResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

class UpdateStackResponseBodyDryRunResult(DaraModel):
    def __init__(
        self,
        parameters_allowed_to_be_modified: List[str] = None,
        parameters_cause_interruption_if_modified: List[str] = None,
        parameters_cause_replacement_if_modified: List[str] = None,
        parameters_conditionally_allowed_to_be_modified: List[str] = None,
        parameters_conditionally_cause_interruption_if_modified: List[str] = None,
        parameters_conditionally_cause_replacement_if_modified: List[str] = None,
        parameters_not_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_cause_interruption_if_modified: List[str] = None,
        parameters_uncertainly_cause_replacement_if_modified: List[str] = None,
    ):
        # The parameters that can be modified. If you change only values of the parameters in a stack template and use the template to update the stack, no validation errors are caused.
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        # The parameters whose changes cause service interruptions.
        # > - This parameter is supported only for a small number of resource types.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_cause_interruption_if_modified = parameters_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources.
        # 
        # > -  This parameter can be returned only if ReplacementOption is set to Enabled.
        # > -  This parameter is valid only for updates on ROS stacks.
        self.parameters_cause_replacement_if_modified = parameters_cause_replacement_if_modified
        # The parameters that can be modified under specific conditions. If you change only values of the parameters in a stack template and use the template to update the stack, the new values of the parameters determine whether validation errors are caused.
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        # The parameters whose changes cause service interruptions under specific conditions.
        # 
        # > - This parameter is supported only for a small number of resource types.
        # > -  This parameter is valid only for updates on ROS stacks.
        self.parameters_conditionally_cause_interruption_if_modified = parameters_conditionally_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources under specific conditions.
        # 
        # > - This parameter can be returned only if ReplacementOption is set to Enabled.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_conditionally_cause_replacement_if_modified = parameters_conditionally_cause_replacement_if_modified
        # The parameters that cannot be modified. If you change only values of the parameters in a stack template and use the template to update the stack, validation errors are caused.
        self.parameters_not_allowed_to_be_modified = parameters_not_allowed_to_be_modified
        # The parameters that can be modified under uncertain conditions. If you change only values of the parameters in a stack template and use the template to update the stack, the actual running environment determines whether validation errors are caused.
        self.parameters_uncertainly_allowed_to_be_modified = parameters_uncertainly_allowed_to_be_modified
        # The parameters whose changes cause service interruptions under uncertain conditions.
        # 
        # > - This parameter is supported only for a small number of resource types.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_uncertainly_cause_interruption_if_modified = parameters_uncertainly_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources under uncertain conditions.
        # 
        # > - This parameter can be returned only if ReplacementOption is set to Enabled.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_uncertainly_cause_replacement_if_modified = parameters_uncertainly_cause_replacement_if_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters_allowed_to_be_modified is not None:
            result['ParametersAllowedToBeModified'] = self.parameters_allowed_to_be_modified

        if self.parameters_cause_interruption_if_modified is not None:
            result['ParametersCauseInterruptionIfModified'] = self.parameters_cause_interruption_if_modified

        if self.parameters_cause_replacement_if_modified is not None:
            result['ParametersCauseReplacementIfModified'] = self.parameters_cause_replacement_if_modified

        if self.parameters_conditionally_allowed_to_be_modified is not None:
            result['ParametersConditionallyAllowedToBeModified'] = self.parameters_conditionally_allowed_to_be_modified

        if self.parameters_conditionally_cause_interruption_if_modified is not None:
            result['ParametersConditionallyCauseInterruptionIfModified'] = self.parameters_conditionally_cause_interruption_if_modified

        if self.parameters_conditionally_cause_replacement_if_modified is not None:
            result['ParametersConditionallyCauseReplacementIfModified'] = self.parameters_conditionally_cause_replacement_if_modified

        if self.parameters_not_allowed_to_be_modified is not None:
            result['ParametersNotAllowedToBeModified'] = self.parameters_not_allowed_to_be_modified

        if self.parameters_uncertainly_allowed_to_be_modified is not None:
            result['ParametersUncertainlyAllowedToBeModified'] = self.parameters_uncertainly_allowed_to_be_modified

        if self.parameters_uncertainly_cause_interruption_if_modified is not None:
            result['ParametersUncertainlyCauseInterruptionIfModified'] = self.parameters_uncertainly_cause_interruption_if_modified

        if self.parameters_uncertainly_cause_replacement_if_modified is not None:
            result['ParametersUncertainlyCauseReplacementIfModified'] = self.parameters_uncertainly_cause_replacement_if_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParametersAllowedToBeModified') is not None:
            self.parameters_allowed_to_be_modified = m.get('ParametersAllowedToBeModified')

        if m.get('ParametersCauseInterruptionIfModified') is not None:
            self.parameters_cause_interruption_if_modified = m.get('ParametersCauseInterruptionIfModified')

        if m.get('ParametersCauseReplacementIfModified') is not None:
            self.parameters_cause_replacement_if_modified = m.get('ParametersCauseReplacementIfModified')

        if m.get('ParametersConditionallyAllowedToBeModified') is not None:
            self.parameters_conditionally_allowed_to_be_modified = m.get('ParametersConditionallyAllowedToBeModified')

        if m.get('ParametersConditionallyCauseInterruptionIfModified') is not None:
            self.parameters_conditionally_cause_interruption_if_modified = m.get('ParametersConditionallyCauseInterruptionIfModified')

        if m.get('ParametersConditionallyCauseReplacementIfModified') is not None:
            self.parameters_conditionally_cause_replacement_if_modified = m.get('ParametersConditionallyCauseReplacementIfModified')

        if m.get('ParametersNotAllowedToBeModified') is not None:
            self.parameters_not_allowed_to_be_modified = m.get('ParametersNotAllowedToBeModified')

        if m.get('ParametersUncertainlyAllowedToBeModified') is not None:
            self.parameters_uncertainly_allowed_to_be_modified = m.get('ParametersUncertainlyAllowedToBeModified')

        if m.get('ParametersUncertainlyCauseInterruptionIfModified') is not None:
            self.parameters_uncertainly_cause_interruption_if_modified = m.get('ParametersUncertainlyCauseInterruptionIfModified')

        if m.get('ParametersUncertainlyCauseReplacementIfModified') is not None:
            self.parameters_uncertainly_cause_replacement_if_modified = m.get('ParametersUncertainlyCauseReplacementIfModified')

        return self

