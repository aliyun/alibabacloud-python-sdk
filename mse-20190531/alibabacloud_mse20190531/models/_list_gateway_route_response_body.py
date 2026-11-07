# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListGatewayRouteResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListGatewayRouteResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Code.
        self.code = code
        # Returned data.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Request result, with the following values:
        # 
        # - `true`: The request is successful.
        # 
        # - `false`: The request failed.
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
            temp_model = main_models.ListGatewayRouteResponseBodyData()
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

class ListGatewayRouteResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.ListGatewayRouteResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        # Page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Data structure.
        self.result = result
        # Total number of entries.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
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

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListGatewayRouteResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListGatewayRouteResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        comment: main_models.ListGatewayRouteResponseBodyDataResultComment = None,
        default_service_id: int = None,
        default_service_name: str = None,
        destination_type: str = None,
        direct_response: main_models.ListGatewayRouteResponseBodyDataResultDirectResponse = None,
        domain_id: int = None,
        domain_id_list: List[int] = None,
        domain_name: str = None,
        domain_name_list: List[str] = None,
        dynamic_route: bool = None,
        enable_waf: str = None,
        fallback: bool = None,
        fallback_services: List[main_models.ListGatewayRouteResponseBodyDataResultFallbackServices] = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        predicates: str = None,
        redirect: main_models.ListGatewayRouteResponseBodyDataResultRedirect = None,
        route_order: int = None,
        route_predicates: main_models.ListGatewayRouteResponseBodyDataResultRoutePredicates = None,
        route_services: List[main_models.ListGatewayRouteResponseBodyDataResultRouteServices] = None,
        services: str = None,
        status: int = None,
        type: str = None,
    ):
        # Route comment (ingress)
        self.comment = comment
        # Default service ID.
        self.default_service_id = default_service_id
        # Default service name.
        self.default_service_name = default_service_name
        # Destination type.
        self.destination_type = destination_type
        # Mock configuration
        self.direct_response = direct_response
        # Domain ID.
        self.domain_id = domain_id
        # Domain list.
        self.domain_id_list = domain_id_list
        # Domain name.
        self.domain_name = domain_name
        # Domain name list.
        self.domain_name_list = domain_name_list
        # Whether to enable dynamic routing
        self.dynamic_route = dynamic_route
        # Whether to enable WAF
        self.enable_waf = enable_waf
        # Whether to enable Fallback service.
        self.fallback = fallback
        # Fallback service.
        self.fallback_services = fallback_services
        # Gateway ID.
        self.gateway_id = gateway_id
        # Gateway unique identifier.
        self.gateway_unique_id = gateway_unique_id
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time
        self.gmt_modified = gmt_modified
        # Route ID.
        self.id = id
        # Name.
        self.name = name
        # Matching rules
        self.predicates = predicates
        # Redirection
        self.redirect = redirect
        # Order
        self.route_order = route_order
        # Matching rules
        self.route_predicates = route_predicates
        # Service.
        self.route_services = route_services
        # Service.
        self.services = services
        # Status.
        self.status = status
        # Route type
        self.type = type

    def validate(self):
        if self.comment:
            self.comment.validate()
        if self.direct_response:
            self.direct_response.validate()
        if self.fallback_services:
            for v1 in self.fallback_services:
                 if v1:
                    v1.validate()
        if self.redirect:
            self.redirect.validate()
        if self.route_predicates:
            self.route_predicates.validate()
        if self.route_services:
            for v1 in self.route_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment.to_map()

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

        if self.dynamic_route is not None:
            result['DynamicRoute'] = self.dynamic_route

        if self.enable_waf is not None:
            result['EnableWaf'] = self.enable_waf

        if self.fallback is not None:
            result['Fallback'] = self.fallback

        result['FallbackServices'] = []
        if self.fallback_services is not None:
            for k1 in self.fallback_services:
                result['FallbackServices'].append(k1.to_map() if k1 else None)

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.predicates is not None:
            result['Predicates'] = self.predicates

        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            temp_model = main_models.ListGatewayRouteResponseBodyDataResultComment()
            self.comment = temp_model.from_map(m.get('Comment'))

        if m.get('DefaultServiceId') is not None:
            self.default_service_id = m.get('DefaultServiceId')

        if m.get('DefaultServiceName') is not None:
            self.default_service_name = m.get('DefaultServiceName')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('DirectResponse') is not None:
            temp_model = main_models.ListGatewayRouteResponseBodyDataResultDirectResponse()
            self.direct_response = temp_model.from_map(m.get('DirectResponse'))

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainIdList') is not None:
            self.domain_id_list = m.get('DomainIdList')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainNameList') is not None:
            self.domain_name_list = m.get('DomainNameList')

        if m.get('DynamicRoute') is not None:
            self.dynamic_route = m.get('DynamicRoute')

        if m.get('EnableWaf') is not None:
            self.enable_waf = m.get('EnableWaf')

        if m.get('Fallback') is not None:
            self.fallback = m.get('Fallback')

        self.fallback_services = []
        if m.get('FallbackServices') is not None:
            for k1 in m.get('FallbackServices'):
                temp_model = main_models.ListGatewayRouteResponseBodyDataResultFallbackServices()
                self.fallback_services.append(temp_model.from_map(k1))

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Predicates') is not None:
            self.predicates = m.get('Predicates')

        if m.get('Redirect') is not None:
            temp_model = main_models.ListGatewayRouteResponseBodyDataResultRedirect()
            self.redirect = temp_model.from_map(m.get('Redirect'))

        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')

        if m.get('RoutePredicates') is not None:
            temp_model = main_models.ListGatewayRouteResponseBodyDataResultRoutePredicates()
            self.route_predicates = temp_model.from_map(m.get('RoutePredicates'))

        self.route_services = []
        if m.get('RouteServices') is not None:
            for k1 in m.get('RouteServices'):
                temp_model = main_models.ListGatewayRouteResponseBodyDataResultRouteServices()
                self.route_services.append(temp_model.from_map(k1))

        if m.get('Services') is not None:
            self.services = m.get('Services')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListGatewayRouteResponseBodyDataResultRouteServices(DaraModel):
    def __init__(
        self,
        agreement_type: str = None,
        group_name: str = None,
        health_status: str = None,
        http_dubbo_transcoder: main_models.ListGatewayRouteResponseBodyDataResultRouteServicesHttpDubboTranscoder = None,
        name: str = None,
        namespace: str = None,
        percent: int = None,
        service_id: int = None,
        service_name: str = None,
        service_port: int = None,
        source_type: str = None,
        unhealthy_endpoints: List[str] = None,
        version: str = None,
    ):
        # Protocol Type.
        self.agreement_type = agreement_type
        # Service group name.
        self.group_name = group_name
        # Health status
        # 
        # - Health
        # 
        # - Unhealthy
        # 
        # - Checking
        # 
        # - Unknown
        self.health_status = health_status
        # Dubbo protocol conversion body.
        self.http_dubbo_transcoder = http_dubbo_transcoder
        # Name.
        self.name = name
        # Namespace.
        self.namespace = namespace
        # Weight percentage
        self.percent = percent
        # Service ID
        self.service_id = service_id
        # Service name.
        self.service_name = service_name
        # Service port.
        self.service_port = service_port
        # Source type
        self.source_type = source_type
        # Unhealthy Endpoint list
        self.unhealthy_endpoints = unhealthy_endpoints
        # Service version.
        self.version = version

    def validate(self):
        if self.http_dubbo_transcoder:
            self.http_dubbo_transcoder.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agreement_type is not None:
            result['AgreementType'] = self.agreement_type

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.http_dubbo_transcoder is not None:
            result['HttpDubboTranscoder'] = self.http_dubbo_transcoder.to_map()

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

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.unhealthy_endpoints is not None:
            result['UnhealthyEndpoints'] = self.unhealthy_endpoints

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementType') is not None:
            self.agreement_type = m.get('AgreementType')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('HttpDubboTranscoder') is not None:
            temp_model = main_models.ListGatewayRouteResponseBodyDataResultRouteServicesHttpDubboTranscoder()
            self.http_dubbo_transcoder = temp_model.from_map(m.get('HttpDubboTranscoder'))

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

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('UnhealthyEndpoints') is not None:
            self.unhealthy_endpoints = m.get('UnhealthyEndpoints')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListGatewayRouteResponseBodyDataResultRouteServicesHttpDubboTranscoder(DaraModel):
    def __init__(
        self,
        dubbo_service_group: str = None,
        dubbo_service_name: str = None,
        dubbo_service_version: str = None,
        mothed_map_list: List[main_models.ListGatewayRouteResponseBodyDataResultRouteServicesHttpDubboTranscoderMothedMapList] = None,
    ):
        # Dubbo service group.
        self.dubbo_service_group = dubbo_service_group
        # Dubbo service name.
        self.dubbo_service_name = dubbo_service_name
        # Dubbo service version.
        self.dubbo_service_version = dubbo_service_version
        # Dubbo forwarding rule list.
        self.mothed_map_list = mothed_map_list

    def validate(self):
        if self.mothed_map_list:
            for v1 in self.mothed_map_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dubbo_service_group is not None:
            result['DubboServiceGroup'] = self.dubbo_service_group

        if self.dubbo_service_name is not None:
            result['DubboServiceName'] = self.dubbo_service_name

        if self.dubbo_service_version is not None:
            result['DubboServiceVersion'] = self.dubbo_service_version

        result['MothedMapList'] = []
        if self.mothed_map_list is not None:
            for k1 in self.mothed_map_list:
                result['MothedMapList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DubboServiceGroup') is not None:
            self.dubbo_service_group = m.get('DubboServiceGroup')

        if m.get('DubboServiceName') is not None:
            self.dubbo_service_name = m.get('DubboServiceName')

        if m.get('DubboServiceVersion') is not None:
            self.dubbo_service_version = m.get('DubboServiceVersion')

        self.mothed_map_list = []
        if m.get('MothedMapList') is not None:
            for k1 in m.get('MothedMapList'):
                temp_model = main_models.ListGatewayRouteResponseBodyDataResultRouteServicesHttpDubboTranscoderMothedMapList()
                self.mothed_map_list.append(temp_model.from_map(k1))

        return self

class ListGatewayRouteResponseBodyDataResultRouteServicesHttpDubboTranscoderMothedMapList(DaraModel):
    def __init__(
        self,
        dubbo_mothed_name: str = None,
        http_mothed: str = None,
        mothedpath: str = None,
        param_maps_list: List[main_models.ListGatewayRouteResponseBodyDataResultRouteServicesHttpDubboTranscoderMothedMapListParamMapsList] = None,
        pass_through_all_headers: str = None,
        pass_through_list: List[str] = None,
    ):
        # Dubbo method name.
        self.dubbo_mothed_name = dubbo_mothed_name
        # Http method.
        # 
        # > Supported HTTP method parameter values.
        # >
        # > - ALL_GET
        # >
        # > - ALL_POST
        # >
        # > - ALL_PUT
        # >
        # > - ALL_DELETE
        # >
        # > - ALL_PATCH
        self.http_mothed = http_mothed
        # Method matching path.
        self.mothedpath = mothedpath
        # Parameter mapping list.
        self.param_maps_list = param_maps_list
        # Header pass-through type.
        # 
        # > Pass-through type enumeration values.
        # >
        # > - Pass through all: PASS_ALL
        # >
        # > - No pass-through: PASS_NOT
        # >
        # > - Specified parameters: PASS_ASSIGN
        self.pass_through_all_headers = pass_through_all_headers
        # Specified pass-through Header list.
        self.pass_through_list = pass_through_list

    def validate(self):
        if self.param_maps_list:
            for v1 in self.param_maps_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dubbo_mothed_name is not None:
            result['DubboMothedName'] = self.dubbo_mothed_name

        if self.http_mothed is not None:
            result['HttpMothed'] = self.http_mothed

        if self.mothedpath is not None:
            result['Mothedpath'] = self.mothedpath

        result['ParamMapsList'] = []
        if self.param_maps_list is not None:
            for k1 in self.param_maps_list:
                result['ParamMapsList'].append(k1.to_map() if k1 else None)

        if self.pass_through_all_headers is not None:
            result['PassThroughAllHeaders'] = self.pass_through_all_headers

        if self.pass_through_list is not None:
            result['PassThroughList'] = self.pass_through_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DubboMothedName') is not None:
            self.dubbo_mothed_name = m.get('DubboMothedName')

        if m.get('HttpMothed') is not None:
            self.http_mothed = m.get('HttpMothed')

        if m.get('Mothedpath') is not None:
            self.mothedpath = m.get('Mothedpath')

        self.param_maps_list = []
        if m.get('ParamMapsList') is not None:
            for k1 in m.get('ParamMapsList'):
                temp_model = main_models.ListGatewayRouteResponseBodyDataResultRouteServicesHttpDubboTranscoderMothedMapListParamMapsList()
                self.param_maps_list.append(temp_model.from_map(k1))

        if m.get('PassThroughAllHeaders') is not None:
            self.pass_through_all_headers = m.get('PassThroughAllHeaders')

        if m.get('PassThroughList') is not None:
            self.pass_through_list = m.get('PassThroughList')

        return self

class ListGatewayRouteResponseBodyDataResultRouteServicesHttpDubboTranscoderMothedMapListParamMapsList(DaraModel):
    def __init__(
        self,
        extract_key: str = None,
        extract_key_spec: str = None,
        mapping_type: str = None,
    ):
        # Extract key from input.
        self.extract_key = extract_key
        # Input parameter position.
        # 
        # > Input parameter position enumeration values.
        # >
        # > - Request parameter: `ALL_QUERY_PARAMETER`
        # >
        # > - Request header: `ALL_HEADER`
        # >
        # > - Request path: `ALL_PATH`
        # >
        # > - Request body: `ALL_BODY`
        self.extract_key_spec = extract_key_spec
        # Backend parameter type.
        self.mapping_type = mapping_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extract_key is not None:
            result['ExtractKey'] = self.extract_key

        if self.extract_key_spec is not None:
            result['ExtractKeySpec'] = self.extract_key_spec

        if self.mapping_type is not None:
            result['MappingType'] = self.mapping_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtractKey') is not None:
            self.extract_key = m.get('ExtractKey')

        if m.get('ExtractKeySpec') is not None:
            self.extract_key_spec = m.get('ExtractKeySpec')

        if m.get('MappingType') is not None:
            self.mapping_type = m.get('MappingType')

        return self

class ListGatewayRouteResponseBodyDataResultRoutePredicates(DaraModel):
    def __init__(
        self,
        header_predicates: List[main_models.ListGatewayRouteResponseBodyDataResultRoutePredicatesHeaderPredicates] = None,
        method_predicates: List[str] = None,
        path_predicates: main_models.ListGatewayRouteResponseBodyDataResultRoutePredicatesPathPredicates = None,
        query_predicates: List[main_models.ListGatewayRouteResponseBodyDataResultRoutePredicatesQueryPredicates] = None,
    ):
        # Header matching
        self.header_predicates = header_predicates
        # HTTP method matching
        self.method_predicates = method_predicates
        # Route Path matching.
        self.path_predicates = path_predicates
        # Parameter matching
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
                temp_model = main_models.ListGatewayRouteResponseBodyDataResultRoutePredicatesHeaderPredicates()
                self.header_predicates.append(temp_model.from_map(k1))

        if m.get('MethodPredicates') is not None:
            self.method_predicates = m.get('MethodPredicates')

        if m.get('PathPredicates') is not None:
            temp_model = main_models.ListGatewayRouteResponseBodyDataResultRoutePredicatesPathPredicates()
            self.path_predicates = temp_model.from_map(m.get('PathPredicates'))

        self.query_predicates = []
        if m.get('QueryPredicates') is not None:
            for k1 in m.get('QueryPredicates'):
                temp_model = main_models.ListGatewayRouteResponseBodyDataResultRoutePredicatesQueryPredicates()
                self.query_predicates.append(temp_model.from_map(k1))

        return self

class ListGatewayRouteResponseBodyDataResultRoutePredicatesQueryPredicates(DaraModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        # Parameter name
        self.key = key
        # Matching type
        self.type = type
        # Matching value
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

class ListGatewayRouteResponseBodyDataResultRoutePredicatesPathPredicates(DaraModel):
    def __init__(
        self,
        ignore_case: bool = None,
        path: str = None,
        type: str = None,
    ):
        # Case insensitive
        self.ignore_case = ignore_case
        # Node path.
        self.path = path
        # Matching type.
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

class ListGatewayRouteResponseBodyDataResultRoutePredicatesHeaderPredicates(DaraModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        # Header KEY
        self.key = key
        # Matching type
        self.type = type
        # Matching value
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

class ListGatewayRouteResponseBodyDataResultRedirect(DaraModel):
    def __init__(
        self,
        code: int = None,
        host: str = None,
        path: str = None,
    ):
        # Response code.
        self.code = code
        # Redirect hostname
        self.host = host
        # Path.
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

class ListGatewayRouteResponseBodyDataResultFallbackServices(DaraModel):
    def __init__(
        self,
        agreement_type: str = None,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        percent: int = None,
        service_id: int = None,
        service_name: str = None,
        service_port: int = None,
        source_type: str = None,
        version: str = None,
    ):
        # Protocol Type.
        self.agreement_type = agreement_type
        # Service group name.
        self.group_name = group_name
        # Name.
        self.name = name
        # Service namespace.
        self.namespace = namespace
        # Weight percentage.
        self.percent = percent
        # Service ID.
        self.service_id = service_id
        # Service name.
        self.service_name = service_name
        # Service port.
        self.service_port = service_port
        # Source type.
        self.source_type = source_type
        # Service version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agreement_type is not None:
            result['AgreementType'] = self.agreement_type

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

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementType') is not None:
            self.agreement_type = m.get('AgreementType')

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

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListGatewayRouteResponseBodyDataResultDirectResponse(DaraModel):
    def __init__(
        self,
        body: str = None,
        code: int = None,
    ):
        # Mock return value
        self.body = body
        # Response code.
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

class ListGatewayRouteResponseBodyDataResultComment(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        # Status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

