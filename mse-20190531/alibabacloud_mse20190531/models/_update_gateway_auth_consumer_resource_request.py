# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayAuthConsumerResourceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        consumer_id: int = None,
        gateway_unique_id: str = None,
        resource_list: List[main_models.UpdateGatewayAuthConsumerResourceRequestResourceList] = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The gateway authentication consumer ID.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # The unique ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # The gateway authentication consumer ID.
        self.resource_list = resource_list

    def validate(self):
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()

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

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.UpdateGatewayAuthConsumerResourceRequestResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        return self

class UpdateGatewayAuthConsumerResourceRequestResourceList(DaraModel):
    def __init__(
        self,
        route_id: int = None,
        route_name: str = None,
    ):
        # The route ID.
        self.route_id = route_id
        # The name of the route.
        self.route_name = route_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_id is not None:
            result['RouteId'] = self.route_id

        if self.route_name is not None:
            result['RouteName'] = self.route_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')

        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')

        return self

