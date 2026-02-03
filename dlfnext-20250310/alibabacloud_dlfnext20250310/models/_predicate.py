# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class Predicate(DaraModel):
    def __init__(
        self,
        children: List[main_models.Predicate] = None,
        function: str = None,
        kind: str = None,
        literals: List[Any] = None,
        transform: main_models.Transform = None,
    ):
        self.children = children
        self.function = function
        self.kind = kind
        self.literals = literals
        self.transform = transform

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()
        if self.transform:
            self.transform.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['children'].append(k1.to_map() if k1 else None)

        if self.function is not None:
            result['function'] = self.function

        if self.kind is not None:
            result['kind'] = self.kind

        if self.literals is not None:
            result['literals'] = self.literals

        if self.transform is not None:
            result['transform'] = self.transform.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('children') is not None:
            for k1 in m.get('children'):
                temp_model = main_models.Predicate()
                self.children.append(temp_model.from_map(k1))

        if m.get('function') is not None:
            self.function = m.get('function')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('literals') is not None:
            self.literals = m.get('literals')

        if m.get('transform') is not None:
            temp_model = main_models.Transform()
            self.transform = temp_model.from_map(m.get('transform'))

        return self

