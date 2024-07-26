# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_apig20240327 import models as apig20240327_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('apig', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_gateway_security_group_rule_with_options(
        self,
        gateway_id: str,
        request: apig20240327_models.AddGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.AddGatewaySecurityGroupRuleResponse:
        """
        @summary 授权网关访问服务的安全组
        
        @param request: AddGatewaySecurityGroupRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGatewaySecurityGroupRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.port_ranges):
            body['portRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.security_group_id):
            body['securityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGatewaySecurityGroupRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/security-group-rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.AddGatewaySecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_security_group_rule_with_options_async(
        self,
        gateway_id: str,
        request: apig20240327_models.AddGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.AddGatewaySecurityGroupRuleResponse:
        """
        @summary 授权网关访问服务的安全组
        
        @param request: AddGatewaySecurityGroupRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGatewaySecurityGroupRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.port_ranges):
            body['portRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.security_group_id):
            body['securityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGatewaySecurityGroupRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/security-group-rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.AddGatewaySecurityGroupRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway_security_group_rule(
        self,
        gateway_id: str,
        request: apig20240327_models.AddGatewaySecurityGroupRuleRequest,
    ) -> apig20240327_models.AddGatewaySecurityGroupRuleResponse:
        """
        @summary 授权网关访问服务的安全组
        
        @param request: AddGatewaySecurityGroupRuleRequest
        @return: AddGatewaySecurityGroupRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_gateway_security_group_rule_with_options(gateway_id, request, headers, runtime)

    async def add_gateway_security_group_rule_async(
        self,
        gateway_id: str,
        request: apig20240327_models.AddGatewaySecurityGroupRuleRequest,
    ) -> apig20240327_models.AddGatewaySecurityGroupRuleResponse:
        """
        @summary 授权网关访问服务的安全组
        
        @param request: AddGatewaySecurityGroupRuleRequest
        @return: AddGatewaySecurityGroupRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_gateway_security_group_rule_with_options_async(gateway_id, request, headers, runtime)

    def create_domain_with_options(
        self,
        request: apig20240327_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateDomainResponse:
        """
        @summary 创建域名
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_cert_indentifier):
            body['caCertIndentifier'] = request.ca_cert_indentifier
        if not UtilClient.is_unset(request.cert_indentifier):
            body['certIndentifier'] = request.cert_indentifier
        if not UtilClient.is_unset(request.force_https):
            body['forceHttps'] = request.force_https
        if not UtilClient.is_unset(request.http_2option):
            body['http2Option'] = request.http_2option
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not UtilClient.is_unset(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: apig20240327_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateDomainResponse:
        """
        @summary 创建域名
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_cert_indentifier):
            body['caCertIndentifier'] = request.ca_cert_indentifier
        if not UtilClient.is_unset(request.cert_indentifier):
            body['certIndentifier'] = request.cert_indentifier
        if not UtilClient.is_unset(request.force_https):
            body['forceHttps'] = request.force_https
        if not UtilClient.is_unset(request.http_2option):
            body['http2Option'] = request.http_2option
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not UtilClient.is_unset(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: apig20240327_models.CreateDomainRequest,
    ) -> apig20240327_models.CreateDomainResponse:
        """
        @summary 创建域名
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_domain_with_options(request, headers, runtime)

    async def create_domain_async(
        self,
        request: apig20240327_models.CreateDomainRequest,
    ) -> apig20240327_models.CreateDomainResponse:
        """
        @summary 创建域名
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_domain_with_options_async(request, headers, runtime)

    def create_environment_with_options(
        self,
        request: apig20240327_models.CreateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateEnvironmentResponse:
        """
        @summary CreateEnvironment
        
        @param request: CreateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEnvironmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_environment_with_options_async(
        self,
        request: apig20240327_models.CreateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateEnvironmentResponse:
        """
        @summary CreateEnvironment
        
        @param request: CreateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEnvironmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_environment(
        self,
        request: apig20240327_models.CreateEnvironmentRequest,
    ) -> apig20240327_models.CreateEnvironmentResponse:
        """
        @summary CreateEnvironment
        
        @param request: CreateEnvironmentRequest
        @return: CreateEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_with_options(request, headers, runtime)

    async def create_environment_async(
        self,
        request: apig20240327_models.CreateEnvironmentRequest,
    ) -> apig20240327_models.CreateEnvironmentResponse:
        """
        @summary CreateEnvironment
        
        @param request: CreateEnvironmentRequest
        @return: CreateEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_environment_with_options_async(request, headers, runtime)

    def create_gateway_route_with_options(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateGatewayRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param request: CreateGatewayRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_config):
            body['domainConfig'] = request.domain_config
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_route_with_options_async(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateGatewayRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param request: CreateGatewayRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_config):
            body['domainConfig'] = request.domain_config
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_route(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateGatewayRouteRequest,
    ) -> apig20240327_models.CreateGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param request: CreateGatewayRouteRequest
        @return: CreateGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_gateway_route_with_options(gateway_id, request, headers, runtime)

    async def create_gateway_route_async(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateGatewayRouteRequest,
    ) -> apig20240327_models.CreateGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param request: CreateGatewayRouteRequest
        @return: CreateGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_gateway_route_with_options_async(gateway_id, request, headers, runtime)

    def create_gateway_service_with_options(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateGatewayServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateGatewayServiceResponse:
        """
        @summary 创建服务
        
        @param request: CreateGatewayServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_service_configs):
            body['gatewayServiceConfigs'] = request.gateway_service_configs
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewayService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_service_with_options_async(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateGatewayServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateGatewayServiceResponse:
        """
        @summary 创建服务
        
        @param request: CreateGatewayServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_service_configs):
            body['gatewayServiceConfigs'] = request.gateway_service_configs
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewayService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateGatewayServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_service(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateGatewayServiceRequest,
    ) -> apig20240327_models.CreateGatewayServiceResponse:
        """
        @summary 创建服务
        
        @param request: CreateGatewayServiceRequest
        @return: CreateGatewayServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_gateway_service_with_options(gateway_id, request, headers, runtime)

    async def create_gateway_service_async(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateGatewayServiceRequest,
    ) -> apig20240327_models.CreateGatewayServiceResponse:
        """
        @summary 创建服务
        
        @param request: CreateGatewayServiceRequest
        @return: CreateGatewayServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_gateway_service_with_options_async(gateway_id, request, headers, runtime)

    def create_gateway_service_version_with_options(
        self,
        gateway_id: str,
        gateway_service_id: str,
        request: apig20240327_models.CreateGatewayServiceVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateGatewayServiceVersionResponse:
        """
        @summary 创建服务版本
        
        @param request: CreateGatewayServiceVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayServiceVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewayServiceVersion',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}/service-versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateGatewayServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_service_version_with_options_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
        request: apig20240327_models.CreateGatewayServiceVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateGatewayServiceVersionResponse:
        """
        @summary 创建服务版本
        
        @param request: CreateGatewayServiceVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayServiceVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewayServiceVersion',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}/service-versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateGatewayServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_service_version(
        self,
        gateway_id: str,
        gateway_service_id: str,
        request: apig20240327_models.CreateGatewayServiceVersionRequest,
    ) -> apig20240327_models.CreateGatewayServiceVersionResponse:
        """
        @summary 创建服务版本
        
        @param request: CreateGatewayServiceVersionRequest
        @return: CreateGatewayServiceVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_gateway_service_version_with_options(gateway_id, gateway_service_id, request, headers, runtime)

    async def create_gateway_service_version_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
        request: apig20240327_models.CreateGatewayServiceVersionRequest,
    ) -> apig20240327_models.CreateGatewayServiceVersionResponse:
        """
        @summary 创建服务版本
        
        @param request: CreateGatewayServiceVersionRequest
        @return: CreateGatewayServiceVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_gateway_service_version_with_options_async(gateway_id, gateway_service_id, request, headers, runtime)

    def create_http_api_with_options(
        self,
        request: apig20240327_models.CreateHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateHttpApiResponse:
        """
        @summary 创建一个HTTP类型的API
        
        @param request: CreateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocols):
            body['protocols'] = request.protocols
        if not UtilClient.is_unset(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_with_options_async(
        self,
        request: apig20240327_models.CreateHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateHttpApiResponse:
        """
        @summary 创建一个HTTP类型的API
        
        @param request: CreateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocols):
            body['protocols'] = request.protocols
        if not UtilClient.is_unset(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api(
        self,
        request: apig20240327_models.CreateHttpApiRequest,
    ) -> apig20240327_models.CreateHttpApiResponse:
        """
        @summary 创建一个HTTP类型的API
        
        @param request: CreateHttpApiRequest
        @return: CreateHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_http_api_with_options(request, headers, runtime)

    async def create_http_api_async(
        self,
        request: apig20240327_models.CreateHttpApiRequest,
    ) -> apig20240327_models.CreateHttpApiResponse:
        """
        @summary 创建一个HTTP类型的API
        
        @param request: CreateHttpApiRequest
        @return: CreateHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_http_api_with_options_async(request, headers, runtime)

    def create_http_api_operation_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateHttpApiOperationResponse:
        """
        @summary 为HTTP API创建Operation
        
        @param request: CreateHttpApiOperationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiOperationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operations):
            body['operations'] = request.operations
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateHttpApiOperationResponse:
        """
        @summary 为HTTP API创建Operation
        
        @param request: CreateHttpApiOperationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiOperationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operations):
            body['operations'] = request.operations
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api_operation(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiOperationRequest,
    ) -> apig20240327_models.CreateHttpApiOperationResponse:
        """
        @summary 为HTTP API创建Operation
        
        @param request: CreateHttpApiOperationRequest
        @return: CreateHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_http_api_operation_with_options(http_api_id, request, headers, runtime)

    async def create_http_api_operation_async(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiOperationRequest,
    ) -> apig20240327_models.CreateHttpApiOperationResponse:
        """
        @summary 为HTTP API创建Operation
        
        @param request: CreateHttpApiOperationRequest
        @return: CreateHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_http_api_operation_with_options_async(http_api_id, request, headers, runtime)

    def create_service_source_with_options(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateServiceSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateServiceSourceResponse:
        """
        @summary 创建服务来源
        
        @param request: CreateServiceSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_service_source_config):
            body['k8sServiceSourceConfig'] = request.k_8s_service_source_config
        if not UtilClient.is_unset(request.nacos_service_source_config):
            body['nacosServiceSourceConfig'] = request.nacos_service_source_config
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceSource',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/service-sources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_source_with_options_async(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateServiceSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateServiceSourceResponse:
        """
        @summary 创建服务来源
        
        @param request: CreateServiceSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_service_source_config):
            body['k8sServiceSourceConfig'] = request.k_8s_service_source_config
        if not UtilClient.is_unset(request.nacos_service_source_config):
            body['nacosServiceSourceConfig'] = request.nacos_service_source_config
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceSource',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/service-sources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateServiceSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_source(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateServiceSourceRequest,
    ) -> apig20240327_models.CreateServiceSourceResponse:
        """
        @summary 创建服务来源
        
        @param request: CreateServiceSourceRequest
        @return: CreateServiceSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_source_with_options(gateway_id, request, headers, runtime)

    async def create_service_source_async(
        self,
        gateway_id: str,
        request: apig20240327_models.CreateServiceSourceRequest,
    ) -> apig20240327_models.CreateServiceSourceResponse:
        """
        @summary 创建服务来源
        
        @param request: CreateServiceSourceRequest
        @return: CreateServiceSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_source_with_options_async(gateway_id, request, headers, runtime)

    def delete_domain_with_options(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteDomainResponse:
        """
        @summary DeleteDomain
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteDomainResponse:
        """
        @summary DeleteDomain
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        domain_id: str,
    ) -> apig20240327_models.DeleteDomainResponse:
        """
        @summary DeleteDomain
        
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(domain_id, headers, runtime)

    async def delete_domain_async(
        self,
        domain_id: str,
    ) -> apig20240327_models.DeleteDomainResponse:
        """
        @summary DeleteDomain
        
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_domain_with_options_async(domain_id, headers, runtime)

    def delete_environment_with_options(
        self,
        environment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteEnvironmentResponse:
        """
        @summary DeleteEnvironment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEnvironmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_with_options_async(
        self,
        environment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteEnvironmentResponse:
        """
        @summary DeleteEnvironment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEnvironmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment(
        self,
        environment_id: str,
    ) -> apig20240327_models.DeleteEnvironmentResponse:
        """
        @summary DeleteEnvironment
        
        @return: DeleteEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(environment_id, headers, runtime)

    async def delete_environment_async(
        self,
        environment_id: str,
    ) -> apig20240327_models.DeleteEnvironmentResponse:
        """
        @summary DeleteEnvironment
        
        @return: DeleteEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_with_options_async(environment_id, headers, runtime)

    def delete_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewayResponse:
        """
        @summary 删除网关
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewayResponse:
        """
        @summary 删除网关
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway(
        self,
        gateway_id: str,
    ) -> apig20240327_models.DeleteGatewayResponse:
        """
        @summary 删除网关
        
        @return: DeleteGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_gateway_with_options(gateway_id, headers, runtime)

    async def delete_gateway_async(
        self,
        gateway_id: str,
    ) -> apig20240327_models.DeleteGatewayResponse:
        """
        @summary 删除网关
        
        @return: DeleteGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_gateway_with_options_async(gateway_id, headers, runtime)

    def delete_gateway_route_with_options(
        self,
        gateway_id: str,
        gateway_route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes/{OpenApiUtilClient.get_encode_param(gateway_route_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_route_with_options_async(
        self,
        gateway_id: str,
        gateway_route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes/{OpenApiUtilClient.get_encode_param(gateway_route_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_route(
        self,
        gateway_id: str,
        gateway_route_id: str,
    ) -> apig20240327_models.DeleteGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @return: DeleteGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_gateway_route_with_options(gateway_id, gateway_route_id, headers, runtime)

    async def delete_gateway_route_async(
        self,
        gateway_id: str,
        gateway_route_id: str,
    ) -> apig20240327_models.DeleteGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @return: DeleteGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_gateway_route_with_options_async(gateway_id, gateway_route_id, headers, runtime)

    def delete_gateway_service_with_options(
        self,
        gateway_id: str,
        gateway_service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewayServiceResponse:
        """
        @summary 删除服务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGatewayService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_service_with_options_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewayServiceResponse:
        """
        @summary 删除服务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGatewayService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewayServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_service(
        self,
        gateway_id: str,
        gateway_service_id: str,
    ) -> apig20240327_models.DeleteGatewayServiceResponse:
        """
        @summary 删除服务
        
        @return: DeleteGatewayServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_gateway_service_with_options(gateway_id, gateway_service_id, headers, runtime)

    async def delete_gateway_service_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
    ) -> apig20240327_models.DeleteGatewayServiceResponse:
        """
        @summary 删除服务
        
        @return: DeleteGatewayServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_gateway_service_with_options_async(gateway_id, gateway_service_id, headers, runtime)

    def delete_gateway_service_version_with_options(
        self,
        gateway_id: str,
        gateway_service_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewayServiceVersionResponse:
        """
        @summary 删除服务版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayServiceVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGatewayServiceVersion',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}/service-versions/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewayServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_service_version_with_options_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewayServiceVersionResponse:
        """
        @summary 删除服务版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayServiceVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGatewayServiceVersion',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}/service-versions/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewayServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_service_version(
        self,
        gateway_id: str,
        gateway_service_id: str,
        name: str,
    ) -> apig20240327_models.DeleteGatewayServiceVersionResponse:
        """
        @summary 删除服务版本
        
        @return: DeleteGatewayServiceVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_gateway_service_version_with_options(gateway_id, gateway_service_id, name, headers, runtime)

    async def delete_gateway_service_version_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
        name: str,
    ) -> apig20240327_models.DeleteGatewayServiceVersionResponse:
        """
        @summary 删除服务版本
        
        @return: DeleteGatewayServiceVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_gateway_service_version_with_options_async(gateway_id, gateway_service_id, name, headers, runtime)

    def delete_http_api_with_options(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteHttpApiResponse:
        """
        @summary 删除HTTP API
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHttpApiResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_http_api_with_options_async(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteHttpApiResponse:
        """
        @summary 删除HTTP API
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHttpApiResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_http_api(
        self,
        http_api_id: str,
    ) -> apig20240327_models.DeleteHttpApiResponse:
        """
        @summary 删除HTTP API
        
        @return: DeleteHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_http_api_with_options(http_api_id, headers, runtime)

    async def delete_http_api_async(
        self,
        http_api_id: str,
    ) -> apig20240327_models.DeleteHttpApiResponse:
        """
        @summary 删除HTTP API
        
        @return: DeleteHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_http_api_with_options_async(http_api_id, headers, runtime)

    def delete_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteHttpApiOperationResponse:
        """
        @summary 删除Operation
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHttpApiOperationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteHttpApiOperationResponse:
        """
        @summary 删除Operation
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHttpApiOperationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> apig20240327_models.DeleteHttpApiOperationResponse:
        """
        @summary 删除Operation
        
        @return: DeleteHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_http_api_operation_with_options(http_api_id, operation_id, headers, runtime)

    async def delete_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> apig20240327_models.DeleteHttpApiOperationResponse:
        """
        @summary 删除Operation
        
        @return: DeleteHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_http_api_operation_with_options_async(http_api_id, operation_id, headers, runtime)

    def delete_service_source_with_options(
        self,
        gateway_id: str,
        service_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteServiceSourceResponse:
        """
        @summary 删除服务来源
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceSource',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/service-sources/{OpenApiUtilClient.get_encode_param(service_source_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_source_with_options_async(
        self,
        gateway_id: str,
        service_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteServiceSourceResponse:
        """
        @summary 删除服务来源
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceSource',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/service-sources/{OpenApiUtilClient.get_encode_param(service_source_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteServiceSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_source(
        self,
        gateway_id: str,
        service_source_id: str,
    ) -> apig20240327_models.DeleteServiceSourceResponse:
        """
        @summary 删除服务来源
        
        @return: DeleteServiceSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_source_with_options(gateway_id, service_source_id, headers, runtime)

    async def delete_service_source_async(
        self,
        gateway_id: str,
        service_source_id: str,
    ) -> apig20240327_models.DeleteServiceSourceResponse:
        """
        @summary 删除服务来源
        
        @return: DeleteServiceSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_source_with_options_async(gateway_id, service_source_id, headers, runtime)

    def get_domain_with_options(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary 查询域名详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_with_options_async(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary 查询域名详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain(
        self,
        domain_id: str,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary 查询域名详情
        
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(domain_id, headers, runtime)

    async def get_domain_async(
        self,
        domain_id: str,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary 查询域名详情
        
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_domain_with_options_async(domain_id, headers, runtime)

    def get_environment_with_options(
        self,
        environment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @summary GetEnvironment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnvironmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_with_options_async(
        self,
        environment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @summary GetEnvironment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnvironmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_environment(
        self,
        environment_id: str,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @summary GetEnvironment
        
        @return: GetEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(environment_id, headers, runtime)

    async def get_environment_async(
        self,
        environment_id: str,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @summary GetEnvironment
        
        @return: GetEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_with_options_async(environment_id, headers, runtime)

    def get_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetGatewayResponse:
        """
        @summary 获取网关实例详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetGatewayResponse:
        """
        @summary 获取网关实例详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway(
        self,
        gateway_id: str,
    ) -> apig20240327_models.GetGatewayResponse:
        """
        @summary 获取网关实例详情
        
        @return: GetGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gateway_with_options(gateway_id, headers, runtime)

    async def get_gateway_async(
        self,
        gateway_id: str,
    ) -> apig20240327_models.GetGatewayResponse:
        """
        @summary 获取网关实例详情
        
        @return: GetGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_gateway_with_options_async(gateway_id, headers, runtime)

    def get_gateway_route_with_options(
        self,
        gateway_id: str,
        gateway_route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGatewayRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes/{OpenApiUtilClient.get_encode_param(gateway_route_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_route_with_options_async(
        self,
        gateway_id: str,
        gateway_route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGatewayRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes/{OpenApiUtilClient.get_encode_param(gateway_route_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_route(
        self,
        gateway_id: str,
        gateway_route_id: str,
    ) -> apig20240327_models.GetGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @return: GetGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gateway_route_with_options(gateway_id, gateway_route_id, headers, runtime)

    async def get_gateway_route_async(
        self,
        gateway_id: str,
        gateway_route_id: str,
    ) -> apig20240327_models.GetGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @return: GetGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_gateway_route_with_options_async(gateway_id, gateway_route_id, headers, runtime)

    def get_gateway_service_with_options(
        self,
        gateway_id: str,
        gateway_service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetGatewayServiceResponse:
        """
        @summary 查询服务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGatewayServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGatewayService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_service_with_options_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetGatewayServiceResponse:
        """
        @summary 查询服务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGatewayServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGatewayService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetGatewayServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_service(
        self,
        gateway_id: str,
        gateway_service_id: str,
    ) -> apig20240327_models.GetGatewayServiceResponse:
        """
        @summary 查询服务
        
        @return: GetGatewayServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gateway_service_with_options(gateway_id, gateway_service_id, headers, runtime)

    async def get_gateway_service_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
    ) -> apig20240327_models.GetGatewayServiceResponse:
        """
        @summary 查询服务
        
        @return: GetGatewayServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_gateway_service_with_options_async(gateway_id, gateway_service_id, headers, runtime)

    def get_http_api_with_options(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiResponse:
        """
        @summary 读取HttpApi
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_with_options_async(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiResponse:
        """
        @summary 读取HttpApi
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api(
        self,
        http_api_id: str,
    ) -> apig20240327_models.GetHttpApiResponse:
        """
        @summary 读取HttpApi
        
        @return: GetHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_http_api_with_options(http_api_id, headers, runtime)

    async def get_http_api_async(
        self,
        http_api_id: str,
    ) -> apig20240327_models.GetHttpApiResponse:
        """
        @summary 读取HttpApi
        
        @return: GetHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_http_api_with_options_async(http_api_id, headers, runtime)

    def get_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiOperationResponse:
        """
        @summary 读取Operation
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiOperationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiOperationResponse:
        """
        @summary 读取Operation
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiOperationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> apig20240327_models.GetHttpApiOperationResponse:
        """
        @summary 读取Operation
        
        @return: GetHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_http_api_operation_with_options(http_api_id, operation_id, headers, runtime)

    async def get_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> apig20240327_models.GetHttpApiOperationResponse:
        """
        @summary 读取Operation
        
        @return: GetHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_http_api_operation_with_options_async(http_api_id, operation_id, headers, runtime)

    def list_domains_with_options(
        self,
        request: apig20240327_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListDomainsResponse:
        """
        @summary ListDomains
        
        @param request: ListDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: apig20240327_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListDomainsResponse:
        """
        @summary ListDomains
        
        @param request: ListDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: apig20240327_models.ListDomainsRequest,
    ) -> apig20240327_models.ListDomainsResponse:
        """
        @summary ListDomains
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(request, headers, runtime)

    async def list_domains_async(
        self,
        request: apig20240327_models.ListDomainsRequest,
    ) -> apig20240327_models.ListDomainsResponse:
        """
        @summary ListDomains
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_domains_with_options_async(request, headers, runtime)

    def list_environments_with_options(
        self,
        request: apig20240327_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListEnvironmentsResponse:
        """
        @summary ListEnvironments
        
        @param request: ListEnvironmentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnvironmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_like):
            query['aliasLike'] = request.alias_like
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_name_like):
            query['gatewayNameLike'] = request.gateway_name_like
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        request: apig20240327_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListEnvironmentsResponse:
        """
        @summary ListEnvironments
        
        @param request: ListEnvironmentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnvironmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_like):
            query['aliasLike'] = request.alias_like
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_name_like):
            query['gatewayNameLike'] = request.gateway_name_like
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environments(
        self,
        request: apig20240327_models.ListEnvironmentsRequest,
    ) -> apig20240327_models.ListEnvironmentsResponse:
        """
        @summary ListEnvironments
        
        @param request: ListEnvironmentsRequest
        @return: ListEnvironmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(request, headers, runtime)

    async def list_environments_async(
        self,
        request: apig20240327_models.ListEnvironmentsRequest,
    ) -> apig20240327_models.ListEnvironmentsResponse:
        """
        @summary ListEnvironments
        
        @param request: ListEnvironmentsRequest
        @return: ListEnvironmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environments_with_options_async(request, headers, runtime)

    def list_gateway_routes_with_options(
        self,
        gateway_id: str,
        request: apig20240327_models.ListGatewayRoutesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListGatewayRoutesResponse:
        """
        @summary 创建网关路由
        
        @param request: ListGatewayRoutesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewayRoutesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGatewayRoutes',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListGatewayRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_routes_with_options_async(
        self,
        gateway_id: str,
        request: apig20240327_models.ListGatewayRoutesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListGatewayRoutesResponse:
        """
        @summary 创建网关路由
        
        @param request: ListGatewayRoutesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewayRoutesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGatewayRoutes',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListGatewayRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_routes(
        self,
        gateway_id: str,
        request: apig20240327_models.ListGatewayRoutesRequest,
    ) -> apig20240327_models.ListGatewayRoutesResponse:
        """
        @summary 创建网关路由
        
        @param request: ListGatewayRoutesRequest
        @return: ListGatewayRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_gateway_routes_with_options(gateway_id, request, headers, runtime)

    async def list_gateway_routes_async(
        self,
        gateway_id: str,
        request: apig20240327_models.ListGatewayRoutesRequest,
    ) -> apig20240327_models.ListGatewayRoutesResponse:
        """
        @summary 创建网关路由
        
        @param request: ListGatewayRoutesRequest
        @return: ListGatewayRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_gateway_routes_with_options_async(gateway_id, request, headers, runtime)

    def list_gateway_services_with_options(
        self,
        gateway_id: str,
        request: apig20240327_models.ListGatewayServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListGatewayServicesResponse:
        """
        @summary 查询服务列表
        
        @param request: ListGatewayServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewayServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGatewayServices',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListGatewayServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_services_with_options_async(
        self,
        gateway_id: str,
        request: apig20240327_models.ListGatewayServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListGatewayServicesResponse:
        """
        @summary 查询服务列表
        
        @param request: ListGatewayServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewayServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGatewayServices',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListGatewayServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_services(
        self,
        gateway_id: str,
        request: apig20240327_models.ListGatewayServicesRequest,
    ) -> apig20240327_models.ListGatewayServicesResponse:
        """
        @summary 查询服务列表
        
        @param request: ListGatewayServicesRequest
        @return: ListGatewayServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_gateway_services_with_options(gateway_id, request, headers, runtime)

    async def list_gateway_services_async(
        self,
        gateway_id: str,
        request: apig20240327_models.ListGatewayServicesRequest,
    ) -> apig20240327_models.ListGatewayServicesResponse:
        """
        @summary 查询服务列表
        
        @param request: ListGatewayServicesRequest
        @return: ListGatewayServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_gateway_services_with_options_async(gateway_id, request, headers, runtime)

    def list_gateways_with_options(
        self,
        request: apig20240327_models.ListGatewaysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListGatewaysResponse:
        """
        @summary 获取已经创建的云原生网关列表
        
        @param request: ListGatewaysRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewaysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGateways',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateways_with_options_async(
        self,
        request: apig20240327_models.ListGatewaysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListGatewaysResponse:
        """
        @summary 获取已经创建的云原生网关列表
        
        @param request: ListGatewaysRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewaysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGateways',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateways(
        self,
        request: apig20240327_models.ListGatewaysRequest,
    ) -> apig20240327_models.ListGatewaysResponse:
        """
        @summary 获取已经创建的云原生网关列表
        
        @param request: ListGatewaysRequest
        @return: ListGatewaysResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_gateways_with_options(request, headers, runtime)

    async def list_gateways_async(
        self,
        request: apig20240327_models.ListGatewaysRequest,
    ) -> apig20240327_models.ListGatewaysResponse:
        """
        @summary 获取已经创建的云原生网关列表
        
        @param request: ListGatewaysRequest
        @return: ListGatewaysResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_gateways_with_options_async(request, headers, runtime)

    def list_http_api_operations_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiOperationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListHttpApiOperationsResponse:
        """
        @summary 列举Operation
        
        @param request: ListHttpApiOperationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApiOperationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path_like):
            query['pathLike'] = request.path_like
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHttpApiOperations',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListHttpApiOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_http_api_operations_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiOperationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListHttpApiOperationsResponse:
        """
        @summary 列举Operation
        
        @param request: ListHttpApiOperationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApiOperationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path_like):
            query['pathLike'] = request.path_like
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHttpApiOperations',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListHttpApiOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_http_api_operations(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiOperationsRequest,
    ) -> apig20240327_models.ListHttpApiOperationsResponse:
        """
        @summary 列举Operation
        
        @param request: ListHttpApiOperationsRequest
        @return: ListHttpApiOperationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_http_api_operations_with_options(http_api_id, request, headers, runtime)

    async def list_http_api_operations_async(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiOperationsRequest,
    ) -> apig20240327_models.ListHttpApiOperationsResponse:
        """
        @summary 列举Operation
        
        @param request: ListHttpApiOperationsRequest
        @return: ListHttpApiOperationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_http_api_operations_with_options_async(http_api_id, request, headers, runtime)

    def list_http_apis_with_options(
        self,
        request: apig20240327_models.ListHttpApisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListHttpApisResponse:
        """
        @summary 列举HTTP API
        
        @param request: ListHttpApisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.published_only):
            query['publishedOnly'] = request.published_only
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHttpApis',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListHttpApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_http_apis_with_options_async(
        self,
        request: apig20240327_models.ListHttpApisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListHttpApisResponse:
        """
        @summary 列举HTTP API
        
        @param request: ListHttpApisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.published_only):
            query['publishedOnly'] = request.published_only
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHttpApis',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListHttpApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_http_apis(
        self,
        request: apig20240327_models.ListHttpApisRequest,
    ) -> apig20240327_models.ListHttpApisResponse:
        """
        @summary 列举HTTP API
        
        @param request: ListHttpApisRequest
        @return: ListHttpApisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_http_apis_with_options(request, headers, runtime)

    async def list_http_apis_async(
        self,
        request: apig20240327_models.ListHttpApisRequest,
    ) -> apig20240327_models.ListHttpApisResponse:
        """
        @summary 列举HTTP API
        
        @param request: ListHttpApisRequest
        @return: ListHttpApisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_http_apis_with_options_async(request, headers, runtime)

    def offline_gateway_route_with_options(
        self,
        gateway_id: str,
        gateway_route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.OfflineGatewayRouteResponse:
        """
        @summary 发布路由
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineGatewayRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OfflineGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes/{OpenApiUtilClient.get_encode_param(gateway_route_id)}/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.OfflineGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_gateway_route_with_options_async(
        self,
        gateway_id: str,
        gateway_route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.OfflineGatewayRouteResponse:
        """
        @summary 发布路由
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineGatewayRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OfflineGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes/{OpenApiUtilClient.get_encode_param(gateway_route_id)}/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.OfflineGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_gateway_route(
        self,
        gateway_id: str,
        gateway_route_id: str,
    ) -> apig20240327_models.OfflineGatewayRouteResponse:
        """
        @summary 发布路由
        
        @return: OfflineGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_gateway_route_with_options(gateway_id, gateway_route_id, headers, runtime)

    async def offline_gateway_route_async(
        self,
        gateway_id: str,
        gateway_route_id: str,
    ) -> apig20240327_models.OfflineGatewayRouteResponse:
        """
        @summary 发布路由
        
        @return: OfflineGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.offline_gateway_route_with_options_async(gateway_id, gateway_route_id, headers, runtime)

    def offline_http_api_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.OfflineHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.OfflineHttpApiResponse:
        """
        @summary 下线已发布的HTTP API
        
        @param request: OfflineHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.OfflineHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_http_api_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.OfflineHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.OfflineHttpApiResponse:
        """
        @summary 下线已发布的HTTP API
        
        @param request: OfflineHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.OfflineHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_http_api(
        self,
        http_api_id: str,
        request: apig20240327_models.OfflineHttpApiRequest,
    ) -> apig20240327_models.OfflineHttpApiResponse:
        """
        @summary 下线已发布的HTTP API
        
        @param request: OfflineHttpApiRequest
        @return: OfflineHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_http_api_with_options(http_api_id, request, headers, runtime)

    async def offline_http_api_async(
        self,
        http_api_id: str,
        request: apig20240327_models.OfflineHttpApiRequest,
    ) -> apig20240327_models.OfflineHttpApiResponse:
        """
        @summary 下线已发布的HTTP API
        
        @param request: OfflineHttpApiRequest
        @return: OfflineHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.offline_http_api_with_options_async(http_api_id, request, headers, runtime)

    def publish_gateway_route_with_options(
        self,
        gateway_id: str,
        gateway_route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.PublishGatewayRouteResponse:
        """
        @summary 发布路由
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishGatewayRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PublishGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes/{OpenApiUtilClient.get_encode_param(gateway_route_id)}/publish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.PublishGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_gateway_route_with_options_async(
        self,
        gateway_id: str,
        gateway_route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.PublishGatewayRouteResponse:
        """
        @summary 发布路由
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishGatewayRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PublishGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes/{OpenApiUtilClient.get_encode_param(gateway_route_id)}/publish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.PublishGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_gateway_route(
        self,
        gateway_id: str,
        gateway_route_id: str,
    ) -> apig20240327_models.PublishGatewayRouteResponse:
        """
        @summary 发布路由
        
        @return: PublishGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_gateway_route_with_options(gateway_id, gateway_route_id, headers, runtime)

    async def publish_gateway_route_async(
        self,
        gateway_id: str,
        gateway_route_id: str,
    ) -> apig20240327_models.PublishGatewayRouteResponse:
        """
        @summary 发布路由
        
        @return: PublishGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_gateway_route_with_options_async(gateway_id, gateway_route_id, headers, runtime)

    def publish_http_api_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.PublishHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.PublishHttpApiResponse:
        """
        @summary 发布HTTP API
        
        @param request: PublishHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.allow_overwrite):
            body['allowOverwrite'] = request.allow_overwrite
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['environment'] = request.environment
        if not UtilClient.is_unset(request.revision_id):
            body['revisionId'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/publish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.PublishHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_http_api_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.PublishHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.PublishHttpApiResponse:
        """
        @summary 发布HTTP API
        
        @param request: PublishHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.allow_overwrite):
            body['allowOverwrite'] = request.allow_overwrite
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['environment'] = request.environment
        if not UtilClient.is_unset(request.revision_id):
            body['revisionId'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/publish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.PublishHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_http_api(
        self,
        http_api_id: str,
        request: apig20240327_models.PublishHttpApiRequest,
    ) -> apig20240327_models.PublishHttpApiResponse:
        """
        @summary 发布HTTP API
        
        @param request: PublishHttpApiRequest
        @return: PublishHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_http_api_with_options(http_api_id, request, headers, runtime)

    async def publish_http_api_async(
        self,
        http_api_id: str,
        request: apig20240327_models.PublishHttpApiRequest,
    ) -> apig20240327_models.PublishHttpApiResponse:
        """
        @summary 发布HTTP API
        
        @param request: PublishHttpApiRequest
        @return: PublishHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_http_api_with_options_async(http_api_id, request, headers, runtime)

    def update_domain_with_options(
        self,
        domain_id: str,
        request: apig20240327_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateDomainResponse:
        """
        @summary UpdateDomain
        
        @param request: UpdateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_cert_indentifier):
            body['caCertIndentifier'] = request.ca_cert_indentifier
        if not UtilClient.is_unset(request.cert_indentifier):
            body['certIndentifier'] = request.cert_indentifier
        if not UtilClient.is_unset(request.force_https):
            body['forceHttps'] = request.force_https
        if not UtilClient.is_unset(request.http_2option):
            body['http2Option'] = request.http_2option
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not UtilClient.is_unset(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_with_options_async(
        self,
        domain_id: str,
        request: apig20240327_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateDomainResponse:
        """
        @summary UpdateDomain
        
        @param request: UpdateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_cert_indentifier):
            body['caCertIndentifier'] = request.ca_cert_indentifier
        if not UtilClient.is_unset(request.cert_indentifier):
            body['certIndentifier'] = request.cert_indentifier
        if not UtilClient.is_unset(request.force_https):
            body['forceHttps'] = request.force_https
        if not UtilClient.is_unset(request.http_2option):
            body['http2Option'] = request.http_2option
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not UtilClient.is_unset(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain(
        self,
        domain_id: str,
        request: apig20240327_models.UpdateDomainRequest,
    ) -> apig20240327_models.UpdateDomainResponse:
        """
        @summary UpdateDomain
        
        @param request: UpdateDomainRequest
        @return: UpdateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_domain_with_options(domain_id, request, headers, runtime)

    async def update_domain_async(
        self,
        domain_id: str,
        request: apig20240327_models.UpdateDomainRequest,
    ) -> apig20240327_models.UpdateDomainResponse:
        """
        @summary UpdateDomain
        
        @param request: UpdateDomainRequest
        @return: UpdateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_domain_with_options_async(domain_id, request, headers, runtime)

    def update_environment_with_options(
        self,
        environment_id: str,
        request: apig20240327_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateEnvironmentResponse:
        """
        @summary UpdateEnvironment
        
        @param request: UpdateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEnvironmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_environment_with_options_async(
        self,
        environment_id: str,
        request: apig20240327_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateEnvironmentResponse:
        """
        @summary UpdateEnvironment
        
        @param request: UpdateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEnvironmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_environment(
        self,
        environment_id: str,
        request: apig20240327_models.UpdateEnvironmentRequest,
    ) -> apig20240327_models.UpdateEnvironmentResponse:
        """
        @summary UpdateEnvironment
        
        @param request: UpdateEnvironmentRequest
        @return: UpdateEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_with_options(environment_id, request, headers, runtime)

    async def update_environment_async(
        self,
        environment_id: str,
        request: apig20240327_models.UpdateEnvironmentRequest,
    ) -> apig20240327_models.UpdateEnvironmentResponse:
        """
        @summary UpdateEnvironment
        
        @param request: UpdateEnvironmentRequest
        @return: UpdateEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_environment_with_options_async(environment_id, request, headers, runtime)

    def update_gateway_route_with_options(
        self,
        gateway_id: str,
        gateway_route_id: str,
        request: apig20240327_models.UpdateGatewayRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param request: UpdateGatewayRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_config):
            body['domainConfig'] = request.domain_config
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes/{OpenApiUtilClient.get_encode_param(gateway_route_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_route_with_options_async(
        self,
        gateway_id: str,
        gateway_route_id: str,
        request: apig20240327_models.UpdateGatewayRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param request: UpdateGatewayRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_config):
            body['domainConfig'] = request.domain_config
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGatewayRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/http-routes/{OpenApiUtilClient.get_encode_param(gateway_route_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_route(
        self,
        gateway_id: str,
        gateway_route_id: str,
        request: apig20240327_models.UpdateGatewayRouteRequest,
    ) -> apig20240327_models.UpdateGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param request: UpdateGatewayRouteRequest
        @return: UpdateGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_gateway_route_with_options(gateway_id, gateway_route_id, request, headers, runtime)

    async def update_gateway_route_async(
        self,
        gateway_id: str,
        gateway_route_id: str,
        request: apig20240327_models.UpdateGatewayRouteRequest,
    ) -> apig20240327_models.UpdateGatewayRouteResponse:
        """
        @summary 创建网关路由
        
        @param request: UpdateGatewayRouteRequest
        @return: UpdateGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_gateway_route_with_options_async(gateway_id, gateway_route_id, request, headers, runtime)

    def update_gateway_service_with_options(
        self,
        gateway_id: str,
        gateway_service_id: str,
        request: apig20240327_models.UpdateGatewayServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateGatewayServiceResponse:
        """
        @summary 更新服务
        
        @param request: UpdateGatewayServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.addresses):
            body['addresses'] = request.addresses
        if not UtilClient.is_unset(request.port):
            body['port'] = request.port
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGatewayService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_service_with_options_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
        request: apig20240327_models.UpdateGatewayServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateGatewayServiceResponse:
        """
        @summary 更新服务
        
        @param request: UpdateGatewayServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.addresses):
            body['addresses'] = request.addresses
        if not UtilClient.is_unset(request.port):
            body['port'] = request.port
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGatewayService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateGatewayServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_service(
        self,
        gateway_id: str,
        gateway_service_id: str,
        request: apig20240327_models.UpdateGatewayServiceRequest,
    ) -> apig20240327_models.UpdateGatewayServiceResponse:
        """
        @summary 更新服务
        
        @param request: UpdateGatewayServiceRequest
        @return: UpdateGatewayServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_gateway_service_with_options(gateway_id, gateway_service_id, request, headers, runtime)

    async def update_gateway_service_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
        request: apig20240327_models.UpdateGatewayServiceRequest,
    ) -> apig20240327_models.UpdateGatewayServiceResponse:
        """
        @summary 更新服务
        
        @param request: UpdateGatewayServiceRequest
        @return: UpdateGatewayServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_gateway_service_with_options_async(gateway_id, gateway_service_id, request, headers, runtime)

    def update_gateway_service_version_with_options(
        self,
        gateway_id: str,
        gateway_service_id: str,
        name: str,
        request: apig20240327_models.UpdateGatewayServiceVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateGatewayServiceVersionResponse:
        """
        @summary 更新服务版本
        
        @param request: UpdateGatewayServiceVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayServiceVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGatewayServiceVersion',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}/service-versions/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateGatewayServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_service_version_with_options_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
        name: str,
        request: apig20240327_models.UpdateGatewayServiceVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateGatewayServiceVersionResponse:
        """
        @summary 更新服务版本
        
        @param request: UpdateGatewayServiceVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayServiceVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGatewayServiceVersion',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-services/{OpenApiUtilClient.get_encode_param(gateway_service_id)}/service-versions/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateGatewayServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_service_version(
        self,
        gateway_id: str,
        gateway_service_id: str,
        name: str,
        request: apig20240327_models.UpdateGatewayServiceVersionRequest,
    ) -> apig20240327_models.UpdateGatewayServiceVersionResponse:
        """
        @summary 更新服务版本
        
        @param request: UpdateGatewayServiceVersionRequest
        @return: UpdateGatewayServiceVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_gateway_service_version_with_options(gateway_id, gateway_service_id, name, request, headers, runtime)

    async def update_gateway_service_version_async(
        self,
        gateway_id: str,
        gateway_service_id: str,
        name: str,
        request: apig20240327_models.UpdateGatewayServiceVersionRequest,
    ) -> apig20240327_models.UpdateGatewayServiceVersionResponse:
        """
        @summary 更新服务版本
        
        @param request: UpdateGatewayServiceVersionRequest
        @return: UpdateGatewayServiceVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_gateway_service_version_with_options_async(gateway_id, gateway_service_id, name, request, headers, runtime)

    def update_http_api_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.UpdateHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateHttpApiResponse:
        """
        @summary 更新HTTP API
        
        @param request: UpdateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.protocols):
            body['protocols'] = request.protocols
        if not UtilClient.is_unset(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_http_api_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.UpdateHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateHttpApiResponse:
        """
        @summary 更新HTTP API
        
        @param request: UpdateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.protocols):
            body['protocols'] = request.protocols
        if not UtilClient.is_unset(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_http_api(
        self,
        http_api_id: str,
        request: apig20240327_models.UpdateHttpApiRequest,
    ) -> apig20240327_models.UpdateHttpApiResponse:
        """
        @summary 更新HTTP API
        
        @param request: UpdateHttpApiRequest
        @return: UpdateHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_http_api_with_options(http_api_id, request, headers, runtime)

    async def update_http_api_async(
        self,
        http_api_id: str,
        request: apig20240327_models.UpdateHttpApiRequest,
    ) -> apig20240327_models.UpdateHttpApiResponse:
        """
        @summary 更新HTTP API
        
        @param request: UpdateHttpApiRequest
        @return: UpdateHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_http_api_with_options_async(http_api_id, request, headers, runtime)

    def update_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        request: apig20240327_models.UpdateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateHttpApiOperationResponse:
        """
        @summary 更新Operation
        
        @param request: UpdateHttpApiOperationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiOperationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['operation'] = request.operation
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        request: apig20240327_models.UpdateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateHttpApiOperationResponse:
        """
        @summary 更新Operation
        
        @param request: UpdateHttpApiOperationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiOperationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['operation'] = request.operation
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
        request: apig20240327_models.UpdateHttpApiOperationRequest,
    ) -> apig20240327_models.UpdateHttpApiOperationResponse:
        """
        @summary 更新Operation
        
        @param request: UpdateHttpApiOperationRequest
        @return: UpdateHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_http_api_operation_with_options(http_api_id, operation_id, request, headers, runtime)

    async def update_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
        request: apig20240327_models.UpdateHttpApiOperationRequest,
    ) -> apig20240327_models.UpdateHttpApiOperationResponse:
        """
        @summary 更新Operation
        
        @param request: UpdateHttpApiOperationRequest
        @return: UpdateHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_http_api_operation_with_options_async(http_api_id, operation_id, request, headers, runtime)

    def update_service_source_with_options(
        self,
        gateway_id: str,
        service_source_id: str,
        request: apig20240327_models.UpdateServiceSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateServiceSourceResponse:
        """
        @summary 更新服务来源
        
        @param request: UpdateServiceSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_service_source_config):
            body['k8sServiceSourceConfig'] = request.k_8s_service_source_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceSource',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/service-sources/{OpenApiUtilClient.get_encode_param(service_source_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_source_with_options_async(
        self,
        gateway_id: str,
        service_source_id: str,
        request: apig20240327_models.UpdateServiceSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateServiceSourceResponse:
        """
        @summary 更新服务来源
        
        @param request: UpdateServiceSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_service_source_config):
            body['k8sServiceSourceConfig'] = request.k_8s_service_source_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceSource',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/service-sources/{OpenApiUtilClient.get_encode_param(service_source_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateServiceSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_source(
        self,
        gateway_id: str,
        service_source_id: str,
        request: apig20240327_models.UpdateServiceSourceRequest,
    ) -> apig20240327_models.UpdateServiceSourceResponse:
        """
        @summary 更新服务来源
        
        @param request: UpdateServiceSourceRequest
        @return: UpdateServiceSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_source_with_options(gateway_id, service_source_id, request, headers, runtime)

    async def update_service_source_async(
        self,
        gateway_id: str,
        service_source_id: str,
        request: apig20240327_models.UpdateServiceSourceRequest,
    ) -> apig20240327_models.UpdateServiceSourceResponse:
        """
        @summary 更新服务来源
        
        @param request: UpdateServiceSourceRequest
        @return: UpdateServiceSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_source_with_options_async(gateway_id, service_source_id, request, headers, runtime)
