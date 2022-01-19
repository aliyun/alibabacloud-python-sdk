# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class GatewayOptionLogConfigDetails(TeaModel):
    def __init__(
        self,
        log_enabled: bool = None,
        log_store_name: str = None,
        project_name: str = None,
    ):
        # 是否开启日志投递
        self.log_enabled = log_enabled
        # 投递的目标logstore
        self.log_store_name = log_store_name
        # 投递的目标project
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_enabled is not None:
            result['LogEnabled'] = self.log_enabled
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogEnabled') is not None:
            self.log_enabled = m.get('LogEnabled')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GatewayOptionTraceDetails(TeaModel):
    def __init__(
        self,
        sample: int = None,
        trace_enabled: bool = None,
    ):
        # trace 采样率
        self.sample = sample
        # trace是否开启
        self.trace_enabled = trace_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.trace_enabled is not None:
            result['TraceEnabled'] = self.trace_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('TraceEnabled') is not None:
            self.trace_enabled = m.get('TraceEnabled')
        return self


class GatewayOption(TeaModel):
    def __init__(
        self,
        log_config_details: GatewayOptionLogConfigDetails = None,
        trace_details: GatewayOptionTraceDetails = None,
    ):
        # 日志配置详情
        self.log_config_details = log_config_details
        # xtrace config option
        self.trace_details = trace_details

    def validate(self):
        if self.log_config_details:
            self.log_config_details.validate()
        if self.trace_details:
            self.trace_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_config_details is not None:
            result['LogConfigDetails'] = self.log_config_details.to_map()
        if self.trace_details is not None:
            result['TraceDetails'] = self.trace_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogConfigDetails') is not None:
            temp_model = GatewayOptionLogConfigDetails()
            self.log_config_details = temp_model.from_map(m['LogConfigDetails'])
        if m.get('TraceDetails') is not None:
            temp_model = GatewayOptionTraceDetails()
            self.trace_details = temp_model.from_map(m['TraceDetails'])
        return self


class TrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie(TeaModel):
    def __init__(
        self,
        name: str = None,
        path: str = None,
        ttl: str = None,
    ):
        # cookie名
        self.name = name
        # cookie path
        self.path = path
        # cookie生命周期
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        if self.ttl is not None:
            result['TTL'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        return self


class TrafficPolicyLoadBalancerSettingsConsistentHashLBConfig(TeaModel):
    def __init__(
        self,
        consistent_hash_lbtype: str = None,
        http_cookie: TrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie = None,
        parameter_name: str = None,
    ):
        # HEADER, COOKIE, SOURCE_IP, QUERY_PARAMETER
        self.consistent_hash_lbtype = consistent_hash_lbtype
        # 使用cookie时配置
        self.http_cookie = http_cookie
        # 使用根据header和参数路由时生效
        self.parameter_name = parameter_name

    def validate(self):
        if self.http_cookie:
            self.http_cookie.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consistent_hash_lbtype is not None:
            result['ConsistentHashLBType'] = self.consistent_hash_lbtype
        if self.http_cookie is not None:
            result['HttpCookie'] = self.http_cookie.to_map()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsistentHashLBType') is not None:
            self.consistent_hash_lbtype = m.get('ConsistentHashLBType')
        if m.get('HttpCookie') is not None:
            temp_model = TrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie()
            self.http_cookie = temp_model.from_map(m['HttpCookie'])
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        return self


class TrafficPolicyLoadBalancerSettings(TeaModel):
    def __init__(
        self,
        consistent_hash_lbconfig: TrafficPolicyLoadBalancerSettingsConsistentHashLBConfig = None,
        loadbalancer_type: str = None,
    ):
        # 一致性hash相关配置
        self.consistent_hash_lbconfig = consistent_hash_lbconfig
        # 负载均衡类型，枚举类可为ROUND_ROBIN, LEAST_CONN,RANDOM, CONSISTENT_HASH
        self.loadbalancer_type = loadbalancer_type

    def validate(self):
        if self.consistent_hash_lbconfig:
            self.consistent_hash_lbconfig.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consistent_hash_lbconfig is not None:
            result['ConsistentHashLBConfig'] = self.consistent_hash_lbconfig.to_map()
        if self.loadbalancer_type is not None:
            result['LoadbalancerType'] = self.loadbalancer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsistentHashLBConfig') is not None:
            temp_model = TrafficPolicyLoadBalancerSettingsConsistentHashLBConfig()
            self.consistent_hash_lbconfig = temp_model.from_map(m['ConsistentHashLBConfig'])
        if m.get('LoadbalancerType') is not None:
            self.loadbalancer_type = m.get('LoadbalancerType')
        return self


class TrafficPolicyTlsSetting(TeaModel):
    def __init__(
        self,
        ca_cert_content: str = None,
        cert_id: str = None,
        sni: str = None,
        tls_mode: str = None,
    ):
        # ca证书内容
        self.ca_cert_content = ca_cert_content
        # 使用的证书id，仅当为mutual时需要填写
        self.cert_id = cert_id
        # 到后端服务些带
        self.sni = sni
        # tls模式。为枚举类，可为NONE, SIMPLE, MUITUAL
        self.tls_mode = tls_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_cert_content is not None:
            result['CaCertContent'] = self.ca_cert_content
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.sni is not None:
            result['Sni'] = self.sni
        if self.tls_mode is not None:
            result['TlsMode'] = self.tls_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCertContent') is not None:
            self.ca_cert_content = m.get('CaCertContent')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('Sni') is not None:
            self.sni = m.get('Sni')
        if m.get('TlsMode') is not None:
            self.tls_mode = m.get('TlsMode')
        return self


class TrafficPolicy(TeaModel):
    def __init__(
        self,
        load_balancer_settings: TrafficPolicyLoadBalancerSettings = None,
        tls_setting: TrafficPolicyTlsSetting = None,
    ):
        # 负载均衡相关配置
        self.load_balancer_settings = load_balancer_settings
        # tls相关配置
        self.tls_setting = tls_setting

    def validate(self):
        if self.load_balancer_settings:
            self.load_balancer_settings.validate()
        if self.tls_setting:
            self.tls_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_settings is not None:
            result['LoadBalancerSettings'] = self.load_balancer_settings.to_map()
        if self.tls_setting is not None:
            result['TlsSetting'] = self.tls_setting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerSettings') is not None:
            temp_model = TrafficPolicyLoadBalancerSettings()
            self.load_balancer_settings = temp_model.from_map(m['LoadBalancerSettings'])
        if m.get('TlsSetting') is not None:
            temp_model = TrafficPolicyTlsSetting()
            self.tls_setting = temp_model.from_map(m['TlsSetting'])
        return self


class GatewayService(TeaModel):
    def __init__(
        self,
        gateway_traffic_policy: TrafficPolicy = None,
        gateway_unique_id: str = None,
        group_name: str = None,
        id: int = None,
        meta_info: str = None,
        name: str = None,
        namespace: str = None,
        source_type: str = None,
    ):
        # 服务的策略
        self.gateway_traffic_policy = gateway_traffic_policy
        # 网关uniqueId
        self.gateway_unique_id = gateway_unique_id
        # 服务所属group
        self.group_name = group_name
        # 服务id
        self.id = id
        # 元信息
        self.meta_info = meta_info
        # 服务名
        self.name = name
        # 服务所属namesapce
        self.namespace = namespace
        # 服务来源
        self.source_type = source_type

    def validate(self):
        if self.gateway_traffic_policy:
            self.gateway_traffic_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_traffic_policy is not None:
            result['GatewayTrafficPolicy'] = self.gateway_traffic_policy.to_map()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayTrafficPolicy') is not None:
            temp_model = TrafficPolicy()
            self.gateway_traffic_policy = temp_model.from_map(m['GatewayTrafficPolicy'])
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class AddAuthResourceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        auth_id: int = None,
        domain_id: int = None,
        gateway_unique_id: str = None,
        path: str = None,
    ):
        self.accept_language = accept_language
        self.auth_id = auth_id
        self.domain_id = domain_id
        self.gateway_unique_id = gateway_unique_id
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.auth_id is not None:
            result['AuthId'] = self.auth_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class AddAuthResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddAuthResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAuthResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAuthResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddBlackWhiteListRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        content: str = None,
        gateway_unique_id: str = None,
        is_white: bool = None,
        resource_type: str = None,
        status: str = None,
        type: str = None,
    ):
        self.accept_language = accept_language
        self.content = content
        self.gateway_unique_id = gateway_unique_id
        self.is_white = is_white
        self.resource_type = resource_type
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.content is not None:
            result['Content'] = self.content
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.is_white is not None:
            result['IsWhite'] = self.is_white
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddBlackWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddBlackWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddBlackWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddBlackWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGatewayRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        enterprise_security_group: bool = None,
        internet_slb_spec: str = None,
        name: str = None,
        region: str = None,
        replica: int = None,
        slb_spec: str = None,
        spec: str = None,
        v_switch_id: str = None,
        v_switch_id_2: str = None,
        vpc: str = None,
    ):
        self.accept_language = accept_language
        # 是否企业安全组类型
        self.enterprise_security_group = enterprise_security_group
        # 外网SLB规格
        self.internet_slb_spec = internet_slb_spec
        # 网关名称
        self.name = name
        # 地域
        self.region = region
        # 节点数量
        self.replica = replica
        # 内网SLB规格
        self.slb_spec = slb_spec
        # 节点规格
        self.spec = spec
        # 主交换机ID
        self.v_switch_id = v_switch_id
        # 备交换机ID
        self.v_switch_id_2 = v_switch_id_2
        # 专有网络ID
        self.vpc = vpc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.enterprise_security_group is not None:
            result['EnterpriseSecurityGroup'] = self.enterprise_security_group
        if self.internet_slb_spec is not None:
            result['InternetSlbSpec'] = self.internet_slb_spec
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.replica is not None:
            result['Replica'] = self.replica
        if self.slb_spec is not None:
            result['SlbSpec'] = self.slb_spec
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_id_2 is not None:
            result['VSwitchId2'] = self.v_switch_id_2
        if self.vpc is not None:
            result['Vpc'] = self.vpc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('EnterpriseSecurityGroup') is not None:
            self.enterprise_security_group = m.get('EnterpriseSecurityGroup')
        if m.get('InternetSlbSpec') is not None:
            self.internet_slb_spec = m.get('InternetSlbSpec')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Replica') is not None:
            self.replica = m.get('Replica')
        if m.get('SlbSpec') is not None:
            self.slb_spec = m.get('SlbSpec')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchId2') is not None:
            self.v_switch_id_2 = m.get('VSwitchId2')
        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')
        return self


class AddGatewayResponseBodyData(TeaModel):
    def __init__(
        self,
        gateway_unique_id: str = None,
    ):
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class AddGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: AddGatewayResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = AddGatewayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddGatewayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGatewayDomainRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cert_identifier: str = None,
        gateway_unique_id: str = None,
        must_https: bool = None,
        name: str = None,
        protocol: str = None,
    ):
        self.accept_language = accept_language
        self.cert_identifier = cert_identifier
        self.gateway_unique_id = gateway_unique_id
        self.must_https = must_https
        self.name = name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.must_https is not None:
            result['MustHttps'] = self.must_https
        if self.name is not None:
            result['Name'] = self.name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class AddGatewayDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddGatewayDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddGatewayDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddGatewayDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGatewayServiceVersionRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        service_id: int = None,
        service_version: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.service_id = service_id
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class AddGatewayServiceVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddGatewayServiceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddGatewayServiceVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddGatewayServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGatewaySlbRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        slb_id: str = None,
        type: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.slb_id = slb_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddGatewaySlbResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddGatewaySlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddGatewaySlbResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddGatewaySlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMockRuleRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        consumer_app_ids: str = None,
        dubbo_mock_items: str = None,
        enable: bool = None,
        extra_json: str = None,
        mock_type: int = None,
        name: str = None,
        provider_app_id: str = None,
        provider_app_name: str = None,
        region: str = None,
        sc_mock_items: str = None,
        source: str = None,
    ):
        self.accept_language = accept_language
        self.consumer_app_ids = consumer_app_ids
        self.dubbo_mock_items = dubbo_mock_items
        self.enable = enable
        self.extra_json = extra_json
        self.mock_type = mock_type
        self.name = name
        self.provider_app_id = provider_app_id
        self.provider_app_name = provider_app_name
        self.region = region
        self.sc_mock_items = sc_mock_items
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.consumer_app_ids is not None:
            result['ConsumerAppIds'] = self.consumer_app_ids
        if self.dubbo_mock_items is not None:
            result['DubboMockItems'] = self.dubbo_mock_items
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.extra_json is not None:
            result['ExtraJson'] = self.extra_json
        if self.mock_type is not None:
            result['MockType'] = self.mock_type
        if self.name is not None:
            result['Name'] = self.name
        if self.provider_app_id is not None:
            result['ProviderAppId'] = self.provider_app_id
        if self.provider_app_name is not None:
            result['ProviderAppName'] = self.provider_app_name
        if self.region is not None:
            result['Region'] = self.region
        if self.sc_mock_items is not None:
            result['ScMockItems'] = self.sc_mock_items
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ConsumerAppIds') is not None:
            self.consumer_app_ids = m.get('ConsumerAppIds')
        if m.get('DubboMockItems') is not None:
            self.dubbo_mock_items = m.get('DubboMockItems')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ExtraJson') is not None:
            self.extra_json = m.get('ExtraJson')
        if m.get('MockType') is not None:
            self.mock_type = m.get('MockType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProviderAppId') is not None:
            self.provider_app_id = m.get('ProviderAppId')
        if m.get('ProviderAppName') is not None:
            self.provider_app_name = m.get('ProviderAppName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ScMockItems') is not None:
            self.sc_mock_items = m.get('ScMockItems')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class AddMockRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        consumer_app_id: str = None,
        consumer_app_name: str = None,
        enable: bool = None,
        extra_json: str = None,
        id: int = None,
        mock_type: int = None,
        name: str = None,
        namespace_id: str = None,
        provider_app_id: str = None,
        provider_app_name: str = None,
        region: str = None,
        sc_mock_item_json: str = None,
        source: str = None,
    ):
        self.account_id = account_id
        self.consumer_app_id = consumer_app_id
        self.consumer_app_name = consumer_app_name
        self.enable = enable
        self.extra_json = extra_json
        self.id = id
        self.mock_type = mock_type
        self.name = name
        self.namespace_id = namespace_id
        self.provider_app_id = provider_app_id
        self.provider_app_name = provider_app_name
        self.region = region
        self.sc_mock_item_json = sc_mock_item_json
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.consumer_app_id is not None:
            result['ConsumerAppId'] = self.consumer_app_id
        if self.consumer_app_name is not None:
            result['ConsumerAppName'] = self.consumer_app_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.extra_json is not None:
            result['ExtraJson'] = self.extra_json
        if self.id is not None:
            result['Id'] = self.id
        if self.mock_type is not None:
            result['MockType'] = self.mock_type
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.provider_app_id is not None:
            result['ProviderAppId'] = self.provider_app_id
        if self.provider_app_name is not None:
            result['ProviderAppName'] = self.provider_app_name
        if self.region is not None:
            result['Region'] = self.region
        if self.sc_mock_item_json is not None:
            result['ScMockItemJson'] = self.sc_mock_item_json
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ConsumerAppId') is not None:
            self.consumer_app_id = m.get('ConsumerAppId')
        if m.get('ConsumerAppName') is not None:
            self.consumer_app_name = m.get('ConsumerAppName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ExtraJson') is not None:
            self.extra_json = m.get('ExtraJson')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MockType') is not None:
            self.mock_type = m.get('MockType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ProviderAppId') is not None:
            self.provider_app_id = m.get('ProviderAppId')
        if m.get('ProviderAppName') is not None:
            self.provider_app_name = m.get('ProviderAppName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ScMockItemJson') is not None:
            self.sc_mock_item_json = m.get('ScMockItemJson')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class AddMockRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: AddMockRuleResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = AddMockRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddMockRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddMockRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddMockRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSSLCertRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cert_identifier: str = None,
        domain_id: int = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.cert_identifier = cert_identifier
        self.domain_id = domain_id
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class AddSSLCertResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddSSLCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSSLCertResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddSSLCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddServiceSourceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        address: str = None,
        gateway_unique_id: str = None,
        name: str = None,
        source: str = None,
        type: str = None,
    ):
        self.accept_language = accept_language
        self.address = address
        self.gateway_unique_id = gateway_unique_id
        self.name = name
        self.source = source
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.address is not None:
            result['Address'] = self.address
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddServiceSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddServiceSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddServiceSourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddServiceSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneNacosConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        ids: str = None,
        instance_id: str = None,
        origin_namespace_id: str = None,
        policy: str = None,
        target_namespace_id: str = None,
    ):
        self.accept_language = accept_language
        self.ids = ids
        self.instance_id = instance_id
        self.origin_namespace_id = origin_namespace_id
        self.policy = policy
        self.target_namespace_id = target_namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.origin_namespace_id is not None:
            result['OriginNamespaceId'] = self.origin_namespace_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.target_namespace_id is not None:
            result['TargetNamespaceId'] = self.target_namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OriginNamespaceId') is not None:
            self.origin_namespace_id = m.get('OriginNamespaceId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('TargetNamespaceId') is not None:
            self.target_namespace_id = m.get('TargetNamespaceId')
        return self


class CloneNacosConfigResponseBodyDataFailData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
    ):
        self.data_id = data_id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class CloneNacosConfigResponseBodyDataSkipData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
    ):
        self.data_id = data_id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class CloneNacosConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_data: List[CloneNacosConfigResponseBodyDataFailData] = None,
        skip_count: int = None,
        skip_data: List[CloneNacosConfigResponseBodyDataSkipData] = None,
        succ_count: int = None,
    ):
        self.fail_data = fail_data
        self.skip_count = skip_count
        self.skip_data = skip_data
        self.succ_count = succ_count

    def validate(self):
        if self.fail_data:
            for k in self.fail_data:
                if k:
                    k.validate()
        if self.skip_data:
            for k in self.skip_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailData'] = []
        if self.fail_data is not None:
            for k in self.fail_data:
                result['FailData'].append(k.to_map() if k else None)
        if self.skip_count is not None:
            result['SkipCount'] = self.skip_count
        result['SkipData'] = []
        if self.skip_data is not None:
            for k in self.skip_data:
                result['SkipData'].append(k.to_map() if k else None)
        if self.succ_count is not None:
            result['SuccCount'] = self.succ_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail_data = []
        if m.get('FailData') is not None:
            for k in m.get('FailData'):
                temp_model = CloneNacosConfigResponseBodyDataFailData()
                self.fail_data.append(temp_model.from_map(k))
        if m.get('SkipCount') is not None:
            self.skip_count = m.get('SkipCount')
        self.skip_data = []
        if m.get('SkipData') is not None:
            for k in m.get('SkipData'):
                temp_model = CloneNacosConfigResponseBodyDataSkipData()
                self.skip_data.append(temp_model.from_map(k))
        if m.get('SuccCount') is not None:
            self.succ_count = m.get('SuccCount')
        return self


class CloneNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CloneNacosConfigResponseBodyData = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            temp_model = CloneNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloneNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloneNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloneNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlarmRuleRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        aggregates: str = None,
        alarm_alias_name: str = None,
        alarm_item: str = None,
        alert_way: Dict[str, Any] = None,
        contact_group_ids: Dict[str, Any] = None,
        instance_id: str = None,
        nvalue: int = None,
        operator: str = None,
        value: float = None,
    ):
        self.accept_language = accept_language
        self.aggregates = aggregates
        self.alarm_alias_name = alarm_alias_name
        self.alarm_item = alarm_item
        self.alert_way = alert_way
        self.contact_group_ids = contact_group_ids
        self.instance_id = instance_id
        self.nvalue = nvalue
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.alarm_alias_name is not None:
            result['AlarmAliasName'] = self.alarm_alias_name
        if self.alarm_item is not None:
            result['AlarmItem'] = self.alarm_item
        if self.alert_way is not None:
            result['AlertWay'] = self.alert_way
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('AlarmAliasName') is not None:
            self.alarm_alias_name = m.get('AlarmAliasName')
        if m.get('AlarmItem') is not None:
            self.alarm_item = m.get('AlarmItem')
        if m.get('AlertWay') is not None:
            self.alert_way = m.get('AlertWay')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAlarmRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        aggregates: str = None,
        alarm_alias_name: str = None,
        alarm_item: str = None,
        alert_way_shrink: str = None,
        contact_group_ids_shrink: str = None,
        instance_id: str = None,
        nvalue: int = None,
        operator: str = None,
        value: float = None,
    ):
        self.accept_language = accept_language
        self.aggregates = aggregates
        self.alarm_alias_name = alarm_alias_name
        self.alarm_item = alarm_item
        self.alert_way_shrink = alert_way_shrink
        self.contact_group_ids_shrink = contact_group_ids_shrink
        self.instance_id = instance_id
        self.nvalue = nvalue
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.alarm_alias_name is not None:
            result['AlarmAliasName'] = self.alarm_alias_name
        if self.alarm_item is not None:
            result['AlarmItem'] = self.alarm_item
        if self.alert_way_shrink is not None:
            result['AlertWay'] = self.alert_way_shrink
        if self.contact_group_ids_shrink is not None:
            result['ContactGroupIds'] = self.contact_group_ids_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('AlarmAliasName') is not None:
            self.alarm_alias_name = m.get('AlarmAliasName')
        if m.get('AlarmItem') is not None:
            self.alarm_item = m.get('AlarmItem')
        if m.get('AlertWay') is not None:
            self.alert_way_shrink = m.get('AlertWay')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids_shrink = m.get('ContactGroupIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAlarmRuleResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAlarmRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        extra_info: str = None,
        language: str = None,
        region: str = None,
        source: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.extra_info = extra_info
        self.language = language
        self.region = region
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.language is not None:
            result['Language'] = self.language
        if self.region is not None:
            result['Region'] = self.region
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        create_time: int = None,
        extra_info: str = None,
        language: str = None,
        license_key: str = None,
        region_id: str = None,
        source: str = None,
        status: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.create_time = create_time
        self.extra_info = extra_info
        self.language = language
        self.license_key = license_key
        self.region_id = region_id
        self.source = source
        self.status = status
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.language is not None:
            result['Language'] = self.language
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateApplicationResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_specification: str = None,
        cluster_type: str = None,
        cluster_version: str = None,
        connection_type: str = None,
        disk_capacity: int = None,
        disk_type: str = None,
        instance_count: int = None,
        mse_version: str = None,
        net_type: str = None,
        private_slb_specification: str = None,
        pub_network_flow: str = None,
        pub_slb_specification: str = None,
        region: str = None,
        request_pars: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_specification = cluster_specification
        self.cluster_type = cluster_type
        self.cluster_version = cluster_version
        self.connection_type = connection_type
        self.disk_capacity = disk_capacity
        self.disk_type = disk_type
        self.instance_count = instance_count
        # 用于区分基础/专业版本
        self.mse_version = mse_version
        self.net_type = net_type
        self.private_slb_specification = private_slb_specification
        self.pub_network_flow = pub_network_flow
        self.pub_slb_specification = pub_slb_specification
        self.region = region
        self.request_pars = request_pars
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.private_slb_specification is not None:
            result['PrivateSlbSpecification'] = self.private_slb_specification
        if self.pub_network_flow is not None:
            result['PubNetworkFlow'] = self.pub_network_flow
        if self.pub_slb_specification is not None:
            result['PubSlbSpecification'] = self.pub_slb_specification
        if self.region is not None:
            result['Region'] = self.region
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('PrivateSlbSpecification') is not None:
            self.private_slb_specification = m.get('PrivateSlbSpecification')
        if m.get('PubNetworkFlow') is not None:
            self.pub_network_flow = m.get('PubNetworkFlow')
        if m.get('PubSlbSpecification') is not None:
            self.pub_slb_specification = m.get('PubSlbSpecification')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        instance_id: str = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.instance_id = instance_id
        self.message = message
        self.order_id = order_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEngineNamespaceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        desc: str = None,
        instance_id: str = None,
        name: str = None,
        service_count: int = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.desc = desc
        self.instance_id = instance_id
        self.name = name
        self.service_count = service_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        return self


class CreateEngineNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        config_count: int = None,
        namespace: str = None,
        namespace_desc: str = None,
        namespace_show_name: str = None,
        quota: int = None,
        service_count: int = None,
        type: int = None,
    ):
        self.config_count = config_count
        self.namespace = namespace
        self.namespace_desc = namespace_desc
        self.namespace_show_name = namespace_show_name
        self.quota = quota
        self.service_count = service_count
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateEngineNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data: CreateEngineNamespaceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.cluster_id = cluster_id
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Data') is not None:
            temp_model = CreateEngineNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEngineNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEngineNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNacosConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        beta_ips: str = None,
        content: str = None,
        data_id: str = None,
        desc: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        tags: str = None,
        type: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.beta_ips = beta_ips
        self.content = content
        self.data_id = data_id
        self.desc = desc
        self.group = group
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.tags = tags
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNacosInstanceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_name: str = None,
        enabled: bool = None,
        ephemeral: bool = None,
        group_name: str = None,
        instance_id: str = None,
        ip: str = None,
        metadata: str = None,
        namespace_id: str = None,
        port: int = None,
        service_name: str = None,
        weight: str = None,
    ):
        self.accept_language = accept_language
        # Nacos集群名
        self.cluster_name = cluster_name
        # 服务禁用标志
        self.enabled = enabled
        # 临时节点标志
        self.ephemeral = ephemeral
        # 分组名
        self.group_name = group_name
        # 实例id
        self.instance_id = instance_id
        # Nacos实例ip
        self.ip = ip
        # 节点元数据
        self.metadata = metadata
        # 命名空间id
        self.namespace_id = namespace_id
        # Nacos实例端口
        self.port = port
        # 服务名
        self.service_name = service_name
        # 权重
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.port is not None:
            result['Port'] = self.port
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateNacosInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 响应码
        self.code = code
        # 修改结果
        self.data = data
        # http状态码
        self.http_status_code = http_status_code
        # 响应信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 成功标志
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNacosInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNacosInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNacosInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNacosServiceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        ephemeral: bool = None,
        group_name: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        protect_threshold: str = None,
        service_name: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.ephemeral = ephemeral
        self.group_name = group_name
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.protect_threshold = protect_threshold
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.protect_threshold is not None:
            result['ProtectThreshold'] = self.protect_threshold
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ProtectThreshold') is not None:
            self.protect_threshold = m.get('ProtectThreshold')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateNacosServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNacosServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNacosServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNacosServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateZnodeRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        data: str = None,
        path: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.data = data
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateZnodeResponseBodyData(TeaModel):
    def __init__(
        self,
        data: str = None,
        dir: bool = None,
        name: str = None,
        path: str = None,
    ):
        self.data = data
        self.dir = dir
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateZnodeResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateZnodeResponseBodyData = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateZnodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateZnodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateZnodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlarmRuleRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        alarm_rule_id: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.alarm_rule_id = alarm_rule_id
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.alarm_rule_id is not None:
            result['AlarmRuleId'] = self.alarm_rule_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AlarmRuleId') is not None:
            self.alarm_rule_id = m.get('AlarmRuleId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class DeleteAlarmRuleResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAlarmRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthResourceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        id: int = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteAuthResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        auth_id: int = None,
        domain_id: int = None,
        domain_name: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_white: bool = None,
        path: str = None,
    ):
        self.auth_id = auth_id
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_white = is_white
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_id is not None:
            result['AuthId'] = self.auth_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
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
        if self.is_white is not None:
            result['IsWhite'] = self.is_white
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DeleteAuthResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DeleteAuthResourceResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DeleteAuthResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAuthResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAuthResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAuthResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
    ):
        self.accept_language = accept_language
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEngineNamespaceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        id: str = None,
        instance_id: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.id = id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteEngineNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEngineNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEngineNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        delete_slb: bool = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.delete_slb = delete_slb
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.delete_slb is not None:
            result['DeleteSlb'] = self.delete_slb
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DeleteSlb') is not None:
            self.delete_slb = m.get('DeleteSlb')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class DeleteGatewayResponseBodyData(TeaModel):
    def __init__(
        self,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        primary_user: str = None,
        region: str = None,
        replica: int = None,
        security_group: str = None,
        spec: str = None,
        status: int = None,
        vpc: str = None,
        vswitch: str = None,
    ):
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.primary_user = primary_user
        self.region = region
        self.replica = replica
        self.security_group = security_group
        self.spec = spec
        self.status = status
        self.vpc = vpc
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user
        if self.region is not None:
            result['Region'] = self.region
        if self.replica is not None:
            result['Replica'] = self.replica
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc is not None:
            result['Vpc'] = self.vpc
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Replica') is not None:
            self.replica = m.get('Replica')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class DeleteGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DeleteGatewayResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DeleteGatewayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGatewayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayDomainRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteGatewayDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        cert_identifier: int = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        must_https: bool = None,
        name: str = None,
        protocol: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.must_https = must_https
        self.name = name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
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
        if self.must_https is not None:
            result['MustHttps'] = self.must_https
        if self.name is not None:
            result['Name'] = self.name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
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
        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DeleteGatewayDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DeleteGatewayDomainResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DeleteGatewayDomainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGatewayDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGatewayDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteGatewayDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayServiceVersionRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        service_id: int = None,
        service_version: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.service_id = service_id
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class DeleteGatewayServiceVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGatewayServiceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGatewayServiceVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteGatewayServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewaySlbRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        delete_slb: bool = None,
        gateway_unique_id: str = None,
        id: str = None,
    ):
        self.accept_language = accept_language
        self.delete_slb = delete_slb
        self.gateway_unique_id = gateway_unique_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.delete_slb is not None:
            result['DeleteSlb'] = self.delete_slb
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DeleteSlb') is not None:
            self.delete_slb = m.get('DeleteSlb')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteGatewaySlbResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGatewaySlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGatewaySlbResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteGatewaySlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        beta: bool = None,
        data_id: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
    ):
        self.accept_language = accept_language
        self.beta = beta
        self.data_id = data_id
        self.group = group
        self.instance_id = instance_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.beta is not None:
            result['Beta'] = self.beta
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Beta') is not None:
            self.beta = m.get('Beta')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosConfigsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        ids: str = None,
        instance_id: str = None,
        namespace_id: str = None,
    ):
        self.accept_language = accept_language
        self.ids = ids
        self.instance_id = instance_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNacosConfigsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNacosConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNacosConfigsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNacosConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosServiceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        group_name: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        service_name: str = None,
    ):
        self.accept_language = accept_language
        self.group_name = group_name
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DeleteNacosServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 响应码
        self.code = code
        # 删除服务的结果
        self.data = data
        # http状态码
        self.http_status_code = http_status_code
        # 响应信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 成功标志
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNacosServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNacosServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNacosServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceSourceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        source_id: int = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class DeleteServiceSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteServiceSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServiceSourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteServiceSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteZnodeRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        path: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.path = path
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class DeleteZnodeResponseBodyData(TeaModel):
    def __init__(
        self,
        data: str = None,
        dir: bool = None,
        name: str = None,
        path: str = None,
    ):
        self.data = data
        self.dir = dir
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DeleteZnodeResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteZnodeResponseBodyData = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteZnodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteZnodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteZnodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportNacosConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        data_id: str = None,
        group: str = None,
        ids: str = None,
        instance_id: str = None,
        namespace_id: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.data_id = data_id
        self.group = group
        self.ids = ids
        self.instance_id = instance_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ExportNacosConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ExportNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ExportNacosConfigResponseBodyData = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            temp_model = ExportNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBlackWhiteListRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        resource_type: str = None,
        type: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.resource_type = resource_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetBlackWhiteListResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_white: bool = None,
        resource_id: int = None,
        resource_type: str = None,
        status: str = None,
        type: str = None,
    ):
        self.content = content
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_white = is_white
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
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
        if self.is_white is not None:
            result['IsWhite'] = self.is_white
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
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
        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetBlackWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetBlackWhiteListResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetBlackWhiteListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetBlackWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBlackWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetBlackWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEngineNamepaceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        id: str = None,
        instance_id: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.id = id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetEngineNamepaceResponseBody(TeaModel):
    def __init__(
        self,
        config_count: str = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        namespace: str = None,
        namespace_desc: str = None,
        namespace_show_name: str = None,
        quota: str = None,
        request_id: str = None,
        success: bool = None,
        type: str = None,
    ):
        self.config_count = config_count
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.namespace = namespace
        self.namespace_desc = namespace_desc
        self.namespace_show_name = namespace_show_name
        self.quota = quota
        self.request_id = request_id
        self.success = success
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetEngineNamepaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEngineNamepaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEngineNamepaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class GetGatewayResponseBodyDataLogConfigDetails(TeaModel):
    def __init__(
        self,
        log_enabled: bool = None,
        log_store_name: str = None,
        project_name: str = None,
    ):
        self.log_enabled = log_enabled
        self.log_store_name = log_store_name
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_enabled is not None:
            result['LogEnabled'] = self.log_enabled
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogEnabled') is not None:
            self.log_enabled = m.get('LogEnabled')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetGatewayResponseBodyDataXtraceDetails(TeaModel):
    def __init__(
        self,
        sample: int = None,
        trace_on: bool = None,
    ):
        self.sample = sample
        self.trace_on = trace_on

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.trace_on is not None:
            result['TraceOn'] = self.trace_on
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('TraceOn') is not None:
            self.trace_on = m.get('TraceOn')
        return self


class GetGatewayResponseBodyData(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        end_date: str = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        log_config_details: GetGatewayResponseBodyDataLogConfigDetails = None,
        name: str = None,
        primary_user: str = None,
        region: str = None,
        replica: int = None,
        security_group: str = None,
        spec: str = None,
        status: int = None,
        vpc: str = None,
        vswitch: str = None,
        vswitch_2: str = None,
        xtrace_details: GetGatewayResponseBodyDataXtraceDetails = None,
    ):
        self.charge_type = charge_type
        self.end_date = end_date
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.log_config_details = log_config_details
        self.name = name
        self.primary_user = primary_user
        self.region = region
        self.replica = replica
        self.security_group = security_group
        self.spec = spec
        self.status = status
        self.vpc = vpc
        self.vswitch = vswitch
        self.vswitch_2 = vswitch_2
        self.xtrace_details = xtrace_details

    def validate(self):
        if self.log_config_details:
            self.log_config_details.validate()
        if self.xtrace_details:
            self.xtrace_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_config_details is not None:
            result['LogConfigDetails'] = self.log_config_details.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user
        if self.region is not None:
            result['Region'] = self.region
        if self.replica is not None:
            result['Replica'] = self.replica
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc is not None:
            result['Vpc'] = self.vpc
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        if self.vswitch_2 is not None:
            result['Vswitch2'] = self.vswitch_2
        if self.xtrace_details is not None:
            result['XtraceDetails'] = self.xtrace_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogConfigDetails') is not None:
            temp_model = GetGatewayResponseBodyDataLogConfigDetails()
            self.log_config_details = temp_model.from_map(m['LogConfigDetails'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Replica') is not None:
            self.replica = m.get('Replica')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        if m.get('Vswitch2') is not None:
            self.vswitch_2 = m.get('Vswitch2')
        if m.get('XtraceDetails') is not None:
            temp_model = GetGatewayResponseBodyDataXtraceDetails()
            self.xtrace_details = temp_model.from_map(m['XtraceDetails'])
        return self


class GetGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetGatewayResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetGatewayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGatewayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayDomainDetailRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetGatewayDomainDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        after_date: int = None,
        algorithm: str = None,
        before_date: int = None,
        cert_identifier: int = None,
        cert_name: str = None,
        common_name: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_after: str = None,
        gmt_before: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        issuer: str = None,
        must_https: bool = None,
        name: str = None,
        protocol: str = None,
        sans: str = None,
    ):
        self.after_date = after_date
        self.algorithm = algorithm
        self.before_date = before_date
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.common_name = common_name
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.gmt_after = gmt_after
        self.gmt_before = gmt_before
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.issuer = issuer
        self.must_https = must_https
        self.name = name
        self.protocol = protocol
        self.sans = sans

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_after is not None:
            result['GmtAfter'] = self.gmt_after
        if self.gmt_before is not None:
            result['GmtBefore'] = self.gmt_before
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.must_https is not None:
            result['MustHttps'] = self.must_https
        if self.name is not None:
            result['Name'] = self.name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.sans is not None:
            result['Sans'] = self.sans
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtAfter') is not None:
            self.gmt_after = m.get('GmtAfter')
        if m.get('GmtBefore') is not None:
            self.gmt_before = m.get('GmtBefore')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        return self


class GetGatewayDomainDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetGatewayDomainDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetGatewayDomainDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGatewayDomainDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGatewayDomainDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGatewayDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayOptionRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class GetGatewayOptionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GatewayOption = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GatewayOption()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGatewayOptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGatewayOptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGatewayOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayServiceDetailRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        service_id: int = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class GetGatewayServiceDetailResponseBodyDataLabelDetails(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersionLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersion(TeaModel):
    def __init__(
        self,
        labels: List[GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersionLabels] = None,
        name: str = None,
    ):
        self.labels = labels
        self.name = name

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersionLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetGatewayServiceDetailResponseBodyDataVersionDetails(TeaModel):
    def __init__(
        self,
        endpoint_num: int = None,
        endpoint_num_percent: str = None,
        service_version: GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersion = None,
    ):
        self.endpoint_num = endpoint_num
        self.endpoint_num_percent = endpoint_num_percent
        self.service_version = service_version

    def validate(self):
        if self.service_version:
            self.service_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_num is not None:
            result['EndpointNum'] = self.endpoint_num
        if self.endpoint_num_percent is not None:
            result['EndpointNumPercent'] = self.endpoint_num_percent
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointNum') is not None:
            self.endpoint_num = m.get('EndpointNum')
        if m.get('EndpointNumPercent') is not None:
            self.endpoint_num_percent = m.get('EndpointNumPercent')
        if m.get('ServiceVersion') is not None:
            temp_model = GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersion()
            self.service_version = temp_model.from_map(m['ServiceVersion'])
        return self


class GetGatewayServiceDetailResponseBodyDataVersions(TeaModel):
    def __init__(
        self,
        label: str = None,
        type: str = None,
        value: str = None,
    ):
        self.label = label
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetGatewayServiceDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        gateway_id: int = None,
        gateway_traffic_policy: TrafficPolicy = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_name: str = None,
        id: int = None,
        ips: List[str] = None,
        label_details: List[GetGatewayServiceDetailResponseBodyDataLabelDetails] = None,
        meta_info: str = None,
        name: str = None,
        namespace: str = None,
        service_name_in_registry: str = None,
        source_id: int = None,
        source_type: str = None,
        version_details: List[GetGatewayServiceDetailResponseBodyDataVersionDetails] = None,
        versions: List[GetGatewayServiceDetailResponseBodyDataVersions] = None,
    ):
        self.gateway_id = gateway_id
        self.gateway_traffic_policy = gateway_traffic_policy
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_name = group_name
        self.id = id
        self.ips = ips
        self.label_details = label_details
        self.meta_info = meta_info
        self.name = name
        self.namespace = namespace
        self.service_name_in_registry = service_name_in_registry
        self.source_id = source_id
        self.source_type = source_type
        self.version_details = version_details
        self.versions = versions

    def validate(self):
        if self.gateway_traffic_policy:
            self.gateway_traffic_policy.validate()
        if self.label_details:
            for k in self.label_details:
                if k:
                    k.validate()
        if self.version_details:
            for k in self.version_details:
                if k:
                    k.validate()
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_traffic_policy is not None:
            result['GatewayTrafficPolicy'] = self.gateway_traffic_policy.to_map()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.ips is not None:
            result['Ips'] = self.ips
        result['LabelDetails'] = []
        if self.label_details is not None:
            for k in self.label_details:
                result['LabelDetails'].append(k.to_map() if k else None)
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_name_in_registry is not None:
            result['ServiceNameInRegistry'] = self.service_name_in_registry
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['VersionDetails'] = []
        if self.version_details is not None:
            for k in self.version_details:
                result['VersionDetails'].append(k.to_map() if k else None)
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayTrafficPolicy') is not None:
            temp_model = TrafficPolicy()
            self.gateway_traffic_policy = temp_model.from_map(m['GatewayTrafficPolicy'])
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        self.label_details = []
        if m.get('LabelDetails') is not None:
            for k in m.get('LabelDetails'):
                temp_model = GetGatewayServiceDetailResponseBodyDataLabelDetails()
                self.label_details.append(temp_model.from_map(k))
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('ServiceNameInRegistry')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.version_details = []
        if m.get('VersionDetails') is not None:
            for k in m.get('VersionDetails'):
                temp_model = GetGatewayServiceDetailResponseBodyDataVersionDetails()
                self.version_details.append(temp_model.from_map(k))
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = GetGatewayServiceDetailResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class GetGatewayServiceDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetGatewayServiceDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetGatewayServiceDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGatewayServiceDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGatewayServiceDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGatewayServiceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGovernanceKubernetesClusterRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetGovernanceKubernetesClusterResponseBodyDataNamespaces(TeaModel):
    def __init__(
        self,
        name: str = None,
        tags: str = None,
    ):
        self.name = name
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GetGovernanceKubernetesClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        k_8s_version: str = None,
        namespace_infos: str = None,
        namespaces: List[GetGovernanceKubernetesClusterResponseBodyDataNamespaces] = None,
        pilot_start_time: str = None,
        region: str = None,
        update_time: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.k_8s_version = k_8s_version
        self.namespace_infos = namespace_infos
        self.namespaces = namespaces
        self.pilot_start_time = pilot_start_time
        self.region = region
        self.update_time = update_time

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.k_8s_version is not None:
            result['K8sVersion'] = self.k_8s_version
        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.pilot_start_time is not None:
            result['PilotStartTime'] = self.pilot_start_time
        if self.region is not None:
            result['Region'] = self.region
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('K8sVersion') is not None:
            self.k_8s_version = m.get('K8sVersion')
        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = GetGovernanceKubernetesClusterResponseBodyDataNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('PilotStartTime') is not None:
            self.pilot_start_time = m.get('PilotStartTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetGovernanceKubernetesClusterResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetGovernanceKubernetesClusterResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetGovernanceKubernetesClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGovernanceKubernetesClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGovernanceKubernetesClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGovernanceKubernetesClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGovernanceKubernetesClusterListRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetGovernanceKubernetesClusterListResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        k_8s_version: str = None,
        namespace_infos: str = None,
        pilot_start_time: str = None,
        region: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.k_8s_version = k_8s_version
        self.namespace_infos = namespace_infos
        self.pilot_start_time = pilot_start_time
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.k_8s_version is not None:
            result['K8sVersion'] = self.k_8s_version
        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos
        if self.pilot_start_time is not None:
            result['PilotStartTime'] = self.pilot_start_time
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('K8sVersion') is not None:
            self.k_8s_version = m.get('K8sVersion')
        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')
        if m.get('PilotStartTime') is not None:
            self.pilot_start_time = m.get('PilotStartTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetGovernanceKubernetesClusterListResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[GetGovernanceKubernetesClusterListResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.result = result
        self.total_size = total_size

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
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
            for k in m.get('Result'):
                temp_model = GetGovernanceKubernetesClusterListResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class GetGovernanceKubernetesClusterListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetGovernanceKubernetesClusterListResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetGovernanceKubernetesClusterListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGovernanceKubernetesClusterListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGovernanceKubernetesClusterListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGovernanceKubernetesClusterListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        version_code: str = None,
    ):
        self.accept_language = accept_language
        # 集群版本
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        return self


class GetImageResponseBodyData(TeaModel):
    def __init__(
        self,
        current_version_full_show_name: str = None,
        max_version_changelog_url: str = None,
        max_version_code: str = None,
        max_version_full_show_name: str = None,
    ):
        # 当前集群镜像版本的4位全名
        self.current_version_full_show_name = current_version_full_show_name
        # 可升级的最大版本变更日志url
        self.max_version_changelog_url = max_version_changelog_url
        # 可升级的增量版本Code
        self.max_version_code = max_version_code
        # 可升级的增量版本全名
        self.max_version_full_show_name = max_version_full_show_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_version_full_show_name is not None:
            result['CurrentVersionFullShowName'] = self.current_version_full_show_name
        if self.max_version_changelog_url is not None:
            result['MaxVersionChangelogUrl'] = self.max_version_changelog_url
        if self.max_version_code is not None:
            result['MaxVersionCode'] = self.max_version_code
        if self.max_version_full_show_name is not None:
            result['MaxVersionFullShowName'] = self.max_version_full_show_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentVersionFullShowName') is not None:
            self.current_version_full_show_name = m.get('CurrentVersionFullShowName')
        if m.get('MaxVersionChangelogUrl') is not None:
            self.max_version_changelog_url = m.get('MaxVersionChangelogUrl')
        if m.get('MaxVersionCode') is not None:
            self.max_version_code = m.get('MaxVersionCode')
        if m.get('MaxVersionFullShowName') is not None:
            self.max_version_full_show_name = m.get('MaxVersionFullShowName')
        return self


class GetImageResponseBody(TeaModel):
    def __init__(
        self,
        data: GetImageResponseBodyData = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImportFileUrlRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        content_type: str = None,
        instance_id: str = None,
        namespace_id: str = None,
    ):
        self.accept_language = accept_language
        self.content_type = content_type
        self.instance_id = instance_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class GetImportFileUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetImportFileUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetImportFileUrlResponseBodyData = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            temp_model = GetImportFileUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetImportFileUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImportFileUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImportFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKubernetesSourceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class GetKubernetesSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        name: str = None,
    ):
        self.cluster = cluster
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cluster') is not None:
            self.cluster = m.get('Cluster')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetKubernetesSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetKubernetesSourceResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = GetKubernetesSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetKubernetesSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetKubernetesSourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetKubernetesSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMseFeatureSwitchRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class GetMseFeatureSwitchResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMseFeatureSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMseFeatureSwitchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMseFeatureSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMseSourceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class GetMseSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        address: str = None,
        cluster_id: str = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.address = address
        self.cluster_id = cluster_id
        self.instance_id = instance_id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetMseSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetMseSourceResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = GetMseSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMseSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMseSourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMseSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNacosConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        beta: bool = None,
        data_id: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
    ):
        self.accept_language = accept_language
        self.beta = beta
        self.data_id = data_id
        self.group = group
        self.instance_id = instance_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.beta is not None:
            result['Beta'] = self.beta
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Beta') is not None:
            self.beta = m.get('Beta')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class GetNacosConfigResponseBodyConfiguration(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        beta_ips: str = None,
        content: str = None,
        data_id: str = None,
        desc: str = None,
        encrypted_data_key: str = None,
        group: str = None,
        md_5: str = None,
        tags: str = None,
        type: str = None,
    ):
        self.app_name = app_name
        self.beta_ips = beta_ips
        self.content = content
        self.data_id = data_id
        self.desc = desc
        self.encrypted_data_key = encrypted_data_key
        self.group = group
        self.md_5 = md_5
        self.tags = tags
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.encrypted_data_key is not None:
            result['EncryptedDataKey'] = self.encrypted_data_key
        if self.group is not None:
            result['Group'] = self.group
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('EncryptedDataKey') is not None:
            self.encrypted_data_key = m.get('EncryptedDataKey')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        configuration: GetNacosConfigResponseBodyConfiguration = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.configuration = configuration
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configuration') is not None:
            temp_model = GetNacosConfigResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNacosHistoryConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        data_id: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        nid: str = None,
    ):
        self.accept_language = accept_language
        self.data_id = data_id
        self.group = group
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.nid = nid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nid is not None:
            result['Nid'] = self.nid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Nid') is not None:
            self.nid = m.get('Nid')
        return self


class GetNacosHistoryConfigResponseBodyConfiguration(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        content: str = None,
        data_id: str = None,
        encrypted_data_key: str = None,
        group: str = None,
        md_5: str = None,
        op_type: str = None,
    ):
        self.app_name = app_name
        self.content = content
        self.data_id = data_id
        self.encrypted_data_key = encrypted_data_key
        self.group = group
        self.md_5 = md_5
        self.op_type = op_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.encrypted_data_key is not None:
            result['EncryptedDataKey'] = self.encrypted_data_key
        if self.group is not None:
            result['Group'] = self.group
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.op_type is not None:
            result['OpType'] = self.op_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('EncryptedDataKey') is not None:
            self.encrypted_data_key = m.get('EncryptedDataKey')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        return self


class GetNacosHistoryConfigResponseBody(TeaModel):
    def __init__(
        self,
        configuration: GetNacosHistoryConfigResponseBodyConfiguration = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.configuration = configuration
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configuration') is not None:
            temp_model = GetNacosHistoryConfigResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNacosHistoryConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNacosHistoryConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetNacosHistoryConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOverviewRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        period: int = None,
        region: str = None,
    ):
        self.accept_language = accept_language
        self.period = period
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.period is not None:
            result['Period'] = self.period
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetOverviewResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOverviewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportNacosConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        file_url: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        policy: str = None,
    ):
        self.accept_language = accept_language
        self.file_url = file_url
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class ImportNacosConfigResponseBodyDataFailData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
    ):
        self.data_id = data_id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ImportNacosConfigResponseBodyDataSkipData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
    ):
        self.data_id = data_id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ImportNacosConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_data: List[ImportNacosConfigResponseBodyDataFailData] = None,
        skip_count: int = None,
        skip_data: List[ImportNacosConfigResponseBodyDataSkipData] = None,
        succ_count: int = None,
    ):
        self.fail_data = fail_data
        self.skip_count = skip_count
        self.skip_data = skip_data
        self.succ_count = succ_count

    def validate(self):
        if self.fail_data:
            for k in self.fail_data:
                if k:
                    k.validate()
        if self.skip_data:
            for k in self.skip_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailData'] = []
        if self.fail_data is not None:
            for k in self.fail_data:
                result['FailData'].append(k.to_map() if k else None)
        if self.skip_count is not None:
            result['SkipCount'] = self.skip_count
        result['SkipData'] = []
        if self.skip_data is not None:
            for k in self.skip_data:
                result['SkipData'].append(k.to_map() if k else None)
        if self.succ_count is not None:
            result['SuccCount'] = self.succ_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail_data = []
        if m.get('FailData') is not None:
            for k in m.get('FailData'):
                temp_model = ImportNacosConfigResponseBodyDataFailData()
                self.fail_data.append(temp_model.from_map(k))
        if m.get('SkipCount') is not None:
            self.skip_count = m.get('SkipCount')
        self.skip_data = []
        if m.get('SkipData') is not None:
            for k in m.get('SkipData'):
                temp_model = ImportNacosConfigResponseBodyDataSkipData()
                self.skip_data.append(temp_model.from_map(k))
        if m.get('SuccCount') is not None:
            self.succ_count = m.get('SuccCount')
        return self


class ImportNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ImportNacosConfigResponseBodyData = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            temp_model = ImportNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportServicesRequestServiceList(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        name: str = None,
        namespace: str = None,
        service_port: int = None,
        service_protocol: str = None,
    ):
        self.group_name = group_name
        self.ips = ips
        self.name = name
        self.namespace = namespace
        # 服务的端口
        self.service_port = service_port
        # 服务的协议版本
        self.service_protocol = service_protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_port is not None:
            result['ServicePort'] = self.service_port
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        return self


class ImportServicesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        service_list: List[ImportServicesRequestServiceList] = None,
        source_id: str = None,
        source_type: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.service_list = service_list
        self.source_id = source_id
        # 服务来源
        self.source_type = source_type

    def validate(self):
        if self.service_list:
            for k in self.service_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        result['ServiceList'] = []
        if self.service_list is not None:
            for k in self.service_list:
                result['ServiceList'].append(k.to_map() if k else None)
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        self.service_list = []
        if m.get('ServiceList') is not None:
            for k in m.get('ServiceList'):
                temp_model = ImportServicesRequestServiceList()
                self.service_list.append(temp_model.from_map(k))
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class ImportServicesShrinkRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        service_list_shrink: str = None,
        source_id: str = None,
        source_type: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.service_list_shrink = service_list_shrink
        self.source_id = source_id
        # 服务来源
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.service_list_shrink is not None:
            result['ServiceList'] = self.service_list_shrink
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('ServiceList') is not None:
            self.service_list_shrink = m.get('ServiceList')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class ImportServicesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmContactGroupsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        page_num: int = None,
        page_size: int = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.page_num = page_num
        self.page_size = page_size
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListAlarmContactGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        contact_group_id: str = None,
        contact_group_name: str = None,
    ):
        self.contact_group_id = contact_group_id
        self.contact_group_name = contact_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        return self


class ListAlarmContactGroupsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAlarmContactGroupsResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmContactGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmContactGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmContactGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmContactGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmHistoriesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        alarm_mse_type: str = None,
        alarm_name: str = None,
        end_time: int = None,
        page_num: int = None,
        page_size: int = None,
        request_pars: str = None,
        start_time: int = None,
    ):
        self.accept_language = accept_language
        self.alarm_mse_type = alarm_mse_type
        self.alarm_name = alarm_name
        self.end_time = end_time
        self.page_num = page_num
        self.page_size = page_size
        self.request_pars = request_pars
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.alarm_mse_type is not None:
            result['AlarmMseType'] = self.alarm_mse_type
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AlarmMseType') is not None:
            self.alarm_mse_type = m.get('AlarmMseType')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListAlarmHistoriesResponseBodyData(TeaModel):
    def __init__(
        self,
        alarm_content: str = None,
        alarm_ding_ding: str = None,
        alarm_email: str = None,
        alarm_name: str = None,
        alarm_phone: str = None,
        alarm_time: str = None,
    ):
        self.alarm_content = alarm_content
        self.alarm_ding_ding = alarm_ding_ding
        self.alarm_email = alarm_email
        self.alarm_name = alarm_name
        self.alarm_phone = alarm_phone
        self.alarm_time = alarm_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_content is not None:
            result['AlarmContent'] = self.alarm_content
        if self.alarm_ding_ding is not None:
            result['AlarmDingDing'] = self.alarm_ding_ding
        if self.alarm_email is not None:
            result['AlarmEmail'] = self.alarm_email
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.alarm_phone is not None:
            result['AlarmPhone'] = self.alarm_phone
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmContent') is not None:
            self.alarm_content = m.get('AlarmContent')
        if m.get('AlarmDingDing') is not None:
            self.alarm_ding_ding = m.get('AlarmDingDing')
        if m.get('AlarmEmail') is not None:
            self.alarm_email = m.get('AlarmEmail')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('AlarmPhone') is not None:
            self.alarm_phone = m.get('AlarmPhone')
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        return self


class ListAlarmHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAlarmHistoriesResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmHistoriesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmItemsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListAlarmItemsResponseBodyData(TeaModel):
    def __init__(
        self,
        alarm_code: str = None,
        alarm_desc: str = None,
        cluster_type: str = None,
    ):
        self.alarm_code = alarm_code
        self.alarm_desc = alarm_desc
        self.cluster_type = cluster_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_code is not None:
            result['AlarmCode'] = self.alarm_code
        if self.alarm_desc is not None:
            result['AlarmDesc'] = self.alarm_desc
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmCode') is not None:
            self.alarm_code = m.get('AlarmCode')
        if m.get('AlarmDesc') is not None:
            self.alarm_desc = m.get('AlarmDesc')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class ListAlarmItemsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAlarmItemsResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmItemsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmRulesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        alarm_mse_type: str = None,
        page_num: int = None,
        page_size: int = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.alarm_mse_type = alarm_mse_type
        self.page_num = page_num
        self.page_size = page_size
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.alarm_mse_type is not None:
            result['AlarmMseType'] = self.alarm_mse_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AlarmMseType') is not None:
            self.alarm_mse_type = m.get('AlarmMseType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListAlarmRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        alarm_name: str = None,
        alarm_rule_detail: str = None,
        alarm_rule_id: str = None,
        alarm_status: str = None,
        create_time: str = None,
    ):
        self.alarm_name = alarm_name
        self.alarm_rule_detail = alarm_rule_detail
        self.alarm_rule_id = alarm_rule_id
        self.alarm_status = alarm_status
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.alarm_rule_detail is not None:
            result['AlarmRuleDetail'] = self.alarm_rule_detail
        if self.alarm_rule_id is not None:
            result['AlarmRuleId'] = self.alarm_rule_id
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('AlarmRuleDetail') is not None:
            self.alarm_rule_detail = m.get('AlarmRuleDetail')
        if m.get('AlarmRuleId') is not None:
            self.alarm_rule_id = m.get('AlarmRuleId')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class ListAlarmRulesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAlarmRulesResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmRulesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsInstancesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        group_name: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        page_num: int = None,
        page_size: int = None,
        request_pars: str = None,
        service_name: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.group_name = group_name
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.page_num = page_num
        self.page_size = page_size
        self.request_pars = request_pars
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListAnsInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        app: str = None,
        cluster_name: str = None,
        datum_key: str = None,
        default_key: str = None,
        enabled: bool = None,
        ephemeral: bool = None,
        fail_count: int = None,
        healthy: bool = None,
        instance_heart_beat_interval: int = None,
        instance_heart_beat_time_out: int = None,
        instance_id: str = None,
        ip: str = None,
        ip_delete_timeout: int = None,
        last_beat: int = None,
        marked: bool = None,
        metadata: Dict[str, Any] = None,
        ok_count: int = None,
        port: int = None,
        service_name: str = None,
        weight: int = None,
    ):
        self.app = app
        self.cluster_name = cluster_name
        self.datum_key = datum_key
        self.default_key = default_key
        self.enabled = enabled
        self.ephemeral = ephemeral
        self.fail_count = fail_count
        self.healthy = healthy
        self.instance_heart_beat_interval = instance_heart_beat_interval
        self.instance_heart_beat_time_out = instance_heart_beat_time_out
        self.instance_id = instance_id
        self.ip = ip
        self.ip_delete_timeout = ip_delete_timeout
        self.last_beat = last_beat
        self.marked = marked
        self.metadata = metadata
        self.ok_count = ok_count
        self.port = port
        self.service_name = service_name
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.datum_key is not None:
            result['DatumKey'] = self.datum_key
        if self.default_key is not None:
            result['DefaultKey'] = self.default_key
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.healthy is not None:
            result['Healthy'] = self.healthy
        if self.instance_heart_beat_interval is not None:
            result['InstanceHeartBeatInterval'] = self.instance_heart_beat_interval
        if self.instance_heart_beat_time_out is not None:
            result['InstanceHeartBeatTimeOut'] = self.instance_heart_beat_time_out
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_delete_timeout is not None:
            result['IpDeleteTimeout'] = self.ip_delete_timeout
        if self.last_beat is not None:
            result['LastBeat'] = self.last_beat
        if self.marked is not None:
            result['Marked'] = self.marked
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.ok_count is not None:
            result['OkCount'] = self.ok_count
        if self.port is not None:
            result['Port'] = self.port
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DatumKey') is not None:
            self.datum_key = m.get('DatumKey')
        if m.get('DefaultKey') is not None:
            self.default_key = m.get('DefaultKey')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('Healthy') is not None:
            self.healthy = m.get('Healthy')
        if m.get('InstanceHeartBeatInterval') is not None:
            self.instance_heart_beat_interval = m.get('InstanceHeartBeatInterval')
        if m.get('InstanceHeartBeatTimeOut') is not None:
            self.instance_heart_beat_time_out = m.get('InstanceHeartBeatTimeOut')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpDeleteTimeout') is not None:
            self.ip_delete_timeout = m.get('IpDeleteTimeout')
        if m.get('LastBeat') is not None:
            self.last_beat = m.get('LastBeat')
        if m.get('Marked') is not None:
            self.marked = m.get('Marked')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('OkCount') is not None:
            self.ok_count = m.get('OkCount')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ListAnsInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAnsInstancesResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAnsInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAnsInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAnsInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAnsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsServiceClustersRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        group_name: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        page_num: int = None,
        page_size: int = None,
        request_pars: str = None,
        service_name: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.group_name = group_name
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.page_num = page_num
        self.page_size = page_size
        self.request_pars = request_pars
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListAnsServiceClustersResponseBodyDataClusters(TeaModel):
    def __init__(
        self,
        default_check_port: int = None,
        default_port: int = None,
        health_checker_type: str = None,
        metadata: Dict[str, Any] = None,
        name: str = None,
        service_name: str = None,
        use_ipport_4check: bool = None,
    ):
        self.default_check_port = default_check_port
        self.default_port = default_port
        self.health_checker_type = health_checker_type
        self.metadata = metadata
        self.name = name
        self.service_name = service_name
        self.use_ipport_4check = use_ipport_4check

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_check_port is not None:
            result['DefaultCheckPort'] = self.default_check_port
        if self.default_port is not None:
            result['DefaultPort'] = self.default_port
        if self.health_checker_type is not None:
            result['HealthCheckerType'] = self.health_checker_type
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.name is not None:
            result['Name'] = self.name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.use_ipport_4check is not None:
            result['UseIPPort4Check'] = self.use_ipport_4check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCheckPort') is not None:
            self.default_check_port = m.get('DefaultCheckPort')
        if m.get('DefaultPort') is not None:
            self.default_port = m.get('DefaultPort')
        if m.get('HealthCheckerType') is not None:
            self.health_checker_type = m.get('HealthCheckerType')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('UseIPPort4Check') is not None:
            self.use_ipport_4check = m.get('UseIPPort4Check')
        return self


class ListAnsServiceClustersResponseBodyData(TeaModel):
    def __init__(
        self,
        clusters: List[ListAnsServiceClustersResponseBodyDataClusters] = None,
        ephemeral: bool = None,
        group_name: str = None,
        metadata: Dict[str, Any] = None,
        name: str = None,
        protect_threshold: float = None,
        selector_type: str = None,
    ):
        self.clusters = clusters
        self.ephemeral = ephemeral
        self.group_name = group_name
        self.metadata = metadata
        self.name = name
        self.protect_threshold = protect_threshold
        self.selector_type = selector_type

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.name is not None:
            result['Name'] = self.name
        if self.protect_threshold is not None:
            result['ProtectThreshold'] = self.protect_threshold
        if self.selector_type is not None:
            result['SelectorType'] = self.selector_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = ListAnsServiceClustersResponseBodyDataClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProtectThreshold') is not None:
            self.protect_threshold = m.get('ProtectThreshold')
        if m.get('SelectorType') is not None:
            self.selector_type = m.get('SelectorType')
        return self


class ListAnsServiceClustersResponseBody(TeaModel):
    def __init__(
        self,
        data: ListAnsServiceClustersResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListAnsServiceClustersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAnsServiceClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAnsServiceClustersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAnsServiceClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsServicesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        group_name: str = None,
        has_ip_count: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        page_num: int = None,
        page_size: int = None,
        request_pars: str = None,
        service_name: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.group_name = group_name
        self.has_ip_count = has_ip_count
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.page_num = page_num
        self.page_size = page_size
        self.request_pars = request_pars
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.has_ip_count is not None:
            result['HasIpCount'] = self.has_ip_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HasIpCount') is not None:
            self.has_ip_count = m.get('HasIpCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListAnsServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_count: int = None,
        group_name: str = None,
        healthy_instance_count: int = None,
        ip_count: int = None,
        name: str = None,
    ):
        self.cluster_count = cluster_count
        self.group_name = group_name
        self.healthy_instance_count = healthy_instance_count
        self.ip_count = ip_count
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.healthy_instance_count is not None:
            result['HealthyInstanceCount'] = self.healthy_instance_count
        if self.ip_count is not None:
            result['IpCount'] = self.ip_count
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HealthyInstanceCount') is not None:
            self.healthy_instance_count = m.get('HealthyInstanceCount')
        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAnsServicesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAnsServicesResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAnsServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAnsServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAnsServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAnsServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterConnectionTypesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class ListClusterConnectionTypesResponseBodyData(TeaModel):
    def __init__(
        self,
        show_name: str = None,
    ):
        self.show_name = show_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class ListClusterConnectionTypesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListClusterConnectionTypesResponseBodyData] = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            for k in m.get('Data'):
                temp_model = ListClusterConnectionTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClusterConnectionTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClusterConnectionTypesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClusterConnectionTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterTypesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        region_id: str = None,
    ):
        self.accept_language = accept_language
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListClusterTypesResponseBodyData(TeaModel):
    def __init__(
        self,
        show_name: str = None,
    ):
        self.show_name = show_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class ListClusterTypesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListClusterTypesResponseBodyData] = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            for k in m.get('Data'):
                temp_model = ListClusterTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClusterTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClusterTypesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClusterTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterVersionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_type: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_type = cluster_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class ListClusterVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        code: str = None,
        show_name: str = None,
    ):
        self.cluster_type = cluster_type
        self.code = code
        self.show_name = show_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.code is not None:
            result['Code'] = self.code
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class ListClusterVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListClusterVersionsResponseBodyData] = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            for k in m.get('Data'):
                temp_model = ListClusterVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClusterVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClusterVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClusterVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_alias_name: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_alias_name = cluster_alias_name
        self.page_num = page_num
        self.page_size = page_size
        self.region_id = region_id
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListClustersResponseBodyData(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        can_update: bool = None,
        charge_type: str = None,
        cluster_alias_name: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        create_time: str = None,
        end_date: str = None,
        init_status: str = None,
        instance_count: int = None,
        instance_id: str = None,
        internet_address: str = None,
        internet_domain: str = None,
        intranet_address: str = None,
        intranet_domain: str = None,
        version_code: str = None,
    ):
        self.app_version = app_version
        self.can_update = can_update
        self.charge_type = charge_type
        self.cluster_alias_name = cluster_alias_name
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.create_time = create_time
        self.end_date = end_date
        self.init_status = init_status
        self.instance_count = instance_count
        self.instance_id = instance_id
        self.internet_address = internet_address
        self.internet_domain = internet_domain
        self.intranet_address = intranet_address
        self.intranet_domain = intranet_domain
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.can_update is not None:
            result['CanUpdate'] = self.can_update
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.init_status is not None:
            result['InitStatus'] = self.init_status
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CanUpdate') is not None:
            self.can_update = m.get('CanUpdate')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InitStatus') is not None:
            self.init_status = m.get('InitStatus')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListClustersResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClustersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClustersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEngineNamespacesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
    ):
        self.accept_language = accept_language
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListEngineNamespacesResponseBodyData(TeaModel):
    def __init__(
        self,
        config_count: int = None,
        namespace: str = None,
        namespace_desc: str = None,
        namespace_show_name: str = None,
        quota: int = None,
        service_count: str = None,
        type: int = None,
    ):
        self.config_count = config_count
        self.namespace = namespace
        self.namespace_desc = namespace_desc
        self.namespace_show_name = namespace_show_name
        self.quota = quota
        self.service_count = service_count
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListEngineNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListEngineNamespacesResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEngineNamespacesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEngineNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEngineNamespacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEngineNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEurekaInstancesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        page_num: int = None,
        page_size: int = None,
        request_pars: str = None,
        service_name: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.page_num = page_num
        self.page_size = page_size
        self.request_pars = request_pars
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListEurekaInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        app: str = None,
        duration_in_secs: int = None,
        home_page_url: str = None,
        host_name: str = None,
        instance_id: str = None,
        ip_addr: str = None,
        last_dirty_timestamp: int = None,
        last_updated_timestamp: int = None,
        metadata: Dict[str, Any] = None,
        port: int = None,
        renewal_interval_in_secs: int = None,
        secure_port: int = None,
        status: str = None,
        vip_address: str = None,
    ):
        self.app = app
        self.duration_in_secs = duration_in_secs
        self.home_page_url = home_page_url
        self.host_name = host_name
        self.instance_id = instance_id
        self.ip_addr = ip_addr
        self.last_dirty_timestamp = last_dirty_timestamp
        self.last_updated_timestamp = last_updated_timestamp
        self.metadata = metadata
        self.port = port
        self.renewal_interval_in_secs = renewal_interval_in_secs
        self.secure_port = secure_port
        self.status = status
        self.vip_address = vip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.duration_in_secs is not None:
            result['DurationInSecs'] = self.duration_in_secs
        if self.home_page_url is not None:
            result['HomePageUrl'] = self.home_page_url
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_addr is not None:
            result['IpAddr'] = self.ip_addr
        if self.last_dirty_timestamp is not None:
            result['LastDirtyTimestamp'] = self.last_dirty_timestamp
        if self.last_updated_timestamp is not None:
            result['LastUpdatedTimestamp'] = self.last_updated_timestamp
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.port is not None:
            result['Port'] = self.port
        if self.renewal_interval_in_secs is not None:
            result['RenewalIntervalInSecs'] = self.renewal_interval_in_secs
        if self.secure_port is not None:
            result['SecurePort'] = self.secure_port
        if self.status is not None:
            result['Status'] = self.status
        if self.vip_address is not None:
            result['VipAddress'] = self.vip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('DurationInSecs') is not None:
            self.duration_in_secs = m.get('DurationInSecs')
        if m.get('HomePageUrl') is not None:
            self.home_page_url = m.get('HomePageUrl')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpAddr') is not None:
            self.ip_addr = m.get('IpAddr')
        if m.get('LastDirtyTimestamp') is not None:
            self.last_dirty_timestamp = m.get('LastDirtyTimestamp')
        if m.get('LastUpdatedTimestamp') is not None:
            self.last_updated_timestamp = m.get('LastUpdatedTimestamp')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RenewalIntervalInSecs') is not None:
            self.renewal_interval_in_secs = m.get('RenewalIntervalInSecs')
        if m.get('SecurePort') is not None:
            self.secure_port = m.get('SecurePort')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VipAddress') is not None:
            self.vip_address = m.get('VipAddress')
        return self


class ListEurekaInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListEurekaInstancesResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEurekaInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEurekaInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEurekaInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEurekaInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEurekaServicesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.page_num = page_num
        self.page_size = page_size
        self.region_id = region_id
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListEurekaServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        instances_id: List[str] = None,
        name: str = None,
        up_status: str = None,
    ):
        self.instances_id = instances_id
        self.name = name
        self.up_status = up_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances_id is not None:
            result['InstancesId'] = self.instances_id
        if self.name is not None:
            result['Name'] = self.name
        if self.up_status is not None:
            result['UpStatus'] = self.up_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstancesId') is not None:
            self.instances_id = m.get('InstancesId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpStatus') is not None:
            self.up_status = m.get('UpStatus')
        return self


class ListEurekaServicesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListEurekaServicesResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEurekaServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEurekaServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEurekaServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEurekaServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayRequestFilterParams(TeaModel):
    def __init__(
        self,
        gateway_type: str = None,
        gateway_unique_id: str = None,
        instance_id: str = None,
        name: str = None,
        vpc: str = None,
    ):
        self.gateway_type = gateway_type
        self.gateway_unique_id = gateway_unique_id
        self.instance_id = instance_id
        self.name = name
        self.vpc = vpc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
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
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')
        return self


class ListGatewayRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        desc_sort: bool = None,
        filter_params: ListGatewayRequestFilterParams = None,
        order_item: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.accept_language = accept_language
        self.desc_sort = desc_sort
        self.filter_params = filter_params
        self.order_item = order_item
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        if self.filter_params:
            self.filter_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListGatewayRequestFilterParams()
            self.filter_params = temp_model.from_map(m['FilterParams'])
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGatewayShrinkRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        desc_sort: bool = None,
        filter_params_shrink: str = None,
        order_item: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.accept_language = accept_language
        self.desc_sort = desc_sort
        self.filter_params_shrink = filter_params_shrink
        self.order_item = order_item
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort
        if self.filter_params_shrink is not None:
            result['FilterParams'] = self.filter_params_shrink
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
            self.filter_params_shrink = m.get('FilterParams')
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGatewayResponseBodyDataResultInternetSlb(TeaModel):
    def __init__(
        self,
        gateway_slb_mode: str = None,
        gateway_slb_status: str = None,
        internet_network_flow: str = None,
        slb_id: str = None,
        slb_ip: str = None,
        slb_port: str = None,
        slb_spec: str = None,
        status_desc: str = None,
        type: str = None,
    ):
        self.gateway_slb_mode = gateway_slb_mode
        self.gateway_slb_status = gateway_slb_status
        self.internet_network_flow = internet_network_flow
        self.slb_id = slb_id
        self.slb_ip = slb_ip
        self.slb_port = slb_port
        self.slb_spec = slb_spec
        self.status_desc = status_desc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_slb_mode is not None:
            result['GatewaySlbMode'] = self.gateway_slb_mode
        if self.gateway_slb_status is not None:
            result['GatewaySlbStatus'] = self.gateway_slb_status
        if self.internet_network_flow is not None:
            result['InternetNetworkFlow'] = self.internet_network_flow
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip
        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port
        if self.slb_spec is not None:
            result['SlbSpec'] = self.slb_spec
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewaySlbMode') is not None:
            self.gateway_slb_mode = m.get('GatewaySlbMode')
        if m.get('GatewaySlbStatus') is not None:
            self.gateway_slb_status = m.get('GatewaySlbStatus')
        if m.get('InternetNetworkFlow') is not None:
            self.internet_network_flow = m.get('InternetNetworkFlow')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')
        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')
        if m.get('SlbSpec') is not None:
            self.slb_spec = m.get('SlbSpec')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListGatewayResponseBodyDataResultSlb(TeaModel):
    def __init__(
        self,
        gateway_slb_mode: str = None,
        gateway_slb_status: str = None,
        slb_id: str = None,
        slb_ip: str = None,
        slb_port: str = None,
        slb_spec: str = None,
        status_desc: str = None,
        type: str = None,
    ):
        self.gateway_slb_mode = gateway_slb_mode
        self.gateway_slb_status = gateway_slb_status
        self.slb_id = slb_id
        self.slb_ip = slb_ip
        self.slb_port = slb_port
        self.slb_spec = slb_spec
        self.status_desc = status_desc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_slb_mode is not None:
            result['GatewaySlbMode'] = self.gateway_slb_mode
        if self.gateway_slb_status is not None:
            result['GatewaySlbStatus'] = self.gateway_slb_status
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip
        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port
        if self.slb_spec is not None:
            result['SlbSpec'] = self.slb_spec
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewaySlbMode') is not None:
            self.gateway_slb_mode = m.get('GatewaySlbMode')
        if m.get('GatewaySlbStatus') is not None:
            self.gateway_slb_status = m.get('GatewaySlbStatus')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')
        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')
        if m.get('SlbSpec') is not None:
            self.slb_spec = m.get('SlbSpec')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListGatewayResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        ahas_on: bool = None,
        arms_on: bool = None,
        charge_type: str = None,
        current_version: str = None,
        end_date: str = None,
        gateway_type: str = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        internet_slb: List[ListGatewayResponseBodyDataResultInternetSlb] = None,
        latest_version: str = None,
        must_upgrade: bool = None,
        name: str = None,
        primary_user: str = None,
        region: str = None,
        replica: int = None,
        slb: List[ListGatewayResponseBodyDataResultSlb] = None,
        spec: str = None,
        status: int = None,
        status_desc: str = None,
        tag: str = None,
        upgrade: bool = None,
        vswitch_2: str = None,
    ):
        self.ahas_on = ahas_on
        self.arms_on = arms_on
        self.charge_type = charge_type
        self.current_version = current_version
        self.end_date = end_date
        self.gateway_type = gateway_type
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.internet_slb = internet_slb
        self.latest_version = latest_version
        self.must_upgrade = must_upgrade
        self.name = name
        self.primary_user = primary_user
        self.region = region
        self.replica = replica
        self.slb = slb
        self.spec = spec
        self.status = status
        self.status_desc = status_desc
        self.tag = tag
        self.upgrade = upgrade
        self.vswitch_2 = vswitch_2

    def validate(self):
        if self.internet_slb:
            for k in self.internet_slb:
                if k:
                    k.validate()
        if self.slb:
            for k in self.slb:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ahas_on is not None:
            result['AhasOn'] = self.ahas_on
        if self.arms_on is not None:
            result['ArmsOn'] = self.arms_on
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['InternetSlb'] = []
        if self.internet_slb is not None:
            for k in self.internet_slb:
                result['InternetSlb'].append(k.to_map() if k else None)
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.must_upgrade is not None:
            result['MustUpgrade'] = self.must_upgrade
        if self.name is not None:
            result['Name'] = self.name
        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user
        if self.region is not None:
            result['Region'] = self.region
        if self.replica is not None:
            result['Replica'] = self.replica
        result['Slb'] = []
        if self.slb is not None:
            for k in self.slb:
                result['Slb'].append(k.to_map() if k else None)
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade
        if self.vswitch_2 is not None:
            result['Vswitch2'] = self.vswitch_2
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AhasOn') is not None:
            self.ahas_on = m.get('AhasOn')
        if m.get('ArmsOn') is not None:
            self.arms_on = m.get('ArmsOn')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.internet_slb = []
        if m.get('InternetSlb') is not None:
            for k in m.get('InternetSlb'):
                temp_model = ListGatewayResponseBodyDataResultInternetSlb()
                self.internet_slb.append(temp_model.from_map(k))
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('MustUpgrade') is not None:
            self.must_upgrade = m.get('MustUpgrade')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Replica') is not None:
            self.replica = m.get('Replica')
        self.slb = []
        if m.get('Slb') is not None:
            for k in m.get('Slb'):
                temp_model = ListGatewayResponseBodyDataResultSlb()
                self.slb.append(temp_model.from_map(k))
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')
        if m.get('Vswitch2') is not None:
            self.vswitch_2 = m.get('Vswitch2')
        return self


class ListGatewayResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[ListGatewayResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.result = result
        self.total_size = total_size

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
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
            for k in m.get('Result'):
                temp_model = ListGatewayResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListGatewayResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListGatewayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGatewayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayDomainRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class ListGatewayDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        cert_before_date: str = None,
        cert_identifier: str = None,
        gateway_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        must_https: bool = None,
        name: str = None,
        protocol: str = None,
    ):
        self.cert_before_date = cert_before_date
        self.cert_identifier = cert_identifier
        self.gateway_id = gateway_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.must_https = must_https
        self.name = name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_before_date is not None:
            result['CertBeforeDate'] = self.cert_before_date
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.must_https is not None:
            result['MustHttps'] = self.must_https
        if self.name is not None:
            result['Name'] = self.name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertBeforeDate') is not None:
            self.cert_before_date = m.get('CertBeforeDate')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class ListGatewayDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListGatewayDomainResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = ListGatewayDomainResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGatewayDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGatewayDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGatewayDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayServiceRequestFilterParams(TeaModel):
    def __init__(
        self,
        gateway_unique_id: str = None,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        source_type: str = None,
    ):
        self.gateway_unique_id = gateway_unique_id
        self.group_name = group_name
        self.name = name
        self.namespace = namespace
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
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
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class ListGatewayServiceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        desc_sort: bool = None,
        filter_params: ListGatewayServiceRequestFilterParams = None,
        order_item: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.accept_language = accept_language
        self.desc_sort = desc_sort
        self.filter_params = filter_params
        self.order_item = order_item
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        if self.filter_params:
            self.filter_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListGatewayServiceRequestFilterParams()
            self.filter_params = temp_model.from_map(m['FilterParams'])
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGatewayServiceShrinkRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        desc_sort: bool = None,
        filter_params_shrink: str = None,
        order_item: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.accept_language = accept_language
        self.desc_sort = desc_sort
        self.filter_params_shrink = filter_params_shrink
        self.order_item = order_item
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort
        if self.filter_params_shrink is not None:
            result['FilterParams'] = self.filter_params_shrink
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
            self.filter_params_shrink = m.get('FilterParams')
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGatewayServiceResponseBodyDataResultVersions(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListGatewayServiceResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_name: str = None,
        id: int = None,
        ips: List[str] = None,
        meta_info: str = None,
        name: str = None,
        namespace: str = None,
        service_name_in_registry: str = None,
        service_port: int = None,
        service_protocol: str = None,
        source_id: int = None,
        source_type: str = None,
        versions: List[ListGatewayServiceResponseBodyDataResultVersions] = None,
    ):
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_name = group_name
        self.id = id
        self.ips = ips
        self.meta_info = meta_info
        self.name = name
        self.namespace = namespace
        self.service_name_in_registry = service_name_in_registry
        self.service_port = service_port
        self.service_protocol = service_protocol
        self.source_id = source_id
        self.source_type = source_type
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_name_in_registry is not None:
            result['ServiceNameInRegistry'] = self.service_name_in_registry
        if self.service_port is not None:
            result['ServicePort'] = self.service_port
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('ServiceNameInRegistry')
        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListGatewayServiceResponseBodyDataResultVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListGatewayServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[ListGatewayServiceResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.result = result
        self.total_size = total_size

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
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
            for k in m.get('Result'):
                temp_model = ListGatewayServiceResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListGatewayServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListGatewayServiceResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListGatewayServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGatewayServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGatewayServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGatewayServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewaySlbRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class ListGatewaySlbResponseBodyData(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        gateway_slb_mode: str = None,
        gateway_slb_status: str = None,
        gmt_create: str = None,
        id: str = None,
        slb_id: str = None,
        slb_ip: str = None,
        slb_port: str = None,
        status_desc: str = None,
        type: str = None,
    ):
        self.gateway_id = gateway_id
        self.gateway_slb_mode = gateway_slb_mode
        self.gateway_slb_status = gateway_slb_status
        self.gmt_create = gmt_create
        self.id = id
        self.slb_id = slb_id
        self.slb_ip = slb_ip
        self.slb_port = slb_port
        self.status_desc = status_desc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_slb_mode is not None:
            result['GatewaySlbMode'] = self.gateway_slb_mode
        if self.gateway_slb_status is not None:
            result['GatewaySlbStatus'] = self.gateway_slb_status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip
        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewaySlbMode') is not None:
            self.gateway_slb_mode = m.get('GatewaySlbMode')
        if m.get('GatewaySlbStatus') is not None:
            self.gateway_slb_status = m.get('GatewaySlbStatus')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')
        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListGatewaySlbResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListGatewaySlbResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = ListGatewaySlbResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGatewaySlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGatewaySlbResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGatewaySlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersByConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        data_id: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.data_id = data_id
        self.group = group
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListListenersByConfigResponseBodyListeners(TeaModel):
    def __init__(
        self,
        ip: str = None,
        md_5: str = None,
    ):
        self.ip = ip
        self.md_5 = md_5

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        return self


class ListListenersByConfigResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        http_code: str = None,
        listeners: List[ListListenersByConfigResponseBodyListeners] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.http_code = http_code
        self.listeners = listeners
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersByConfigResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenersByConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListListenersByConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListListenersByConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersByIpRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        ip: str = None,
        namespace_id: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.instance_id = instance_id
        self.ip = ip
        self.namespace_id = namespace_id
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListListenersByIpResponseBodyListeners(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
        md_5: str = None,
    ):
        self.data_id = data_id
        self.group = group
        self.md_5 = md_5

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        return self


class ListListenersByIpResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        http_code: str = None,
        listeners: List[ListListenersByIpResponseBodyListeners] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.http_code = http_code
        self.listeners = listeners
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersByIpResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenersByIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListListenersByIpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListListenersByIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNacosConfigsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        data_id: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        request_pars: str = None,
        tags: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.data_id = data_id
        self.group = group
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.page_num = page_num
        self.page_size = page_size
        self.region_id = region_id
        self.request_pars = request_pars
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListNacosConfigsResponseBodyConfigurations(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        data_id: str = None,
        group: str = None,
        id: str = None,
    ):
        self.app_name = app_name
        self.data_id = data_id
        self.group = group
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListNacosConfigsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        configurations: List[ListNacosConfigsResponseBodyConfigurations] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.configurations = configurations
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.configurations:
            for k in self.configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Configurations'] = []
        if self.configurations is not None:
            for k in self.configurations:
                result['Configurations'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.configurations = []
        if m.get('Configurations') is not None:
            for k in m.get('Configurations'):
                temp_model = ListNacosConfigsResponseBodyConfigurations()
                self.configurations.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNacosConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNacosConfigsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNacosConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNacosHistoryConfigsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        data_id: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.data_id = data_id
        self.group = group
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.page_num = page_num
        self.page_size = page_size
        self.region_id = region_id
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListNacosHistoryConfigsResponseBodyHistoryItems(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        data_id: str = None,
        group: str = None,
        id: int = None,
        last_modified_time: int = None,
        op_type: str = None,
    ):
        self.app_name = app_name
        self.data_id = data_id
        self.group = group
        self.id = id
        self.last_modified_time = last_modified_time
        self.op_type = op_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.op_type is not None:
            result['OpType'] = self.op_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        return self


class ListNacosHistoryConfigsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        history_items: List[ListNacosHistoryConfigsResponseBodyHistoryItems] = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.history_items = history_items
        self.http_code = http_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.history_items:
            for k in self.history_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['HistoryItems'] = []
        if self.history_items is not None:
            for k in self.history_items:
                result['HistoryItems'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.history_items = []
        if m.get('HistoryItems') is not None:
            for k in m.get('HistoryItems'):
                temp_model = ListNacosHistoryConfigsResponseBodyHistoryItems()
                self.history_items.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNacosHistoryConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNacosHistoryConfigsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNacosHistoryConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSSLCertRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class ListSSLCertResponseBodyData(TeaModel):
    def __init__(
        self,
        after_date: str = None,
        algorithm: str = None,
        before_date: str = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        gmt_after: str = None,
        gmt_before: str = None,
        issuer: str = None,
        sans: str = None,
    ):
        self.after_date = after_date
        self.algorithm = algorithm
        self.before_date = before_date
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.common_name = common_name
        self.gmt_after = gmt_after
        self.gmt_before = gmt_before
        self.issuer = issuer
        self.sans = sans

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.gmt_after is not None:
            result['GmtAfter'] = self.gmt_after
        if self.gmt_before is not None:
            result['GmtBefore'] = self.gmt_before
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.sans is not None:
            result['Sans'] = self.sans
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('GmtAfter') is not None:
            self.gmt_after = m.get('GmtAfter')
        if m.get('GmtBefore') is not None:
            self.gmt_before = m.get('GmtBefore')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        return self


class ListSSLCertResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListSSLCertResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = ListSSLCertResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSSLCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSSLCertResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSSLCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceSourceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class ListServiceSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        address: str = None,
        binding_with_gateway: int = None,
        gateway_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        source: str = None,
        source_unique_id: str = None,
        type: str = None,
    ):
        self.address = address
        self.binding_with_gateway = binding_with_gateway
        self.gateway_id = gateway_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.source = source
        self.source_unique_id = source_unique_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.binding_with_gateway is not None:
            result['BindingWithGateway'] = self.binding_with_gateway
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        if self.source_unique_id is not None:
            result['SourceUniqueId'] = self.source_unique_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BindingWithGateway') is not None:
            self.binding_with_gateway = m.get('BindingWithGateway')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUniqueId') is not None:
            self.source_unique_id = m.get('SourceUniqueId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListServiceSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListServiceSourceResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = ListServiceSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListServiceSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServiceSourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListServiceSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZnodeChildrenRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        path: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ListZnodeChildrenResponseBodyData(TeaModel):
    def __init__(
        self,
        data: str = None,
        dir: bool = None,
        name: str = None,
        path: str = None,
    ):
        self.data = data
        self.dir = dir
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ListZnodeChildrenResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListZnodeChildrenResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListZnodeChildrenResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListZnodeChildrenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListZnodeChildrenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListZnodeChildrenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGovernanceKubernetesClusterRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        namespace_infos: str = None,
        region_id: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.namespace_infos = namespace_infos
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyGovernanceKubernetesClusterResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyGovernanceKubernetesClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyGovernanceKubernetesClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyGovernanceKubernetesClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PullServicesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        source_id: str = None,
        source_type: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.source_id = source_id
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class PullServicesResponseBodyDataServices(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        source_id: str = None,
        source_type: str = None,
    ):
        self.group_name = group_name
        self.name = name
        self.namespace = namespace
        self.source_id = source_id
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class PullServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        namespace: str = None,
        services: List[PullServicesResponseBodyDataServices] = None,
    ):
        self.group_name = group_name
        self.namespace = namespace
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = PullServicesResponseBodyDataServices()
                self.services.append(temp_model.from_map(k))
        return self


class PullServicesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[PullServicesResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = PullServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PullServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PullServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PullServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBusinessLocationsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class QueryBusinessLocationsResponseBodyData(TeaModel):
    def __init__(
        self,
        cn_name: str = None,
        description: str = None,
        district_cn_name: str = None,
        district_en_name: str = None,
        district_id: str = None,
        district_ordering: int = None,
        district_show_name: str = None,
        en_description: str = None,
        en_name: str = None,
        name: str = None,
        ordering: int = None,
        show_name: str = None,
        type: str = None,
    ):
        self.cn_name = cn_name
        self.description = description
        self.district_cn_name = district_cn_name
        self.district_en_name = district_en_name
        self.district_id = district_id
        self.district_ordering = district_ordering
        self.district_show_name = district_show_name
        self.en_description = en_description
        self.en_name = en_name
        self.name = name
        self.ordering = ordering
        self.show_name = show_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cn_name is not None:
            result['CnName'] = self.cn_name
        if self.description is not None:
            result['Description'] = self.description
        if self.district_cn_name is not None:
            result['DistrictCnName'] = self.district_cn_name
        if self.district_en_name is not None:
            result['DistrictEnName'] = self.district_en_name
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.district_ordering is not None:
            result['DistrictOrdering'] = self.district_ordering
        if self.district_show_name is not None:
            result['DistrictShowName'] = self.district_show_name
        if self.en_description is not None:
            result['EnDescription'] = self.en_description
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.name is not None:
            result['Name'] = self.name
        if self.ordering is not None:
            result['Ordering'] = self.ordering
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistrictCnName') is not None:
            self.district_cn_name = m.get('DistrictCnName')
        if m.get('DistrictEnName') is not None:
            self.district_en_name = m.get('DistrictEnName')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('DistrictOrdering') is not None:
            self.district_ordering = m.get('DistrictOrdering')
        if m.get('DistrictShowName') is not None:
            self.district_show_name = m.get('DistrictShowName')
        if m.get('EnDescription') is not None:
            self.en_description = m.get('EnDescription')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ordering') is not None:
            self.ordering = m.get('Ordering')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryBusinessLocationsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryBusinessLocationsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryBusinessLocationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBusinessLocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBusinessLocationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryBusinessLocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterDetailRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        order_id: str = None,
    ):
        self.accept_language = accept_language
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class QueryClusterDetailResponseBodyDataInstanceModels(TeaModel):
    def __init__(
        self,
        creation_timestamp: str = None,
        health_status: str = None,
        internet_ip: str = None,
        ip: str = None,
        pod_name: str = None,
        role: str = None,
        single_tunnel_vip: str = None,
    ):
        self.creation_timestamp = creation_timestamp
        self.health_status = health_status
        self.internet_ip = internet_ip
        self.ip = ip
        self.pod_name = pod_name
        self.role = role
        self.single_tunnel_vip = single_tunnel_vip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_timestamp is not None:
            result['CreationTimestamp'] = self.creation_timestamp
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.role is not None:
            result['Role'] = self.role
        if self.single_tunnel_vip is not None:
            result['SingleTunnelVip'] = self.single_tunnel_vip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTimestamp') is not None:
            self.creation_timestamp = m.get('CreationTimestamp')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SingleTunnelVip') is not None:
            self.single_tunnel_vip = m.get('SingleTunnelVip')
        return self


class QueryClusterDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        acl_entry_list: str = None,
        acl_id: str = None,
        app_version: str = None,
        charge_type: str = None,
        cluster_alias_name: str = None,
        cluster_name: str = None,
        cluster_specification: str = None,
        cluster_type: str = None,
        cluster_version: str = None,
        connection_type: str = None,
        cpu: int = None,
        create_time: str = None,
        disk_capacity: int = None,
        disk_type: str = None,
        health_status: str = None,
        init_cost_time: int = None,
        init_status: str = None,
        instance_count: int = None,
        instance_id: str = None,
        instance_models: List[QueryClusterDetailResponseBodyDataInstanceModels] = None,
        internet_address: str = None,
        internet_domain: str = None,
        internet_port: str = None,
        intranet_address: str = None,
        intranet_domain: str = None,
        intranet_port: str = None,
        memory_capacity: int = None,
        mse_version: str = None,
        net_type: str = None,
        pay_info: str = None,
        pub_network_flow: str = None,
        region_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.acl_entry_list = acl_entry_list
        self.acl_id = acl_id
        self.app_version = app_version
        self.charge_type = charge_type
        self.cluster_alias_name = cluster_alias_name
        self.cluster_name = cluster_name
        self.cluster_specification = cluster_specification
        self.cluster_type = cluster_type
        self.cluster_version = cluster_version
        self.connection_type = connection_type
        self.cpu = cpu
        self.create_time = create_time
        self.disk_capacity = disk_capacity
        self.disk_type = disk_type
        self.health_status = health_status
        self.init_cost_time = init_cost_time
        self.init_status = init_status
        self.instance_count = instance_count
        self.instance_id = instance_id
        self.instance_models = instance_models
        self.internet_address = internet_address
        self.internet_domain = internet_domain
        self.internet_port = internet_port
        self.intranet_address = intranet_address
        self.intranet_domain = intranet_domain
        self.intranet_port = intranet_port
        self.memory_capacity = memory_capacity
        self.mse_version = mse_version
        self.net_type = net_type
        self.pay_info = pay_info
        self.pub_network_flow = pub_network_flow
        self.region_id = region_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        if self.instance_models:
            for k in self.instance_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_entry_list is not None:
            result['AclEntryList'] = self.acl_entry_list
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.init_cost_time is not None:
            result['InitCostTime'] = self.init_cost_time
        if self.init_status is not None:
            result['InitStatus'] = self.init_status
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['InstanceModels'] = []
        if self.instance_models is not None:
            for k in self.instance_models:
                result['InstanceModels'].append(k.to_map() if k else None)
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.internet_port is not None:
            result['InternetPort'] = self.internet_port
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.intranet_port is not None:
            result['IntranetPort'] = self.intranet_port
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.pay_info is not None:
            result['PayInfo'] = self.pay_info
        if self.pub_network_flow is not None:
            result['PubNetworkFlow'] = self.pub_network_flow
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntryList') is not None:
            self.acl_entry_list = m.get('AclEntryList')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('InitCostTime') is not None:
            self.init_cost_time = m.get('InitCostTime')
        if m.get('InitStatus') is not None:
            self.init_status = m.get('InitStatus')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.instance_models = []
        if m.get('InstanceModels') is not None:
            for k in m.get('InstanceModels'):
                temp_model = QueryClusterDetailResponseBodyDataInstanceModels()
                self.instance_models.append(temp_model.from_map(k))
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('InternetPort') is not None:
            self.internet_port = m.get('InternetPort')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('IntranetPort') is not None:
            self.intranet_port = m.get('IntranetPort')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('PayInfo') is not None:
            self.pay_info = m.get('PayInfo')
        if m.get('PubNetworkFlow') is not None:
            self.pub_network_flow = m.get('PubNetworkFlow')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class QueryClusterDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryClusterDetailResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryClusterDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryClusterDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryClusterDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterDiskSpecificationRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_type: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_type = cluster_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class QueryClusterDiskSpecificationResponseBodyData(TeaModel):
    def __init__(
        self,
        max: int = None,
        min: int = None,
        step: int = None,
    ):
        self.max = max
        self.min = min
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class QueryClusterDiskSpecificationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryClusterDiskSpecificationResponseBodyData = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            temp_model = QueryClusterDiskSpecificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryClusterDiskSpecificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryClusterDiskSpecificationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryClusterDiskSpecificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterSpecificationRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class QueryClusterSpecificationResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_specification_name: str = None,
        cpu_capacity: str = None,
        disk_capacity: str = None,
        instance_count: str = None,
        max_con: str = None,
        max_tps: str = None,
        memory_capacity: str = None,
    ):
        self.cluster_specification_name = cluster_specification_name
        self.cpu_capacity = cpu_capacity
        self.disk_capacity = disk_capacity
        self.instance_count = instance_count
        self.max_con = max_con
        self.max_tps = max_tps
        self.memory_capacity = memory_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_specification_name is not None:
            result['ClusterSpecificationName'] = self.cluster_specification_name
        if self.cpu_capacity is not None:
            result['CpuCapacity'] = self.cpu_capacity
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.max_con is not None:
            result['MaxCon'] = self.max_con
        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterSpecificationName') is not None:
            self.cluster_specification_name = m.get('ClusterSpecificationName')
        if m.get('CpuCapacity') is not None:
            self.cpu_capacity = m.get('CpuCapacity')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('MaxCon') is not None:
            self.max_con = m.get('MaxCon')
        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        return self


class QueryClusterSpecificationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[QueryClusterSpecificationResponseBodyData] = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            for k in m.get('Data'):
                temp_model = QueryClusterSpecificationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryClusterSpecificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryClusterSpecificationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryClusterSpecificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        config_type: str = None,
        instance_id: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.config_type = config_type
        self.instance_id = instance_id
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class QueryConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        autopurge_purge_interval: str = None,
        autopurge_snap_retain_count: str = None,
        cluster_name: str = None,
        config_auth_enabled: bool = None,
        config_auth_supported: bool = None,
        config_secret_enabled: bool = None,
        config_secret_supported: bool = None,
        init_limit: str = None,
        jute_maxbuffer: str = None,
        jvm_flags_custom: str = None,
        mcpenabled: bool = None,
        mcpsupported: bool = None,
        max_client_cnxns: str = None,
        max_session_timeout: str = None,
        min_session_timeout: str = None,
        naming_create_service_supported: bool = None,
        open_super_acl: bool = None,
        pass_word: str = None,
        restart_flag: bool = None,
        sync_limit: str = None,
        tick_time: str = None,
        user_name: str = None,
    ):
        self.autopurge_purge_interval = autopurge_purge_interval
        self.autopurge_snap_retain_count = autopurge_snap_retain_count
        self.cluster_name = cluster_name
        self.config_auth_enabled = config_auth_enabled
        self.config_auth_supported = config_auth_supported
        self.config_secret_enabled = config_secret_enabled
        self.config_secret_supported = config_secret_supported
        self.init_limit = init_limit
        self.jute_maxbuffer = jute_maxbuffer
        self.jvm_flags_custom = jvm_flags_custom
        self.mcpenabled = mcpenabled
        self.mcpsupported = mcpsupported
        self.max_client_cnxns = max_client_cnxns
        # 最大超时时间
        self.max_session_timeout = max_session_timeout
        # 最小超时时间
        self.min_session_timeout = min_session_timeout
        self.naming_create_service_supported = naming_create_service_supported
        self.open_super_acl = open_super_acl
        self.pass_word = pass_word
        self.restart_flag = restart_flag
        self.sync_limit = sync_limit
        self.tick_time = tick_time
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autopurge_purge_interval is not None:
            result['AutopurgePurgeInterval'] = self.autopurge_purge_interval
        if self.autopurge_snap_retain_count is not None:
            result['AutopurgeSnapRetainCount'] = self.autopurge_snap_retain_count
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.config_auth_enabled is not None:
            result['ConfigAuthEnabled'] = self.config_auth_enabled
        if self.config_auth_supported is not None:
            result['ConfigAuthSupported'] = self.config_auth_supported
        if self.config_secret_enabled is not None:
            result['ConfigSecretEnabled'] = self.config_secret_enabled
        if self.config_secret_supported is not None:
            result['ConfigSecretSupported'] = self.config_secret_supported
        if self.init_limit is not None:
            result['InitLimit'] = self.init_limit
        if self.jute_maxbuffer is not None:
            result['JuteMaxbuffer'] = self.jute_maxbuffer
        if self.jvm_flags_custom is not None:
            result['JvmFlagsCustom'] = self.jvm_flags_custom
        if self.mcpenabled is not None:
            result['MCPEnabled'] = self.mcpenabled
        if self.mcpsupported is not None:
            result['MCPSupported'] = self.mcpsupported
        if self.max_client_cnxns is not None:
            result['MaxClientCnxns'] = self.max_client_cnxns
        if self.max_session_timeout is not None:
            result['MaxSessionTimeout'] = self.max_session_timeout
        if self.min_session_timeout is not None:
            result['MinSessionTimeout'] = self.min_session_timeout
        if self.naming_create_service_supported is not None:
            result['NamingCreateServiceSupported'] = self.naming_create_service_supported
        if self.open_super_acl is not None:
            result['OpenSuperAcl'] = self.open_super_acl
        if self.pass_word is not None:
            result['PassWord'] = self.pass_word
        if self.restart_flag is not None:
            result['RestartFlag'] = self.restart_flag
        if self.sync_limit is not None:
            result['SyncLimit'] = self.sync_limit
        if self.tick_time is not None:
            result['TickTime'] = self.tick_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutopurgePurgeInterval') is not None:
            self.autopurge_purge_interval = m.get('AutopurgePurgeInterval')
        if m.get('AutopurgeSnapRetainCount') is not None:
            self.autopurge_snap_retain_count = m.get('AutopurgeSnapRetainCount')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ConfigAuthEnabled') is not None:
            self.config_auth_enabled = m.get('ConfigAuthEnabled')
        if m.get('ConfigAuthSupported') is not None:
            self.config_auth_supported = m.get('ConfigAuthSupported')
        if m.get('ConfigSecretEnabled') is not None:
            self.config_secret_enabled = m.get('ConfigSecretEnabled')
        if m.get('ConfigSecretSupported') is not None:
            self.config_secret_supported = m.get('ConfigSecretSupported')
        if m.get('InitLimit') is not None:
            self.init_limit = m.get('InitLimit')
        if m.get('JuteMaxbuffer') is not None:
            self.jute_maxbuffer = m.get('JuteMaxbuffer')
        if m.get('JvmFlagsCustom') is not None:
            self.jvm_flags_custom = m.get('JvmFlagsCustom')
        if m.get('MCPEnabled') is not None:
            self.mcpenabled = m.get('MCPEnabled')
        if m.get('MCPSupported') is not None:
            self.mcpsupported = m.get('MCPSupported')
        if m.get('MaxClientCnxns') is not None:
            self.max_client_cnxns = m.get('MaxClientCnxns')
        if m.get('MaxSessionTimeout') is not None:
            self.max_session_timeout = m.get('MaxSessionTimeout')
        if m.get('MinSessionTimeout') is not None:
            self.min_session_timeout = m.get('MinSessionTimeout')
        if m.get('NamingCreateServiceSupported') is not None:
            self.naming_create_service_supported = m.get('NamingCreateServiceSupported')
        if m.get('OpenSuperAcl') is not None:
            self.open_super_acl = m.get('OpenSuperAcl')
        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')
        if m.get('RestartFlag') is not None:
            self.restart_flag = m.get('RestartFlag')
        if m.get('SyncLimit') is not None:
            self.sync_limit = m.get('SyncLimit')
        if m.get('TickTime') is not None:
            self.tick_time = m.get('TickTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryConfigResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = QueryConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGatewayRegionRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class QueryGatewayRegionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[str] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGatewayRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGatewayRegionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryGatewayRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGatewayTypeRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class QueryGatewayTypeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[str] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGatewayTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGatewayTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryGatewayTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGovernanceKubernetesClusterRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryGovernanceKubernetesClusterResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        k_8s_version: str = None,
        namespace_infos: str = None,
        pilot_start_time: str = None,
        region: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.k_8s_version = k_8s_version
        self.namespace_infos = namespace_infos
        self.pilot_start_time = pilot_start_time
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.k_8s_version is not None:
            result['K8sVersion'] = self.k_8s_version
        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos
        if self.pilot_start_time is not None:
            result['PilotStartTime'] = self.pilot_start_time
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('K8sVersion') is not None:
            self.k_8s_version = m.get('K8sVersion')
        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')
        if m.get('PilotStartTime') is not None:
            self.pilot_start_time = m.get('PilotStartTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class QueryGovernanceKubernetesClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[QueryGovernanceKubernetesClusterResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.result = result
        self.total_size = total_size

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
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
            for k in m.get('Result'):
                temp_model = QueryGovernanceKubernetesClusterResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class QueryGovernanceKubernetesClusterResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryGovernanceKubernetesClusterResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = QueryGovernanceKubernetesClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGovernanceKubernetesClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGovernanceKubernetesClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryGovernanceKubernetesClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonitorRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        end_time: int = None,
        instance_id: str = None,
        monitor_type: str = None,
        request_pars: str = None,
        start_time: int = None,
        step: int = None,
    ):
        self.accept_language = accept_language
        self.end_time = end_time
        self.instance_id = instance_id
        self.monitor_type = monitor_type
        self.request_pars = request_pars
        self.start_time = start_time
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class QueryMonitorResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMonitorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySlbSpecRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class QuerySlbSpecResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        max_connection: str = None,
        name: str = None,
        new_connection_per_second: str = None,
        qps: str = None,
        spec: str = None,
    ):
        self.id = id
        self.max_connection = max_connection
        self.name = name
        self.new_connection_per_second = new_connection_per_second
        self.qps = qps
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection
        if self.name is not None:
            result['Name'] = self.name
        if self.new_connection_per_second is not None:
            result['NewConnectionPerSecond'] = self.new_connection_per_second
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewConnectionPerSecond') is not None:
            self.new_connection_per_second = m.get('NewConnectionPerSecond')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class QuerySlbSpecResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[QuerySlbSpecResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = QuerySlbSpecResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySlbSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySlbSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySlbSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryZnodeDetailRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        path: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.path = path
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class QueryZnodeDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        data: str = None,
        dir: bool = None,
        name: str = None,
        path: str = None,
    ):
        self.data = data
        self.dir = dir
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class QueryZnodeDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryZnodeDetailResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryZnodeDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryZnodeDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryZnodeDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryZnodeDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartClusterRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        instance_id: str = None,
        pod_name_list: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.instance_id = instance_id
        self.pod_name_list = pod_name_list
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pod_name_list is not None:
            result['PodNameList'] = self.pod_name_list
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PodNameList') is not None:
            self.pod_name_list = m.get('PodNameList')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class RestartClusterResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryClusterRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.instance_id = instance_id
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class RetryClusterResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RetryClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RetryClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RetryClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScalingClusterRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_specification: str = None,
        cpu: int = None,
        instance_count: int = None,
        instance_id: str = None,
        memory_capacity: int = None,
    ):
        self.accept_language = accept_language
        self.cluster_specification = cluster_specification
        self.cpu = cpu
        self.instance_count = instance_count
        self.instance_id = instance_id
        self.memory_capacity = memory_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        return self


class ScalingClusterResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScalingClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ScalingClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ScalingClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SelectGatewaySlbRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SelectGatewaySlbResponseBodyData(TeaModel):
    def __init__(
        self,
        slb_id: str = None,
        slb_name: str = None,
    ):
        self.slb_id = slb_id
        self.slb_name = slb_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_name is not None:
            result['SlbName'] = self.slb_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbName') is not None:
            self.slb_name = m.get('SlbName')
        return self


class SelectGatewaySlbResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[SelectGatewaySlbResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = SelectGatewaySlbResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SelectGatewaySlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SelectGatewaySlbResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SelectGatewaySlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAclRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        acl_entry_list: str = None,
        instance_id: str = None,
    ):
        self.accept_language = accept_language
        self.acl_entry_list = acl_entry_list
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.acl_entry_list is not None:
            result['AclEntryList'] = self.acl_entry_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AclEntryList') is not None:
            self.acl_entry_list = m.get('AclEntryList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateAclResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAclResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBlackWhiteListRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        content: str = None,
        gateway_unique_id: str = None,
        id: int = None,
        resource_type: str = None,
        status: str = None,
        type: str = None,
    ):
        self.accept_language = accept_language
        self.content = content
        self.gateway_unique_id = gateway_unique_id
        self.id = id
        self.resource_type = resource_type
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.content is not None:
            result['Content'] = self.content
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateBlackWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateBlackWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateBlackWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateBlackWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_alias_name: str = None,
        instance_id: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_alias_name = cluster_alias_name
        self.instance_id = instance_id
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class UpdateClusterResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        autopurge_purge_interval: str = None,
        autopurge_snap_retain_count: str = None,
        cluster_id: str = None,
        config_auth_enabled: bool = None,
        config_secret_enabled: bool = None,
        config_type: str = None,
        init_limit: str = None,
        instance_id: str = None,
        jute_maxbuffer: str = None,
        mcpenabled: bool = None,
        max_client_cnxns: str = None,
        max_session_timeout: str = None,
        min_session_timeout: str = None,
        open_super_acl: str = None,
        pass_word: str = None,
        request_pars: str = None,
        sync_limit: str = None,
        tick_time: str = None,
        user_name: str = None,
    ):
        self.accept_language = accept_language
        self.autopurge_purge_interval = autopurge_purge_interval
        self.autopurge_snap_retain_count = autopurge_snap_retain_count
        self.cluster_id = cluster_id
        self.config_auth_enabled = config_auth_enabled
        self.config_secret_enabled = config_secret_enabled
        self.config_type = config_type
        self.init_limit = init_limit
        self.instance_id = instance_id
        self.jute_maxbuffer = jute_maxbuffer
        self.mcpenabled = mcpenabled
        self.max_client_cnxns = max_client_cnxns
        # 最大超时时间
        self.max_session_timeout = max_session_timeout
        # 最小超时时间
        self.min_session_timeout = min_session_timeout
        self.open_super_acl = open_super_acl
        self.pass_word = pass_word
        self.request_pars = request_pars
        self.sync_limit = sync_limit
        self.tick_time = tick_time
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.autopurge_purge_interval is not None:
            result['AutopurgePurgeInterval'] = self.autopurge_purge_interval
        if self.autopurge_snap_retain_count is not None:
            result['AutopurgeSnapRetainCount'] = self.autopurge_snap_retain_count
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.config_auth_enabled is not None:
            result['ConfigAuthEnabled'] = self.config_auth_enabled
        if self.config_secret_enabled is not None:
            result['ConfigSecretEnabled'] = self.config_secret_enabled
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.init_limit is not None:
            result['InitLimit'] = self.init_limit
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.jute_maxbuffer is not None:
            result['JuteMaxbuffer'] = self.jute_maxbuffer
        if self.mcpenabled is not None:
            result['MCPEnabled'] = self.mcpenabled
        if self.max_client_cnxns is not None:
            result['MaxClientCnxns'] = self.max_client_cnxns
        if self.max_session_timeout is not None:
            result['MaxSessionTimeout'] = self.max_session_timeout
        if self.min_session_timeout is not None:
            result['MinSessionTimeout'] = self.min_session_timeout
        if self.open_super_acl is not None:
            result['OpenSuperAcl'] = self.open_super_acl
        if self.pass_word is not None:
            result['PassWord'] = self.pass_word
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.sync_limit is not None:
            result['SyncLimit'] = self.sync_limit
        if self.tick_time is not None:
            result['TickTime'] = self.tick_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AutopurgePurgeInterval') is not None:
            self.autopurge_purge_interval = m.get('AutopurgePurgeInterval')
        if m.get('AutopurgeSnapRetainCount') is not None:
            self.autopurge_snap_retain_count = m.get('AutopurgeSnapRetainCount')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConfigAuthEnabled') is not None:
            self.config_auth_enabled = m.get('ConfigAuthEnabled')
        if m.get('ConfigSecretEnabled') is not None:
            self.config_secret_enabled = m.get('ConfigSecretEnabled')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('InitLimit') is not None:
            self.init_limit = m.get('InitLimit')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JuteMaxbuffer') is not None:
            self.jute_maxbuffer = m.get('JuteMaxbuffer')
        if m.get('MCPEnabled') is not None:
            self.mcpenabled = m.get('MCPEnabled')
        if m.get('MaxClientCnxns') is not None:
            self.max_client_cnxns = m.get('MaxClientCnxns')
        if m.get('MaxSessionTimeout') is not None:
            self.max_session_timeout = m.get('MaxSessionTimeout')
        if m.get('MinSessionTimeout') is not None:
            self.min_session_timeout = m.get('MinSessionTimeout')
        if m.get('OpenSuperAcl') is not None:
            self.open_super_acl = m.get('OpenSuperAcl')
        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('SyncLimit') is not None:
            self.sync_limit = m.get('SyncLimit')
        if m.get('TickTime') is not None:
            self.tick_time = m.get('TickTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class UpdateConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEngineNamespaceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        desc: str = None,
        id: str = None,
        instance_id: str = None,
        name: str = None,
        service_count: int = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.desc = desc
        self.id = id
        self.instance_id = instance_id
        self.name = name
        self.service_count = service_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        return self


class UpdateEngineNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        config_count: int = None,
        namespace: str = None,
        namespace_desc: str = None,
        namespace_show_name: str = None,
        quota: int = None,
        type: int = None,
    ):
        self.config_count = config_count
        self.namespace = namespace
        self.namespace_desc = namespace_desc
        self.namespace_show_name = namespace_show_name
        self.quota = quota
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateEngineNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateEngineNamespaceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateEngineNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEngineNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEngineNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayDomainRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cert_identifier: str = None,
        gateway_unique_id: str = None,
        id: int = None,
        must_https: bool = None,
        protocol: str = None,
    ):
        self.accept_language = accept_language
        self.cert_identifier = cert_identifier
        self.gateway_unique_id = gateway_unique_id
        self.id = id
        self.must_https = must_https
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        if self.must_https is not None:
            result['MustHttps'] = self.must_https
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class UpdateGatewayDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGatewayDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateGatewayDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayNameRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        name: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateGatewayNameResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGatewayNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateGatewayNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayOptionRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_id: int = None,
        gateway_option: GatewayOption = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_id = gateway_id
        self.gateway_option = gateway_option
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        if self.gateway_option:
            self.gateway_option.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_option is not None:
            result['GatewayOption'] = self.gateway_option.to_map()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayOption') is not None:
            temp_model = GatewayOption()
            self.gateway_option = temp_model.from_map(m['GatewayOption'])
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class UpdateGatewayOptionShrinkRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_id: int = None,
        gateway_option_shrink: str = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_id = gateway_id
        self.gateway_option_shrink = gateway_option_shrink
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_option_shrink is not None:
            result['GatewayOption'] = self.gateway_option_shrink
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayOption') is not None:
            self.gateway_option_shrink = m.get('GatewayOption')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class UpdateGatewayOptionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GatewayOption = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GatewayOption()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayOptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGatewayOptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateGatewayOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayRouteHTTPRewriteRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        http_rewrite_json: str = None,
        id: int = None,
    ):
        self.accept_language = accept_language
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.http_rewrite_json = http_rewrite_json
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.http_rewrite_json is not None:
            result['HttpRewriteJSON'] = self.http_rewrite_json
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('HttpRewriteJSON') is not None:
            self.http_rewrite_json = m.get('HttpRewriteJSON')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateGatewayRouteHTTPRewriteResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayRouteHTTPRewriteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGatewayRouteHTTPRewriteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateGatewayRouteHTTPRewriteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayServiceVersionRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        service_id: int = None,
        service_version: str = None,
    ):
        self.accept_language = accept_language
        self.gateway_unique_id = gateway_unique_id
        self.service_id = service_id
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class UpdateGatewayServiceVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayServiceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGatewayServiceVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateGatewayServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        version_code: str = None,
    ):
        self.accept_language = accept_language
        # 目标集群的id
        self.cluster_id = cluster_id
        # 想修改的镜像版本code
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        return self


class UpdateImageResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosClusterRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        check_port: int = None,
        cluster_name: str = None,
        group_name: str = None,
        health_checker: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        service_name: str = None,
        use_instance_port_for_check: bool = None,
    ):
        self.accept_language = accept_language
        # 健康检查端口
        self.check_port = check_port
        # Nacos集群名
        self.cluster_name = cluster_name
        # 分组名
        self.group_name = group_name
        # 健康检查类型
        self.health_checker = health_checker
        # 实例id
        self.instance_id = instance_id
        # 命名空间id
        self.namespace_id = namespace_id
        # 服务名
        self.service_name = service_name
        # 是否使用实例端口进行健康检查
        self.use_instance_port_for_check = use_instance_port_for_check

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.check_port is not None:
            result['CheckPort'] = self.check_port
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.health_checker is not None:
            result['HealthChecker'] = self.health_checker
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.use_instance_port_for_check is not None:
            result['UseInstancePortForCheck'] = self.use_instance_port_for_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CheckPort') is not None:
            self.check_port = m.get('CheckPort')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HealthChecker') is not None:
            self.health_checker = m.get('HealthChecker')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('UseInstancePortForCheck') is not None:
            self.use_instance_port_for_check = m.get('UseInstancePortForCheck')
        return self


class UpdateNacosClusterResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 响应码
        self.code = code
        # 修改结果
        self.data = data
        # http状态码
        self.http_status_code = http_status_code
        # 响应信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 成功标志
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNacosClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNacosClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNacosClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        beta_ips: str = None,
        content: str = None,
        data_id: str = None,
        desc: str = None,
        encrypted_data_key: str = None,
        group: str = None,
        instance_id: str = None,
        md_5: str = None,
        namespace_id: str = None,
        tags: str = None,
        type: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.beta_ips = beta_ips
        self.content = content
        self.data_id = data_id
        self.desc = desc
        self.encrypted_data_key = encrypted_data_key
        self.group = group
        self.instance_id = instance_id
        self.md_5 = md_5
        self.namespace_id = namespace_id
        self.tags = tags
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.encrypted_data_key is not None:
            result['EncryptedDataKey'] = self.encrypted_data_key
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('EncryptedDataKey') is not None:
            self.encrypted_data_key = m.get('EncryptedDataKey')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosInstanceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_name: str = None,
        enabled: bool = None,
        ephemeral: bool = None,
        group_name: str = None,
        instance_id: str = None,
        ip: str = None,
        metadata: str = None,
        namespace_id: str = None,
        port: int = None,
        service_name: str = None,
        weight: str = None,
    ):
        self.accept_language = accept_language
        # Nacos集群名
        self.cluster_name = cluster_name
        # 服务禁用标志
        self.enabled = enabled
        # 临时节点标志
        self.ephemeral = ephemeral
        # 分组名
        self.group_name = group_name
        # 实例id
        self.instance_id = instance_id
        # Nacos实例ip
        self.ip = ip
        # 节点元数据
        self.metadata = metadata
        # 命名空间id
        self.namespace_id = namespace_id
        # Nacos实例端口
        self.port = port
        # 服务名
        self.service_name = service_name
        # 权重
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.port is not None:
            result['Port'] = self.port
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateNacosInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 响应码
        self.code = code
        # 修改结果
        self.data = data
        # http状态码
        self.http_status_code = http_status_code
        # 响应信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 成功标志
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNacosInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNacosInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNacosInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosServiceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        group_name: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        protect_threshold: str = None,
        service_name: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.group_name = group_name
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.protect_threshold = protect_threshold
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.protect_threshold is not None:
            result['ProtectThreshold'] = self.protect_threshold
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ProtectThreshold') is not None:
            self.protect_threshold = m.get('ProtectThreshold')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class UpdateNacosServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNacosServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNacosServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNacosServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSSLCertRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cert_identifier: str = None,
        domain_id: int = None,
        gateway_unique_id: str = None,
    ):
        self.accept_language = accept_language
        self.cert_identifier = cert_identifier
        self.domain_id = domain_id
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class UpdateSSLCertResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSSLCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSSLCertResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSSLCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateZnodeRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        data: str = None,
        path: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        self.cluster_id = cluster_id
        self.data = data
        self.path = path
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class UpdateZnodeResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateZnodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateZnodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClusterRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        request_pars: str = None,
        upgrade_version: str = None,
    ):
        self.accept_language = accept_language
        self.instance_id = instance_id
        self.request_pars = request_pars
        self.upgrade_version = upgrade_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.upgrade_version is not None:
            result['UpgradeVersion'] = self.upgrade_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('UpgradeVersion') is not None:
            self.upgrade_version = m.get('UpgradeVersion')
        return self


class UpgradeClusterResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


