# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetGatewayRouteDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetGatewayRouteDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. A value of 200 indicates that the request is successful.
        self.code = code
        # The data returned.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned if the request failed.
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
            temp_model = main_models.GetGatewayRouteDetailResponseBodyData()
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

class GetGatewayRouteDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        ahas_status: int = None,
        cors: main_models.GetGatewayRouteDetailResponseBodyDataCors = None,
        default_service_id: int = None,
        default_service_name: str = None,
        description: str = None,
        destination_type: str = None,
        direct_response: main_models.GetGatewayRouteDetailResponseBodyDataDirectResponse = None,
        domain_id: int = None,
        domain_id_list: List[int] = None,
        domain_name: str = None,
        domain_name_list: List[str] = None,
        enable_waf: bool = None,
        fallback: bool = None,
        fallback_services: List[main_models.GetGatewayRouteDetailResponseBodyDataFallbackServices] = None,
        flow_mirror: main_models.GetGatewayRouteDetailResponseBodyDataFlowMirror = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        httprewrite: main_models.GetGatewayRouteDetailResponseBodyDataHTTPRewrite = None,
        header_op: main_models.GetGatewayRouteDetailResponseBodyDataHeaderOp = None,
        id: int = None,
        name: str = None,
        policies: str = None,
        predicates: str = None,
        redirect: main_models.GetGatewayRouteDetailResponseBodyDataRedirect = None,
        retry: main_models.GetGatewayRouteDetailResponseBodyDataRetry = None,
        route_order: int = None,
        route_predicates: main_models.GetGatewayRouteDetailResponseBodyDataRoutePredicates = None,
        route_services: List[main_models.GetGatewayRouteDetailResponseBodyDataRouteServices] = None,
        services: str = None,
        status: int = None,
        timeout: main_models.GetGatewayRouteDetailResponseBodyDataTimeout = None,
    ):
        # The status of Application High Availability Service (AHAS).
        self.ahas_status = ahas_status
        # The configuration for cross-origin resource sharing (CORS).
        self.cors = cors
        # The default service ID.
        self.default_service_id = default_service_id
        # The default service name.
        self.default_service_name = default_service_name
        self.description = description
        # The destination service type.
        self.destination_type = destination_type
        # The information about service mocking.
        self.direct_response = direct_response
        # The domain ID.
        self.domain_id = domain_id
        # The IDs of domains.
        self.domain_id_list = domain_id_list
        # The domain name.
        self.domain_name = domain_name
        # The list of domain names.
        self.domain_name_list = domain_name_list
        # Indicates whether Web Application Firewall (WAF) is activated.
        self.enable_waf = enable_waf
        # Indicates whether the Fallback service is enabled.
        self.fallback = fallback
        # The information of the Fallback service.
        self.fallback_services = fallback_services
        # 流量镜像配置。
        self.flow_mirror = flow_mirror
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The creation time.
        self.gmt_create = gmt_create
        # The last modification time.
        self.gmt_modified = gmt_modified
        # The information about the rewrite policy.
        self.httprewrite = httprewrite
        # The header settings.
        self.header_op = header_op
        # The ID.
        self.id = id
        # The name.
        self.name = name
        # The routing policy in a JSON string.
        self.policies = policies
        # The matching conditions.
        self.predicates = predicates
        # The configuration of the redirection.
        self.redirect = redirect
        # The retry configuration.
        self.retry = retry
        # The sequence number of the route.
        self.route_order = route_order
        # The information about route matching.
        self.route_predicates = route_predicates
        # The services.
        self.route_services = route_services
        # The configurations of services.
        self.services = services
        # The status of the route. Valid values:
        # 
        # *   0: unpublished
        # *   2: publishing
        # *   3: published
        # *   4: editing (updated but not published)
        # *   5: unpublishing
        # *   6: unavailable
        self.status = status
        # The timeout configuration.
        self.timeout = timeout

    def validate(self):
        if self.cors:
            self.cors.validate()
        if self.direct_response:
            self.direct_response.validate()
        if self.fallback_services:
            for v1 in self.fallback_services:
                 if v1:
                    v1.validate()
        if self.flow_mirror:
            self.flow_mirror.validate()
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
        if self.ahas_status is not None:
            result['AhasStatus'] = self.ahas_status

        if self.cors is not None:
            result['Cors'] = self.cors.to_map()

        if self.default_service_id is not None:
            result['DefaultServiceId'] = self.default_service_id

        if self.default_service_name is not None:
            result['DefaultServiceName'] = self.default_service_name

        if self.description is not None:
            result['Description'] = self.description

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

        if self.fallback is not None:
            result['Fallback'] = self.fallback

        result['FallbackServices'] = []
        if self.fallback_services is not None:
            for k1 in self.fallback_services:
                result['FallbackServices'].append(k1.to_map() if k1 else None)

        if self.flow_mirror is not None:
            result['FlowMirror'] = self.flow_mirror.to_map()

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

        if self.policies is not None:
            result['Policies'] = self.policies

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
        if m.get('AhasStatus') is not None:
            self.ahas_status = m.get('AhasStatus')

        if m.get('Cors') is not None:
            temp_model = main_models.GetGatewayRouteDetailResponseBodyDataCors()
            self.cors = temp_model.from_map(m.get('Cors'))

        if m.get('DefaultServiceId') is not None:
            self.default_service_id = m.get('DefaultServiceId')

        if m.get('DefaultServiceName') is not None:
            self.default_service_name = m.get('DefaultServiceName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('DirectResponse') is not None:
            temp_model = main_models.GetGatewayRouteDetailResponseBodyDataDirectResponse()
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

        if m.get('Fallback') is not None:
            self.fallback = m.get('Fallback')

        self.fallback_services = []
        if m.get('FallbackServices') is not None:
            for k1 in m.get('FallbackServices'):
                temp_model = main_models.GetGatewayRouteDetailResponseBodyDataFallbackServices()
                self.fallback_services.append(temp_model.from_map(k1))

        if m.get('FlowMirror') is not None:
            temp_model = main_models.GetGatewayRouteDetailResponseBodyDataFlowMirror()
            self.flow_mirror = temp_model.from_map(m.get('FlowMirror'))

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HTTPRewrite') is not None:
            temp_model = main_models.GetGatewayRouteDetailResponseBodyDataHTTPRewrite()
            self.httprewrite = temp_model.from_map(m.get('HTTPRewrite'))

        if m.get('HeaderOp') is not None:
            temp_model = main_models.GetGatewayRouteDetailResponseBodyDataHeaderOp()
            self.header_op = temp_model.from_map(m.get('HeaderOp'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policies') is not None:
            self.policies = m.get('Policies')

        if m.get('Predicates') is not None:
            self.predicates = m.get('Predicates')

        if m.get('Redirect') is not None:
            temp_model = main_models.GetGatewayRouteDetailResponseBodyDataRedirect()
            self.redirect = temp_model.from_map(m.get('Redirect'))

        if m.get('Retry') is not None:
            temp_model = main_models.GetGatewayRouteDetailResponseBodyDataRetry()
            self.retry = temp_model.from_map(m.get('Retry'))

        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')

        if m.get('RoutePredicates') is not None:
            temp_model = main_models.GetGatewayRouteDetailResponseBodyDataRoutePredicates()
            self.route_predicates = temp_model.from_map(m.get('RoutePredicates'))

        self.route_services = []
        if m.get('RouteServices') is not None:
            for k1 in m.get('RouteServices'):
                temp_model = main_models.GetGatewayRouteDetailResponseBodyDataRouteServices()
                self.route_services.append(temp_model.from_map(k1))

        if m.get('Services') is not None:
            self.services = m.get('Services')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Timeout') is not None:
            temp_model = main_models.GetGatewayRouteDetailResponseBodyDataTimeout()
            self.timeout = temp_model.from_map(m.get('Timeout'))

        return self

class GetGatewayRouteDetailResponseBodyDataTimeout(DaraModel):
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

class GetGatewayRouteDetailResponseBodyDataRouteServices(DaraModel):
    def __init__(
        self,
        agreement_type: str = None,
        group_name: str = None,
        health_status: str = None,
        http_dubbo_transcoder: main_models.GetGatewayRouteDetailResponseBodyDataRouteServicesHttpDubboTranscoder = None,
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
        # The protocol type.
        self.agreement_type = agreement_type
        # The name of the group to which the service belongs.
        self.group_name = group_name
        self.health_status = health_status
        self.http_dubbo_transcoder = http_dubbo_transcoder
        # The service name.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # The weight.
        self.percent = percent
        # The service ID.
        self.service_id = service_id
        # The service name.
        self.service_name = service_name
        # The port number of the service.
        self.service_port = service_port
        # The source type of the service.
        self.source_type = source_type
        self.unhealthy_endpoints = unhealthy_endpoints
        # The service version.
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
            temp_model = main_models.GetGatewayRouteDetailResponseBodyDataRouteServicesHttpDubboTranscoder()
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

class GetGatewayRouteDetailResponseBodyDataRouteServicesHttpDubboTranscoder(DaraModel):
    def __init__(
        self,
        dubbo_service_group: str = None,
        dubbo_service_name: str = None,
        dubbo_service_version: str = None,
        mothed_map_list: List[main_models.GetGatewayRouteDetailResponseBodyDataRouteServicesHttpDubboTranscoderMothedMapList] = None,
    ):
        self.dubbo_service_group = dubbo_service_group
        self.dubbo_service_name = dubbo_service_name
        self.dubbo_service_version = dubbo_service_version
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
                temp_model = main_models.GetGatewayRouteDetailResponseBodyDataRouteServicesHttpDubboTranscoderMothedMapList()
                self.mothed_map_list.append(temp_model.from_map(k1))

        return self

class GetGatewayRouteDetailResponseBodyDataRouteServicesHttpDubboTranscoderMothedMapList(DaraModel):
    def __init__(
        self,
        dubbo_mothed_name: str = None,
        http_mothed: str = None,
        mothedpath: str = None,
        param_maps_list: List[main_models.GetGatewayRouteDetailResponseBodyDataRouteServicesHttpDubboTranscoderMothedMapListParamMapsList] = None,
        pass_through_all_headers: str = None,
        pass_through_list: List[str] = None,
    ):
        self.dubbo_mothed_name = dubbo_mothed_name
        self.http_mothed = http_mothed
        self.mothedpath = mothedpath
        self.param_maps_list = param_maps_list
        self.pass_through_all_headers = pass_through_all_headers
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
                temp_model = main_models.GetGatewayRouteDetailResponseBodyDataRouteServicesHttpDubboTranscoderMothedMapListParamMapsList()
                self.param_maps_list.append(temp_model.from_map(k1))

        if m.get('PassThroughAllHeaders') is not None:
            self.pass_through_all_headers = m.get('PassThroughAllHeaders')

        if m.get('PassThroughList') is not None:
            self.pass_through_list = m.get('PassThroughList')

        return self

class GetGatewayRouteDetailResponseBodyDataRouteServicesHttpDubboTranscoderMothedMapListParamMapsList(DaraModel):
    def __init__(
        self,
        extract_key: str = None,
        extract_key_spec: str = None,
        mapping_type: str = None,
    ):
        self.extract_key = extract_key
        self.extract_key_spec = extract_key_spec
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

class GetGatewayRouteDetailResponseBodyDataRoutePredicates(DaraModel):
    def __init__(
        self,
        header_predicates: List[main_models.GetGatewayRouteDetailResponseBodyDataRoutePredicatesHeaderPredicates] = None,
        method_predicates: List[str] = None,
        path_predicates: main_models.GetGatewayRouteDetailResponseBodyDataRoutePredicatesPathPredicates = None,
        query_predicates: List[main_models.GetGatewayRouteDetailResponseBodyDataRoutePredicatesQueryPredicates] = None,
    ):
        # The information about header matching.
        self.header_predicates = header_predicates
        # The information about method matching.
        self.method_predicates = method_predicates
        # The information about route matching.
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
                temp_model = main_models.GetGatewayRouteDetailResponseBodyDataRoutePredicatesHeaderPredicates()
                self.header_predicates.append(temp_model.from_map(k1))

        if m.get('MethodPredicates') is not None:
            self.method_predicates = m.get('MethodPredicates')

        if m.get('PathPredicates') is not None:
            temp_model = main_models.GetGatewayRouteDetailResponseBodyDataRoutePredicatesPathPredicates()
            self.path_predicates = temp_model.from_map(m.get('PathPredicates'))

        self.query_predicates = []
        if m.get('QueryPredicates') is not None:
            for k1 in m.get('QueryPredicates'):
                temp_model = main_models.GetGatewayRouteDetailResponseBodyDataRoutePredicatesQueryPredicates()
                self.query_predicates.append(temp_model.from_map(k1))

        return self

class GetGatewayRouteDetailResponseBodyDataRoutePredicatesQueryPredicates(DaraModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        # The parameter name.
        self.key = key
        # The route type.
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

class GetGatewayRouteDetailResponseBodyDataRoutePredicatesPathPredicates(DaraModel):
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

class GetGatewayRouteDetailResponseBodyDataRoutePredicatesHeaderPredicates(DaraModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        # The key of the request header.
        self.key = key
        # The route type.
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

class GetGatewayRouteDetailResponseBodyDataRetry(DaraModel):
    def __init__(
        self,
        attempts: int = None,
        http_codes: List[str] = None,
        retry_on: List[str] = None,
        status: str = None,
    ):
        # The number of retries allowed.
        self.attempts = attempts
        # The HTTP status codes.
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

class GetGatewayRouteDetailResponseBodyDataRedirect(DaraModel):
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

class GetGatewayRouteDetailResponseBodyDataHeaderOp(DaraModel):
    def __init__(
        self,
        header_op_items: List[main_models.GetGatewayRouteDetailResponseBodyDataHeaderOpHeaderOpItems] = None,
        status: str = None,
    ):
        # The information about headers.
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
                temp_model = main_models.GetGatewayRouteDetailResponseBodyDataHeaderOpHeaderOpItems()
                self.header_op_items.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetGatewayRouteDetailResponseBodyDataHeaderOpHeaderOpItems(DaraModel):
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
        # The type of the operation.
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

class GetGatewayRouteDetailResponseBodyDataHTTPRewrite(DaraModel):
    def __init__(
        self,
        host: str = None,
        path: str = None,
        path_type: str = None,
        pattern: str = None,
        status: str = None,
        substitution: str = None,
    ):
        # The hostname of the gateway.
        self.host = host
        # The path of the node.
        self.path = path
        # The rewrite type.
        self.path_type = path_type
        # The matching pattern.
        self.pattern = pattern
        # The status of the policy.
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

class GetGatewayRouteDetailResponseBodyDataFlowMirror(DaraModel):
    def __init__(
        self,
        percentage: int = None,
        port: int = None,
        status: str = None,
        target_service_id: int = None,
        target_service_name: str = None,
    ):
        # 流量复制比例（%），取值0-100。
        self.percentage = percentage
        # 目标服务端口。
        self.port = port
        # 开启状态，取值：
        # 
        # - on：开启
        # - off：关闭
        self.status = status
        # 目标服务ID。
        self.target_service_id = target_service_id
        # 目标服务名称。
        self.target_service_name = target_service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.port is not None:
            result['Port'] = self.port

        if self.status is not None:
            result['Status'] = self.status

        if self.target_service_id is not None:
            result['TargetServiceId'] = self.target_service_id

        if self.target_service_name is not None:
            result['TargetServiceName'] = self.target_service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetServiceId') is not None:
            self.target_service_id = m.get('TargetServiceId')

        if m.get('TargetServiceName') is not None:
            self.target_service_name = m.get('TargetServiceName')

        return self

class GetGatewayRouteDetailResponseBodyDataFallbackServices(DaraModel):
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
        # The protocol type.
        self.agreement_type = agreement_type
        # The name of the group to which the service belongs.
        self.group_name = group_name
        # The name.
        self.name = name
        # The namespace to which the service belongs.
        self.namespace = namespace
        # The weight in the form of a percentage value.
        self.percent = percent
        # The service ID.
        self.service_id = service_id
        # The service name.
        self.service_name = service_name
        # The port number of the service.
        self.service_port = service_port
        # The source type of the service.
        self.source_type = source_type
        # The service version.
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

class GetGatewayRouteDetailResponseBodyDataDirectResponse(DaraModel):
    def __init__(
        self,
        body: str = None,
        code: int = None,
    ):
        # The mock return value.
        self.body = body
        # The response code returned.
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

class GetGatewayRouteDetailResponseBodyDataCors(DaraModel):
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

