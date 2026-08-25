# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class InstallNodePoolComponentsRequest(DaraModel):
    def __init__(
        self,
        components: List[main_models.InstallNodePoolComponentsRequestComponents] = None,
        node_names: List[str] = None,
        rolling_policy: main_models.InstallNodePoolComponentsRequestRollingPolicy = None,
    ):
        # The list of node components.
        self.components = components
        # The list of node names for the rolling operation. By default, all nodes are included.
        self.node_names = node_names
        # The rolling policy configuration.
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
            result['nodeNames'] = self.node_names

        if self.rolling_policy is not None:
            result['rollingPolicy'] = self.rolling_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components = []
        if m.get('components') is not None:
            for k1 in m.get('components'):
                temp_model = main_models.InstallNodePoolComponentsRequestComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('nodeNames') is not None:
            self.node_names = m.get('nodeNames')

        if m.get('rollingPolicy') is not None:
            temp_model = main_models.InstallNodePoolComponentsRequestRollingPolicy()
            self.rolling_policy = temp_model.from_map(m.get('rollingPolicy'))

        return self

class InstallNodePoolComponentsRequestRollingPolicy(DaraModel):
    def __init__(
        self,
        batch_interval: int = None,
        max_failed_nodes: int = None,
        max_parallelism: int = None,
        pause_policy: str = None,
    ):
        # The upgrade interval between batches. Unit: seconds.
        self.batch_interval = batch_interval
        # The maximum number of nodes that are allowed to fail during the rolling process. Default value: 0, which indicates that the task is considered failed if any node fails. If the value is greater than 0, the task is considered failed and stops when the cumulative number of failed nodes exceeds this value.
        self.max_failed_nodes = max_failed_nodes
        # The maximum number of parallel operations per batch. Default value: 1.
        self.max_parallelism = max_parallelism
        # The automatic pause policy during the node upgrade process.
        self.pause_policy = pause_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_interval is not None:
            result['batchInterval'] = self.batch_interval

        if self.max_failed_nodes is not None:
            result['maxFailedNodes'] = self.max_failed_nodes

        if self.max_parallelism is not None:
            result['maxParallelism'] = self.max_parallelism

        if self.pause_policy is not None:
            result['pausePolicy'] = self.pause_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchInterval') is not None:
            self.batch_interval = m.get('batchInterval')

        if m.get('maxFailedNodes') is not None:
            self.max_failed_nodes = m.get('maxFailedNodes')

        if m.get('maxParallelism') is not None:
            self.max_parallelism = m.get('maxParallelism')

        if m.get('pausePolicy') is not None:
            self.pause_policy = m.get('pausePolicy')

        return self

class InstallNodePoolComponentsRequestComponents(DaraModel):
    def __init__(
        self,
        config: main_models.InstallNodePoolComponentsRequestComponentsConfig = None,
        name: str = None,
        version: str = None,
    ):
        # The component configuration.
        self.config = config
        # The component name.
        # 
        # This parameter is required.
        self.name = name
        # The component version.
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
            temp_model = main_models.InstallNodePoolComponentsRequestComponentsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class InstallNodePoolComponentsRequestComponentsConfig(DaraModel):
    def __init__(
        self,
        custom_config: Dict[str, Any] = None,
        envs: List[main_models.InstallNodePoolComponentsRequestComponentsConfigEnvs] = None,
    ):
        # The custom configuration of the component.
        self.custom_config = custom_config
        # The environment variables of the node component.
        self.envs = envs

    def validate(self):
        if self.envs:
            for v1 in self.envs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_config is not None:
            result['customConfig'] = self.custom_config

        result['envs'] = []
        if self.envs is not None:
            for k1 in self.envs:
                result['envs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customConfig') is not None:
            self.custom_config = m.get('customConfig')

        self.envs = []
        if m.get('envs') is not None:
            for k1 in m.get('envs'):
                temp_model = main_models.InstallNodePoolComponentsRequestComponentsConfigEnvs()
                self.envs.append(temp_model.from_map(k1))

        return self

class InstallNodePoolComponentsRequestComponentsConfigEnvs(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the environment variable.
        self.name = name
        # The value of the environment variable.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

