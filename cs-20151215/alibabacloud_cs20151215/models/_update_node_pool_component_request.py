# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class UpdateNodePoolComponentRequest(DaraModel):
    def __init__(
        self,
        config: main_models.UpdateNodePoolComponentRequestConfig = None,
        disable_rolling: bool = None,
        name: str = None,
        node_names: List[str] = None,
        rolling_policy: main_models.UpdateNodePoolComponentRequestRollingPolicy = None,
        version: str = None,
    ):
        # The configuration of the node component.
        self.config = config
        # Specifies whether to disable log rotation. Default value: false. Updating the baseline configuration triggers log rotation on nodes.
        self.disable_rolling = disable_rolling
        # The name of the node component.
        self.name = name
        # The list of nodes for log rotation. By default, all nodes are included.
        self.node_names = node_names
        # The log rotation configuration.
        self.rolling_policy = rolling_policy
        # The version of the node component.
        self.version = version

    def validate(self):
        if self.config:
            self.config.validate()
        if self.rolling_policy:
            self.rolling_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.disable_rolling is not None:
            result['disableRolling'] = self.disable_rolling

        if self.name is not None:
            result['name'] = self.name

        if self.node_names is not None:
            result['nodeNames'] = self.node_names

        if self.rolling_policy is not None:
            result['rollingPolicy'] = self.rolling_policy.to_map()

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.UpdateNodePoolComponentRequestConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('disableRolling') is not None:
            self.disable_rolling = m.get('disableRolling')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nodeNames') is not None:
            self.node_names = m.get('nodeNames')

        if m.get('rollingPolicy') is not None:
            temp_model = main_models.UpdateNodePoolComponentRequestRollingPolicy()
            self.rolling_policy = temp_model.from_map(m.get('rollingPolicy'))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class UpdateNodePoolComponentRequestRollingPolicy(DaraModel):
    def __init__(
        self,
        batch_interval: int = None,
        max_failed_nodes: int = None,
        max_parallelism: int = None,
        pause_policy: str = None,
    ):
        # The upgrade interval between batches. Unit: seconds.
        self.batch_interval = batch_interval
        # The maximum number of nodes that can fail during the rolling update. Default value: 0, which means the task fails if any node fails. If the value is greater than 0, the task fails and stops when the cumulative number of failed nodes exceeds this value.
        self.max_failed_nodes = max_failed_nodes
        # The maximum number of parallel operations per batch. Default value: 1.
        self.max_parallelism = max_parallelism
        # The automatic pause policy during node upgrade.
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

class UpdateNodePoolComponentRequestConfig(DaraModel):
    def __init__(
        self,
        custom_config: Dict[str, Any] = None,
        envs: List[main_models.UpdateNodePoolComponentRequestConfigEnvs] = None,
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
                temp_model = main_models.UpdateNodePoolComponentRequestConfigEnvs()
                self.envs.append(temp_model.from_map(k1))

        return self

class UpdateNodePoolComponentRequestConfigEnvs(DaraModel):
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

