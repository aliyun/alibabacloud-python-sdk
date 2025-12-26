# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class NodeSpec(DaraModel):
    def __init__(
        self,
        binding_policy: main_models.BindingPolicy = None,
        count: int = None,
        hyper_type: str = None,
        type: str = None,
    ):
        self.binding_policy = binding_policy
        self.count = count
        self.hyper_type = hyper_type
        self.type = type

    def validate(self):
        if self.binding_policy:
            self.binding_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_policy is not None:
            result['BindingPolicy'] = self.binding_policy.to_map()

        if self.count is not None:
            result['Count'] = self.count

        if self.hyper_type is not None:
            result['HyperType'] = self.hyper_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingPolicy') is not None:
            temp_model = main_models.BindingPolicy()
            self.binding_policy = temp_model.from_map(m.get('BindingPolicy'))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('HyperType') is not None:
            self.hyper_type = m.get('HyperType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

