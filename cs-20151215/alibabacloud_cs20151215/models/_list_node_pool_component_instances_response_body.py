# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListNodePoolComponentInstancesResponseBody(DaraModel):
    def __init__(
        self,
        component_instances: List[main_models.ListNodePoolComponentInstancesResponseBodyComponentInstances] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.component_instances = component_instances
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.component_instances:
            for v1 in self.component_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['component_instances'] = []
        if self.component_instances is not None:
            for k1 in self.component_instances:
                result['component_instances'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['max_results'] = self.max_results

        if self.next_token is not None:
            result['next_token'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_instances = []
        if m.get('component_instances') is not None:
            for k1 in m.get('component_instances'):
                temp_model = main_models.ListNodePoolComponentInstancesResponseBodyComponentInstances()
                self.component_instances.append(temp_model.from_map(k1))

        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')

        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')

        return self

class ListNodePoolComponentInstancesResponseBodyComponentInstances(DaraModel):
    def __init__(
        self,
        config: main_models.ListNodePoolComponentInstancesResponseBodyComponentInstancesConfig = None,
        config_revision: str = None,
        name: str = None,
        state: str = None,
        version: str = None,
    ):
        self.config = config
        self.config_revision = config_revision
        self.name = name
        self.state = state
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

        if self.config_revision is not None:
            result['config_revision'] = self.config_revision

        if self.name is not None:
            result['name'] = self.name

        if self.state is not None:
            result['state'] = self.state

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.ListNodePoolComponentInstancesResponseBodyComponentInstancesConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('config_revision') is not None:
            self.config_revision = m.get('config_revision')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListNodePoolComponentInstancesResponseBodyComponentInstancesConfig(DaraModel):
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

