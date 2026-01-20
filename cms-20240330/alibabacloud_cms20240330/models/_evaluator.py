# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class Evaluator(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        data_scope: str = None,
        filters: Dict[str, str] = None,
        name: str = None,
        result_name: str = None,
        result_type: str = None,
        variable_mapping: Dict[str, str] = None,
    ):
        self.config = config
        self.data_scope = data_scope
        self.filters = filters
        self.name = name
        self.result_name = result_name
        self.result_type = result_type
        self.variable_mapping = variable_mapping

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.data_scope is not None:
            result['dataScope'] = self.data_scope

        if self.filters is not None:
            result['filters'] = self.filters

        if self.name is not None:
            result['name'] = self.name

        if self.result_name is not None:
            result['resultName'] = self.result_name

        if self.result_type is not None:
            result['resultType'] = self.result_type

        if self.variable_mapping is not None:
            result['variableMapping'] = self.variable_mapping

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('dataScope') is not None:
            self.data_scope = m.get('dataScope')

        if m.get('filters') is not None:
            self.filters = m.get('filters')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resultName') is not None:
            self.result_name = m.get('resultName')

        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')

        if m.get('variableMapping') is not None:
            self.variable_mapping = m.get('variableMapping')

        return self

