# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeRenderingInstanceConfigurationRequest(DaraModel):
    def __init__(
        self,
        configuration: List[main_models.DescribeRenderingInstanceConfigurationRequestConfiguration] = None,
        rendering_instance_id: str = None,
    ):
        self.configuration = configuration
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

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

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configuration = []
        if m.get('Configuration') is not None:
            for k1 in m.get('Configuration'):
                temp_model = main_models.DescribeRenderingInstanceConfigurationRequestConfiguration()
                self.configuration.append(temp_model.from_map(k1))

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

class DescribeRenderingInstanceConfigurationRequestConfiguration(DaraModel):
    def __init__(
        self,
        attribute_names: List[str] = None,
        module_name: str = None,
    ):
        self.attribute_names = attribute_names
        # This parameter is required.
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_names is not None:
            result['AttributeNames'] = self.attribute_names

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeNames') is not None:
            self.attribute_names = m.get('AttributeNames')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

