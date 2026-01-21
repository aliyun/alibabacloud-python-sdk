# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_privatelink20200415 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('privatelink', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_user_to_vpc_endpoint_service_with_options(
        self,
        request: main_models.AddUserToVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.user_arn):
            query['UserARN'] = request.user_arn
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_vpc_endpoint_service_with_options_async(
        self,
        request: main_models.AddUserToVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.user_arn):
            query['UserARN'] = request.user_arn
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_vpc_endpoint_service(
        self,
        request: main_models.AddUserToVpcEndpointServiceRequest,
    ) -> main_models.AddUserToVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return self.add_user_to_vpc_endpoint_service_with_options(request, runtime)

    async def add_user_to_vpc_endpoint_service_async(
        self,
        request: main_models.AddUserToVpcEndpointServiceRequest,
    ) -> main_models.AddUserToVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return await self.add_user_to_vpc_endpoint_service_with_options_async(request, runtime)

    def add_zone_to_vpc_endpoint_with_options(
        self,
        request: main_models.AddZoneToVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddZoneToVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddZoneToVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddZoneToVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_zone_to_vpc_endpoint_with_options_async(
        self,
        request: main_models.AddZoneToVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddZoneToVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddZoneToVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddZoneToVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_zone_to_vpc_endpoint(
        self,
        request: main_models.AddZoneToVpcEndpointRequest,
    ) -> main_models.AddZoneToVpcEndpointResponse:
        runtime = RuntimeOptions()
        return self.add_zone_to_vpc_endpoint_with_options(request, runtime)

    async def add_zone_to_vpc_endpoint_async(
        self,
        request: main_models.AddZoneToVpcEndpointRequest,
    ) -> main_models.AddZoneToVpcEndpointResponse:
        runtime = RuntimeOptions()
        return await self.add_zone_to_vpc_endpoint_with_options_async(request, runtime)

    def attach_resource_to_vpc_endpoint_service_with_options(
        self,
        request: main_models.AttachResourceToVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachResourceToVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachResourceToVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachResourceToVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_resource_to_vpc_endpoint_service_with_options_async(
        self,
        request: main_models.AttachResourceToVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachResourceToVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachResourceToVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachResourceToVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_resource_to_vpc_endpoint_service(
        self,
        request: main_models.AttachResourceToVpcEndpointServiceRequest,
    ) -> main_models.AttachResourceToVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return self.attach_resource_to_vpc_endpoint_service_with_options(request, runtime)

    async def attach_resource_to_vpc_endpoint_service_async(
        self,
        request: main_models.AttachResourceToVpcEndpointServiceRequest,
    ) -> main_models.AttachResourceToVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return await self.attach_resource_to_vpc_endpoint_service_with_options_async(request, runtime)

    def attach_security_group_to_vpc_endpoint_with_options(
        self,
        request: main_models.AttachSecurityGroupToVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachSecurityGroupToVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachSecurityGroupToVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachSecurityGroupToVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_security_group_to_vpc_endpoint_with_options_async(
        self,
        request: main_models.AttachSecurityGroupToVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachSecurityGroupToVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachSecurityGroupToVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachSecurityGroupToVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_security_group_to_vpc_endpoint(
        self,
        request: main_models.AttachSecurityGroupToVpcEndpointRequest,
    ) -> main_models.AttachSecurityGroupToVpcEndpointResponse:
        runtime = RuntimeOptions()
        return self.attach_security_group_to_vpc_endpoint_with_options(request, runtime)

    async def attach_security_group_to_vpc_endpoint_async(
        self,
        request: main_models.AttachSecurityGroupToVpcEndpointRequest,
    ) -> main_models.AttachSecurityGroupToVpcEndpointResponse:
        runtime = RuntimeOptions()
        return await self.attach_security_group_to_vpc_endpoint_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_product_open_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CheckProductOpenResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CheckProductOpen',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckProductOpenResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_product_open_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CheckProductOpenResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CheckProductOpen',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckProductOpenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_product_open(self) -> main_models.CheckProductOpenResponse:
        runtime = RuntimeOptions()
        return self.check_product_open_with_options(runtime)

    async def check_product_open_async(self) -> main_models.CheckProductOpenResponse:
        runtime = RuntimeOptions()
        return await self.check_product_open_with_options_async(runtime)

    def create_vpc_endpoint_with_options(
        self,
        request: main_models.CreateVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_region_bandwidth):
            query['CrossRegionBandwidth'] = request.cross_region_bandwidth
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_description):
            query['EndpointDescription'] = request.endpoint_description
        if not DaraCore.is_null(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.protected_enabled):
            query['ProtectedEnabled'] = request.protected_enabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone):
            query['Zone'] = request.zone
        if not DaraCore.is_null(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        if not DaraCore.is_null(request.zone_private_ip_address_count):
            query['ZonePrivateIpAddressCount'] = request.zone_private_ip_address_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_endpoint_with_options_async(
        self,
        request: main_models.CreateVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_region_bandwidth):
            query['CrossRegionBandwidth'] = request.cross_region_bandwidth
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_description):
            query['EndpointDescription'] = request.endpoint_description
        if not DaraCore.is_null(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.protected_enabled):
            query['ProtectedEnabled'] = request.protected_enabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone):
            query['Zone'] = request.zone
        if not DaraCore.is_null(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        if not DaraCore.is_null(request.zone_private_ip_address_count):
            query['ZonePrivateIpAddressCount'] = request.zone_private_ip_address_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_endpoint(
        self,
        request: main_models.CreateVpcEndpointRequest,
    ) -> main_models.CreateVpcEndpointResponse:
        runtime = RuntimeOptions()
        return self.create_vpc_endpoint_with_options(request, runtime)

    async def create_vpc_endpoint_async(
        self,
        request: main_models.CreateVpcEndpointRequest,
    ) -> main_models.CreateVpcEndpointResponse:
        runtime = RuntimeOptions()
        return await self.create_vpc_endpoint_with_options_async(request, runtime)

    def create_vpc_endpoint_service_with_options(
        self,
        request: main_models.CreateVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.payer):
            query['Payer'] = request.payer
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        if not DaraCore.is_null(request.service_support_ipv_6):
            query['ServiceSupportIPv6'] = request.service_support_ipv_6
        if not DaraCore.is_null(request.supported_region_list):
            query['SupportedRegionList'] = request.supported_region_list
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_endpoint_service_with_options_async(
        self,
        request: main_models.CreateVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.payer):
            query['Payer'] = request.payer
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        if not DaraCore.is_null(request.service_support_ipv_6):
            query['ServiceSupportIPv6'] = request.service_support_ipv_6
        if not DaraCore.is_null(request.supported_region_list):
            query['SupportedRegionList'] = request.supported_region_list
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_endpoint_service(
        self,
        request: main_models.CreateVpcEndpointServiceRequest,
    ) -> main_models.CreateVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return self.create_vpc_endpoint_service_with_options(request, runtime)

    async def create_vpc_endpoint_service_async(
        self,
        request: main_models.CreateVpcEndpointServiceRequest,
    ) -> main_models.CreateVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return await self.create_vpc_endpoint_service_with_options_async(request, runtime)

    def delete_vpc_endpoint_with_options(
        self,
        request: main_models.DeleteVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_endpoint_with_options_async(
        self,
        request: main_models.DeleteVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_endpoint(
        self,
        request: main_models.DeleteVpcEndpointRequest,
    ) -> main_models.DeleteVpcEndpointResponse:
        runtime = RuntimeOptions()
        return self.delete_vpc_endpoint_with_options(request, runtime)

    async def delete_vpc_endpoint_async(
        self,
        request: main_models.DeleteVpcEndpointRequest,
    ) -> main_models.DeleteVpcEndpointResponse:
        runtime = RuntimeOptions()
        return await self.delete_vpc_endpoint_with_options_async(request, runtime)

    def delete_vpc_endpoint_service_with_options(
        self,
        request: main_models.DeleteVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_endpoint_service_with_options_async(
        self,
        request: main_models.DeleteVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_endpoint_service(
        self,
        request: main_models.DeleteVpcEndpointServiceRequest,
    ) -> main_models.DeleteVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return self.delete_vpc_endpoint_service_with_options(request, runtime)

    async def delete_vpc_endpoint_service_async(
        self,
        request: main_models.DeleteVpcEndpointServiceRequest,
    ) -> main_models.DeleteVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return await self.delete_vpc_endpoint_service_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_resource_from_vpc_endpoint_service_with_options(
        self,
        request: main_models.DetachResourceFromVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachResourceFromVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachResourceFromVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachResourceFromVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_resource_from_vpc_endpoint_service_with_options_async(
        self,
        request: main_models.DetachResourceFromVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachResourceFromVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachResourceFromVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachResourceFromVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_resource_from_vpc_endpoint_service(
        self,
        request: main_models.DetachResourceFromVpcEndpointServiceRequest,
    ) -> main_models.DetachResourceFromVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return self.detach_resource_from_vpc_endpoint_service_with_options(request, runtime)

    async def detach_resource_from_vpc_endpoint_service_async(
        self,
        request: main_models.DetachResourceFromVpcEndpointServiceRequest,
    ) -> main_models.DetachResourceFromVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return await self.detach_resource_from_vpc_endpoint_service_with_options_async(request, runtime)

    def detach_security_group_from_vpc_endpoint_with_options(
        self,
        request: main_models.DetachSecurityGroupFromVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachSecurityGroupFromVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachSecurityGroupFromVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachSecurityGroupFromVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_security_group_from_vpc_endpoint_with_options_async(
        self,
        request: main_models.DetachSecurityGroupFromVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachSecurityGroupFromVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachSecurityGroupFromVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachSecurityGroupFromVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_security_group_from_vpc_endpoint(
        self,
        request: main_models.DetachSecurityGroupFromVpcEndpointRequest,
    ) -> main_models.DetachSecurityGroupFromVpcEndpointResponse:
        runtime = RuntimeOptions()
        return self.detach_security_group_from_vpc_endpoint_with_options(request, runtime)

    async def detach_security_group_from_vpc_endpoint_async(
        self,
        request: main_models.DetachSecurityGroupFromVpcEndpointRequest,
    ) -> main_models.DetachSecurityGroupFromVpcEndpointResponse:
        runtime = RuntimeOptions()
        return await self.detach_security_group_from_vpc_endpoint_with_options_async(request, runtime)

    def disable_vpc_endpoint_connection_with_options(
        self,
        request: main_models.DisableVpcEndpointConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableVpcEndpointConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableVpcEndpointConnection',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableVpcEndpointConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_vpc_endpoint_connection_with_options_async(
        self,
        request: main_models.DisableVpcEndpointConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableVpcEndpointConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableVpcEndpointConnection',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableVpcEndpointConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_vpc_endpoint_connection(
        self,
        request: main_models.DisableVpcEndpointConnectionRequest,
    ) -> main_models.DisableVpcEndpointConnectionResponse:
        runtime = RuntimeOptions()
        return self.disable_vpc_endpoint_connection_with_options(request, runtime)

    async def disable_vpc_endpoint_connection_async(
        self,
        request: main_models.DisableVpcEndpointConnectionRequest,
    ) -> main_models.DisableVpcEndpointConnectionResponse:
        runtime = RuntimeOptions()
        return await self.disable_vpc_endpoint_connection_with_options_async(request, runtime)

    def disable_vpc_endpoint_zone_connection_with_options(
        self,
        request: main_models.DisableVpcEndpointZoneConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableVpcEndpointZoneConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replaced_resource):
            query['ReplacedResource'] = request.replaced_resource
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableVpcEndpointZoneConnection',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableVpcEndpointZoneConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_vpc_endpoint_zone_connection_with_options_async(
        self,
        request: main_models.DisableVpcEndpointZoneConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableVpcEndpointZoneConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replaced_resource):
            query['ReplacedResource'] = request.replaced_resource
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableVpcEndpointZoneConnection',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableVpcEndpointZoneConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_vpc_endpoint_zone_connection(
        self,
        request: main_models.DisableVpcEndpointZoneConnectionRequest,
    ) -> main_models.DisableVpcEndpointZoneConnectionResponse:
        runtime = RuntimeOptions()
        return self.disable_vpc_endpoint_zone_connection_with_options(request, runtime)

    async def disable_vpc_endpoint_zone_connection_async(
        self,
        request: main_models.DisableVpcEndpointZoneConnectionRequest,
    ) -> main_models.DisableVpcEndpointZoneConnectionResponse:
        runtime = RuntimeOptions()
        return await self.disable_vpc_endpoint_zone_connection_with_options_async(request, runtime)

    def enable_vpc_endpoint_connection_with_options(
        self,
        request: main_models.EnableVpcEndpointConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableVpcEndpointConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.traffic_control_mode):
            query['TrafficControlMode'] = request.traffic_control_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableVpcEndpointConnection',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableVpcEndpointConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_vpc_endpoint_connection_with_options_async(
        self,
        request: main_models.EnableVpcEndpointConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableVpcEndpointConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.traffic_control_mode):
            query['TrafficControlMode'] = request.traffic_control_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableVpcEndpointConnection',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableVpcEndpointConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_vpc_endpoint_connection(
        self,
        request: main_models.EnableVpcEndpointConnectionRequest,
    ) -> main_models.EnableVpcEndpointConnectionResponse:
        runtime = RuntimeOptions()
        return self.enable_vpc_endpoint_connection_with_options(request, runtime)

    async def enable_vpc_endpoint_connection_async(
        self,
        request: main_models.EnableVpcEndpointConnectionRequest,
    ) -> main_models.EnableVpcEndpointConnectionResponse:
        runtime = RuntimeOptions()
        return await self.enable_vpc_endpoint_connection_with_options_async(request, runtime)

    def enable_vpc_endpoint_zone_connection_with_options(
        self,
        request: main_models.EnableVpcEndpointZoneConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableVpcEndpointZoneConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableVpcEndpointZoneConnection',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableVpcEndpointZoneConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_vpc_endpoint_zone_connection_with_options_async(
        self,
        request: main_models.EnableVpcEndpointZoneConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableVpcEndpointZoneConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableVpcEndpointZoneConnection',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableVpcEndpointZoneConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_vpc_endpoint_zone_connection(
        self,
        request: main_models.EnableVpcEndpointZoneConnectionRequest,
    ) -> main_models.EnableVpcEndpointZoneConnectionResponse:
        runtime = RuntimeOptions()
        return self.enable_vpc_endpoint_zone_connection_with_options(request, runtime)

    async def enable_vpc_endpoint_zone_connection_async(
        self,
        request: main_models.EnableVpcEndpointZoneConnectionRequest,
    ) -> main_models.EnableVpcEndpointZoneConnectionResponse:
        runtime = RuntimeOptions()
        return await self.enable_vpc_endpoint_zone_connection_with_options_async(request, runtime)

    def get_vpc_endpoint_attribute_with_options(
        self,
        request: main_models.GetVpcEndpointAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpcEndpointAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVpcEndpointAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpcEndpointAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpc_endpoint_attribute_with_options_async(
        self,
        request: main_models.GetVpcEndpointAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpcEndpointAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVpcEndpointAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpcEndpointAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpc_endpoint_attribute(
        self,
        request: main_models.GetVpcEndpointAttributeRequest,
    ) -> main_models.GetVpcEndpointAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_vpc_endpoint_attribute_with_options(request, runtime)

    async def get_vpc_endpoint_attribute_async(
        self,
        request: main_models.GetVpcEndpointAttributeRequest,
    ) -> main_models.GetVpcEndpointAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_vpc_endpoint_attribute_with_options_async(request, runtime)

    def get_vpc_endpoint_service_attribute_with_options(
        self,
        request: main_models.GetVpcEndpointServiceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpcEndpointServiceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVpcEndpointServiceAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpcEndpointServiceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpc_endpoint_service_attribute_with_options_async(
        self,
        request: main_models.GetVpcEndpointServiceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpcEndpointServiceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVpcEndpointServiceAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpcEndpointServiceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpc_endpoint_service_attribute(
        self,
        request: main_models.GetVpcEndpointServiceAttributeRequest,
    ) -> main_models.GetVpcEndpointServiceAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_vpc_endpoint_service_attribute_with_options(request, runtime)

    async def get_vpc_endpoint_service_attribute_async(
        self,
        request: main_models.GetVpcEndpointServiceAttributeRequest,
    ) -> main_models.GetVpcEndpointServiceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_vpc_endpoint_service_attribute_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_vpc_endpoint_connections_with_options(
        self,
        request: main_models.ListVpcEndpointConnectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_status):
            query['ConnectionStatus'] = request.connection_status
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.endpoint_owner_id):
            query['EndpointOwnerId'] = request.endpoint_owner_id
        if not DaraCore.is_null(request.eni_id):
            query['EniId'] = request.eni_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replaced_resource_id):
            query['ReplacedResourceId'] = request.replaced_resource_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointConnections',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_connections_with_options_async(
        self,
        request: main_models.ListVpcEndpointConnectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_status):
            query['ConnectionStatus'] = request.connection_status
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.endpoint_owner_id):
            query['EndpointOwnerId'] = request.endpoint_owner_id
        if not DaraCore.is_null(request.eni_id):
            query['EniId'] = request.eni_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replaced_resource_id):
            query['ReplacedResourceId'] = request.replaced_resource_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointConnections',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_connections(
        self,
        request: main_models.ListVpcEndpointConnectionsRequest,
    ) -> main_models.ListVpcEndpointConnectionsResponse:
        runtime = RuntimeOptions()
        return self.list_vpc_endpoint_connections_with_options(request, runtime)

    async def list_vpc_endpoint_connections_async(
        self,
        request: main_models.ListVpcEndpointConnectionsRequest,
    ) -> main_models.ListVpcEndpointConnectionsResponse:
        runtime = RuntimeOptions()
        return await self.list_vpc_endpoint_connections_with_options_async(request, runtime)

    def list_vpc_endpoint_security_groups_with_options(
        self,
        request: main_models.ListVpcEndpointSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointSecurityGroups',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_security_groups_with_options_async(
        self,
        request: main_models.ListVpcEndpointSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointSecurityGroups',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_security_groups(
        self,
        request: main_models.ListVpcEndpointSecurityGroupsRequest,
    ) -> main_models.ListVpcEndpointSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_vpc_endpoint_security_groups_with_options(request, runtime)

    async def list_vpc_endpoint_security_groups_async(
        self,
        request: main_models.ListVpcEndpointSecurityGroupsRequest,
    ) -> main_models.ListVpcEndpointSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_vpc_endpoint_security_groups_with_options_async(request, runtime)

    def list_vpc_endpoint_service_resources_with_options(
        self,
        request: main_models.ListVpcEndpointServiceResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointServiceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointServiceResources',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointServiceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_service_resources_with_options_async(
        self,
        request: main_models.ListVpcEndpointServiceResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointServiceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointServiceResources',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointServiceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_service_resources(
        self,
        request: main_models.ListVpcEndpointServiceResourcesRequest,
    ) -> main_models.ListVpcEndpointServiceResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_vpc_endpoint_service_resources_with_options(request, runtime)

    async def list_vpc_endpoint_service_resources_async(
        self,
        request: main_models.ListVpcEndpointServiceResourcesRequest,
    ) -> main_models.ListVpcEndpointServiceResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_vpc_endpoint_service_resources_with_options_async(request, runtime)

    def list_vpc_endpoint_service_users_with_options(
        self,
        request: main_models.ListVpcEndpointServiceUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointServiceUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_list_type):
            query['UserListType'] = request.user_list_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointServiceUsers',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointServiceUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_service_users_with_options_async(
        self,
        request: main_models.ListVpcEndpointServiceUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointServiceUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_list_type):
            query['UserListType'] = request.user_list_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointServiceUsers',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointServiceUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_service_users(
        self,
        request: main_models.ListVpcEndpointServiceUsersRequest,
    ) -> main_models.ListVpcEndpointServiceUsersResponse:
        runtime = RuntimeOptions()
        return self.list_vpc_endpoint_service_users_with_options(request, runtime)

    async def list_vpc_endpoint_service_users_async(
        self,
        request: main_models.ListVpcEndpointServiceUsersRequest,
    ) -> main_models.ListVpcEndpointServiceUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_vpc_endpoint_service_users_with_options_async(request, runtime)

    def list_vpc_endpoint_services_with_options(
        self,
        request: main_models.ListVpcEndpointServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.service_business_status):
            query['ServiceBusinessStatus'] = request.service_business_status
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        if not DaraCore.is_null(request.service_status):
            query['ServiceStatus'] = request.service_status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointServices',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_services_with_options_async(
        self,
        request: main_models.ListVpcEndpointServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.service_business_status):
            query['ServiceBusinessStatus'] = request.service_business_status
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        if not DaraCore.is_null(request.service_status):
            query['ServiceStatus'] = request.service_status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointServices',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_services(
        self,
        request: main_models.ListVpcEndpointServicesRequest,
    ) -> main_models.ListVpcEndpointServicesResponse:
        runtime = RuntimeOptions()
        return self.list_vpc_endpoint_services_with_options(request, runtime)

    async def list_vpc_endpoint_services_async(
        self,
        request: main_models.ListVpcEndpointServicesRequest,
    ) -> main_models.ListVpcEndpointServicesResponse:
        runtime = RuntimeOptions()
        return await self.list_vpc_endpoint_services_with_options_async(request, runtime)

    def list_vpc_endpoint_services_by_end_user_with_options(
        self,
        request: main_models.ListVpcEndpointServicesByEndUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointServicesByEndUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointServicesByEndUser',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointServicesByEndUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_services_by_end_user_with_options_async(
        self,
        request: main_models.ListVpcEndpointServicesByEndUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointServicesByEndUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointServicesByEndUser',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointServicesByEndUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_services_by_end_user(
        self,
        request: main_models.ListVpcEndpointServicesByEndUserRequest,
    ) -> main_models.ListVpcEndpointServicesByEndUserResponse:
        runtime = RuntimeOptions()
        return self.list_vpc_endpoint_services_by_end_user_with_options(request, runtime)

    async def list_vpc_endpoint_services_by_end_user_async(
        self,
        request: main_models.ListVpcEndpointServicesByEndUserRequest,
    ) -> main_models.ListVpcEndpointServicesByEndUserResponse:
        runtime = RuntimeOptions()
        return await self.list_vpc_endpoint_services_by_end_user_with_options_async(request, runtime)

    def list_vpc_endpoint_zones_with_options(
        self,
        request: main_models.ListVpcEndpointZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointZones',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_zones_with_options_async(
        self,
        request: main_models.ListVpcEndpointZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpointZones',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_zones(
        self,
        request: main_models.ListVpcEndpointZonesRequest,
    ) -> main_models.ListVpcEndpointZonesResponse:
        runtime = RuntimeOptions()
        return self.list_vpc_endpoint_zones_with_options(request, runtime)

    async def list_vpc_endpoint_zones_async(
        self,
        request: main_models.ListVpcEndpointZonesRequest,
    ) -> main_models.ListVpcEndpointZonesResponse:
        runtime = RuntimeOptions()
        return await self.list_vpc_endpoint_zones_with_options_async(request, runtime)

    def list_vpc_endpoints_with_options(
        self,
        request: main_models.ListVpcEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.connection_status):
            query['ConnectionStatus'] = request.connection_status
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.endpoint_status):
            query['EndpointStatus'] = request.endpoint_status
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpoints',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoints_with_options_async(
        self,
        request: main_models.ListVpcEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.connection_status):
            query['ConnectionStatus'] = request.connection_status
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.endpoint_status):
            query['EndpointStatus'] = request.endpoint_status
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpoints',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoints(
        self,
        request: main_models.ListVpcEndpointsRequest,
    ) -> main_models.ListVpcEndpointsResponse:
        runtime = RuntimeOptions()
        return self.list_vpc_endpoints_with_options(request, runtime)

    async def list_vpc_endpoints_async(
        self,
        request: main_models.ListVpcEndpointsRequest,
    ) -> main_models.ListVpcEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.list_vpc_endpoints_with_options_async(request, runtime)

    def open_private_link_service_with_options(
        self,
        request: main_models.OpenPrivateLinkServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenPrivateLinkServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenPrivateLinkService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenPrivateLinkServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_private_link_service_with_options_async(
        self,
        request: main_models.OpenPrivateLinkServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenPrivateLinkServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenPrivateLinkService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenPrivateLinkServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_private_link_service(
        self,
        request: main_models.OpenPrivateLinkServiceRequest,
    ) -> main_models.OpenPrivateLinkServiceResponse:
        runtime = RuntimeOptions()
        return self.open_private_link_service_with_options(request, runtime)

    async def open_private_link_service_async(
        self,
        request: main_models.OpenPrivateLinkServiceRequest,
    ) -> main_models.OpenPrivateLinkServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_private_link_service_with_options_async(request, runtime)

    def remove_user_from_vpc_endpoint_service_with_options(
        self,
        request: main_models.RemoveUserFromVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserFromVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.user_arn):
            query['UserARN'] = request.user_arn
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserFromVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_from_vpc_endpoint_service_with_options_async(
        self,
        request: main_models.RemoveUserFromVpcEndpointServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserFromVpcEndpointServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.user_arn):
            query['UserARN'] = request.user_arn
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromVpcEndpointService',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserFromVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_from_vpc_endpoint_service(
        self,
        request: main_models.RemoveUserFromVpcEndpointServiceRequest,
    ) -> main_models.RemoveUserFromVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return self.remove_user_from_vpc_endpoint_service_with_options(request, runtime)

    async def remove_user_from_vpc_endpoint_service_async(
        self,
        request: main_models.RemoveUserFromVpcEndpointServiceRequest,
    ) -> main_models.RemoveUserFromVpcEndpointServiceResponse:
        runtime = RuntimeOptions()
        return await self.remove_user_from_vpc_endpoint_service_with_options_async(request, runtime)

    def remove_zone_from_vpc_endpoint_with_options(
        self,
        request: main_models.RemoveZoneFromVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveZoneFromVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveZoneFromVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveZoneFromVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_zone_from_vpc_endpoint_with_options_async(
        self,
        request: main_models.RemoveZoneFromVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveZoneFromVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveZoneFromVpcEndpoint',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveZoneFromVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_zone_from_vpc_endpoint(
        self,
        request: main_models.RemoveZoneFromVpcEndpointRequest,
    ) -> main_models.RemoveZoneFromVpcEndpointResponse:
        runtime = RuntimeOptions()
        return self.remove_zone_from_vpc_endpoint_with_options(request, runtime)

    async def remove_zone_from_vpc_endpoint_async(
        self,
        request: main_models.RemoveZoneFromVpcEndpointRequest,
    ) -> main_models.RemoveZoneFromVpcEndpointResponse:
        runtime = RuntimeOptions()
        return await self.remove_zone_from_vpc_endpoint_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            body_flat['TagKey'] = request.tag_key
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            body_flat['TagKey'] = request.tag_key
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_vpc_endpoint_attribute_with_options(
        self,
        request: main_models.UpdateVpcEndpointAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpcEndpointAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_region_bandwidth):
            query['CrossRegionBandwidth'] = request.cross_region_bandwidth
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_description):
            query['EndpointDescription'] = request.endpoint_description
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reset_policy):
            query['ResetPolicy'] = request.reset_policy
        if not DaraCore.is_null(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpcEndpointAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpcEndpointAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpc_endpoint_attribute_with_options_async(
        self,
        request: main_models.UpdateVpcEndpointAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpcEndpointAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_region_bandwidth):
            query['CrossRegionBandwidth'] = request.cross_region_bandwidth
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_description):
            query['EndpointDescription'] = request.endpoint_description
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reset_policy):
            query['ResetPolicy'] = request.reset_policy
        if not DaraCore.is_null(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpcEndpointAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpcEndpointAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpc_endpoint_attribute(
        self,
        request: main_models.UpdateVpcEndpointAttributeRequest,
    ) -> main_models.UpdateVpcEndpointAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_vpc_endpoint_attribute_with_options(request, runtime)

    async def update_vpc_endpoint_attribute_async(
        self,
        request: main_models.UpdateVpcEndpointAttributeRequest,
    ) -> main_models.UpdateVpcEndpointAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_vpc_endpoint_attribute_with_options_async(request, runtime)

    def update_vpc_endpoint_connection_attribute_with_options(
        self,
        request: main_models.UpdateVpcEndpointConnectionAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpcEndpointConnectionAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.traffic_control_mode):
            query['TrafficControlMode'] = request.traffic_control_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpcEndpointConnectionAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpcEndpointConnectionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpc_endpoint_connection_attribute_with_options_async(
        self,
        request: main_models.UpdateVpcEndpointConnectionAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpcEndpointConnectionAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.traffic_control_mode):
            query['TrafficControlMode'] = request.traffic_control_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpcEndpointConnectionAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpcEndpointConnectionAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpc_endpoint_connection_attribute(
        self,
        request: main_models.UpdateVpcEndpointConnectionAttributeRequest,
    ) -> main_models.UpdateVpcEndpointConnectionAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_vpc_endpoint_connection_attribute_with_options(request, runtime)

    async def update_vpc_endpoint_connection_attribute_async(
        self,
        request: main_models.UpdateVpcEndpointConnectionAttributeRequest,
    ) -> main_models.UpdateVpcEndpointConnectionAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_vpc_endpoint_connection_attribute_with_options_async(request, runtime)

    def update_vpc_endpoint_service_attribute_with_options(
        self,
        request: main_models.UpdateVpcEndpointServiceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpcEndpointServiceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_supported_region_set):
            query['AddSupportedRegionSet'] = request.add_supported_region_set
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connect_bandwidth):
            query['ConnectBandwidth'] = request.connect_bandwidth
        if not DaraCore.is_null(request.delete_supported_region_set):
            query['DeleteSupportedRegionSet'] = request.delete_supported_region_set
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_support_ipv_6):
            query['ServiceSupportIPv6'] = request.service_support_ipv_6
        if not DaraCore.is_null(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpcEndpointServiceAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpcEndpointServiceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpc_endpoint_service_attribute_with_options_async(
        self,
        request: main_models.UpdateVpcEndpointServiceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpcEndpointServiceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_supported_region_set):
            query['AddSupportedRegionSet'] = request.add_supported_region_set
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connect_bandwidth):
            query['ConnectBandwidth'] = request.connect_bandwidth
        if not DaraCore.is_null(request.delete_supported_region_set):
            query['DeleteSupportedRegionSet'] = request.delete_supported_region_set
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_support_ipv_6):
            query['ServiceSupportIPv6'] = request.service_support_ipv_6
        if not DaraCore.is_null(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpcEndpointServiceAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpcEndpointServiceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpc_endpoint_service_attribute(
        self,
        request: main_models.UpdateVpcEndpointServiceAttributeRequest,
    ) -> main_models.UpdateVpcEndpointServiceAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_vpc_endpoint_service_attribute_with_options(request, runtime)

    async def update_vpc_endpoint_service_attribute_async(
        self,
        request: main_models.UpdateVpcEndpointServiceAttributeRequest,
    ) -> main_models.UpdateVpcEndpointServiceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_vpc_endpoint_service_attribute_with_options_async(request, runtime)

    def update_vpc_endpoint_service_resource_attribute_with_options(
        self,
        request: main_models.UpdateVpcEndpointServiceResourceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpcEndpointServiceResourceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_allocated_enabled):
            query['AutoAllocatedEnabled'] = request.auto_allocated_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpcEndpointServiceResourceAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpcEndpointServiceResourceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpc_endpoint_service_resource_attribute_with_options_async(
        self,
        request: main_models.UpdateVpcEndpointServiceResourceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpcEndpointServiceResourceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_allocated_enabled):
            query['AutoAllocatedEnabled'] = request.auto_allocated_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpcEndpointServiceResourceAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpcEndpointServiceResourceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpc_endpoint_service_resource_attribute(
        self,
        request: main_models.UpdateVpcEndpointServiceResourceAttributeRequest,
    ) -> main_models.UpdateVpcEndpointServiceResourceAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_vpc_endpoint_service_resource_attribute_with_options(request, runtime)

    async def update_vpc_endpoint_service_resource_attribute_async(
        self,
        request: main_models.UpdateVpcEndpointServiceResourceAttributeRequest,
    ) -> main_models.UpdateVpcEndpointServiceResourceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_vpc_endpoint_service_resource_attribute_with_options_async(request, runtime)

    def update_vpc_endpoint_zone_connection_resource_attribute_with_options(
        self,
        request: main_models.UpdateVpcEndpointZoneConnectionResourceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_allocate_mode):
            query['ResourceAllocateMode'] = request.resource_allocate_mode
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_replace_mode):
            query['ResourceReplaceMode'] = request.resource_replace_mode
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpcEndpointZoneConnectionResourceAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpc_endpoint_zone_connection_resource_attribute_with_options_async(
        self,
        request: main_models.UpdateVpcEndpointZoneConnectionResourceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_allocate_mode):
            query['ResourceAllocateMode'] = request.resource_allocate_mode
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_replace_mode):
            query['ResourceReplaceMode'] = request.resource_replace_mode
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpcEndpointZoneConnectionResourceAttribute',
            version = '2020-04-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpc_endpoint_zone_connection_resource_attribute(
        self,
        request: main_models.UpdateVpcEndpointZoneConnectionResourceAttributeRequest,
    ) -> main_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_vpc_endpoint_zone_connection_resource_attribute_with_options(request, runtime)

    async def update_vpc_endpoint_zone_connection_resource_attribute_async(
        self,
        request: main_models.UpdateVpcEndpointZoneConnectionResourceAttributeRequest,
    ) -> main_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_vpc_endpoint_zone_connection_resource_attribute_with_options_async(request, runtime)
