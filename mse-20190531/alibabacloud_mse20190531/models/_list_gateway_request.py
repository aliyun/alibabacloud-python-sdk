# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListGatewayRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        desc_sort: bool = None,
        filter_params: main_models.ListGatewayRequestFilterParams = None,
        order_item: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # Specifies whether to enable the sorting feature. This feature is not available.
        self.desc_sort = desc_sort
        # The details of parameters.
        self.filter_params = filter_params
        # The order information.
        self.order_item = order_item
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
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
            temp_model = main_models.ListGatewayRequestFilterParams()
            self.filter_params = temp_model.from_map(m.get('FilterParams'))

        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListGatewayRequestFilterParams(DaraModel):
    def __init__(
        self,
        gateway_type: str = None,
        gateway_unique_id: str = None,
        instance_id: str = None,
        mse_tag: str = None,
        name: str = None,
        resource_group_id: str = None,
        vpc: str = None,
    ):
        # The type of the gateway.
        self.gateway_type = gateway_type
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the instance.
        self.instance_id = instance_id
        # The tag of the instance.
        self.mse_tag = mse_tag
        # The name of the gateway.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the virtual private cloud (VPC).
        self.vpc = vpc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mse_tag is not None:
            result['MseTag'] = self.mse_tag

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.vpc is not None:
            result['Vpc'] = self.vpc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MseTag') is not None:
            self.mse_tag = m.get('MseTag')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')

        return self

