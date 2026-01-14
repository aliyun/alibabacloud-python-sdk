# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListGatewayRouteOnAuthResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListGatewayRouteOnAuthResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The details of the data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListGatewayRouteOnAuthResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListGatewayRouteOnAuthResponseBodyData(DaraModel):
    def __init__(
        self,
        domain_id: int = None,
        domain_id_list: List[int] = None,
        domain_name: str = None,
        domain_name_list: List[str] = None,
        gateway_id: str = None,
        gateway_unique_id: str = None,
        id: int = None,
        name: str = None,
        route_predicates: main_models.ListGatewayRouteOnAuthResponseBodyDataRoutePredicates = None,
    ):
        # The domain ID.
        self.domain_id = domain_id
        # The domain IDs.
        self.domain_id_list = domain_id_list
        # The domain name.
        self.domain_name = domain_name
        # The domain names.
        self.domain_name_list = domain_name_list
        # The gateway ID.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The route ID.
        self.id = id
        # The name of the route.
        self.name = name
        # The information about route matching.
        self.route_predicates = route_predicates

    def validate(self):
        if self.route_predicates:
            self.route_predicates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_id_list is not None:
            result['DomainIdList'] = self.domain_id_list

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_name_list is not None:
            result['DomainNameList'] = self.domain_name_list

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.route_predicates is not None:
            result['RoutePredicates'] = self.route_predicates.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainIdList') is not None:
            self.domain_id_list = m.get('DomainIdList')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainNameList') is not None:
            self.domain_name_list = m.get('DomainNameList')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RoutePredicates') is not None:
            temp_model = main_models.ListGatewayRouteOnAuthResponseBodyDataRoutePredicates()
            self.route_predicates = temp_model.from_map(m.get('RoutePredicates'))

        return self

class ListGatewayRouteOnAuthResponseBodyDataRoutePredicates(DaraModel):
    def __init__(
        self,
        path_predicates: main_models.ListGatewayRouteOnAuthResponseBodyDataRoutePredicatesPathPredicates = None,
    ):
        # The information about route matching.
        self.path_predicates = path_predicates

    def validate(self):
        if self.path_predicates:
            self.path_predicates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path_predicates is not None:
            result['PathPredicates'] = self.path_predicates.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PathPredicates') is not None:
            temp_model = main_models.ListGatewayRouteOnAuthResponseBodyDataRoutePredicatesPathPredicates()
            self.path_predicates = temp_model.from_map(m.get('PathPredicates'))

        return self

class ListGatewayRouteOnAuthResponseBodyDataRoutePredicatesPathPredicates(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The path.
        self.path = path
        # The matching type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

