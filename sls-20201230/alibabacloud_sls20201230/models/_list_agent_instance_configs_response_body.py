# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ListAgentInstanceConfigsResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListAgentInstanceConfigsResponseBodyConfigs] = None,
        size: int = None,
        total: int = None,
    ):
        self.configs = configs
        self.size = size
        self.total = total

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['configs'].append(k1.to_map() if k1 else None)

        if self.size is not None:
            result['size'] = self.size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('configs') is not None:
            for k1 in m.get('configs'):
                temp_model = main_models.ListAgentInstanceConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAgentInstanceConfigsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        config_type: str = None,
    ):
        self.attributes = attributes
        self.config_type = config_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.config_type is not None:
            result['configType'] = self.config_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        return self

