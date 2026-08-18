# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class CreateNodePoolComponentInstancesRequest(DaraModel):
    def __init__(
        self,
        components: List[main_models.CreateNodePoolComponentInstancesRequestComponents] = None,
        node_names: List[str] = None,
        rolling_policy: main_models.CreateNodePoolComponentInstancesRequestRollingPolicy = None,
    ):
        # This parameter is required.
        self.components = components
        self.node_names = node_names
        self.rolling_policy = rolling_policy

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()
        if self.rolling_policy:
            self.rolling_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['components'].append(k1.to_map() if k1 else None)

        if self.node_names is not None:
            result['node_names'] = self.node_names

        if self.rolling_policy is not None:
            result['rolling_policy'] = self.rolling_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components = []
        if m.get('components') is not None:
            for k1 in m.get('components'):
                temp_model = main_models.CreateNodePoolComponentInstancesRequestComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('node_names') is not None:
            self.node_names = m.get('node_names')

        if m.get('rolling_policy') is not None:
            temp_model = main_models.CreateNodePoolComponentInstancesRequestRollingPolicy()
            self.rolling_policy = temp_model.from_map(m.get('rolling_policy'))

        return self

class CreateNodePoolComponentInstancesRequestRollingPolicy(DaraModel):
    def __init__(
        self,
        batch_interval: int = None,
        max_failed_nodes: int = None,
        max_parallelism: int = None,
        pause_policy: str = None,
    ):
        self.batch_interval = batch_interval
        self.max_failed_nodes = max_failed_nodes
        self.max_parallelism = max_parallelism
        self.pause_policy = pause_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_interval is not None:
            result['batch_interval'] = self.batch_interval

        if self.max_failed_nodes is not None:
            result['max_failed_nodes'] = self.max_failed_nodes

        if self.max_parallelism is not None:
            result['max_parallelism'] = self.max_parallelism

        if self.pause_policy is not None:
            result['pause_policy'] = self.pause_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batch_interval') is not None:
            self.batch_interval = m.get('batch_interval')

        if m.get('max_failed_nodes') is not None:
            self.max_failed_nodes = m.get('max_failed_nodes')

        if m.get('max_parallelism') is not None:
            self.max_parallelism = m.get('max_parallelism')

        if m.get('pause_policy') is not None:
            self.pause_policy = m.get('pause_policy')

        return self

class CreateNodePoolComponentInstancesRequestComponents(DaraModel):
    def __init__(
        self,
        config: main_models.CreateNodePoolComponentInstancesRequestComponentsConfig = None,
        name: str = None,
        version: str = None,
    ):
        self.config = config
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.CreateNodePoolComponentInstancesRequestComponentsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class CreateNodePoolComponentInstancesRequestComponentsConfig(DaraModel):
    def __init__(
        self,
        custom_config: Dict[str, Any] = None,
    ):
        self.custom_config = custom_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_config is not None:
            result['custom_config'] = self.custom_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('custom_config') is not None:
            self.custom_config = m.get('custom_config')

        return self

