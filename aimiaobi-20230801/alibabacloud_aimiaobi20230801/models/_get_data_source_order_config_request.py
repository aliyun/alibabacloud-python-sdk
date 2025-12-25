# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataSourceOrderConfigRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        generate_technology: str = None,
        product_code: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.generate_technology = generate_technology
        # This parameter is required.
        self.product_code = product_code

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('GenerateTechnology') is not None:
            self.generate_technology = m.get('GenerateTechnology')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

