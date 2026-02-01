# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class InstallAgentRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        install_type: str = None,
        instances: List[main_models.InstallAgentRequestInstances] = None,
    ):
        # This parameter is required.
        self.agent_id = agent_id
        # This parameter is required.
        self.agent_version = agent_version
        # This parameter is required.
        self.install_type = install_type
        # This parameter is required.
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
            result['agent_id'] = self.agent_id

        if self.agent_version is not None:
            result['agent_version'] = self.agent_version

        if self.install_type is not None:
            result['install_type'] = self.install_type

        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('agent_version') is not None:
            self.agent_version = m.get('agent_version')

        if m.get('install_type') is not None:
            self.install_type = m.get('install_type')

        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.InstallAgentRequestInstances()
                self.instances.append(temp_model.from_map(k1))

        return self

class InstallAgentRequestInstances(DaraModel):
    def __init__(
        self,
        instance: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.instance = instance
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

