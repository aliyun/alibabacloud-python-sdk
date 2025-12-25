# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveDataSourceOrderConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        generate_technology: str = None,
        product_code: str = None,
        user_config_data_source_list_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.generate_technology = generate_technology
        # This parameter is required.
        self.product_code = product_code
        # This parameter is required.
        self.user_config_data_source_list_shrink = user_config_data_source_list_shrink

    def validate(self):
        pass

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

        if self.user_config_data_source_list_shrink is not None:
            result['UserConfigDataSourceList'] = self.user_config_data_source_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('GenerateTechnology') is not None:
            self.generate_technology = m.get('GenerateTechnology')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('UserConfigDataSourceList') is not None:
            self.user_config_data_source_list_shrink = m.get('UserConfigDataSourceList')

        return self

