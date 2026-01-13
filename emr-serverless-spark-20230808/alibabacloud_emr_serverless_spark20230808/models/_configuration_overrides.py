# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ConfigurationOverrides(DaraModel):
    def __init__(
        self,
        configurations: List[main_models.ConfigurationOverridesConfigurations] = None,
    ):
        self.configurations = configurations

    def validate(self):
        if self.configurations:
            for v1 in self.configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['configurations'] = []
        if self.configurations is not None:
            for k1 in self.configurations:
                result['configurations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configurations = []
        if m.get('configurations') is not None:
            for k1 in m.get('configurations'):
                temp_model = main_models.ConfigurationOverridesConfigurations()
                self.configurations.append(temp_model.from_map(k1))

        return self



class ConfigurationOverridesConfigurations(DaraModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        self.config_file_name = config_file_name
        self.config_item_key = config_item_key
        self.config_item_value = config_item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_file_name is not None:
            result['configFileName'] = self.config_file_name

        if self.config_item_key is not None:
            result['configItemKey'] = self.config_item_key

        if self.config_item_value is not None:
            result['configItemValue'] = self.config_item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configFileName') is not None:
            self.config_file_name = m.get('configFileName')

        if m.get('configItemKey') is not None:
            self.config_item_key = m.get('configItemKey')

        if m.get('configItemValue') is not None:
            self.config_item_value = m.get('configItemValue')

        return self

