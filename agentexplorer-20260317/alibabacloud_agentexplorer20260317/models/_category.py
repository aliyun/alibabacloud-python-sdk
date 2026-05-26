# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentexplorer20260317 import models as main_models
from darabonba.model import DaraModel

class Category(DaraModel):
    def __init__(
        self,
        children: List[main_models.CategoryChildren] = None,
        code: str = None,
        name: str = None,
    ):
        self.children = children
        self.code = code
        self.name = name

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['children'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['code'] = self.code

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('children') is not None:
            for k1 in m.get('children'):
                temp_model = main_models.CategoryChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self



class CategoryChildren(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

