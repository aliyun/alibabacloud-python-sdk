# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pvtz20180101 import models as pvtz_20180101_models
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
        self._endpoint = self.get_endpoint('pvtz', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_custom_line_with_options(
        self,
        request: pvtz_20180101_models.AddCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddCustomLineResponse:
        """
        @param request: AddCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_category):
            query['DnsCategory'] = request.dns_category
        if not UtilClient.is_unset(request.ipv_4s):
            query['Ipv4s'] = request.ipv_4s
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.share_scope):
            query['ShareScope'] = request.share_scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCustomLine',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_line_with_options_async(
        self,
        request: pvtz_20180101_models.AddCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddCustomLineResponse:
        """
        @param request: AddCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_category):
            query['DnsCategory'] = request.dns_category
        if not UtilClient.is_unset(request.ipv_4s):
            query['Ipv4s'] = request.ipv_4s
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.share_scope):
            query['ShareScope'] = request.share_scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCustomLine',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_line(
        self,
        request: pvtz_20180101_models.AddCustomLineRequest,
    ) -> pvtz_20180101_models.AddCustomLineResponse:
        """
        @param request: AddCustomLineRequest
        @return: AddCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_custom_line_with_options(request, runtime)

    async def add_custom_line_async(
        self,
        request: pvtz_20180101_models.AddCustomLineRequest,
    ) -> pvtz_20180101_models.AddCustomLineResponse:
        """
        @param request: AddCustomLineRequest
        @return: AddCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_custom_line_with_options_async(request, runtime)

    def add_resolver_endpoint_with_options(
        self,
        request: pvtz_20180101_models.AddResolverEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddResolverEndpointResponse:
        """
        @summary Creates an endpoint.
        
        @param request: AddResolverEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddResolverEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_config):
            query['IpConfig'] = request.ip_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddResolverEndpoint',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddResolverEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_resolver_endpoint_with_options_async(
        self,
        request: pvtz_20180101_models.AddResolverEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddResolverEndpointResponse:
        """
        @summary Creates an endpoint.
        
        @param request: AddResolverEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddResolverEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_config):
            query['IpConfig'] = request.ip_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddResolverEndpoint',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddResolverEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_resolver_endpoint(
        self,
        request: pvtz_20180101_models.AddResolverEndpointRequest,
    ) -> pvtz_20180101_models.AddResolverEndpointResponse:
        """
        @summary Creates an endpoint.
        
        @param request: AddResolverEndpointRequest
        @return: AddResolverEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_resolver_endpoint_with_options(request, runtime)

    async def add_resolver_endpoint_async(
        self,
        request: pvtz_20180101_models.AddResolverEndpointRequest,
    ) -> pvtz_20180101_models.AddResolverEndpointResponse:
        """
        @summary Creates an endpoint.
        
        @param request: AddResolverEndpointRequest
        @return: AddResolverEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_resolver_endpoint_with_options_async(request, runtime)

    def add_resolver_rule_with_options(
        self,
        request: pvtz_20180101_models.AddResolverRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddResolverRuleResponse:
        """
        @summary Creates a forwarding rule.
        
        @param request: AddResolverRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddResolverRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.forward_ip):
            query['ForwardIp'] = request.forward_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddResolverRule',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddResolverRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_resolver_rule_with_options_async(
        self,
        request: pvtz_20180101_models.AddResolverRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddResolverRuleResponse:
        """
        @summary Creates a forwarding rule.
        
        @param request: AddResolverRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddResolverRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.forward_ip):
            query['ForwardIp'] = request.forward_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddResolverRule',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddResolverRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_resolver_rule(
        self,
        request: pvtz_20180101_models.AddResolverRuleRequest,
    ) -> pvtz_20180101_models.AddResolverRuleResponse:
        """
        @summary Creates a forwarding rule.
        
        @param request: AddResolverRuleRequest
        @return: AddResolverRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_resolver_rule_with_options(request, runtime)

    async def add_resolver_rule_async(
        self,
        request: pvtz_20180101_models.AddResolverRuleRequest,
    ) -> pvtz_20180101_models.AddResolverRuleResponse:
        """
        @summary Creates a forwarding rule.
        
        @param request: AddResolverRuleRequest
        @return: AddResolverRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_resolver_rule_with_options_async(request, runtime)

    def add_user_vpc_authorization_with_options(
        self,
        request: pvtz_20180101_models.AddUserVpcAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddUserVpcAuthorizationResponse:
        """
        @summary Adds another account to associate one or more virtual private clouds (VPCs) of the current account with a private zone.
        
        @param request: AddUserVpcAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserVpcAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_channel):
            query['AuthChannel'] = request.auth_channel
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserVpcAuthorization',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddUserVpcAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_vpc_authorization_with_options_async(
        self,
        request: pvtz_20180101_models.AddUserVpcAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddUserVpcAuthorizationResponse:
        """
        @summary Adds another account to associate one or more virtual private clouds (VPCs) of the current account with a private zone.
        
        @param request: AddUserVpcAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserVpcAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_channel):
            query['AuthChannel'] = request.auth_channel
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserVpcAuthorization',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddUserVpcAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_vpc_authorization(
        self,
        request: pvtz_20180101_models.AddUserVpcAuthorizationRequest,
    ) -> pvtz_20180101_models.AddUserVpcAuthorizationResponse:
        """
        @summary Adds another account to associate one or more virtual private clouds (VPCs) of the current account with a private zone.
        
        @param request: AddUserVpcAuthorizationRequest
        @return: AddUserVpcAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_vpc_authorization_with_options(request, runtime)

    async def add_user_vpc_authorization_async(
        self,
        request: pvtz_20180101_models.AddUserVpcAuthorizationRequest,
    ) -> pvtz_20180101_models.AddUserVpcAuthorizationResponse:
        """
        @summary Adds another account to associate one or more virtual private clouds (VPCs) of the current account with a private zone.
        
        @param request: AddUserVpcAuthorizationRequest
        @return: AddUserVpcAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_vpc_authorization_with_options_async(request, runtime)

    def add_zone_with_options(
        self,
        request: pvtz_20180101_models.AddZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddZoneResponse:
        """
        @summary Creates a zone.
        
        @param request: AddZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dns_group):
            query['DnsGroup'] = request.dns_group
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zone_name):
            query['ZoneName'] = request.zone_name
        if not UtilClient.is_unset(request.zone_tag):
            query['ZoneTag'] = request.zone_tag
        if not UtilClient.is_unset(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddZone',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_zone_with_options_async(
        self,
        request: pvtz_20180101_models.AddZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddZoneResponse:
        """
        @summary Creates a zone.
        
        @param request: AddZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dns_group):
            query['DnsGroup'] = request.dns_group
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zone_name):
            query['ZoneName'] = request.zone_name
        if not UtilClient.is_unset(request.zone_tag):
            query['ZoneTag'] = request.zone_tag
        if not UtilClient.is_unset(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddZone',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_zone(
        self,
        request: pvtz_20180101_models.AddZoneRequest,
    ) -> pvtz_20180101_models.AddZoneResponse:
        """
        @summary Creates a zone.
        
        @param request: AddZoneRequest
        @return: AddZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_zone_with_options(request, runtime)

    async def add_zone_async(
        self,
        request: pvtz_20180101_models.AddZoneRequest,
    ) -> pvtz_20180101_models.AddZoneResponse:
        """
        @summary Creates a zone.
        
        @param request: AddZoneRequest
        @return: AddZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_zone_with_options_async(request, runtime)

    def add_zone_record_with_options(
        self,
        request: pvtz_20180101_models.AddZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddZoneRecordResponse:
        """
        @summary Adds a Domain Name System (DNS) record for a zone.
        
        @param request: AddZoneRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddZoneRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rr):
            query['Rr'] = request.rr
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddZoneRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_zone_record_with_options_async(
        self,
        request: pvtz_20180101_models.AddZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddZoneRecordResponse:
        """
        @summary Adds a Domain Name System (DNS) record for a zone.
        
        @param request: AddZoneRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddZoneRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rr):
            query['Rr'] = request.rr
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddZoneRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_zone_record(
        self,
        request: pvtz_20180101_models.AddZoneRecordRequest,
    ) -> pvtz_20180101_models.AddZoneRecordResponse:
        """
        @summary Adds a Domain Name System (DNS) record for a zone.
        
        @param request: AddZoneRecordRequest
        @return: AddZoneRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_zone_record_with_options(request, runtime)

    async def add_zone_record_async(
        self,
        request: pvtz_20180101_models.AddZoneRecordRequest,
    ) -> pvtz_20180101_models.AddZoneRecordResponse:
        """
        @summary Adds a Domain Name System (DNS) record for a zone.
        
        @param request: AddZoneRecordRequest
        @return: AddZoneRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_zone_record_with_options_async(request, runtime)

    def bind_resolver_rule_vpc_with_options(
        self,
        request: pvtz_20180101_models.BindResolverRuleVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.BindResolverRuleVpcResponse:
        """
        @summary Associates a forwarding rule with virtual private clouds (VPCs).
        
        @param request: BindResolverRuleVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindResolverRuleVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.vpc):
            query['Vpc'] = request.vpc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindResolverRuleVpc',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.BindResolverRuleVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_resolver_rule_vpc_with_options_async(
        self,
        request: pvtz_20180101_models.BindResolverRuleVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.BindResolverRuleVpcResponse:
        """
        @summary Associates a forwarding rule with virtual private clouds (VPCs).
        
        @param request: BindResolverRuleVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindResolverRuleVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.vpc):
            query['Vpc'] = request.vpc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindResolverRuleVpc',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.BindResolverRuleVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_resolver_rule_vpc(
        self,
        request: pvtz_20180101_models.BindResolverRuleVpcRequest,
    ) -> pvtz_20180101_models.BindResolverRuleVpcResponse:
        """
        @summary Associates a forwarding rule with virtual private clouds (VPCs).
        
        @param request: BindResolverRuleVpcRequest
        @return: BindResolverRuleVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_resolver_rule_vpc_with_options(request, runtime)

    async def bind_resolver_rule_vpc_async(
        self,
        request: pvtz_20180101_models.BindResolverRuleVpcRequest,
    ) -> pvtz_20180101_models.BindResolverRuleVpcResponse:
        """
        @summary Associates a forwarding rule with virtual private clouds (VPCs).
        
        @param request: BindResolverRuleVpcRequest
        @return: BindResolverRuleVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_resolver_rule_vpc_with_options_async(request, runtime)

    def bind_zone_vpc_with_options(
        self,
        request: pvtz_20180101_models.BindZoneVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.BindZoneVpcResponse:
        """
        @summary Binds a zone to virtual private clouds (VPCs) or unbinds a zone from VPCs.
        
        @param request: BindZoneVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindZoneVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.vpcs):
            query['Vpcs'] = request.vpcs
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindZoneVpc',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.BindZoneVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_zone_vpc_with_options_async(
        self,
        request: pvtz_20180101_models.BindZoneVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.BindZoneVpcResponse:
        """
        @summary Binds a zone to virtual private clouds (VPCs) or unbinds a zone from VPCs.
        
        @param request: BindZoneVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindZoneVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.vpcs):
            query['Vpcs'] = request.vpcs
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindZoneVpc',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.BindZoneVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_zone_vpc(
        self,
        request: pvtz_20180101_models.BindZoneVpcRequest,
    ) -> pvtz_20180101_models.BindZoneVpcResponse:
        """
        @summary Binds a zone to virtual private clouds (VPCs) or unbinds a zone from VPCs.
        
        @param request: BindZoneVpcRequest
        @return: BindZoneVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_zone_vpc_with_options(request, runtime)

    async def bind_zone_vpc_async(
        self,
        request: pvtz_20180101_models.BindZoneVpcRequest,
    ) -> pvtz_20180101_models.BindZoneVpcResponse:
        """
        @summary Binds a zone to virtual private clouds (VPCs) or unbinds a zone from VPCs.
        
        @param request: BindZoneVpcRequest
        @return: BindZoneVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_zone_vpc_with_options_async(request, runtime)

    def change_zone_dns_group_with_options(
        self,
        request: pvtz_20180101_models.ChangeZoneDnsGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.ChangeZoneDnsGroupResponse:
        """
        @param request: ChangeZoneDnsGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeZoneDnsGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dns_group):
            query['DnsGroup'] = request.dns_group
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeZoneDnsGroup',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.ChangeZoneDnsGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_zone_dns_group_with_options_async(
        self,
        request: pvtz_20180101_models.ChangeZoneDnsGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.ChangeZoneDnsGroupResponse:
        """
        @param request: ChangeZoneDnsGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeZoneDnsGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dns_group):
            query['DnsGroup'] = request.dns_group
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeZoneDnsGroup',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.ChangeZoneDnsGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_zone_dns_group(
        self,
        request: pvtz_20180101_models.ChangeZoneDnsGroupRequest,
    ) -> pvtz_20180101_models.ChangeZoneDnsGroupResponse:
        """
        @param request: ChangeZoneDnsGroupRequest
        @return: ChangeZoneDnsGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_zone_dns_group_with_options(request, runtime)

    async def change_zone_dns_group_async(
        self,
        request: pvtz_20180101_models.ChangeZoneDnsGroupRequest,
    ) -> pvtz_20180101_models.ChangeZoneDnsGroupResponse:
        """
        @param request: ChangeZoneDnsGroupRequest
        @return: ChangeZoneDnsGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_zone_dns_group_with_options_async(request, runtime)

    def check_zone_name_with_options(
        self,
        request: pvtz_20180101_models.CheckZoneNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.CheckZoneNameResponse:
        """
        @summary Checks whether the name of a zone is valid based on specific rules.
        
        @param request: CheckZoneNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckZoneNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckZoneName',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.CheckZoneNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_zone_name_with_options_async(
        self,
        request: pvtz_20180101_models.CheckZoneNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.CheckZoneNameResponse:
        """
        @summary Checks whether the name of a zone is valid based on specific rules.
        
        @param request: CheckZoneNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckZoneNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckZoneName',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.CheckZoneNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_zone_name(
        self,
        request: pvtz_20180101_models.CheckZoneNameRequest,
    ) -> pvtz_20180101_models.CheckZoneNameResponse:
        """
        @summary Checks whether the name of a zone is valid based on specific rules.
        
        @param request: CheckZoneNameRequest
        @return: CheckZoneNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_zone_name_with_options(request, runtime)

    async def check_zone_name_async(
        self,
        request: pvtz_20180101_models.CheckZoneNameRequest,
    ) -> pvtz_20180101_models.CheckZoneNameResponse:
        """
        @summary Checks whether the name of a zone is valid based on specific rules.
        
        @param request: CheckZoneNameRequest
        @return: CheckZoneNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_zone_name_with_options_async(request, runtime)

    def delete_custom_line_with_options(
        self,
        request: pvtz_20180101_models.DeleteCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteCustomLineResponse:
        """
        @param request: DeleteCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomLine',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_line_with_options_async(
        self,
        request: pvtz_20180101_models.DeleteCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteCustomLineResponse:
        """
        @param request: DeleteCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomLine',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_line(
        self,
        request: pvtz_20180101_models.DeleteCustomLineRequest,
    ) -> pvtz_20180101_models.DeleteCustomLineResponse:
        """
        @param request: DeleteCustomLineRequest
        @return: DeleteCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_line_with_options(request, runtime)

    async def delete_custom_line_async(
        self,
        request: pvtz_20180101_models.DeleteCustomLineRequest,
    ) -> pvtz_20180101_models.DeleteCustomLineResponse:
        """
        @param request: DeleteCustomLineRequest
        @return: DeleteCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_line_with_options_async(request, runtime)

    def delete_resolver_endpoint_with_options(
        self,
        request: pvtz_20180101_models.DeleteResolverEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteResolverEndpointResponse:
        """
        @summary Deletes an endpoint.
        
        @param request: DeleteResolverEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResolverEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResolverEndpoint',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteResolverEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resolver_endpoint_with_options_async(
        self,
        request: pvtz_20180101_models.DeleteResolverEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteResolverEndpointResponse:
        """
        @summary Deletes an endpoint.
        
        @param request: DeleteResolverEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResolverEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResolverEndpoint',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteResolverEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resolver_endpoint(
        self,
        request: pvtz_20180101_models.DeleteResolverEndpointRequest,
    ) -> pvtz_20180101_models.DeleteResolverEndpointResponse:
        """
        @summary Deletes an endpoint.
        
        @param request: DeleteResolverEndpointRequest
        @return: DeleteResolverEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_resolver_endpoint_with_options(request, runtime)

    async def delete_resolver_endpoint_async(
        self,
        request: pvtz_20180101_models.DeleteResolverEndpointRequest,
    ) -> pvtz_20180101_models.DeleteResolverEndpointResponse:
        """
        @summary Deletes an endpoint.
        
        @param request: DeleteResolverEndpointRequest
        @return: DeleteResolverEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_resolver_endpoint_with_options_async(request, runtime)

    def delete_resolver_rule_with_options(
        self,
        request: pvtz_20180101_models.DeleteResolverRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteResolverRuleResponse:
        """
        @summary Deletes a forwarding rule.
        
        @param request: DeleteResolverRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResolverRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResolverRule',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteResolverRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resolver_rule_with_options_async(
        self,
        request: pvtz_20180101_models.DeleteResolverRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteResolverRuleResponse:
        """
        @summary Deletes a forwarding rule.
        
        @param request: DeleteResolverRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResolverRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResolverRule',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteResolverRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resolver_rule(
        self,
        request: pvtz_20180101_models.DeleteResolverRuleRequest,
    ) -> pvtz_20180101_models.DeleteResolverRuleResponse:
        """
        @summary Deletes a forwarding rule.
        
        @param request: DeleteResolverRuleRequest
        @return: DeleteResolverRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_resolver_rule_with_options(request, runtime)

    async def delete_resolver_rule_async(
        self,
        request: pvtz_20180101_models.DeleteResolverRuleRequest,
    ) -> pvtz_20180101_models.DeleteResolverRuleResponse:
        """
        @summary Deletes a forwarding rule.
        
        @param request: DeleteResolverRuleRequest
        @return: DeleteResolverRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_resolver_rule_with_options_async(request, runtime)

    def delete_user_vpc_authorization_with_options(
        self,
        request: pvtz_20180101_models.DeleteUserVpcAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteUserVpcAuthorizationResponse:
        """
        @summary Deletes an account whose one or more virtual private clouds (VPCs) are associated with a private zone.
        
        @param request: DeleteUserVpcAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserVpcAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserVpcAuthorization',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteUserVpcAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_vpc_authorization_with_options_async(
        self,
        request: pvtz_20180101_models.DeleteUserVpcAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteUserVpcAuthorizationResponse:
        """
        @summary Deletes an account whose one or more virtual private clouds (VPCs) are associated with a private zone.
        
        @param request: DeleteUserVpcAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserVpcAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserVpcAuthorization',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteUserVpcAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_vpc_authorization(
        self,
        request: pvtz_20180101_models.DeleteUserVpcAuthorizationRequest,
    ) -> pvtz_20180101_models.DeleteUserVpcAuthorizationResponse:
        """
        @summary Deletes an account whose one or more virtual private clouds (VPCs) are associated with a private zone.
        
        @param request: DeleteUserVpcAuthorizationRequest
        @return: DeleteUserVpcAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_vpc_authorization_with_options(request, runtime)

    async def delete_user_vpc_authorization_async(
        self,
        request: pvtz_20180101_models.DeleteUserVpcAuthorizationRequest,
    ) -> pvtz_20180101_models.DeleteUserVpcAuthorizationResponse:
        """
        @summary Deletes an account whose one or more virtual private clouds (VPCs) are associated with a private zone.
        
        @param request: DeleteUserVpcAuthorizationRequest
        @return: DeleteUserVpcAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_vpc_authorization_with_options_async(request, runtime)

    def delete_zone_with_options(
        self,
        request: pvtz_20180101_models.DeleteZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteZoneResponse:
        """
        @summary Deletes a zone.
        
        @param request: DeleteZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteZone',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_zone_with_options_async(
        self,
        request: pvtz_20180101_models.DeleteZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteZoneResponse:
        """
        @summary Deletes a zone.
        
        @param request: DeleteZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteZone',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_zone(
        self,
        request: pvtz_20180101_models.DeleteZoneRequest,
    ) -> pvtz_20180101_models.DeleteZoneResponse:
        """
        @summary Deletes a zone.
        
        @param request: DeleteZoneRequest
        @return: DeleteZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_zone_with_options(request, runtime)

    async def delete_zone_async(
        self,
        request: pvtz_20180101_models.DeleteZoneRequest,
    ) -> pvtz_20180101_models.DeleteZoneResponse:
        """
        @summary Deletes a zone.
        
        @param request: DeleteZoneRequest
        @return: DeleteZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_zone_with_options_async(request, runtime)

    def delete_zone_record_with_options(
        self,
        request: pvtz_20180101_models.DeleteZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteZoneRecordResponse:
        """
        @summary Deletes a Domain Name System (DNS) record of a zone.
        
        @param request: DeleteZoneRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteZoneRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteZoneRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_zone_record_with_options_async(
        self,
        request: pvtz_20180101_models.DeleteZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteZoneRecordResponse:
        """
        @summary Deletes a Domain Name System (DNS) record of a zone.
        
        @param request: DeleteZoneRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteZoneRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteZoneRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_zone_record(
        self,
        request: pvtz_20180101_models.DeleteZoneRecordRequest,
    ) -> pvtz_20180101_models.DeleteZoneRecordResponse:
        """
        @summary Deletes a Domain Name System (DNS) record of a zone.
        
        @param request: DeleteZoneRecordRequest
        @return: DeleteZoneRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_zone_record_with_options(request, runtime)

    async def delete_zone_record_async(
        self,
        request: pvtz_20180101_models.DeleteZoneRecordRequest,
    ) -> pvtz_20180101_models.DeleteZoneRecordResponse:
        """
        @summary Deletes a Domain Name System (DNS) record of a zone.
        
        @param request: DeleteZoneRecordRequest
        @return: DeleteZoneRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_zone_record_with_options_async(request, runtime)

    def describe_change_logs_with_options(
        self,
        request: pvtz_20180101_models.DescribeChangeLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeChangeLogsResponse:
        """
        @summary Queries a list of operation logs.
        
        @param request: DescribeChangeLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChangeLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChangeLogs',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeChangeLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_change_logs_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeChangeLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeChangeLogsResponse:
        """
        @summary Queries a list of operation logs.
        
        @param request: DescribeChangeLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChangeLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChangeLogs',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeChangeLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_change_logs(
        self,
        request: pvtz_20180101_models.DescribeChangeLogsRequest,
    ) -> pvtz_20180101_models.DescribeChangeLogsResponse:
        """
        @summary Queries a list of operation logs.
        
        @param request: DescribeChangeLogsRequest
        @return: DescribeChangeLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_change_logs_with_options(request, runtime)

    async def describe_change_logs_async(
        self,
        request: pvtz_20180101_models.DescribeChangeLogsRequest,
    ) -> pvtz_20180101_models.DescribeChangeLogsResponse:
        """
        @summary Queries a list of operation logs.
        
        @param request: DescribeChangeLogsRequest
        @return: DescribeChangeLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_change_logs_with_options_async(request, runtime)

    def describe_custom_line_info_with_options(
        self,
        request: pvtz_20180101_models.DescribeCustomLineInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeCustomLineInfoResponse:
        """
        @param request: DescribeCustomLineInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomLineInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLineInfo',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeCustomLineInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_line_info_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeCustomLineInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeCustomLineInfoResponse:
        """
        @param request: DescribeCustomLineInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomLineInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLineInfo',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeCustomLineInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_line_info(
        self,
        request: pvtz_20180101_models.DescribeCustomLineInfoRequest,
    ) -> pvtz_20180101_models.DescribeCustomLineInfoResponse:
        """
        @param request: DescribeCustomLineInfoRequest
        @return: DescribeCustomLineInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_line_info_with_options(request, runtime)

    async def describe_custom_line_info_async(
        self,
        request: pvtz_20180101_models.DescribeCustomLineInfoRequest,
    ) -> pvtz_20180101_models.DescribeCustomLineInfoResponse:
        """
        @param request: DescribeCustomLineInfoRequest
        @return: DescribeCustomLineInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_line_info_with_options_async(request, runtime)

    def describe_custom_lines_with_options(
        self,
        request: pvtz_20180101_models.DescribeCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeCustomLinesResponse:
        """
        @param request: DescribeCustomLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomLinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLines',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeCustomLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_lines_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeCustomLinesResponse:
        """
        @param request: DescribeCustomLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomLinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLines',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeCustomLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_lines(
        self,
        request: pvtz_20180101_models.DescribeCustomLinesRequest,
    ) -> pvtz_20180101_models.DescribeCustomLinesResponse:
        """
        @param request: DescribeCustomLinesRequest
        @return: DescribeCustomLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_lines_with_options(request, runtime)

    async def describe_custom_lines_async(
        self,
        request: pvtz_20180101_models.DescribeCustomLinesRequest,
    ) -> pvtz_20180101_models.DescribeCustomLinesResponse:
        """
        @param request: DescribeCustomLinesRequest
        @return: DescribeCustomLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_lines_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: pvtz_20180101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeRegionsResponse:
        """
        @summary Queries a list of available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.vpc_type):
            query['VpcType'] = request.vpc_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeRegionsResponse:
        """
        @summary Queries a list of available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.vpc_type):
            query['VpcType'] = request.vpc_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: pvtz_20180101_models.DescribeRegionsRequest,
    ) -> pvtz_20180101_models.DescribeRegionsResponse:
        """
        @summary Queries a list of available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: pvtz_20180101_models.DescribeRegionsRequest,
    ) -> pvtz_20180101_models.DescribeRegionsResponse:
        """
        @summary Queries a list of available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_request_graph_with_options(
        self,
        request: pvtz_20180101_models.DescribeRequestGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeRequestGraphResponse:
        """
        @summary Queries the information about Domain Name System (DNS) requests.
        
        @param request: DescribeRequestGraphRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRequestGraphResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRequestGraph',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeRequestGraphResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_request_graph_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeRequestGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeRequestGraphResponse:
        """
        @summary Queries the information about Domain Name System (DNS) requests.
        
        @param request: DescribeRequestGraphRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRequestGraphResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRequestGraph',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeRequestGraphResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_request_graph(
        self,
        request: pvtz_20180101_models.DescribeRequestGraphRequest,
    ) -> pvtz_20180101_models.DescribeRequestGraphResponse:
        """
        @summary Queries the information about Domain Name System (DNS) requests.
        
        @param request: DescribeRequestGraphRequest
        @return: DescribeRequestGraphResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_request_graph_with_options(request, runtime)

    async def describe_request_graph_async(
        self,
        request: pvtz_20180101_models.DescribeRequestGraphRequest,
    ) -> pvtz_20180101_models.DescribeRequestGraphResponse:
        """
        @summary Queries the information about Domain Name System (DNS) requests.
        
        @param request: DescribeRequestGraphRequest
        @return: DescribeRequestGraphResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_request_graph_with_options_async(request, runtime)

    def describe_resolver_available_zones_with_options(
        self,
        request: pvtz_20180101_models.DescribeResolverAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeResolverAvailableZonesResponse:
        """
        @summary Queries a list of available zones.
        
        @param request: DescribeResolverAvailableZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResolverAvailableZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.az_id):
            query['AzId'] = request.az_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resolver_region_id):
            query['ResolverRegionId'] = request.resolver_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResolverAvailableZones',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeResolverAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resolver_available_zones_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeResolverAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeResolverAvailableZonesResponse:
        """
        @summary Queries a list of available zones.
        
        @param request: DescribeResolverAvailableZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResolverAvailableZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.az_id):
            query['AzId'] = request.az_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resolver_region_id):
            query['ResolverRegionId'] = request.resolver_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResolverAvailableZones',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeResolverAvailableZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resolver_available_zones(
        self,
        request: pvtz_20180101_models.DescribeResolverAvailableZonesRequest,
    ) -> pvtz_20180101_models.DescribeResolverAvailableZonesResponse:
        """
        @summary Queries a list of available zones.
        
        @param request: DescribeResolverAvailableZonesRequest
        @return: DescribeResolverAvailableZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resolver_available_zones_with_options(request, runtime)

    async def describe_resolver_available_zones_async(
        self,
        request: pvtz_20180101_models.DescribeResolverAvailableZonesRequest,
    ) -> pvtz_20180101_models.DescribeResolverAvailableZonesResponse:
        """
        @summary Queries a list of available zones.
        
        @param request: DescribeResolverAvailableZonesRequest
        @return: DescribeResolverAvailableZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resolver_available_zones_with_options_async(request, runtime)

    def describe_resolver_endpoint_with_options(
        self,
        request: pvtz_20180101_models.DescribeResolverEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeResolverEndpointResponse:
        """
        @summary Queries the information about an endpoint.
        
        @param request: DescribeResolverEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResolverEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResolverEndpoint',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeResolverEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resolver_endpoint_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeResolverEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeResolverEndpointResponse:
        """
        @summary Queries the information about an endpoint.
        
        @param request: DescribeResolverEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResolverEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResolverEndpoint',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeResolverEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resolver_endpoint(
        self,
        request: pvtz_20180101_models.DescribeResolverEndpointRequest,
    ) -> pvtz_20180101_models.DescribeResolverEndpointResponse:
        """
        @summary Queries the information about an endpoint.
        
        @param request: DescribeResolverEndpointRequest
        @return: DescribeResolverEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resolver_endpoint_with_options(request, runtime)

    async def describe_resolver_endpoint_async(
        self,
        request: pvtz_20180101_models.DescribeResolverEndpointRequest,
    ) -> pvtz_20180101_models.DescribeResolverEndpointResponse:
        """
        @summary Queries the information about an endpoint.
        
        @param request: DescribeResolverEndpointRequest
        @return: DescribeResolverEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resolver_endpoint_with_options_async(request, runtime)

    def describe_resolver_endpoints_with_options(
        self,
        request: pvtz_20180101_models.DescribeResolverEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeResolverEndpointsResponse:
        """
        @summary Queries a list of endpoints.
        
        @param request: DescribeResolverEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResolverEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResolverEndpoints',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeResolverEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resolver_endpoints_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeResolverEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeResolverEndpointsResponse:
        """
        @summary Queries a list of endpoints.
        
        @param request: DescribeResolverEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResolverEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResolverEndpoints',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeResolverEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resolver_endpoints(
        self,
        request: pvtz_20180101_models.DescribeResolverEndpointsRequest,
    ) -> pvtz_20180101_models.DescribeResolverEndpointsResponse:
        """
        @summary Queries a list of endpoints.
        
        @param request: DescribeResolverEndpointsRequest
        @return: DescribeResolverEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resolver_endpoints_with_options(request, runtime)

    async def describe_resolver_endpoints_async(
        self,
        request: pvtz_20180101_models.DescribeResolverEndpointsRequest,
    ) -> pvtz_20180101_models.DescribeResolverEndpointsResponse:
        """
        @summary Queries a list of endpoints.
        
        @param request: DescribeResolverEndpointsRequest
        @return: DescribeResolverEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resolver_endpoints_with_options_async(request, runtime)

    def describe_resolver_rule_with_options(
        self,
        request: pvtz_20180101_models.DescribeResolverRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeResolverRuleResponse:
        """
        @summary Queries the information about a forwarding rule.
        
        @param request: DescribeResolverRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResolverRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResolverRule',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeResolverRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resolver_rule_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeResolverRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeResolverRuleResponse:
        """
        @summary Queries the information about a forwarding rule.
        
        @param request: DescribeResolverRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResolverRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResolverRule',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeResolverRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resolver_rule(
        self,
        request: pvtz_20180101_models.DescribeResolverRuleRequest,
    ) -> pvtz_20180101_models.DescribeResolverRuleResponse:
        """
        @summary Queries the information about a forwarding rule.
        
        @param request: DescribeResolverRuleRequest
        @return: DescribeResolverRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resolver_rule_with_options(request, runtime)

    async def describe_resolver_rule_async(
        self,
        request: pvtz_20180101_models.DescribeResolverRuleRequest,
    ) -> pvtz_20180101_models.DescribeResolverRuleResponse:
        """
        @summary Queries the information about a forwarding rule.
        
        @param request: DescribeResolverRuleRequest
        @return: DescribeResolverRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resolver_rule_with_options_async(request, runtime)

    def describe_resolver_rules_with_options(
        self,
        request: pvtz_20180101_models.DescribeResolverRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeResolverRulesResponse:
        """
        @summary Queries a list of forwarding rules.
        
        @param request: DescribeResolverRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResolverRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResolverRules',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeResolverRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resolver_rules_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeResolverRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeResolverRulesResponse:
        """
        @summary Queries a list of forwarding rules.
        
        @param request: DescribeResolverRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResolverRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResolverRules',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeResolverRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resolver_rules(
        self,
        request: pvtz_20180101_models.DescribeResolverRulesRequest,
    ) -> pvtz_20180101_models.DescribeResolverRulesResponse:
        """
        @summary Queries a list of forwarding rules.
        
        @param request: DescribeResolverRulesRequest
        @return: DescribeResolverRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resolver_rules_with_options(request, runtime)

    async def describe_resolver_rules_async(
        self,
        request: pvtz_20180101_models.DescribeResolverRulesRequest,
    ) -> pvtz_20180101_models.DescribeResolverRulesResponse:
        """
        @summary Queries a list of forwarding rules.
        
        @param request: DescribeResolverRulesRequest
        @return: DescribeResolverRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resolver_rules_with_options_async(request, runtime)

    def describe_statistic_summary_with_options(
        self,
        request: pvtz_20180101_models.DescribeStatisticSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeStatisticSummaryResponse:
        """
        @summary Queries the statistics on the Domain Name System (DNS) requests received on the previous day.
        
        @param request: DescribeStatisticSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStatisticSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStatisticSummary',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeStatisticSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_statistic_summary_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeStatisticSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeStatisticSummaryResponse:
        """
        @summary Queries the statistics on the Domain Name System (DNS) requests received on the previous day.
        
        @param request: DescribeStatisticSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStatisticSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStatisticSummary',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeStatisticSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_statistic_summary(
        self,
        request: pvtz_20180101_models.DescribeStatisticSummaryRequest,
    ) -> pvtz_20180101_models.DescribeStatisticSummaryResponse:
        """
        @summary Queries the statistics on the Domain Name System (DNS) requests received on the previous day.
        
        @param request: DescribeStatisticSummaryRequest
        @return: DescribeStatisticSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_statistic_summary_with_options(request, runtime)

    async def describe_statistic_summary_async(
        self,
        request: pvtz_20180101_models.DescribeStatisticSummaryRequest,
    ) -> pvtz_20180101_models.DescribeStatisticSummaryResponse:
        """
        @summary Queries the statistics on the Domain Name System (DNS) requests received on the previous day.
        
        @param request: DescribeStatisticSummaryRequest
        @return: DescribeStatisticSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_statistic_summary_with_options_async(request, runtime)

    def describe_sync_ecs_host_task_with_options(
        self,
        request: pvtz_20180101_models.DescribeSyncEcsHostTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeSyncEcsHostTaskResponse:
        """
        @summary Queries the information about a hostname synchronization task.
        
        @param request: DescribeSyncEcsHostTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncEcsHostTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncEcsHostTask',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeSyncEcsHostTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_ecs_host_task_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeSyncEcsHostTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeSyncEcsHostTaskResponse:
        """
        @summary Queries the information about a hostname synchronization task.
        
        @param request: DescribeSyncEcsHostTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncEcsHostTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncEcsHostTask',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeSyncEcsHostTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_ecs_host_task(
        self,
        request: pvtz_20180101_models.DescribeSyncEcsHostTaskRequest,
    ) -> pvtz_20180101_models.DescribeSyncEcsHostTaskResponse:
        """
        @summary Queries the information about a hostname synchronization task.
        
        @param request: DescribeSyncEcsHostTaskRequest
        @return: DescribeSyncEcsHostTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sync_ecs_host_task_with_options(request, runtime)

    async def describe_sync_ecs_host_task_async(
        self,
        request: pvtz_20180101_models.DescribeSyncEcsHostTaskRequest,
    ) -> pvtz_20180101_models.DescribeSyncEcsHostTaskResponse:
        """
        @summary Queries the information about a hostname synchronization task.
        
        @param request: DescribeSyncEcsHostTaskRequest
        @return: DescribeSyncEcsHostTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sync_ecs_host_task_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: pvtz_20180101_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeTagsResponse:
        """
        @summary Queries a list of existing tags.
        
        @param request: DescribeTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeTagsResponse:
        """
        @summary Queries a list of existing tags.
        
        @param request: DescribeTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags(
        self,
        request: pvtz_20180101_models.DescribeTagsRequest,
    ) -> pvtz_20180101_models.DescribeTagsResponse:
        """
        @summary Queries a list of existing tags.
        
        @param request: DescribeTagsRequest
        @return: DescribeTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: pvtz_20180101_models.DescribeTagsRequest,
    ) -> pvtz_20180101_models.DescribeTagsResponse:
        """
        @summary Queries a list of existing tags.
        
        @param request: DescribeTagsRequest
        @return: DescribeTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_user_vpc_authorizations_with_options(
        self,
        request: pvtz_20180101_models.DescribeUserVpcAuthorizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeUserVpcAuthorizationsResponse:
        """
        @summary Queries a list of accounts whose virtual private clouds (VPCs) are associated with a private zone.
        
        @param request: DescribeUserVpcAuthorizationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserVpcAuthorizationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserVpcAuthorizations',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeUserVpcAuthorizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_vpc_authorizations_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeUserVpcAuthorizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeUserVpcAuthorizationsResponse:
        """
        @summary Queries a list of accounts whose virtual private clouds (VPCs) are associated with a private zone.
        
        @param request: DescribeUserVpcAuthorizationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserVpcAuthorizationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserVpcAuthorizations',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeUserVpcAuthorizationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_vpc_authorizations(
        self,
        request: pvtz_20180101_models.DescribeUserVpcAuthorizationsRequest,
    ) -> pvtz_20180101_models.DescribeUserVpcAuthorizationsResponse:
        """
        @summary Queries a list of accounts whose virtual private clouds (VPCs) are associated with a private zone.
        
        @param request: DescribeUserVpcAuthorizationsRequest
        @return: DescribeUserVpcAuthorizationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_vpc_authorizations_with_options(request, runtime)

    async def describe_user_vpc_authorizations_async(
        self,
        request: pvtz_20180101_models.DescribeUserVpcAuthorizationsRequest,
    ) -> pvtz_20180101_models.DescribeUserVpcAuthorizationsResponse:
        """
        @summary Queries a list of accounts whose virtual private clouds (VPCs) are associated with a private zone.
        
        @param request: DescribeUserVpcAuthorizationsRequest
        @return: DescribeUserVpcAuthorizationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_vpc_authorizations_with_options_async(request, runtime)

    def describe_zone_info_with_options(
        self,
        request: pvtz_20180101_models.DescribeZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneInfoResponse:
        """
        @summary Queries the information about a zone.
        
        @param request: DescribeZoneInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZoneInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZoneInfo',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zone_info_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneInfoResponse:
        """
        @summary Queries the information about a zone.
        
        @param request: DescribeZoneInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZoneInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZoneInfo',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zone_info(
        self,
        request: pvtz_20180101_models.DescribeZoneInfoRequest,
    ) -> pvtz_20180101_models.DescribeZoneInfoResponse:
        """
        @summary Queries the information about a zone.
        
        @param request: DescribeZoneInfoRequest
        @return: DescribeZoneInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zone_info_with_options(request, runtime)

    async def describe_zone_info_async(
        self,
        request: pvtz_20180101_models.DescribeZoneInfoRequest,
    ) -> pvtz_20180101_models.DescribeZoneInfoResponse:
        """
        @summary Queries the information about a zone.
        
        @param request: DescribeZoneInfoRequest
        @return: DescribeZoneInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zone_info_with_options_async(request, runtime)

    def describe_zone_record_with_options(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneRecordResponse:
        """
        @param request: DescribeZoneRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZoneRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zone_record_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneRecordResponse:
        """
        @param request: DescribeZoneRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZoneRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zone_record(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordRequest,
    ) -> pvtz_20180101_models.DescribeZoneRecordResponse:
        """
        @param request: DescribeZoneRecordRequest
        @return: DescribeZoneRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zone_record_with_options(request, runtime)

    async def describe_zone_record_async(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordRequest,
    ) -> pvtz_20180101_models.DescribeZoneRecordResponse:
        """
        @param request: DescribeZoneRecordRequest
        @return: DescribeZoneRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zone_record_with_options_async(request, runtime)

    def describe_zone_records_with_options(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneRecordsResponse:
        """
        @summary Queries a list of Domain Name System (DNS) records for a zone.
        
        @param request: DescribeZoneRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZoneRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZoneRecords',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zone_records_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneRecordsResponse:
        """
        @summary Queries a list of Domain Name System (DNS) records for a zone.
        
        @param request: DescribeZoneRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZoneRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZoneRecords',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zone_records(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordsRequest,
    ) -> pvtz_20180101_models.DescribeZoneRecordsResponse:
        """
        @summary Queries a list of Domain Name System (DNS) records for a zone.
        
        @param request: DescribeZoneRecordsRequest
        @return: DescribeZoneRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zone_records_with_options(request, runtime)

    async def describe_zone_records_async(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordsRequest,
    ) -> pvtz_20180101_models.DescribeZoneRecordsResponse:
        """
        @summary Queries a list of Domain Name System (DNS) records for a zone.
        
        @param request: DescribeZoneRecordsRequest
        @return: DescribeZoneRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zone_records_with_options_async(request, runtime)

    def describe_zone_vpc_tree_with_options(
        self,
        request: pvtz_20180101_models.DescribeZoneVpcTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneVpcTreeResponse:
        """
        @summary Queries a list of zones and a list of virtual private clouds (VPCs) that are bound to the zones.
        
        @description We recommend that you do not call this API operation due to its poor performance. Instead, you can call the DescribeZones operation to query a list of zones. If you want to query the information about VPCs to which a zone is bound, you can call the DescribeZoneInfo operation based on the zone ID.
        
        @param request: DescribeZoneVpcTreeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZoneVpcTreeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZoneVpcTree',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneVpcTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zone_vpc_tree_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZoneVpcTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneVpcTreeResponse:
        """
        @summary Queries a list of zones and a list of virtual private clouds (VPCs) that are bound to the zones.
        
        @description We recommend that you do not call this API operation due to its poor performance. Instead, you can call the DescribeZones operation to query a list of zones. If you want to query the information about VPCs to which a zone is bound, you can call the DescribeZoneInfo operation based on the zone ID.
        
        @param request: DescribeZoneVpcTreeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZoneVpcTreeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZoneVpcTree',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneVpcTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zone_vpc_tree(
        self,
        request: pvtz_20180101_models.DescribeZoneVpcTreeRequest,
    ) -> pvtz_20180101_models.DescribeZoneVpcTreeResponse:
        """
        @summary Queries a list of zones and a list of virtual private clouds (VPCs) that are bound to the zones.
        
        @description We recommend that you do not call this API operation due to its poor performance. Instead, you can call the DescribeZones operation to query a list of zones. If you want to query the information about VPCs to which a zone is bound, you can call the DescribeZoneInfo operation based on the zone ID.
        
        @param request: DescribeZoneVpcTreeRequest
        @return: DescribeZoneVpcTreeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zone_vpc_tree_with_options(request, runtime)

    async def describe_zone_vpc_tree_async(
        self,
        request: pvtz_20180101_models.DescribeZoneVpcTreeRequest,
    ) -> pvtz_20180101_models.DescribeZoneVpcTreeResponse:
        """
        @summary Queries a list of zones and a list of virtual private clouds (VPCs) that are bound to the zones.
        
        @description We recommend that you do not call this API operation due to its poor performance. Instead, you can call the DescribeZones operation to query a list of zones. If you want to query the information about VPCs to which a zone is bound, you can call the DescribeZoneInfo operation based on the zone ID.
        
        @param request: DescribeZoneVpcTreeRequest
        @return: DescribeZoneVpcTreeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zone_vpc_tree_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: pvtz_20180101_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZonesResponse:
        """
        @summary Queries a list of zones for a user.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_region_id):
            query['QueryRegionId'] = request.query_region_id
        if not UtilClient.is_unset(request.query_vpc_id):
            query['QueryVpcId'] = request.query_vpc_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_tag):
            query['ResourceTag'] = request.resource_tag
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.zone_tag):
            query['ZoneTag'] = request.zone_tag
        if not UtilClient.is_unset(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZonesResponse:
        """
        @summary Queries a list of zones for a user.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_region_id):
            query['QueryRegionId'] = request.query_region_id
        if not UtilClient.is_unset(request.query_vpc_id):
            query['QueryVpcId'] = request.query_vpc_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_tag):
            query['ResourceTag'] = request.resource_tag
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.zone_tag):
            query['ZoneTag'] = request.zone_tag
        if not UtilClient.is_unset(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: pvtz_20180101_models.DescribeZonesRequest,
    ) -> pvtz_20180101_models.DescribeZonesResponse:
        """
        @summary Queries a list of zones for a user.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: pvtz_20180101_models.DescribeZonesRequest,
    ) -> pvtz_20180101_models.DescribeZonesResponse:
        """
        @summary Queries a list of zones for a user.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: pvtz_20180101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.ListTagResourcesResponse:
        """
        @summary Queries a list of tags added to one or more resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: pvtz_20180101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.ListTagResourcesResponse:
        """
        @summary Queries a list of tags added to one or more resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: pvtz_20180101_models.ListTagResourcesRequest,
    ) -> pvtz_20180101_models.ListTagResourcesResponse:
        """
        @summary Queries a list of tags added to one or more resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: pvtz_20180101_models.ListTagResourcesRequest,
    ) -> pvtz_20180101_models.ListTagResourcesResponse:
        """
        @summary Queries a list of tags added to one or more resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: pvtz_20180101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.MoveResourceGroupResponse:
        """
        @summary Moves a zone to another resource group.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: pvtz_20180101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.MoveResourceGroupResponse:
        """
        @summary Moves a zone to another resource group.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: pvtz_20180101_models.MoveResourceGroupRequest,
    ) -> pvtz_20180101_models.MoveResourceGroupResponse:
        """
        @summary Moves a zone to another resource group.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: pvtz_20180101_models.MoveResourceGroupRequest,
    ) -> pvtz_20180101_models.MoveResourceGroupResponse:
        """
        @summary Moves a zone to another resource group.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def search_custom_lines_with_options(
        self,
        request: pvtz_20180101_models.SearchCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SearchCustomLinesResponse:
        """
        @param request: SearchCustomLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCustomLinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_timestamp_end):
            query['CreateTimestampEnd'] = request.create_timestamp_end
        if not UtilClient.is_unset(request.create_timestamp_start):
            query['CreateTimestampStart'] = request.create_timestamp_start
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.ipv_4):
            query['Ipv4'] = request.ipv_4
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.update_timestamp_end):
            query['UpdateTimestampEnd'] = request.update_timestamp_end
        if not UtilClient.is_unset(request.update_timestamp_start):
            query['UpdateTimestampStart'] = request.update_timestamp_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCustomLines',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.SearchCustomLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_custom_lines_with_options_async(
        self,
        request: pvtz_20180101_models.SearchCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SearchCustomLinesResponse:
        """
        @param request: SearchCustomLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCustomLinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_timestamp_end):
            query['CreateTimestampEnd'] = request.create_timestamp_end
        if not UtilClient.is_unset(request.create_timestamp_start):
            query['CreateTimestampStart'] = request.create_timestamp_start
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.ipv_4):
            query['Ipv4'] = request.ipv_4
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.update_timestamp_end):
            query['UpdateTimestampEnd'] = request.update_timestamp_end
        if not UtilClient.is_unset(request.update_timestamp_start):
            query['UpdateTimestampStart'] = request.update_timestamp_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCustomLines',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.SearchCustomLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_custom_lines(
        self,
        request: pvtz_20180101_models.SearchCustomLinesRequest,
    ) -> pvtz_20180101_models.SearchCustomLinesResponse:
        """
        @param request: SearchCustomLinesRequest
        @return: SearchCustomLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_custom_lines_with_options(request, runtime)

    async def search_custom_lines_async(
        self,
        request: pvtz_20180101_models.SearchCustomLinesRequest,
    ) -> pvtz_20180101_models.SearchCustomLinesResponse:
        """
        @param request: SearchCustomLinesRequest
        @return: SearchCustomLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_custom_lines_with_options_async(request, runtime)

    def set_proxy_pattern_with_options(
        self,
        request: pvtz_20180101_models.SetProxyPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SetProxyPatternResponse:
        """
        @summary Configures the recursive resolution proxy feature.
        
        @param request: SetProxyPatternRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetProxyPatternResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetProxyPattern',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.SetProxyPatternResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_proxy_pattern_with_options_async(
        self,
        request: pvtz_20180101_models.SetProxyPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SetProxyPatternResponse:
        """
        @summary Configures the recursive resolution proxy feature.
        
        @param request: SetProxyPatternRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetProxyPatternResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetProxyPattern',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.SetProxyPatternResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_proxy_pattern(
        self,
        request: pvtz_20180101_models.SetProxyPatternRequest,
    ) -> pvtz_20180101_models.SetProxyPatternResponse:
        """
        @summary Configures the recursive resolution proxy feature.
        
        @param request: SetProxyPatternRequest
        @return: SetProxyPatternResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_proxy_pattern_with_options(request, runtime)

    async def set_proxy_pattern_async(
        self,
        request: pvtz_20180101_models.SetProxyPatternRequest,
    ) -> pvtz_20180101_models.SetProxyPatternResponse:
        """
        @summary Configures the recursive resolution proxy feature.
        
        @param request: SetProxyPatternRequest
        @return: SetProxyPatternResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_proxy_pattern_with_options_async(request, runtime)

    def set_zone_record_status_with_options(
        self,
        request: pvtz_20180101_models.SetZoneRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SetZoneRecordStatusResponse:
        """
        @summary Specifies the status of a Domain Name System (DNS) record for a zone.
        
        @param request: SetZoneRecordStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetZoneRecordStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetZoneRecordStatus',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.SetZoneRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_zone_record_status_with_options_async(
        self,
        request: pvtz_20180101_models.SetZoneRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SetZoneRecordStatusResponse:
        """
        @summary Specifies the status of a Domain Name System (DNS) record for a zone.
        
        @param request: SetZoneRecordStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetZoneRecordStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetZoneRecordStatus',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.SetZoneRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_zone_record_status(
        self,
        request: pvtz_20180101_models.SetZoneRecordStatusRequest,
    ) -> pvtz_20180101_models.SetZoneRecordStatusResponse:
        """
        @summary Specifies the status of a Domain Name System (DNS) record for a zone.
        
        @param request: SetZoneRecordStatusRequest
        @return: SetZoneRecordStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_zone_record_status_with_options(request, runtime)

    async def set_zone_record_status_async(
        self,
        request: pvtz_20180101_models.SetZoneRecordStatusRequest,
    ) -> pvtz_20180101_models.SetZoneRecordStatusResponse:
        """
        @summary Specifies the status of a Domain Name System (DNS) record for a zone.
        
        @param request: SetZoneRecordStatusRequest
        @return: SetZoneRecordStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_zone_record_status_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: pvtz_20180101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.over_write):
            query['OverWrite'] = request.over_write
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: pvtz_20180101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.over_write):
            query['OverWrite'] = request.over_write
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: pvtz_20180101_models.TagResourcesRequest,
    ) -> pvtz_20180101_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: pvtz_20180101_models.TagResourcesRequest,
    ) -> pvtz_20180101_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: pvtz_20180101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: pvtz_20180101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: pvtz_20180101_models.UntagResourcesRequest,
    ) -> pvtz_20180101_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: pvtz_20180101_models.UntagResourcesRequest,
    ) -> pvtz_20180101_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_custom_line_with_options(
        self,
        request: pvtz_20180101_models.UpdateCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateCustomLineResponse:
        """
        @param request: UpdateCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipv_4s):
            query['Ipv4s'] = request.ipv_4s
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomLine',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_line_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateCustomLineResponse:
        """
        @param request: UpdateCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipv_4s):
            query['Ipv4s'] = request.ipv_4s
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomLine',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_line(
        self,
        request: pvtz_20180101_models.UpdateCustomLineRequest,
    ) -> pvtz_20180101_models.UpdateCustomLineResponse:
        """
        @param request: UpdateCustomLineRequest
        @return: UpdateCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_line_with_options(request, runtime)

    async def update_custom_line_async(
        self,
        request: pvtz_20180101_models.UpdateCustomLineRequest,
    ) -> pvtz_20180101_models.UpdateCustomLineResponse:
        """
        @param request: UpdateCustomLineRequest
        @return: UpdateCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_line_with_options_async(request, runtime)

    def update_record_remark_with_options(
        self,
        request: pvtz_20180101_models.UpdateRecordRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateRecordRemarkResponse:
        """
        @summary Modifies the description of a Domain Name System (DNS) record that is added for a zone.
        
        @param request: UpdateRecordRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRecordRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecordRemark',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateRecordRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_remark_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateRecordRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateRecordRemarkResponse:
        """
        @summary Modifies the description of a Domain Name System (DNS) record that is added for a zone.
        
        @param request: UpdateRecordRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRecordRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecordRemark',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateRecordRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_record_remark(
        self,
        request: pvtz_20180101_models.UpdateRecordRemarkRequest,
    ) -> pvtz_20180101_models.UpdateRecordRemarkResponse:
        """
        @summary Modifies the description of a Domain Name System (DNS) record that is added for a zone.
        
        @param request: UpdateRecordRemarkRequest
        @return: UpdateRecordRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_record_remark_with_options(request, runtime)

    async def update_record_remark_async(
        self,
        request: pvtz_20180101_models.UpdateRecordRemarkRequest,
    ) -> pvtz_20180101_models.UpdateRecordRemarkResponse:
        """
        @summary Modifies the description of a Domain Name System (DNS) record that is added for a zone.
        
        @param request: UpdateRecordRemarkRequest
        @return: UpdateRecordRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_record_remark_with_options_async(request, runtime)

    def update_resolver_endpoint_with_options(
        self,
        request: pvtz_20180101_models.UpdateResolverEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateResolverEndpointResponse:
        """
        @summary Modifies an endpoint.
        
        @param request: UpdateResolverEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResolverEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.ip_config):
            query['IpConfig'] = request.ip_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResolverEndpoint',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateResolverEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resolver_endpoint_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateResolverEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateResolverEndpointResponse:
        """
        @summary Modifies an endpoint.
        
        @param request: UpdateResolverEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResolverEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.ip_config):
            query['IpConfig'] = request.ip_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResolverEndpoint',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateResolverEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resolver_endpoint(
        self,
        request: pvtz_20180101_models.UpdateResolverEndpointRequest,
    ) -> pvtz_20180101_models.UpdateResolverEndpointResponse:
        """
        @summary Modifies an endpoint.
        
        @param request: UpdateResolverEndpointRequest
        @return: UpdateResolverEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_resolver_endpoint_with_options(request, runtime)

    async def update_resolver_endpoint_async(
        self,
        request: pvtz_20180101_models.UpdateResolverEndpointRequest,
    ) -> pvtz_20180101_models.UpdateResolverEndpointResponse:
        """
        @summary Modifies an endpoint.
        
        @param request: UpdateResolverEndpointRequest
        @return: UpdateResolverEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_resolver_endpoint_with_options_async(request, runtime)

    def update_resolver_rule_with_options(
        self,
        request: pvtz_20180101_models.UpdateResolverRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateResolverRuleResponse:
        """
        @summary Modifies a forwarding rule.
        
        @param request: UpdateResolverRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResolverRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.forward_ip):
            query['ForwardIp'] = request.forward_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResolverRule',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateResolverRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resolver_rule_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateResolverRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateResolverRuleResponse:
        """
        @summary Modifies a forwarding rule.
        
        @param request: UpdateResolverRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResolverRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.forward_ip):
            query['ForwardIp'] = request.forward_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResolverRule',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateResolverRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resolver_rule(
        self,
        request: pvtz_20180101_models.UpdateResolverRuleRequest,
    ) -> pvtz_20180101_models.UpdateResolverRuleResponse:
        """
        @summary Modifies a forwarding rule.
        
        @param request: UpdateResolverRuleRequest
        @return: UpdateResolverRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_resolver_rule_with_options(request, runtime)

    async def update_resolver_rule_async(
        self,
        request: pvtz_20180101_models.UpdateResolverRuleRequest,
    ) -> pvtz_20180101_models.UpdateResolverRuleResponse:
        """
        @summary Modifies a forwarding rule.
        
        @param request: UpdateResolverRuleRequest
        @return: UpdateResolverRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_resolver_rule_with_options_async(request, runtime)

    def update_sync_ecs_host_task_with_options(
        self,
        request: pvtz_20180101_models.UpdateSyncEcsHostTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateSyncEcsHostTaskResponse:
        """
        @summary Creates and updates a hostname synchronize task.
        
        @param request: UpdateSyncEcsHostTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSyncEcsHostTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSyncEcsHostTask',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateSyncEcsHostTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sync_ecs_host_task_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateSyncEcsHostTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateSyncEcsHostTaskResponse:
        """
        @summary Creates and updates a hostname synchronize task.
        
        @param request: UpdateSyncEcsHostTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSyncEcsHostTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSyncEcsHostTask',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateSyncEcsHostTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sync_ecs_host_task(
        self,
        request: pvtz_20180101_models.UpdateSyncEcsHostTaskRequest,
    ) -> pvtz_20180101_models.UpdateSyncEcsHostTaskResponse:
        """
        @summary Creates and updates a hostname synchronize task.
        
        @param request: UpdateSyncEcsHostTaskRequest
        @return: UpdateSyncEcsHostTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_sync_ecs_host_task_with_options(request, runtime)

    async def update_sync_ecs_host_task_async(
        self,
        request: pvtz_20180101_models.UpdateSyncEcsHostTaskRequest,
    ) -> pvtz_20180101_models.UpdateSyncEcsHostTaskResponse:
        """
        @summary Creates and updates a hostname synchronize task.
        
        @param request: UpdateSyncEcsHostTaskRequest
        @return: UpdateSyncEcsHostTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_sync_ecs_host_task_with_options_async(request, runtime)

    def update_zone_record_with_options(
        self,
        request: pvtz_20180101_models.UpdateZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateZoneRecordResponse:
        """
        @summary Modifies a Domain Name System (DNS) record of a zone.
        
        @param request: UpdateZoneRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateZoneRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.rr):
            query['Rr'] = request.rr
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateZoneRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_zone_record_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateZoneRecordResponse:
        """
        @summary Modifies a Domain Name System (DNS) record of a zone.
        
        @param request: UpdateZoneRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateZoneRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.rr):
            query['Rr'] = request.rr
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateZoneRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_zone_record(
        self,
        request: pvtz_20180101_models.UpdateZoneRecordRequest,
    ) -> pvtz_20180101_models.UpdateZoneRecordResponse:
        """
        @summary Modifies a Domain Name System (DNS) record of a zone.
        
        @param request: UpdateZoneRecordRequest
        @return: UpdateZoneRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_zone_record_with_options(request, runtime)

    async def update_zone_record_async(
        self,
        request: pvtz_20180101_models.UpdateZoneRecordRequest,
    ) -> pvtz_20180101_models.UpdateZoneRecordResponse:
        """
        @summary Modifies a Domain Name System (DNS) record of a zone.
        
        @param request: UpdateZoneRecordRequest
        @return: UpdateZoneRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_zone_record_with_options_async(request, runtime)

    def update_zone_remark_with_options(
        self,
        request: pvtz_20180101_models.UpdateZoneRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateZoneRemarkResponse:
        """
        @summary Modifies the description of a zone.
        
        @param request: UpdateZoneRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateZoneRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateZoneRemark',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateZoneRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_zone_remark_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateZoneRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateZoneRemarkResponse:
        """
        @summary Modifies the description of a zone.
        
        @param request: UpdateZoneRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateZoneRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateZoneRemark',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateZoneRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_zone_remark(
        self,
        request: pvtz_20180101_models.UpdateZoneRemarkRequest,
    ) -> pvtz_20180101_models.UpdateZoneRemarkResponse:
        """
        @summary Modifies the description of a zone.
        
        @param request: UpdateZoneRemarkRequest
        @return: UpdateZoneRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_zone_remark_with_options(request, runtime)

    async def update_zone_remark_async(
        self,
        request: pvtz_20180101_models.UpdateZoneRemarkRequest,
    ) -> pvtz_20180101_models.UpdateZoneRemarkResponse:
        """
        @summary Modifies the description of a zone.
        
        @param request: UpdateZoneRemarkRequest
        @return: UpdateZoneRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_zone_remark_with_options_async(request, runtime)
