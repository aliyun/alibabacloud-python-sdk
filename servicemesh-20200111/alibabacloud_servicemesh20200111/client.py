# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_servicemesh20200111 import models as servicemesh_20200111_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('servicemesh', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_builtin_envoy_filter_with_options(
        self,
        request: servicemesh_20200111_models.AddBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddBuiltinEnvoyFilter',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_builtin_envoy_filter_with_options_async(
        self,
        request: servicemesh_20200111_models.AddBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddBuiltinEnvoyFilter',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_builtin_envoy_filter(
        self,
        request: servicemesh_20200111_models.AddBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_builtin_envoy_filter_with_options(request, runtime)

    async def add_builtin_envoy_filter_async(
        self,
        request: servicemesh_20200111_models.AddBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_builtin_envoy_filter_with_options_async(request, runtime)

    def add_cluster_into_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddClusterIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddClusterIntoServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cluster_into_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddClusterIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddClusterIntoServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cluster_into_service_mesh(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cluster_into_service_mesh_with_options(request, runtime)

    async def add_cluster_into_service_mesh_async(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cluster_into_service_mesh_with_options_async(request, runtime)

    def add_mesh_tag_to_ecs_with_options(
        self,
        request: servicemesh_20200111_models.AddMeshTagToEcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddMeshTagToEcsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMeshTagToEcs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddMeshTagToEcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_mesh_tag_to_ecs_with_options_async(
        self,
        request: servicemesh_20200111_models.AddMeshTagToEcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddMeshTagToEcsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMeshTagToEcs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddMeshTagToEcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_mesh_tag_to_ecs(
        self,
        request: servicemesh_20200111_models.AddMeshTagToEcsRequest,
    ) -> servicemesh_20200111_models.AddMeshTagToEcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_mesh_tag_to_ecs_with_options(request, runtime)

    async def add_mesh_tag_to_ecs_async(
        self,
        request: servicemesh_20200111_models.AddMeshTagToEcsRequest,
    ) -> servicemesh_20200111_models.AddMeshTagToEcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_mesh_tag_to_ecs_with_options_async(request, runtime)

    def add_vminto_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVMIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddVMIntoServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vminto_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVMIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddVMIntoServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vminto_service_mesh(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_vminto_service_mesh_with_options(request, runtime)

    async def add_vminto_service_mesh_async(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_vminto_service_mesh_with_options_async(request, runtime)

    def create_extension_provider_with_options(
        self,
        request: servicemesh_20200111_models.CreateExtensionProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateExtensionProviderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExtensionProvider',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateExtensionProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_extension_provider_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateExtensionProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateExtensionProviderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExtensionProvider',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateExtensionProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_extension_provider(
        self,
        request: servicemesh_20200111_models.CreateExtensionProviderRequest,
    ) -> servicemesh_20200111_models.CreateExtensionProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_extension_provider_with_options(request, runtime)

    async def create_extension_provider_async(
        self,
        request: servicemesh_20200111_models.CreateExtensionProviderRequest,
    ) -> servicemesh_20200111_models.CreateExtensionProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_extension_provider_with_options_async(request, runtime)

    def create_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.api_server_public_eip):
            body['ApiServerPublicEip'] = request.api_server_public_eip
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.control_plane_log_enabled):
            body['ControlPlaneLogEnabled'] = request.control_plane_log_enabled
        if not UtilClient.is_unset(request.control_plane_log_project):
            body['ControlPlaneLogProject'] = request.control_plane_log_project
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.edition):
            body['Edition'] = request.edition
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.api_server_public_eip):
            body['ApiServerPublicEip'] = request.api_server_public_eip
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.control_plane_log_enabled):
            body['ControlPlaneLogEnabled'] = request.control_plane_log_enabled
        if not UtilClient.is_unset(request.control_plane_log_project):
            body['ControlPlaneLogProject'] = request.control_plane_log_project
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.edition):
            body['Edition'] = request.edition
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_mesh(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_mesh_with_options(request, runtime)

    async def create_service_mesh_async(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_mesh_with_options_async(request, runtime)

    def delete_extension_provider_with_options(
        self,
        request: servicemesh_20200111_models.DeleteExtensionProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteExtensionProviderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteExtensionProvider',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteExtensionProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_extension_provider_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteExtensionProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteExtensionProviderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteExtensionProvider',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteExtensionProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_extension_provider(
        self,
        request: servicemesh_20200111_models.DeleteExtensionProviderRequest,
    ) -> servicemesh_20200111_models.DeleteExtensionProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_extension_provider_with_options(request, runtime)

    async def delete_extension_provider_async(
        self,
        request: servicemesh_20200111_models.DeleteExtensionProviderRequest,
    ) -> servicemesh_20200111_models.DeleteExtensionProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_extension_provider_with_options_async(request, runtime)

    def delete_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.retain_resources):
            body['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.retain_resources):
            body['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_mesh(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_mesh_with_options(request, runtime)

    async def delete_service_mesh_async(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_mesh_with_options_async(request, runtime)

    def describe_alert_action_policies_with_options(
        self,
        request: servicemesh_20200111_models.DescribeAlertActionPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeAlertActionPoliciesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertActionPolicies',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeAlertActionPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_action_policies_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeAlertActionPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeAlertActionPoliciesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertActionPolicies',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeAlertActionPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_action_policies(
        self,
        request: servicemesh_20200111_models.DescribeAlertActionPoliciesRequest,
    ) -> servicemesh_20200111_models.DescribeAlertActionPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_action_policies_with_options(request, runtime)

    async def describe_alert_action_policies_async(
        self,
        request: servicemesh_20200111_models.DescribeAlertActionPoliciesRequest,
    ) -> servicemesh_20200111_models.DescribeAlertActionPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_action_policies_with_options_async(request, runtime)

    def describe_available_nacos_instances_with_options(
        self,
        request: servicemesh_20200111_models.DescribeAvailableNacosInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableNacosInstances',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_nacos_instances_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeAvailableNacosInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableNacosInstances',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_nacos_instances(
        self,
        request: servicemesh_20200111_models.DescribeAvailableNacosInstancesRequest,
    ) -> servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_nacos_instances_with_options(request, runtime)

    async def describe_available_nacos_instances_async(
        self,
        request: servicemesh_20200111_models.DescribeAvailableNacosInstancesRequest,
    ) -> servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_nacos_instances_with_options_async(request, runtime)

    def describe_cens_with_options(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCensResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cens_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cens(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    async def describe_cens_async(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cens_with_options_async(request, runtime)

    def describe_cluster_grafana_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterGrafana',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_grafana_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterGrafana',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterGrafanaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_grafana(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_grafana_with_options(request, runtime)

    async def describe_cluster_grafana_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_grafana_with_options_async(request, runtime)

    def describe_cluster_prometheus_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.k_8s_cluster_region_id):
            query['K8sClusterRegionId'] = request.k_8s_cluster_region_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterPrometheus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterPrometheusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_prometheus_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.k_8s_cluster_region_id):
            query['K8sClusterRegionId'] = request.k_8s_cluster_region_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterPrometheus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterPrometheusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_prometheus(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_prometheus_with_options(request, runtime)

    async def describe_cluster_prometheus_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_prometheus_with_options_async(request, runtime)

    def describe_clusters_in_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClustersInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClustersInServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_clusters_in_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClustersInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClustersInServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clusters_in_service_mesh(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_in_service_mesh_with_options(request, runtime)

    async def describe_clusters_in_service_mesh_async(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_clusters_in_service_mesh_with_options_async(request, runtime)

    def describe_control_plane_log_alert_rules_with_options(
        self,
        request: servicemesh_20200111_models.DescribeControlPlaneLogAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeControlPlaneLogAlertRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeControlPlaneLogAlertRules',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeControlPlaneLogAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_control_plane_log_alert_rules_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeControlPlaneLogAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeControlPlaneLogAlertRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeControlPlaneLogAlertRules',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeControlPlaneLogAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_control_plane_log_alert_rules(
        self,
        request: servicemesh_20200111_models.DescribeControlPlaneLogAlertRulesRequest,
    ) -> servicemesh_20200111_models.DescribeControlPlaneLogAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_control_plane_log_alert_rules_with_options(request, runtime)

    async def describe_control_plane_log_alert_rules_async(
        self,
        request: servicemesh_20200111_models.DescribeControlPlaneLogAlertRulesRequest,
    ) -> servicemesh_20200111_models.DescribeControlPlaneLogAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_control_plane_log_alert_rules_with_options_async(request, runtime)

    def describe_cr_templates_with_options(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kind):
            body['Kind'] = request.kind
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCrTemplates',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCrTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cr_templates_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kind):
            body['Kind'] = request.kind
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCrTemplates',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCrTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cr_templates(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cr_templates_with_options(request, runtime)

    async def describe_cr_templates_async(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cr_templates_with_options_async(request, runtime)

    def describe_extension_provider_with_options(
        self,
        request: servicemesh_20200111_models.DescribeExtensionProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeExtensionProviderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExtensionProvider',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeExtensionProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_extension_provider_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeExtensionProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeExtensionProviderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExtensionProvider',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeExtensionProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_extension_provider(
        self,
        request: servicemesh_20200111_models.DescribeExtensionProviderRequest,
    ) -> servicemesh_20200111_models.DescribeExtensionProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_extension_provider_with_options(request, runtime)

    async def describe_extension_provider_async(
        self,
        request: servicemesh_20200111_models.DescribeExtensionProviderRequest,
    ) -> servicemesh_20200111_models.DescribeExtensionProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_extension_provider_with_options_async(request, runtime)

    def describe_guest_cluster_access_log_dashboards_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterAccessLogDashboards',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_guest_cluster_access_log_dashboards_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterAccessLogDashboards',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_guest_cluster_access_log_dashboards(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_guest_cluster_access_log_dashboards_with_options(request, runtime)

    async def describe_guest_cluster_access_log_dashboards_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_guest_cluster_access_log_dashboards_with_options_async(request, runtime)

    def describe_guest_cluster_namespaces_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_guest_cluster_namespaces_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_guest_cluster_namespaces(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_guest_cluster_namespaces_with_options(request, runtime)

    async def describe_guest_cluster_namespaces_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_guest_cluster_namespaces_with_options_async(request, runtime)

    def describe_guest_cluster_pods_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterPods',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterPodsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_guest_cluster_pods_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterPods',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterPodsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_guest_cluster_pods(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_guest_cluster_pods_with_options(request, runtime)

    async def describe_guest_cluster_pods_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_guest_cluster_pods_with_options_async(request, runtime)

    def describe_ingress_gateways_with_options(
        self,
        request: servicemesh_20200111_models.DescribeIngressGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIngressGatewaysResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIngressGateways',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIngressGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ingress_gateways_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeIngressGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIngressGatewaysResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIngressGateways',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIngressGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ingress_gateways(
        self,
        request: servicemesh_20200111_models.DescribeIngressGatewaysRequest,
    ) -> servicemesh_20200111_models.DescribeIngressGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ingress_gateways_with_options(request, runtime)

    async def describe_ingress_gateways_async(
        self,
        request: servicemesh_20200111_models.DescribeIngressGatewaysRequest,
    ) -> servicemesh_20200111_models.DescribeIngressGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ingress_gateways_with_options_async(request, runtime)

    def describe_namespace_scope_sidecar_config_with_options(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_scope_sidecar_config_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace_scope_sidecar_config(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_namespace_scope_sidecar_config_with_options(request, runtime)

    async def describe_namespace_scope_sidecar_config_async(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_namespace_scope_sidecar_config_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: servicemesh_20200111_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: servicemesh_20200111_models.DescribeRegionsRequest,
    ) -> servicemesh_20200111_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: servicemesh_20200111_models.DescribeRegionsRequest,
    ) -> servicemesh_20200111_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_service_mesh_detail_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_detail_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_detail(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_detail_with_options(request, runtime)

    async def describe_service_mesh_detail_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_detail_with_options_async(request, runtime)

    def describe_service_mesh_gateway_pod_status_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshGatewayPodStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshGatewayPodStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.gateway_full_name):
            body['GatewayFullName'] = request.gateway_full_name
        if not UtilClient.is_unset(request.guest_cluster_ids):
            body['GuestClusterIds'] = request.guest_cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshGatewayPodStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshGatewayPodStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_gateway_pod_status_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshGatewayPodStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshGatewayPodStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.gateway_full_name):
            body['GatewayFullName'] = request.gateway_full_name
        if not UtilClient.is_unset(request.guest_cluster_ids):
            body['GuestClusterIds'] = request.guest_cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshGatewayPodStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshGatewayPodStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_gateway_pod_status(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshGatewayPodStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshGatewayPodStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_gateway_pod_status_with_options(request, runtime)

    async def describe_service_mesh_gateway_pod_status_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshGatewayPodStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshGatewayPodStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_gateway_pod_status_with_options_async(request, runtime)

    def describe_service_mesh_gateway_slbstatus_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshGatewaySLBStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshGatewaySLBStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.gateway_addresses):
            body['GatewayAddresses'] = request.gateway_addresses
        if not UtilClient.is_unset(request.gateway_full_name):
            body['GatewayFullName'] = request.gateway_full_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshGatewaySLBStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshGatewaySLBStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_gateway_slbstatus_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshGatewaySLBStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshGatewaySLBStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.gateway_addresses):
            body['GatewayAddresses'] = request.gateway_addresses
        if not UtilClient.is_unset(request.gateway_full_name):
            body['GatewayFullName'] = request.gateway_full_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshGatewaySLBStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshGatewaySLBStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_gateway_slbstatus(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshGatewaySLBStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshGatewaySLBStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_gateway_slbstatus_with_options(request, runtime)

    async def describe_service_mesh_gateway_slbstatus_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshGatewaySLBStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshGatewaySLBStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_gateway_slbstatus_with_options_async(request, runtime)

    def describe_service_mesh_kubeconfig_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_kubeconfig_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_kubeconfig(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_kubeconfig_with_options(request, runtime)

    async def describe_service_mesh_kubeconfig_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_kubeconfig_with_options_async(request, runtime)

    def describe_service_mesh_upgrade_status_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.all_istio_gateway_full_names):
            body['AllIstioGatewayFullNames'] = request.all_istio_gateway_full_names
        if not UtilClient.is_unset(request.guest_cluster_ids):
            body['GuestClusterIds'] = request.guest_cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshUpgradeStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_upgrade_status_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.all_istio_gateway_full_names):
            body['AllIstioGatewayFullNames'] = request.all_istio_gateway_full_names
        if not UtilClient.is_unset(request.guest_cluster_ids):
            body['GuestClusterIds'] = request.guest_cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshUpgradeStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_upgrade_status(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_upgrade_status_with_options(request, runtime)

    async def describe_service_mesh_upgrade_status_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_upgrade_status_with_options_async(request, runtime)

    def describe_service_mesh_vms_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshVMs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshVMsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_vms_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshVMs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshVMsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_vms(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_vms_with_options(request, runtime)

    async def describe_service_mesh_vms_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_vms_with_options_async(request, runtime)

    def describe_service_meshes_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeServiceMeshes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_meshes_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeServiceMeshes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_meshes(self) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_meshes_with_options(runtime)

    async def describe_service_meshes_async(self) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_meshes_with_options_async(runtime)

    def describe_upgrade_version_with_options(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpgradeVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUpgradeVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_upgrade_version_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpgradeVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUpgradeVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_upgrade_version(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_upgrade_version_with_options(request, runtime)

    async def describe_upgrade_version_async(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_upgrade_version_with_options_async(request, runtime)

    def describe_vms_in_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVMsInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVMsInServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vms_in_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVMsInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVMsInServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vms_in_service_mesh(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vms_in_service_mesh_with_options(request, runtime)

    async def describe_vms_in_service_mesh_async(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vms_in_service_mesh_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vswitches(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_versions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVersionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVersions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_versions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVersionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVersions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_versions(self) -> servicemesh_20200111_models.DescribeVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_versions_with_options(runtime)

    async def describe_versions_async(self) -> servicemesh_20200111_models.DescribeVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_versions_with_options_async(runtime)

    def describe_vpcs_with_options(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVpcs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpcs_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVpcs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVpcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpcs(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    async def describe_vpcs_async(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpcs_with_options_async(request, runtime)

    def disable_control_plane_log_alert_with_options(
        self,
        request: servicemesh_20200111_models.DisableControlPlaneLogAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DisableControlPlaneLogAlertResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableControlPlaneLogAlert',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DisableControlPlaneLogAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_control_plane_log_alert_with_options_async(
        self,
        request: servicemesh_20200111_models.DisableControlPlaneLogAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DisableControlPlaneLogAlertResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableControlPlaneLogAlert',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DisableControlPlaneLogAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_control_plane_log_alert(
        self,
        request: servicemesh_20200111_models.DisableControlPlaneLogAlertRequest,
    ) -> servicemesh_20200111_models.DisableControlPlaneLogAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_control_plane_log_alert_with_options(request, runtime)

    async def disable_control_plane_log_alert_async(
        self,
        request: servicemesh_20200111_models.DisableControlPlaneLogAlertRequest,
    ) -> servicemesh_20200111_models.DisableControlPlaneLogAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_control_plane_log_alert_with_options_async(request, runtime)

    def enable_control_plane_log_alert_with_options(
        self,
        request: servicemesh_20200111_models.EnableControlPlaneLogAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.EnableControlPlaneLogAlertResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_policy_id):
            body['ActionPolicyId'] = request.action_policy_id
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableControlPlaneLogAlert',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.EnableControlPlaneLogAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_control_plane_log_alert_with_options_async(
        self,
        request: servicemesh_20200111_models.EnableControlPlaneLogAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.EnableControlPlaneLogAlertResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_policy_id):
            body['ActionPolicyId'] = request.action_policy_id
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableControlPlaneLogAlert',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.EnableControlPlaneLogAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_control_plane_log_alert(
        self,
        request: servicemesh_20200111_models.EnableControlPlaneLogAlertRequest,
    ) -> servicemesh_20200111_models.EnableControlPlaneLogAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_control_plane_log_alert_with_options(request, runtime)

    async def enable_control_plane_log_alert_async(
        self,
        request: servicemesh_20200111_models.EnableControlPlaneLogAlertRequest,
    ) -> servicemesh_20200111_models.EnableControlPlaneLogAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_control_plane_log_alert_with_options_async(request, runtime)

    def get_auto_injection_label_sync_status_with_options(
        self,
        request: servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoInjectionLabelSyncStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_injection_label_sync_status_with_options_async(
        self,
        request: servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoInjectionLabelSyncStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_injection_label_sync_status(
        self,
        request: servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusRequest,
    ) -> servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auto_injection_label_sync_status_with_options(request, runtime)

    async def get_auto_injection_label_sync_status_async(
        self,
        request: servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusRequest,
    ) -> servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_injection_label_sync_status_with_options_async(request, runtime)

    def get_builtin_envoy_filter_with_options(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBuiltinEnvoyFilter',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_builtin_envoy_filter_with_options_async(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBuiltinEnvoyFilter',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_builtin_envoy_filter(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_builtin_envoy_filter_with_options(request, runtime)

    async def get_builtin_envoy_filter_async(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_builtin_envoy_filter_with_options_async(request, runtime)

    def get_builtin_envoy_filter_catalog_with_options(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBuiltinEnvoyFilterCatalog',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_builtin_envoy_filter_catalog_with_options_async(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBuiltinEnvoyFilterCatalog',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_builtin_envoy_filter_catalog(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogRequest,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_builtin_envoy_filter_catalog_with_options(request, runtime)

    async def get_builtin_envoy_filter_catalog_async(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogRequest,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_builtin_envoy_filter_catalog_with_options_async(request, runtime)

    def get_ca_cert_with_options(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCaCert',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetCaCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ca_cert_with_options_async(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCaCert',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetCaCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ca_cert(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ca_cert_with_options(request, runtime)

    async def get_ca_cert_async(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ca_cert_with_options_async(request, runtime)

    def get_diagnosis_with_options(
        self,
        request: servicemesh_20200111_models.GetDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetDiagnosisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnosis',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_diagnosis_with_options_async(
        self,
        request: servicemesh_20200111_models.GetDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetDiagnosisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnosis',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_diagnosis(
        self,
        request: servicemesh_20200111_models.GetDiagnosisRequest,
    ) -> servicemesh_20200111_models.GetDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_diagnosis_with_options(request, runtime)

    async def get_diagnosis_async(
        self,
        request: servicemesh_20200111_models.GetDiagnosisRequest,
    ) -> servicemesh_20200111_models.GetDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_diagnosis_with_options_async(request, runtime)

    def get_ecs_list_with_options(
        self,
        request: servicemesh_20200111_models.GetEcsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetEcsListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEcsList',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetEcsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ecs_list_with_options_async(
        self,
        request: servicemesh_20200111_models.GetEcsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetEcsListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEcsList',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetEcsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ecs_list(
        self,
        request: servicemesh_20200111_models.GetEcsListRequest,
    ) -> servicemesh_20200111_models.GetEcsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ecs_list_with_options(request, runtime)

    async def get_ecs_list_async(
        self,
        request: servicemesh_20200111_models.GetEcsListRequest,
    ) -> servicemesh_20200111_models.GetEcsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ecs_list_with_options_async(request, runtime)

    def get_registered_service_endpoints_with_options(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceEndpoints',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registered_service_endpoints_with_options_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceEndpoints',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registered_service_endpoints(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_registered_service_endpoints_with_options(request, runtime)

    async def get_registered_service_endpoints_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_registered_service_endpoints_with_options_async(request, runtime)

    def get_registered_service_namespaces_with_options(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registered_service_namespaces_with_options_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registered_service_namespaces(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_registered_service_namespaces_with_options(request, runtime)

    async def get_registered_service_namespaces_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_registered_service_namespaces_with_options_async(request, runtime)

    def get_registered_services_with_options(
        self,
        request: servicemesh_20200111_models.GetRegisteredServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegisteredServices',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registered_services_with_options_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegisteredServices',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registered_services(
        self,
        request: servicemesh_20200111_models.GetRegisteredServicesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_registered_services_with_options(request, runtime)

    async def get_registered_services_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServicesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_registered_services_with_options_async(request, runtime)

    def get_sa_token_with_options(
        self,
        request: servicemesh_20200111_models.GetSaTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSaTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.need_refresh):
            body['NeedRefresh'] = request.need_refresh
        if not UtilClient.is_unset(request.service_account_name):
            body['ServiceAccountName'] = request.service_account_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSaToken',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSaTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sa_token_with_options_async(
        self,
        request: servicemesh_20200111_models.GetSaTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSaTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.need_refresh):
            body['NeedRefresh'] = request.need_refresh
        if not UtilClient.is_unset(request.service_account_name):
            body['ServiceAccountName'] = request.service_account_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSaToken',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSaTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sa_token(
        self,
        request: servicemesh_20200111_models.GetSaTokenRequest,
    ) -> servicemesh_20200111_models.GetSaTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sa_token_with_options(request, runtime)

    async def get_sa_token_async(
        self,
        request: servicemesh_20200111_models.GetSaTokenRequest,
    ) -> servicemesh_20200111_models.GetSaTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sa_token_with_options_async(request, runtime)

    def get_service_mesh_slb_with_options(
        self,
        request: servicemesh_20200111_models.GetServiceMeshSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetServiceMeshSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceMeshSlb',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetServiceMeshSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_mesh_slb_with_options_async(
        self,
        request: servicemesh_20200111_models.GetServiceMeshSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetServiceMeshSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceMeshSlb',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetServiceMeshSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_mesh_slb(
        self,
        request: servicemesh_20200111_models.GetServiceMeshSlbRequest,
    ) -> servicemesh_20200111_models.GetServiceMeshSlbResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_mesh_slb_with_options(request, runtime)

    async def get_service_mesh_slb_async(
        self,
        request: servicemesh_20200111_models.GetServiceMeshSlbRequest,
    ) -> servicemesh_20200111_models.GetServiceMeshSlbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_mesh_slb_with_options_async(request, runtime)

    def get_service_registry_source_with_options(
        self,
        request: servicemesh_20200111_models.GetServiceRegistrySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetServiceRegistrySourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceRegistrySource',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetServiceRegistrySourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_registry_source_with_options_async(
        self,
        request: servicemesh_20200111_models.GetServiceRegistrySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetServiceRegistrySourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceRegistrySource',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetServiceRegistrySourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_registry_source(
        self,
        request: servicemesh_20200111_models.GetServiceRegistrySourceRequest,
    ) -> servicemesh_20200111_models.GetServiceRegistrySourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_registry_source_with_options(request, runtime)

    async def get_service_registry_source_async(
        self,
        request: servicemesh_20200111_models.GetServiceRegistrySourceRequest,
    ) -> servicemesh_20200111_models.GetServiceRegistrySourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_registry_source_with_options_async(request, runtime)

    def get_vm_app_mesh_info_with_options(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmAppMeshInfo',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmAppMeshInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vm_app_mesh_info_with_options_async(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmAppMeshInfo',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmAppMeshInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vm_app_mesh_info(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vm_app_mesh_info_with_options(request, runtime)

    async def get_vm_app_mesh_info_async(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vm_app_mesh_info_with_options_async(request, runtime)

    def get_vm_meta_with_options(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmMeta',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vm_meta_with_options_async(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmMeta',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vm_meta(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vm_meta_with_options(request, runtime)

    async def get_vm_meta_async(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vm_meta_with_options_async(request, runtime)

    def initialize_asmrole_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.InitializeASMRoleResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitializeASMRole',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.InitializeASMRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_asmrole_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.InitializeASMRoleResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitializeASMRole',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.InitializeASMRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_asmrole(self) -> servicemesh_20200111_models.InitializeASMRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.initialize_asmrole_with_options(runtime)

    async def initialize_asmrole_async(self) -> servicemesh_20200111_models.InitializeASMRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initialize_asmrole_with_options_async(runtime)

    def list_builtin_envoy_filter_with_options(
        self,
        request: servicemesh_20200111_models.ListBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBuiltinEnvoyFilter',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_builtin_envoy_filter_with_options_async(
        self,
        request: servicemesh_20200111_models.ListBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBuiltinEnvoyFilter',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_builtin_envoy_filter(
        self,
        request: servicemesh_20200111_models.ListBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_builtin_envoy_filter_with_options(request, runtime)

    async def list_builtin_envoy_filter_async(
        self,
        request: servicemesh_20200111_models.ListBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_builtin_envoy_filter_with_options_async(request, runtime)

    def modify_builtin_envoy_filter_with_options(
        self,
        request: servicemesh_20200111_models.ModifyBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyBuiltinEnvoyFilter',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_builtin_envoy_filter_with_options_async(
        self,
        request: servicemesh_20200111_models.ModifyBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyBuiltinEnvoyFilter',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_builtin_envoy_filter(
        self,
        request: servicemesh_20200111_models.ModifyBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_builtin_envoy_filter_with_options(request, runtime)

    async def modify_builtin_envoy_filter_async(
        self,
        request: servicemesh_20200111_models.ModifyBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_builtin_envoy_filter_with_options_async(request, runtime)

    def modify_service_mesh_name_with_options(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyServiceMeshName',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyServiceMeshNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_service_mesh_name_with_options_async(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyServiceMeshName',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyServiceMeshNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_service_mesh_name(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_service_mesh_name_with_options(request, runtime)

    async def modify_service_mesh_name_async(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_service_mesh_name_with_options_async(request, runtime)

    def re_activate_audit_with_options(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReActivateAudit',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ReActivateAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_activate_audit_with_options_async(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReActivateAudit',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ReActivateAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_activate_audit(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        runtime = util_models.RuntimeOptions()
        return self.re_activate_audit_with_options(request, runtime)

    async def re_activate_audit_async(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.re_activate_audit_with_options_async(request, runtime)

    def remove_builtin_envoy_filter_with_options(
        self,
        request: servicemesh_20200111_models.RemoveBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveBuiltinEnvoyFilter',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_builtin_envoy_filter_with_options_async(
        self,
        request: servicemesh_20200111_models.RemoveBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveBuiltinEnvoyFilter',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_builtin_envoy_filter(
        self,
        request: servicemesh_20200111_models.RemoveBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_builtin_envoy_filter_with_options(request, runtime)

    async def remove_builtin_envoy_filter_async(
        self,
        request: servicemesh_20200111_models.RemoveBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_builtin_envoy_filter_with_options_async(request, runtime)

    def remove_cluster_from_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveClusterFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_cluster_from_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveClusterFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_cluster_from_service_mesh(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_cluster_from_service_mesh_with_options(request, runtime)

    async def remove_cluster_from_service_mesh_async(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_cluster_from_service_mesh_with_options_async(request, runtime)

    def remove_vmfrom_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVMFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveVMFromServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_vmfrom_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVMFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveVMFromServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_vmfrom_service_mesh(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_vmfrom_service_mesh_with_options(request, runtime)

    async def remove_vmfrom_service_mesh_async(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_vmfrom_service_mesh_with_options_async(request, runtime)

    def revoke_kubeconfig_with_options(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RevokeKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_kubeconfig_with_options_async(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RevokeKubeconfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_kubeconfig(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_kubeconfig_with_options(request, runtime)

    async def revoke_kubeconfig_async(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_kubeconfig_with_options_async(request, runtime)

    def run_diagnosis_with_options(
        self,
        request: servicemesh_20200111_models.RunDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RunDiagnosisResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDiagnosis',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RunDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_diagnosis_with_options_async(
        self,
        request: servicemesh_20200111_models.RunDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RunDiagnosisResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDiagnosis',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RunDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_diagnosis(
        self,
        request: servicemesh_20200111_models.RunDiagnosisRequest,
    ) -> servicemesh_20200111_models.RunDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_diagnosis_with_options(request, runtime)

    async def run_diagnosis_async(
        self,
        request: servicemesh_20200111_models.RunDiagnosisRequest,
    ) -> servicemesh_20200111_models.RunDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_diagnosis_with_options_async(request, runtime)

    def set_service_registry_source_with_options(
        self,
        tmp_req: servicemesh_20200111_models.SetServiceRegistrySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.SetServiceRegistrySourceResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.SetServiceRegistrySourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        body = {}
        if not UtilClient.is_unset(request.config_shrink):
            body['Config'] = request.config_shrink
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetServiceRegistrySource',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.SetServiceRegistrySourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_service_registry_source_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.SetServiceRegistrySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.SetServiceRegistrySourceResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.SetServiceRegistrySourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        body = {}
        if not UtilClient.is_unset(request.config_shrink):
            body['Config'] = request.config_shrink
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetServiceRegistrySource',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.SetServiceRegistrySourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_service_registry_source(
        self,
        request: servicemesh_20200111_models.SetServiceRegistrySourceRequest,
    ) -> servicemesh_20200111_models.SetServiceRegistrySourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_service_registry_source_with_options(request, runtime)

    async def set_service_registry_source_async(
        self,
        request: servicemesh_20200111_models.SetServiceRegistrySourceRequest,
    ) -> servicemesh_20200111_models.SetServiceRegistrySourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_service_registry_source_with_options_async(request, runtime)

    def update_control_plane_log_alert_action_policy_with_options(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogAlertActionPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogAlertActionPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_policy_id):
            body['ActionPolicyId'] = request.action_policy_id
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateControlPlaneLogAlertActionPolicy',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateControlPlaneLogAlertActionPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_control_plane_log_alert_action_policy_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogAlertActionPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogAlertActionPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_policy_id):
            body['ActionPolicyId'] = request.action_policy_id
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateControlPlaneLogAlertActionPolicy',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateControlPlaneLogAlertActionPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_control_plane_log_alert_action_policy(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogAlertActionPolicyRequest,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogAlertActionPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_control_plane_log_alert_action_policy_with_options(request, runtime)

    async def update_control_plane_log_alert_action_policy_async(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogAlertActionPolicyRequest,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogAlertActionPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_control_plane_log_alert_action_policy_with_options_async(request, runtime)

    def update_control_plane_log_config_with_options(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enabled):
            body['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.project):
            body['Project'] = request.project
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateControlPlaneLogConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_control_plane_log_config_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enabled):
            body['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.project):
            body['Project'] = request.project
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateControlPlaneLogConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_control_plane_log_config(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogConfigRequest,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_control_plane_log_config_with_options(request, runtime)

    async def update_control_plane_log_config_async(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogConfigRequest,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_control_plane_log_config_with_options_async(request, runtime)

    def update_extension_provider_with_options(
        self,
        request: servicemesh_20200111_models.UpdateExtensionProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateExtensionProviderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExtensionProvider',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateExtensionProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_extension_provider_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateExtensionProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateExtensionProviderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExtensionProvider',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateExtensionProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_extension_provider(
        self,
        request: servicemesh_20200111_models.UpdateExtensionProviderRequest,
    ) -> servicemesh_20200111_models.UpdateExtensionProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_extension_provider_with_options(request, runtime)

    async def update_extension_provider_async(
        self,
        request: servicemesh_20200111_models.UpdateExtensionProviderRequest,
    ) -> servicemesh_20200111_models.UpdateExtensionProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_extension_provider_with_options_async(request, runtime)

    def update_istio_injection_config_with_options(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_istio_injection):
            body['EnableIstioInjection'] = request.enable_istio_injection
        if not UtilClient.is_unset(request.enable_sidecar_set_injection):
            body['EnableSidecarSetInjection'] = request.enable_sidecar_set_injection
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioInjectionConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioInjectionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_istio_injection_config_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_istio_injection):
            body['EnableIstioInjection'] = request.enable_istio_injection
        if not UtilClient.is_unset(request.enable_sidecar_set_injection):
            body['EnableSidecarSetInjection'] = request.enable_sidecar_set_injection
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioInjectionConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioInjectionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_istio_injection_config(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_istio_injection_config_with_options(request, runtime)

    async def update_istio_injection_config_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_istio_injection_config_with_options_async(request, runtime)

    def update_mesh_feature_with_options(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.auto_injection_policy_enabled):
            body['AutoInjectionPolicyEnabled'] = request.auto_injection_policy_enabled
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.cni_enabled):
            body['CniEnabled'] = request.cni_enabled
        if not UtilClient.is_unset(request.cni_exclude_namespaces):
            body['CniExcludeNamespaces'] = request.cni_exclude_namespaces
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.discovery_selectors):
            body['DiscoverySelectors'] = request.discovery_selectors
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_namespaces_by_default):
            body['EnableNamespacesByDefault'] = request.enable_namespaces_by_default
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.http_10enabled):
            body['Http10Enabled'] = request.http_10enabled
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.multi_buffer_enabled):
            body['MultiBufferEnabled'] = request.multi_buffer_enabled
        if not UtilClient.is_unset(request.multi_buffer_poll_delay):
            body['MultiBufferPollDelay'] = request.multi_buffer_poll_delay
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.outbound_traffic_policy):
            body['OutboundTrafficPolicy'] = request.outbound_traffic_policy
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_injector_limit_cpu):
            body['SidecarInjectorLimitCPU'] = request.sidecar_injector_limit_cpu
        if not UtilClient.is_unset(request.sidecar_injector_limit_memory):
            body['SidecarInjectorLimitMemory'] = request.sidecar_injector_limit_memory
        if not UtilClient.is_unset(request.sidecar_injector_request_cpu):
            body['SidecarInjectorRequestCPU'] = request.sidecar_injector_request_cpu
        if not UtilClient.is_unset(request.sidecar_injector_request_memory):
            body['SidecarInjectorRequestMemory'] = request.sidecar_injector_request_memory
        if not UtilClient.is_unset(request.sidecar_injector_webhook_as_yaml):
            body['SidecarInjectorWebhookAsYaml'] = request.sidecar_injector_webhook_as_yaml
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshFeature',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mesh_feature_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.auto_injection_policy_enabled):
            body['AutoInjectionPolicyEnabled'] = request.auto_injection_policy_enabled
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.cni_enabled):
            body['CniEnabled'] = request.cni_enabled
        if not UtilClient.is_unset(request.cni_exclude_namespaces):
            body['CniExcludeNamespaces'] = request.cni_exclude_namespaces
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.discovery_selectors):
            body['DiscoverySelectors'] = request.discovery_selectors
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_namespaces_by_default):
            body['EnableNamespacesByDefault'] = request.enable_namespaces_by_default
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.http_10enabled):
            body['Http10Enabled'] = request.http_10enabled
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.multi_buffer_enabled):
            body['MultiBufferEnabled'] = request.multi_buffer_enabled
        if not UtilClient.is_unset(request.multi_buffer_poll_delay):
            body['MultiBufferPollDelay'] = request.multi_buffer_poll_delay
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.outbound_traffic_policy):
            body['OutboundTrafficPolicy'] = request.outbound_traffic_policy
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_injector_limit_cpu):
            body['SidecarInjectorLimitCPU'] = request.sidecar_injector_limit_cpu
        if not UtilClient.is_unset(request.sidecar_injector_limit_memory):
            body['SidecarInjectorLimitMemory'] = request.sidecar_injector_limit_memory
        if not UtilClient.is_unset(request.sidecar_injector_request_cpu):
            body['SidecarInjectorRequestCPU'] = request.sidecar_injector_request_cpu
        if not UtilClient.is_unset(request.sidecar_injector_request_memory):
            body['SidecarInjectorRequestMemory'] = request.sidecar_injector_request_memory
        if not UtilClient.is_unset(request.sidecar_injector_webhook_as_yaml):
            body['SidecarInjectorWebhookAsYaml'] = request.sidecar_injector_webhook_as_yaml
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshFeature',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mesh_feature(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_mesh_feature_with_options(request, runtime)

    async def update_mesh_feature_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_mesh_feature_with_options_async(request, runtime)

    def update_namespace_scope_sidecar_config_with_options(
        self,
        request: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.include_outbound_ports):
            body['IncludeOutboundPorts'] = request.include_outbound_ports
        if not UtilClient.is_unset(request.istio_dnsproxy_enabled):
            body['IstioDNSProxyEnabled'] = request.istio_dnsproxy_enabled
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_limit):
            body['SidecarProxyCPUResourceLimit'] = request.sidecar_proxy_cpuresource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_request):
            body['SidecarProxyCPUResourceRequest'] = request.sidecar_proxy_cpuresource_request
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_limit):
            body['SidecarProxyMemoryResourceLimit'] = request.sidecar_proxy_memory_resource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_request):
            body['SidecarProxyMemoryResourceRequest'] = request.sidecar_proxy_memory_resource_request
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_scope_sidecar_config_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.include_outbound_ports):
            body['IncludeOutboundPorts'] = request.include_outbound_ports
        if not UtilClient.is_unset(request.istio_dnsproxy_enabled):
            body['IstioDNSProxyEnabled'] = request.istio_dnsproxy_enabled
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_limit):
            body['SidecarProxyCPUResourceLimit'] = request.sidecar_proxy_cpuresource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_request):
            body['SidecarProxyCPUResourceRequest'] = request.sidecar_proxy_cpuresource_request
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_limit):
            body['SidecarProxyMemoryResourceLimit'] = request.sidecar_proxy_memory_resource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_request):
            body['SidecarProxyMemoryResourceRequest'] = request.sidecar_proxy_memory_resource_request
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace_scope_sidecar_config(
        self,
        request: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_namespace_scope_sidecar_config_with_options(request, runtime)

    async def update_namespace_scope_sidecar_config_async(
        self,
        request: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_namespace_scope_sidecar_config_with_options_async(request, runtime)

    def upgrade_mesh_version_with_options(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMeshVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_mesh_version_with_options_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMeshVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_mesh_version(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_mesh_version_with_options(request, runtime)

    async def upgrade_mesh_version_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_mesh_version_with_options_async(request, runtime)
