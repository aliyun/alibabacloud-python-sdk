# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListGatewayServiceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        desc_sort: bool = None,
        filter_params: main_models.ListGatewayServiceRequestFilterParams = None,
        order_item: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # Specifies whether to enable sorting.
        self.desc_sort = desc_sort
        # The parameters that are used to specify filter conditions. The values of the parameters are in the format of {"key1":"value1"}.
        self.filter_params = filter_params
        # The item based on which entries are sorted.
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
            temp_model = main_models.ListGatewayServiceRequestFilterParams()
            self.filter_params = temp_model.from_map(m.get('FilterParams'))

        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListGatewayServiceRequestFilterParams(DaraModel):
    def __init__(
        self,
        gateway_unique_id: str = None,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        service_protocol: str = None,
        source_type: str = None,
    ):
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The group.
        self.group_name = group_name
        # The name of the service.
        self.name = name
        # The namespace to which the service belongs.
        self.namespace = namespace
        # The protocol of the service.
        # 
        # *   HTTP
        # *   HTTPS
        # *   HTTP2
        # *   GRPC
        # *   DUBBO
        self.service_protocol = service_protocol
        # The type of the source.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

