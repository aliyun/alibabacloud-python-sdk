# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeAddonsResponseBody(DaraModel):
    def __init__(
        self,
        component_groups: List[main_models.DescribeAddonsResponseBodyComponentGroups] = None,
        standard_components: Dict[str, main_models.StandardComponentsValue] = None,
    ):
        # The list of the returned components.
        self.component_groups = component_groups
        # Standard components.
        self.standard_components = standard_components

    def validate(self):
        if self.component_groups:
            for v1 in self.component_groups:
                 if v1:
                    v1.validate()
        if self.standard_components:
            for v1 in self.standard_components.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComponentGroups'] = []
        if self.component_groups is not None:
            for k1 in self.component_groups:
                result['ComponentGroups'].append(k1.to_map() if k1 else None)

        result['StandardComponents'] = {}
        if self.standard_components is not None:
            for k1, v1 in self.standard_components.items():
                result['StandardComponents'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_groups = []
        if m.get('ComponentGroups') is not None:
            for k1 in m.get('ComponentGroups'):
                temp_model = main_models.DescribeAddonsResponseBodyComponentGroups()
                self.component_groups.append(temp_model.from_map(k1))

        self.standard_components = {}
        if m.get('StandardComponents') is not None:
            for k1, v1 in m.get('StandardComponents').items():
                temp_model = main_models.StandardComponentsValue()
                self.standard_components[k1] = temp_model.from_map(v1)

        return self

class DescribeAddonsResponseBodyComponentGroups(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        items: List[main_models.DescribeAddonsResponseBodyComponentGroupsItems] = None,
    ):
        # The name of the component group.
        self.group_name = group_name
        # The names of the components in the component group.
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['group_name'] = self.group_name

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.DescribeAddonsResponseBodyComponentGroupsItems()
                self.items.append(temp_model.from_map(k1))

        return self

class DescribeAddonsResponseBodyComponentGroupsItems(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the component.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

