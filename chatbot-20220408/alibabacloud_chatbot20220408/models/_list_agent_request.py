# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        goods_codes: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The name of the business space. Use this parameter to filter the results.
        self.agent_name = agent_name
        # The commodity code. Filters the results to return only business spaces associated with a specific commodity code.
        self.goods_codes = goods_codes
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.goods_codes is not None:
            result['GoodsCodes'] = self.goods_codes

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('GoodsCodes') is not None:
            self.goods_codes = m.get('GoodsCodes')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

