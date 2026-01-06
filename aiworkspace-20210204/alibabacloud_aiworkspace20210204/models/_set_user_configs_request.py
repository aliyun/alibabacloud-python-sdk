# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class SetUserConfigsRequest(DaraModel):
    def __init__(
        self,
        configs: List[main_models.SetUserConfigsRequestConfigs] = None,
    ):
        # The configurations list.
        self.configs = configs

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
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.SetUserConfigsRequestConfigs()
                self.configs.append(temp_model.from_map(k1))

        return self

class SetUserConfigsRequestConfigs(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        config_key: str = None,
        config_value: str = None,
        scope: str = None,
    ):
        # The category. Only DataPrivacyConfig is supported.
        # 
        # This parameter is required.
        self.category_name = category_name
        # The key of the configuration item.
        # 
        # This parameter is required.
        self.config_key = config_key
        # The value of the configuration item.
        # 
        # This parameter is required.
        self.config_value = config_value
        # The scope. Valid values: subUser and owner.
        # 
        # This parameter is required.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

