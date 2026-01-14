# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayRouteWafStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.UpdateGatewayRouteWafStatusResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. A value of 200 indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateGatewayRouteWafStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        cors: main_models.UpdateGatewayRouteWafStatusResponseBodyDataCors = None,
        default_service_id: int = None,
        default_service_name: str = None,
        destination_type: str = None,
        direct_response: main_models.UpdateGatewayRouteWafStatusResponseBodyDataDirectResponse = None,
        domain_id: int = None,
        domain_id_list: List[int] = None,
        domain_name: str = None,
        domain_name_list: List[str] = None,
        enable_waf: bool = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        httprewrite: main_models.UpdateGatewayRouteWafStatusResponseBodyDataHTTPRewrite = None,
        header_op: main_models.UpdateGatewayRouteWafStatusResponseBodyDataHeaderOp = None,
        id: int = None,
        name: str = None,
        predicates: str = None,
        redirect: main_models.UpdateGatewayRouteWafStatusResponseBodyDataRedirect = None,
        retry: main_models.UpdateGatewayRouteWafStatusResponseBodyDataRetry = None,
        route_order: int = None,
        route_predicates: main_models.UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicates = None,
        route_services: List[main_models.UpdateGatewayRouteWafStatusResponseBodyDataRouteServices] = None,
        services: str = None,
        status: int = None,
        timeout: main_models.UpdateGatewayRouteWafStatusResponseBodyDataTimeout = None,
    ):
        # The configuration for cross-origin resource sharing (CORS).
        self.cors = cors
        # The default service ID.
        self.default_service_id = default_service_id
        # The default service name.
        self.default_service_name = default_service_name
        # The destination service type.
        self.destination_type = destination_type
        # The information about service mocking.
        self.direct_response = direct_response
        # The domain ID.
        self.domain_id = domain_id
        # The list of domain IDs.
        self.domain_id_list = domain_id_list
        # The domain name.
        self.domain_name = domain_name
        # The domain names.
        self.domain_name_list = domain_name_list
        # Indicates whether WAF is activated.
        self.enable_waf = enable_waf
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The information about the rewrite policy.
        self.httprewrite = httprewrite
        # The header settings.
        self.header_op = header_op
        # The ID of the route.
        self.id = id
        # The name of the route.
        self.name = name
        # The matching rule.
        self.predicates = predicates
        # The configuration of the redirection.
        self.redirect = redirect
        # The retry configuration.
        self.retry = retry
        # The sequence number of the route.
        self.route_order = route_order
        # The information about route matching.
        self.route_predicates = route_predicates
        # The information about services.
        self.route_services = route_services
        # The information about services.
        self.services = services
        # The status of the route.
        self.status = status
        # The timeout configuration.
        self.timeout = timeout

    def validate(self):
        if self.cors:
            self.cors.validate()
        if self.direct_response:
            self.direct_response.validate()
        if self.httprewrite:
            self.httprewrite.validate()
        if self.header_op:
            self.header_op.validate()
        if self.redirect:
            self.redirect.validate()
        if self.retry:
            self.retry.validate()
        if self.route_predicates:
            self.route_predicates.validate()
        if self.route_services:
            for v1 in self.route_services:
                 if v1:
                    v1.validate()
        if self.timeout:
            self.timeout.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cors is not None:
            result['Cors'] = self.cors.to_map()

        if self.default_service_id is not None:
            result['DefaultServiceId'] = self.default_service_id

        if self.default_service_name is not None:
            result['DefaultServiceName'] = self.default_service_name

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.direct_response is not None:
            result['DirectResponse'] = self.direct_response.to_map()

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_id_list is not None:
            result['DomainIdList'] = self.domain_id_list

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_name_list is not None:
            result['DomainNameList'] = self.domain_name_list

        if self.enable_waf is not None:
            result['EnableWaf'] = self.enable_waf

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.httprewrite is not None:
            result['HTTPRewrite'] = self.httprewrite.to_map()

        if self.header_op is not None:
            result['HeaderOp'] = self.header_op.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.predicates is not None:
            result['Predicates'] = self.predicates

        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()

        if self.retry is not None:
            result['Retry'] = self.retry.to_map()

        if self.route_order is not None:
            result['RouteOrder'] = self.route_order

        if self.route_predicates is not None:
            result['RoutePredicates'] = self.route_predicates.to_map()

        result['RouteServices'] = []
        if self.route_services is not None:
            for k1 in self.route_services:
                result['RouteServices'].append(k1.to_map() if k1 else None)

        if self.services is not None:
            result['Services'] = self.services

        if self.status is not None:
            result['Status'] = self.status

        if self.timeout is not None:
            result['Timeout'] = self.timeout.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cors') is not None:
            temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataCors()
            self.cors = temp_model.from_map(m.get('Cors'))

        if m.get('DefaultServiceId') is not None:
            self.default_service_id = m.get('DefaultServiceId')

        if m.get('DefaultServiceName') is not None:
            self.default_service_name = m.get('DefaultServiceName')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('DirectResponse') is not None:
            temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataDirectResponse()
            self.direct_response = temp_model.from_map(m.get('DirectResponse'))

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainIdList') is not None:
            self.domain_id_list = m.get('DomainIdList')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainNameList') is not None:
            self.domain_name_list = m.get('DomainNameList')

        if m.get('EnableWaf') is not None:
            self.enable_waf = m.get('EnableWaf')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HTTPRewrite') is not None:
            temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataHTTPRewrite()
            self.httprewrite = temp_model.from_map(m.get('HTTPRewrite'))

        if m.get('HeaderOp') is not None:
            temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataHeaderOp()
            self.header_op = temp_model.from_map(m.get('HeaderOp'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Predicates') is not None:
            self.predicates = m.get('Predicates')

        if m.get('Redirect') is not None:
            temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataRedirect()
            self.redirect = temp_model.from_map(m.get('Redirect'))

        if m.get('Retry') is not None:
            temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataRetry()
            self.retry = temp_model.from_map(m.get('Retry'))

        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')

        if m.get('RoutePredicates') is not None:
            temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicates()
            self.route_predicates = temp_model.from_map(m.get('RoutePredicates'))

        self.route_services = []
        if m.get('RouteServices') is not None:
            for k1 in m.get('RouteServices'):
                temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataRouteServices()
                self.route_services.append(temp_model.from_map(k1))

        if m.get('Services') is not None:
            self.services = m.get('Services')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Timeout') is not None:
            temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataTimeout()
            self.timeout = temp_model.from_map(m.get('Timeout'))

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataTimeout(DaraModel):
    def __init__(
        self,
        status: str = None,
        time_unit: str = None,
        unit_num: int = None,
    ):
        # The status.
        self.status = status
        # The time unit.
        self.time_unit = time_unit
        # The unit number.
        self.unit_num = unit_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataRouteServices(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        percent: int = None,
        service_id: int = None,
        service_name: str = None,
        source_type: str = None,
        version: str = None,
    ):
        # The name of the group to which the service belongs.
        self.group_name = group_name
        # The name of the service.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # The weight.
        self.percent = percent
        # The ID of the service.
        self.service_id = service_id
        # The name of the service.
        self.service_name = service_name
        # The source type of the service.
        self.source_type = source_type
        # The version of the service.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicates(DaraModel):
    def __init__(
        self,
        header_predicates: List[main_models.UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicatesHeaderPredicates] = None,
        method_predicates: List[str] = None,
        path_predicates: main_models.UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicatesPathPredicates = None,
        query_predicates: List[main_models.UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicatesQueryPredicates] = None,
    ):
        # The information about matching based on request headers.
        self.header_predicates = header_predicates
        # The information about method matching.
        self.method_predicates = method_predicates
        # The information about route matching.
        self.path_predicates = path_predicates
        # The parameter matching rules.
        self.query_predicates = query_predicates

    def validate(self):
        if self.header_predicates:
            for v1 in self.header_predicates:
                 if v1:
                    v1.validate()
        if self.path_predicates:
            self.path_predicates.validate()
        if self.query_predicates:
            for v1 in self.query_predicates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HeaderPredicates'] = []
        if self.header_predicates is not None:
            for k1 in self.header_predicates:
                result['HeaderPredicates'].append(k1.to_map() if k1 else None)

        if self.method_predicates is not None:
            result['MethodPredicates'] = self.method_predicates

        if self.path_predicates is not None:
            result['PathPredicates'] = self.path_predicates.to_map()

        result['QueryPredicates'] = []
        if self.query_predicates is not None:
            for k1 in self.query_predicates:
                result['QueryPredicates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.header_predicates = []
        if m.get('HeaderPredicates') is not None:
            for k1 in m.get('HeaderPredicates'):
                temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicatesHeaderPredicates()
                self.header_predicates.append(temp_model.from_map(k1))

        if m.get('MethodPredicates') is not None:
            self.method_predicates = m.get('MethodPredicates')

        if m.get('PathPredicates') is not None:
            temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicatesPathPredicates()
            self.path_predicates = temp_model.from_map(m.get('PathPredicates'))

        self.query_predicates = []
        if m.get('QueryPredicates') is not None:
            for k1 in m.get('QueryPredicates'):
                temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicatesQueryPredicates()
                self.query_predicates.append(temp_model.from_map(k1))

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicatesQueryPredicates(DaraModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.key = key
        # The type.
        self.type = type
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicatesPathPredicates(DaraModel):
    def __init__(
        self,
        ignore_case: bool = None,
        path: str = None,
        type: str = None,
    ):
        # Indicates whether case sensitivity is ignored.
        self.ignore_case = ignore_case
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
        if self.ignore_case is not None:
            result['IgnoreCase'] = self.ignore_case

        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreCase') is not None:
            self.ignore_case = m.get('IgnoreCase')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataRoutePredicatesHeaderPredicates(DaraModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        # The key of the request header.
        self.key = key
        # The matching type.
        self.type = type
        # The value of the request header.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataRetry(DaraModel):
    def __init__(
        self,
        attempts: int = None,
        http_codes: List[str] = None,
        retry_on: List[str] = None,
        status: str = None,
    ):
        # The number of retries allowed for a request.
        self.attempts = attempts
        # The HTTP status code.
        self.http_codes = http_codes
        # The retry condition.
        self.retry_on = retry_on
        # The retry status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempts is not None:
            result['Attempts'] = self.attempts

        if self.http_codes is not None:
            result['HttpCodes'] = self.http_codes

        if self.retry_on is not None:
            result['RetryOn'] = self.retry_on

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attempts') is not None:
            self.attempts = m.get('Attempts')

        if m.get('HttpCodes') is not None:
            self.http_codes = m.get('HttpCodes')

        if m.get('RetryOn') is not None:
            self.retry_on = m.get('RetryOn')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataRedirect(DaraModel):
    def __init__(
        self,
        code: int = None,
        host: str = None,
        path: str = None,
    ):
        # The response code returned.
        self.code = code
        # The hostname.
        self.host = host
        # The path.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.host is not None:
            result['Host'] = self.host

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataHeaderOp(DaraModel):
    def __init__(
        self,
        header_op_items: List[main_models.UpdateGatewayRouteWafStatusResponseBodyDataHeaderOpHeaderOpItems] = None,
        status: str = None,
    ):
        # The policy.
        self.header_op_items = header_op_items
        # The status.
        self.status = status

    def validate(self):
        if self.header_op_items:
            for v1 in self.header_op_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HeaderOpItems'] = []
        if self.header_op_items is not None:
            for k1 in self.header_op_items:
                result['HeaderOpItems'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.header_op_items = []
        if m.get('HeaderOpItems') is not None:
            for k1 in m.get('HeaderOpItems'):
                temp_model = main_models.UpdateGatewayRouteWafStatusResponseBodyDataHeaderOpHeaderOpItems()
                self.header_op_items.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataHeaderOpHeaderOpItems(DaraModel):
    def __init__(
        self,
        direction_type: str = None,
        key: str = None,
        op_type: str = None,
        value: str = None,
    ):
        # The request or response.
        self.direction_type = direction_type
        # The header key.
        self.key = key
        # The operation type.
        self.op_type = op_type
        # The header value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction_type is not None:
            result['DirectionType'] = self.direction_type

        if self.key is not None:
            result['Key'] = self.key

        if self.op_type is not None:
            result['OpType'] = self.op_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectionType') is not None:
            self.direction_type = m.get('DirectionType')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataHTTPRewrite(DaraModel):
    def __init__(
        self,
        host: str = None,
        path: str = None,
        path_type: str = None,
        pattern: str = None,
        status: str = None,
        substitution: str = None,
    ):
        # The domain name.
        self.host = host
        # The HTTP request path.
        self.path = path
        # The path type of the HTTP request.
        self.path_type = path_type
        # The matching pattern.
        self.pattern = pattern
        # The HTTP status.
        self.status = status
        # The replacement.
        self.substitution = substitution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.path is not None:
            result['Path'] = self.path

        if self.path_type is not None:
            result['PathType'] = self.path_type

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.status is not None:
            result['Status'] = self.status

        if self.substitution is not None:
            result['Substitution'] = self.substitution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PathType') is not None:
            self.path_type = m.get('PathType')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Substitution') is not None:
            self.substitution = m.get('Substitution')

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataDirectResponse(DaraModel):
    def __init__(
        self,
        body: str = None,
        code: int = None,
    ):
        # The mock return value.
        self.body = body
        # The return value.
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body

        if self.code is not None:
            result['Code'] = self.code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        return self

class UpdateGatewayRouteWafStatusResponseBodyDataCors(DaraModel):
    def __init__(
        self,
        allow_credentials: bool = None,
        allow_headers: str = None,
        allow_methods: str = None,
        allow_origins: str = None,
        expose_headers: str = None,
        status: str = None,
        time_unit: str = None,
        unit_num: int = None,
    ):
        # The credentials allowed.
        self.allow_credentials = allow_credentials
        # The headers allowed.
        self.allow_headers = allow_headers
        # The methods allowed.
        self.allow_methods = allow_methods
        # The origins allowed.
        self.allow_origins = allow_origins
        # The response headers.
        self.expose_headers = expose_headers
        # The status.
        self.status = status
        # The time unit.
        self.time_unit = time_unit
        # The unit number.
        self.unit_num = unit_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_credentials is not None:
            result['AllowCredentials'] = self.allow_credentials

        if self.allow_headers is not None:
            result['AllowHeaders'] = self.allow_headers

        if self.allow_methods is not None:
            result['AllowMethods'] = self.allow_methods

        if self.allow_origins is not None:
            result['AllowOrigins'] = self.allow_origins

        if self.expose_headers is not None:
            result['ExposeHeaders'] = self.expose_headers

        if self.status is not None:
            result['Status'] = self.status

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCredentials') is not None:
            self.allow_credentials = m.get('AllowCredentials')

        if m.get('AllowHeaders') is not None:
            self.allow_headers = m.get('AllowHeaders')

        if m.get('AllowMethods') is not None:
            self.allow_methods = m.get('AllowMethods')

        if m.get('AllowOrigins') is not None:
            self.allow_origins = m.get('AllowOrigins')

        if m.get('ExposeHeaders') is not None:
            self.expose_headers = m.get('ExposeHeaders')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')

        return self

