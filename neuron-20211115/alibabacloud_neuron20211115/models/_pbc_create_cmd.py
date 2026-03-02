# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcCreateCmd(DaraModel):
    def __init__(
        self,
        alias: str = None,
        company: str = None,
        company_id: int = None,
        description: str = None,
        developer_id: str = None,
        industry: str = None,
        market_id: int = None,
        name: str = None,
        type: str = None,
    ):
        self.alias = alias
        self.company = company
        self.company_id = company_id
        self.description = description
        self.developer_id = developer_id
        self.industry = industry
        self.market_id = market_id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.company is not None:
            result['company'] = self.company

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.description is not None:
            result['description'] = self.description

        if self.developer_id is not None:
            result['developerId'] = self.developer_id

        if self.industry is not None:
            result['industry'] = self.industry

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('company') is not None:
            self.company = m.get('company')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('developerId') is not None:
            self.developer_id = m.get('developerId')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

