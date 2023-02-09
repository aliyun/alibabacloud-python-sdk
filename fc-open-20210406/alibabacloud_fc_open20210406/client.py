# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from requests import Response, Request
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_fc_open20210406 import models as fc__open_20210406_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_gateway_fc_util.client import Client as FCUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'account-id.ap-northeast-1.fc.aliyuncs.com',
            'ap-south-1': 'account-id.ap-south-1.fc.aliyuncs.com',
            'ap-southeast-1': 'account-id.ap-southeast-1.fc.aliyuncs.com',
            'ap-southeast-2': 'account-id.ap-southeast-2.fc.aliyuncs.com',
            'ap-southeast-3': 'account-id.ap-southeast-3.fc.aliyuncs.com',
            'ap-southeast-5': 'account-id.ap-southeast-5.fc.aliyuncs.com',
            'cn-beijing': 'account-id.cn-beijing.fc.aliyuncs.com',
            'cn-chengdu': 'account-id.cn-chengdu.fc.aliyuncs.com',
            'cn-hangzhou': 'account-id.cn-hangzhou.fc.aliyuncs.com',
            'cn-hangzhou-finance': 'account-id.cn-hangzhou-finance.fc.aliyuncs.com',
            'cn-hongkong': 'account-id.cn-hongkong.fc.aliyuncs.com',
            'cn-huhehaote': 'account-id.cn-huhehaote.fc.aliyuncs.com',
            'cn-north-2-gov-1': 'account-id.cn-north-2-gov-1.fc.aliyuncs.com',
            'cn-qingdao': 'account-id.cn-qingdao.fc.aliyuncs.com',
            'cn-shanghai': 'account-id.cn-shanghai.fc.aliyuncs.com',
            'cn-shenzhen': 'account-id.cn-shenzhen.fc.aliyuncs.com',
            'cn-zhangjiakou': 'account-id.cn-zhangjiakou.fc.aliyuncs.com',
            'eu-central-1': 'account-id.eu-central-1.fc.aliyuncs.com',
            'eu-west-1': 'account-id.eu-west-1.fc.aliyuncs.com',
            'us-east-1': 'account-id.us-east-1.fc.aliyuncs.com',
            'us-west-1': 'account-id.us-west-1.fc.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('fc-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def claim_gpuinstance_with_options(
        self,
        request: fc__open_20210406_models.ClaimGPUInstanceRequest,
        headers: fc__open_20210406_models.ClaimGPUInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ClaimGPUInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.disk_performance_level):
            body['diskPerformanceLevel'] = request.disk_performance_level
        if not UtilClient.is_unset(request.disk_size_gigabytes):
            body['diskSizeGigabytes'] = request.disk_size_gigabytes
        if not UtilClient.is_unset(request.image_id):
            body['imageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_bandwidth_out):
            body['internetBandwidthOut'] = request.internet_bandwidth_out
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.sg_id):
            body['sgId'] = request.sg_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            body['sourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.tcp_port_range):
            body['tcpPortRange'] = request.tcp_port_range
        if not UtilClient.is_unset(request.udp_port_range):
            body['udpPortRange'] = request.udp_port_range
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vsw_id):
            body['vswId'] = request.vsw_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ClaimGPUInstance',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/gpuInstances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ClaimGPUInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def claim_gpuinstance_with_options_async(
        self,
        request: fc__open_20210406_models.ClaimGPUInstanceRequest,
        headers: fc__open_20210406_models.ClaimGPUInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ClaimGPUInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.disk_performance_level):
            body['diskPerformanceLevel'] = request.disk_performance_level
        if not UtilClient.is_unset(request.disk_size_gigabytes):
            body['diskSizeGigabytes'] = request.disk_size_gigabytes
        if not UtilClient.is_unset(request.image_id):
            body['imageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_bandwidth_out):
            body['internetBandwidthOut'] = request.internet_bandwidth_out
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.sg_id):
            body['sgId'] = request.sg_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            body['sourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.tcp_port_range):
            body['tcpPortRange'] = request.tcp_port_range
        if not UtilClient.is_unset(request.udp_port_range):
            body['udpPortRange'] = request.udp_port_range
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vsw_id):
            body['vswId'] = request.vsw_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ClaimGPUInstance',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/gpuInstances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ClaimGPUInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def claim_gpuinstance(
        self,
        request: fc__open_20210406_models.ClaimGPUInstanceRequest,
    ) -> fc__open_20210406_models.ClaimGPUInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ClaimGPUInstanceHeaders()
        return self.claim_gpuinstance_with_options(request, headers, runtime)

    async def claim_gpuinstance_async(
        self,
        request: fc__open_20210406_models.ClaimGPUInstanceRequest,
    ) -> fc__open_20210406_models.ClaimGPUInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ClaimGPUInstanceHeaders()
        return await self.claim_gpuinstance_with_options_async(request, headers, runtime)

    def create_alias_with_options(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateAliasRequest,
        headers: fc__open_20210406_models.CreateAliasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateAliasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_version_weight):
            body['additionalVersionWeight'] = request.additional_version_weight
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.resolve_policy):
            body['resolvePolicy'] = request.resolve_policy
        if not UtilClient.is_unset(request.route_policy):
            body['routePolicy'] = request.route_policy
        if not UtilClient.is_unset(request.version_id):
            body['versionId'] = request.version_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlias',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/aliases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alias_with_options_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateAliasRequest,
        headers: fc__open_20210406_models.CreateAliasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateAliasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_version_weight):
            body['additionalVersionWeight'] = request.additional_version_weight
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.resolve_policy):
            body['resolvePolicy'] = request.resolve_policy
        if not UtilClient.is_unset(request.route_policy):
            body['routePolicy'] = request.route_policy
        if not UtilClient.is_unset(request.version_id):
            body['versionId'] = request.version_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlias',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/aliases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alias(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateAliasRequest,
    ) -> fc__open_20210406_models.CreateAliasResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateAliasHeaders()
        return self.create_alias_with_options(service_name, request, headers, runtime)

    async def create_alias_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateAliasRequest,
    ) -> fc__open_20210406_models.CreateAliasResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateAliasHeaders()
        return await self.create_alias_with_options_async(service_name, request, headers, runtime)

    def create_custom_domain_with_options(
        self,
        request: fc__open_20210406_models.CreateCustomDomainRequest,
        headers: fc__open_20210406_models.CreateCustomDomainHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateCustomDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_config):
            body['certConfig'] = request.cert_config
        if not UtilClient.is_unset(request.domain_name):
            body['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.route_config):
            body['routeConfig'] = request.route_config
        if not UtilClient.is_unset(request.tls_config):
            body['tlsConfig'] = request.tls_config
        if not UtilClient.is_unset(request.waf_config):
            body['wafConfig'] = request.waf_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCustomDomain',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/custom-domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_domain_with_options_async(
        self,
        request: fc__open_20210406_models.CreateCustomDomainRequest,
        headers: fc__open_20210406_models.CreateCustomDomainHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateCustomDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_config):
            body['certConfig'] = request.cert_config
        if not UtilClient.is_unset(request.domain_name):
            body['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.route_config):
            body['routeConfig'] = request.route_config
        if not UtilClient.is_unset(request.tls_config):
            body['tlsConfig'] = request.tls_config
        if not UtilClient.is_unset(request.waf_config):
            body['wafConfig'] = request.waf_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCustomDomain',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/custom-domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_domain(
        self,
        request: fc__open_20210406_models.CreateCustomDomainRequest,
    ) -> fc__open_20210406_models.CreateCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateCustomDomainHeaders()
        return self.create_custom_domain_with_options(request, headers, runtime)

    async def create_custom_domain_async(
        self,
        request: fc__open_20210406_models.CreateCustomDomainRequest,
    ) -> fc__open_20210406_models.CreateCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateCustomDomainHeaders()
        return await self.create_custom_domain_with_options_async(request, headers, runtime)

    def create_function_with_options(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateFunctionRequest,
        headers: fc__open_20210406_models.CreateFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_port):
            body['caPort'] = request.ca_port
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_container_config):
            body['customContainerConfig'] = request.custom_container_config
        if not UtilClient.is_unset(request.custom_dns):
            body['customDNS'] = request.custom_dns
        if not UtilClient.is_unset(request.custom_health_check_config):
            body['customHealthCheckConfig'] = request.custom_health_check_config
        if not UtilClient.is_unset(request.custom_runtime_config):
            body['customRuntimeConfig'] = request.custom_runtime_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disk_size):
            body['diskSize'] = request.disk_size
        if not UtilClient.is_unset(request.environment_variables):
            body['environmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.function_name):
            body['functionName'] = request.function_name
        if not UtilClient.is_unset(request.gpu_memory_size):
            body['gpuMemorySize'] = request.gpu_memory_size
        if not UtilClient.is_unset(request.handler):
            body['handler'] = request.handler
        if not UtilClient.is_unset(request.initialization_timeout):
            body['initializationTimeout'] = request.initialization_timeout
        if not UtilClient.is_unset(request.initializer):
            body['initializer'] = request.initializer
        if not UtilClient.is_unset(request.instance_concurrency):
            body['instanceConcurrency'] = request.instance_concurrency
        if not UtilClient.is_unset(request.instance_lifecycle_config):
            body['instanceLifecycleConfig'] = request.instance_lifecycle_config
        if not UtilClient.is_unset(request.instance_soft_concurrency):
            body['instanceSoftConcurrency'] = request.instance_soft_concurrency
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.layers):
            body['layers'] = request.layers
        if not UtilClient.is_unset(request.memory_size):
            body['memorySize'] = request.memory_size
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['X-Fc-Code-Checksum'] = UtilClient.to_jsonstring(headers.x_fc_code_checksum)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_with_options_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateFunctionRequest,
        headers: fc__open_20210406_models.CreateFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_port):
            body['caPort'] = request.ca_port
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_container_config):
            body['customContainerConfig'] = request.custom_container_config
        if not UtilClient.is_unset(request.custom_dns):
            body['customDNS'] = request.custom_dns
        if not UtilClient.is_unset(request.custom_health_check_config):
            body['customHealthCheckConfig'] = request.custom_health_check_config
        if not UtilClient.is_unset(request.custom_runtime_config):
            body['customRuntimeConfig'] = request.custom_runtime_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disk_size):
            body['diskSize'] = request.disk_size
        if not UtilClient.is_unset(request.environment_variables):
            body['environmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.function_name):
            body['functionName'] = request.function_name
        if not UtilClient.is_unset(request.gpu_memory_size):
            body['gpuMemorySize'] = request.gpu_memory_size
        if not UtilClient.is_unset(request.handler):
            body['handler'] = request.handler
        if not UtilClient.is_unset(request.initialization_timeout):
            body['initializationTimeout'] = request.initialization_timeout
        if not UtilClient.is_unset(request.initializer):
            body['initializer'] = request.initializer
        if not UtilClient.is_unset(request.instance_concurrency):
            body['instanceConcurrency'] = request.instance_concurrency
        if not UtilClient.is_unset(request.instance_lifecycle_config):
            body['instanceLifecycleConfig'] = request.instance_lifecycle_config
        if not UtilClient.is_unset(request.instance_soft_concurrency):
            body['instanceSoftConcurrency'] = request.instance_soft_concurrency
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.layers):
            body['layers'] = request.layers
        if not UtilClient.is_unset(request.memory_size):
            body['memorySize'] = request.memory_size
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['X-Fc-Code-Checksum'] = UtilClient.to_jsonstring(headers.x_fc_code_checksum)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateFunctionRequest,
    ) -> fc__open_20210406_models.CreateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateFunctionHeaders()
        return self.create_function_with_options(service_name, request, headers, runtime)

    async def create_function_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateFunctionRequest,
    ) -> fc__open_20210406_models.CreateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateFunctionHeaders()
        return await self.create_function_with_options_async(service_name, request, headers, runtime)

    def create_layer_version_with_options(
        self,
        layer_name: str,
        request: fc__open_20210406_models.CreateLayerVersionRequest,
        headers: fc__open_20210406_models.CreateLayerVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateLayerVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.compatible_runtime):
            body['compatibleRuntime'] = request.compatible_runtime
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLayerVersion',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_layer_version_with_options_async(
        self,
        layer_name: str,
        request: fc__open_20210406_models.CreateLayerVersionRequest,
        headers: fc__open_20210406_models.CreateLayerVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateLayerVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.compatible_runtime):
            body['compatibleRuntime'] = request.compatible_runtime
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLayerVersion',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateLayerVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_layer_version(
        self,
        layer_name: str,
        request: fc__open_20210406_models.CreateLayerVersionRequest,
    ) -> fc__open_20210406_models.CreateLayerVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateLayerVersionHeaders()
        return self.create_layer_version_with_options(layer_name, request, headers, runtime)

    async def create_layer_version_async(
        self,
        layer_name: str,
        request: fc__open_20210406_models.CreateLayerVersionRequest,
    ) -> fc__open_20210406_models.CreateLayerVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateLayerVersionHeaders()
        return await self.create_layer_version_with_options_async(layer_name, request, headers, runtime)

    def create_service_with_options(
        self,
        request: fc__open_20210406_models.CreateServiceRequest,
        headers: fc__open_20210406_models.CreateServiceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.internet_access):
            body['internetAccess'] = request.internet_access
        if not UtilClient.is_unset(request.log_config):
            body['logConfig'] = request.log_config
        if not UtilClient.is_unset(request.nas_config):
            body['nasConfig'] = request.nas_config
        if not UtilClient.is_unset(request.oss_mount_config):
            body['ossMountConfig'] = request.oss_mount_config
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.tracing_config):
            body['tracingConfig'] = request.tracing_config
        if not UtilClient.is_unset(request.vpc_config):
            body['vpcConfig'] = request.vpc_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: fc__open_20210406_models.CreateServiceRequest,
        headers: fc__open_20210406_models.CreateServiceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.internet_access):
            body['internetAccess'] = request.internet_access
        if not UtilClient.is_unset(request.log_config):
            body['logConfig'] = request.log_config
        if not UtilClient.is_unset(request.nas_config):
            body['nasConfig'] = request.nas_config
        if not UtilClient.is_unset(request.oss_mount_config):
            body['ossMountConfig'] = request.oss_mount_config
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.tracing_config):
            body['tracingConfig'] = request.tracing_config
        if not UtilClient.is_unset(request.vpc_config):
            body['vpcConfig'] = request.vpc_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: fc__open_20210406_models.CreateServiceRequest,
    ) -> fc__open_20210406_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateServiceHeaders()
        return self.create_service_with_options(request, headers, runtime)

    async def create_service_async(
        self,
        request: fc__open_20210406_models.CreateServiceRequest,
    ) -> fc__open_20210406_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateServiceHeaders()
        return await self.create_service_with_options_async(request, headers, runtime)

    def create_trigger_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.CreateTriggerRequest,
        headers: fc__open_20210406_models.CreateTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.invocation_role):
            body['invocationRole'] = request.invocation_role
        if not UtilClient.is_unset(request.qualifier):
            body['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.source_arn):
            body['sourceArn'] = request.source_arn
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.trigger_name):
            body['triggerName'] = request.trigger_name
        if not UtilClient.is_unset(request.trigger_type):
            body['triggerType'] = request.trigger_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trigger_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.CreateTriggerRequest,
        headers: fc__open_20210406_models.CreateTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.invocation_role):
            body['invocationRole'] = request.invocation_role
        if not UtilClient.is_unset(request.qualifier):
            body['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.source_arn):
            body['sourceArn'] = request.source_arn
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.trigger_name):
            body['triggerName'] = request.trigger_name
        if not UtilClient.is_unset(request.trigger_type):
            body['triggerType'] = request.trigger_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trigger(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.CreateTriggerRequest,
    ) -> fc__open_20210406_models.CreateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateTriggerHeaders()
        return self.create_trigger_with_options(service_name, function_name, request, headers, runtime)

    async def create_trigger_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.CreateTriggerRequest,
    ) -> fc__open_20210406_models.CreateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateTriggerHeaders()
        return await self.create_trigger_with_options_async(service_name, function_name, request, headers, runtime)

    def create_vpc_binding_with_options(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateVpcBindingRequest,
        headers: fc__open_20210406_models.CreateVpcBindingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateVpcBindingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpcBinding',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/bindings',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateVpcBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_binding_with_options_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateVpcBindingRequest,
        headers: fc__open_20210406_models.CreateVpcBindingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.CreateVpcBindingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpcBinding',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/bindings',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateVpcBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_binding(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateVpcBindingRequest,
    ) -> fc__open_20210406_models.CreateVpcBindingResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateVpcBindingHeaders()
        return self.create_vpc_binding_with_options(service_name, request, headers, runtime)

    async def create_vpc_binding_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.CreateVpcBindingRequest,
    ) -> fc__open_20210406_models.CreateVpcBindingResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateVpcBindingHeaders()
        return await self.create_vpc_binding_with_options_async(service_name, request, headers, runtime)

    def delete_alias_with_options(
        self,
        service_name: str,
        alias_name: str,
        headers: fc__open_20210406_models.DeleteAliasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteAliasResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteAlias',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alias_with_options_async(
        self,
        service_name: str,
        alias_name: str,
        headers: fc__open_20210406_models.DeleteAliasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteAliasResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteAlias',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alias(
        self,
        service_name: str,
        alias_name: str,
    ) -> fc__open_20210406_models.DeleteAliasResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteAliasHeaders()
        return self.delete_alias_with_options(service_name, alias_name, headers, runtime)

    async def delete_alias_async(
        self,
        service_name: str,
        alias_name: str,
    ) -> fc__open_20210406_models.DeleteAliasResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteAliasHeaders()
        return await self.delete_alias_with_options_async(service_name, alias_name, headers, runtime)

    def delete_custom_domain_with_options(
        self,
        domain_name: str,
        headers: fc__open_20210406_models.DeleteCustomDomainHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteCustomDomainResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteCustomDomain',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_domain_with_options_async(
        self,
        domain_name: str,
        headers: fc__open_20210406_models.DeleteCustomDomainHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteCustomDomainResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteCustomDomain',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_domain(
        self,
        domain_name: str,
    ) -> fc__open_20210406_models.DeleteCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteCustomDomainHeaders()
        return self.delete_custom_domain_with_options(domain_name, headers, runtime)

    async def delete_custom_domain_async(
        self,
        domain_name: str,
    ) -> fc__open_20210406_models.DeleteCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteCustomDomainHeaders()
        return await self.delete_custom_domain_with_options_async(domain_name, headers, runtime)

    def delete_function_with_options(
        self,
        service_name: str,
        function_name: str,
        headers: fc__open_20210406_models.DeleteFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteFunctionResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_with_options_async(
        self,
        service_name: str,
        function_name: str,
        headers: fc__open_20210406_models.DeleteFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteFunctionResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function(
        self,
        service_name: str,
        function_name: str,
    ) -> fc__open_20210406_models.DeleteFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteFunctionHeaders()
        return self.delete_function_with_options(service_name, function_name, headers, runtime)

    async def delete_function_async(
        self,
        service_name: str,
        function_name: str,
    ) -> fc__open_20210406_models.DeleteFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteFunctionHeaders()
        return await self.delete_function_with_options_async(service_name, function_name, headers, runtime)

    def delete_function_async_invoke_config_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigRequest,
        headers: fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFunctionAsyncInvokeConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_async_invoke_config_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigRequest,
        headers: fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFunctionAsyncInvokeConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function_async_invoke_config(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigRequest,
    ) -> fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigHeaders()
        return self.delete_function_async_invoke_config_with_options(service_name, function_name, request, headers, runtime)

    async def delete_function_async_invoke_config_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigRequest,
    ) -> fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigHeaders()
        return await self.delete_function_async_invoke_config_with_options_async(service_name, function_name, request, headers, runtime)

    def delete_function_on_demand_config_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.DeleteFunctionOnDemandConfigRequest,
        headers: fc__open_20210406_models.DeleteFunctionOnDemandConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteFunctionOnDemandConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFunctionOnDemandConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/on-demand-config',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteFunctionOnDemandConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_on_demand_config_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.DeleteFunctionOnDemandConfigRequest,
        headers: fc__open_20210406_models.DeleteFunctionOnDemandConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteFunctionOnDemandConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFunctionOnDemandConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/on-demand-config',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteFunctionOnDemandConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function_on_demand_config(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.DeleteFunctionOnDemandConfigRequest,
    ) -> fc__open_20210406_models.DeleteFunctionOnDemandConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteFunctionOnDemandConfigHeaders()
        return self.delete_function_on_demand_config_with_options(service_name, function_name, request, headers, runtime)

    async def delete_function_on_demand_config_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.DeleteFunctionOnDemandConfigRequest,
    ) -> fc__open_20210406_models.DeleteFunctionOnDemandConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteFunctionOnDemandConfigHeaders()
        return await self.delete_function_on_demand_config_with_options_async(service_name, function_name, request, headers, runtime)

    def delete_layer_version_with_options(
        self,
        layer_name: str,
        version: str,
        headers: fc__open_20210406_models.DeleteLayerVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteLayerVersionResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteLayerVersion',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions/{OpenApiUtilClient.get_encode_param(version)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_layer_version_with_options_async(
        self,
        layer_name: str,
        version: str,
        headers: fc__open_20210406_models.DeleteLayerVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteLayerVersionResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteLayerVersion',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions/{OpenApiUtilClient.get_encode_param(version)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteLayerVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_layer_version(
        self,
        layer_name: str,
        version: str,
    ) -> fc__open_20210406_models.DeleteLayerVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteLayerVersionHeaders()
        return self.delete_layer_version_with_options(layer_name, version, headers, runtime)

    async def delete_layer_version_async(
        self,
        layer_name: str,
        version: str,
    ) -> fc__open_20210406_models.DeleteLayerVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteLayerVersionHeaders()
        return await self.delete_layer_version_with_options_async(layer_name, version, headers, runtime)

    def delete_service_with_options(
        self,
        service_name: str,
        headers: fc__open_20210406_models.DeleteServiceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteServiceResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        service_name: str,
        headers: fc__open_20210406_models.DeleteServiceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteServiceResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        service_name: str,
    ) -> fc__open_20210406_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteServiceHeaders()
        return self.delete_service_with_options(service_name, headers, runtime)

    async def delete_service_async(
        self,
        service_name: str,
    ) -> fc__open_20210406_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteServiceHeaders()
        return await self.delete_service_with_options_async(service_name, headers, runtime)

    def delete_service_version_with_options(
        self,
        service_name: str,
        version_id: str,
        headers: fc__open_20210406_models.DeleteServiceVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteServiceVersionResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteServiceVersion',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/versions/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_version_with_options_async(
        self,
        service_name: str,
        version_id: str,
        headers: fc__open_20210406_models.DeleteServiceVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteServiceVersionResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteServiceVersion',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/versions/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_version(
        self,
        service_name: str,
        version_id: str,
    ) -> fc__open_20210406_models.DeleteServiceVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteServiceVersionHeaders()
        return self.delete_service_version_with_options(service_name, version_id, headers, runtime)

    async def delete_service_version_async(
        self,
        service_name: str,
        version_id: str,
    ) -> fc__open_20210406_models.DeleteServiceVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteServiceVersionHeaders()
        return await self.delete_service_version_with_options_async(service_name, version_id, headers, runtime)

    def delete_trigger_with_options(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
        headers: fc__open_20210406_models.DeleteTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteTriggerResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trigger_with_options_async(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
        headers: fc__open_20210406_models.DeleteTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteTriggerResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trigger(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
    ) -> fc__open_20210406_models.DeleteTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteTriggerHeaders()
        return self.delete_trigger_with_options(service_name, function_name, trigger_name, headers, runtime)

    async def delete_trigger_async(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
    ) -> fc__open_20210406_models.DeleteTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteTriggerHeaders()
        return await self.delete_trigger_with_options_async(service_name, function_name, trigger_name, headers, runtime)

    def delete_vpc_binding_with_options(
        self,
        service_name: str,
        vpc_id: str,
        headers: fc__open_20210406_models.DeleteVpcBindingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteVpcBindingResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteVpcBinding',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/bindings/{OpenApiUtilClient.get_encode_param(vpc_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteVpcBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_binding_with_options_async(
        self,
        service_name: str,
        vpc_id: str,
        headers: fc__open_20210406_models.DeleteVpcBindingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeleteVpcBindingResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteVpcBinding',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/bindings/{OpenApiUtilClient.get_encode_param(vpc_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteVpcBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_binding(
        self,
        service_name: str,
        vpc_id: str,
    ) -> fc__open_20210406_models.DeleteVpcBindingResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteVpcBindingHeaders()
        return self.delete_vpc_binding_with_options(service_name, vpc_id, headers, runtime)

    async def delete_vpc_binding_async(
        self,
        service_name: str,
        vpc_id: str,
    ) -> fc__open_20210406_models.DeleteVpcBindingResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteVpcBindingHeaders()
        return await self.delete_vpc_binding_with_options_async(service_name, vpc_id, headers, runtime)

    def deregister_event_source_with_options(
        self,
        service_name: str,
        function_name: str,
        source_arn: str,
        request: fc__open_20210406_models.DeregisterEventSourceRequest,
        headers: fc__open_20210406_models.DeregisterEventSourceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeregisterEventSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterEventSource',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/event-sources/{OpenApiUtilClient.get_encode_param(source_arn)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeregisterEventSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_event_source_with_options_async(
        self,
        service_name: str,
        function_name: str,
        source_arn: str,
        request: fc__open_20210406_models.DeregisterEventSourceRequest,
        headers: fc__open_20210406_models.DeregisterEventSourceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.DeregisterEventSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterEventSource',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/event-sources/{OpenApiUtilClient.get_encode_param(source_arn)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeregisterEventSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_event_source(
        self,
        service_name: str,
        function_name: str,
        source_arn: str,
        request: fc__open_20210406_models.DeregisterEventSourceRequest,
    ) -> fc__open_20210406_models.DeregisterEventSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeregisterEventSourceHeaders()
        return self.deregister_event_source_with_options(service_name, function_name, source_arn, request, headers, runtime)

    async def deregister_event_source_async(
        self,
        service_name: str,
        function_name: str,
        source_arn: str,
        request: fc__open_20210406_models.DeregisterEventSourceRequest,
    ) -> fc__open_20210406_models.DeregisterEventSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeregisterEventSourceHeaders()
        return await self.deregister_event_source_with_options_async(service_name, function_name, source_arn, request, headers, runtime)

    def get_account_settings_with_options(
        self,
        headers: fc__open_20210406_models.GetAccountSettingsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetAccountSettingsResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetAccountSettings',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/account-settings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetAccountSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_settings_with_options_async(
        self,
        headers: fc__open_20210406_models.GetAccountSettingsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetAccountSettingsResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetAccountSettings',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/account-settings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetAccountSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_settings(self) -> fc__open_20210406_models.GetAccountSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetAccountSettingsHeaders()
        return self.get_account_settings_with_options(headers, runtime)

    async def get_account_settings_async(self) -> fc__open_20210406_models.GetAccountSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetAccountSettingsHeaders()
        return await self.get_account_settings_with_options_async(headers, runtime)

    def get_alias_with_options(
        self,
        service_name: str,
        alias_name: str,
        headers: fc__open_20210406_models.GetAliasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetAliasResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetAlias',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alias_with_options_async(
        self,
        service_name: str,
        alias_name: str,
        headers: fc__open_20210406_models.GetAliasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetAliasResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetAlias',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alias(
        self,
        service_name: str,
        alias_name: str,
    ) -> fc__open_20210406_models.GetAliasResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetAliasHeaders()
        return self.get_alias_with_options(service_name, alias_name, headers, runtime)

    async def get_alias_async(
        self,
        service_name: str,
        alias_name: str,
    ) -> fc__open_20210406_models.GetAliasResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetAliasHeaders()
        return await self.get_alias_with_options_async(service_name, alias_name, headers, runtime)

    def get_custom_domain_with_options(
        self,
        domain_name: str,
        headers: fc__open_20210406_models.GetCustomDomainHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetCustomDomainResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetCustomDomain',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_domain_with_options_async(
        self,
        domain_name: str,
        headers: fc__open_20210406_models.GetCustomDomainHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetCustomDomainResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetCustomDomain',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_domain(
        self,
        domain_name: str,
    ) -> fc__open_20210406_models.GetCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetCustomDomainHeaders()
        return self.get_custom_domain_with_options(domain_name, headers, runtime)

    async def get_custom_domain_async(
        self,
        domain_name: str,
    ) -> fc__open_20210406_models.GetCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetCustomDomainHeaders()
        return await self.get_custom_domain_with_options_async(domain_name, headers, runtime)

    def get_function_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionRequest,
        headers: fc__open_20210406_models.GetFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetFunctionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionRequest,
        headers: fc__open_20210406_models.GetFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetFunctionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionRequest,
    ) -> fc__open_20210406_models.GetFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetFunctionHeaders()
        return self.get_function_with_options(service_name, function_name, request, headers, runtime)

    async def get_function_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionRequest,
    ) -> fc__open_20210406_models.GetFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetFunctionHeaders()
        return await self.get_function_with_options_async(service_name, function_name, request, headers, runtime)

    def get_function_async_invoke_config_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionAsyncInvokeConfigRequest,
        headers: fc__open_20210406_models.GetFunctionAsyncInvokeConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetFunctionAsyncInvokeConfigResponse:
        """
        StatefulAsyncInvocation indicates whether the asynchronous task feature is enabled. If the value of StatefulAsyncInvocation is true, the asynchronous task feature is enabled. All asynchronous invocations change to asynchronous task mode.
        
        @param request: GetFunctionAsyncInvokeConfigRequest
        @param headers: GetFunctionAsyncInvokeConfigHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionAsyncInvokeConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_async_invoke_config_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionAsyncInvokeConfigRequest,
        headers: fc__open_20210406_models.GetFunctionAsyncInvokeConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetFunctionAsyncInvokeConfigResponse:
        """
        StatefulAsyncInvocation indicates whether the asynchronous task feature is enabled. If the value of StatefulAsyncInvocation is true, the asynchronous task feature is enabled. All asynchronous invocations change to asynchronous task mode.
        
        @param request: GetFunctionAsyncInvokeConfigRequest
        @param headers: GetFunctionAsyncInvokeConfigHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionAsyncInvokeConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionAsyncInvokeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_async_invoke_config(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionAsyncInvokeConfigRequest,
    ) -> fc__open_20210406_models.GetFunctionAsyncInvokeConfigResponse:
        """
        StatefulAsyncInvocation indicates whether the asynchronous task feature is enabled. If the value of StatefulAsyncInvocation is true, the asynchronous task feature is enabled. All asynchronous invocations change to asynchronous task mode.
        
        @param request: GetFunctionAsyncInvokeConfigRequest
        @return: GetFunctionAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetFunctionAsyncInvokeConfigHeaders()
        return self.get_function_async_invoke_config_with_options(service_name, function_name, request, headers, runtime)

    async def get_function_async_invoke_config_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionAsyncInvokeConfigRequest,
    ) -> fc__open_20210406_models.GetFunctionAsyncInvokeConfigResponse:
        """
        StatefulAsyncInvocation indicates whether the asynchronous task feature is enabled. If the value of StatefulAsyncInvocation is true, the asynchronous task feature is enabled. All asynchronous invocations change to asynchronous task mode.
        
        @param request: GetFunctionAsyncInvokeConfigRequest
        @return: GetFunctionAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetFunctionAsyncInvokeConfigHeaders()
        return await self.get_function_async_invoke_config_with_options_async(service_name, function_name, request, headers, runtime)

    def get_function_code_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionCodeRequest,
        headers: fc__open_20210406_models.GetFunctionCodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetFunctionCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionCode',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/code',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_code_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionCodeRequest,
        headers: fc__open_20210406_models.GetFunctionCodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetFunctionCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionCode',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/code',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_code(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionCodeRequest,
    ) -> fc__open_20210406_models.GetFunctionCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetFunctionCodeHeaders()
        return self.get_function_code_with_options(service_name, function_name, request, headers, runtime)

    async def get_function_code_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionCodeRequest,
    ) -> fc__open_20210406_models.GetFunctionCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetFunctionCodeHeaders()
        return await self.get_function_code_with_options_async(service_name, function_name, request, headers, runtime)

    def get_function_on_demand_config_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionOnDemandConfigRequest,
        headers: fc__open_20210406_models.GetFunctionOnDemandConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetFunctionOnDemandConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionOnDemandConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/on-demand-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionOnDemandConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_on_demand_config_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionOnDemandConfigRequest,
        headers: fc__open_20210406_models.GetFunctionOnDemandConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetFunctionOnDemandConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionOnDemandConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/on-demand-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionOnDemandConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_on_demand_config(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionOnDemandConfigRequest,
    ) -> fc__open_20210406_models.GetFunctionOnDemandConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetFunctionOnDemandConfigHeaders()
        return self.get_function_on_demand_config_with_options(service_name, function_name, request, headers, runtime)

    async def get_function_on_demand_config_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetFunctionOnDemandConfigRequest,
    ) -> fc__open_20210406_models.GetFunctionOnDemandConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetFunctionOnDemandConfigHeaders()
        return await self.get_function_on_demand_config_with_options_async(service_name, function_name, request, headers, runtime)

    def get_layer_version_with_options(
        self,
        layer_name: str,
        version: str,
        headers: fc__open_20210406_models.GetLayerVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetLayerVersionResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetLayerVersion',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions/{OpenApiUtilClient.get_encode_param(version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_layer_version_with_options_async(
        self,
        layer_name: str,
        version: str,
        headers: fc__open_20210406_models.GetLayerVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetLayerVersionResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetLayerVersion',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions/{OpenApiUtilClient.get_encode_param(version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetLayerVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_layer_version(
        self,
        layer_name: str,
        version: str,
    ) -> fc__open_20210406_models.GetLayerVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetLayerVersionHeaders()
        return self.get_layer_version_with_options(layer_name, version, headers, runtime)

    async def get_layer_version_async(
        self,
        layer_name: str,
        version: str,
    ) -> fc__open_20210406_models.GetLayerVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetLayerVersionHeaders()
        return await self.get_layer_version_with_options_async(layer_name, version, headers, runtime)

    def get_provision_config_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetProvisionConfigRequest,
        headers: fc__open_20210406_models.GetProvisionConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetProvisionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProvisionConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/provision-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetProvisionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_provision_config_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetProvisionConfigRequest,
        headers: fc__open_20210406_models.GetProvisionConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetProvisionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProvisionConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/provision-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetProvisionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_provision_config(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetProvisionConfigRequest,
    ) -> fc__open_20210406_models.GetProvisionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetProvisionConfigHeaders()
        return self.get_provision_config_with_options(service_name, function_name, request, headers, runtime)

    async def get_provision_config_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.GetProvisionConfigRequest,
    ) -> fc__open_20210406_models.GetProvisionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetProvisionConfigHeaders()
        return await self.get_provision_config_with_options_async(service_name, function_name, request, headers, runtime)

    def get_resource_tags_with_options(
        self,
        request: fc__open_20210406_models.GetResourceTagsRequest,
        headers: fc__open_20210406_models.GetResourceTagsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetResourceTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_arn):
            query['resourceArn'] = request.resource_arn
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceTags',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/tag',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetResourceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_tags_with_options_async(
        self,
        request: fc__open_20210406_models.GetResourceTagsRequest,
        headers: fc__open_20210406_models.GetResourceTagsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetResourceTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_arn):
            query['resourceArn'] = request.resource_arn
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceTags',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/tag',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetResourceTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_tags(
        self,
        request: fc__open_20210406_models.GetResourceTagsRequest,
    ) -> fc__open_20210406_models.GetResourceTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetResourceTagsHeaders()
        return self.get_resource_tags_with_options(request, headers, runtime)

    async def get_resource_tags_async(
        self,
        request: fc__open_20210406_models.GetResourceTagsRequest,
    ) -> fc__open_20210406_models.GetResourceTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetResourceTagsHeaders()
        return await self.get_resource_tags_with_options_async(request, headers, runtime)

    def get_service_with_options(
        self,
        service_name: str,
        request: fc__open_20210406_models.GetServiceRequest,
        headers: fc__open_20210406_models.GetServiceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.GetServiceRequest,
        headers: fc__open_20210406_models.GetServiceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        service_name: str,
        request: fc__open_20210406_models.GetServiceRequest,
    ) -> fc__open_20210406_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetServiceHeaders()
        return self.get_service_with_options(service_name, request, headers, runtime)

    async def get_service_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.GetServiceRequest,
    ) -> fc__open_20210406_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetServiceHeaders()
        return await self.get_service_with_options_async(service_name, request, headers, runtime)

    def get_stateful_async_invocation_with_options(
        self,
        service_name: str,
        function_name: str,
        invocation_id: str,
        request: fc__open_20210406_models.GetStatefulAsyncInvocationRequest,
        headers: fc__open_20210406_models.GetStatefulAsyncInvocationHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetStatefulAsyncInvocationResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: GetStatefulAsyncInvocationRequest
        @param headers: GetStatefulAsyncInvocationHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStatefulAsyncInvocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['X-Fc-Code-Checksum'] = UtilClient.to_jsonstring(headers.x_fc_code_checksum)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['X-Fc-Invocation-Type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['X-Fc-Log-Type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStatefulAsyncInvocation',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/stateful-async-invocations/{OpenApiUtilClient.get_encode_param(invocation_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetStatefulAsyncInvocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stateful_async_invocation_with_options_async(
        self,
        service_name: str,
        function_name: str,
        invocation_id: str,
        request: fc__open_20210406_models.GetStatefulAsyncInvocationRequest,
        headers: fc__open_20210406_models.GetStatefulAsyncInvocationHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetStatefulAsyncInvocationResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: GetStatefulAsyncInvocationRequest
        @param headers: GetStatefulAsyncInvocationHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStatefulAsyncInvocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['X-Fc-Code-Checksum'] = UtilClient.to_jsonstring(headers.x_fc_code_checksum)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['X-Fc-Invocation-Type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['X-Fc-Log-Type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStatefulAsyncInvocation',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/stateful-async-invocations/{OpenApiUtilClient.get_encode_param(invocation_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetStatefulAsyncInvocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stateful_async_invocation(
        self,
        service_name: str,
        function_name: str,
        invocation_id: str,
        request: fc__open_20210406_models.GetStatefulAsyncInvocationRequest,
    ) -> fc__open_20210406_models.GetStatefulAsyncInvocationResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: GetStatefulAsyncInvocationRequest
        @return: GetStatefulAsyncInvocationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetStatefulAsyncInvocationHeaders()
        return self.get_stateful_async_invocation_with_options(service_name, function_name, invocation_id, request, headers, runtime)

    async def get_stateful_async_invocation_async(
        self,
        service_name: str,
        function_name: str,
        invocation_id: str,
        request: fc__open_20210406_models.GetStatefulAsyncInvocationRequest,
    ) -> fc__open_20210406_models.GetStatefulAsyncInvocationResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: GetStatefulAsyncInvocationRequest
        @return: GetStatefulAsyncInvocationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetStatefulAsyncInvocationHeaders()
        return await self.get_stateful_async_invocation_with_options_async(service_name, function_name, invocation_id, request, headers, runtime)

    def get_trigger_with_options(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
        headers: fc__open_20210406_models.GetTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetTriggerResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetTrigger',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trigger_with_options_async(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
        headers: fc__open_20210406_models.GetTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.GetTriggerResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetTrigger',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trigger(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
    ) -> fc__open_20210406_models.GetTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetTriggerHeaders()
        return self.get_trigger_with_options(service_name, function_name, trigger_name, headers, runtime)

    async def get_trigger_async(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
    ) -> fc__open_20210406_models.GetTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.GetTriggerHeaders()
        return await self.get_trigger_with_options_async(service_name, function_name, trigger_name, headers, runtime)

    def invoke_function_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.InvokeFunctionRequest,
        headers: fc__open_20210406_models.InvokeFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.InvokeFunctionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = ''
        if not UtilClient.is_unset(request.body):
            body = UtilClient.to_string(request.body)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['X-Fc-Invocation-Type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['X-Fc-Log-Type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        if not UtilClient.is_unset(headers.x_fc_stateful_async_invocation_id):
            real_headers['X-Fc-Stateful-Async-Invocation-Id'] = UtilClient.to_jsonstring(headers.x_fc_stateful_async_invocation_id)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=body
        )
        params = open_api_models.Params(
            action='InvokeFunction',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/invocations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='byte'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.InvokeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_function_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.InvokeFunctionRequest,
        headers: fc__open_20210406_models.InvokeFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.InvokeFunctionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = ''
        if not UtilClient.is_unset(request.body):
            body = UtilClient.to_string(request.body)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['X-Fc-Invocation-Type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['X-Fc-Log-Type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        if not UtilClient.is_unset(headers.x_fc_stateful_async_invocation_id):
            real_headers['X-Fc-Stateful-Async-Invocation-Id'] = UtilClient.to_jsonstring(headers.x_fc_stateful_async_invocation_id)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=body
        )
        params = open_api_models.Params(
            action='InvokeFunction',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/invocations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='byte'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.InvokeFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_function(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.InvokeFunctionRequest,
    ) -> fc__open_20210406_models.InvokeFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.InvokeFunctionHeaders()
        return self.invoke_function_with_options(service_name, function_name, request, headers, runtime)

    async def invoke_function_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.InvokeFunctionRequest,
    ) -> fc__open_20210406_models.InvokeFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.InvokeFunctionHeaders()
        return await self.invoke_function_with_options_async(service_name, function_name, request, headers, runtime)

    def list_aliases_with_options(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListAliasesRequest,
        headers: fc__open_20210406_models.ListAliasesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListAliasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAliases',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/aliases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliases_with_options_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListAliasesRequest,
        headers: fc__open_20210406_models.ListAliasesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListAliasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAliases',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/aliases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListAliasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliases(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListAliasesRequest,
    ) -> fc__open_20210406_models.ListAliasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListAliasesHeaders()
        return self.list_aliases_with_options(service_name, request, headers, runtime)

    async def list_aliases_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListAliasesRequest,
    ) -> fc__open_20210406_models.ListAliasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListAliasesHeaders()
        return await self.list_aliases_with_options_async(service_name, request, headers, runtime)

    def list_custom_domains_with_options(
        self,
        request: fc__open_20210406_models.ListCustomDomainsRequest,
        headers: fc__open_20210406_models.ListCustomDomainsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListCustomDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomDomains',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/custom-domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListCustomDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_domains_with_options_async(
        self,
        request: fc__open_20210406_models.ListCustomDomainsRequest,
        headers: fc__open_20210406_models.ListCustomDomainsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListCustomDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomDomains',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/custom-domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListCustomDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_domains(
        self,
        request: fc__open_20210406_models.ListCustomDomainsRequest,
    ) -> fc__open_20210406_models.ListCustomDomainsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListCustomDomainsHeaders()
        return self.list_custom_domains_with_options(request, headers, runtime)

    async def list_custom_domains_async(
        self,
        request: fc__open_20210406_models.ListCustomDomainsRequest,
    ) -> fc__open_20210406_models.ListCustomDomainsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListCustomDomainsHeaders()
        return await self.list_custom_domains_with_options_async(request, headers, runtime)

    def list_event_sources_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListEventSourcesRequest,
        headers: fc__open_20210406_models.ListEventSourcesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListEventSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventSources',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/event-sources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListEventSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_sources_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListEventSourcesRequest,
        headers: fc__open_20210406_models.ListEventSourcesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListEventSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventSources',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/event-sources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListEventSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_sources(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListEventSourcesRequest,
    ) -> fc__open_20210406_models.ListEventSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListEventSourcesHeaders()
        return self.list_event_sources_with_options(service_name, function_name, request, headers, runtime)

    async def list_event_sources_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListEventSourcesRequest,
    ) -> fc__open_20210406_models.ListEventSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListEventSourcesHeaders()
        return await self.list_event_sources_with_options_async(service_name, function_name, request, headers, runtime)

    def list_function_async_invoke_configs_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListFunctionAsyncInvokeConfigsRequest,
        headers: fc__open_20210406_models.ListFunctionAsyncInvokeConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListFunctionAsyncInvokeConfigsResponse:
        """
        StatefulAsyncInvocation indicates whether the asynchronous task feature is enabled. If StatefulAsyncInvocation is set to true, the asynchronous task is enabled. All asynchronous invocations to the function corresponding to this configuration change to asynchronous task mode.
        
        @param request: ListFunctionAsyncInvokeConfigsRequest
        @param headers: ListFunctionAsyncInvokeConfigsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionAsyncInvokeConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['X-Fc-Code-Checksum'] = UtilClient.to_jsonstring(headers.x_fc_code_checksum)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['X-Fc-Invocation-Type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['X-Fc-Log-Type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionAsyncInvokeConfigs',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListFunctionAsyncInvokeConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_async_invoke_configs_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListFunctionAsyncInvokeConfigsRequest,
        headers: fc__open_20210406_models.ListFunctionAsyncInvokeConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListFunctionAsyncInvokeConfigsResponse:
        """
        StatefulAsyncInvocation indicates whether the asynchronous task feature is enabled. If StatefulAsyncInvocation is set to true, the asynchronous task is enabled. All asynchronous invocations to the function corresponding to this configuration change to asynchronous task mode.
        
        @param request: ListFunctionAsyncInvokeConfigsRequest
        @param headers: ListFunctionAsyncInvokeConfigsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionAsyncInvokeConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['X-Fc-Code-Checksum'] = UtilClient.to_jsonstring(headers.x_fc_code_checksum)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['X-Fc-Invocation-Type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['X-Fc-Log-Type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionAsyncInvokeConfigs',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListFunctionAsyncInvokeConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_async_invoke_configs(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListFunctionAsyncInvokeConfigsRequest,
    ) -> fc__open_20210406_models.ListFunctionAsyncInvokeConfigsResponse:
        """
        StatefulAsyncInvocation indicates whether the asynchronous task feature is enabled. If StatefulAsyncInvocation is set to true, the asynchronous task is enabled. All asynchronous invocations to the function corresponding to this configuration change to asynchronous task mode.
        
        @param request: ListFunctionAsyncInvokeConfigsRequest
        @return: ListFunctionAsyncInvokeConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListFunctionAsyncInvokeConfigsHeaders()
        return self.list_function_async_invoke_configs_with_options(service_name, function_name, request, headers, runtime)

    async def list_function_async_invoke_configs_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListFunctionAsyncInvokeConfigsRequest,
    ) -> fc__open_20210406_models.ListFunctionAsyncInvokeConfigsResponse:
        """
        StatefulAsyncInvocation indicates whether the asynchronous task feature is enabled. If StatefulAsyncInvocation is set to true, the asynchronous task is enabled. All asynchronous invocations to the function corresponding to this configuration change to asynchronous task mode.
        
        @param request: ListFunctionAsyncInvokeConfigsRequest
        @return: ListFunctionAsyncInvokeConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListFunctionAsyncInvokeConfigsHeaders()
        return await self.list_function_async_invoke_configs_with_options_async(service_name, function_name, request, headers, runtime)

    def list_functions_with_options(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListFunctionsRequest,
        headers: fc__open_20210406_models.ListFunctionsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListFunctionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_functions_with_options_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListFunctionsRequest,
        headers: fc__open_20210406_models.ListFunctionsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListFunctionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_functions(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListFunctionsRequest,
    ) -> fc__open_20210406_models.ListFunctionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListFunctionsHeaders()
        return self.list_functions_with_options(service_name, request, headers, runtime)

    async def list_functions_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListFunctionsRequest,
    ) -> fc__open_20210406_models.ListFunctionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListFunctionsHeaders()
        return await self.list_functions_with_options_async(service_name, request, headers, runtime)

    def list_instances_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListInstancesRequest,
        headers: fc__open_20210406_models.ListInstancesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListInstancesResponse:
        """
        The ListInstances operation allows you to query the available instances of a function.
        Available instances are instances that are processing requests or can be scheduled to process requests. Available instances queried by the ListInstances operation are the same as those that can be used when you call the InvokeFunction operation with the same values specified for the `serviceName`, `functionName`, and `qualifier` parameters.
        
        @param request: ListInstancesRequest
        @param headers: ListInstancesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['instanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListInstancesRequest,
        headers: fc__open_20210406_models.ListInstancesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListInstancesResponse:
        """
        The ListInstances operation allows you to query the available instances of a function.
        Available instances are instances that are processing requests or can be scheduled to process requests. Available instances queried by the ListInstances operation are the same as those that can be used when you call the InvokeFunction operation with the same values specified for the `serviceName`, `functionName`, and `qualifier` parameters.
        
        @param request: ListInstancesRequest
        @param headers: ListInstancesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['instanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListInstancesRequest,
    ) -> fc__open_20210406_models.ListInstancesResponse:
        """
        The ListInstances operation allows you to query the available instances of a function.
        Available instances are instances that are processing requests or can be scheduled to process requests. Available instances queried by the ListInstances operation are the same as those that can be used when you call the InvokeFunction operation with the same values specified for the `serviceName`, `functionName`, and `qualifier` parameters.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListInstancesHeaders()
        return self.list_instances_with_options(service_name, function_name, request, headers, runtime)

    async def list_instances_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListInstancesRequest,
    ) -> fc__open_20210406_models.ListInstancesResponse:
        """
        The ListInstances operation allows you to query the available instances of a function.
        Available instances are instances that are processing requests or can be scheduled to process requests. Available instances queried by the ListInstances operation are the same as those that can be used when you call the InvokeFunction operation with the same values specified for the `serviceName`, `functionName`, and `qualifier` parameters.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListInstancesHeaders()
        return await self.list_instances_with_options_async(service_name, function_name, request, headers, runtime)

    def list_layer_versions_with_options(
        self,
        layer_name: str,
        request: fc__open_20210406_models.ListLayerVersionsRequest,
        headers: fc__open_20210406_models.ListLayerVersionsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListLayerVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.start_version):
            query['startVersion'] = request.start_version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayerVersions',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListLayerVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_layer_versions_with_options_async(
        self,
        layer_name: str,
        request: fc__open_20210406_models.ListLayerVersionsRequest,
        headers: fc__open_20210406_models.ListLayerVersionsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListLayerVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.start_version):
            query['startVersion'] = request.start_version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayerVersions',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListLayerVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_layer_versions(
        self,
        layer_name: str,
        request: fc__open_20210406_models.ListLayerVersionsRequest,
    ) -> fc__open_20210406_models.ListLayerVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListLayerVersionsHeaders()
        return self.list_layer_versions_with_options(layer_name, request, headers, runtime)

    async def list_layer_versions_async(
        self,
        layer_name: str,
        request: fc__open_20210406_models.ListLayerVersionsRequest,
    ) -> fc__open_20210406_models.ListLayerVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListLayerVersionsHeaders()
        return await self.list_layer_versions_with_options_async(layer_name, request, headers, runtime)

    def list_layers_with_options(
        self,
        request: fc__open_20210406_models.ListLayersRequest,
        headers: fc__open_20210406_models.ListLayersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListLayersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.official):
            query['official'] = request.official
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayers',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListLayersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_layers_with_options_async(
        self,
        request: fc__open_20210406_models.ListLayersRequest,
        headers: fc__open_20210406_models.ListLayersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListLayersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.official):
            query['official'] = request.official
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayers',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListLayersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_layers(
        self,
        request: fc__open_20210406_models.ListLayersRequest,
    ) -> fc__open_20210406_models.ListLayersResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListLayersHeaders()
        return self.list_layers_with_options(request, headers, runtime)

    async def list_layers_async(
        self,
        request: fc__open_20210406_models.ListLayersRequest,
    ) -> fc__open_20210406_models.ListLayersResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListLayersHeaders()
        return await self.list_layers_with_options_async(request, headers, runtime)

    def list_on_demand_configs_with_options(
        self,
        request: fc__open_20210406_models.ListOnDemandConfigsRequest,
        headers: fc__open_20210406_models.ListOnDemandConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListOnDemandConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnDemandConfigs',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/on-demand-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListOnDemandConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_on_demand_configs_with_options_async(
        self,
        request: fc__open_20210406_models.ListOnDemandConfigsRequest,
        headers: fc__open_20210406_models.ListOnDemandConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListOnDemandConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnDemandConfigs',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/on-demand-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListOnDemandConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_on_demand_configs(
        self,
        request: fc__open_20210406_models.ListOnDemandConfigsRequest,
    ) -> fc__open_20210406_models.ListOnDemandConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListOnDemandConfigsHeaders()
        return self.list_on_demand_configs_with_options(request, headers, runtime)

    async def list_on_demand_configs_async(
        self,
        request: fc__open_20210406_models.ListOnDemandConfigsRequest,
    ) -> fc__open_20210406_models.ListOnDemandConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListOnDemandConfigsHeaders()
        return await self.list_on_demand_configs_with_options_async(request, headers, runtime)

    def list_provision_configs_with_options(
        self,
        request: fc__open_20210406_models.ListProvisionConfigsRequest,
        headers: fc__open_20210406_models.ListProvisionConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListProvisionConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionConfigs',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/provision-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListProvisionConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_provision_configs_with_options_async(
        self,
        request: fc__open_20210406_models.ListProvisionConfigsRequest,
        headers: fc__open_20210406_models.ListProvisionConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListProvisionConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionConfigs',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/provision-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListProvisionConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_provision_configs(
        self,
        request: fc__open_20210406_models.ListProvisionConfigsRequest,
    ) -> fc__open_20210406_models.ListProvisionConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListProvisionConfigsHeaders()
        return self.list_provision_configs_with_options(request, headers, runtime)

    async def list_provision_configs_async(
        self,
        request: fc__open_20210406_models.ListProvisionConfigsRequest,
    ) -> fc__open_20210406_models.ListProvisionConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListProvisionConfigsHeaders()
        return await self.list_provision_configs_with_options_async(request, headers, runtime)

    def list_reserved_capacities_with_options(
        self,
        request: fc__open_20210406_models.ListReservedCapacitiesRequest,
        headers: fc__open_20210406_models.ListReservedCapacitiesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListReservedCapacitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReservedCapacities',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/reserved-capacities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListReservedCapacitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_reserved_capacities_with_options_async(
        self,
        request: fc__open_20210406_models.ListReservedCapacitiesRequest,
        headers: fc__open_20210406_models.ListReservedCapacitiesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListReservedCapacitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReservedCapacities',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/reserved-capacities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListReservedCapacitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_reserved_capacities(
        self,
        request: fc__open_20210406_models.ListReservedCapacitiesRequest,
    ) -> fc__open_20210406_models.ListReservedCapacitiesResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListReservedCapacitiesHeaders()
        return self.list_reserved_capacities_with_options(request, headers, runtime)

    async def list_reserved_capacities_async(
        self,
        request: fc__open_20210406_models.ListReservedCapacitiesRequest,
    ) -> fc__open_20210406_models.ListReservedCapacitiesResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListReservedCapacitiesHeaders()
        return await self.list_reserved_capacities_with_options_async(request, headers, runtime)

    def list_service_versions_with_options(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListServiceVersionsRequest,
        headers: fc__open_20210406_models.ListServiceVersionsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListServiceVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceVersions',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListServiceVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_versions_with_options_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListServiceVersionsRequest,
        headers: fc__open_20210406_models.ListServiceVersionsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListServiceVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceVersions',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListServiceVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_versions(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListServiceVersionsRequest,
    ) -> fc__open_20210406_models.ListServiceVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListServiceVersionsHeaders()
        return self.list_service_versions_with_options(service_name, request, headers, runtime)

    async def list_service_versions_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.ListServiceVersionsRequest,
    ) -> fc__open_20210406_models.ListServiceVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListServiceVersionsHeaders()
        return await self.list_service_versions_with_options_async(service_name, request, headers, runtime)

    def list_services_with_options(
        self,
        request: fc__open_20210406_models.ListServicesRequest,
        headers: fc__open_20210406_models.ListServicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: fc__open_20210406_models.ListServicesRequest,
        headers: fc__open_20210406_models.ListServicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: fc__open_20210406_models.ListServicesRequest,
    ) -> fc__open_20210406_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListServicesHeaders()
        return self.list_services_with_options(request, headers, runtime)

    async def list_services_async(
        self,
        request: fc__open_20210406_models.ListServicesRequest,
    ) -> fc__open_20210406_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListServicesHeaders()
        return await self.list_services_with_options_async(request, headers, runtime)

    def list_stateful_async_invocation_functions_with_options(
        self,
        request: fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsRequest,
        headers: fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: ListStatefulAsyncInvocationFunctionsRequest
        @param headers: ListStatefulAsyncInvocationFunctionsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStatefulAsyncInvocationFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStatefulAsyncInvocationFunctions',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/stateful-async-invocation-functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stateful_async_invocation_functions_with_options_async(
        self,
        request: fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsRequest,
        headers: fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: ListStatefulAsyncInvocationFunctionsRequest
        @param headers: ListStatefulAsyncInvocationFunctionsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStatefulAsyncInvocationFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStatefulAsyncInvocationFunctions',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/stateful-async-invocation-functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stateful_async_invocation_functions(
        self,
        request: fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsRequest,
    ) -> fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: ListStatefulAsyncInvocationFunctionsRequest
        @return: ListStatefulAsyncInvocationFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsHeaders()
        return self.list_stateful_async_invocation_functions_with_options(request, headers, runtime)

    async def list_stateful_async_invocation_functions_async(
        self,
        request: fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsRequest,
    ) -> fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: ListStatefulAsyncInvocationFunctionsRequest
        @return: ListStatefulAsyncInvocationFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListStatefulAsyncInvocationFunctionsHeaders()
        return await self.list_stateful_async_invocation_functions_with_options_async(request, headers, runtime)

    def list_stateful_async_invocations_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListStatefulAsyncInvocationsRequest,
        headers: fc__open_20210406_models.ListStatefulAsyncInvocationsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListStatefulAsyncInvocationsResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: ListStatefulAsyncInvocationsRequest
        @param headers: ListStatefulAsyncInvocationsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStatefulAsyncInvocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_payload):
            query['includePayload'] = request.include_payload
        if not UtilClient.is_unset(request.invocation_id_prefix):
            query['invocationIdPrefix'] = request.invocation_id_prefix
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.sort_order_by_time):
            query['sortOrderByTime'] = request.sort_order_by_time
        if not UtilClient.is_unset(request.started_time_begin):
            query['startedTimeBegin'] = request.started_time_begin
        if not UtilClient.is_unset(request.started_time_end):
            query['startedTimeEnd'] = request.started_time_end
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['X-Fc-Code-Checksum'] = UtilClient.to_jsonstring(headers.x_fc_code_checksum)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['X-Fc-Invocation-Type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['X-Fc-Log-Type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStatefulAsyncInvocations',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/stateful-async-invocations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListStatefulAsyncInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stateful_async_invocations_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListStatefulAsyncInvocationsRequest,
        headers: fc__open_20210406_models.ListStatefulAsyncInvocationsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListStatefulAsyncInvocationsResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: ListStatefulAsyncInvocationsRequest
        @param headers: ListStatefulAsyncInvocationsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStatefulAsyncInvocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_payload):
            query['includePayload'] = request.include_payload
        if not UtilClient.is_unset(request.invocation_id_prefix):
            query['invocationIdPrefix'] = request.invocation_id_prefix
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.sort_order_by_time):
            query['sortOrderByTime'] = request.sort_order_by_time
        if not UtilClient.is_unset(request.started_time_begin):
            query['startedTimeBegin'] = request.started_time_begin
        if not UtilClient.is_unset(request.started_time_end):
            query['startedTimeEnd'] = request.started_time_end
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['X-Fc-Code-Checksum'] = UtilClient.to_jsonstring(headers.x_fc_code_checksum)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['X-Fc-Invocation-Type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['X-Fc-Log-Type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStatefulAsyncInvocations',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/stateful-async-invocations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListStatefulAsyncInvocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stateful_async_invocations(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListStatefulAsyncInvocationsRequest,
    ) -> fc__open_20210406_models.ListStatefulAsyncInvocationsResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: ListStatefulAsyncInvocationsRequest
        @return: ListStatefulAsyncInvocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListStatefulAsyncInvocationsHeaders()
        return self.list_stateful_async_invocations_with_options(service_name, function_name, request, headers, runtime)

    async def list_stateful_async_invocations_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListStatefulAsyncInvocationsRequest,
    ) -> fc__open_20210406_models.ListStatefulAsyncInvocationsResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: ListStatefulAsyncInvocationsRequest
        @return: ListStatefulAsyncInvocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListStatefulAsyncInvocationsHeaders()
        return await self.list_stateful_async_invocations_with_options_async(service_name, function_name, request, headers, runtime)

    def list_tagged_resources_with_options(
        self,
        request: fc__open_20210406_models.ListTaggedResourcesRequest,
        headers: fc__open_20210406_models.ListTaggedResourcesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListTaggedResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaggedResources',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListTaggedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tagged_resources_with_options_async(
        self,
        request: fc__open_20210406_models.ListTaggedResourcesRequest,
        headers: fc__open_20210406_models.ListTaggedResourcesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListTaggedResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaggedResources',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListTaggedResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tagged_resources(
        self,
        request: fc__open_20210406_models.ListTaggedResourcesRequest,
    ) -> fc__open_20210406_models.ListTaggedResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListTaggedResourcesHeaders()
        return self.list_tagged_resources_with_options(request, headers, runtime)

    async def list_tagged_resources_async(
        self,
        request: fc__open_20210406_models.ListTaggedResourcesRequest,
    ) -> fc__open_20210406_models.ListTaggedResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListTaggedResourcesHeaders()
        return await self.list_tagged_resources_with_options_async(request, headers, runtime)

    def list_triggers_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListTriggersRequest,
        headers: fc__open_20210406_models.ListTriggersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListTriggersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTriggers',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListTriggersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_triggers_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListTriggersRequest,
        headers: fc__open_20210406_models.ListTriggersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListTriggersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTriggers',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListTriggersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_triggers(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListTriggersRequest,
    ) -> fc__open_20210406_models.ListTriggersResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListTriggersHeaders()
        return self.list_triggers_with_options(service_name, function_name, request, headers, runtime)

    async def list_triggers_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.ListTriggersRequest,
    ) -> fc__open_20210406_models.ListTriggersResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListTriggersHeaders()
        return await self.list_triggers_with_options_async(service_name, function_name, request, headers, runtime)

    def list_vpc_bindings_with_options(
        self,
        service_name: str,
        headers: fc__open_20210406_models.ListVpcBindingsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListVpcBindingsResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListVpcBindings',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/bindings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListVpcBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_bindings_with_options_async(
        self,
        service_name: str,
        headers: fc__open_20210406_models.ListVpcBindingsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ListVpcBindingsResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListVpcBindings',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/bindings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListVpcBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_bindings(
        self,
        service_name: str,
    ) -> fc__open_20210406_models.ListVpcBindingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListVpcBindingsHeaders()
        return self.list_vpc_bindings_with_options(service_name, headers, runtime)

    async def list_vpc_bindings_async(
        self,
        service_name: str,
    ) -> fc__open_20210406_models.ListVpcBindingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ListVpcBindingsHeaders()
        return await self.list_vpc_bindings_with_options_async(service_name, headers, runtime)

    def publish_service_version_with_options(
        self,
        service_name: str,
        request: fc__open_20210406_models.PublishServiceVersionRequest,
        headers: fc__open_20210406_models.PublishServiceVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.PublishServiceVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishServiceVersion',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PublishServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_service_version_with_options_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.PublishServiceVersionRequest,
        headers: fc__open_20210406_models.PublishServiceVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.PublishServiceVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishServiceVersion',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PublishServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_service_version(
        self,
        service_name: str,
        request: fc__open_20210406_models.PublishServiceVersionRequest,
    ) -> fc__open_20210406_models.PublishServiceVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PublishServiceVersionHeaders()
        return self.publish_service_version_with_options(service_name, request, headers, runtime)

    async def publish_service_version_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.PublishServiceVersionRequest,
    ) -> fc__open_20210406_models.PublishServiceVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PublishServiceVersionHeaders()
        return await self.publish_service_version_with_options_async(service_name, request, headers, runtime)

    def put_function_async_invoke_config_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutFunctionAsyncInvokeConfigRequest,
        headers: fc__open_20210406_models.PutFunctionAsyncInvokeConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.PutFunctionAsyncInvokeConfigResponse:
        """
        StatefulAsyncInvocation specifies the configurations of the asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: PutFunctionAsyncInvokeConfigRequest
        @param headers: PutFunctionAsyncInvokeConfigHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutFunctionAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.destination_config):
            body['destinationConfig'] = request.destination_config
        if not UtilClient.is_unset(request.max_async_event_age_in_seconds):
            body['maxAsyncEventAgeInSeconds'] = request.max_async_event_age_in_seconds
        if not UtilClient.is_unset(request.max_async_retry_attempts):
            body['maxAsyncRetryAttempts'] = request.max_async_retry_attempts
        if not UtilClient.is_unset(request.stateful_invocation):
            body['statefulInvocation'] = request.stateful_invocation
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutFunctionAsyncInvokeConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PutFunctionAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_function_async_invoke_config_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutFunctionAsyncInvokeConfigRequest,
        headers: fc__open_20210406_models.PutFunctionAsyncInvokeConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.PutFunctionAsyncInvokeConfigResponse:
        """
        StatefulAsyncInvocation specifies the configurations of the asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: PutFunctionAsyncInvokeConfigRequest
        @param headers: PutFunctionAsyncInvokeConfigHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutFunctionAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.destination_config):
            body['destinationConfig'] = request.destination_config
        if not UtilClient.is_unset(request.max_async_event_age_in_seconds):
            body['maxAsyncEventAgeInSeconds'] = request.max_async_event_age_in_seconds
        if not UtilClient.is_unset(request.max_async_retry_attempts):
            body['maxAsyncRetryAttempts'] = request.max_async_retry_attempts
        if not UtilClient.is_unset(request.stateful_invocation):
            body['statefulInvocation'] = request.stateful_invocation
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutFunctionAsyncInvokeConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PutFunctionAsyncInvokeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_function_async_invoke_config(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutFunctionAsyncInvokeConfigRequest,
    ) -> fc__open_20210406_models.PutFunctionAsyncInvokeConfigResponse:
        """
        StatefulAsyncInvocation specifies the configurations of the asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: PutFunctionAsyncInvokeConfigRequest
        @return: PutFunctionAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PutFunctionAsyncInvokeConfigHeaders()
        return self.put_function_async_invoke_config_with_options(service_name, function_name, request, headers, runtime)

    async def put_function_async_invoke_config_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutFunctionAsyncInvokeConfigRequest,
    ) -> fc__open_20210406_models.PutFunctionAsyncInvokeConfigResponse:
        """
        StatefulAsyncInvocation specifies the configurations of the asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: PutFunctionAsyncInvokeConfigRequest
        @return: PutFunctionAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PutFunctionAsyncInvokeConfigHeaders()
        return await self.put_function_async_invoke_config_with_options_async(service_name, function_name, request, headers, runtime)

    def put_function_on_demand_config_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutFunctionOnDemandConfigRequest,
        headers: fc__open_20210406_models.PutFunctionOnDemandConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.PutFunctionOnDemandConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.maximum_instance_count):
            body['maximumInstanceCount'] = request.maximum_instance_count
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutFunctionOnDemandConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/on-demand-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PutFunctionOnDemandConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_function_on_demand_config_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutFunctionOnDemandConfigRequest,
        headers: fc__open_20210406_models.PutFunctionOnDemandConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.PutFunctionOnDemandConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.maximum_instance_count):
            body['maximumInstanceCount'] = request.maximum_instance_count
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutFunctionOnDemandConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/on-demand-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PutFunctionOnDemandConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_function_on_demand_config(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutFunctionOnDemandConfigRequest,
    ) -> fc__open_20210406_models.PutFunctionOnDemandConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PutFunctionOnDemandConfigHeaders()
        return self.put_function_on_demand_config_with_options(service_name, function_name, request, headers, runtime)

    async def put_function_on_demand_config_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutFunctionOnDemandConfigRequest,
    ) -> fc__open_20210406_models.PutFunctionOnDemandConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PutFunctionOnDemandConfigHeaders()
        return await self.put_function_on_demand_config_with_options_async(service_name, function_name, request, headers, runtime)

    def put_layer_aclwith_options(
        self,
        layer_name: str,
        request: fc__open_20210406_models.PutLayerACLRequest,
        headers: fc__open_20210406_models.PutLayerACLHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.PutLayerACLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutLayerACL',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/acl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PutLayerACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_layer_aclwith_options_async(
        self,
        layer_name: str,
        request: fc__open_20210406_models.PutLayerACLRequest,
        headers: fc__open_20210406_models.PutLayerACLHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.PutLayerACLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutLayerACL',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/acl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PutLayerACLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_layer_acl(
        self,
        layer_name: str,
        request: fc__open_20210406_models.PutLayerACLRequest,
    ) -> fc__open_20210406_models.PutLayerACLResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PutLayerACLHeaders()
        return self.put_layer_aclwith_options(layer_name, request, headers, runtime)

    async def put_layer_acl_async(
        self,
        layer_name: str,
        request: fc__open_20210406_models.PutLayerACLRequest,
    ) -> fc__open_20210406_models.PutLayerACLResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PutLayerACLHeaders()
        return await self.put_layer_aclwith_options_async(layer_name, request, headers, runtime)

    def put_provision_config_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutProvisionConfigRequest,
        headers: fc__open_20210406_models.PutProvisionConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.PutProvisionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.always_allocate_cpu):
            body['alwaysAllocateCPU'] = request.always_allocate_cpu
        if not UtilClient.is_unset(request.scheduled_actions):
            body['scheduledActions'] = request.scheduled_actions
        if not UtilClient.is_unset(request.target):
            body['target'] = request.target
        if not UtilClient.is_unset(request.target_tracking_policies):
            body['targetTrackingPolicies'] = request.target_tracking_policies
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutProvisionConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/provision-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PutProvisionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_provision_config_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutProvisionConfigRequest,
        headers: fc__open_20210406_models.PutProvisionConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.PutProvisionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.always_allocate_cpu):
            body['alwaysAllocateCPU'] = request.always_allocate_cpu
        if not UtilClient.is_unset(request.scheduled_actions):
            body['scheduledActions'] = request.scheduled_actions
        if not UtilClient.is_unset(request.target):
            body['target'] = request.target
        if not UtilClient.is_unset(request.target_tracking_policies):
            body['targetTrackingPolicies'] = request.target_tracking_policies
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutProvisionConfig',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/provision-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PutProvisionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_provision_config(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutProvisionConfigRequest,
    ) -> fc__open_20210406_models.PutProvisionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PutProvisionConfigHeaders()
        return self.put_provision_config_with_options(service_name, function_name, request, headers, runtime)

    async def put_provision_config_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.PutProvisionConfigRequest,
    ) -> fc__open_20210406_models.PutProvisionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PutProvisionConfigHeaders()
        return await self.put_provision_config_with_options_async(service_name, function_name, request, headers, runtime)

    def register_event_source_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.RegisterEventSourceRequest,
        headers: fc__open_20210406_models.RegisterEventSourceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.RegisterEventSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.source_arn):
            body['sourceArn'] = request.source_arn
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterEventSource',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/event-sources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.RegisterEventSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_event_source_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.RegisterEventSourceRequest,
        headers: fc__open_20210406_models.RegisterEventSourceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.RegisterEventSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.source_arn):
            body['sourceArn'] = request.source_arn
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterEventSource',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/event-sources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.RegisterEventSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_event_source(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.RegisterEventSourceRequest,
    ) -> fc__open_20210406_models.RegisterEventSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.RegisterEventSourceHeaders()
        return self.register_event_source_with_options(service_name, function_name, request, headers, runtime)

    async def register_event_source_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.RegisterEventSourceRequest,
    ) -> fc__open_20210406_models.RegisterEventSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.RegisterEventSourceHeaders()
        return await self.register_event_source_with_options_async(service_name, function_name, request, headers, runtime)

    def release_gpuinstance_with_options(
        self,
        instance_id: str,
        headers: fc__open_20210406_models.ReleaseGPUInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ReleaseGPUInstanceResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ReleaseGPUInstance',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/gpuInstances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ReleaseGPUInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_gpuinstance_with_options_async(
        self,
        instance_id: str,
        headers: fc__open_20210406_models.ReleaseGPUInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.ReleaseGPUInstanceResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ReleaseGPUInstance',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/gpuInstances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ReleaseGPUInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_gpuinstance(
        self,
        instance_id: str,
    ) -> fc__open_20210406_models.ReleaseGPUInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ReleaseGPUInstanceHeaders()
        return self.release_gpuinstance_with_options(instance_id, headers, runtime)

    async def release_gpuinstance_async(
        self,
        instance_id: str,
    ) -> fc__open_20210406_models.ReleaseGPUInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.ReleaseGPUInstanceHeaders()
        return await self.release_gpuinstance_with_options_async(instance_id, headers, runtime)

    def stop_stateful_async_invocation_with_options(
        self,
        service_name: str,
        function_name: str,
        invocation_id: str,
        request: fc__open_20210406_models.StopStatefulAsyncInvocationRequest,
        headers: fc__open_20210406_models.StopStatefulAsyncInvocationHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.StopStatefulAsyncInvocationResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: StopStatefulAsyncInvocationRequest
        @param headers: StopStatefulAsyncInvocationHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopStatefulAsyncInvocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopStatefulAsyncInvocation',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/stateful-async-invocations/{OpenApiUtilClient.get_encode_param(invocation_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.StopStatefulAsyncInvocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_stateful_async_invocation_with_options_async(
        self,
        service_name: str,
        function_name: str,
        invocation_id: str,
        request: fc__open_20210406_models.StopStatefulAsyncInvocationRequest,
        headers: fc__open_20210406_models.StopStatefulAsyncInvocationHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.StopStatefulAsyncInvocationResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: StopStatefulAsyncInvocationRequest
        @param headers: StopStatefulAsyncInvocationHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopStatefulAsyncInvocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopStatefulAsyncInvocation',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/stateful-async-invocations/{OpenApiUtilClient.get_encode_param(invocation_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.StopStatefulAsyncInvocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_stateful_async_invocation(
        self,
        service_name: str,
        function_name: str,
        invocation_id: str,
        request: fc__open_20210406_models.StopStatefulAsyncInvocationRequest,
    ) -> fc__open_20210406_models.StopStatefulAsyncInvocationResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: StopStatefulAsyncInvocationRequest
        @return: StopStatefulAsyncInvocationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.StopStatefulAsyncInvocationHeaders()
        return self.stop_stateful_async_invocation_with_options(service_name, function_name, invocation_id, request, headers, runtime)

    async def stop_stateful_async_invocation_async(
        self,
        service_name: str,
        function_name: str,
        invocation_id: str,
        request: fc__open_20210406_models.StopStatefulAsyncInvocationRequest,
    ) -> fc__open_20210406_models.StopStatefulAsyncInvocationResponse:
        """
        StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        
        @param request: StopStatefulAsyncInvocationRequest
        @return: StopStatefulAsyncInvocationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.StopStatefulAsyncInvocationHeaders()
        return await self.stop_stateful_async_invocation_with_options_async(service_name, function_name, invocation_id, request, headers, runtime)

    def tag_resource_with_options(
        self,
        request: fc__open_20210406_models.TagResourceRequest,
        headers: fc__open_20210406_models.TagResourceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.TagResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['resourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResource',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/tag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.TagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resource_with_options_async(
        self,
        request: fc__open_20210406_models.TagResourceRequest,
        headers: fc__open_20210406_models.TagResourceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.TagResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['resourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResource',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/tag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.TagResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resource(
        self,
        request: fc__open_20210406_models.TagResourceRequest,
    ) -> fc__open_20210406_models.TagResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.TagResourceHeaders()
        return self.tag_resource_with_options(request, headers, runtime)

    async def tag_resource_async(
        self,
        request: fc__open_20210406_models.TagResourceRequest,
    ) -> fc__open_20210406_models.TagResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.TagResourceHeaders()
        return await self.tag_resource_with_options_async(request, headers, runtime)

    def untag_resource_with_options(
        self,
        request: fc__open_20210406_models.UntagResourceRequest,
        headers: fc__open_20210406_models.UntagResourceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UntagResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['all'] = request.all
        if not UtilClient.is_unset(request.resource_arn):
            body['resourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.tag_keys):
            body['tagKeys'] = request.tag_keys
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResource',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/tag',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UntagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resource_with_options_async(
        self,
        request: fc__open_20210406_models.UntagResourceRequest,
        headers: fc__open_20210406_models.UntagResourceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UntagResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['all'] = request.all
        if not UtilClient.is_unset(request.resource_arn):
            body['resourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.tag_keys):
            body['tagKeys'] = request.tag_keys
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResource',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/tag',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UntagResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resource(
        self,
        request: fc__open_20210406_models.UntagResourceRequest,
    ) -> fc__open_20210406_models.UntagResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UntagResourceHeaders()
        return self.untag_resource_with_options(request, headers, runtime)

    async def untag_resource_async(
        self,
        request: fc__open_20210406_models.UntagResourceRequest,
    ) -> fc__open_20210406_models.UntagResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UntagResourceHeaders()
        return await self.untag_resource_with_options_async(request, headers, runtime)

    def update_alias_with_options(
        self,
        service_name: str,
        alias_name: str,
        request: fc__open_20210406_models.UpdateAliasRequest,
        headers: fc__open_20210406_models.UpdateAliasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UpdateAliasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_version_weight):
            body['additionalVersionWeight'] = request.additional_version_weight
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.resolve_policy):
            body['resolvePolicy'] = request.resolve_policy
        if not UtilClient.is_unset(request.route_policy):
            body['routePolicy'] = request.route_policy
        if not UtilClient.is_unset(request.version_id):
            body['versionId'] = request.version_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAlias',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alias_with_options_async(
        self,
        service_name: str,
        alias_name: str,
        request: fc__open_20210406_models.UpdateAliasRequest,
        headers: fc__open_20210406_models.UpdateAliasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UpdateAliasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_version_weight):
            body['additionalVersionWeight'] = request.additional_version_weight
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.resolve_policy):
            body['resolvePolicy'] = request.resolve_policy
        if not UtilClient.is_unset(request.route_policy):
            body['routePolicy'] = request.route_policy
        if not UtilClient.is_unset(request.version_id):
            body['versionId'] = request.version_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAlias',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alias(
        self,
        service_name: str,
        alias_name: str,
        request: fc__open_20210406_models.UpdateAliasRequest,
    ) -> fc__open_20210406_models.UpdateAliasResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateAliasHeaders()
        return self.update_alias_with_options(service_name, alias_name, request, headers, runtime)

    async def update_alias_async(
        self,
        service_name: str,
        alias_name: str,
        request: fc__open_20210406_models.UpdateAliasRequest,
    ) -> fc__open_20210406_models.UpdateAliasResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateAliasHeaders()
        return await self.update_alias_with_options_async(service_name, alias_name, request, headers, runtime)

    def update_custom_domain_with_options(
        self,
        domain_name: str,
        request: fc__open_20210406_models.UpdateCustomDomainRequest,
        headers: fc__open_20210406_models.UpdateCustomDomainHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UpdateCustomDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_config):
            body['certConfig'] = request.cert_config
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.route_config):
            body['routeConfig'] = request.route_config
        if not UtilClient.is_unset(request.tls_config):
            body['tlsConfig'] = request.tls_config
        if not UtilClient.is_unset(request.waf_config):
            body['wafConfig'] = request.waf_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomDomain',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_domain_with_options_async(
        self,
        domain_name: str,
        request: fc__open_20210406_models.UpdateCustomDomainRequest,
        headers: fc__open_20210406_models.UpdateCustomDomainHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UpdateCustomDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_config):
            body['certConfig'] = request.cert_config
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.route_config):
            body['routeConfig'] = request.route_config
        if not UtilClient.is_unset(request.tls_config):
            body['tlsConfig'] = request.tls_config
        if not UtilClient.is_unset(request.waf_config):
            body['wafConfig'] = request.waf_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomDomain',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_domain(
        self,
        domain_name: str,
        request: fc__open_20210406_models.UpdateCustomDomainRequest,
    ) -> fc__open_20210406_models.UpdateCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateCustomDomainHeaders()
        return self.update_custom_domain_with_options(domain_name, request, headers, runtime)

    async def update_custom_domain_async(
        self,
        domain_name: str,
        request: fc__open_20210406_models.UpdateCustomDomainRequest,
    ) -> fc__open_20210406_models.UpdateCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateCustomDomainHeaders()
        return await self.update_custom_domain_with_options_async(domain_name, request, headers, runtime)

    def update_function_with_options(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.UpdateFunctionRequest,
        headers: fc__open_20210406_models.UpdateFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UpdateFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_concurrency):
            body['InstanceConcurrency'] = request.instance_concurrency
        if not UtilClient.is_unset(request.ca_port):
            body['caPort'] = request.ca_port
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_container_config):
            body['customContainerConfig'] = request.custom_container_config
        if not UtilClient.is_unset(request.custom_dns):
            body['customDNS'] = request.custom_dns
        if not UtilClient.is_unset(request.custom_health_check_config):
            body['customHealthCheckConfig'] = request.custom_health_check_config
        if not UtilClient.is_unset(request.custom_runtime_config):
            body['customRuntimeConfig'] = request.custom_runtime_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disk_size):
            body['diskSize'] = request.disk_size
        if not UtilClient.is_unset(request.environment_variables):
            body['environmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.gpu_memory_size):
            body['gpuMemorySize'] = request.gpu_memory_size
        if not UtilClient.is_unset(request.handler):
            body['handler'] = request.handler
        if not UtilClient.is_unset(request.initialization_timeout):
            body['initializationTimeout'] = request.initialization_timeout
        if not UtilClient.is_unset(request.initializer):
            body['initializer'] = request.initializer
        if not UtilClient.is_unset(request.instance_lifecycle_config):
            body['instanceLifecycleConfig'] = request.instance_lifecycle_config
        if not UtilClient.is_unset(request.instance_soft_concurrency):
            body['instanceSoftConcurrency'] = request.instance_soft_concurrency
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.layers):
            body['layers'] = request.layers
        if not UtilClient.is_unset(request.memory_size):
            body['memorySize'] = request.memory_size
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['X-Fc-Code-Checksum'] = UtilClient.to_jsonstring(headers.x_fc_code_checksum)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_with_options_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.UpdateFunctionRequest,
        headers: fc__open_20210406_models.UpdateFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UpdateFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_concurrency):
            body['InstanceConcurrency'] = request.instance_concurrency
        if not UtilClient.is_unset(request.ca_port):
            body['caPort'] = request.ca_port
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_container_config):
            body['customContainerConfig'] = request.custom_container_config
        if not UtilClient.is_unset(request.custom_dns):
            body['customDNS'] = request.custom_dns
        if not UtilClient.is_unset(request.custom_health_check_config):
            body['customHealthCheckConfig'] = request.custom_health_check_config
        if not UtilClient.is_unset(request.custom_runtime_config):
            body['customRuntimeConfig'] = request.custom_runtime_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disk_size):
            body['diskSize'] = request.disk_size
        if not UtilClient.is_unset(request.environment_variables):
            body['environmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.gpu_memory_size):
            body['gpuMemorySize'] = request.gpu_memory_size
        if not UtilClient.is_unset(request.handler):
            body['handler'] = request.handler
        if not UtilClient.is_unset(request.initialization_timeout):
            body['initializationTimeout'] = request.initialization_timeout
        if not UtilClient.is_unset(request.initializer):
            body['initializer'] = request.initializer
        if not UtilClient.is_unset(request.instance_lifecycle_config):
            body['instanceLifecycleConfig'] = request.instance_lifecycle_config
        if not UtilClient.is_unset(request.instance_soft_concurrency):
            body['instanceSoftConcurrency'] = request.instance_soft_concurrency
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.layers):
            body['layers'] = request.layers
        if not UtilClient.is_unset(request.memory_size):
            body['memorySize'] = request.memory_size
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['X-Fc-Code-Checksum'] = UtilClient.to_jsonstring(headers.x_fc_code_checksum)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.UpdateFunctionRequest,
    ) -> fc__open_20210406_models.UpdateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateFunctionHeaders()
        return self.update_function_with_options(service_name, function_name, request, headers, runtime)

    async def update_function_async(
        self,
        service_name: str,
        function_name: str,
        request: fc__open_20210406_models.UpdateFunctionRequest,
    ) -> fc__open_20210406_models.UpdateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateFunctionHeaders()
        return await self.update_function_with_options_async(service_name, function_name, request, headers, runtime)

    def update_service_with_options(
        self,
        service_name: str,
        request: fc__open_20210406_models.UpdateServiceRequest,
        headers: fc__open_20210406_models.UpdateServiceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.internet_access):
            body['internetAccess'] = request.internet_access
        if not UtilClient.is_unset(request.log_config):
            body['logConfig'] = request.log_config
        if not UtilClient.is_unset(request.nas_config):
            body['nasConfig'] = request.nas_config
        if not UtilClient.is_unset(request.oss_mount_config):
            body['ossMountConfig'] = request.oss_mount_config
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.tracing_config):
            body['tracingConfig'] = request.tracing_config
        if not UtilClient.is_unset(request.vpc_config):
            body['vpcConfig'] = request.vpc_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.UpdateServiceRequest,
        headers: fc__open_20210406_models.UpdateServiceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.internet_access):
            body['internetAccess'] = request.internet_access
        if not UtilClient.is_unset(request.log_config):
            body['logConfig'] = request.log_config
        if not UtilClient.is_unset(request.nas_config):
            body['nasConfig'] = request.nas_config
        if not UtilClient.is_unset(request.oss_mount_config):
            body['ossMountConfig'] = request.oss_mount_config
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.tracing_config):
            body['tracingConfig'] = request.tracing_config
        if not UtilClient.is_unset(request.vpc_config):
            body['vpcConfig'] = request.vpc_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        service_name: str,
        request: fc__open_20210406_models.UpdateServiceRequest,
    ) -> fc__open_20210406_models.UpdateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateServiceHeaders()
        return self.update_service_with_options(service_name, request, headers, runtime)

    async def update_service_async(
        self,
        service_name: str,
        request: fc__open_20210406_models.UpdateServiceRequest,
    ) -> fc__open_20210406_models.UpdateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateServiceHeaders()
        return await self.update_service_with_options_async(service_name, request, headers, runtime)

    def update_trigger_with_options(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
        request: fc__open_20210406_models.UpdateTriggerRequest,
        headers: fc__open_20210406_models.UpdateTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UpdateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.invocation_role):
            body['invocationRole'] = request.invocation_role
        if not UtilClient.is_unset(request.qualifier):
            body['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrigger',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_trigger_with_options_async(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
        request: fc__open_20210406_models.UpdateTriggerRequest,
        headers: fc__open_20210406_models.UpdateTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc__open_20210406_models.UpdateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.invocation_role):
            body['invocationRole'] = request.invocation_role
        if not UtilClient.is_unset(request.qualifier):
            body['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = UtilClient.to_jsonstring(headers.x_fc_account_id)
        if not UtilClient.is_unset(headers.x_fc_date):
            real_headers['X-Fc-Date'] = UtilClient.to_jsonstring(headers.x_fc_date)
        if not UtilClient.is_unset(headers.x_fc_trace_id):
            real_headers['X-Fc-Trace-Id'] = UtilClient.to_jsonstring(headers.x_fc_trace_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrigger',
            version='2021-04-06',
            protocol='HTTPS',
            pathname=f'/2021-04-06/services/{OpenApiUtilClient.get_encode_param(service_name)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_trigger(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
        request: fc__open_20210406_models.UpdateTriggerRequest,
    ) -> fc__open_20210406_models.UpdateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateTriggerHeaders()
        return self.update_trigger_with_options(service_name, function_name, trigger_name, request, headers, runtime)

    async def update_trigger_async(
        self,
        service_name: str,
        function_name: str,
        trigger_name: str,
        request: fc__open_20210406_models.UpdateTriggerRequest,
    ) -> fc__open_20210406_models.UpdateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateTriggerHeaders()
        return await self.update_trigger_with_options_async(service_name, function_name, trigger_name, request, headers, runtime)

    def invoke_httptrigger(
        self,
        url: str,
        method: str,
        body: bytes,
        headers: Dict[str, str],
    ) -> Response:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return util_client.invoke_httptrigger(url, method, body, headers)

    async def invoke_httptrigger_async(
        self,
        url: str,
        method: str,
        body: bytes,
        headers: Dict[str, str],
    ) -> Response:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return await util_client.invoke_httptrigger_async(url, method, body, headers)

    def invoke_anonymous_httptrigger(
        self,
        url: str,
        method: str,
        body: bytes,
        headers: Dict[str, str],
    ) -> Response:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return util_client.invoke_anonymous_httptrigger(url, method, body, headers)

    async def invoke_anonymous_httptrigger_async(
        self,
        url: str,
        method: str,
        body: bytes,
        headers: Dict[str, str],
    ) -> Response:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return await util_client.invoke_anonymous_httptrigger_async(url, method, body, headers)

    def send_httprequest_with_authorization(
        self,
        req: Request,
    ) -> Response:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return util_client.send_httprequest_with_authorization(req)

    async def send_httprequest_with_authorization_async(
        self,
        req: Request,
    ) -> Response:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return await util_client.send_httprequest_with_authorization_async(req)

    def send_httprequest(
        self,
        req: Request,
    ) -> Response:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return util_client.send_httprequest(req)

    async def send_httprequest_async(
        self,
        req: Request,
    ) -> Response:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return await util_client.send_httprequest_async(req)

    def sign_request(
        self,
        req: Request,
    ) -> Request:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return util_client.sign_request(req)

    async def sign_request_async(
        self,
        req: Request,
    ) -> Request:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return await util_client.sign_request_async(req)

    def sign_request_with_content_md5(
        self,
        req: Request,
        content_md5: str,
    ) -> Request:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return util_client.sign_request_with_content_md5(req, content_md5)

    async def sign_request_with_content_md5_async(
        self,
        req: Request,
        content_md5: str,
    ) -> Request:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return await util_client.sign_request_with_content_md5_async(req, content_md5)

    def build_httprequest(
        self,
        url: str,
        method: str,
        body: bytes,
        headers: Dict[str, str],
    ) -> Request:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return util_client.build_httprequest(url, method, body, headers)

    async def build_httprequest_async(
        self,
        url: str,
        method: str,
        body: bytes,
        headers: Dict[str, str],
    ) -> Request:
        cred = self._credential
        util_client = FCUtilClient(cred)
        return await util_client.build_httprequest_async(url, method, body, headers)
