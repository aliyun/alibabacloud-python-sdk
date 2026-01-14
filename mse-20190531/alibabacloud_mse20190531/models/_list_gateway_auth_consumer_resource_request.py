# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewayAuthConsumerResourceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        consumer_id: int = None,
        gateway_unique_id: str = None,
        page_num: str = None,
        page_size: str = None,
        resource_status: bool = None,
        route_name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the consumer.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # The unique ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_num = page_num
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The resource authorization status. Valid values:
        # 
        # *   true: enabled
        # *   false: disabled
        self.resource_status = resource_status
        # The name of the route.
        self.route_name = route_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status

        if self.route_name is not None:
            result['RouteName'] = self.route_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')

        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')

        return self

