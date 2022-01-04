# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddBuiltinEnvoyFilterRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        istio_version: str = None,
        name: str = None,
        parameters: str = None,
        service_mesh_id: str = None,
    ):
        self.id = id
        self.istio_version = istio_version
        self.name = name
        self.parameters = parameters
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class AddBuiltinEnvoyFilterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddBuiltinEnvoyFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddBuiltinEnvoyFilterResponseBody = None,
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
            temp_model = AddBuiltinEnvoyFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddClusterIntoServiceMeshRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        service_mesh_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class AddClusterIntoServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddClusterIntoServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddClusterIntoServiceMeshResponseBody = None,
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
            temp_model = AddClusterIntoServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMeshTagToEcsRequest(TeaModel):
    def __init__(
        self,
        ecs_id: str = None,
        service_mesh_id: str = None,
    ):
        self.ecs_id = ecs_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class AddMeshTagToEcsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddMeshTagToEcsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddMeshTagToEcsResponseBody = None,
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
            temp_model = AddMeshTagToEcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVMIntoServiceMeshRequest(TeaModel):
    def __init__(
        self,
        ecs_id: str = None,
        service_mesh_id: str = None,
    ):
        self.ecs_id = ecs_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class AddVMIntoServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddVMIntoServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddVMIntoServiceMeshResponseBody = None,
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
            temp_model = AddVMIntoServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExtensionProviderRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        service_mesh_id: str = None,
        type: str = None,
    ):
        self.config = config
        self.name = name
        self.service_mesh_id = service_mesh_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateExtensionProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExtensionProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateExtensionProviderResponseBody = None,
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
            temp_model = CreateExtensionProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceMeshRequest(TeaModel):
    def __init__(
        self,
        access_log_enabled: bool = None,
        access_log_file: str = None,
        access_log_format: str = None,
        access_log_project: str = None,
        access_log_service_enabled: bool = None,
        access_log_service_host: str = None,
        access_log_service_port: int = None,
        api_server_public_eip: bool = None,
        audit_project: str = None,
        craggregation_enabled: bool = None,
        config_source_enabled: bool = None,
        config_source_nacos_id: str = None,
        control_plane_log_enabled: bool = None,
        control_plane_log_project: str = None,
        customized_prometheus: bool = None,
        customized_zipkin: bool = None,
        dnsproxying_enabled: bool = None,
        dubbo_filter_enabled: bool = None,
        edition: str = None,
        enable_audit: bool = None,
        enable_crhistory: bool = None,
        enable_sdsserver: bool = None,
        exclude_ipranges: str = None,
        exclude_inbound_ports: str = None,
        exclude_outbound_ports: str = None,
        filter_gateway_cluster_config: bool = None,
        gateway_apienabled: bool = None,
        include_ipranges: str = None,
        istio_version: str = None,
        kiali_enabled: bool = None,
        locality_lbconf: str = None,
        locality_load_balancing: bool = None,
        mseenabled: bool = None,
        mysql_filter_enabled: bool = None,
        name: str = None,
        opalimit_cpu: str = None,
        opalimit_memory: str = None,
        opalog_level: str = None,
        oparequest_cpu: str = None,
        oparequest_memory: str = None,
        opa_enabled: bool = None,
        open_agent_policy: bool = None,
        prometheus_url: str = None,
        proxy_limit_cpu: str = None,
        proxy_limit_memory: str = None,
        proxy_request_cpu: str = None,
        proxy_request_memory: str = None,
        redis_filter_enabled: bool = None,
        region_id: str = None,
        telemetry: bool = None,
        thrift_filter_enabled: bool = None,
        trace_sampling: float = None,
        tracing: bool = None,
        v_switches: str = None,
        vpc_id: str = None,
        web_assembly_filter_enabled: bool = None,
    ):
        self.access_log_enabled = access_log_enabled
        self.access_log_file = access_log_file
        self.access_log_format = access_log_format
        self.access_log_project = access_log_project
        self.access_log_service_enabled = access_log_service_enabled
        self.access_log_service_host = access_log_service_host
        self.access_log_service_port = access_log_service_port
        self.api_server_public_eip = api_server_public_eip
        self.audit_project = audit_project
        self.craggregation_enabled = craggregation_enabled
        self.config_source_enabled = config_source_enabled
        self.config_source_nacos_id = config_source_nacos_id
        self.control_plane_log_enabled = control_plane_log_enabled
        self.control_plane_log_project = control_plane_log_project
        self.customized_prometheus = customized_prometheus
        self.customized_zipkin = customized_zipkin
        self.dnsproxying_enabled = dnsproxying_enabled
        self.dubbo_filter_enabled = dubbo_filter_enabled
        self.edition = edition
        self.enable_audit = enable_audit
        self.enable_crhistory = enable_crhistory
        self.enable_sdsserver = enable_sdsserver
        self.exclude_ipranges = exclude_ipranges
        self.exclude_inbound_ports = exclude_inbound_ports
        self.exclude_outbound_ports = exclude_outbound_ports
        self.filter_gateway_cluster_config = filter_gateway_cluster_config
        self.gateway_apienabled = gateway_apienabled
        self.include_ipranges = include_ipranges
        self.istio_version = istio_version
        self.kiali_enabled = kiali_enabled
        self.locality_lbconf = locality_lbconf
        self.locality_load_balancing = locality_load_balancing
        self.mseenabled = mseenabled
        self.mysql_filter_enabled = mysql_filter_enabled
        self.name = name
        self.opalimit_cpu = opalimit_cpu
        self.opalimit_memory = opalimit_memory
        self.opalog_level = opalog_level
        self.oparequest_cpu = oparequest_cpu
        self.oparequest_memory = oparequest_memory
        self.opa_enabled = opa_enabled
        self.open_agent_policy = open_agent_policy
        self.prometheus_url = prometheus_url
        self.proxy_limit_cpu = proxy_limit_cpu
        self.proxy_limit_memory = proxy_limit_memory
        self.proxy_request_cpu = proxy_request_cpu
        self.proxy_request_memory = proxy_request_memory
        self.redis_filter_enabled = redis_filter_enabled
        self.region_id = region_id
        self.telemetry = telemetry
        self.thrift_filter_enabled = thrift_filter_enabled
        self.trace_sampling = trace_sampling
        self.tracing = tracing
        self.v_switches = v_switches
        self.vpc_id = vpc_id
        self.web_assembly_filter_enabled = web_assembly_filter_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_enabled is not None:
            result['AccessLogEnabled'] = self.access_log_enabled
        if self.access_log_file is not None:
            result['AccessLogFile'] = self.access_log_file
        if self.access_log_format is not None:
            result['AccessLogFormat'] = self.access_log_format
        if self.access_log_project is not None:
            result['AccessLogProject'] = self.access_log_project
        if self.access_log_service_enabled is not None:
            result['AccessLogServiceEnabled'] = self.access_log_service_enabled
        if self.access_log_service_host is not None:
            result['AccessLogServiceHost'] = self.access_log_service_host
        if self.access_log_service_port is not None:
            result['AccessLogServicePort'] = self.access_log_service_port
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.audit_project is not None:
            result['AuditProject'] = self.audit_project
        if self.craggregation_enabled is not None:
            result['CRAggregationEnabled'] = self.craggregation_enabled
        if self.config_source_enabled is not None:
            result['ConfigSourceEnabled'] = self.config_source_enabled
        if self.config_source_nacos_id is not None:
            result['ConfigSourceNacosID'] = self.config_source_nacos_id
        if self.control_plane_log_enabled is not None:
            result['ControlPlaneLogEnabled'] = self.control_plane_log_enabled
        if self.control_plane_log_project is not None:
            result['ControlPlaneLogProject'] = self.control_plane_log_project
        if self.customized_prometheus is not None:
            result['CustomizedPrometheus'] = self.customized_prometheus
        if self.customized_zipkin is not None:
            result['CustomizedZipkin'] = self.customized_zipkin
        if self.dnsproxying_enabled is not None:
            result['DNSProxyingEnabled'] = self.dnsproxying_enabled
        if self.dubbo_filter_enabled is not None:
            result['DubboFilterEnabled'] = self.dubbo_filter_enabled
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
        if self.enable_crhistory is not None:
            result['EnableCRHistory'] = self.enable_crhistory
        if self.enable_sdsserver is not None:
            result['EnableSDSServer'] = self.enable_sdsserver
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.filter_gateway_cluster_config is not None:
            result['FilterGatewayClusterConfig'] = self.filter_gateway_cluster_config
        if self.gateway_apienabled is not None:
            result['GatewayAPIEnabled'] = self.gateway_apienabled
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.kiali_enabled is not None:
            result['KialiEnabled'] = self.kiali_enabled
        if self.locality_lbconf is not None:
            result['LocalityLBConf'] = self.locality_lbconf
        if self.locality_load_balancing is not None:
            result['LocalityLoadBalancing'] = self.locality_load_balancing
        if self.mseenabled is not None:
            result['MSEEnabled'] = self.mseenabled
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.opalimit_cpu is not None:
            result['OPALimitCPU'] = self.opalimit_cpu
        if self.opalimit_memory is not None:
            result['OPALimitMemory'] = self.opalimit_memory
        if self.opalog_level is not None:
            result['OPALogLevel'] = self.opalog_level
        if self.oparequest_cpu is not None:
            result['OPARequestCPU'] = self.oparequest_cpu
        if self.oparequest_memory is not None:
            result['OPARequestMemory'] = self.oparequest_memory
        if self.opa_enabled is not None:
            result['OpaEnabled'] = self.opa_enabled
        if self.open_agent_policy is not None:
            result['OpenAgentPolicy'] = self.open_agent_policy
        if self.prometheus_url is not None:
            result['PrometheusUrl'] = self.prometheus_url
        if self.proxy_limit_cpu is not None:
            result['ProxyLimitCPU'] = self.proxy_limit_cpu
        if self.proxy_limit_memory is not None:
            result['ProxyLimitMemory'] = self.proxy_limit_memory
        if self.proxy_request_cpu is not None:
            result['ProxyRequestCPU'] = self.proxy_request_cpu
        if self.proxy_request_memory is not None:
            result['ProxyRequestMemory'] = self.proxy_request_memory
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.web_assembly_filter_enabled is not None:
            result['WebAssemblyFilterEnabled'] = self.web_assembly_filter_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogEnabled') is not None:
            self.access_log_enabled = m.get('AccessLogEnabled')
        if m.get('AccessLogFile') is not None:
            self.access_log_file = m.get('AccessLogFile')
        if m.get('AccessLogFormat') is not None:
            self.access_log_format = m.get('AccessLogFormat')
        if m.get('AccessLogProject') is not None:
            self.access_log_project = m.get('AccessLogProject')
        if m.get('AccessLogServiceEnabled') is not None:
            self.access_log_service_enabled = m.get('AccessLogServiceEnabled')
        if m.get('AccessLogServiceHost') is not None:
            self.access_log_service_host = m.get('AccessLogServiceHost')
        if m.get('AccessLogServicePort') is not None:
            self.access_log_service_port = m.get('AccessLogServicePort')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        if m.get('AuditProject') is not None:
            self.audit_project = m.get('AuditProject')
        if m.get('CRAggregationEnabled') is not None:
            self.craggregation_enabled = m.get('CRAggregationEnabled')
        if m.get('ConfigSourceEnabled') is not None:
            self.config_source_enabled = m.get('ConfigSourceEnabled')
        if m.get('ConfigSourceNacosID') is not None:
            self.config_source_nacos_id = m.get('ConfigSourceNacosID')
        if m.get('ControlPlaneLogEnabled') is not None:
            self.control_plane_log_enabled = m.get('ControlPlaneLogEnabled')
        if m.get('ControlPlaneLogProject') is not None:
            self.control_plane_log_project = m.get('ControlPlaneLogProject')
        if m.get('CustomizedPrometheus') is not None:
            self.customized_prometheus = m.get('CustomizedPrometheus')
        if m.get('CustomizedZipkin') is not None:
            self.customized_zipkin = m.get('CustomizedZipkin')
        if m.get('DNSProxyingEnabled') is not None:
            self.dnsproxying_enabled = m.get('DNSProxyingEnabled')
        if m.get('DubboFilterEnabled') is not None:
            self.dubbo_filter_enabled = m.get('DubboFilterEnabled')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
        if m.get('EnableCRHistory') is not None:
            self.enable_crhistory = m.get('EnableCRHistory')
        if m.get('EnableSDSServer') is not None:
            self.enable_sdsserver = m.get('EnableSDSServer')
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('FilterGatewayClusterConfig') is not None:
            self.filter_gateway_cluster_config = m.get('FilterGatewayClusterConfig')
        if m.get('GatewayAPIEnabled') is not None:
            self.gateway_apienabled = m.get('GatewayAPIEnabled')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('KialiEnabled') is not None:
            self.kiali_enabled = m.get('KialiEnabled')
        if m.get('LocalityLBConf') is not None:
            self.locality_lbconf = m.get('LocalityLBConf')
        if m.get('LocalityLoadBalancing') is not None:
            self.locality_load_balancing = m.get('LocalityLoadBalancing')
        if m.get('MSEEnabled') is not None:
            self.mseenabled = m.get('MSEEnabled')
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OPALimitCPU') is not None:
            self.opalimit_cpu = m.get('OPALimitCPU')
        if m.get('OPALimitMemory') is not None:
            self.opalimit_memory = m.get('OPALimitMemory')
        if m.get('OPALogLevel') is not None:
            self.opalog_level = m.get('OPALogLevel')
        if m.get('OPARequestCPU') is not None:
            self.oparequest_cpu = m.get('OPARequestCPU')
        if m.get('OPARequestMemory') is not None:
            self.oparequest_memory = m.get('OPARequestMemory')
        if m.get('OpaEnabled') is not None:
            self.opa_enabled = m.get('OpaEnabled')
        if m.get('OpenAgentPolicy') is not None:
            self.open_agent_policy = m.get('OpenAgentPolicy')
        if m.get('PrometheusUrl') is not None:
            self.prometheus_url = m.get('PrometheusUrl')
        if m.get('ProxyLimitCPU') is not None:
            self.proxy_limit_cpu = m.get('ProxyLimitCPU')
        if m.get('ProxyLimitMemory') is not None:
            self.proxy_limit_memory = m.get('ProxyLimitMemory')
        if m.get('ProxyRequestCPU') is not None:
            self.proxy_request_cpu = m.get('ProxyRequestCPU')
        if m.get('ProxyRequestMemory') is not None:
            self.proxy_request_memory = m.get('ProxyRequestMemory')
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WebAssemblyFilterEnabled') is not None:
            self.web_assembly_filter_enabled = m.get('WebAssemblyFilterEnabled')
        return self


class CreateServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_mesh_id: str = None,
    ):
        self.request_id = request_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class CreateServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceMeshResponseBody = None,
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
            temp_model = CreateServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExtensionProviderRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        service_mesh_id: str = None,
        type: str = None,
    ):
        self.name = name
        self.service_mesh_id = service_mesh_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DeleteExtensionProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteExtensionProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteExtensionProviderResponseBody = None,
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
            temp_model = DeleteExtensionProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceMeshRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        retain_resources: str = None,
        service_mesh_id: str = None,
    ):
        self.force = force
        self.retain_resources = retain_resources
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DeleteServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServiceMeshResponseBody = None,
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
            temp_model = DeleteServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertActionPoliciesRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
    ):
        self.page = page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class DescribeAlertActionPoliciesResponseBodyActionPolicyList(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeAlertActionPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        action_policy_list: List[DescribeAlertActionPoliciesResponseBodyActionPolicyList] = None,
        page_total: int = None,
        request_id: str = None,
    ):
        self.action_policy_list = action_policy_list
        self.page_total = page_total
        self.request_id = request_id

    def validate(self):
        if self.action_policy_list:
            for k in self.action_policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActionPolicyList'] = []
        if self.action_policy_list is not None:
            for k in self.action_policy_list:
                result['ActionPolicyList'].append(k.to_map() if k else None)
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_policy_list = []
        if m.get('ActionPolicyList') is not None:
            for k in m.get('ActionPolicyList'):
                temp_model = DescribeAlertActionPoliciesResponseBodyActionPolicyList()
                self.action_policy_list.append(temp_model.from_map(k))
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAlertActionPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAlertActionPoliciesResponseBody = None,
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
            temp_model = DescribeAlertActionPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableNacosInstancesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
    ):
        self.region_id = region_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeAvailableNacosInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableNacosInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAvailableNacosInstancesResponseBody = None,
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
            temp_model = DescribeAvailableNacosInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCensRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeCensResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[str] = None,
        request_id: str = None,
    ):
        self.clusters = clusters
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCensResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCensResponseBody = None,
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
            temp_model = DescribeCensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterGrafanaRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
        service_mesh_id: str = None,
    ):
        self.k_8s_cluster_id = k_8s_cluster_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeClusterGrafanaResponseBodyDashboards(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeClusterGrafanaResponseBody(TeaModel):
    def __init__(
        self,
        dashboards: List[DescribeClusterGrafanaResponseBodyDashboards] = None,
        request_id: str = None,
    ):
        self.dashboards = dashboards
        self.request_id = request_id

    def validate(self):
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k in m.get('Dashboards'):
                temp_model = DescribeClusterGrafanaResponseBodyDashboards()
                self.dashboards.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterGrafanaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClusterGrafanaResponseBody = None,
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
            temp_model = DescribeClusterGrafanaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterPrometheusRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
        k_8s_cluster_region_id: str = None,
        service_mesh_id: str = None,
    ):
        self.k_8s_cluster_id = k_8s_cluster_id
        self.k_8s_cluster_region_id = k_8s_cluster_region_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.k_8s_cluster_region_id is not None:
            result['K8sClusterRegionId'] = self.k_8s_cluster_region_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('K8sClusterRegionId') is not None:
            self.k_8s_cluster_region_id = m.get('K8sClusterRegionId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeClusterPrometheusResponseBody(TeaModel):
    def __init__(
        self,
        prometheus: str = None,
        request_id: str = None,
    ):
        self.prometheus = prometheus
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus is not None:
            result['Prometheus'] = self.prometheus
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prometheus') is not None:
            self.prometheus = m.get('Prometheus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterPrometheusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClusterPrometheusResponseBody = None,
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
            temp_model = DescribeClusterPrometheusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersInServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeClustersInServiceMeshResponseBodyClusters(TeaModel):
    def __init__(
        self,
        access_log_dashboards: List[DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards] = None,
        cluster_domain: str = None,
        cluster_id: str = None,
        cluster_type: str = None,
        creation_time: str = None,
        error_message: str = None,
        logtail_installed_state: str = None,
        name: str = None,
        region_id: str = None,
        sg_id: str = None,
        state: str = None,
        update_time: str = None,
        version: str = None,
        vpc_id: str = None,
    ):
        self.access_log_dashboards = access_log_dashboards
        self.cluster_domain = cluster_domain
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.creation_time = creation_time
        self.error_message = error_message
        self.logtail_installed_state = logtail_installed_state
        self.name = name
        self.region_id = region_id
        self.sg_id = sg_id
        self.state = state
        self.update_time = update_time
        self.version = version
        self.vpc_id = vpc_id

    def validate(self):
        if self.access_log_dashboards:
            for k in self.access_log_dashboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessLogDashboards'] = []
        if self.access_log_dashboards is not None:
            for k in self.access_log_dashboards:
                result['AccessLogDashboards'].append(k.to_map() if k else None)
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.logtail_installed_state is not None:
            result['LogtailInstalledState'] = self.logtail_installed_state
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sg_id is not None:
            result['SgId'] = self.sg_id
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_log_dashboards = []
        if m.get('AccessLogDashboards') is not None:
            for k in m.get('AccessLogDashboards'):
                temp_model = DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards()
                self.access_log_dashboards.append(temp_model.from_map(k))
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LogtailInstalledState') is not None:
            self.logtail_installed_state = m.get('LogtailInstalledState')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeClustersInServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[DescribeClustersInServiceMeshResponseBodyClusters] = None,
        request_id: str = None,
    ):
        self.clusters = clusters
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeClustersInServiceMeshResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClustersInServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClustersInServiceMeshResponseBody = None,
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
            temp_model = DescribeClustersInServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeControlPlaneLogAlertRulesRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeControlPlaneLogAlertRulesResponseBodyDataInfo(TeaModel):
    def __init__(
        self,
        description: str = None,
        title: str = None,
    ):
        self.description = description
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeControlPlaneLogAlertRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        action_policy_id: str = None,
        enabled: bool = None,
        info: DescribeControlPlaneLogAlertRulesResponseBodyDataInfo = None,
        rule_id: str = None,
    ):
        self.action_policy_id = action_policy_id
        self.enabled = enabled
        self.info = info
        self.rule_id = rule_id

    def validate(self):
        if self.info:
            self.info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_policy_id is not None:
            result['ActionPolicyId'] = self.action_policy_id
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.info is not None:
            result['Info'] = self.info.to_map()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPolicyId') is not None:
            self.action_policy_id = m.get('ActionPolicyId')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Info') is not None:
            temp_model = DescribeControlPlaneLogAlertRulesResponseBodyDataInfo()
            self.info = temp_model.from_map(m['Info'])
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeControlPlaneLogAlertRulesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeControlPlaneLogAlertRulesResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeControlPlaneLogAlertRulesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeControlPlaneLogAlertRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeControlPlaneLogAlertRulesResponseBody = None,
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
            temp_model = DescribeControlPlaneLogAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCrTemplatesRequest(TeaModel):
    def __init__(
        self,
        istio_version: str = None,
        kind: str = None,
    ):
        self.istio_version = istio_version
        self.kind = kind

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.kind is not None:
            result['Kind'] = self.kind
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        return self


class DescribeCrTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        chinese_name: str = None,
        english_name: str = None,
        yaml: str = None,
    ):
        self.chinese_name = chinese_name
        self.english_name = english_name
        self.yaml = yaml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chinese_name is not None:
            result['ChineseName'] = self.chinese_name
        if self.english_name is not None:
            result['EnglishName'] = self.english_name
        if self.yaml is not None:
            result['Yaml'] = self.yaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChineseName') is not None:
            self.chinese_name = m.get('ChineseName')
        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')
        if m.get('Yaml') is not None:
            self.yaml = m.get('Yaml')
        return self


class DescribeCrTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        templates: List[DescribeCrTemplatesResponseBodyTemplates] = None,
    ):
        self.request_id = request_id
        self.templates = templates

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = DescribeCrTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class DescribeCrTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCrTemplatesResponseBody = None,
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
            temp_model = DescribeCrTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExtensionProviderRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        type: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeExtensionProviderResponseBody(TeaModel):
    def __init__(
        self,
        extension_providers: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.extension_providers = extension_providers
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension_providers is not None:
            result['ExtensionProviders'] = self.extension_providers
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtensionProviders') is not None:
            self.extension_providers = m.get('ExtensionProviders')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeExtensionProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExtensionProviderResponseBody = None,
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
            temp_model = DescribeExtensionProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGuestClusterAccessLogDashboardsRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
    ):
        self.k_8s_cluster_id = k_8s_cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        return self


class DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeGuestClusterAccessLogDashboardsResponseBody(TeaModel):
    def __init__(
        self,
        dashboards: List[DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards] = None,
        k_8s_cluster_id: str = None,
        request_id: str = None,
    ):
        self.dashboards = dashboards
        self.k_8s_cluster_id = k_8s_cluster_id
        self.request_id = request_id

    def validate(self):
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k in m.get('Dashboards'):
                temp_model = DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards()
                self.dashboards.append(temp_model.from_map(k))
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGuestClusterAccessLogDashboardsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGuestClusterAccessLogDashboardsResponseBody = None,
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
            temp_model = DescribeGuestClusterAccessLogDashboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGuestClusterNamespacesRequest(TeaModel):
    def __init__(
        self,
        guest_cluster_id: str = None,
        service_mesh_id: str = None,
    ):
        self.guest_cluster_id = guest_cluster_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guest_cluster_id is not None:
            result['GuestClusterID'] = self.guest_cluster_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestClusterID') is not None:
            self.guest_cluster_id = m.get('GuestClusterID')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeGuestClusterNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        ns_list: List[str] = None,
        request_id: str = None,
    ):
        self.ns_list = ns_list
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ns_list is not None:
            result['NsList'] = self.ns_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NsList') is not None:
            self.ns_list = m.get('NsList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGuestClusterNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGuestClusterNamespacesResponseBody = None,
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
            temp_model = DescribeGuestClusterNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGuestClusterPodsRequest(TeaModel):
    def __init__(
        self,
        guest_cluster_id: str = None,
        namespace: str = None,
        service_mesh_id: str = None,
    ):
        self.guest_cluster_id = guest_cluster_id
        self.namespace = namespace
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guest_cluster_id is not None:
            result['GuestClusterID'] = self.guest_cluster_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestClusterID') is not None:
            self.guest_cluster_id = m.get('GuestClusterID')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeGuestClusterPodsResponseBody(TeaModel):
    def __init__(
        self,
        pod_list: List[str] = None,
        request_id: str = None,
    ):
        self.pod_list = pod_list
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pod_list is not None:
            result['PodList'] = self.pod_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PodList') is not None:
            self.pod_list = m.get('PodList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGuestClusterPodsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGuestClusterPodsResponseBody = None,
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
            temp_model = DescribeGuestClusterPodsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIngressGatewaysRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeIngressGatewaysResponseBody(TeaModel):
    def __init__(
        self,
        ingress_gateways: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.ingress_gateways = ingress_gateways
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_gateways is not None:
            result['IngressGateways'] = self.ingress_gateways
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressGateways') is not None:
            self.ingress_gateways = m.get('IngressGateways')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIngressGatewaysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIngressGatewaysResponseBody = None,
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
            temp_model = DescribeIngressGatewaysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceScopeSidecarConfigRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        service_mesh_id: str = None,
    ):
        self.namespace = namespace
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceLimit(TeaModel):
    def __init__(
        self,
        resource_cpulimit: str = None,
        resource_memory_limit: str = None,
    ):
        self.resource_cpulimit = resource_cpulimit
        self.resource_memory_limit = resource_memory_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpulimit is not None:
            result['ResourceCPULimit'] = self.resource_cpulimit
        if self.resource_memory_limit is not None:
            result['ResourceMemoryLimit'] = self.resource_memory_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPULimit') is not None:
            self.resource_cpulimit = m.get('ResourceCPULimit')
        if m.get('ResourceMemoryLimit') is not None:
            self.resource_memory_limit = m.get('ResourceMemoryLimit')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceRequest(TeaModel):
    def __init__(
        self,
        resource_cpurequest: str = None,
        resource_memory_request: str = None,
    ):
        self.resource_cpurequest = resource_cpurequest
        self.resource_memory_request = resource_memory_request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpurequest is not None:
            result['ResourceCPURequest'] = self.resource_cpurequest
        if self.resource_memory_request is not None:
            result['ResourceMemoryRequest'] = self.resource_memory_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPURequest') is not None:
            self.resource_cpurequest = m.get('ResourceCPURequest')
        if m.get('ResourceMemoryRequest') is not None:
            self.resource_memory_request = m.get('ResourceMemoryRequest')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceLimit(TeaModel):
    def __init__(
        self,
        resource_cpulimit: str = None,
        resource_memory_limit: str = None,
    ):
        self.resource_cpulimit = resource_cpulimit
        self.resource_memory_limit = resource_memory_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpulimit is not None:
            result['ResourceCPULimit'] = self.resource_cpulimit
        if self.resource_memory_limit is not None:
            result['ResourceMemoryLimit'] = self.resource_memory_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPULimit') is not None:
            self.resource_cpulimit = m.get('ResourceCPULimit')
        if m.get('ResourceMemoryLimit') is not None:
            self.resource_memory_limit = m.get('ResourceMemoryLimit')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceRequest(TeaModel):
    def __init__(
        self,
        resource_cpurequest: str = None,
        resource_memory_request: str = None,
    ):
        self.resource_cpurequest = resource_cpurequest
        self.resource_memory_request = resource_memory_request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpurequest is not None:
            result['ResourceCPURequest'] = self.resource_cpurequest
        if self.resource_memory_request is not None:
            result['ResourceMemoryRequest'] = self.resource_memory_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPURequest') is not None:
            self.resource_cpurequest = m.get('ResourceCPURequest')
        if m.get('ResourceMemoryRequest') is not None:
            self.resource_memory_request = m.get('ResourceMemoryRequest')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatches(TeaModel):
    def __init__(
        self,
        exclude_inbound_ports: str = None,
        exclude_outbound_ipranges: str = None,
        exclude_outbound_ports: str = None,
        include_inbound_ports: str = None,
        include_outbound_ipranges: str = None,
        include_outbound_ports: str = None,
        istio_dnsproxy_enabled: bool = None,
        lifecycle_str: str = None,
        sidecar_proxy_init_resource_limit: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceLimit = None,
        sidecar_proxy_init_resource_request: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceRequest = None,
        sidecar_proxy_resource_limit: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceLimit = None,
        sidecar_proxy_resource_request: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceRequest = None,
        termination_drain_duration: str = None,
    ):
        self.exclude_inbound_ports = exclude_inbound_ports
        self.exclude_outbound_ipranges = exclude_outbound_ipranges
        self.exclude_outbound_ports = exclude_outbound_ports
        self.include_inbound_ports = include_inbound_ports
        self.include_outbound_ipranges = include_outbound_ipranges
        self.include_outbound_ports = include_outbound_ports
        self.istio_dnsproxy_enabled = istio_dnsproxy_enabled
        self.lifecycle_str = lifecycle_str
        self.sidecar_proxy_init_resource_limit = sidecar_proxy_init_resource_limit
        self.sidecar_proxy_init_resource_request = sidecar_proxy_init_resource_request
        self.sidecar_proxy_resource_limit = sidecar_proxy_resource_limit
        self.sidecar_proxy_resource_request = sidecar_proxy_resource_request
        self.termination_drain_duration = termination_drain_duration

    def validate(self):
        if self.sidecar_proxy_init_resource_limit:
            self.sidecar_proxy_init_resource_limit.validate()
        if self.sidecar_proxy_init_resource_request:
            self.sidecar_proxy_init_resource_request.validate()
        if self.sidecar_proxy_resource_limit:
            self.sidecar_proxy_resource_limit.validate()
        if self.sidecar_proxy_resource_request:
            self.sidecar_proxy_resource_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ipranges is not None:
            result['ExcludeOutboundIPRanges'] = self.exclude_outbound_ipranges
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.include_inbound_ports is not None:
            result['IncludeInboundPorts'] = self.include_inbound_ports
        if self.include_outbound_ipranges is not None:
            result['IncludeOutboundIPRanges'] = self.include_outbound_ipranges
        if self.include_outbound_ports is not None:
            result['IncludeOutboundPorts'] = self.include_outbound_ports
        if self.istio_dnsproxy_enabled is not None:
            result['IstioDNSProxyEnabled'] = self.istio_dnsproxy_enabled
        if self.lifecycle_str is not None:
            result['LifecycleStr'] = self.lifecycle_str
        if self.sidecar_proxy_init_resource_limit is not None:
            result['SidecarProxyInitResourceLimit'] = self.sidecar_proxy_init_resource_limit.to_map()
        if self.sidecar_proxy_init_resource_request is not None:
            result['SidecarProxyInitResourceRequest'] = self.sidecar_proxy_init_resource_request.to_map()
        if self.sidecar_proxy_resource_limit is not None:
            result['SidecarProxyResourceLimit'] = self.sidecar_proxy_resource_limit.to_map()
        if self.sidecar_proxy_resource_request is not None:
            result['SidecarProxyResourceRequest'] = self.sidecar_proxy_resource_request.to_map()
        if self.termination_drain_duration is not None:
            result['TerminationDrainDuration'] = self.termination_drain_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundIPRanges') is not None:
            self.exclude_outbound_ipranges = m.get('ExcludeOutboundIPRanges')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('IncludeInboundPorts') is not None:
            self.include_inbound_ports = m.get('IncludeInboundPorts')
        if m.get('IncludeOutboundIPRanges') is not None:
            self.include_outbound_ipranges = m.get('IncludeOutboundIPRanges')
        if m.get('IncludeOutboundPorts') is not None:
            self.include_outbound_ports = m.get('IncludeOutboundPorts')
        if m.get('IstioDNSProxyEnabled') is not None:
            self.istio_dnsproxy_enabled = m.get('IstioDNSProxyEnabled')
        if m.get('LifecycleStr') is not None:
            self.lifecycle_str = m.get('LifecycleStr')
        if m.get('SidecarProxyInitResourceLimit') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceLimit()
            self.sidecar_proxy_init_resource_limit = temp_model.from_map(m['SidecarProxyInitResourceLimit'])
        if m.get('SidecarProxyInitResourceRequest') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceRequest()
            self.sidecar_proxy_init_resource_request = temp_model.from_map(m['SidecarProxyInitResourceRequest'])
        if m.get('SidecarProxyResourceLimit') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceLimit()
            self.sidecar_proxy_resource_limit = temp_model.from_map(m['SidecarProxyResourceLimit'])
        if m.get('SidecarProxyResourceRequest') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceRequest()
            self.sidecar_proxy_resource_request = temp_model.from_map(m['SidecarProxyResourceRequest'])
        if m.get('TerminationDrainDuration') is not None:
            self.termination_drain_duration = m.get('TerminationDrainDuration')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBody(TeaModel):
    def __init__(
        self,
        config_patches: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatches = None,
        request_id: str = None,
    ):
        self.config_patches = config_patches
        self.request_id = request_id

    def validate(self):
        if self.config_patches:
            self.config_patches.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_patches is not None:
            result['ConfigPatches'] = self.config_patches.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigPatches') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatches()
            self.config_patches = temp_model.from_map(m['ConfigPatches'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNamespaceScopeSidecarConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNamespaceScopeSidecarConfigResponseBody = None,
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
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
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


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        business_locations: str = None,
        request_id: str = None,
    ):
        self.business_locations = business_locations
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_locations is not None:
            result['BusinessLocations'] = self.business_locations
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessLocations') is not None:
            self.business_locations = m.get('BusinessLocations')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshDetailRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints(TeaModel):
    def __init__(
        self,
        intranet_api_server_endpoint: str = None,
        intranet_pilot_endpoint: str = None,
        public_api_server_endpoint: str = None,
        public_pilot_endpoint: str = None,
    ):
        self.intranet_api_server_endpoint = intranet_api_server_endpoint
        self.intranet_pilot_endpoint = intranet_pilot_endpoint
        self.public_api_server_endpoint = public_api_server_endpoint
        self.public_pilot_endpoint = public_pilot_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.intranet_pilot_endpoint is not None:
            result['IntranetPilotEndpoint'] = self.intranet_pilot_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        if self.public_pilot_endpoint is not None:
            result['PublicPilotEndpoint'] = self.public_pilot_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('IntranetPilotEndpoint') is not None:
            self.intranet_pilot_endpoint = m.get('IntranetPilotEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        if m.get('PublicPilotEndpoint') is not None:
            self.public_pilot_endpoint = m.get('PublicPilotEndpoint')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        error_message: str = None,
        name: str = None,
        profile: str = None,
        region_id: str = None,
        service_mesh_id: str = None,
        state: str = None,
        update_time: str = None,
        version: str = None,
    ):
        self.creation_time = creation_time
        self.error_message = error_message
        self.name = name
        self.profile = profile
        self.region_id = region_id
        self.service_mesh_id = service_mesh_id
        self.state = state
        self.update_time = update_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer(TeaModel):
    def __init__(
        self,
        api_server_loadbalancer_id: str = None,
        api_server_public_eip: bool = None,
        pilot_public_eip: bool = None,
        pilot_public_loadbalancer_id: str = None,
    ):
        self.api_server_loadbalancer_id = api_server_loadbalancer_id
        self.api_server_public_eip = api_server_public_eip
        self.pilot_public_eip = pilot_public_eip
        self.pilot_public_loadbalancer_id = pilot_public_loadbalancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_loadbalancer_id is not None:
            result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.pilot_public_loadbalancer_id is not None:
            result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiServerLoadbalancerId') is not None:
            self.api_server_loadbalancer_id = m.get('ApiServerLoadbalancerId')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        if m.get('PilotPublicEip') is not None:
            self.pilot_public_eip = m.get('PilotPublicEip')
        if m.get('PilotPublicLoadbalancerId') is not None:
            self.pilot_public_loadbalancer_id = m.get('PilotPublicLoadbalancerId')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        project: str = None,
    ):
        self.enabled = enabled
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit(TeaModel):
    def __init__(
        self,
        audit_project_status: str = None,
        enabled: bool = None,
        project: str = None,
    ):
        self.audit_project_status = audit_project_status
        self.enabled = enabled
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_project_status is not None:
            result['AuditProjectStatus'] = self.audit_project_status
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditProjectStatus') is not None:
            self.audit_project_status = m.get('AuditProjectStatus')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigControlPlaneLogInfo(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        project: str = None,
    ):
        self.enabled = enabled
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigEdition(TeaModel):
    def __init__(
        self,
        istiod_image_tag: str = None,
        name: str = None,
        proxy_image_tag: str = None,
    ):
        self.istiod_image_tag = istiod_image_tag
        self.name = name
        self.proxy_image_tag = proxy_image_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istiod_image_tag is not None:
            result['IstiodImageTag'] = self.istiod_image_tag
        if self.name is not None:
            result['Name'] = self.name
        if self.proxy_image_tag is not None:
            result['ProxyImageTag'] = self.proxy_image_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstiodImageTag') is not None:
            self.istiod_image_tag = m.get('IstiodImageTag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProxyImageTag') is not None:
            self.proxy_image_tag = m.get('ProxyImageTag')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationIstioCRHistory(TeaModel):
    def __init__(
        self,
        enable_history: bool = None,
    ):
        self.enable_history = enable_history

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_history is not None:
            result['EnableHistory'] = self.enable_history
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableHistory') is not None:
            self.enable_history = m.get('EnableHistory')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGetHTTPHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGet(TeaModel):
    def __init__(
        self,
        httpheaders: List[DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGetHTTPHeaders] = None,
        host: str = None,
        port: str = None,
        scheme: str = None,
    ):
        self.httpheaders = httpheaders
        self.host = host
        self.port = port
        self.scheme = scheme

    def validate(self):
        if self.httpheaders:
            for k in self.httpheaders:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HTTPHeaders'] = []
        if self.httpheaders is not None:
            for k in self.httpheaders:
                result['HTTPHeaders'].append(k.to_map() if k else None)
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.httpheaders = []
        if m.get('HTTPHeaders') is not None:
            for k in m.get('HTTPHeaders'):
                temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGetHTTPHeaders()
                self.httpheaders.append(temp_model.from_map(k))
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartTCPSocket(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStart(TeaModel):
    def __init__(
        self,
        exec: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartExec = None,
        httpget: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGet = None,
        tcpsocket: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartTCPSocket = None,
    ):
        self.exec = exec
        self.httpget = httpget
        self.tcpsocket = tcpsocket

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.httpget:
            self.httpget.validate()
        if self.tcpsocket:
            self.tcpsocket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.httpget is not None:
            result['HTTPGet'] = self.httpget.to_map()
        if self.tcpsocket is not None:
            result['TCPSocket'] = self.tcpsocket.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('HTTPGet') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGet()
            self.httpget = temp_model.from_map(m['HTTPGet'])
        if m.get('TCPSocket') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartTCPSocket()
            self.tcpsocket = temp_model.from_map(m['TCPSocket'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGetHTTPHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGet(TeaModel):
    def __init__(
        self,
        httpheaders: List[DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGetHTTPHeaders] = None,
        host: str = None,
        port: str = None,
        scheme: str = None,
    ):
        self.httpheaders = httpheaders
        self.host = host
        self.port = port
        self.scheme = scheme

    def validate(self):
        if self.httpheaders:
            for k in self.httpheaders:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HTTPHeaders'] = []
        if self.httpheaders is not None:
            for k in self.httpheaders:
                result['HTTPHeaders'].append(k.to_map() if k else None)
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.httpheaders = []
        if m.get('HTTPHeaders') is not None:
            for k in m.get('HTTPHeaders'):
                temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGetHTTPHeaders()
                self.httpheaders.append(temp_model.from_map(k))
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopTCPSocket(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStop(TeaModel):
    def __init__(
        self,
        exec: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopExec = None,
        httpget: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGet = None,
        tcpsocket: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopTCPSocket = None,
    ):
        self.exec = exec
        self.httpget = httpget
        self.tcpsocket = tcpsocket

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.httpget:
            self.httpget.validate()
        if self.tcpsocket:
            self.tcpsocket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.httpget is not None:
            result['HTTPGet'] = self.httpget.to_map()
        if self.tcpsocket is not None:
            result['TCPSocket'] = self.tcpsocket.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('HTTPGet') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGet()
            self.httpget = temp_model.from_map(m['HTTPGet'])
        if m.get('TCPSocket') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopTCPSocket()
            self.tcpsocket = temp_model.from_map(m['TCPSocket'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecycle(TeaModel):
    def __init__(
        self,
        post_start: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStart = None,
        pre_stop: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStop = None,
    ):
        self.post_start = post_start
        self.pre_stop = pre_stop

    def validate(self):
        if self.post_start:
            self.post_start.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.post_start is not None:
            result['PostStart'] = self.post_start.to_map()
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostStart') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStart()
            self.post_start = temp_model.from_map(m['PostStart'])
        if m.get('PreStop') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStop()
            self.pre_stop = temp_model.from_map(m['PreStop'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationMultiBuffer(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        poll_delay: str = None,
    ):
        self.enabled = enabled
        self.poll_delay = poll_delay

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.poll_delay is not None:
            result['PollDelay'] = self.poll_delay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('PollDelay') is not None:
            self.poll_delay = m.get('PollDelay')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceLimit(TeaModel):
    def __init__(
        self,
        resource_cpulimit: str = None,
        resource_memory_limit: str = None,
    ):
        self.resource_cpulimit = resource_cpulimit
        self.resource_memory_limit = resource_memory_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpulimit is not None:
            result['ResourceCPULimit'] = self.resource_cpulimit
        if self.resource_memory_limit is not None:
            result['ResourceMemoryLimit'] = self.resource_memory_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPULimit') is not None:
            self.resource_cpulimit = m.get('ResourceCPULimit')
        if m.get('ResourceMemoryLimit') is not None:
            self.resource_memory_limit = m.get('ResourceMemoryLimit')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceRequest(TeaModel):
    def __init__(
        self,
        resource_cpurequest: str = None,
        resource_memory_request: str = None,
    ):
        self.resource_cpurequest = resource_cpurequest
        self.resource_memory_request = resource_memory_request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpurequest is not None:
            result['ResourceCPURequest'] = self.resource_cpurequest
        if self.resource_memory_request is not None:
            result['ResourceMemoryRequest'] = self.resource_memory_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPURequest') is not None:
            self.resource_cpurequest = m.get('ResourceCPURequest')
        if m.get('ResourceMemoryRequest') is not None:
            self.resource_memory_request = m.get('ResourceMemoryRequest')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfiguration(TeaModel):
    def __init__(
        self,
        craggregation_enabled: bool = None,
        discovery_selectors: List[Dict[str, Any]] = None,
        istio_crhistory: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationIstioCRHistory = None,
        lifecycle: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecycle = None,
        multi_buffer: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationMultiBuffer = None,
        sidecar_proxy_init_resource_limit: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceLimit = None,
        sidecar_proxy_init_resource_request: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceRequest = None,
        termination_drain_duration: str = None,
    ):
        self.craggregation_enabled = craggregation_enabled
        self.discovery_selectors = discovery_selectors
        self.istio_crhistory = istio_crhistory
        self.lifecycle = lifecycle
        self.multi_buffer = multi_buffer
        self.sidecar_proxy_init_resource_limit = sidecar_proxy_init_resource_limit
        self.sidecar_proxy_init_resource_request = sidecar_proxy_init_resource_request
        self.termination_drain_duration = termination_drain_duration

    def validate(self):
        if self.istio_crhistory:
            self.istio_crhistory.validate()
        if self.lifecycle:
            self.lifecycle.validate()
        if self.multi_buffer:
            self.multi_buffer.validate()
        if self.sidecar_proxy_init_resource_limit:
            self.sidecar_proxy_init_resource_limit.validate()
        if self.sidecar_proxy_init_resource_request:
            self.sidecar_proxy_init_resource_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.craggregation_enabled is not None:
            result['CRAggregationEnabled'] = self.craggregation_enabled
        if self.discovery_selectors is not None:
            result['DiscoverySelectors'] = self.discovery_selectors
        if self.istio_crhistory is not None:
            result['IstioCRHistory'] = self.istio_crhistory.to_map()
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle.to_map()
        if self.multi_buffer is not None:
            result['MultiBuffer'] = self.multi_buffer.to_map()
        if self.sidecar_proxy_init_resource_limit is not None:
            result['SidecarProxyInitResourceLimit'] = self.sidecar_proxy_init_resource_limit.to_map()
        if self.sidecar_proxy_init_resource_request is not None:
            result['SidecarProxyInitResourceRequest'] = self.sidecar_proxy_init_resource_request.to_map()
        if self.termination_drain_duration is not None:
            result['TerminationDrainDuration'] = self.termination_drain_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CRAggregationEnabled') is not None:
            self.craggregation_enabled = m.get('CRAggregationEnabled')
        if m.get('DiscoverySelectors') is not None:
            self.discovery_selectors = m.get('DiscoverySelectors')
        if m.get('IstioCRHistory') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationIstioCRHistory()
            self.istio_crhistory = temp_model.from_map(m['IstioCRHistory'])
        if m.get('Lifecycle') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecycle()
            self.lifecycle = temp_model.from_map(m['Lifecycle'])
        if m.get('MultiBuffer') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationMultiBuffer()
            self.multi_buffer = temp_model.from_map(m['MultiBuffer'])
        if m.get('SidecarProxyInitResourceLimit') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceLimit()
            self.sidecar_proxy_init_resource_limit = temp_model.from_map(m['SidecarProxyInitResourceLimit'])
        if m.get('SidecarProxyInitResourceRequest') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceRequest()
            self.sidecar_proxy_init_resource_request = temp_model.from_map(m['SidecarProxyInitResourceRequest'])
        if m.get('TerminationDrainDuration') is not None:
            self.termination_drain_duration = m.get('TerminationDrainDuration')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigK8sNewAPIsSupport(TeaModel):
    def __init__(
        self,
        gateway_apienabled: bool = None,
    ):
        self.gateway_apienabled = gateway_apienabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_apienabled is not None:
            result['GatewayAPIEnabled'] = self.gateway_apienabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayAPIEnabled') is not None:
            self.gateway_apienabled = m.get('GatewayAPIEnabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        url: str = None,
    ):
        self.enabled = enabled
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigLocalityLB(TeaModel):
    def __init__(
        self,
        distribute: Dict[str, Any] = None,
        enabled: bool = None,
        failover: Dict[str, Any] = None,
    ):
        self.distribute = distribute
        self.enabled = enabled
        self.failover = failover

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribute is not None:
            result['Distribute'] = self.distribute
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.failover is not None:
            result['Failover'] = self.failover
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Distribute') is not None:
            self.distribute = m.get('Distribute')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Failover') is not None:
            self.failover = m.get('Failover')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        limit_cpu: str = None,
        limit_memory: str = None,
        log_level: str = None,
        request_cpu: str = None,
        request_memory: str = None,
    ):
        self.enabled = enabled
        self.limit_cpu = limit_cpu
        self.limit_memory = limit_memory
        self.log_level = log_level
        self.request_cpu = request_cpu
        self.request_memory = request_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotConfigSource(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        nacos_id: str = None,
    ):
        self.enabled = enabled
        self.nacos_id = nacos_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.nacos_id is not None:
            result['NacosID'] = self.nacos_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('NacosID') is not None:
            self.nacos_id = m.get('NacosID')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotFeature(TeaModel):
    def __init__(
        self,
        enable_sdsserver: bool = None,
        filter_gateway_cluster_config: bool = None,
    ):
        self.enable_sdsserver = enable_sdsserver
        self.filter_gateway_cluster_config = filter_gateway_cluster_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_sdsserver is not None:
            result['EnableSDSServer'] = self.enable_sdsserver
        if self.filter_gateway_cluster_config is not None:
            result['FilterGatewayClusterConfig'] = self.filter_gateway_cluster_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSDSServer') is not None:
            self.enable_sdsserver = m.get('EnableSDSServer')
        if m.get('FilterGatewayClusterConfig') is not None:
            self.filter_gateway_cluster_config = m.get('FilterGatewayClusterConfig')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot(TeaModel):
    def __init__(
        self,
        config_source: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotConfigSource = None,
        feature: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotFeature = None,
        http_10enabled: bool = None,
        trace_sampling: float = None,
    ):
        self.config_source = config_source
        self.feature = feature
        self.http_10enabled = http_10enabled
        self.trace_sampling = trace_sampling

    def validate(self):
        if self.config_source:
            self.config_source.validate()
        if self.feature:
            self.feature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_source is not None:
            result['ConfigSource'] = self.config_source.to_map()
        if self.feature is not None:
            result['Feature'] = self.feature.to_map()
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSource') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotConfigSource()
            self.config_source = temp_model.from_map(m['ConfigSource'])
        if m.get('Feature') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotFeature()
            self.feature = temp_model.from_map(m['Feature'])
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus(TeaModel):
    def __init__(
        self,
        external_url: str = None,
        use_external: bool = None,
    ):
        self.external_url = external_url
        self.use_external = use_external

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.use_external is not None:
            result['UseExternal'] = self.use_external
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('UseExternal') is not None:
            self.use_external = m.get('UseExternal')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport(TeaModel):
    def __init__(
        self,
        dubbo_filter_enabled: bool = None,
        mysql_filter_enabled: bool = None,
        redis_filter_enabled: bool = None,
        thrift_filter_enabled: bool = None,
    ):
        self.dubbo_filter_enabled = dubbo_filter_enabled
        self.mysql_filter_enabled = mysql_filter_enabled
        self.redis_filter_enabled = redis_filter_enabled
        self.thrift_filter_enabled = thrift_filter_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dubbo_filter_enabled is not None:
            result['DubboFilterEnabled'] = self.dubbo_filter_enabled
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DubboFilterEnabled') is not None:
            self.dubbo_filter_enabled = m.get('DubboFilterEnabled')
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy(TeaModel):
    def __init__(
        self,
        access_log_file: str = None,
        access_log_format: str = None,
        access_log_service_enabled: bool = None,
        access_log_service_host: str = None,
        access_log_service_port: int = None,
        cluster_domain: str = None,
        enable_dnsproxying: bool = None,
        limit_cpu: str = None,
        limit_memory: str = None,
        request_cpu: str = None,
        request_memory: str = None,
    ):
        self.access_log_file = access_log_file
        self.access_log_format = access_log_format
        self.access_log_service_enabled = access_log_service_enabled
        self.access_log_service_host = access_log_service_host
        self.access_log_service_port = access_log_service_port
        self.cluster_domain = cluster_domain
        self.enable_dnsproxying = enable_dnsproxying
        self.limit_cpu = limit_cpu
        self.limit_memory = limit_memory
        self.request_cpu = request_cpu
        self.request_memory = request_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_file is not None:
            result['AccessLogFile'] = self.access_log_file
        if self.access_log_format is not None:
            result['AccessLogFormat'] = self.access_log_format
        if self.access_log_service_enabled is not None:
            result['AccessLogServiceEnabled'] = self.access_log_service_enabled
        if self.access_log_service_host is not None:
            result['AccessLogServiceHost'] = self.access_log_service_host
        if self.access_log_service_port is not None:
            result['AccessLogServicePort'] = self.access_log_service_port
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.enable_dnsproxying is not None:
            result['EnableDNSProxying'] = self.enable_dnsproxying
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogFile') is not None:
            self.access_log_file = m.get('AccessLogFile')
        if m.get('AccessLogFormat') is not None:
            self.access_log_format = m.get('AccessLogFormat')
        if m.get('AccessLogServiceEnabled') is not None:
            self.access_log_service_enabled = m.get('AccessLogServiceEnabled')
        if m.get('AccessLogServiceHost') is not None:
            self.access_log_service_host = m.get('AccessLogServiceHost')
        if m.get('AccessLogServicePort') is not None:
            self.access_log_service_port = m.get('AccessLogServicePort')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('EnableDNSProxying') is not None:
            self.enable_dnsproxying = m.get('EnableDNSProxying')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        exclude_namespaces: str = None,
    ):
        self.enabled = enabled
        self.exclude_namespaces = exclude_namespaces

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.exclude_namespaces is not None:
            result['ExcludeNamespaces'] = self.exclude_namespaces
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExcludeNamespaces') is not None:
            self.exclude_namespaces = m.get('ExcludeNamespaces')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(
        self,
        auto_injection_policy_enabled: bool = None,
        enable_namespaces_by_default: bool = None,
        init_cniconfiguration: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration = None,
        limit_cpu: str = None,
        limit_memory: str = None,
        request_cpu: str = None,
        request_memory: str = None,
        sidecar_injector_webhook_as_yaml: str = None,
    ):
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        self.enable_namespaces_by_default = enable_namespaces_by_default
        self.init_cniconfiguration = init_cniconfiguration
        self.limit_cpu = limit_cpu
        self.limit_memory = limit_memory
        self.request_cpu = request_cpu
        self.request_memory = request_memory
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml

    def validate(self):
        if self.init_cniconfiguration:
            self.init_cniconfiguration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.init_cniconfiguration is not None:
            result['InitCNIConfiguration'] = self.init_cniconfiguration.to_map()
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.sidecar_injector_webhook_as_yaml is not None:
            result['SidecarInjectorWebhookAsYaml'] = self.sidecar_injector_webhook_as_yaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('InitCNIConfiguration') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(m['InitCNIConfiguration'])
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = m.get('SidecarInjectorWebhookAsYaml')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig(TeaModel):
    def __init__(
        self,
        access_log: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog = None,
        audit: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit = None,
        control_plane_log_info: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigControlPlaneLogInfo = None,
        customized_zipkin: bool = None,
        edition: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigEdition = None,
        enable_locality_lb: bool = None,
        exclude_ipranges: str = None,
        exclude_inbound_ports: str = None,
        exclude_outbound_ports: str = None,
        extra_configuration: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfiguration = None,
        include_ipranges: str = None,
        k_8s_new_apis_support: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigK8sNewAPIsSupport = None,
        kiali: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali = None,
        locality_lb: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigLocalityLB = None,
        mse: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE = None,
        opa: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA = None,
        outbound_traffic_policy: str = None,
        pilot: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot = None,
        prometheus: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus = None,
        protocol_support: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport = None,
        proxy: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy = None,
        sidecar_injector: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector = None,
        telemetry: bool = None,
        tracing: bool = None,
        web_assembly_filter_deployment: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment = None,
    ):
        self.access_log = access_log
        self.audit = audit
        self.control_plane_log_info = control_plane_log_info
        self.customized_zipkin = customized_zipkin
        self.edition = edition
        self.enable_locality_lb = enable_locality_lb
        self.exclude_ipranges = exclude_ipranges
        self.exclude_inbound_ports = exclude_inbound_ports
        self.exclude_outbound_ports = exclude_outbound_ports
        self.extra_configuration = extra_configuration
        self.include_ipranges = include_ipranges
        self.k_8s_new_apis_support = k_8s_new_apis_support
        self.kiali = kiali
        self.locality_lb = locality_lb
        self.mse = mse
        self.opa = opa
        self.outbound_traffic_policy = outbound_traffic_policy
        self.pilot = pilot
        self.prometheus = prometheus
        self.protocol_support = protocol_support
        self.proxy = proxy
        self.sidecar_injector = sidecar_injector
        self.telemetry = telemetry
        self.tracing = tracing
        self.web_assembly_filter_deployment = web_assembly_filter_deployment

    def validate(self):
        if self.access_log:
            self.access_log.validate()
        if self.audit:
            self.audit.validate()
        if self.control_plane_log_info:
            self.control_plane_log_info.validate()
        if self.edition:
            self.edition.validate()
        if self.extra_configuration:
            self.extra_configuration.validate()
        if self.k_8s_new_apis_support:
            self.k_8s_new_apis_support.validate()
        if self.kiali:
            self.kiali.validate()
        if self.locality_lb:
            self.locality_lb.validate()
        if self.mse:
            self.mse.validate()
        if self.opa:
            self.opa.validate()
        if self.pilot:
            self.pilot.validate()
        if self.prometheus:
            self.prometheus.validate()
        if self.protocol_support:
            self.protocol_support.validate()
        if self.proxy:
            self.proxy.validate()
        if self.sidecar_injector:
            self.sidecar_injector.validate()
        if self.web_assembly_filter_deployment:
            self.web_assembly_filter_deployment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log is not None:
            result['AccessLog'] = self.access_log.to_map()
        if self.audit is not None:
            result['Audit'] = self.audit.to_map()
        if self.control_plane_log_info is not None:
            result['ControlPlaneLogInfo'] = self.control_plane_log_info.to_map()
        if self.customized_zipkin is not None:
            result['CustomizedZipkin'] = self.customized_zipkin
        if self.edition is not None:
            result['Edition'] = self.edition.to_map()
        if self.enable_locality_lb is not None:
            result['EnableLocalityLB'] = self.enable_locality_lb
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.extra_configuration is not None:
            result['ExtraConfiguration'] = self.extra_configuration.to_map()
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.k_8s_new_apis_support is not None:
            result['K8sNewAPIsSupport'] = self.k_8s_new_apis_support.to_map()
        if self.kiali is not None:
            result['Kiali'] = self.kiali.to_map()
        if self.locality_lb is not None:
            result['LocalityLB'] = self.locality_lb.to_map()
        if self.mse is not None:
            result['MSE'] = self.mse.to_map()
        if self.opa is not None:
            result['OPA'] = self.opa.to_map()
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.pilot is not None:
            result['Pilot'] = self.pilot.to_map()
        if self.prometheus is not None:
            result['Prometheus'] = self.prometheus.to_map()
        if self.protocol_support is not None:
            result['ProtocolSupport'] = self.protocol_support.to_map()
        if self.proxy is not None:
            result['Proxy'] = self.proxy.to_map()
        if self.sidecar_injector is not None:
            result['SidecarInjector'] = self.sidecar_injector.to_map()
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.web_assembly_filter_deployment is not None:
            result['WebAssemblyFilterDeployment'] = self.web_assembly_filter_deployment.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLog') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog()
            self.access_log = temp_model.from_map(m['AccessLog'])
        if m.get('Audit') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit()
            self.audit = temp_model.from_map(m['Audit'])
        if m.get('ControlPlaneLogInfo') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigControlPlaneLogInfo()
            self.control_plane_log_info = temp_model.from_map(m['ControlPlaneLogInfo'])
        if m.get('CustomizedZipkin') is not None:
            self.customized_zipkin = m.get('CustomizedZipkin')
        if m.get('Edition') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigEdition()
            self.edition = temp_model.from_map(m['Edition'])
        if m.get('EnableLocalityLB') is not None:
            self.enable_locality_lb = m.get('EnableLocalityLB')
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('ExtraConfiguration') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfiguration()
            self.extra_configuration = temp_model.from_map(m['ExtraConfiguration'])
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('K8sNewAPIsSupport') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigK8sNewAPIsSupport()
            self.k_8s_new_apis_support = temp_model.from_map(m['K8sNewAPIsSupport'])
        if m.get('Kiali') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali()
            self.kiali = temp_model.from_map(m['Kiali'])
        if m.get('LocalityLB') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigLocalityLB()
            self.locality_lb = temp_model.from_map(m['LocalityLB'])
        if m.get('MSE') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE()
            self.mse = temp_model.from_map(m['MSE'])
        if m.get('OPA') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA()
            self.opa = temp_model.from_map(m['OPA'])
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('Pilot') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(m['Pilot'])
        if m.get('Prometheus') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus()
            self.prometheus = temp_model.from_map(m['Prometheus'])
        if m.get('ProtocolSupport') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport()
            self.protocol_support = temp_model.from_map(m['ProtocolSupport'])
        if m.get('Proxy') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy()
            self.proxy = temp_model.from_map(m['Proxy'])
        if m.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(m['SidecarInjector'])
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('WebAssemblyFilterDeployment') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment()
            self.web_assembly_filter_deployment = temp_model.from_map(m['WebAssemblyFilterDeployment'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switches: List[str] = None,
        vpc_id: str = None,
    ):
        self.security_group_id = security_group_id
        self.v_switches = v_switches
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpec(TeaModel):
    def __init__(
        self,
        load_balancer: DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer = None,
        mesh_config: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig = None,
        network: DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork = None,
    ):
        self.load_balancer = load_balancer
        self.mesh_config = mesh_config
        self.network = network

    def validate(self):
        if self.load_balancer:
            self.load_balancer.validate()
        if self.mesh_config:
            self.mesh_config.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(m['LoadBalancer'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        if m.get('Network') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMesh(TeaModel):
    def __init__(
        self,
        clusters: List[str] = None,
        endpoints: DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints = None,
        service_mesh_info: DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo = None,
        spec: DescribeServiceMeshDetailResponseBodyServiceMeshSpec = None,
    ):
        self.clusters = clusters
        self.endpoints = endpoints
        self.service_mesh_info = service_mesh_info
        self.spec = spec

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()
        if self.service_mesh_info:
            self.service_mesh_info.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        if m.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(m['ServiceMeshInfo'])
        if m.get('Spec') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class DescribeServiceMeshDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_mesh: DescribeServiceMeshDetailResponseBodyServiceMesh = None,
    ):
        self.request_id = request_id
        self.service_mesh = service_mesh

    def validate(self):
        if self.service_mesh:
            self.service_mesh.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_mesh is not None:
            result['ServiceMesh'] = self.service_mesh.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceMesh') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMesh()
            self.service_mesh = temp_model.from_map(m['ServiceMesh'])
        return self


class DescribeServiceMeshDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServiceMeshDetailResponseBody = None,
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
            temp_model = DescribeServiceMeshDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshGatewayPodStatusRequest(TeaModel):
    def __init__(
        self,
        gateway_full_name: str = None,
        guest_cluster_ids: str = None,
        service_mesh_id: str = None,
    ):
        self.gateway_full_name = gateway_full_name
        self.guest_cluster_ids = guest_cluster_ids
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_full_name is not None:
            result['GatewayFullName'] = self.gateway_full_name
        if self.guest_cluster_ids is not None:
            result['GuestClusterIds'] = self.guest_cluster_ids
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayFullName') is not None:
            self.gateway_full_name = m.get('GatewayFullName')
        if m.get('GuestClusterIds') is not None:
            self.guest_cluster_ids = m.get('GuestClusterIds')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshGatewayPodStatusResponseBodyASMGatewayDetails(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        gateway_name: str = None,
        ready_pod_num: int = None,
        spec_pod_num: int = None,
    ):
        self.cluster_id = cluster_id
        self.gateway_name = gateway_name
        self.ready_pod_num = ready_pod_num
        self.spec_pod_num = spec_pod_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterID'] = self.cluster_id
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.ready_pod_num is not None:
            result['ReadyPodNum'] = self.ready_pod_num
        if self.spec_pod_num is not None:
            result['SpecPodNum'] = self.spec_pod_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterID') is not None:
            self.cluster_id = m.get('ClusterID')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('ReadyPodNum') is not None:
            self.ready_pod_num = m.get('ReadyPodNum')
        if m.get('SpecPodNum') is not None:
            self.spec_pod_num = m.get('SpecPodNum')
        return self


class DescribeServiceMeshGatewayPodStatusResponseBody(TeaModel):
    def __init__(
        self,
        asmgateway_details: List[DescribeServiceMeshGatewayPodStatusResponseBodyASMGatewayDetails] = None,
        request_id: str = None,
    ):
        self.asmgateway_details = asmgateway_details
        self.request_id = request_id

    def validate(self):
        if self.asmgateway_details:
            for k in self.asmgateway_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ASMGatewayDetails'] = []
        if self.asmgateway_details is not None:
            for k in self.asmgateway_details:
                result['ASMGatewayDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asmgateway_details = []
        if m.get('ASMGatewayDetails') is not None:
            for k in m.get('ASMGatewayDetails'):
                temp_model = DescribeServiceMeshGatewayPodStatusResponseBodyASMGatewayDetails()
                self.asmgateway_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceMeshGatewayPodStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServiceMeshGatewayPodStatusResponseBody = None,
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
            temp_model = DescribeServiceMeshGatewayPodStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshGatewaySLBStatusRequest(TeaModel):
    def __init__(
        self,
        gateway_addresses: str = None,
        gateway_full_name: str = None,
        service_mesh_id: str = None,
    ):
        self.gateway_addresses = gateway_addresses
        self.gateway_full_name = gateway_full_name
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_addresses is not None:
            result['GatewayAddresses'] = self.gateway_addresses
        if self.gateway_full_name is not None:
            result['GatewayFullName'] = self.gateway_full_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayAddresses') is not None:
            self.gateway_addresses = m.get('GatewayAddresses')
        if m.get('GatewayFullName') is not None:
            self.gateway_full_name = m.get('GatewayFullName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GatewaySLBValueBackendServers(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        server_ip: str = None,
        server_health_status: str = None,
        server_id: str = None,
        vpc_id: str = None,
        listener_port: int = None,
        weight: str = None,
        description: str = None,
        eni_host: str = None,
        type: str = None,
    ):
        self.port = port
        self.protocol = protocol
        self.server_ip = server_ip
        self.server_health_status = server_health_status
        self.server_id = server_id
        self.vpc_id = vpc_id
        self.listener_port = listener_port
        self.weight = weight
        self.description = description
        self.eni_host = eni_host
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_health_status is not None:
            result['ServerHealthStatus'] = self.server_health_status
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.eni_host is not None:
            result['EniHost'] = self.eni_host
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerHealthStatus') is not None:
            self.server_health_status = m.get('ServerHealthStatus')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EniHost') is not None:
            self.eni_host = m.get('EniHost')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GatewaySLBValue(TeaModel):
    def __init__(
        self,
        slbaddress: str = None,
        load_balancer_id: str = None,
        backend_servers: GatewaySLBValueBackendServers = None,
        slbhealth_check_state: str = None,
    ):
        self.slbaddress = slbaddress
        self.load_balancer_id = load_balancer_id
        self.backend_servers = backend_servers
        self.slbhealth_check_state = slbhealth_check_state

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slbaddress is not None:
            result['SLBAddress'] = self.slbaddress
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        if self.slbhealth_check_state is not None:
            result['SLBHealthCheckState'] = self.slbhealth_check_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SLBAddress') is not None:
            self.slbaddress = m.get('SLBAddress')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('BackendServers') is not None:
            temp_model = GatewaySLBValueBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        if m.get('SLBHealthCheckState') is not None:
            self.slbhealth_check_state = m.get('SLBHealthCheckState')
        return self


class DescribeServiceMeshGatewaySLBStatusResponseBody(TeaModel):
    def __init__(
        self,
        gateway_slb: Dict[str, GatewaySLBValue] = None,
        request_id: str = None,
    ):
        self.gateway_slb = gateway_slb
        self.request_id = request_id

    def validate(self):
        if self.gateway_slb:
            for v in self.gateway_slb.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GatewaySLB'] = {}
        if self.gateway_slb is not None:
            for k, v in self.gateway_slb.items():
                result['GatewaySLB'][k] = v.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway_slb = {}
        if m.get('GatewaySLB') is not None:
            for k, v in m.get('GatewaySLB').items():
                temp_model = GatewaySLBValue()
                self.gateway_slb[k] = temp_model.from_map(v)
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceMeshGatewaySLBStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServiceMeshGatewaySLBStatusResponseBody = None,
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
            temp_model = DescribeServiceMeshGatewaySLBStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshKubeconfigRequest(TeaModel):
    def __init__(
        self,
        private_ip_address: bool = None,
        service_mesh_id: str = None,
    ):
        self.private_ip_address = private_ip_address
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshKubeconfigResponseBody(TeaModel):
    def __init__(
        self,
        kubeconfig: str = None,
        request_id: str = None,
    ):
        self.kubeconfig = kubeconfig
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubeconfig is not None:
            result['Kubeconfig'] = self.kubeconfig
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Kubeconfig') is not None:
            self.kubeconfig = m.get('Kubeconfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceMeshKubeconfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServiceMeshKubeconfigResponseBody = None,
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
            temp_model = DescribeServiceMeshKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshUpgradeStatusRequest(TeaModel):
    def __init__(
        self,
        all_istio_gateway_full_names: str = None,
        guest_cluster_ids: str = None,
        service_mesh_id: str = None,
    ):
        self.all_istio_gateway_full_names = all_istio_gateway_full_names
        self.guest_cluster_ids = guest_cluster_ids
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_istio_gateway_full_names is not None:
            result['AllIstioGatewayFullNames'] = self.all_istio_gateway_full_names
        if self.guest_cluster_ids is not None:
            result['GuestClusterIds'] = self.guest_cluster_ids
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllIstioGatewayFullNames') is not None:
            self.all_istio_gateway_full_names = m.get('AllIstioGatewayFullNames')
        if m.get('GuestClusterIds') is not None:
            self.guest_cluster_ids = m.get('GuestClusterIds')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpgradeDetailGatewayStatusRecordValue(TeaModel):
    def __init__(
        self,
        status: str = None,
        message: str = None,
        version: str = None,
    ):
        self.status = status
        self.message = message
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.message is not None:
            result['Message'] = self.message
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeServiceMeshUpgradeStatusResponseBodyUpgradeDetail(TeaModel):
    def __init__(
        self,
        finished_gateways_num: int = None,
        gateway_status_record: Dict[str, UpgradeDetailGatewayStatusRecordValue] = None,
        mesh_status: str = None,
        total_gateways_num: int = None,
    ):
        self.finished_gateways_num = finished_gateways_num
        self.gateway_status_record = gateway_status_record
        self.mesh_status = mesh_status
        self.total_gateways_num = total_gateways_num

    def validate(self):
        if self.gateway_status_record:
            for v in self.gateway_status_record.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished_gateways_num is not None:
            result['FinishedGatewaysNum'] = self.finished_gateways_num
        result['GatewayStatusRecord'] = {}
        if self.gateway_status_record is not None:
            for k, v in self.gateway_status_record.items():
                result['GatewayStatusRecord'][k] = v.to_map()
        if self.mesh_status is not None:
            result['MeshStatus'] = self.mesh_status
        if self.total_gateways_num is not None:
            result['TotalGatewaysNum'] = self.total_gateways_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishedGatewaysNum') is not None:
            self.finished_gateways_num = m.get('FinishedGatewaysNum')
        self.gateway_status_record = {}
        if m.get('GatewayStatusRecord') is not None:
            for k, v in m.get('GatewayStatusRecord').items():
                temp_model = UpgradeDetailGatewayStatusRecordValue()
                self.gateway_status_record[k] = temp_model.from_map(v)
        if m.get('MeshStatus') is not None:
            self.mesh_status = m.get('MeshStatus')
        if m.get('TotalGatewaysNum') is not None:
            self.total_gateways_num = m.get('TotalGatewaysNum')
        return self


class DescribeServiceMeshUpgradeStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        upgrade_detail: DescribeServiceMeshUpgradeStatusResponseBodyUpgradeDetail = None,
    ):
        self.request_id = request_id
        self.upgrade_detail = upgrade_detail

    def validate(self):
        if self.upgrade_detail:
            self.upgrade_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upgrade_detail is not None:
            result['UpgradeDetail'] = self.upgrade_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpgradeDetail') is not None:
            temp_model = DescribeServiceMeshUpgradeStatusResponseBodyUpgradeDetail()
            self.upgrade_detail = temp_model.from_map(m['UpgradeDetail'])
        return self


class DescribeServiceMeshUpgradeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServiceMeshUpgradeStatusResponseBody = None,
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
            temp_model = DescribeServiceMeshUpgradeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshVMsRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshVMsResponseBodyVMs(TeaModel):
    def __init__(
        self,
        has_tag: bool = None,
        host_name: str = None,
        instance_id: str = None,
        ip_address: str = None,
        region: str = None,
        security_group_ids: str = None,
        service_mesh_id: str = None,
        status: str = None,
    ):
        self.has_tag = has_tag
        self.host_name = host_name
        self.instance_id = instance_id
        self.ip_address = ip_address
        self.region = region
        self.security_group_ids = security_group_ids
        self.service_mesh_id = service_mesh_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_tag is not None:
            result['HasTag'] = self.has_tag
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.region is not None:
            result['Region'] = self.region
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasTag') is not None:
            self.has_tag = m.get('HasTag')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeServiceMeshVMsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vms: List[DescribeServiceMeshVMsResponseBodyVMs] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.vms = vms

    def validate(self):
        if self.vms:
            for k in self.vms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VMs'] = []
        if self.vms is not None:
            for k in self.vms:
                result['VMs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.vms = []
        if m.get('VMs') is not None:
            for k in m.get('VMs'):
                temp_model = DescribeServiceMeshVMsResponseBodyVMs()
                self.vms.append(temp_model.from_map(k))
        return self


class DescribeServiceMeshVMsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServiceMeshVMsResponseBody = None,
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
            temp_model = DescribeServiceMeshVMsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesEndpoints(TeaModel):
    def __init__(
        self,
        intranet_api_server_endpoint: str = None,
        intranet_pilot_endpoint: str = None,
        public_api_server_endpoint: str = None,
        public_pilot_endpoint: str = None,
        reverse_tunnel_endpoint: str = None,
    ):
        self.intranet_api_server_endpoint = intranet_api_server_endpoint
        self.intranet_pilot_endpoint = intranet_pilot_endpoint
        self.public_api_server_endpoint = public_api_server_endpoint
        self.public_pilot_endpoint = public_pilot_endpoint
        self.reverse_tunnel_endpoint = reverse_tunnel_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.intranet_pilot_endpoint is not None:
            result['IntranetPilotEndpoint'] = self.intranet_pilot_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        if self.public_pilot_endpoint is not None:
            result['PublicPilotEndpoint'] = self.public_pilot_endpoint
        if self.reverse_tunnel_endpoint is not None:
            result['ReverseTunnelEndpoint'] = self.reverse_tunnel_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('IntranetPilotEndpoint') is not None:
            self.intranet_pilot_endpoint = m.get('IntranetPilotEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        if m.get('PublicPilotEndpoint') is not None:
            self.public_pilot_endpoint = m.get('PublicPilotEndpoint')
        if m.get('ReverseTunnelEndpoint') is not None:
            self.reverse_tunnel_endpoint = m.get('ReverseTunnelEndpoint')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        error_message: str = None,
        name: str = None,
        profile: str = None,
        region_id: str = None,
        service_mesh_id: str = None,
        state: str = None,
        update_time: str = None,
        version: str = None,
    ):
        self.creation_time = creation_time
        self.error_message = error_message
        self.name = name
        self.profile = profile
        self.region_id = region_id
        self.service_mesh_id = service_mesh_id
        self.state = state
        self.update_time = update_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer(TeaModel):
    def __init__(
        self,
        api_server_loadbalancer_id: str = None,
        api_server_public_eip: bool = None,
        pilot_public_eip: bool = None,
        pilot_public_loadbalancer_id: str = None,
    ):
        self.api_server_loadbalancer_id = api_server_loadbalancer_id
        self.api_server_public_eip = api_server_public_eip
        self.pilot_public_eip = pilot_public_eip
        self.pilot_public_loadbalancer_id = pilot_public_loadbalancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_loadbalancer_id is not None:
            result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.pilot_public_loadbalancer_id is not None:
            result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiServerLoadbalancerId') is not None:
            self.api_server_loadbalancer_id = m.get('ApiServerLoadbalancerId')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        if m.get('PilotPublicEip') is not None:
            self.pilot_public_eip = m.get('PilotPublicEip')
        if m.get('PilotPublicLoadbalancerId') is not None:
            self.pilot_public_loadbalancer_id = m.get('PilotPublicLoadbalancerId')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot(TeaModel):
    def __init__(
        self,
        http_10enabled: bool = None,
        trace_sampling: float = None,
    ):
        self.http_10enabled = http_10enabled
        self.trace_sampling = trace_sampling

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        exclude_namespaces: str = None,
    ):
        self.enabled = enabled
        self.exclude_namespaces = exclude_namespaces

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.exclude_namespaces is not None:
            result['ExcludeNamespaces'] = self.exclude_namespaces
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExcludeNamespaces') is not None:
            self.exclude_namespaces = m.get('ExcludeNamespaces')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(
        self,
        auto_injection_policy_enabled: bool = None,
        enable_namespaces_by_default: bool = None,
        init_cniconfiguration: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration = None,
    ):
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        self.enable_namespaces_by_default = enable_namespaces_by_default
        self.init_cniconfiguration = init_cniconfiguration

    def validate(self):
        if self.init_cniconfiguration:
            self.init_cniconfiguration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.init_cniconfiguration is not None:
            result['InitCNIConfiguration'] = self.init_cniconfiguration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('InitCNIConfiguration') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(m['InitCNIConfiguration'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig(TeaModel):
    def __init__(
        self,
        mtls: bool = None,
        outbound_traffic_policy: str = None,
        pilot: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot = None,
        sidecar_injector: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector = None,
        strict_mtls: bool = None,
        telemetry: bool = None,
        tracing: bool = None,
    ):
        self.mtls = mtls
        self.outbound_traffic_policy = outbound_traffic_policy
        self.pilot = pilot
        self.sidecar_injector = sidecar_injector
        self.strict_mtls = strict_mtls
        self.telemetry = telemetry
        self.tracing = tracing

    def validate(self):
        if self.pilot:
            self.pilot.validate()
        if self.sidecar_injector:
            self.sidecar_injector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mtls is not None:
            result['Mtls'] = self.mtls
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.pilot is not None:
            result['Pilot'] = self.pilot.to_map()
        if self.sidecar_injector is not None:
            result['SidecarInjector'] = self.sidecar_injector.to_map()
        if self.strict_mtls is not None:
            result['StrictMtls'] = self.strict_mtls
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mtls') is not None:
            self.mtls = m.get('Mtls')
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('Pilot') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(m['Pilot'])
        if m.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(m['SidecarInjector'])
        if m.get('StrictMtls') is not None:
            self.strict_mtls = m.get('StrictMtls')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switches: List[str] = None,
        vpc_id: str = None,
    ):
        self.security_group_id = security_group_id
        self.v_switches = v_switches
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpec(TeaModel):
    def __init__(
        self,
        load_balancer: DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer = None,
        mesh_config: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig = None,
        network: DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork = None,
    ):
        self.load_balancer = load_balancer
        self.mesh_config = mesh_config
        self.network = network

    def validate(self):
        if self.load_balancer:
            self.load_balancer.validate()
        if self.mesh_config:
            self.mesh_config.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(m['LoadBalancer'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        if m.get('Network') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshes(TeaModel):
    def __init__(
        self,
        clusters: List[str] = None,
        endpoints: DescribeServiceMeshesResponseBodyServiceMeshesEndpoints = None,
        service_mesh_info: DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo = None,
        spec: DescribeServiceMeshesResponseBodyServiceMeshesSpec = None,
    ):
        self.clusters = clusters
        self.endpoints = endpoints
        self.service_mesh_info = service_mesh_info
        self.spec = spec

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()
        if self.service_mesh_info:
            self.service_mesh_info.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        if m.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(m['ServiceMeshInfo'])
        if m.get('Spec') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class DescribeServiceMeshesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_meshes: List[DescribeServiceMeshesResponseBodyServiceMeshes] = None,
    ):
        self.request_id = request_id
        self.service_meshes = service_meshes

    def validate(self):
        if self.service_meshes:
            for k in self.service_meshes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceMeshes'] = []
        if self.service_meshes is not None:
            for k in self.service_meshes:
                result['ServiceMeshes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_meshes = []
        if m.get('ServiceMeshes') is not None:
            for k in m.get('ServiceMeshes'):
                temp_model = DescribeServiceMeshesResponseBodyServiceMeshes()
                self.service_meshes.append(temp_model.from_map(k))
        return self


class DescribeServiceMeshesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServiceMeshesResponseBody = None,
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
            temp_model = DescribeServiceMeshesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUpgradeVersionRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeUpgradeVersionResponseBodyVersion(TeaModel):
    def __init__(
        self,
        istio_operator_version: str = None,
        istio_version: str = None,
        kubernetes_version: str = None,
    ):
        self.istio_operator_version = istio_operator_version
        self.istio_version = istio_version
        self.kubernetes_version = kubernetes_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istio_operator_version is not None:
            result['IstioOperatorVersion'] = self.istio_operator_version
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstioOperatorVersion') is not None:
            self.istio_operator_version = m.get('IstioOperatorVersion')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('KubernetesVersion') is not None:
            self.kubernetes_version = m.get('KubernetesVersion')
        return self


class DescribeUpgradeVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version: DescribeUpgradeVersionResponseBodyVersion = None,
    ):
        self.request_id = request_id
        self.version = version

    def validate(self):
        if self.version:
            self.version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            temp_model = DescribeUpgradeVersionResponseBodyVersion()
            self.version = temp_model.from_map(m['Version'])
        return self


class DescribeUpgradeVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUpgradeVersionResponseBody = None,
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
            temp_model = DescribeUpgradeVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVMsInServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeVMsInServiceMeshResponseBodyVMs(TeaModel):
    def __init__(
        self,
        has_tag: bool = None,
        host_name: str = None,
        instance_id: str = None,
        ip_address: str = None,
        region: str = None,
        security_group_ids: str = None,
        status: str = None,
    ):
        self.has_tag = has_tag
        self.host_name = host_name
        self.instance_id = instance_id
        self.ip_address = ip_address
        self.region = region
        self.security_group_ids = security_group_ids
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_tag is not None:
            result['HasTag'] = self.has_tag
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.region is not None:
            result['Region'] = self.region
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasTag') is not None:
            self.has_tag = m.get('HasTag')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeVMsInServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vms: List[DescribeVMsInServiceMeshResponseBodyVMs] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.vms = vms

    def validate(self):
        if self.vms:
            for k in self.vms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VMs'] = []
        if self.vms is not None:
            for k in self.vms:
                result['VMs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.vms = []
        if m.get('VMs') is not None:
            for k in m.get('VMs'):
                temp_model = DescribeVMsInServiceMeshResponseBodyVMs()
                self.vms.append(temp_model.from_map(k))
        return self


class DescribeVMsInServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVMsInServiceMeshResponseBody = None,
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
            temp_model = DescribeVMsInServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVSwitchesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
    ):
        self.region_id = region_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeVSwitchesResponseBodyVSwitches(TeaModel):
    def __init__(
        self,
        is_default: bool = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
    ):
        self.is_default = is_default
        self.status = status
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeVSwitchesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        v_switches: List[DescribeVSwitchesResponseBodyVSwitches] = None,
    ):
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # VSwitches
        self.v_switches = v_switches

    def validate(self):
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = DescribeVSwitchesResponseBodyVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        return self


class DescribeVSwitchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVSwitchesResponseBody = None,
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
            temp_model = DescribeVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVersionsResponseBodyVersionInfo(TeaModel):
    def __init__(
        self,
        edition: str = None,
        versions: List[str] = None,
    ):
        self.edition = edition
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.versions is not None:
            result['Versions'] = self.versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Versions') is not None:
            self.versions = m.get('Versions')
        return self


class DescribeVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version_info: List[DescribeVersionsResponseBodyVersionInfo] = None,
    ):
        self.request_id = request_id
        self.version_info = version_info

    def validate(self):
        if self.version_info:
            for k in self.version_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VersionInfo'] = []
        if self.version_info is not None:
            for k in self.version_info:
                result['VersionInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.version_info = []
        if m.get('VersionInfo') is not None:
            for k in m.get('VersionInfo'):
                temp_model = DescribeVersionsResponseBodyVersionInfo()
                self.version_info.append(temp_model.from_map(k))
        return self


class DescribeVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVersionsResponseBody = None,
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
            temp_model = DescribeVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeVpcsResponseBodyVpcs(TeaModel):
    def __init__(
        self,
        is_default: bool = None,
        status: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.is_default = is_default
        self.status = status
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        vpcs: List[DescribeVpcsResponseBodyVpcs] = None,
    ):
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # Vpcs
        self.vpcs = vpcs

    def validate(self):
        if self.vpcs:
            for k in self.vpcs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Vpcs'] = []
        if self.vpcs is not None:
            for k in self.vpcs:
                result['Vpcs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vpcs = []
        if m.get('Vpcs') is not None:
            for k in m.get('Vpcs'):
                temp_model = DescribeVpcsResponseBodyVpcs()
                self.vpcs.append(temp_model.from_map(k))
        return self


class DescribeVpcsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVpcsResponseBody = None,
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
            temp_model = DescribeVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableControlPlaneLogAlertRequest(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        service_mesh_id: str = None,
    ):
        self.rule_id = rule_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DisableControlPlaneLogAlertResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableControlPlaneLogAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableControlPlaneLogAlertResponseBody = None,
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
            temp_model = DisableControlPlaneLogAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableControlPlaneLogAlertRequest(TeaModel):
    def __init__(
        self,
        action_policy_id: str = None,
        rule_id: str = None,
        service_mesh_id: str = None,
    ):
        self.action_policy_id = action_policy_id
        self.rule_id = rule_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_policy_id is not None:
            result['ActionPolicyId'] = self.action_policy_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPolicyId') is not None:
            self.action_policy_id = m.get('ActionPolicyId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class EnableControlPlaneLogAlertResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableControlPlaneLogAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableControlPlaneLogAlertResponseBody = None,
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
            temp_model = EnableControlPlaneLogAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoInjectionLabelSyncStatusRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetAutoInjectionLabelSyncStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAutoInjectionLabelSyncStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutoInjectionLabelSyncStatusResponseBody = None,
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
            temp_model = GetAutoInjectionLabelSyncStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBuiltinEnvoyFilterRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        istio_version: str = None,
        name: str = None,
        service_mesh_id: str = None,
    ):
        self.id = id
        self.istio_version = istio_version
        self.name = name
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.name is not None:
            result['Name'] = self.name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetBuiltinEnvoyFilterResponseBody(TeaModel):
    def __init__(
        self,
        parameters: str = None,
        request_id: str = None,
    ):
        self.parameters = parameters
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBuiltinEnvoyFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBuiltinEnvoyFilterResponseBody = None,
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
            temp_model = GetBuiltinEnvoyFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBuiltinEnvoyFilterCatalogRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetBuiltinEnvoyFilterCatalogResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBuiltinEnvoyFilterCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBuiltinEnvoyFilterCatalogResponseBody = None,
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
            temp_model = GetBuiltinEnvoyFilterCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCaCertRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetCaCertResponseBody(TeaModel):
    def __init__(
        self,
        ca_cert: str = None,
        request_id: str = None,
    ):
        # base64 encode format
        self.ca_cert = ca_cert
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_cert is not None:
            result['CaCert'] = self.ca_cert
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCert') is not None:
            self.ca_cert = m.get('CaCert')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCaCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCaCertResponseBody = None,
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
            temp_model = GetCaCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiagnosisRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        run_at: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.run_at = run_at
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.run_at is not None:
            result['RunAt'] = self.run_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RunAt') is not None:
            self.run_at = m.get('RunAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDiagnosisResponseBody = None,
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
            temp_model = GetDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEcsListRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetEcsListResponseBodyEcsInstances(TeaModel):
    def __init__(
        self,
        has_tag: bool = None,
        host_name: str = None,
        instance_id: str = None,
        ip_address: str = None,
        security_group_ids: List[str] = None,
        status: str = None,
    ):
        self.has_tag = has_tag
        self.host_name = host_name
        self.instance_id = instance_id
        self.ip_address = ip_address
        self.security_group_ids = security_group_ids
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_tag is not None:
            result['HasTag'] = self.has_tag
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasTag') is not None:
            self.has_tag = m.get('HasTag')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetEcsListResponseBody(TeaModel):
    def __init__(
        self,
        ecs_instances: List[GetEcsListResponseBodyEcsInstances] = None,
        request_id: str = None,
    ):
        self.ecs_instances = ecs_instances
        self.request_id = request_id

    def validate(self):
        if self.ecs_instances:
            for k in self.ecs_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsInstances'] = []
        if self.ecs_instances is not None:
            for k in self.ecs_instances:
                result['EcsInstances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_instances = []
        if m.get('EcsInstances') is not None:
            for k in m.get('EcsInstances'):
                temp_model = GetEcsListResponseBodyEcsInstances()
                self.ecs_instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEcsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEcsListResponseBody = None,
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
            temp_model = GetEcsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegisteredServiceEndpointsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        service_mesh_id: str = None,
    ):
        self.name = name
        self.namespace = namespace
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetRegisteredServiceEndpointsResponseBodyServiceEndpoints(TeaModel):
    def __init__(
        self,
        address: str = None,
        cluster_id: str = None,
    ):
        self.address = address
        self.cluster_id = cluster_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetRegisteredServiceEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_endpoints: List[GetRegisteredServiceEndpointsResponseBodyServiceEndpoints] = None,
    ):
        self.request_id = request_id
        self.service_endpoints = service_endpoints

    def validate(self):
        if self.service_endpoints:
            for k in self.service_endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceEndpoints'] = []
        if self.service_endpoints is not None:
            for k in self.service_endpoints:
                result['ServiceEndpoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_endpoints = []
        if m.get('ServiceEndpoints') is not None:
            for k in m.get('ServiceEndpoints'):
                temp_model = GetRegisteredServiceEndpointsResponseBodyServiceEndpoints()
                self.service_endpoints.append(temp_model.from_map(k))
        return self


class GetRegisteredServiceEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRegisteredServiceEndpointsResponseBody = None,
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
            temp_model = GetRegisteredServiceEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegisteredServiceNamespacesRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetRegisteredServiceNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        namespaces: List[str] = None,
        request_id: str = None,
    ):
        self.namespaces = namespaces
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRegisteredServiceNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRegisteredServiceNamespacesResponseBody = None,
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
            temp_model = GetRegisteredServiceNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegisteredServicesRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        service_mesh_id: str = None,
    ):
        self.namespace = namespace
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetRegisteredServicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        services: List[str] = None,
    ):
        self.request_id = request_id
        self.services = services

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.services is not None:
            result['Services'] = self.services
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Services') is not None:
            self.services = m.get('Services')
        return self


class GetRegisteredServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRegisteredServicesResponseBody = None,
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
            temp_model = GetRegisteredServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSaTokenRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        need_refresh: bool = None,
        service_account_name: str = None,
        service_mesh_id: str = None,
    ):
        self.namespace = namespace
        self.need_refresh = need_refresh
        self.service_account_name = service_account_name
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.need_refresh is not None:
            result['NeedRefresh'] = self.need_refresh
        if self.service_account_name is not None:
            result['ServiceAccountName'] = self.service_account_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NeedRefresh') is not None:
            self.need_refresh = m.get('NeedRefresh')
        if m.get('ServiceAccountName') is not None:
            self.service_account_name = m.get('ServiceAccountName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetSaTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        token: str = None,
    ):
        self.request_id = request_id
        # Token of service account
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetSaTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSaTokenResponseBody = None,
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
            temp_model = GetSaTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceMeshSlbRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetServiceMeshSlbResponseBodyData(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        server_health_status: str = None,
        status: str = None,
    ):
        self.load_balancer_id = load_balancer_id
        self.server_health_status = server_health_status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.server_health_status is not None:
            result['ServerHealthStatus'] = self.server_health_status
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ServerHealthStatus') is not None:
            self.server_health_status = m.get('ServerHealthStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetServiceMeshSlbResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetServiceMeshSlbResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetServiceMeshSlbResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetServiceMeshSlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetServiceMeshSlbResponseBody = None,
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
            temp_model = GetServiceMeshSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceRegistrySourceRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetServiceRegistrySourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetServiceRegistrySourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetServiceRegistrySourceResponseBody = None,
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
            temp_model = GetServiceRegistrySourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVmAppMeshInfoRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetVmAppMeshInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVmAppMeshInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVmAppMeshInfoResponseBody = None,
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
            temp_model = GetVmAppMeshInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVmMetaRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        service_account: str = None,
        service_mesh_id: str = None,
        trust_domain: str = None,
    ):
        self.namespace = namespace
        self.service_account = service_account
        self.service_mesh_id = service_mesh_id
        self.trust_domain = trust_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_account is not None:
            result['ServiceAccount'] = self.service_account
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.trust_domain is not None:
            result['TrustDomain'] = self.trust_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceAccount') is not None:
            self.service_account = m.get('ServiceAccount')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('TrustDomain') is not None:
            self.trust_domain = m.get('TrustDomain')
        return self


class GetVmMetaResponseBodyVmMetaInfo(TeaModel):
    def __init__(
        self,
        envoy_env_content: str = None,
        hosts_content: str = None,
        token_content: str = None,
    ):
        self.envoy_env_content = envoy_env_content
        self.hosts_content = hosts_content
        self.token_content = token_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.envoy_env_content is not None:
            result['EnvoyEnvContent'] = self.envoy_env_content
        if self.hosts_content is not None:
            result['HostsContent'] = self.hosts_content
        if self.token_content is not None:
            result['TokenContent'] = self.token_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvoyEnvContent') is not None:
            self.envoy_env_content = m.get('EnvoyEnvContent')
        if m.get('HostsContent') is not None:
            self.hosts_content = m.get('HostsContent')
        if m.get('TokenContent') is not None:
            self.token_content = m.get('TokenContent')
        return self


class GetVmMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vm_meta_info: GetVmMetaResponseBodyVmMetaInfo = None,
    ):
        self.request_id = request_id
        self.vm_meta_info = vm_meta_info

    def validate(self):
        if self.vm_meta_info:
            self.vm_meta_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vm_meta_info is not None:
            result['VmMetaInfo'] = self.vm_meta_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VmMetaInfo') is not None:
            temp_model = GetVmMetaResponseBodyVmMetaInfo()
            self.vm_meta_info = temp_model.from_map(m['VmMetaInfo'])
        return self


class GetVmMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVmMetaResponseBody = None,
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
            temp_model = GetVmMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeASMRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InitializeASMRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitializeASMRoleResponseBody = None,
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
            temp_model = InitializeASMRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBuiltinEnvoyFilterRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        service_mesh_id: str = None,
    ):
        self.id = id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class ListBuiltinEnvoyFilterResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBuiltinEnvoyFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBuiltinEnvoyFilterResponseBody = None,
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
            temp_model = ListBuiltinEnvoyFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBuiltinEnvoyFilterRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        istio_version: str = None,
        name: str = None,
        parameters: str = None,
        service_mesh_id: str = None,
    ):
        self.id = id
        self.istio_version = istio_version
        self.name = name
        self.parameters = parameters
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class ModifyBuiltinEnvoyFilterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBuiltinEnvoyFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBuiltinEnvoyFilterResponseBody = None,
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
            temp_model = ModifyBuiltinEnvoyFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyServiceMeshNameRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        service_mesh_id: str = None,
    ):
        self.name = name
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class ModifyServiceMeshNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyServiceMeshNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyServiceMeshNameResponseBody = None,
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
            temp_model = ModifyServiceMeshNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReActivateAuditRequest(TeaModel):
    def __init__(
        self,
        enable_audit: bool = None,
        service_mesh_id: str = None,
    ):
        self.enable_audit = enable_audit
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class ReActivateAuditResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReActivateAuditResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReActivateAuditResponseBody = None,
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
            temp_model = ReActivateAuditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveBuiltinEnvoyFilterRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        istio_version: str = None,
        name: str = None,
        service_mesh_id: str = None,
    ):
        self.id = id
        self.istio_version = istio_version
        self.name = name
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.name is not None:
            result['Name'] = self.name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class RemoveBuiltinEnvoyFilterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveBuiltinEnvoyFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveBuiltinEnvoyFilterResponseBody = None,
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
            temp_model = RemoveBuiltinEnvoyFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClusterFromServiceMeshRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        service_mesh_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class RemoveClusterFromServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveClusterFromServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveClusterFromServiceMeshResponseBody = None,
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
            temp_model = RemoveClusterFromServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveVMFromServiceMeshRequest(TeaModel):
    def __init__(
        self,
        ecs_id: str = None,
        service_mesh_id: str = None,
    ):
        self.ecs_id = ecs_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class RemoveVMFromServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveVMFromServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveVMFromServiceMeshResponseBody = None,
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
            temp_model = RemoveVMFromServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeKubeconfigRequest(TeaModel):
    def __init__(
        self,
        private_ip_address: bool = None,
        service_mesh_id: str = None,
    ):
        self.private_ip_address = private_ip_address
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class RevokeKubeconfigResponseBody(TeaModel):
    def __init__(
        self,
        kubeconfig: str = None,
        request_id: str = None,
    ):
        self.kubeconfig = kubeconfig
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubeconfig is not None:
            result['Kubeconfig'] = self.kubeconfig
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Kubeconfig') is not None:
            self.kubeconfig = m.get('Kubeconfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeKubeconfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RevokeKubeconfigResponseBody = None,
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
            temp_model = RevokeKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunDiagnosisRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class RunDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RunDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunDiagnosisResponseBody = None,
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
            temp_model = RunDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetServiceRegistrySourceRequest(TeaModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        service_mesh_id: str = None,
    ):
        self.config = config
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class SetServiceRegistrySourceShrinkRequest(TeaModel):
    def __init__(
        self,
        config_shrink: str = None,
        service_mesh_id: str = None,
    ):
        self.config_shrink = config_shrink
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class SetServiceRegistrySourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetServiceRegistrySourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetServiceRegistrySourceResponseBody = None,
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
            temp_model = SetServiceRegistrySourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateControlPlaneLogAlertActionPolicyRequest(TeaModel):
    def __init__(
        self,
        action_policy_id: str = None,
        rule_id: str = None,
        service_mesh_id: str = None,
    ):
        self.action_policy_id = action_policy_id
        self.rule_id = rule_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_policy_id is not None:
            result['ActionPolicyId'] = self.action_policy_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPolicyId') is not None:
            self.action_policy_id = m.get('ActionPolicyId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpdateControlPlaneLogAlertActionPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateControlPlaneLogAlertActionPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateControlPlaneLogAlertActionPolicyResponseBody = None,
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
            temp_model = UpdateControlPlaneLogAlertActionPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateControlPlaneLogConfigRequest(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        project: str = None,
        service_mesh_id: str = None,
    ):
        self.enabled = enabled
        self.project = project
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.project is not None:
            result['Project'] = self.project
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpdateControlPlaneLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateControlPlaneLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateControlPlaneLogConfigResponseBody = None,
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
            temp_model = UpdateControlPlaneLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExtensionProviderRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        service_mesh_id: str = None,
        type: str = None,
    ):
        self.config = config
        self.name = name
        self.service_mesh_id = service_mesh_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateExtensionProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateExtensionProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExtensionProviderResponseBody = None,
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
            temp_model = UpdateExtensionProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIstioInjectionConfigRequest(TeaModel):
    def __init__(
        self,
        enable_istio_injection: bool = None,
        enable_sidecar_set_injection: bool = None,
        namespace: str = None,
        service_mesh_id: str = None,
    ):
        self.enable_istio_injection = enable_istio_injection
        self.enable_sidecar_set_injection = enable_sidecar_set_injection
        self.namespace = namespace
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_istio_injection is not None:
            result['EnableIstioInjection'] = self.enable_istio_injection
        if self.enable_sidecar_set_injection is not None:
            result['EnableSidecarSetInjection'] = self.enable_sidecar_set_injection
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableIstioInjection') is not None:
            self.enable_istio_injection = m.get('EnableIstioInjection')
        if m.get('EnableSidecarSetInjection') is not None:
            self.enable_sidecar_set_injection = m.get('EnableSidecarSetInjection')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpdateIstioInjectionConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateIstioInjectionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateIstioInjectionConfigResponseBody = None,
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
            temp_model = UpdateIstioInjectionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMeshFeatureRequest(TeaModel):
    def __init__(
        self,
        access_log_enabled: bool = None,
        access_log_file: str = None,
        access_log_format: str = None,
        access_log_project: str = None,
        access_log_service_enabled: bool = None,
        access_log_service_host: str = None,
        access_log_service_port: int = None,
        audit_project: str = None,
        auto_injection_policy_enabled: bool = None,
        craggregation_enabled: bool = None,
        cni_enabled: bool = None,
        cni_exclude_namespaces: str = None,
        config_source_enabled: bool = None,
        config_source_nacos_id: str = None,
        customized_prometheus: bool = None,
        customized_zipkin: bool = None,
        dnsproxying_enabled: bool = None,
        discovery_selectors: str = None,
        dubbo_filter_enabled: bool = None,
        enable_audit: bool = None,
        enable_crhistory: bool = None,
        enable_namespaces_by_default: bool = None,
        enable_sdsserver: bool = None,
        exclude_ipranges: str = None,
        exclude_inbound_ports: str = None,
        exclude_outbound_ports: str = None,
        filter_gateway_cluster_config: bool = None,
        gateway_apienabled: bool = None,
        http_10enabled: bool = None,
        include_ipranges: str = None,
        include_inbound_ports: str = None,
        kiali_enabled: bool = None,
        lifecycle: str = None,
        locality_lbconf: str = None,
        locality_load_balancing: bool = None,
        mseenabled: bool = None,
        multi_buffer_enabled: bool = None,
        multi_buffer_poll_delay: str = None,
        mysql_filter_enabled: bool = None,
        opalimit_cpu: str = None,
        opalimit_memory: str = None,
        opalog_level: str = None,
        oparequest_cpu: str = None,
        oparequest_memory: str = None,
        opa_enabled: bool = None,
        open_agent_policy: bool = None,
        outbound_traffic_policy: str = None,
        prometheus_url: str = None,
        proxy_init_cpuresource_limit: str = None,
        proxy_init_cpuresource_request: str = None,
        proxy_init_memory_resource_limit: str = None,
        proxy_init_memory_resource_request: str = None,
        proxy_limit_cpu: str = None,
        proxy_limit_memory: str = None,
        proxy_request_cpu: str = None,
        proxy_request_memory: str = None,
        redis_filter_enabled: bool = None,
        service_mesh_id: str = None,
        sidecar_injector_limit_cpu: str = None,
        sidecar_injector_limit_memory: str = None,
        sidecar_injector_request_cpu: str = None,
        sidecar_injector_request_memory: str = None,
        sidecar_injector_webhook_as_yaml: str = None,
        telemetry: bool = None,
        termination_drain_duration: str = None,
        thrift_filter_enabled: bool = None,
        trace_sampling: float = None,
        tracing: bool = None,
        web_assembly_filter_enabled: bool = None,
    ):
        self.access_log_enabled = access_log_enabled
        self.access_log_file = access_log_file
        self.access_log_format = access_log_format
        self.access_log_project = access_log_project
        self.access_log_service_enabled = access_log_service_enabled
        self.access_log_service_host = access_log_service_host
        self.access_log_service_port = access_log_service_port
        self.audit_project = audit_project
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        self.craggregation_enabled = craggregation_enabled
        self.cni_enabled = cni_enabled
        self.cni_exclude_namespaces = cni_exclude_namespaces
        self.config_source_enabled = config_source_enabled
        self.config_source_nacos_id = config_source_nacos_id
        self.customized_prometheus = customized_prometheus
        self.customized_zipkin = customized_zipkin
        self.dnsproxying_enabled = dnsproxying_enabled
        self.discovery_selectors = discovery_selectors
        self.dubbo_filter_enabled = dubbo_filter_enabled
        self.enable_audit = enable_audit
        self.enable_crhistory = enable_crhistory
        self.enable_namespaces_by_default = enable_namespaces_by_default
        self.enable_sdsserver = enable_sdsserver
        self.exclude_ipranges = exclude_ipranges
        self.exclude_inbound_ports = exclude_inbound_ports
        self.exclude_outbound_ports = exclude_outbound_ports
        self.filter_gateway_cluster_config = filter_gateway_cluster_config
        self.gateway_apienabled = gateway_apienabled
        self.http_10enabled = http_10enabled
        self.include_ipranges = include_ipranges
        self.include_inbound_ports = include_inbound_ports
        self.kiali_enabled = kiali_enabled
        self.lifecycle = lifecycle
        self.locality_lbconf = locality_lbconf
        self.locality_load_balancing = locality_load_balancing
        self.mseenabled = mseenabled
        self.multi_buffer_enabled = multi_buffer_enabled
        self.multi_buffer_poll_delay = multi_buffer_poll_delay
        self.mysql_filter_enabled = mysql_filter_enabled
        self.opalimit_cpu = opalimit_cpu
        self.opalimit_memory = opalimit_memory
        self.opalog_level = opalog_level
        self.oparequest_cpu = oparequest_cpu
        self.oparequest_memory = oparequest_memory
        self.opa_enabled = opa_enabled
        self.open_agent_policy = open_agent_policy
        self.outbound_traffic_policy = outbound_traffic_policy
        self.prometheus_url = prometheus_url
        self.proxy_init_cpuresource_limit = proxy_init_cpuresource_limit
        self.proxy_init_cpuresource_request = proxy_init_cpuresource_request
        self.proxy_init_memory_resource_limit = proxy_init_memory_resource_limit
        self.proxy_init_memory_resource_request = proxy_init_memory_resource_request
        self.proxy_limit_cpu = proxy_limit_cpu
        self.proxy_limit_memory = proxy_limit_memory
        self.proxy_request_cpu = proxy_request_cpu
        self.proxy_request_memory = proxy_request_memory
        self.redis_filter_enabled = redis_filter_enabled
        self.service_mesh_id = service_mesh_id
        self.sidecar_injector_limit_cpu = sidecar_injector_limit_cpu
        self.sidecar_injector_limit_memory = sidecar_injector_limit_memory
        self.sidecar_injector_request_cpu = sidecar_injector_request_cpu
        self.sidecar_injector_request_memory = sidecar_injector_request_memory
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml
        self.telemetry = telemetry
        self.termination_drain_duration = termination_drain_duration
        self.thrift_filter_enabled = thrift_filter_enabled
        self.trace_sampling = trace_sampling
        self.tracing = tracing
        self.web_assembly_filter_enabled = web_assembly_filter_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_enabled is not None:
            result['AccessLogEnabled'] = self.access_log_enabled
        if self.access_log_file is not None:
            result['AccessLogFile'] = self.access_log_file
        if self.access_log_format is not None:
            result['AccessLogFormat'] = self.access_log_format
        if self.access_log_project is not None:
            result['AccessLogProject'] = self.access_log_project
        if self.access_log_service_enabled is not None:
            result['AccessLogServiceEnabled'] = self.access_log_service_enabled
        if self.access_log_service_host is not None:
            result['AccessLogServiceHost'] = self.access_log_service_host
        if self.access_log_service_port is not None:
            result['AccessLogServicePort'] = self.access_log_service_port
        if self.audit_project is not None:
            result['AuditProject'] = self.audit_project
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.craggregation_enabled is not None:
            result['CRAggregationEnabled'] = self.craggregation_enabled
        if self.cni_enabled is not None:
            result['CniEnabled'] = self.cni_enabled
        if self.cni_exclude_namespaces is not None:
            result['CniExcludeNamespaces'] = self.cni_exclude_namespaces
        if self.config_source_enabled is not None:
            result['ConfigSourceEnabled'] = self.config_source_enabled
        if self.config_source_nacos_id is not None:
            result['ConfigSourceNacosID'] = self.config_source_nacos_id
        if self.customized_prometheus is not None:
            result['CustomizedPrometheus'] = self.customized_prometheus
        if self.customized_zipkin is not None:
            result['CustomizedZipkin'] = self.customized_zipkin
        if self.dnsproxying_enabled is not None:
            result['DNSProxyingEnabled'] = self.dnsproxying_enabled
        if self.discovery_selectors is not None:
            result['DiscoverySelectors'] = self.discovery_selectors
        if self.dubbo_filter_enabled is not None:
            result['DubboFilterEnabled'] = self.dubbo_filter_enabled
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
        if self.enable_crhistory is not None:
            result['EnableCRHistory'] = self.enable_crhistory
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.enable_sdsserver is not None:
            result['EnableSDSServer'] = self.enable_sdsserver
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.filter_gateway_cluster_config is not None:
            result['FilterGatewayClusterConfig'] = self.filter_gateway_cluster_config
        if self.gateway_apienabled is not None:
            result['GatewayAPIEnabled'] = self.gateway_apienabled
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.include_inbound_ports is not None:
            result['IncludeInboundPorts'] = self.include_inbound_ports
        if self.kiali_enabled is not None:
            result['KialiEnabled'] = self.kiali_enabled
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.locality_lbconf is not None:
            result['LocalityLBConf'] = self.locality_lbconf
        if self.locality_load_balancing is not None:
            result['LocalityLoadBalancing'] = self.locality_load_balancing
        if self.mseenabled is not None:
            result['MSEEnabled'] = self.mseenabled
        if self.multi_buffer_enabled is not None:
            result['MultiBufferEnabled'] = self.multi_buffer_enabled
        if self.multi_buffer_poll_delay is not None:
            result['MultiBufferPollDelay'] = self.multi_buffer_poll_delay
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.opalimit_cpu is not None:
            result['OPALimitCPU'] = self.opalimit_cpu
        if self.opalimit_memory is not None:
            result['OPALimitMemory'] = self.opalimit_memory
        if self.opalog_level is not None:
            result['OPALogLevel'] = self.opalog_level
        if self.oparequest_cpu is not None:
            result['OPARequestCPU'] = self.oparequest_cpu
        if self.oparequest_memory is not None:
            result['OPARequestMemory'] = self.oparequest_memory
        if self.opa_enabled is not None:
            result['OpaEnabled'] = self.opa_enabled
        if self.open_agent_policy is not None:
            result['OpenAgentPolicy'] = self.open_agent_policy
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.prometheus_url is not None:
            result['PrometheusUrl'] = self.prometheus_url
        if self.proxy_init_cpuresource_limit is not None:
            result['ProxyInitCPUResourceLimit'] = self.proxy_init_cpuresource_limit
        if self.proxy_init_cpuresource_request is not None:
            result['ProxyInitCPUResourceRequest'] = self.proxy_init_cpuresource_request
        if self.proxy_init_memory_resource_limit is not None:
            result['ProxyInitMemoryResourceLimit'] = self.proxy_init_memory_resource_limit
        if self.proxy_init_memory_resource_request is not None:
            result['ProxyInitMemoryResourceRequest'] = self.proxy_init_memory_resource_request
        if self.proxy_limit_cpu is not None:
            result['ProxyLimitCPU'] = self.proxy_limit_cpu
        if self.proxy_limit_memory is not None:
            result['ProxyLimitMemory'] = self.proxy_limit_memory
        if self.proxy_request_cpu is not None:
            result['ProxyRequestCPU'] = self.proxy_request_cpu
        if self.proxy_request_memory is not None:
            result['ProxyRequestMemory'] = self.proxy_request_memory
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.sidecar_injector_limit_cpu is not None:
            result['SidecarInjectorLimitCPU'] = self.sidecar_injector_limit_cpu
        if self.sidecar_injector_limit_memory is not None:
            result['SidecarInjectorLimitMemory'] = self.sidecar_injector_limit_memory
        if self.sidecar_injector_request_cpu is not None:
            result['SidecarInjectorRequestCPU'] = self.sidecar_injector_request_cpu
        if self.sidecar_injector_request_memory is not None:
            result['SidecarInjectorRequestMemory'] = self.sidecar_injector_request_memory
        if self.sidecar_injector_webhook_as_yaml is not None:
            result['SidecarInjectorWebhookAsYaml'] = self.sidecar_injector_webhook_as_yaml
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.termination_drain_duration is not None:
            result['TerminationDrainDuration'] = self.termination_drain_duration
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.web_assembly_filter_enabled is not None:
            result['WebAssemblyFilterEnabled'] = self.web_assembly_filter_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogEnabled') is not None:
            self.access_log_enabled = m.get('AccessLogEnabled')
        if m.get('AccessLogFile') is not None:
            self.access_log_file = m.get('AccessLogFile')
        if m.get('AccessLogFormat') is not None:
            self.access_log_format = m.get('AccessLogFormat')
        if m.get('AccessLogProject') is not None:
            self.access_log_project = m.get('AccessLogProject')
        if m.get('AccessLogServiceEnabled') is not None:
            self.access_log_service_enabled = m.get('AccessLogServiceEnabled')
        if m.get('AccessLogServiceHost') is not None:
            self.access_log_service_host = m.get('AccessLogServiceHost')
        if m.get('AccessLogServicePort') is not None:
            self.access_log_service_port = m.get('AccessLogServicePort')
        if m.get('AuditProject') is not None:
            self.audit_project = m.get('AuditProject')
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('CRAggregationEnabled') is not None:
            self.craggregation_enabled = m.get('CRAggregationEnabled')
        if m.get('CniEnabled') is not None:
            self.cni_enabled = m.get('CniEnabled')
        if m.get('CniExcludeNamespaces') is not None:
            self.cni_exclude_namespaces = m.get('CniExcludeNamespaces')
        if m.get('ConfigSourceEnabled') is not None:
            self.config_source_enabled = m.get('ConfigSourceEnabled')
        if m.get('ConfigSourceNacosID') is not None:
            self.config_source_nacos_id = m.get('ConfigSourceNacosID')
        if m.get('CustomizedPrometheus') is not None:
            self.customized_prometheus = m.get('CustomizedPrometheus')
        if m.get('CustomizedZipkin') is not None:
            self.customized_zipkin = m.get('CustomizedZipkin')
        if m.get('DNSProxyingEnabled') is not None:
            self.dnsproxying_enabled = m.get('DNSProxyingEnabled')
        if m.get('DiscoverySelectors') is not None:
            self.discovery_selectors = m.get('DiscoverySelectors')
        if m.get('DubboFilterEnabled') is not None:
            self.dubbo_filter_enabled = m.get('DubboFilterEnabled')
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
        if m.get('EnableCRHistory') is not None:
            self.enable_crhistory = m.get('EnableCRHistory')
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('EnableSDSServer') is not None:
            self.enable_sdsserver = m.get('EnableSDSServer')
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('FilterGatewayClusterConfig') is not None:
            self.filter_gateway_cluster_config = m.get('FilterGatewayClusterConfig')
        if m.get('GatewayAPIEnabled') is not None:
            self.gateway_apienabled = m.get('GatewayAPIEnabled')
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('IncludeInboundPorts') is not None:
            self.include_inbound_ports = m.get('IncludeInboundPorts')
        if m.get('KialiEnabled') is not None:
            self.kiali_enabled = m.get('KialiEnabled')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('LocalityLBConf') is not None:
            self.locality_lbconf = m.get('LocalityLBConf')
        if m.get('LocalityLoadBalancing') is not None:
            self.locality_load_balancing = m.get('LocalityLoadBalancing')
        if m.get('MSEEnabled') is not None:
            self.mseenabled = m.get('MSEEnabled')
        if m.get('MultiBufferEnabled') is not None:
            self.multi_buffer_enabled = m.get('MultiBufferEnabled')
        if m.get('MultiBufferPollDelay') is not None:
            self.multi_buffer_poll_delay = m.get('MultiBufferPollDelay')
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('OPALimitCPU') is not None:
            self.opalimit_cpu = m.get('OPALimitCPU')
        if m.get('OPALimitMemory') is not None:
            self.opalimit_memory = m.get('OPALimitMemory')
        if m.get('OPALogLevel') is not None:
            self.opalog_level = m.get('OPALogLevel')
        if m.get('OPARequestCPU') is not None:
            self.oparequest_cpu = m.get('OPARequestCPU')
        if m.get('OPARequestMemory') is not None:
            self.oparequest_memory = m.get('OPARequestMemory')
        if m.get('OpaEnabled') is not None:
            self.opa_enabled = m.get('OpaEnabled')
        if m.get('OpenAgentPolicy') is not None:
            self.open_agent_policy = m.get('OpenAgentPolicy')
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('PrometheusUrl') is not None:
            self.prometheus_url = m.get('PrometheusUrl')
        if m.get('ProxyInitCPUResourceLimit') is not None:
            self.proxy_init_cpuresource_limit = m.get('ProxyInitCPUResourceLimit')
        if m.get('ProxyInitCPUResourceRequest') is not None:
            self.proxy_init_cpuresource_request = m.get('ProxyInitCPUResourceRequest')
        if m.get('ProxyInitMemoryResourceLimit') is not None:
            self.proxy_init_memory_resource_limit = m.get('ProxyInitMemoryResourceLimit')
        if m.get('ProxyInitMemoryResourceRequest') is not None:
            self.proxy_init_memory_resource_request = m.get('ProxyInitMemoryResourceRequest')
        if m.get('ProxyLimitCPU') is not None:
            self.proxy_limit_cpu = m.get('ProxyLimitCPU')
        if m.get('ProxyLimitMemory') is not None:
            self.proxy_limit_memory = m.get('ProxyLimitMemory')
        if m.get('ProxyRequestCPU') is not None:
            self.proxy_request_cpu = m.get('ProxyRequestCPU')
        if m.get('ProxyRequestMemory') is not None:
            self.proxy_request_memory = m.get('ProxyRequestMemory')
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('SidecarInjectorLimitCPU') is not None:
            self.sidecar_injector_limit_cpu = m.get('SidecarInjectorLimitCPU')
        if m.get('SidecarInjectorLimitMemory') is not None:
            self.sidecar_injector_limit_memory = m.get('SidecarInjectorLimitMemory')
        if m.get('SidecarInjectorRequestCPU') is not None:
            self.sidecar_injector_request_cpu = m.get('SidecarInjectorRequestCPU')
        if m.get('SidecarInjectorRequestMemory') is not None:
            self.sidecar_injector_request_memory = m.get('SidecarInjectorRequestMemory')
        if m.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = m.get('SidecarInjectorWebhookAsYaml')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('TerminationDrainDuration') is not None:
            self.termination_drain_duration = m.get('TerminationDrainDuration')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('WebAssemblyFilterEnabled') is not None:
            self.web_assembly_filter_enabled = m.get('WebAssemblyFilterEnabled')
        return self


class UpdateMeshFeatureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateMeshFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMeshFeatureResponseBody = None,
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
            temp_model = UpdateMeshFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceScopeSidecarConfigRequest(TeaModel):
    def __init__(
        self,
        exclude_ipranges: str = None,
        exclude_inbound_ports: str = None,
        exclude_outbound_ports: str = None,
        include_ipranges: str = None,
        include_inbound_ports: str = None,
        include_outbound_ports: str = None,
        istio_dnsproxy_enabled: bool = None,
        lifecycle: str = None,
        namespace: str = None,
        proxy_init_cpuresource_limit: str = None,
        proxy_init_cpuresource_request: str = None,
        proxy_init_memory_resource_limit: str = None,
        proxy_init_memory_resource_request: str = None,
        service_mesh_id: str = None,
        sidecar_proxy_cpuresource_limit: str = None,
        sidecar_proxy_cpuresource_request: str = None,
        sidecar_proxy_memory_resource_limit: str = None,
        sidecar_proxy_memory_resource_request: str = None,
        termination_drain_duration: str = None,
    ):
        self.exclude_ipranges = exclude_ipranges
        self.exclude_inbound_ports = exclude_inbound_ports
        self.exclude_outbound_ports = exclude_outbound_ports
        self.include_ipranges = include_ipranges
        self.include_inbound_ports = include_inbound_ports
        self.include_outbound_ports = include_outbound_ports
        self.istio_dnsproxy_enabled = istio_dnsproxy_enabled
        self.lifecycle = lifecycle
        self.namespace = namespace
        self.proxy_init_cpuresource_limit = proxy_init_cpuresource_limit
        self.proxy_init_cpuresource_request = proxy_init_cpuresource_request
        self.proxy_init_memory_resource_limit = proxy_init_memory_resource_limit
        self.proxy_init_memory_resource_request = proxy_init_memory_resource_request
        self.service_mesh_id = service_mesh_id
        self.sidecar_proxy_cpuresource_limit = sidecar_proxy_cpuresource_limit
        self.sidecar_proxy_cpuresource_request = sidecar_proxy_cpuresource_request
        self.sidecar_proxy_memory_resource_limit = sidecar_proxy_memory_resource_limit
        self.sidecar_proxy_memory_resource_request = sidecar_proxy_memory_resource_request
        self.termination_drain_duration = termination_drain_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.include_inbound_ports is not None:
            result['IncludeInboundPorts'] = self.include_inbound_ports
        if self.include_outbound_ports is not None:
            result['IncludeOutboundPorts'] = self.include_outbound_ports
        if self.istio_dnsproxy_enabled is not None:
            result['IstioDNSProxyEnabled'] = self.istio_dnsproxy_enabled
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.proxy_init_cpuresource_limit is not None:
            result['ProxyInitCPUResourceLimit'] = self.proxy_init_cpuresource_limit
        if self.proxy_init_cpuresource_request is not None:
            result['ProxyInitCPUResourceRequest'] = self.proxy_init_cpuresource_request
        if self.proxy_init_memory_resource_limit is not None:
            result['ProxyInitMemoryResourceLimit'] = self.proxy_init_memory_resource_limit
        if self.proxy_init_memory_resource_request is not None:
            result['ProxyInitMemoryResourceRequest'] = self.proxy_init_memory_resource_request
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.sidecar_proxy_cpuresource_limit is not None:
            result['SidecarProxyCPUResourceLimit'] = self.sidecar_proxy_cpuresource_limit
        if self.sidecar_proxy_cpuresource_request is not None:
            result['SidecarProxyCPUResourceRequest'] = self.sidecar_proxy_cpuresource_request
        if self.sidecar_proxy_memory_resource_limit is not None:
            result['SidecarProxyMemoryResourceLimit'] = self.sidecar_proxy_memory_resource_limit
        if self.sidecar_proxy_memory_resource_request is not None:
            result['SidecarProxyMemoryResourceRequest'] = self.sidecar_proxy_memory_resource_request
        if self.termination_drain_duration is not None:
            result['TerminationDrainDuration'] = self.termination_drain_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('IncludeInboundPorts') is not None:
            self.include_inbound_ports = m.get('IncludeInboundPorts')
        if m.get('IncludeOutboundPorts') is not None:
            self.include_outbound_ports = m.get('IncludeOutboundPorts')
        if m.get('IstioDNSProxyEnabled') is not None:
            self.istio_dnsproxy_enabled = m.get('IstioDNSProxyEnabled')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ProxyInitCPUResourceLimit') is not None:
            self.proxy_init_cpuresource_limit = m.get('ProxyInitCPUResourceLimit')
        if m.get('ProxyInitCPUResourceRequest') is not None:
            self.proxy_init_cpuresource_request = m.get('ProxyInitCPUResourceRequest')
        if m.get('ProxyInitMemoryResourceLimit') is not None:
            self.proxy_init_memory_resource_limit = m.get('ProxyInitMemoryResourceLimit')
        if m.get('ProxyInitMemoryResourceRequest') is not None:
            self.proxy_init_memory_resource_request = m.get('ProxyInitMemoryResourceRequest')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('SidecarProxyCPUResourceLimit') is not None:
            self.sidecar_proxy_cpuresource_limit = m.get('SidecarProxyCPUResourceLimit')
        if m.get('SidecarProxyCPUResourceRequest') is not None:
            self.sidecar_proxy_cpuresource_request = m.get('SidecarProxyCPUResourceRequest')
        if m.get('SidecarProxyMemoryResourceLimit') is not None:
            self.sidecar_proxy_memory_resource_limit = m.get('SidecarProxyMemoryResourceLimit')
        if m.get('SidecarProxyMemoryResourceRequest') is not None:
            self.sidecar_proxy_memory_resource_request = m.get('SidecarProxyMemoryResourceRequest')
        if m.get('TerminationDrainDuration') is not None:
            self.termination_drain_duration = m.get('TerminationDrainDuration')
        return self


class UpdateNamespaceScopeSidecarConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNamespaceScopeSidecarConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNamespaceScopeSidecarConfigResponseBody = None,
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
            temp_model = UpdateNamespaceScopeSidecarConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeMeshVersionRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpgradeMeshVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeMeshVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeMeshVersionResponseBody = None,
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
            temp_model = UpgradeMeshVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


