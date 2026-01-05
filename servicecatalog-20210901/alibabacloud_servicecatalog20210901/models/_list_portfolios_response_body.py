# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListPortfoliosResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        portfolio_details: List[main_models.ListPortfoliosResponseBodyPortfolioDetails] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.portfolio_details = portfolio_details
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.portfolio_details:
            for v1 in self.portfolio_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PortfolioDetails'] = []
        if self.portfolio_details is not None:
            for k1 in self.portfolio_details:
                result['PortfolioDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.portfolio_details = []
        if m.get('PortfolioDetails') is not None:
            for k1 in m.get('PortfolioDetails'):
                temp_model = main_models.ListPortfoliosResponseBodyPortfolioDetails()
                self.portfolio_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPortfoliosResponseBodyPortfolioDetails(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        portfolio_arn: str = None,
        portfolio_id: str = None,
        portfolio_name: str = None,
        provider_name: str = None,
    ):
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 产品组合描述
        self.description = description
        self.portfolio_arn = portfolio_arn
        # 代表资源一级ID的资源属性字段
        self.portfolio_id = portfolio_id
        # 代表资源名称的资源属性字段
        self.portfolio_name = portfolio_name
        # 产品组合提供方
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.portfolio_arn is not None:
            result['PortfolioArn'] = self.portfolio_arn

        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PortfolioArn') is not None:
            self.portfolio_arn = m.get('PortfolioArn')

        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        return self

