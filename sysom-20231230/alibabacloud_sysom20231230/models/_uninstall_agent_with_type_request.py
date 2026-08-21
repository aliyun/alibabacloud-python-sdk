# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class UninstallAgentWithTypeRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        agent_id: str = None,
        agent_version: str = None,
        instance_type: str = None,
        instances: List[main_models.UninstallAgentWithTypeRequestInstances] = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The ID of the component to uninstall.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The version of the component to uninstall.
        # 
        # This parameter is required.
        self.agent_version = agent_version
        # The instance type.
        self.instance_type = instance_type
        # The list of instances from which to uninstall the component.
        # 
        # This parameter is required.
        self.instances = instances
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_version is not None:
            result['agentVersion'] = self.agent_version

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentVersion') is not None:
            self.agent_version = m.get('agentVersion')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.UninstallAgentWithTypeRequestInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

class UninstallAgentWithTypeRequestInstances(DaraModel):
    def __init__(
        self,
        instance: str = None,
        region: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance = instance
        # The region ID.
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['instance'] = self.instance

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

