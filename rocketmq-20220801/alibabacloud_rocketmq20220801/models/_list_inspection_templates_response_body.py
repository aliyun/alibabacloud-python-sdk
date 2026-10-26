# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListInspectionTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListInspectionTemplatesResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        total: int = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListInspectionTemplatesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListInspectionTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        configuration: main_models.ListInspectionTemplatesResponseBodyDataConfiguration = None,
        description: str = None,
        name: str = None,
        params: Any = None,
        scope_type: str = None,
        template_code: str = None,
        version: str = None,
    ):
        self.configuration = configuration
        self.description = description
        self.name = name
        self.params = params
        self.scope_type = scope_type
        self.template_code = template_code
        self.version = version

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.params is not None:
            result['params'] = self.params

        if self.scope_type is not None:
            result['scopeType'] = self.scope_type

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.ListInspectionTemplatesResponseBodyDataConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListInspectionTemplatesResponseBodyDataConfiguration(DaraModel):
    def __init__(
        self,
        parameters: List[main_models.ListInspectionTemplatesResponseBodyDataConfigurationParameters] = None,
    ):
        self.parameters = parameters

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['parameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('parameters') is not None:
            for k1 in m.get('parameters'):
                temp_model = main_models.ListInspectionTemplatesResponseBodyDataConfigurationParameters()
                self.parameters.append(temp_model.from_map(k1))

        return self

class ListInspectionTemplatesResponseBodyDataConfigurationParameters(DaraModel):
    def __init__(
        self,
        default: Any = None,
        enum: List[str] = None,
        format: str = None,
        key: str = None,
        max_lookback_seconds: int = None,
        maximum: float = None,
        minimum: float = None,
        name: str = None,
        required: bool = None,
        type: str = None,
        unit: str = None,
        whole_days: bool = None,
    ):
        self.default = default
        self.enum = enum
        self.format = format
        self.key = key
        self.max_lookback_seconds = max_lookback_seconds
        self.maximum = maximum
        self.minimum = minimum
        self.name = name
        self.required = required
        self.type = type
        self.unit = unit
        self.whole_days = whole_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['default'] = self.default

        if self.enum is not None:
            result['enum'] = self.enum

        if self.format is not None:
            result['format'] = self.format

        if self.key is not None:
            result['key'] = self.key

        if self.max_lookback_seconds is not None:
            result['maxLookbackSeconds'] = self.max_lookback_seconds

        if self.maximum is not None:
            result['maximum'] = self.maximum

        if self.minimum is not None:
            result['minimum'] = self.minimum

        if self.name is not None:
            result['name'] = self.name

        if self.required is not None:
            result['required'] = self.required

        if self.type is not None:
            result['type'] = self.type

        if self.unit is not None:
            result['unit'] = self.unit

        if self.whole_days is not None:
            result['wholeDays'] = self.whole_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('default') is not None:
            self.default = m.get('default')

        if m.get('enum') is not None:
            self.enum = m.get('enum')

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('maxLookbackSeconds') is not None:
            self.max_lookback_seconds = m.get('maxLookbackSeconds')

        if m.get('maximum') is not None:
            self.maximum = m.get('maximum')

        if m.get('minimum') is not None:
            self.minimum = m.get('minimum')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('wholeDays') is not None:
            self.whole_days = m.get('wholeDays')

        return self

