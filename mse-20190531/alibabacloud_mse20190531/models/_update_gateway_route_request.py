# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayRouteRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        description: str = None,
        destination_type: str = None,
        direct_response_json: main_models.UpdateGatewayRouteRequestDirectResponseJSON = None,
        domain_id_list_json: str = None,
        enable_waf: bool = None,
        fallback: bool = None,
        fallback_services: List[main_models.UpdateGatewayRouteRequestFallbackServices] = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
        name: str = None,
        predicates: main_models.UpdateGatewayRouteRequestPredicates = None,
        redirect_json: main_models.UpdateGatewayRouteRequestRedirectJSON = None,
        route_order: int = None,
        services: List[main_models.UpdateGatewayRouteRequestServices] = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        self.description = description
        # The destination service type.
        self.destination_type = destination_type
        # The information about service mocking.
        self.direct_response_json = direct_response_json
        # The associated domain name.
        self.domain_id_list_json = domain_id_list_json
        # Specifies whether to activate Web Application Firewall (WAF).
        self.enable_waf = enable_waf
        # Specifies whether to enable the Fallback service.
        self.fallback = fallback
        # The information about the Fallback service.
        self.fallback_services = fallback_services
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the route.
        self.id = id
        # The name of the route.
        self.name = name
        # The route matching conditions.
        self.predicates = predicates
        # The information about redirection.
        self.redirect_json = redirect_json
        # The sequence number of the route.
        self.route_order = route_order
        # The information about destination services.
        self.services = services

    def validate(self):
        if self.direct_response_json:
            self.direct_response_json.validate()
        if self.fallback_services:
            for v1 in self.fallback_services:
                 if v1:
                    v1.validate()
        if self.predicates:
            self.predicates.validate()
        if self.redirect_json:
            self.redirect_json.validate()
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.direct_response_json is not None:
            result['DirectResponseJSON'] = self.direct_response_json.to_map()

        if self.domain_id_list_json is not None:
            result['DomainIdListJSON'] = self.domain_id_list_json

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

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.predicates is not None:
            result['Predicates'] = self.predicates.to_map()

        if self.redirect_json is not None:
            result['RedirectJSON'] = self.redirect_json.to_map()

        if self.route_order is not None:
            result['RouteOrder'] = self.route_order

        result['Services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['Services'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('DirectResponseJSON') is not None:
            temp_model = main_models.UpdateGatewayRouteRequestDirectResponseJSON()
            self.direct_response_json = temp_model.from_map(m.get('DirectResponseJSON'))

        if m.get('DomainIdListJSON') is not None:
            self.domain_id_list_json = m.get('DomainIdListJSON')

        if m.get('EnableWaf') is not None:
            self.enable_waf = m.get('EnableWaf')

        if m.get('Fallback') is not None:
            self.fallback = m.get('Fallback')

        self.fallback_services = []
        if m.get('FallbackServices') is not None:
            for k1 in m.get('FallbackServices'):
                temp_model = main_models.UpdateGatewayRouteRequestFallbackServices()
                self.fallback_services.append(temp_model.from_map(k1))

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Predicates') is not None:
            temp_model = main_models.UpdateGatewayRouteRequestPredicates()
            self.predicates = temp_model.from_map(m.get('Predicates'))

        if m.get('RedirectJSON') is not None:
            temp_model = main_models.UpdateGatewayRouteRequestRedirectJSON()
            self.redirect_json = temp_model.from_map(m.get('RedirectJSON'))

        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')

        self.services = []
        if m.get('Services') is not None:
            for k1 in m.get('Services'):
                temp_model = main_models.UpdateGatewayRouteRequestServices()
                self.services.append(temp_model.from_map(k1))

        return self

class UpdateGatewayRouteRequestServices(DaraModel):
    def __init__(
        self,
        agreement_type: str = None,
        group_name: str = None,
        http_dubbo_transcoder: main_models.UpdateGatewayRouteRequestServicesHttpDubboTranscoder = None,
        name: str = None,
        namespace: str = None,
        percent: int = None,
        service_id: int = None,
        service_port: int = None,
        source_type: str = None,
        version: str = None,
    ):
        # The type of the protocol. Valid values:
        self.agreement_type = agreement_type
        # The name of the group to which the service belongs.
        self.group_name = group_name
        # The transcoder of the Dubbo protocol.
        self.http_dubbo_transcoder = http_dubbo_transcoder
        # The name.
        self.name = name
        # The namespace in which the service resides.
        self.namespace = namespace
        # The percentage.
        self.percent = percent
        # The ID of the service.
        self.service_id = service_id
        # The Dubbo port number.
        self.service_port = service_port
        # The source type.
        self.source_type = source_type
        # The version of the service.
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

        if m.get('HttpDubboTranscoder') is not None:
            temp_model = main_models.UpdateGatewayRouteRequestServicesHttpDubboTranscoder()
            self.http_dubbo_transcoder = temp_model.from_map(m.get('HttpDubboTranscoder'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class UpdateGatewayRouteRequestServicesHttpDubboTranscoder(DaraModel):
    def __init__(
        self,
        dubbo_service_group: str = None,
        dubbo_service_name: str = None,
        dubbo_service_version: str = None,
        mothed_map_list: List[main_models.UpdateGatewayRouteRequestServicesHttpDubboTranscoderMothedMapList] = None,
    ):
        # The Dubbo service group.
        self.dubbo_service_group = dubbo_service_group
        # The name of the Dubbo service.
        self.dubbo_service_name = dubbo_service_name
        # The version of the Dubbo service.
        self.dubbo_service_version = dubbo_service_version
        # The forwarding rules of the Dubbo service.
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
                temp_model = main_models.UpdateGatewayRouteRequestServicesHttpDubboTranscoderMothedMapList()
                self.mothed_map_list.append(temp_model.from_map(k1))

        return self

class UpdateGatewayRouteRequestServicesHttpDubboTranscoderMothedMapList(DaraModel):
    def __init__(
        self,
        dubbo_mothed_name: str = None,
        http_mothed: str = None,
        mothedpath: str = None,
        param_maps_list: List[main_models.UpdateGatewayRouteRequestServicesHttpDubboTranscoderMothedMapListParamMapsList] = None,
        pass_through_all_headers: str = None,
        pass_through_list: List[str] = None,
    ):
        # The method name of the Dubbo service.
        self.dubbo_mothed_name = dubbo_mothed_name
        # The HTTP method.
        # 
        # > Valid values:
        # 
        # *   ALL_GET
        # 
        # *   ALL_POST
        # 
        # *   ALL_PUT
        # 
        # *   ALL_DELETE
        # 
        # *   ALL_PATCH
        self.http_mothed = http_mothed
        # The path that is used to match a method.
        self.mothedpath = mothedpath
        # The information of parameter mappings.
        self.param_maps_list = param_maps_list
        # The pass-through type of the header.
        # 
        # > Valid values:
        # 
        # *   PASS_ALL: All headers are passed through.
        # 
        # *   PASS_NOT: All headers are not passed through.
        # 
        # *   PASS_ASSIGN: Specified headers are passed through.
        self.pass_through_all_headers = pass_through_all_headers
        # The list of headers to be passed through.
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
                temp_model = main_models.UpdateGatewayRouteRequestServicesHttpDubboTranscoderMothedMapListParamMapsList()
                self.param_maps_list.append(temp_model.from_map(k1))

        if m.get('PassThroughAllHeaders') is not None:
            self.pass_through_all_headers = m.get('PassThroughAllHeaders')

        if m.get('PassThroughList') is not None:
            self.pass_through_list = m.get('PassThroughList')

        return self

class UpdateGatewayRouteRequestServicesHttpDubboTranscoderMothedMapListParamMapsList(DaraModel):
    def __init__(
        self,
        extract_key: str = None,
        extract_key_spec: str = None,
        mapping_type: str = None,
    ):
        # The key extracted from the input parameter.
        self.extract_key = extract_key
        # The position of the input parameter.
        # 
        # > Valid values:
        # 
        # *   `ALL_QUERY_PARAMETER`: request parameter
        # 
        # *   `ALL_HEADER`: request header
        # 
        # *   `ALL_PATH`: request path
        # 
        # *   `ALL_BODY`: request body
        self.extract_key_spec = extract_key_spec
        # The type of the backend service parameter.
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

class UpdateGatewayRouteRequestRedirectJSON(DaraModel):
    def __init__(
        self,
        code: int = None,
        host: str = None,
        path: str = None,
    ):
        # The status code returned.
        self.code = code
        # The hostname to be redirected to.
        self.host = host
        # The path to be redirected to.
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

class UpdateGatewayRouteRequestPredicates(DaraModel):
    def __init__(
        self,
        header_predicates: List[main_models.UpdateGatewayRouteRequestPredicatesHeaderPredicates] = None,
        method_predicates: List[str] = None,
        path_predicates: main_models.UpdateGatewayRouteRequestPredicatesPathPredicates = None,
        query_predicates: List[main_models.UpdateGatewayRouteRequestPredicatesQueryPredicates] = None,
    ):
        # The information about header matching.
        self.header_predicates = header_predicates
        # The information about method matching.
        self.method_predicates = method_predicates
        # The information about path matching.
        self.path_predicates = path_predicates
        # The information about parameter matching.
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
                temp_model = main_models.UpdateGatewayRouteRequestPredicatesHeaderPredicates()
                self.header_predicates.append(temp_model.from_map(k1))

        if m.get('MethodPredicates') is not None:
            self.method_predicates = m.get('MethodPredicates')

        if m.get('PathPredicates') is not None:
            temp_model = main_models.UpdateGatewayRouteRequestPredicatesPathPredicates()
            self.path_predicates = temp_model.from_map(m.get('PathPredicates'))

        self.query_predicates = []
        if m.get('QueryPredicates') is not None:
            for k1 in m.get('QueryPredicates'):
                temp_model = main_models.UpdateGatewayRouteRequestPredicatesQueryPredicates()
                self.query_predicates.append(temp_model.from_map(k1))

        return self

class UpdateGatewayRouteRequestPredicatesQueryPredicates(DaraModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.key = key
        # The matching type.
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

class UpdateGatewayRouteRequestPredicatesPathPredicates(DaraModel):
    def __init__(
        self,
        ignore_case: bool = None,
        path: str = None,
        type: str = None,
    ):
        # Specifies whether to perform case-insensitive matching.
        self.ignore_case = ignore_case
        # The path used for route matching.
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

class UpdateGatewayRouteRequestPredicatesHeaderPredicates(DaraModel):
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

class UpdateGatewayRouteRequestFallbackServices(DaraModel):
    def __init__(
        self,
        agreement_type: str = None,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        percent: int = None,
        service_id: int = None,
        service_port: int = None,
        source_type: str = None,
        version: str = None,
    ):
        # The type of the protocol. Valid values:
        self.agreement_type = agreement_type
        # The name of the group to which the service belongs.
        self.group_name = group_name
        # The name.
        self.name = name
        # The namespace in which the service resides.
        self.namespace = namespace
        # The weight in the form of a percentage value.
        self.percent = percent
        # The ID of the service.
        self.service_id = service_id
        # The service port number.
        self.service_port = service_port
        # The source type.
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

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class UpdateGatewayRouteRequestDirectResponseJSON(DaraModel):
    def __init__(
        self,
        body: str = None,
        code: int = None,
    ):
        # The mock return value.
        self.body = body
        # The mock return code.
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

