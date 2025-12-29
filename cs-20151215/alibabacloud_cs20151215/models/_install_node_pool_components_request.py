# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class InstallNodePoolComponentsRequest(DaraModel):
    def __init__(
        self,
        components: List[main_models.InstallNodePoolComponentsRequestComponents] = None,
        node_names: List[str] = None,
        rolling_policy: main_models.InstallNodePoolComponentsRequestRollingPolicy = None,
    ):
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

class InstallNodePoolComponentsRequestComponents(DaraModel):
    def __init__(
        self,
        config: main_models.InstallNodePoolComponentsRequestComponentsConfig = None,
        name: str = None,
        version: str = None,
    ):
        self.config = config
        # This parameter is required.
        self.name = name
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

