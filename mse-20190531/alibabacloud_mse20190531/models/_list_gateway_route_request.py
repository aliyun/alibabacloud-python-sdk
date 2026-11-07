# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListGatewayRouteRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        desc_sort: bool = None,
        filter_params: main_models.ListGatewayRouteRequestFilterParams = None,
        order_item: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Language type for returned information:
        # 
        # - zh: Chinese
        # 
        # - en: English
        self.accept_language = accept_language
        # Sorting. This field is currently unavailable and being deprecated.
        self.desc_sort = desc_sort
        # Filter conditions in the format {"key1":"value1"}
        self.filter_params = filter_params
        # Sorting property.
        self.order_item = order_item
        # Page number.
        self.page_number = page_number
        # Number of instances displayed per page (currently not in effect, queries all instances by default).
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
            temp_model = main_models.ListGatewayRouteRequestFilterParams()
            self.filter_params = temp_model.from_map(m.get('FilterParams'))

        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListGatewayRouteRequestFilterParams(DaraModel):
    def __init__(
        self,
        default_service_id: int = None,
        domain_id: int = None,
        domain_name: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        name: str = None,
        path: str = None,
        route_order: int = None,
        status: int = None,
    ):
        # Default service ID
        self.default_service_id = default_service_id
        # Domain ID
        self.domain_id = domain_id
        # Associated domain
        self.domain_name = domain_name
        # Gateway ID
        self.gateway_id = gateway_id
        # Gateway unique identifier ID
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # Route name
        self.name = name
        # Route path
        self.path = path
        # Order (unused)
        self.route_order = route_order
        # Route status:
        # 
        # - Unpublished: 0
        # 
        # - Publishing: 2
        # 
        # - Published: 3
        # 
        # - Editing (updates not published): 4
        # 
        # - Unpublishing: 5
        # 
        # - Unavailable: 6
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_service_id is not None:
            result['DefaultServiceId'] = self.default_service_id

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.route_order is not None:
            result['RouteOrder'] = self.route_order

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultServiceId') is not None:
            self.default_service_id = m.get('DefaultServiceId')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

