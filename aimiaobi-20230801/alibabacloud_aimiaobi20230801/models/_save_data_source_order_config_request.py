# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class SaveDataSourceOrderConfigRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        generate_technology: str = None,
        product_code: str = None,
        user_config_data_source_list: List[main_models.SaveDataSourceOrderConfigRequestUserConfigDataSourceList] = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.generate_technology = generate_technology
        # This parameter is required.
        self.product_code = product_code
        # This parameter is required.
        self.user_config_data_source_list = user_config_data_source_list

    def validate(self):
        if self.user_config_data_source_list:
            for v1 in self.user_config_data_source_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.generate_technology is not None:
            result['GenerateTechnology'] = self.generate_technology

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        result['UserConfigDataSourceList'] = []
        if self.user_config_data_source_list is not None:
            for k1 in self.user_config_data_source_list:
                result['UserConfigDataSourceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('GenerateTechnology') is not None:
            self.generate_technology = m.get('GenerateTechnology')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        self.user_config_data_source_list = []
        if m.get('UserConfigDataSourceList') is not None:
            for k1 in m.get('UserConfigDataSourceList'):
                temp_model = main_models.SaveDataSourceOrderConfigRequestUserConfigDataSourceList()
                self.user_config_data_source_list.append(temp_model.from_map(k1))

        return self

class SaveDataSourceOrderConfigRequestUserConfigDataSourceList(DaraModel):
    def __init__(
        self,
        code: str = None,
        enable: bool = None,
        name: str = None,
        number: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.code = code
        self.enable = enable
        self.name = name
        # This parameter is required.
        self.number = number
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.name is not None:
            result['Name'] = self.name

        if self.number is not None:
            result['Number'] = self.number

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

