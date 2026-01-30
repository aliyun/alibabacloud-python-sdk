# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeRenderingInstanceConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        configuration: List[main_models.DescribeRenderingInstanceConfigurationResponseBodyConfiguration] = None,
        request_id: str = None,
    ):
        self.configuration = configuration
        self.request_id = request_id

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
        result['Configuration'] = []
        if self.configuration is not None:
            for k1 in self.configuration:
                result['Configuration'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configuration = []
        if m.get('Configuration') is not None:
            for k1 in m.get('Configuration'):
                temp_model = main_models.DescribeRenderingInstanceConfigurationResponseBodyConfiguration()
                self.configuration.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRenderingInstanceConfigurationResponseBodyConfiguration(DaraModel):
    def __init__(
        self,
        attributes: List[main_models.DescribeRenderingInstanceConfigurationResponseBodyConfigurationAttributes] = None,
        module_name: str = None,
    ):
        self.attributes = attributes
        self.module_name = module_name

    def validate(self):
        if self.attributes:
            for v1 in self.attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attributes'] = []
        if self.attributes is not None:
            for k1 in self.attributes:
                result['Attributes'].append(k1.to_map() if k1 else None)

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k1 in m.get('Attributes'):
                temp_model = main_models.DescribeRenderingInstanceConfigurationResponseBodyConfigurationAttributes()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

class DescribeRenderingInstanceConfigurationResponseBodyConfigurationAttributes(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: Any = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

