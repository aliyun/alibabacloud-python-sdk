# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class GetPortfolioResponseBody(DaraModel):
    def __init__(
        self,
        portfolio_detail: main_models.GetPortfolioResponseBodyPortfolioDetail = None,
        request_id: str = None,
        tag_options: List[main_models.GetPortfolioResponseBodyTagOptions] = None,
    ):
        # The details of the product portfolio.
        self.portfolio_detail = portfolio_detail
        # The ID of the request.
        self.request_id = request_id
        # The tag options associated with the service portfolio.
        self.tag_options = tag_options

    def validate(self):
        if self.portfolio_detail:
            self.portfolio_detail.validate()
        if self.tag_options:
            for v1 in self.tag_options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.portfolio_detail is not None:
            result['PortfolioDetail'] = self.portfolio_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TagOptions'] = []
        if self.tag_options is not None:
            for k1 in self.tag_options:
                result['TagOptions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioDetail') is not None:
            temp_model = main_models.GetPortfolioResponseBodyPortfolioDetail()
            self.portfolio_detail = temp_model.from_map(m.get('PortfolioDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tag_options = []
        if m.get('TagOptions') is not None:
            for k1 in m.get('TagOptions'):
                temp_model = main_models.GetPortfolioResponseBodyTagOptions()
                self.tag_options.append(temp_model.from_map(k1))

        return self

class GetPortfolioResponseBodyTagOptions(DaraModel):
    def __init__(
        self,
        active: bool = None,
        key: str = None,
        owner: str = None,
        tag_option_id: str = None,
        value: str = None,
    ):
        # Indicates whether the tag option is enabled. Valid values:
        # 
        # - true (default)
        # - false
        self.active = active
        # The key of the tag option.
        self.key = key
        # The ID of the owner of the tag option.
        self.owner = owner
        # The ID of the tag option.
        self.tag_option_id = tag_option_id
        # The value of the tag option.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.key is not None:
            result['Key'] = self.key

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetPortfolioResponseBodyPortfolioDetail(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        portfolio_arn: str = None,
        portfolio_id: str = None,
        portfolio_name: str = None,
        provider_name: str = None,
    ):
        # The time when the product portfolio was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the product portfolio.
        self.description = description
        # The Alibaba Cloud Resource Name (ARN) of the product portfolio.
        self.portfolio_arn = portfolio_arn
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id
        # The name of the product portfolio.
        self.portfolio_name = portfolio_name
        # The provider of the product portfolio.
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

