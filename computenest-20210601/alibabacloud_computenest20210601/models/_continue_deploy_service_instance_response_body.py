# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ContinueDeployServiceInstanceResponseBody(DaraModel):
    def __init__(
        self,
        dry_run_result: main_models.ContinueDeployServiceInstanceResponseBodyDryRunResult = None,
        request_id: str = None,
        service_instance_id: str = None,
    ):
        # The dry run result.
        self.dry_run_result = dry_run_result
        # The request ID.
        self.request_id = request_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id

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

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRunResult') is not None:
            temp_model = main_models.ContinueDeployServiceInstanceResponseBodyDryRunResult()
            self.dry_run_result = temp_model.from_map(m.get('DryRunResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

class ContinueDeployServiceInstanceResponseBodyDryRunResult(DaraModel):
    def __init__(
        self,
        parameters_allowed_to_be_modified: List[str] = None,
        parameters_conditionally_allowed_to_be_modified: List[str] = None,
        parameters_not_allowed_to_be_modified: List[str] = None,
    ):
        # The parameters that can be modified. The operation that is performed to modify the parameters does not cause a validation error.
        # 
        # > This parameter is returned only if DryRun is set to true.
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        # The parameters that can be modified under specific conditions. The new values of the parameters determine whether the operation that is performed to modify the parameters causes a validation error.
        # 
        # > This parameter is returned only if DryRun is set to true.
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        # The parameters that cannot be modified. The operation that is performed to modify the parameters causes a validation error.
        # 
        # > This parameter is returned only if DryRun is set to true.
        self.parameters_not_allowed_to_be_modified = parameters_not_allowed_to_be_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters_allowed_to_be_modified is not None:
            result['ParametersAllowedToBeModified'] = self.parameters_allowed_to_be_modified

        if self.parameters_conditionally_allowed_to_be_modified is not None:
            result['ParametersConditionallyAllowedToBeModified'] = self.parameters_conditionally_allowed_to_be_modified

        if self.parameters_not_allowed_to_be_modified is not None:
            result['ParametersNotAllowedToBeModified'] = self.parameters_not_allowed_to_be_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParametersAllowedToBeModified') is not None:
            self.parameters_allowed_to_be_modified = m.get('ParametersAllowedToBeModified')

        if m.get('ParametersConditionallyAllowedToBeModified') is not None:
            self.parameters_conditionally_allowed_to_be_modified = m.get('ParametersConditionallyAllowedToBeModified')

        if m.get('ParametersNotAllowedToBeModified') is not None:
            self.parameters_not_allowed_to_be_modified = m.get('ParametersNotAllowedToBeModified')

        return self

