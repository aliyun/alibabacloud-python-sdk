# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListNodePoolComponentInstanceNodesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        node_list: List[main_models.ListNodePoolComponentInstanceNodesResponseBodyNodeList] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.node_list = node_list
        self.total_count = total_count

    def validate(self):
        if self.node_list:
            for v1 in self.node_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['max_results'] = self.max_results

        if self.next_token is not None:
            result['next_token'] = self.next_token

        result['node_list'] = []
        if self.node_list is not None:
            for k1 in self.node_list:
                result['node_list'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['total_count'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')

        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')

        self.node_list = []
        if m.get('node_list') is not None:
            for k1 in m.get('node_list'):
                temp_model = main_models.ListNodePoolComponentInstanceNodesResponseBodyNodeList()
                self.node_list.append(temp_model.from_map(k1))

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        return self

class ListNodePoolComponentInstanceNodesResponseBodyNodeList(DaraModel):
    def __init__(
        self,
        component: main_models.ListNodePoolComponentInstanceNodesResponseBodyNodeListComponent = None,
        instance_id: str = None,
        node_name: str = None,
    ):
        self.component = component
        self.instance_id = instance_id
        self.node_name = node_name

    def validate(self):
        if self.component:
            self.component.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component is not None:
            result['component'] = self.component.to_map()

        if self.instance_id is not None:
            result['instance_id'] = self.instance_id

        if self.node_name is not None:
            result['node_name'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('component') is not None:
            temp_model = main_models.ListNodePoolComponentInstanceNodesResponseBodyNodeListComponent()
            self.component = temp_model.from_map(m.get('component'))

        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')

        if m.get('node_name') is not None:
            self.node_name = m.get('node_name')

        return self

class ListNodePoolComponentInstanceNodesResponseBodyNodeListComponent(DaraModel):
    def __init__(
        self,
        config: main_models.ListNodePoolComponentInstanceNodesResponseBodyNodeListComponentConfig = None,
        config_revision: str = None,
        name: str = None,
        version: str = None,
    ):
        self.config = config
        self.config_revision = config_revision
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

        if self.config_revision is not None:
            result['config_revision'] = self.config_revision

        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.ListNodePoolComponentInstanceNodesResponseBodyNodeListComponentConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('config_revision') is not None:
            self.config_revision = m.get('config_revision')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListNodePoolComponentInstanceNodesResponseBodyNodeListComponentConfig(DaraModel):
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

