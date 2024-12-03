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
        @summary Authorize the security group for gateway to access services
        
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
        @summary Authorize the security group for gateway to access services
        
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
        @summary Authorize the security group for gateway to access services
        
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
        @summary Authorize the security group for gateway to access services
        
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
        @summary Create Domain
        
        @description Create Domain.
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not UtilClient.is_unset(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.force_https):
            body['forceHttps'] = request.force_https
        if not UtilClient.is_unset(request.http_2option):
            body['http2Option'] = request.http_2option
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
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
        @summary Create Domain
        
        @description Create Domain.
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not UtilClient.is_unset(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.force_https):
            body['forceHttps'] = request.force_https
        if not UtilClient.is_unset(request.http_2option):
            body['http2Option'] = request.http_2option
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
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
        @summary Create Domain
        
        @description Create Domain.
        
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
        @summary Create Domain
        
        @description Create Domain.
        
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
        
        @description Create environment.
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
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
        
        @description Create environment.
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
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
        
        @description Create environment.
        
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
        
        @description Create environment.
        
        @param request: CreateEnvironmentRequest
        @return: CreateEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_environment_with_options_async(request, headers, runtime)

    def create_http_api_with_options(
        self,
        request: apig20240327_models.CreateHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateHttpApiResponse:
        """
        @summary Create an API of HTTP type
        
        @param request: CreateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocols):
            body['protocols'] = request.protocols
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
        @summary Create an API of HTTP type
        
        @param request: CreateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocols):
            body['protocols'] = request.protocols
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
        @summary Create an API of HTTP type
        
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
        @summary Create an API of HTTP type
        
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
        @summary Create an Operation for HTTP API
        
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
        @summary Create an Operation for HTTP API
        
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
        @summary Create an Operation for HTTP API
        
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
        @summary Create an Operation for HTTP API
        
        @param request: CreateHttpApiOperationRequest
        @return: CreateHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_http_api_operation_with_options_async(http_api_id, request, headers, runtime)

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
        @summary Delete Gateway
        
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
        @summary Delete Gateway
        
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
        @summary Delete Gateway
        
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
        @summary Delete Gateway
        
        @return: DeleteGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_gateway_with_options_async(gateway_id, headers, runtime)

    def delete_http_api_with_options(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteHttpApiResponse:
        """
        @summary Delete HTTP API
        
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
        @summary Delete HTTP API
        
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
        @summary Delete HTTP API
        
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
        @summary Delete HTTP API
        
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
        @summary Delete Operation
        
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
        @summary Delete Operation
        
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
        @summary Delete Operation
        
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
        @summary Delete Operation
        
        @return: DeleteHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_http_api_operation_with_options_async(http_api_id, operation_id, headers, runtime)

    def get_domain_with_options(
        self,
        domain_id: str,
        request: apig20240327_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary Query domain details
        
        @param request: GetDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
        request: apig20240327_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary Query domain details
        
        @param request: GetDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
        request: apig20240327_models.GetDomainRequest,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary Query domain details
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(domain_id, request, headers, runtime)

    async def get_domain_async(
        self,
        domain_id: str,
        request: apig20240327_models.GetDomainRequest,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary Query domain details
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_domain_with_options_async(domain_id, request, headers, runtime)

    def get_environment_with_options(
        self,
        environment_id: str,
        request: apig20240327_models.GetEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @summary GetEnvironment
        
        @param request: GetEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnvironmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        if not UtilClient.is_unset(request.with_vpc_info):
            query['withVpcInfo'] = request.with_vpc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
        request: apig20240327_models.GetEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @summary GetEnvironment
        
        @param request: GetEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnvironmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        if not UtilClient.is_unset(request.with_vpc_info):
            query['withVpcInfo'] = request.with_vpc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
        request: apig20240327_models.GetEnvironmentRequest,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @summary GetEnvironment
        
        @param request: GetEnvironmentRequest
        @return: GetEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(environment_id, request, headers, runtime)

    async def get_environment_async(
        self,
        environment_id: str,
        request: apig20240327_models.GetEnvironmentRequest,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @summary GetEnvironment
        
        @param request: GetEnvironmentRequest
        @return: GetEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_with_options_async(environment_id, request, headers, runtime)

    def get_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetGatewayResponse:
        """
        @summary Get a gateway.
        
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
        @summary Get a gateway.
        
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
        @summary Get a gateway.
        
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
        @summary Get a gateway.
        
        @return: GetGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_gateway_with_options_async(gateway_id, headers, runtime)

    def get_http_api_with_options(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiResponse:
        """
        @summary Read HttpApi
        
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
        @summary Read HttpApi
        
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
        @summary Read HttpApi
        
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
        @summary Read HttpApi
        
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
        @summary Get Operation
        
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
        @summary Get Operation
        
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
        @summary Get Operation
        
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
        @summary Get Operation
        
        @return: GetHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_http_api_operation_with_options_async(http_api_id, operation_id, headers, runtime)

    def get_http_api_route_with_options(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiRouteResponse:
        """
        @summary 获取HttpApi的路由详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApiRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes/{OpenApiUtilClient.get_encode_param(route_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_route_with_options_async(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiRouteResponse:
        """
        @summary 获取HttpApi的路由详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApiRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes/{OpenApiUtilClient.get_encode_param(route_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api_route(
        self,
        http_api_id: str,
        route_id: str,
    ) -> apig20240327_models.GetHttpApiRouteResponse:
        """
        @summary 获取HttpApi的路由详情
        
        @return: GetHttpApiRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_http_api_route_with_options(http_api_id, route_id, headers, runtime)

    async def get_http_api_route_async(
        self,
        http_api_id: str,
        route_id: str,
    ) -> apig20240327_models.GetHttpApiRouteResponse:
        """
        @summary 获取HttpApi的路由详情
        
        @return: GetHttpApiRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_http_api_route_with_options_async(http_api_id, route_id, headers, runtime)

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
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
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
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
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

    def list_gateways_with_options(
        self,
        tmp_req: apig20240327_models.ListGatewaysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListGatewaysResponse:
        """
        @summary Retrieve the list of created cloud-native gateways
        
        @param tmp_req: ListGatewaysRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewaysResponse
        """
        UtilClient.validate_model(tmp_req)
        request = apig20240327_models.ListGatewaysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
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
        tmp_req: apig20240327_models.ListGatewaysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListGatewaysResponse:
        """
        @summary Retrieve the list of created cloud-native gateways
        
        @param tmp_req: ListGatewaysRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewaysResponse
        """
        UtilClient.validate_model(tmp_req)
        request = apig20240327_models.ListGatewaysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
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
        @summary Retrieve the list of created cloud-native gateways
        
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
        @summary Retrieve the list of created cloud-native gateways
        
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
        @summary List Operations
        
        @param request: ListHttpApiOperationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApiOperationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path_like):
            query['pathLike'] = request.path_like
        if not UtilClient.is_unset(request.with_consumer_in_environment_id):
            query['withConsumerInEnvironmentId'] = request.with_consumer_in_environment_id
        if not UtilClient.is_unset(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not UtilClient.is_unset(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
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
        @summary List Operations
        
        @param request: ListHttpApiOperationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApiOperationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path_like):
            query['pathLike'] = request.path_like
        if not UtilClient.is_unset(request.with_consumer_in_environment_id):
            query['withConsumerInEnvironmentId'] = request.with_consumer_in_environment_id
        if not UtilClient.is_unset(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not UtilClient.is_unset(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
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
        @summary List Operations
        
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
        @summary List Operations
        
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
        @summary List HTTP APIs
        
        @param request: ListHttpApisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApisResponse
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        if not UtilClient.is_unset(request.with_auth_policy_in_environment_id):
            query['withAuthPolicyInEnvironmentId'] = request.with_auth_policy_in_environment_id
        if not UtilClient.is_unset(request.with_auth_policy_list):
            query['withAuthPolicyList'] = request.with_auth_policy_list
        if not UtilClient.is_unset(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not UtilClient.is_unset(request.with_environment_info):
            query['withEnvironmentInfo'] = request.with_environment_info
        if not UtilClient.is_unset(request.with_environment_info_by_id):
            query['withEnvironmentInfoById'] = request.with_environment_info_by_id
        if not UtilClient.is_unset(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
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
        @summary List HTTP APIs
        
        @param request: ListHttpApisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApisResponse
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        if not UtilClient.is_unset(request.with_auth_policy_in_environment_id):
            query['withAuthPolicyInEnvironmentId'] = request.with_auth_policy_in_environment_id
        if not UtilClient.is_unset(request.with_auth_policy_list):
            query['withAuthPolicyList'] = request.with_auth_policy_list
        if not UtilClient.is_unset(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not UtilClient.is_unset(request.with_environment_info):
            query['withEnvironmentInfo'] = request.with_environment_info
        if not UtilClient.is_unset(request.with_environment_info_by_id):
            query['withEnvironmentInfoById'] = request.with_environment_info_by_id
        if not UtilClient.is_unset(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
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
        @summary List HTTP APIs
        
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
        @summary List HTTP APIs
        
        @param request: ListHttpApisRequest
        @return: ListHttpApisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_http_apis_with_options_async(request, headers, runtime)

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
        if not UtilClient.is_unset(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
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
        if not UtilClient.is_unset(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
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

    def update_http_api_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.UpdateHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateHttpApiResponse:
        """
        @summary Update HTTP API
        
        @param request: UpdateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
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
        @summary Update HTTP API
        
        @param request: UpdateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
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
        @summary Update HTTP API
        
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
        @summary Update HTTP API
        
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
        @summary Update Operation
        
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
        @summary Update Operation
        
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
        @summary Update Operation
        
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
        @summary Update Operation
        
        @param request: UpdateHttpApiOperationRequest
        @return: UpdateHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_http_api_operation_with_options_async(http_api_id, operation_id, request, headers, runtime)
