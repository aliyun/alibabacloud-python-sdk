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
        self.config = config
        self.disable_rolling = disable_rolling
        self.node_names = node_names
        self.rolling_policy = rolling_policy
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

class UpdateNodePoolComponentInstanceRequestConfig(DaraModel):
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

