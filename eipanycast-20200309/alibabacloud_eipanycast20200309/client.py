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
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
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
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
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
        runtime = util_models.RuntimeOptions()
        return self.allocate_anycast_eip_address_with_options(request, runtime)

    async def allocate_anycast_eip_address_async(
        self,
        request: eipanycast_20200309_models.AllocateAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.AllocateAnycastEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_anycast_eip_address_with_options_async(request, runtime)

    def associate_anycast_eip_address_with_options(
        self,
        request: eipanycast_20200309_models.AssociateAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.AssociateAnycastEipAddressResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.associate_anycast_eip_address_with_options(request, runtime)

    async def associate_anycast_eip_address_async(
        self,
        request: eipanycast_20200309_models.AssociateAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.AssociateAnycastEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_anycast_eip_address_with_options_async(request, runtime)

    def describe_anycast_eip_address_with_options(
        self,
        request: eipanycast_20200309_models.DescribeAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.DescribeAnycastEipAddressResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_anycast_eip_address_with_options(request, runtime)

    async def describe_anycast_eip_address_async(
        self,
        request: eipanycast_20200309_models.DescribeAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.DescribeAnycastEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_anycast_eip_address_with_options_async(request, runtime)

    def describe_anycast_pop_locations_with_options(
        self,
        request: eipanycast_20200309_models.DescribeAnycastPopLocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.DescribeAnycastPopLocationsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_anycast_pop_locations_with_options(request, runtime)

    async def describe_anycast_pop_locations_async(
        self,
        request: eipanycast_20200309_models.DescribeAnycastPopLocationsRequest,
    ) -> eipanycast_20200309_models.DescribeAnycastPopLocationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_anycast_pop_locations_with_options_async(request, runtime)

    def describe_anycast_server_regions_with_options(
        self,
        request: eipanycast_20200309_models.DescribeAnycastServerRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.DescribeAnycastServerRegionsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_anycast_server_regions_with_options(request, runtime)

    async def describe_anycast_server_regions_async(
        self,
        request: eipanycast_20200309_models.DescribeAnycastServerRegionsRequest,
    ) -> eipanycast_20200309_models.DescribeAnycastServerRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_anycast_server_regions_with_options_async(request, runtime)

    def list_anycast_eip_addresses_with_options(
        self,
        request: eipanycast_20200309_models.ListAnycastEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ListAnycastEipAddressesResponse:
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
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
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
        if not UtilClient.is_unset(request.service_location):
            query['ServiceLocation'] = request.service_location
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
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
        runtime = util_models.RuntimeOptions()
        return self.list_anycast_eip_addresses_with_options(request, runtime)

    async def list_anycast_eip_addresses_async(
        self,
        request: eipanycast_20200309_models.ListAnycastEipAddressesRequest,
    ) -> eipanycast_20200309_models.ListAnycastEipAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_anycast_eip_addresses_with_options_async(request, runtime)

    def modify_anycast_eip_address_attribute_with_options(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressAttributeResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.modify_anycast_eip_address_attribute_with_options(request, runtime)

    async def modify_anycast_eip_address_attribute_async(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressAttributeRequest,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_anycast_eip_address_attribute_with_options_async(request, runtime)

    def modify_anycast_eip_address_spec_with_options(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressSpecResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.modify_anycast_eip_address_spec_with_options(request, runtime)

    async def modify_anycast_eip_address_spec_async(
        self,
        request: eipanycast_20200309_models.ModifyAnycastEipAddressSpecRequest,
    ) -> eipanycast_20200309_models.ModifyAnycastEipAddressSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_anycast_eip_address_spec_with_options_async(request, runtime)

    def release_anycast_eip_address_with_options(
        self,
        request: eipanycast_20200309_models.ReleaseAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.ReleaseAnycastEipAddressResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.release_anycast_eip_address_with_options(request, runtime)

    async def release_anycast_eip_address_async(
        self,
        request: eipanycast_20200309_models.ReleaseAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.ReleaseAnycastEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_anycast_eip_address_with_options_async(request, runtime)

    def unassociate_anycast_eip_address_with_options(
        self,
        request: eipanycast_20200309_models.UnassociateAnycastEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.UnassociateAnycastEipAddressResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.unassociate_anycast_eip_address_with_options(request, runtime)

    async def unassociate_anycast_eip_address_async(
        self,
        request: eipanycast_20200309_models.UnassociateAnycastEipAddressRequest,
    ) -> eipanycast_20200309_models.UnassociateAnycastEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_anycast_eip_address_with_options_async(request, runtime)

    def update_anycast_eip_address_associations_with_options(
        self,
        request: eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_anycast_eip_address_associations_with_options(request, runtime)

    async def update_anycast_eip_address_associations_async(
        self,
        request: eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsRequest,
    ) -> eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_anycast_eip_address_associations_with_options_async(request, runtime)
