# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePortfolioRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        portfolio_id: str = None,
        portfolio_name: str = None,
        provider_name: str = None,
    ):
        # 产品组合描述
        self.description = description
        # 代表资源一级ID的资源属性字段
        # 
        # This parameter is required.
        self.portfolio_id = portfolio_id
        # 代表资源名称的资源属性字段
        # 
        # This parameter is required.
        self.portfolio_name = portfolio_name
        # 产品组合提供方
        # 
        # This parameter is required.
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        return self

