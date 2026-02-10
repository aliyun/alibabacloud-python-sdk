# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListVulGlobalConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vul_global_config_list: List[main_models.ListVulGlobalConfigResponseBodyVulGlobalConfigList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The configurations.
        self.vul_global_config_list = vul_global_config_list

    def validate(self):
        if self.vul_global_config_list:
            for v1 in self.vul_global_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VulGlobalConfigList'] = []
        if self.vul_global_config_list is not None:
            for k1 in self.vul_global_config_list:
                result['VulGlobalConfigList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.vul_global_config_list = []
        if m.get('VulGlobalConfigList') is not None:
            for k1 in m.get('VulGlobalConfigList'):
                temp_model = main_models.ListVulGlobalConfigResponseBodyVulGlobalConfigList()
                self.vul_global_config_list.append(temp_model.from_map(k1))

        return self

class ListVulGlobalConfigResponseBodyVulGlobalConfigList(DaraModel):
    def __init__(
        self,
        config_key: str = None,
        config_value: str = None,
    ):
        # The key of the configuration item.
        self.config_key = config_key
        # The value of the configuration item.
        self.config_value = config_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        return self

