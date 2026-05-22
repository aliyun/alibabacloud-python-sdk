# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class CreateServiceResponseBody(DaraModel):
    def __init__(
        self,
        dry_run_result: main_models.CreateServiceResponseBodyDryRunResult = None,
        request_id: str = None,
        service_id: str = None,
        status: str = None,
        version: str = None,
    ):
        # The dry run result.
        self.dry_run_result = dry_run_result
        # The request ID.
        self.request_id = request_id
        # The service ID.
        self.service_id = service_id
        # The status of the service.
        self.status = status
        # The service version.
        self.version = version

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

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRunResult') is not None:
            temp_model = main_models.CreateServiceResponseBodyDryRunResult()
            self.dry_run_result = temp_model.from_map(m.get('DryRunResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateServiceResponseBodyDryRunResult(DaraModel):
    def __init__(
        self,
        role_policy: main_models.CreateServiceResponseBodyDryRunResultRolePolicy = None,
    ):
        # The required ram policy for deploying role.
        self.role_policy = role_policy

    def validate(self):
        if self.role_policy:
            self.role_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_policy is not None:
            result['RolePolicy'] = self.role_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RolePolicy') is not None:
            temp_model = main_models.CreateServiceResponseBodyDryRunResultRolePolicy()
            self.role_policy = temp_model.from_map(m.get('RolePolicy'))

        return self

class CreateServiceResponseBodyDryRunResultRolePolicy(DaraModel):
    def __init__(
        self,
        missing_policy: List[main_models.CreateServiceResponseBodyDryRunResultRolePolicyMissingPolicy] = None,
        policy: str = None,
    ):
        # The missing ram policy for deploying role.
        self.missing_policy = missing_policy
        # The required ram policy for deploying role.
        self.policy = policy

    def validate(self):
        if self.missing_policy:
            for v1 in self.missing_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MissingPolicy'] = []
        if self.missing_policy is not None:
            for k1 in self.missing_policy:
                result['MissingPolicy'].append(k1.to_map() if k1 else None)

        if self.policy is not None:
            result['Policy'] = self.policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.missing_policy = []
        if m.get('MissingPolicy') is not None:
            for k1 in m.get('MissingPolicy'):
                temp_model = main_models.CreateServiceResponseBodyDryRunResultRolePolicyMissingPolicy()
                self.missing_policy.append(temp_model.from_map(k1))

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

class CreateServiceResponseBodyDryRunResultRolePolicyMissingPolicy(DaraModel):
    def __init__(
        self,
        action: List[str] = None,
        resource: str = None,
        service_name: str = None,
    ):
        # The Actions.
        self.action = action
        # Resource in ram policy.
        self.resource = resource
        # The service name in ram policy.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

