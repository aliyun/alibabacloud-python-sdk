# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class UpdateNodePoolComponentInstanceRequest(DaraModel):
    def __init__(
        self,
        config: main_models.UpdateNodePoolComponentInstanceRequestConfig = None,
        disable_rolling: bool = None,
        node_names: List[str] = None,
        rolling_policy: main_models.UpdateNodePoolComponentInstanceRequestRollingPolicy = None,
        version: str = None,
    ):
        # The node component configuration.
        self.config = config
        # Specifies whether to disable the rolling update. Default value: false. Updating the baseline configuration triggers a rolling update of the nodes.
        self.disable_rolling = disable_rolling
        # The list of nodes to be updated in a rolling manner. By default, all nodes are updated.
        self.node_names = node_names
        # The rolling update configuration.
        self.rolling_policy = rolling_policy
        # The node component version.
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
            result['disable_rolling'] = self.disable_rolling

        if self.node_names is not None:
            result['node_names'] = self.node_names

        if self.rolling_policy is not None:
            result['rolling_policy'] = self.rolling_policy.to_map()

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.UpdateNodePoolComponentInstanceRequestConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('disable_rolling') is not None:
            self.disable_rolling = m.get('disable_rolling')

        if m.get('node_names') is not None:
            self.node_names = m.get('node_names')

        if m.get('rolling_policy') is not None:
            temp_model = main_models.UpdateNodePoolComponentInstanceRequestRollingPolicy()
            self.rolling_policy = temp_model.from_map(m.get('rolling_policy'))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class UpdateNodePoolComponentInstanceRequestRollingPolicy(DaraModel):
    def __init__(
        self,
        batch_interval: int = None,
        max_failed_nodes: int = None,
        max_parallelism: int = None,
        pause_policy: str = None,
    ):
        # The upgrade interval between batches, in seconds. Default value: 0.
        self.batch_interval = batch_interval
        # The maximum number of nodes that are allowed to fail during the rolling update. Default value: 0. A value of 0 indicates that the task fails if any node fails. A value greater than 0 indicates that the task fails and stops if the cumulative number of failed nodes exceeds this value.
        self.max_failed_nodes = max_failed_nodes
        # The maximum number of parallel updates per batch. Default value: 1.
        self.max_parallelism = max_parallelism
        # The auto-pause policy during the node upgrade process. Valid values: NotPause, FirstBatch, and EveryBatch. Default value: NotPause.
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

class UpdateNodePoolComponentInstanceRequestConfig(DaraModel):
    def __init__(
        self,
        custom_config: Dict[str, Any] = None,
        envs: List[main_models.UpdateNodePoolComponentInstanceRequestConfigEnvs] = None,
    ):
        # The custom configuration of the node component.
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
            result['custom_config'] = self.custom_config

        result['envs'] = []
        if self.envs is not None:
            for k1 in self.envs:
                result['envs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('custom_config') is not None:
            self.custom_config = m.get('custom_config')

        self.envs = []
        if m.get('envs') is not None:
            for k1 in m.get('envs'):
                temp_model = main_models.UpdateNodePoolComponentInstanceRequestConfigEnvs()
                self.envs.append(temp_model.from_map(k1))

        return self

class UpdateNodePoolComponentInstanceRequestConfigEnvs(DaraModel):
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

