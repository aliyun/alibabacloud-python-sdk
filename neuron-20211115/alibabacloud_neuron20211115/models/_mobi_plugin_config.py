# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MobiPluginConfig(DaraModel):
    def __init__(
        self,
        content: str = None,
        mappings: List[main_models.AppConfigMapping] = None,
    ):
        self.content = content
        self.mappings = mappings

    def validate(self):
        if self.mappings:
            for v1 in self.mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        result['mappings'] = []
        if self.mappings is not None:
            for k1 in self.mappings:
                result['mappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        self.mappings = []
        if m.get('mappings') is not None:
            for k1 in m.get('mappings'):
                temp_model = main_models.AppConfigMapping()
                self.mappings.append(temp_model.from_map(k1))

        return self

