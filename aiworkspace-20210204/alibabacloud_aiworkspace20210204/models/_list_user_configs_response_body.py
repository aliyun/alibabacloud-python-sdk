# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListUserConfigsResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListUserConfigsResponseBodyConfigs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The configurations list.
        self.configs = configs
        # The request ID.
        self.request_id = request_id
        # The number of items returned.
        self.total_count = total_count

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.ListUserConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUserConfigsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        config_key: str = None,
        config_value: str = None,
        scope: str = None,
    ):
        # The category. Currently, only DataPrivacyConfig is supported.
        self.category_name = category_name
        # The key of the configuration item.
        self.config_key = config_key
        # The value of the configuration item.
        self.config_value = config_value
        # The scope. Currently, subUser and owner are supported.
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

