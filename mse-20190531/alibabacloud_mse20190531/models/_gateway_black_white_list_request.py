# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GatewayBlackWhiteListRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        desc_sort: bool = None,
        filter_params: main_models.GatewayBlackWhiteListRequestFilterParams = None,
        order_item: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The language in which you want to display the results. Valid values: zh and en. zh indicates Chinese, which is the default value. en indicates English.
        self.accept_language = accept_language
        # This parameter is unavailable for public use.
        self.desc_sort = desc_sort
        # The filter parameters.
        self.filter_params = filter_params
        # This parameter is unavailable for public use.
        self.order_item = order_item
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 1.
        self.page_size = page_size

    def validate(self):
        if self.filter_params:
            self.filter_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort

        if self.filter_params is not None:
            result['FilterParams'] = self.filter_params.to_map()

        if self.order_item is not None:
            result['OrderItem'] = self.order_item

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('DescSort') is not None:
            self.desc_sort = m.get('DescSort')

        if m.get('FilterParams') is not None:
            temp_model = main_models.GatewayBlackWhiteListRequestFilterParams()
            self.filter_params = temp_model.from_map(m.get('FilterParams'))

        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class GatewayBlackWhiteListRequestFilterParams(DaraModel):
    def __init__(
        self,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        is_white: bool = None,
        resource_type: str = None,
        search_content: str = None,
        search_type: str = None,
        type: str = None,
    ):
        # The gateway ID.
        self.gateway_id = gateway_id
        # The unique ID of the gateway. If this parameter is used together with the GatewayId parameter, the value of the GatewayId parameter is used.
        self.gateway_unique_id = gateway_unique_id
        # This parameter is unavailable for public use.
        self.is_white = is_white
        # This parameter is unavailable for public use.
        self.resource_type = resource_type
        # The content that you want to query.
        self.search_content = search_content
        # The query type. Valid values:
        # 
        # *   ROUTE: The list is queried by route. If the value of this parameter is ROUTE, set the SearchContent parameter to the route name.
        # *   DOMAIN: The list is queried by domain name. If the value of this parameter is DOMAIN, set the SearchContent parameter to the domain name.
        # *   IP: The list is queried by specified IP address. If the value of this parameter is IP, set the SearchContent parameter to the IP address.
        self.search_type = search_type
        # This parameter is unavailable for public use.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.is_white is not None:
            result['IsWhite'] = self.is_white

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.search_content is not None:
            result['SearchContent'] = self.search_content

        if self.search_type is not None:
            result['SearchType'] = self.search_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SearchContent') is not None:
            self.search_content = m.get('SearchContent')

        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

