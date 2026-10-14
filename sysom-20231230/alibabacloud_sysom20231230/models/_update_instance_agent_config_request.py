# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class UpdateInstanceAgentConfigRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        config_id: str = None,
        instances: List[main_models.UpdateInstanceAgentConfigRequestInstances] = None,
    ):
        # The ID of the component whose configuration is to be updated.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The ID of the component configuration to be applied to the instance.
        # 
        # This parameter is required.
        self.config_id = config_id
        # The instance information.
        self.instances = instances

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
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.config_id is not None:
            result['configId'] = self.config_id

        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('configId') is not None:
            self.config_id = m.get('configId')

        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.UpdateInstanceAgentConfigRequestInstances()
                self.instances.append(temp_model.from_map(k1))

        return self

class UpdateInstanceAgentConfigRequestInstances(DaraModel):
    def __init__(
        self,
        instance: str = None,
        region: str = None,
    ):
        # The instance ID.
        self.instance = instance
        # The region ID.
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

