# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetStackDeploymentsResponseBody(DaraModel):
    def __init__(
        self,
        deployments: List[main_models.GetStackDeploymentsResponseBodyDeployments] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.deployments = deployments
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.deployments:
            for v1 in self.deployments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['deployments'] = []
        if self.deployments is not None:
            for k1 in self.deployments:
                result['deployments'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployments = []
        if m.get('deployments') is not None:
            for k1 in m.get('deployments'):
                temp_model = main_models.GetStackDeploymentsResponseBodyDeployments()
                self.deployments.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class GetStackDeploymentsResponseBodyDeployments(DaraModel):
    def __init__(
        self,
        config: main_models.GetStackDeploymentsResponseBodyDeploymentsConfig = None,
        config_version: str = None,
        create_time: str = None,
        deployment_name: str = None,
        deployment_no: str = None,
        deployment_version: str = None,
        elapsed_time: int = None,
        execute_type: str = None,
        failed_reason: str = None,
        job_id: str = None,
        outputs: List[main_models.GetStackDeploymentsResponseBodyDeploymentsOutputs] = None,
        parameters: List[main_models.GetStackDeploymentsResponseBodyDeploymentsParameters] = None,
        plan_outputs: List[main_models.GetStackDeploymentsResponseBodyDeploymentsPlanOutputs] = None,
        status: str = None,
        task_id: str = None,
    ):
        self.config = config
        self.config_version = config_version
        self.create_time = create_time
        self.deployment_name = deployment_name
        self.deployment_no = deployment_no
        self.deployment_version = deployment_version
        self.elapsed_time = elapsed_time
        self.execute_type = execute_type
        self.failed_reason = failed_reason
        self.job_id = job_id
        self.outputs = outputs
        self.parameters = parameters
        self.plan_outputs = plan_outputs
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.config:
            self.config.validate()
        if self.outputs:
            for v1 in self.outputs:
                 if v1:
                    v1.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.plan_outputs:
            for v1 in self.plan_outputs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.config_version is not None:
            result['configVersion'] = self.config_version

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.deployment_name is not None:
            result['deploymentName'] = self.deployment_name

        if self.deployment_no is not None:
            result['deploymentNo'] = self.deployment_no

        if self.deployment_version is not None:
            result['deploymentVersion'] = self.deployment_version

        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time

        if self.execute_type is not None:
            result['executeType'] = self.execute_type

        if self.failed_reason is not None:
            result['failedReason'] = self.failed_reason

        if self.job_id is not None:
            result['jobId'] = self.job_id

        result['outputs'] = []
        if self.outputs is not None:
            for k1 in self.outputs:
                result['outputs'].append(k1.to_map() if k1 else None)

        result['parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['parameters'].append(k1.to_map() if k1 else None)

        result['planOutputs'] = []
        if self.plan_outputs is not None:
            for k1 in self.plan_outputs:
                result['planOutputs'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.GetStackDeploymentsResponseBodyDeploymentsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('configVersion') is not None:
            self.config_version = m.get('configVersion')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('deploymentName') is not None:
            self.deployment_name = m.get('deploymentName')

        if m.get('deploymentNo') is not None:
            self.deployment_no = m.get('deploymentNo')

        if m.get('deploymentVersion') is not None:
            self.deployment_version = m.get('deploymentVersion')

        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')

        if m.get('executeType') is not None:
            self.execute_type = m.get('executeType')

        if m.get('failedReason') is not None:
            self.failed_reason = m.get('failedReason')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        self.outputs = []
        if m.get('outputs') is not None:
            for k1 in m.get('outputs'):
                temp_model = main_models.GetStackDeploymentsResponseBodyDeploymentsOutputs()
                self.outputs.append(temp_model.from_map(k1))

        self.parameters = []
        if m.get('parameters') is not None:
            for k1 in m.get('parameters'):
                temp_model = main_models.GetStackDeploymentsResponseBodyDeploymentsParameters()
                self.parameters.append(temp_model.from_map(k1))

        self.plan_outputs = []
        if m.get('planOutputs') is not None:
            for k1 in m.get('planOutputs'):
                temp_model = main_models.GetStackDeploymentsResponseBodyDeploymentsPlanOutputs()
                self.plan_outputs.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class GetStackDeploymentsResponseBodyDeploymentsPlanOutputs(DaraModel):
    def __init__(
        self,
        module_action: str = None,
        module_action_detail: main_models.GetStackDeploymentsResponseBodyDeploymentsPlanOutputsModuleActionDetail = None,
        resource_changes: List[main_models.GetStackDeploymentsResponseBodyDeploymentsPlanOutputsResourceChanges] = None,
        stack_module_name: str = None,
    ):
        self.module_action = module_action
        self.module_action_detail = module_action_detail
        self.resource_changes = resource_changes
        self.stack_module_name = stack_module_name

    def validate(self):
        if self.module_action_detail:
            self.module_action_detail.validate()
        if self.resource_changes:
            for v1 in self.resource_changes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_action is not None:
            result['moduleAction'] = self.module_action

        if self.module_action_detail is not None:
            result['moduleActionDetail'] = self.module_action_detail.to_map()

        result['resourceChanges'] = []
        if self.resource_changes is not None:
            for k1 in self.resource_changes:
                result['resourceChanges'].append(k1.to_map() if k1 else None)

        if self.stack_module_name is not None:
            result['stackModuleName'] = self.stack_module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('moduleAction') is not None:
            self.module_action = m.get('moduleAction')

        if m.get('moduleActionDetail') is not None:
            temp_model = main_models.GetStackDeploymentsResponseBodyDeploymentsPlanOutputsModuleActionDetail()
            self.module_action_detail = temp_model.from_map(m.get('moduleActionDetail'))

        self.resource_changes = []
        if m.get('resourceChanges') is not None:
            for k1 in m.get('resourceChanges'):
                temp_model = main_models.GetStackDeploymentsResponseBodyDeploymentsPlanOutputsResourceChanges()
                self.resource_changes.append(temp_model.from_map(k1))

        if m.get('stackModuleName') is not None:
            self.stack_module_name = m.get('stackModuleName')

        return self

class GetStackDeploymentsResponseBodyDeploymentsPlanOutputsResourceChanges(DaraModel):
    def __init__(
        self,
        change: str = None,
        resource_actions: List[str] = None,
        resource_identifier: str = None,
    ):
        self.change = change
        self.resource_actions = resource_actions
        self.resource_identifier = resource_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change is not None:
            result['change'] = self.change

        if self.resource_actions is not None:
            result['resourceActions'] = self.resource_actions

        if self.resource_identifier is not None:
            result['resourceIdentifier'] = self.resource_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change') is not None:
            self.change = m.get('change')

        if m.get('resourceActions') is not None:
            self.resource_actions = m.get('resourceActions')

        if m.get('resourceIdentifier') is not None:
            self.resource_identifier = m.get('resourceIdentifier')

        return self

class GetStackDeploymentsResponseBodyDeploymentsPlanOutputsModuleActionDetail(DaraModel):
    def __init__(
        self,
        add: int = None,
        change: int = None,
        destroy: int = None,
    ):
        self.add = add
        self.change = change
        self.destroy = destroy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add is not None:
            result['add'] = self.add

        if self.change is not None:
            result['change'] = self.change

        if self.destroy is not None:
            result['destroy'] = self.destroy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add') is not None:
            self.add = m.get('add')

        if m.get('change') is not None:
            self.change = m.get('change')

        if m.get('destroy') is not None:
            self.destroy = m.get('destroy')

        return self

class GetStackDeploymentsResponseBodyDeploymentsParameters(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['defaultValue'] = self.default_value

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class GetStackDeploymentsResponseBodyDeploymentsOutputs(DaraModel):
    def __init__(
        self,
        description: str = None,
        expression: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.description = description
        self.expression = expression
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.expression is not None:
            result['expression'] = self.expression

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class GetStackDeploymentsResponseBodyDeploymentsConfig(DaraModel):
    def __init__(
        self,
        auto_apply: bool = None,
        is_destroy: bool = None,
    ):
        self.auto_apply = auto_apply
        self.is_destroy = is_destroy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply

        if self.is_destroy is not None:
            result['isDestroy'] = self.is_destroy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')

        if m.get('isDestroy') is not None:
            self.is_destroy = m.get('isDestroy')

        return self

