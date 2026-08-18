# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListNodePoolComponentsResponseBody(DaraModel):
    def __init__(
        self,
        components: List[main_models.ListNodePoolComponentsResponseBodyComponents] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.components = components
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['components'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['max_results'] = self.max_results

        if self.next_token is not None:
            result['next_token'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components = []
        if m.get('components') is not None:
            for k1 in m.get('components'):
                temp_model = main_models.ListNodePoolComponentsResponseBodyComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')

        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')

        return self

class ListNodePoolComponentsResponseBodyComponents(DaraModel):
    def __init__(
        self,
        config_schema: str = None,
        name: str = None,
        version: str = None,
    ):
        self.config_schema = config_schema
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_schema is not None:
            result['config_schema'] = self.config_schema

        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config_schema') is not None:
            self.config_schema = m.get('config_schema')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

