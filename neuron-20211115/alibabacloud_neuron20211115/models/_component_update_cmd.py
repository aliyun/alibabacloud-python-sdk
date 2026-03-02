# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class ComponentUpdateCmd(DaraModel):
    def __init__(
        self,
        configuration: List[main_models.ConfigModel] = None,
        description: str = None,
        id: int = None,
        scope: str = None,
        use_scope: str = None,
        use_type: str = None,
    ):
        self.configuration = configuration
        self.description = description
        self.id = id
        self.scope = scope
        self.use_scope = use_scope
        self.use_type = use_type

    def validate(self):
        if self.configuration:
            for v1 in self.configuration:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['configuration'] = []
        if self.configuration is not None:
            for k1 in self.configuration:
                result['configuration'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.scope is not None:
            result['scope'] = self.scope

        if self.use_scope is not None:
            result['useScope'] = self.use_scope

        if self.use_type is not None:
            result['useType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configuration = []
        if m.get('configuration') is not None:
            for k1 in m.get('configuration'):
                temp_model = main_models.ConfigModel()
                self.configuration.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('useScope') is not None:
            self.use_scope = m.get('useScope')

        if m.get('useType') is not None:
            self.use_type = m.get('useType')

        return self

