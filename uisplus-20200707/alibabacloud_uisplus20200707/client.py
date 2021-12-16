# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_uisplus20200707 import models as uisplus_20200707_models
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
        self._endpoint = self.get_endpoint('uisplus', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def associate_eip_with_options(
        self,
        request: uisplus_20200707_models.AssociateEipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.AssociateEipResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateEip',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.AssociateEipResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_eip_with_options_async(
        self,
        request: uisplus_20200707_models.AssociateEipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.AssociateEipResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateEip',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.AssociateEipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_eip(
        self,
        request: uisplus_20200707_models.AssociateEipRequest,
    ) -> uisplus_20200707_models.AssociateEipResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_eip_with_options(request, runtime)

    async def associate_eip_async(
        self,
        request: uisplus_20200707_models.AssociateEipRequest,
    ) -> uisplus_20200707_models.AssociateEipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_eip_with_options_async(request, runtime)

    def create_gre_connection_with_options(
        self,
        request: uisplus_20200707_models.CreateGreConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.CreateGreConnectionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGreConnection',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.CreateGreConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gre_connection_with_options_async(
        self,
        request: uisplus_20200707_models.CreateGreConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.CreateGreConnectionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGreConnection',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.CreateGreConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gre_connection(
        self,
        request: uisplus_20200707_models.CreateGreConnectionRequest,
    ) -> uisplus_20200707_models.CreateGreConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gre_connection_with_options(request, runtime)

    async def create_gre_connection_async(
        self,
        request: uisplus_20200707_models.CreateGreConnectionRequest,
    ) -> uisplus_20200707_models.CreateGreConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gre_connection_with_options_async(request, runtime)

    def create_uis_with_options(
        self,
        request: uisplus_20200707_models.CreateUisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.CreateUisResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUis',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.CreateUisResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_uis_with_options_async(
        self,
        request: uisplus_20200707_models.CreateUisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.CreateUisResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUis',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.CreateUisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_uis(
        self,
        request: uisplus_20200707_models.CreateUisRequest,
    ) -> uisplus_20200707_models.CreateUisResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_uis_with_options(request, runtime)

    async def create_uis_async(
        self,
        request: uisplus_20200707_models.CreateUisRequest,
    ) -> uisplus_20200707_models.CreateUisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_uis_with_options_async(request, runtime)

    def create_vnet_with_options(
        self,
        request: uisplus_20200707_models.CreateVnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.CreateVnetResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVnet',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.CreateVnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vnet_with_options_async(
        self,
        request: uisplus_20200707_models.CreateVnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.CreateVnetResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVnet',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.CreateVnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vnet(
        self,
        request: uisplus_20200707_models.CreateVnetRequest,
    ) -> uisplus_20200707_models.CreateVnetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vnet_with_options(request, runtime)

    async def create_vnet_async(
        self,
        request: uisplus_20200707_models.CreateVnetRequest,
    ) -> uisplus_20200707_models.CreateVnetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vnet_with_options_async(request, runtime)

    def create_vnet_route_entry_with_options(
        self,
        request: uisplus_20200707_models.CreateVnetRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.CreateVnetRouteEntryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVnetRouteEntry',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.CreateVnetRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vnet_route_entry_with_options_async(
        self,
        request: uisplus_20200707_models.CreateVnetRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.CreateVnetRouteEntryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVnetRouteEntry',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.CreateVnetRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vnet_route_entry(
        self,
        request: uisplus_20200707_models.CreateVnetRouteEntryRequest,
    ) -> uisplus_20200707_models.CreateVnetRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vnet_route_entry_with_options(request, runtime)

    async def create_vnet_route_entry_async(
        self,
        request: uisplus_20200707_models.CreateVnetRouteEntryRequest,
    ) -> uisplus_20200707_models.CreateVnetRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vnet_route_entry_with_options_async(request, runtime)

    def delete_gre_connection_with_options(
        self,
        request: uisplus_20200707_models.DeleteGreConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DeleteGreConnectionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGreConnection',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DeleteGreConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gre_connection_with_options_async(
        self,
        request: uisplus_20200707_models.DeleteGreConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DeleteGreConnectionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGreConnection',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DeleteGreConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gre_connection(
        self,
        request: uisplus_20200707_models.DeleteGreConnectionRequest,
    ) -> uisplus_20200707_models.DeleteGreConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gre_connection_with_options(request, runtime)

    async def delete_gre_connection_async(
        self,
        request: uisplus_20200707_models.DeleteGreConnectionRequest,
    ) -> uisplus_20200707_models.DeleteGreConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gre_connection_with_options_async(request, runtime)

    def delete_uis_with_options(
        self,
        request: uisplus_20200707_models.DeleteUisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DeleteUisResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUis',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DeleteUisResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_uis_with_options_async(
        self,
        request: uisplus_20200707_models.DeleteUisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DeleteUisResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUis',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DeleteUisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_uis(
        self,
        request: uisplus_20200707_models.DeleteUisRequest,
    ) -> uisplus_20200707_models.DeleteUisResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_uis_with_options(request, runtime)

    async def delete_uis_async(
        self,
        request: uisplus_20200707_models.DeleteUisRequest,
    ) -> uisplus_20200707_models.DeleteUisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_uis_with_options_async(request, runtime)

    def delete_vnet_with_options(
        self,
        request: uisplus_20200707_models.DeleteVnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DeleteVnetResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVnet',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DeleteVnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vnet_with_options_async(
        self,
        request: uisplus_20200707_models.DeleteVnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DeleteVnetResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVnet',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DeleteVnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vnet(
        self,
        request: uisplus_20200707_models.DeleteVnetRequest,
    ) -> uisplus_20200707_models.DeleteVnetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vnet_with_options(request, runtime)

    async def delete_vnet_async(
        self,
        request: uisplus_20200707_models.DeleteVnetRequest,
    ) -> uisplus_20200707_models.DeleteVnetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vnet_with_options_async(request, runtime)

    def delete_vnet_route_entry_with_options(
        self,
        request: uisplus_20200707_models.DeleteVnetRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DeleteVnetRouteEntryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVnetRouteEntry',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DeleteVnetRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vnet_route_entry_with_options_async(
        self,
        request: uisplus_20200707_models.DeleteVnetRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DeleteVnetRouteEntryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVnetRouteEntry',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DeleteVnetRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vnet_route_entry(
        self,
        request: uisplus_20200707_models.DeleteVnetRouteEntryRequest,
    ) -> uisplus_20200707_models.DeleteVnetRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vnet_route_entry_with_options(request, runtime)

    async def delete_vnet_route_entry_async(
        self,
        request: uisplus_20200707_models.DeleteVnetRouteEntryRequest,
    ) -> uisplus_20200707_models.DeleteVnetRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vnet_route_entry_with_options_async(request, runtime)

    def describe_gre_connection_with_options(
        self,
        request: uisplus_20200707_models.DescribeGreConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeGreConnectionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGreConnection',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeGreConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gre_connection_with_options_async(
        self,
        request: uisplus_20200707_models.DescribeGreConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeGreConnectionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGreConnection',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeGreConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gre_connection(
        self,
        request: uisplus_20200707_models.DescribeGreConnectionRequest,
    ) -> uisplus_20200707_models.DescribeGreConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gre_connection_with_options(request, runtime)

    async def describe_gre_connection_async(
        self,
        request: uisplus_20200707_models.DescribeGreConnectionRequest,
    ) -> uisplus_20200707_models.DescribeGreConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gre_connection_with_options_async(request, runtime)

    def describe_gre_connections_with_options(
        self,
        request: uisplus_20200707_models.DescribeGreConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeGreConnectionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGreConnections',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeGreConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gre_connections_with_options_async(
        self,
        request: uisplus_20200707_models.DescribeGreConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeGreConnectionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGreConnections',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeGreConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gre_connections(
        self,
        request: uisplus_20200707_models.DescribeGreConnectionsRequest,
    ) -> uisplus_20200707_models.DescribeGreConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gre_connections_with_options(request, runtime)

    async def describe_gre_connections_async(
        self,
        request: uisplus_20200707_models.DescribeGreConnectionsRequest,
    ) -> uisplus_20200707_models.DescribeGreConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gre_connections_with_options_async(request, runtime)

    def describe_uis_with_options(
        self,
        request: uisplus_20200707_models.DescribeUisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeUisResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUis',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeUisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_uis_with_options_async(
        self,
        request: uisplus_20200707_models.DescribeUisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeUisResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUis',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeUisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_uis(
        self,
        request: uisplus_20200707_models.DescribeUisRequest,
    ) -> uisplus_20200707_models.DescribeUisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_uis_with_options(request, runtime)

    async def describe_uis_async(
        self,
        request: uisplus_20200707_models.DescribeUisRequest,
    ) -> uisplus_20200707_models.DescribeUisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_uis_with_options_async(request, runtime)

    def describe_uiss_with_options(
        self,
        request: uisplus_20200707_models.DescribeUissRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeUissResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUiss',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeUissResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_uiss_with_options_async(
        self,
        request: uisplus_20200707_models.DescribeUissRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeUissResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUiss',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeUissResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_uiss(
        self,
        request: uisplus_20200707_models.DescribeUissRequest,
    ) -> uisplus_20200707_models.DescribeUissResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_uiss_with_options(request, runtime)

    async def describe_uiss_async(
        self,
        request: uisplus_20200707_models.DescribeUissRequest,
    ) -> uisplus_20200707_models.DescribeUissResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_uiss_with_options_async(request, runtime)

    def describe_vnet_with_options(
        self,
        request: uisplus_20200707_models.DescribeVnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeVnetResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVnet',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeVnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vnet_with_options_async(
        self,
        request: uisplus_20200707_models.DescribeVnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeVnetResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVnet',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeVnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vnet(
        self,
        request: uisplus_20200707_models.DescribeVnetRequest,
    ) -> uisplus_20200707_models.DescribeVnetResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vnet_with_options(request, runtime)

    async def describe_vnet_async(
        self,
        request: uisplus_20200707_models.DescribeVnetRequest,
    ) -> uisplus_20200707_models.DescribeVnetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vnet_with_options_async(request, runtime)

    def describe_vnet_route_entry_list_with_options(
        self,
        request: uisplus_20200707_models.DescribeVnetRouteEntryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeVnetRouteEntryListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVnetRouteEntryList',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeVnetRouteEntryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vnet_route_entry_list_with_options_async(
        self,
        request: uisplus_20200707_models.DescribeVnetRouteEntryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeVnetRouteEntryListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVnetRouteEntryList',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeVnetRouteEntryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vnet_route_entry_list(
        self,
        request: uisplus_20200707_models.DescribeVnetRouteEntryListRequest,
    ) -> uisplus_20200707_models.DescribeVnetRouteEntryListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vnet_route_entry_list_with_options(request, runtime)

    async def describe_vnet_route_entry_list_async(
        self,
        request: uisplus_20200707_models.DescribeVnetRouteEntryListRequest,
    ) -> uisplus_20200707_models.DescribeVnetRouteEntryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vnet_route_entry_list_with_options_async(request, runtime)

    def describe_vnets_with_options(
        self,
        request: uisplus_20200707_models.DescribeVnetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeVnetsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVnets',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeVnetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vnets_with_options_async(
        self,
        request: uisplus_20200707_models.DescribeVnetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DescribeVnetsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVnets',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DescribeVnetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vnets(
        self,
        request: uisplus_20200707_models.DescribeVnetsRequest,
    ) -> uisplus_20200707_models.DescribeVnetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vnets_with_options(request, runtime)

    async def describe_vnets_async(
        self,
        request: uisplus_20200707_models.DescribeVnetsRequest,
    ) -> uisplus_20200707_models.DescribeVnetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vnets_with_options_async(request, runtime)

    def disable_uis_wildcard_domain_with_options(
        self,
        request: uisplus_20200707_models.DisableUisWildcardDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DisableUisWildcardDomainResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableUisWildcardDomain',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DisableUisWildcardDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_uis_wildcard_domain_with_options_async(
        self,
        request: uisplus_20200707_models.DisableUisWildcardDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DisableUisWildcardDomainResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableUisWildcardDomain',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DisableUisWildcardDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_uis_wildcard_domain(
        self,
        request: uisplus_20200707_models.DisableUisWildcardDomainRequest,
    ) -> uisplus_20200707_models.DisableUisWildcardDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_uis_wildcard_domain_with_options(request, runtime)

    async def disable_uis_wildcard_domain_async(
        self,
        request: uisplus_20200707_models.DisableUisWildcardDomainRequest,
    ) -> uisplus_20200707_models.DisableUisWildcardDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_uis_wildcard_domain_with_options_async(request, runtime)

    def disable_vnet_wildcard_domain_with_options(
        self,
        request: uisplus_20200707_models.DisableVnetWildcardDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DisableVnetWildcardDomainResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableVnetWildcardDomain',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DisableVnetWildcardDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_vnet_wildcard_domain_with_options_async(
        self,
        request: uisplus_20200707_models.DisableVnetWildcardDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.DisableVnetWildcardDomainResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableVnetWildcardDomain',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.DisableVnetWildcardDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_vnet_wildcard_domain(
        self,
        request: uisplus_20200707_models.DisableVnetWildcardDomainRequest,
    ) -> uisplus_20200707_models.DisableVnetWildcardDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_vnet_wildcard_domain_with_options(request, runtime)

    async def disable_vnet_wildcard_domain_async(
        self,
        request: uisplus_20200707_models.DisableVnetWildcardDomainRequest,
    ) -> uisplus_20200707_models.DisableVnetWildcardDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_vnet_wildcard_domain_with_options_async(request, runtime)

    def enable_uis_wildcard_domain_with_options(
        self,
        request: uisplus_20200707_models.EnableUisWildcardDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.EnableUisWildcardDomainResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableUisWildcardDomain',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.EnableUisWildcardDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_uis_wildcard_domain_with_options_async(
        self,
        request: uisplus_20200707_models.EnableUisWildcardDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.EnableUisWildcardDomainResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableUisWildcardDomain',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.EnableUisWildcardDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_uis_wildcard_domain(
        self,
        request: uisplus_20200707_models.EnableUisWildcardDomainRequest,
    ) -> uisplus_20200707_models.EnableUisWildcardDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_uis_wildcard_domain_with_options(request, runtime)

    async def enable_uis_wildcard_domain_async(
        self,
        request: uisplus_20200707_models.EnableUisWildcardDomainRequest,
    ) -> uisplus_20200707_models.EnableUisWildcardDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_uis_wildcard_domain_with_options_async(request, runtime)

    def modify_gre_connection_with_options(
        self,
        request: uisplus_20200707_models.ModifyGreConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.ModifyGreConnectionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGreConnection',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.ModifyGreConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_gre_connection_with_options_async(
        self,
        request: uisplus_20200707_models.ModifyGreConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.ModifyGreConnectionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGreConnection',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.ModifyGreConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_gre_connection(
        self,
        request: uisplus_20200707_models.ModifyGreConnectionRequest,
    ) -> uisplus_20200707_models.ModifyGreConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_gre_connection_with_options(request, runtime)

    async def modify_gre_connection_async(
        self,
        request: uisplus_20200707_models.ModifyGreConnectionRequest,
    ) -> uisplus_20200707_models.ModifyGreConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_gre_connection_with_options_async(request, runtime)

    def modify_vnet_with_options(
        self,
        request: uisplus_20200707_models.ModifyVnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.ModifyVnetResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVnet',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.ModifyVnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vnet_with_options_async(
        self,
        request: uisplus_20200707_models.ModifyVnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.ModifyVnetResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVnet',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.ModifyVnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vnet(
        self,
        request: uisplus_20200707_models.ModifyVnetRequest,
    ) -> uisplus_20200707_models.ModifyVnetResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vnet_with_options(request, runtime)

    async def modify_vnet_async(
        self,
        request: uisplus_20200707_models.ModifyVnetRequest,
    ) -> uisplus_20200707_models.ModifyVnetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vnet_with_options_async(request, runtime)

    def un_associate_eip_with_options(
        self,
        request: uisplus_20200707_models.UnAssociateEipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.UnAssociateEipResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnAssociateEip',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.UnAssociateEipResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_associate_eip_with_options_async(
        self,
        request: uisplus_20200707_models.UnAssociateEipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uisplus_20200707_models.UnAssociateEipResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnAssociateEip',
            version='2020-07-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            uisplus_20200707_models.UnAssociateEipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_associate_eip(
        self,
        request: uisplus_20200707_models.UnAssociateEipRequest,
    ) -> uisplus_20200707_models.UnAssociateEipResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_associate_eip_with_options(request, runtime)

    async def un_associate_eip_async(
        self,
        request: uisplus_20200707_models.UnAssociateEipRequest,
    ) -> uisplus_20200707_models.UnAssociateEipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_associate_eip_with_options_async(request, runtime)
