# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

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
        self.config = config
        self.disable_rolling = disable_rolling
        self.name = name
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
        max_parallelism: int = None,
        pause_policy: str = None,
    ):
        self.batch_interval = batch_interval
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
            result['batchInterval'] = self.batch_interval

        if self.max_parallelism is not None:
            result['maxParallelism'] = self.max_parallelism

        if self.pause_policy is not None:
            result['pausePolicy'] = self.pause_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchInterval') is not None:
            self.batch_interval = m.get('batchInterval')

        if m.get('maxParallelism') is not None:
            self.max_parallelism = m.get('maxParallelism')

        if m.get('pausePolicy') is not None:
            self.pause_policy = m.get('pausePolicy')

        return self

class UpdateNodePoolComponentRequestConfig(DaraModel):
    def __init__(
        self,
        custom_config: Dict[str, str] = None,
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
            result['customConfig'] = self.custom_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customConfig') is not None:
            self.custom_config = m.get('customConfig')

        return self

