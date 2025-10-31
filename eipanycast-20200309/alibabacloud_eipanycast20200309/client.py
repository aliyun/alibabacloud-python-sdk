# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eipanycast20200309 import models as eipanycast_20200309_models
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
        self._endpoint = self.get_endpoint('eipanycast', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_anycast_eip_address_with_options(
        self,
        request: eipanycast_20200309_models.AllocateAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.AllocateAnycastEipAddressResponse:
        """
        @summary Creates an Anycast elastic IP address (Anycast EIP).
        
        @param request: AllocateAnycastEipAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateAnycastEipAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.AllocateAnycastEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_anycast_eip_address_with_options_async(
        self,
        request: eipanycast_20200309_models.AllocateAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.AllocateAnycastEipAddressResponse:
        """
        @summary Creates an Anycast elastic IP address (Anycast EIP).
        
        @param request: AllocateAnycastEipAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateAnycastEipAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.AllocateAnycastEipAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_anycast_eip_address(
        self,
        request: eipanycast_20200309_models.AllocateAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.AllocateAnycastEipAddressResponse:
        """
        @summary Creates an Anycast elastic IP address (Anycast EIP).
        
        @param request: AllocateAnycastEipAddressRequest
        @return: AllocateAnycastEipAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_anycast_eip_address_with_options(request, runtime)

    async def allocate_anycast_eip_address_async(
        self,
        request: eipanycast_20200309_models.AllocateAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.AllocateAnycastEipAddressResponse:
        """
        @summary Creates an Anycast elastic IP address (Anycast EIP).
        
        @param request: AllocateAnycastEipAddressRequest
        @return: AllocateAnycastEipAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_anycast_eip_address_with_options_async(request, runtime)

    def associate_anycast_eip_address_with_options(
        self,
        request: eipanycast_20200309_models.AssociateAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.AssociateAnycastEipAddressResponse:
        """
        @summary Associates an Anycast elastic IP address (Anycast EIP) with an endpoint.
        
        @param request: AssociateAnycastEipAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateAnycastEipAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.association_mode):
            query['AssociationMode'] = request.association_mode
        if not UtilClient.is_unset(request.bind_instance_id):
            query['BindInstanceId'] = request.bind_instance_id
        if not UtilClient.is_unset(request.bind_instance_region_id):
            query['BindInstanceRegionId'] = request.bind_instance_region_id
        if not UtilClient.is_unset(request.bind_instance_type):
            query['BindInstanceType'] = request.bind_instance_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.pop_locations):
            query['PopLocations'] = request.pop_locations
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.AssociateAnycastEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_anycast_eip_address_with_options_async(
        self,
        request: eipanycast_20200309_models.AssociateAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.AssociateAnycastEipAddressResponse:
        """
        @summary Associates an Anycast elastic IP address (Anycast EIP) with an endpoint.
        
        @param request: AssociateAnycastEipAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateAnycastEipAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.association_mode):
            query['AssociationMode'] = request.association_mode
        if not UtilClient.is_unset(request.bind_instance_id):
            query['BindInstanceId'] = request.bind_instance_id
        if not UtilClient.is_unset(request.bind_instance_region_id):
            query['BindInstanceRegionId'] = request.bind_instance_region_id
        if not UtilClient.is_unset(request.bind_instance_type):
            query['BindInstanceType'] = request.bind_instance_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.pop_locations):
            query['PopLocations'] = request.pop_locations
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.AssociateAnycastEipAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_anycast_eip_address(
        self,
        request: eipanycast_20200309_models.AssociateAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.AssociateAnycastEipAddressResponse:
        """
        @summary Associates an Anycast elastic IP address (Anycast EIP) with an endpoint.
        
        @param request: AssociateAnycastEipAddressRequest
        @return: AssociateAnycastEipAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_anycast_eip_address_with_options(request, runtime)

    async def associate_anycast_eip_address_async(
        self,
        request: eipanycast_20200309_models.AssociateAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.AssociateAnycastEipAddressResponse:
        """
        @summary Associates an Anycast elastic IP address (Anycast EIP) with an endpoint.
        
        @param request: AssociateAnycastEipAddressRequest
        @return: AssociateAnycastEipAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_anycast_eip_address_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: eipanycast_20200309_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ChangeResourceGroupResponse:
        """
        @summary 修改AnycastEIp实例资源组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: eipanycast_20200309_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ChangeResourceGroupResponse:
        """
        @summary 修改AnycastEIp实例资源组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: eipanycast_20200309_models.ChangeResourceGroupRequest,
    ) -> eipanycast_20200309_models.ChangeResourceGroupResponse:
        """
        @summary 修改AnycastEIp实例资源组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: eipanycast_20200309_models.ChangeResourceGroupRequest,
    ) -> eipanycast_20200309_models.ChangeResourceGroupResponse:
        """
        @summary 修改AnycastEIp实例资源组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def describe_anycast_eip_address_with_options(
        self,
        request: eipanycast_20200309_models.DescribeAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.DescribeAnycastEipAddressResponse:
        """
        @summary Queries Anycast elastic IP addresses (Anycast EIPs) associated with specified instance IP addresses or instance IDs, including instance status, maximum bandwidth, and associated resources.
        
        @param request: DescribeAnycastEipAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAnycastEipAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.bind_instance_id):
            query['BindInstanceId'] = request.bind_instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.DescribeAnycastEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_anycast_eip_address_with_options_async(
        self,
        request: eipanycast_20200309_models.DescribeAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.DescribeAnycastEipAddressResponse:
        """
        @summary Queries Anycast elastic IP addresses (Anycast EIPs) associated with specified instance IP addresses or instance IDs, including instance status, maximum bandwidth, and associated resources.
        
        @param request: DescribeAnycastEipAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAnycastEipAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.bind_instance_id):
            query['BindInstanceId'] = request.bind_instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.DescribeAnycastEipAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_anycast_eip_address(
        self,
        request: eipanycast_20200309_models.DescribeAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.DescribeAnycastEipAddressResponse:
        """
        @summary Queries Anycast elastic IP addresses (Anycast EIPs) associated with specified instance IP addresses or instance IDs, including instance status, maximum bandwidth, and associated resources.
        
        @param request: DescribeAnycastEipAddressRequest
        @return: DescribeAnycastEipAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_anycast_eip_address_with_options(request, runtime)

    async def describe_anycast_eip_address_async(
        self,
        request: eipanycast_20200309_models.DescribeAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.DescribeAnycastEipAddressResponse:
        """
        @summary Queries Anycast elastic IP addresses (Anycast EIPs) associated with specified instance IP addresses or instance IDs, including instance status, maximum bandwidth, and associated resources.
        
        @param request: DescribeAnycastEipAddressRequest
        @return: DescribeAnycastEipAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_anycast_eip_address_with_options_async(request, runtime)

    def describe_anycast_pop_locations_with_options(
        self,
        request: eipanycast_20200309_models.DescribeAnycastPopLocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.DescribeAnycastPopLocationsResponse:
        """
        @summary Queries the information about the access points in an area.
        
        @param request: DescribeAnycastPopLocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAnycastPopLocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnycastPopLocations',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.DescribeAnycastPopLocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_anycast_pop_locations_with_options_async(
        self,
        request: eipanycast_20200309_models.DescribeAnycastPopLocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.DescribeAnycastPopLocationsResponse:
        """
        @summary Queries the information about the access points in an area.
        
        @param request: DescribeAnycastPopLocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAnycastPopLocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnycastPopLocations',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.DescribeAnycastPopLocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_anycast_pop_locations(
        self,
        request: eipanycast_20200309_models.DescribeAnycastPopLocationsRequest,
    ) -> eipanycast_20200309_models.DescribeAnycastPopLocationsResponse:
        """
        @summary Queries the information about the access points in an area.
        
        @param request: DescribeAnycastPopLocationsRequest
        @return: DescribeAnycastPopLocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_anycast_pop_locations_with_options(request, runtime)

    async def describe_anycast_pop_locations_async(
        self,
        request: eipanycast_20200309_models.DescribeAnycastPopLocationsRequest,
    ) -> eipanycast_20200309_models.DescribeAnycastPopLocationsResponse:
        """
        @summary Queries the information about the access points in an area.
        
        @param request: DescribeAnycastPopLocationsRequest
        @return: DescribeAnycastPopLocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_anycast_pop_locations_with_options_async(request, runtime)

    def describe_anycast_server_regions_with_options(
        self,
        request: eipanycast_20200309_models.DescribeAnycastServerRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.DescribeAnycastServerRegionsResponse:
        """
        @summary Queries the regions where you can associate Anycast elastic IP addresses (Anycast EIPs) with endpoints.
        
        @param request: DescribeAnycastServerRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAnycastServerRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnycastServerRegions',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.DescribeAnycastServerRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_anycast_server_regions_with_options_async(
        self,
        request: eipanycast_20200309_models.DescribeAnycastServerRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.DescribeAnycastServerRegionsResponse:
        """
        @summary Queries the regions where you can associate Anycast elastic IP addresses (Anycast EIPs) with endpoints.
        
        @param request: DescribeAnycastServerRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAnycastServerRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnycastServerRegions',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.DescribeAnycastServerRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_anycast_server_regions(
        self,
        request: eipanycast_20200309_models.DescribeAnycastServerRegionsRequest,
    ) -> eipanycast_20200309_models.DescribeAnycastServerRegionsResponse:
        """
        @summary Queries the regions where you can associate Anycast elastic IP addresses (Anycast EIPs) with endpoints.
        
        @param request: DescribeAnycastServerRegionsRequest
        @return: DescribeAnycastServerRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_anycast_server_regions_with_options(request, runtime)

    async def describe_anycast_server_regions_async(
        self,
        request: eipanycast_20200309_models.DescribeAnycastServerRegionsRequest,
    ) -> eipanycast_20200309_models.DescribeAnycastServerRegionsResponse:
        """
        @summary Queries the regions where you can associate Anycast elastic IP addresses (Anycast EIPs) with endpoints.
        
        @param request: DescribeAnycastServerRegionsRequest
        @return: DescribeAnycastServerRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_anycast_server_regions_with_options_async(request, runtime)

    def list_anycast_eip_addresses_with_options(
        self,
        request: eipanycast_20200309_models.ListAnycastEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ListAnycastEipAddressesResponse:
        """
        @summary Queries information about Anycast elastic IP addresses (Anycast EIPs) in an access area, including instance status, maximum bandwidth, and associated resources.
        
        @param request: ListAnycastEipAddressesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnycastEipAddressesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_eip_address):
            query['AnycastEipAddress'] = request.anycast_eip_address
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.anycast_ids):
            query['AnycastIds'] = request.anycast_ids
        if not UtilClient.is_unset(request.bind_instance_ids):
            query['BindInstanceIds'] = request.bind_instance_ids
        if not UtilClient.is_unset(request.business_status):
            query['BusinessStatus'] = request.business_status
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnycastEipAddresses',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ListAnycastEipAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_anycast_eip_addresses_with_options_async(
        self,
        request: eipanycast_20200309_models.ListAnycastEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ListAnycastEipAddressesResponse:
        """
        @summary Queries information about Anycast elastic IP addresses (Anycast EIPs) in an access area, including instance status, maximum bandwidth, and associated resources.
        
        @param request: ListAnycastEipAddressesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnycastEipAddressesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_eip_address):
            query['AnycastEipAddress'] = request.anycast_eip_address
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.anycast_ids):
            query['AnycastIds'] = request.anycast_ids
        if not UtilClient.is_unset(request.bind_instance_ids):
            query['BindInstanceIds'] = request.bind_instance_ids
        if not UtilClient.is_unset(request.business_status):
            query['BusinessStatus'] = request.business_status
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnycastEipAddresses',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ListAnycastEipAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_anycast_eip_addresses(
        self,
        request: eipanycast_20200309_models.ListAnycastEipAddressesRequest,
    ) -> eipanycast_20200309_models.ListAnycastEipAddressesResponse:
        """
        @summary Queries information about Anycast elastic IP addresses (Anycast EIPs) in an access area, including instance status, maximum bandwidth, and associated resources.
        
        @param request: ListAnycastEipAddressesRequest
        @return: ListAnycastEipAddressesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_anycast_eip_addresses_with_options(request, runtime)

    async def list_anycast_eip_addresses_async(
        self,
        request: eipanycast_20200309_models.ListAnycastEipAddressesRequest,
    ) -> eipanycast_20200309_models.ListAnycastEipAddressesResponse:
        """
        @summary Queries information about Anycast elastic IP addresses (Anycast EIPs) in an access area, including instance status, maximum bandwidth, and associated resources.
        
        @param request: ListAnycastEipAddressesRequest
        @return: ListAnycastEipAddressesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_anycast_eip_addresses_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: eipanycast_20200309_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='ListTagResources',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: eipanycast_20200309_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='ListTagResources',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: eipanycast_20200309_models.ListTagResourcesRequest,
    ) -> eipanycast_20200309_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: eipanycast_20200309_models.ListTagResourcesRequest,
    ) -> eipanycast_20200309_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_anycast_eip_address_attribute_with_options(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressAttributeResponse:
        """
        @summary Modifies the name and description of an Anycast elastic IP address (Anycast EIP).
        
        @param request: ModifyAnycastEipAddressAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAnycastEipAddressAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAnycastEipAddressAttribute',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ModifyAnycastEipAddressAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_anycast_eip_address_attribute_with_options_async(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressAttributeResponse:
        """
        @summary Modifies the name and description of an Anycast elastic IP address (Anycast EIP).
        
        @param request: ModifyAnycastEipAddressAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAnycastEipAddressAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAnycastEipAddressAttribute',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ModifyAnycastEipAddressAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_anycast_eip_address_attribute(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressAttributeRequest,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressAttributeResponse:
        """
        @summary Modifies the name and description of an Anycast elastic IP address (Anycast EIP).
        
        @param request: ModifyAnycastEipAddressAttributeRequest
        @return: ModifyAnycastEipAddressAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_anycast_eip_address_attribute_with_options(request, runtime)

    async def modify_anycast_eip_address_attribute_async(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressAttributeRequest,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressAttributeResponse:
        """
        @summary Modifies the name and description of an Anycast elastic IP address (Anycast EIP).
        
        @param request: ModifyAnycastEipAddressAttributeRequest
        @return: ModifyAnycastEipAddressAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_anycast_eip_address_attribute_with_options_async(request, runtime)

    def modify_anycast_eip_address_spec_with_options(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressSpecResponse:
        """
        @summary Modifies the maximum bandwidth of an Anycast elastic IP address (Anycast EIP).
        
        @param request: ModifyAnycastEipAddressSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAnycastEipAddressSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAnycastEipAddressSpec',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ModifyAnycastEipAddressSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_anycast_eip_address_spec_with_options_async(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressSpecResponse:
        """
        @summary Modifies the maximum bandwidth of an Anycast elastic IP address (Anycast EIP).
        
        @param request: ModifyAnycastEipAddressSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAnycastEipAddressSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAnycastEipAddressSpec',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ModifyAnycastEipAddressSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_anycast_eip_address_spec(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressSpecRequest,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressSpecResponse:
        """
        @summary Modifies the maximum bandwidth of an Anycast elastic IP address (Anycast EIP).
        
        @param request: ModifyAnycastEipAddressSpecRequest
        @return: ModifyAnycastEipAddressSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_anycast_eip_address_spec_with_options(request, runtime)

    async def modify_anycast_eip_address_spec_async(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressSpecRequest,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressSpecResponse:
        """
        @summary Modifies the maximum bandwidth of an Anycast elastic IP address (Anycast EIP).
        
        @param request: ModifyAnycastEipAddressSpecRequest
        @return: ModifyAnycastEipAddressSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_anycast_eip_address_spec_with_options_async(request, runtime)

    def release_anycast_eip_address_with_options(
        self,
        request: eipanycast_20200309_models.ReleaseAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ReleaseAnycastEipAddressResponse:
        """
        @summary Releases an Anycast elastic IP address (Anycast EIP).
        
        @param request: ReleaseAnycastEipAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseAnycastEipAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ReleaseAnycastEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_anycast_eip_address_with_options_async(
        self,
        request: eipanycast_20200309_models.ReleaseAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ReleaseAnycastEipAddressResponse:
        """
        @summary Releases an Anycast elastic IP address (Anycast EIP).
        
        @param request: ReleaseAnycastEipAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseAnycastEipAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ReleaseAnycastEipAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_anycast_eip_address(
        self,
        request: eipanycast_20200309_models.ReleaseAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.ReleaseAnycastEipAddressResponse:
        """
        @summary Releases an Anycast elastic IP address (Anycast EIP).
        
        @param request: ReleaseAnycastEipAddressRequest
        @return: ReleaseAnycastEipAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_anycast_eip_address_with_options(request, runtime)

    async def release_anycast_eip_address_async(
        self,
        request: eipanycast_20200309_models.ReleaseAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.ReleaseAnycastEipAddressResponse:
        """
        @summary Releases an Anycast elastic IP address (Anycast EIP).
        
        @param request: ReleaseAnycastEipAddressRequest
        @return: ReleaseAnycastEipAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_anycast_eip_address_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: eipanycast_20200309_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.TagResourcesResponse:
        """
        @summary Creates and adds tags to resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: eipanycast_20200309_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.TagResourcesResponse:
        """
        @summary Creates and adds tags to resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: eipanycast_20200309_models.TagResourcesRequest,
    ) -> eipanycast_20200309_models.TagResourcesResponse:
        """
        @summary Creates and adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: eipanycast_20200309_models.TagResourcesRequest,
    ) -> eipanycast_20200309_models.TagResourcesResponse:
        """
        @summary Creates and adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unassociate_anycast_eip_address_with_options(
        self,
        request: eipanycast_20200309_models.UnassociateAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.UnassociateAnycastEipAddressResponse:
        """
        @summary Disassociates an Anycast elastic IP address (Anycast EIP) from an endpoint.
        
        @param request: UnassociateAnycastEipAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnassociateAnycastEipAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.bind_instance_id):
            query['BindInstanceId'] = request.bind_instance_id
        if not UtilClient.is_unset(request.bind_instance_region_id):
            query['BindInstanceRegionId'] = request.bind_instance_region_id
        if not UtilClient.is_unset(request.bind_instance_type):
            query['BindInstanceType'] = request.bind_instance_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnassociateAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.UnassociateAnycastEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def unassociate_anycast_eip_address_with_options_async(
        self,
        request: eipanycast_20200309_models.UnassociateAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.UnassociateAnycastEipAddressResponse:
        """
        @summary Disassociates an Anycast elastic IP address (Anycast EIP) from an endpoint.
        
        @param request: UnassociateAnycastEipAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnassociateAnycastEipAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.bind_instance_id):
            query['BindInstanceId'] = request.bind_instance_id
        if not UtilClient.is_unset(request.bind_instance_region_id):
            query['BindInstanceRegionId'] = request.bind_instance_region_id
        if not UtilClient.is_unset(request.bind_instance_type):
            query['BindInstanceType'] = request.bind_instance_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnassociateAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.UnassociateAnycastEipAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unassociate_anycast_eip_address(
        self,
        request: eipanycast_20200309_models.UnassociateAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.UnassociateAnycastEipAddressResponse:
        """
        @summary Disassociates an Anycast elastic IP address (Anycast EIP) from an endpoint.
        
        @param request: UnassociateAnycastEipAddressRequest
        @return: UnassociateAnycastEipAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unassociate_anycast_eip_address_with_options(request, runtime)

    async def unassociate_anycast_eip_address_async(
        self,
        request: eipanycast_20200309_models.UnassociateAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.UnassociateAnycastEipAddressResponse:
        """
        @summary Disassociates an Anycast elastic IP address (Anycast EIP) from an endpoint.
        
        @param request: UnassociateAnycastEipAddressRequest
        @return: UnassociateAnycastEipAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_anycast_eip_address_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: eipanycast_20200309_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.UntagResourcesResponse:
        """
        @summary Removes tags from Anycast EIPs.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: eipanycast_20200309_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.UntagResourcesResponse:
        """
        @summary Removes tags from Anycast EIPs.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: eipanycast_20200309_models.UntagResourcesRequest,
    ) -> eipanycast_20200309_models.UntagResourcesResponse:
        """
        @summary Removes tags from Anycast EIPs.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: eipanycast_20200309_models.UntagResourcesRequest,
    ) -> eipanycast_20200309_models.UntagResourcesResponse:
        """
        @summary Removes tags from Anycast EIPs.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_anycast_eip_address_associations_with_options(
        self,
        request: eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsResponse:
        """
        @summary If an Anycast EIP is associated with endpoints in different regions, you can change the access points that are mapped to an endpoint. You can call UpdateAnycastEipAddressAssociations to add or delete endpoints to modify the mappings between endpoints and access points.
        
        @param request: UpdateAnycastEipAddressAssociationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAnycastEipAddressAssociationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.association_mode):
            query['AssociationMode'] = request.association_mode
        if not UtilClient.is_unset(request.bind_instance_id):
            query['BindInstanceId'] = request.bind_instance_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.pop_location_add_list):
            query['PopLocationAddList'] = request.pop_location_add_list
        if not UtilClient.is_unset(request.pop_location_delete_list):
            query['PopLocationDeleteList'] = request.pop_location_delete_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAnycastEipAddressAssociations',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_anycast_eip_address_associations_with_options_async(
        self,
        request: eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsResponse:
        """
        @summary If an Anycast EIP is associated with endpoints in different regions, you can change the access points that are mapped to an endpoint. You can call UpdateAnycastEipAddressAssociations to add or delete endpoints to modify the mappings between endpoints and access points.
        
        @param request: UpdateAnycastEipAddressAssociationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAnycastEipAddressAssociationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anycast_id):
            query['AnycastId'] = request.anycast_id
        if not UtilClient.is_unset(request.association_mode):
            query['AssociationMode'] = request.association_mode
        if not UtilClient.is_unset(request.bind_instance_id):
            query['BindInstanceId'] = request.bind_instance_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.pop_location_add_list):
            query['PopLocationAddList'] = request.pop_location_add_list
        if not UtilClient.is_unset(request.pop_location_delete_list):
            query['PopLocationDeleteList'] = request.pop_location_delete_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAnycastEipAddressAssociations',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_anycast_eip_address_associations(
        self,
        request: eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsRequest,
    ) -> eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsResponse:
        """
        @summary If an Anycast EIP is associated with endpoints in different regions, you can change the access points that are mapped to an endpoint. You can call UpdateAnycastEipAddressAssociations to add or delete endpoints to modify the mappings between endpoints and access points.
        
        @param request: UpdateAnycastEipAddressAssociationsRequest
        @return: UpdateAnycastEipAddressAssociationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_anycast_eip_address_associations_with_options(request, runtime)

    async def update_anycast_eip_address_associations_async(
        self,
        request: eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsRequest,
    ) -> eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsResponse:
        """
        @summary If an Anycast EIP is associated with endpoints in different regions, you can change the access points that are mapped to an endpoint. You can call UpdateAnycastEipAddressAssociations to add or delete endpoints to modify the mappings between endpoints and access points.
        
        @param request: UpdateAnycastEipAddressAssociationsRequest
        @return: UpdateAnycastEipAddressAssociationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_anycast_eip_address_associations_with_options_async(request, runtime)
