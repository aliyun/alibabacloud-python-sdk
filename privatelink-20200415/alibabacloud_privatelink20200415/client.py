# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_privatelink20200415 import models as privatelink_20200415_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_user_to_vpc_endpoint_service_with_options(
        self,
        request: privatelink_20200415_models.AddUserToVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.AddUserToVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.AddUserToVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_vpc_endpoint_service_with_options_async(
        self,
        request: privatelink_20200415_models.AddUserToVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.AddUserToVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.AddUserToVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_vpc_endpoint_service(
        self,
        request: privatelink_20200415_models.AddUserToVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.AddUserToVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_vpc_endpoint_service_with_options(request, runtime)

    async def add_user_to_vpc_endpoint_service_async(
        self,
        request: privatelink_20200415_models.AddUserToVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.AddUserToVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_vpc_endpoint_service_with_options_async(request, runtime)

    def add_zone_to_vpc_endpoint_with_options(
        self,
        request: privatelink_20200415_models.AddZoneToVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.AddZoneToVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddZoneToVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.AddZoneToVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_zone_to_vpc_endpoint_with_options_async(
        self,
        request: privatelink_20200415_models.AddZoneToVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.AddZoneToVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddZoneToVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.AddZoneToVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_zone_to_vpc_endpoint(
        self,
        request: privatelink_20200415_models.AddZoneToVpcEndpointRequest,
    ) -> privatelink_20200415_models.AddZoneToVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_zone_to_vpc_endpoint_with_options(request, runtime)

    async def add_zone_to_vpc_endpoint_async(
        self,
        request: privatelink_20200415_models.AddZoneToVpcEndpointRequest,
    ) -> privatelink_20200415_models.AddZoneToVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_zone_to_vpc_endpoint_with_options_async(request, runtime)

    def attach_resource_to_vpc_endpoint_service_with_options(
        self,
        request: privatelink_20200415_models.AttachResourceToVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.AttachResourceToVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachResourceToVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.AttachResourceToVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_resource_to_vpc_endpoint_service_with_options_async(
        self,
        request: privatelink_20200415_models.AttachResourceToVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.AttachResourceToVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachResourceToVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.AttachResourceToVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_resource_to_vpc_endpoint_service(
        self,
        request: privatelink_20200415_models.AttachResourceToVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.AttachResourceToVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_resource_to_vpc_endpoint_service_with_options(request, runtime)

    async def attach_resource_to_vpc_endpoint_service_async(
        self,
        request: privatelink_20200415_models.AttachResourceToVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.AttachResourceToVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_resource_to_vpc_endpoint_service_with_options_async(request, runtime)

    def attach_security_group_to_vpc_endpoint_with_options(
        self,
        request: privatelink_20200415_models.AttachSecurityGroupToVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.AttachSecurityGroupToVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachSecurityGroupToVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.AttachSecurityGroupToVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_security_group_to_vpc_endpoint_with_options_async(
        self,
        request: privatelink_20200415_models.AttachSecurityGroupToVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.AttachSecurityGroupToVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachSecurityGroupToVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.AttachSecurityGroupToVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_security_group_to_vpc_endpoint(
        self,
        request: privatelink_20200415_models.AttachSecurityGroupToVpcEndpointRequest,
    ) -> privatelink_20200415_models.AttachSecurityGroupToVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_security_group_to_vpc_endpoint_with_options(request, runtime)

    async def attach_security_group_to_vpc_endpoint_async(
        self,
        request: privatelink_20200415_models.AttachSecurityGroupToVpcEndpointRequest,
    ) -> privatelink_20200415_models.AttachSecurityGroupToVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_security_group_to_vpc_endpoint_with_options_async(request, runtime)

    def check_product_open_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.CheckProductOpenResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CheckProductOpen',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.CheckProductOpenResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_product_open_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.CheckProductOpenResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CheckProductOpen',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.CheckProductOpenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_product_open(self) -> privatelink_20200415_models.CheckProductOpenResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_product_open_with_options(runtime)

    async def check_product_open_async(self) -> privatelink_20200415_models.CheckProductOpenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_product_open_with_options_async(runtime)

    def create_vpc_endpoint_with_options(
        self,
        request: privatelink_20200415_models.CreateVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.CreateVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_description):
            query['EndpointDescription'] = request.endpoint_description
        if not UtilClient.is_unset(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.protected_enabled):
            query['ProtectedEnabled'] = request.protected_enabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone):
            query['Zone'] = request.zone
        if not UtilClient.is_unset(request.zone_private_ip_address_count):
            query['ZonePrivateIpAddressCount'] = request.zone_private_ip_address_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.CreateVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_endpoint_with_options_async(
        self,
        request: privatelink_20200415_models.CreateVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.CreateVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_description):
            query['EndpointDescription'] = request.endpoint_description
        if not UtilClient.is_unset(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.protected_enabled):
            query['ProtectedEnabled'] = request.protected_enabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone):
            query['Zone'] = request.zone
        if not UtilClient.is_unset(request.zone_private_ip_address_count):
            query['ZonePrivateIpAddressCount'] = request.zone_private_ip_address_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.CreateVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_endpoint(
        self,
        request: privatelink_20200415_models.CreateVpcEndpointRequest,
    ) -> privatelink_20200415_models.CreateVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_endpoint_with_options(request, runtime)

    async def create_vpc_endpoint_async(
        self,
        request: privatelink_20200415_models.CreateVpcEndpointRequest,
    ) -> privatelink_20200415_models.CreateVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_endpoint_with_options_async(request, runtime)

    def create_vpc_endpoint_service_with_options(
        self,
        request: privatelink_20200415_models.CreateVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.CreateVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.payer):
            query['Payer'] = request.payer
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        if not UtilClient.is_unset(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.CreateVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_endpoint_service_with_options_async(
        self,
        request: privatelink_20200415_models.CreateVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.CreateVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.payer):
            query['Payer'] = request.payer
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        if not UtilClient.is_unset(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.CreateVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_endpoint_service(
        self,
        request: privatelink_20200415_models.CreateVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.CreateVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_endpoint_service_with_options(request, runtime)

    async def create_vpc_endpoint_service_async(
        self,
        request: privatelink_20200415_models.CreateVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.CreateVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_endpoint_service_with_options_async(request, runtime)

    def delete_vpc_endpoint_with_options(
        self,
        request: privatelink_20200415_models.DeleteVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DeleteVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DeleteVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_endpoint_with_options_async(
        self,
        request: privatelink_20200415_models.DeleteVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DeleteVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DeleteVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_endpoint(
        self,
        request: privatelink_20200415_models.DeleteVpcEndpointRequest,
    ) -> privatelink_20200415_models.DeleteVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_endpoint_with_options(request, runtime)

    async def delete_vpc_endpoint_async(
        self,
        request: privatelink_20200415_models.DeleteVpcEndpointRequest,
    ) -> privatelink_20200415_models.DeleteVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_endpoint_with_options_async(request, runtime)

    def delete_vpc_endpoint_service_with_options(
        self,
        request: privatelink_20200415_models.DeleteVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DeleteVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DeleteVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_endpoint_service_with_options_async(
        self,
        request: privatelink_20200415_models.DeleteVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DeleteVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DeleteVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_endpoint_service(
        self,
        request: privatelink_20200415_models.DeleteVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.DeleteVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_endpoint_service_with_options(request, runtime)

    async def delete_vpc_endpoint_service_async(
        self,
        request: privatelink_20200415_models.DeleteVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.DeleteVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_endpoint_service_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: privatelink_20200415_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: privatelink_20200415_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: privatelink_20200415_models.DescribeRegionsRequest,
    ) -> privatelink_20200415_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: privatelink_20200415_models.DescribeRegionsRequest,
    ) -> privatelink_20200415_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: privatelink_20200415_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: privatelink_20200415_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: privatelink_20200415_models.DescribeZonesRequest,
    ) -> privatelink_20200415_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: privatelink_20200415_models.DescribeZonesRequest,
    ) -> privatelink_20200415_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_resource_from_vpc_endpoint_service_with_options(
        self,
        request: privatelink_20200415_models.DetachResourceFromVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DetachResourceFromVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachResourceFromVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DetachResourceFromVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_resource_from_vpc_endpoint_service_with_options_async(
        self,
        request: privatelink_20200415_models.DetachResourceFromVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DetachResourceFromVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachResourceFromVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DetachResourceFromVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_resource_from_vpc_endpoint_service(
        self,
        request: privatelink_20200415_models.DetachResourceFromVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.DetachResourceFromVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_resource_from_vpc_endpoint_service_with_options(request, runtime)

    async def detach_resource_from_vpc_endpoint_service_async(
        self,
        request: privatelink_20200415_models.DetachResourceFromVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.DetachResourceFromVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_resource_from_vpc_endpoint_service_with_options_async(request, runtime)

    def detach_security_group_from_vpc_endpoint_with_options(
        self,
        request: privatelink_20200415_models.DetachSecurityGroupFromVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DetachSecurityGroupFromVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachSecurityGroupFromVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DetachSecurityGroupFromVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_security_group_from_vpc_endpoint_with_options_async(
        self,
        request: privatelink_20200415_models.DetachSecurityGroupFromVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DetachSecurityGroupFromVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachSecurityGroupFromVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DetachSecurityGroupFromVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_security_group_from_vpc_endpoint(
        self,
        request: privatelink_20200415_models.DetachSecurityGroupFromVpcEndpointRequest,
    ) -> privatelink_20200415_models.DetachSecurityGroupFromVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_security_group_from_vpc_endpoint_with_options(request, runtime)

    async def detach_security_group_from_vpc_endpoint_async(
        self,
        request: privatelink_20200415_models.DetachSecurityGroupFromVpcEndpointRequest,
    ) -> privatelink_20200415_models.DetachSecurityGroupFromVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_security_group_from_vpc_endpoint_with_options_async(request, runtime)

    def disable_vpc_endpoint_connection_with_options(
        self,
        request: privatelink_20200415_models.DisableVpcEndpointConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DisableVpcEndpointConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableVpcEndpointConnection',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DisableVpcEndpointConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_vpc_endpoint_connection_with_options_async(
        self,
        request: privatelink_20200415_models.DisableVpcEndpointConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DisableVpcEndpointConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableVpcEndpointConnection',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DisableVpcEndpointConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_vpc_endpoint_connection(
        self,
        request: privatelink_20200415_models.DisableVpcEndpointConnectionRequest,
    ) -> privatelink_20200415_models.DisableVpcEndpointConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_vpc_endpoint_connection_with_options(request, runtime)

    async def disable_vpc_endpoint_connection_async(
        self,
        request: privatelink_20200415_models.DisableVpcEndpointConnectionRequest,
    ) -> privatelink_20200415_models.DisableVpcEndpointConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_vpc_endpoint_connection_with_options_async(request, runtime)

    def disable_vpc_endpoint_zone_connection_with_options(
        self,
        request: privatelink_20200415_models.DisableVpcEndpointZoneConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DisableVpcEndpointZoneConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replaced_resource):
            query['ReplacedResource'] = request.replaced_resource
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableVpcEndpointZoneConnection',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DisableVpcEndpointZoneConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_vpc_endpoint_zone_connection_with_options_async(
        self,
        request: privatelink_20200415_models.DisableVpcEndpointZoneConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.DisableVpcEndpointZoneConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replaced_resource):
            query['ReplacedResource'] = request.replaced_resource
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableVpcEndpointZoneConnection',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.DisableVpcEndpointZoneConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_vpc_endpoint_zone_connection(
        self,
        request: privatelink_20200415_models.DisableVpcEndpointZoneConnectionRequest,
    ) -> privatelink_20200415_models.DisableVpcEndpointZoneConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_vpc_endpoint_zone_connection_with_options(request, runtime)

    async def disable_vpc_endpoint_zone_connection_async(
        self,
        request: privatelink_20200415_models.DisableVpcEndpointZoneConnectionRequest,
    ) -> privatelink_20200415_models.DisableVpcEndpointZoneConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_vpc_endpoint_zone_connection_with_options_async(request, runtime)

    def enable_vpc_endpoint_connection_with_options(
        self,
        request: privatelink_20200415_models.EnableVpcEndpointConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.EnableVpcEndpointConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableVpcEndpointConnection',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.EnableVpcEndpointConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_vpc_endpoint_connection_with_options_async(
        self,
        request: privatelink_20200415_models.EnableVpcEndpointConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.EnableVpcEndpointConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableVpcEndpointConnection',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.EnableVpcEndpointConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_vpc_endpoint_connection(
        self,
        request: privatelink_20200415_models.EnableVpcEndpointConnectionRequest,
    ) -> privatelink_20200415_models.EnableVpcEndpointConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_vpc_endpoint_connection_with_options(request, runtime)

    async def enable_vpc_endpoint_connection_async(
        self,
        request: privatelink_20200415_models.EnableVpcEndpointConnectionRequest,
    ) -> privatelink_20200415_models.EnableVpcEndpointConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_vpc_endpoint_connection_with_options_async(request, runtime)

    def enable_vpc_endpoint_zone_connection_with_options(
        self,
        request: privatelink_20200415_models.EnableVpcEndpointZoneConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.EnableVpcEndpointZoneConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableVpcEndpointZoneConnection',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.EnableVpcEndpointZoneConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_vpc_endpoint_zone_connection_with_options_async(
        self,
        request: privatelink_20200415_models.EnableVpcEndpointZoneConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.EnableVpcEndpointZoneConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableVpcEndpointZoneConnection',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.EnableVpcEndpointZoneConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_vpc_endpoint_zone_connection(
        self,
        request: privatelink_20200415_models.EnableVpcEndpointZoneConnectionRequest,
    ) -> privatelink_20200415_models.EnableVpcEndpointZoneConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_vpc_endpoint_zone_connection_with_options(request, runtime)

    async def enable_vpc_endpoint_zone_connection_async(
        self,
        request: privatelink_20200415_models.EnableVpcEndpointZoneConnectionRequest,
    ) -> privatelink_20200415_models.EnableVpcEndpointZoneConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_vpc_endpoint_zone_connection_with_options_async(request, runtime)

    def get_vpc_endpoint_attribute_with_options(
        self,
        request: privatelink_20200415_models.GetVpcEndpointAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.GetVpcEndpointAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVpcEndpointAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.GetVpcEndpointAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpc_endpoint_attribute_with_options_async(
        self,
        request: privatelink_20200415_models.GetVpcEndpointAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.GetVpcEndpointAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVpcEndpointAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.GetVpcEndpointAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpc_endpoint_attribute(
        self,
        request: privatelink_20200415_models.GetVpcEndpointAttributeRequest,
    ) -> privatelink_20200415_models.GetVpcEndpointAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vpc_endpoint_attribute_with_options(request, runtime)

    async def get_vpc_endpoint_attribute_async(
        self,
        request: privatelink_20200415_models.GetVpcEndpointAttributeRequest,
    ) -> privatelink_20200415_models.GetVpcEndpointAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vpc_endpoint_attribute_with_options_async(request, runtime)

    def get_vpc_endpoint_service_attribute_with_options(
        self,
        request: privatelink_20200415_models.GetVpcEndpointServiceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.GetVpcEndpointServiceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVpcEndpointServiceAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.GetVpcEndpointServiceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpc_endpoint_service_attribute_with_options_async(
        self,
        request: privatelink_20200415_models.GetVpcEndpointServiceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.GetVpcEndpointServiceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVpcEndpointServiceAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.GetVpcEndpointServiceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpc_endpoint_service_attribute(
        self,
        request: privatelink_20200415_models.GetVpcEndpointServiceAttributeRequest,
    ) -> privatelink_20200415_models.GetVpcEndpointServiceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vpc_endpoint_service_attribute_with_options(request, runtime)

    async def get_vpc_endpoint_service_attribute_async(
        self,
        request: privatelink_20200415_models.GetVpcEndpointServiceAttributeRequest,
    ) -> privatelink_20200415_models.GetVpcEndpointServiceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vpc_endpoint_service_attribute_with_options_async(request, runtime)

    def list_vpc_endpoint_connections_with_options(
        self,
        request: privatelink_20200415_models.ListVpcEndpointConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointConnectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_status):
            query['ConnectionStatus'] = request.connection_status
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.endpoint_owner_id):
            query['EndpointOwnerId'] = request.endpoint_owner_id
        if not UtilClient.is_unset(request.eni_id):
            query['EniId'] = request.eni_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replaced_resource_id):
            query['ReplacedResourceId'] = request.replaced_resource_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointConnections',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_connections_with_options_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointConnectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_status):
            query['ConnectionStatus'] = request.connection_status
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.endpoint_owner_id):
            query['EndpointOwnerId'] = request.endpoint_owner_id
        if not UtilClient.is_unset(request.eni_id):
            query['EniId'] = request.eni_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replaced_resource_id):
            query['ReplacedResourceId'] = request.replaced_resource_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointConnections',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_connections(
        self,
        request: privatelink_20200415_models.ListVpcEndpointConnectionsRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_endpoint_connections_with_options(request, runtime)

    async def list_vpc_endpoint_connections_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointConnectionsRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_endpoint_connections_with_options_async(request, runtime)

    def list_vpc_endpoint_security_groups_with_options(
        self,
        request: privatelink_20200415_models.ListVpcEndpointSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointSecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointSecurityGroups',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_security_groups_with_options_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointSecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointSecurityGroups',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_security_groups(
        self,
        request: privatelink_20200415_models.ListVpcEndpointSecurityGroupsRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_endpoint_security_groups_with_options(request, runtime)

    async def list_vpc_endpoint_security_groups_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointSecurityGroupsRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_endpoint_security_groups_with_options_async(request, runtime)

    def list_vpc_endpoint_service_resources_with_options(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServiceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointServiceResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointServiceResources',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointServiceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_service_resources_with_options_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServiceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointServiceResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointServiceResources',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointServiceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_service_resources(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServiceResourcesRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointServiceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_endpoint_service_resources_with_options(request, runtime)

    async def list_vpc_endpoint_service_resources_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServiceResourcesRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointServiceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_endpoint_service_resources_with_options_async(request, runtime)

    def list_vpc_endpoint_service_users_with_options(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServiceUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointServiceUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointServiceUsers',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointServiceUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_service_users_with_options_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServiceUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointServiceUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointServiceUsers',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointServiceUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_service_users(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServiceUsersRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointServiceUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_endpoint_service_users_with_options(request, runtime)

    async def list_vpc_endpoint_service_users_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServiceUsersRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointServiceUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_endpoint_service_users_with_options_async(request, runtime)

    def list_vpc_endpoint_services_with_options(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_business_status):
            query['ServiceBusinessStatus'] = request.service_business_status
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        if not UtilClient.is_unset(request.service_status):
            query['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointServices',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_services_with_options_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_business_status):
            query['ServiceBusinessStatus'] = request.service_business_status
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_resource_type):
            query['ServiceResourceType'] = request.service_resource_type
        if not UtilClient.is_unset(request.service_status):
            query['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointServices',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_services(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServicesRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_endpoint_services_with_options(request, runtime)

    async def list_vpc_endpoint_services_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServicesRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_endpoint_services_with_options_async(request, runtime)

    def list_vpc_endpoint_services_by_end_user_with_options(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServicesByEndUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointServicesByEndUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointServicesByEndUser',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointServicesByEndUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_services_by_end_user_with_options_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServicesByEndUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointServicesByEndUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointServicesByEndUser',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointServicesByEndUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_services_by_end_user(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServicesByEndUserRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointServicesByEndUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_endpoint_services_by_end_user_with_options(request, runtime)

    async def list_vpc_endpoint_services_by_end_user_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointServicesByEndUserRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointServicesByEndUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_endpoint_services_by_end_user_with_options_async(request, runtime)

    def list_vpc_endpoint_zones_with_options(
        self,
        request: privatelink_20200415_models.ListVpcEndpointZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointZones',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoint_zones_with_options_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpointZones',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoint_zones(
        self,
        request: privatelink_20200415_models.ListVpcEndpointZonesRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_endpoint_zones_with_options(request, runtime)

    async def list_vpc_endpoint_zones_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointZonesRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_endpoint_zones_with_options_async(request, runtime)

    def list_vpc_endpoints_with_options(
        self,
        request: privatelink_20200415_models.ListVpcEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_status):
            query['ConnectionStatus'] = request.connection_status
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not UtilClient.is_unset(request.endpoint_status):
            query['EndpointStatus'] = request.endpoint_status
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpoints',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoints_with_options_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.ListVpcEndpointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_status):
            query['ConnectionStatus'] = request.connection_status
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not UtilClient.is_unset(request.endpoint_status):
            query['EndpointStatus'] = request.endpoint_status
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpoints',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.ListVpcEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoints(
        self,
        request: privatelink_20200415_models.ListVpcEndpointsRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_endpoints_with_options(request, runtime)

    async def list_vpc_endpoints_async(
        self,
        request: privatelink_20200415_models.ListVpcEndpointsRequest,
    ) -> privatelink_20200415_models.ListVpcEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_endpoints_with_options_async(request, runtime)

    def open_private_link_service_with_options(
        self,
        request: privatelink_20200415_models.OpenPrivateLinkServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.OpenPrivateLinkServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenPrivateLinkService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.OpenPrivateLinkServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_private_link_service_with_options_async(
        self,
        request: privatelink_20200415_models.OpenPrivateLinkServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.OpenPrivateLinkServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenPrivateLinkService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.OpenPrivateLinkServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_private_link_service(
        self,
        request: privatelink_20200415_models.OpenPrivateLinkServiceRequest,
    ) -> privatelink_20200415_models.OpenPrivateLinkServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_private_link_service_with_options(request, runtime)

    async def open_private_link_service_async(
        self,
        request: privatelink_20200415_models.OpenPrivateLinkServiceRequest,
    ) -> privatelink_20200415_models.OpenPrivateLinkServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_private_link_service_with_options_async(request, runtime)

    def remove_user_from_vpc_endpoint_service_with_options(
        self,
        request: privatelink_20200415_models.RemoveUserFromVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.RemoveUserFromVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.RemoveUserFromVpcEndpointServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_from_vpc_endpoint_service_with_options_async(
        self,
        request: privatelink_20200415_models.RemoveUserFromVpcEndpointServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.RemoveUserFromVpcEndpointServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromVpcEndpointService',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.RemoveUserFromVpcEndpointServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_from_vpc_endpoint_service(
        self,
        request: privatelink_20200415_models.RemoveUserFromVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.RemoveUserFromVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_vpc_endpoint_service_with_options(request, runtime)

    async def remove_user_from_vpc_endpoint_service_async(
        self,
        request: privatelink_20200415_models.RemoveUserFromVpcEndpointServiceRequest,
    ) -> privatelink_20200415_models.RemoveUserFromVpcEndpointServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_from_vpc_endpoint_service_with_options_async(request, runtime)

    def remove_zone_from_vpc_endpoint_with_options(
        self,
        request: privatelink_20200415_models.RemoveZoneFromVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.RemoveZoneFromVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveZoneFromVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.RemoveZoneFromVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_zone_from_vpc_endpoint_with_options_async(
        self,
        request: privatelink_20200415_models.RemoveZoneFromVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.RemoveZoneFromVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveZoneFromVpcEndpoint',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.RemoveZoneFromVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_zone_from_vpc_endpoint(
        self,
        request: privatelink_20200415_models.RemoveZoneFromVpcEndpointRequest,
    ) -> privatelink_20200415_models.RemoveZoneFromVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_zone_from_vpc_endpoint_with_options(request, runtime)

    async def remove_zone_from_vpc_endpoint_async(
        self,
        request: privatelink_20200415_models.RemoveZoneFromVpcEndpointRequest,
    ) -> privatelink_20200415_models.RemoveZoneFromVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_zone_from_vpc_endpoint_with_options_async(request, runtime)

    def update_vpc_endpoint_attribute_with_options(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.UpdateVpcEndpointAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_description):
            query['EndpointDescription'] = request.endpoint_description
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVpcEndpointAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.UpdateVpcEndpointAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpc_endpoint_attribute_with_options_async(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.UpdateVpcEndpointAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_description):
            query['EndpointDescription'] = request.endpoint_description
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.endpoint_name):
            query['EndpointName'] = request.endpoint_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVpcEndpointAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.UpdateVpcEndpointAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpc_endpoint_attribute(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointAttributeRequest,
    ) -> privatelink_20200415_models.UpdateVpcEndpointAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vpc_endpoint_attribute_with_options(request, runtime)

    async def update_vpc_endpoint_attribute_async(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointAttributeRequest,
    ) -> privatelink_20200415_models.UpdateVpcEndpointAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vpc_endpoint_attribute_with_options_async(request, runtime)

    def update_vpc_endpoint_connection_attribute_with_options(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.UpdateVpcEndpointConnectionAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVpcEndpointConnectionAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.UpdateVpcEndpointConnectionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpc_endpoint_connection_attribute_with_options_async(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.UpdateVpcEndpointConnectionAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVpcEndpointConnectionAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.UpdateVpcEndpointConnectionAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpc_endpoint_connection_attribute(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointConnectionAttributeRequest,
    ) -> privatelink_20200415_models.UpdateVpcEndpointConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vpc_endpoint_connection_attribute_with_options(request, runtime)

    async def update_vpc_endpoint_connection_attribute_async(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointConnectionAttributeRequest,
    ) -> privatelink_20200415_models.UpdateVpcEndpointConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vpc_endpoint_connection_attribute_with_options_async(request, runtime)

    def update_vpc_endpoint_service_attribute_with_options(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointServiceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.UpdateVpcEndpointServiceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connect_bandwidth):
            query['ConnectBandwidth'] = request.connect_bandwidth
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVpcEndpointServiceAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.UpdateVpcEndpointServiceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpc_endpoint_service_attribute_with_options_async(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointServiceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.UpdateVpcEndpointServiceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_accept_enabled):
            query['AutoAcceptEnabled'] = request.auto_accept_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connect_bandwidth):
            query['ConnectBandwidth'] = request.connect_bandwidth
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.zone_affinity_enabled):
            query['ZoneAffinityEnabled'] = request.zone_affinity_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVpcEndpointServiceAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.UpdateVpcEndpointServiceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpc_endpoint_service_attribute(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointServiceAttributeRequest,
    ) -> privatelink_20200415_models.UpdateVpcEndpointServiceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vpc_endpoint_service_attribute_with_options(request, runtime)

    async def update_vpc_endpoint_service_attribute_async(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointServiceAttributeRequest,
    ) -> privatelink_20200415_models.UpdateVpcEndpointServiceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vpc_endpoint_service_attribute_with_options_async(request, runtime)

    def update_vpc_endpoint_service_resource_attribute_with_options(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointServiceResourceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.UpdateVpcEndpointServiceResourceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_allocated_enabled):
            query['AutoAllocatedEnabled'] = request.auto_allocated_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVpcEndpointServiceResourceAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.UpdateVpcEndpointServiceResourceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpc_endpoint_service_resource_attribute_with_options_async(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointServiceResourceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.UpdateVpcEndpointServiceResourceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_allocated_enabled):
            query['AutoAllocatedEnabled'] = request.auto_allocated_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVpcEndpointServiceResourceAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.UpdateVpcEndpointServiceResourceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpc_endpoint_service_resource_attribute(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointServiceResourceAttributeRequest,
    ) -> privatelink_20200415_models.UpdateVpcEndpointServiceResourceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vpc_endpoint_service_resource_attribute_with_options(request, runtime)

    async def update_vpc_endpoint_service_resource_attribute_async(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointServiceResourceAttributeRequest,
    ) -> privatelink_20200415_models.UpdateVpcEndpointServiceResourceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vpc_endpoint_service_resource_attribute_with_options_async(request, runtime)

    def update_vpc_endpoint_zone_connection_resource_attribute_with_options(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointZoneConnectionResourceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_allocate_mode):
            query['ResourceAllocateMode'] = request.resource_allocate_mode
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_replace_mode):
            query['ResourceReplaceMode'] = request.resource_replace_mode
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVpcEndpointZoneConnectionResourceAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpc_endpoint_zone_connection_resource_attribute_with_options_async(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointZoneConnectionResourceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> privatelink_20200415_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_allocate_mode):
            query['ResourceAllocateMode'] = request.resource_allocate_mode
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_replace_mode):
            query['ResourceReplaceMode'] = request.resource_replace_mode
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVpcEndpointZoneConnectionResourceAttribute',
            version='2020-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            privatelink_20200415_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpc_endpoint_zone_connection_resource_attribute(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointZoneConnectionResourceAttributeRequest,
    ) -> privatelink_20200415_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vpc_endpoint_zone_connection_resource_attribute_with_options(request, runtime)

    async def update_vpc_endpoint_zone_connection_resource_attribute_async(
        self,
        request: privatelink_20200415_models.UpdateVpcEndpointZoneConnectionResourceAttributeRequest,
    ) -> privatelink_20200415_models.UpdateVpcEndpointZoneConnectionResourceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vpc_endpoint_zone_connection_resource_attribute_with_options_async(request, runtime)
