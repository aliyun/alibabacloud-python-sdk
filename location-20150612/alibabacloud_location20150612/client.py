# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_location20150612 import models as location_20150612_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('location', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_endpoint_with_options(
        self,
        request: location_20150612_models.DescribeEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.DescribeEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.DescribeEndpointResponse(),
            self.do_rpcrequest('DescribeEndpoint', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_endpoint_with_options_async(
        self,
        request: location_20150612_models.DescribeEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.DescribeEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.DescribeEndpointResponse(),
            await self.do_rpcrequest_async('DescribeEndpoint', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_endpoint(
        self,
        request: location_20150612_models.DescribeEndpointRequest,
    ) -> location_20150612_models.DescribeEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoint_with_options(request, runtime)

    async def describe_endpoint_async(
        self,
        request: location_20150612_models.DescribeEndpointRequest,
    ) -> location_20150612_models.DescribeEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_endpoint_with_options_async(request, runtime)

    def describe_endpoints_with_options(
        self,
        request: location_20150612_models.DescribeEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.DescribeEndpointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.DescribeEndpointsResponse(),
            self.do_rpcrequest('DescribeEndpoints', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_endpoints_with_options_async(
        self,
        request: location_20150612_models.DescribeEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.DescribeEndpointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.DescribeEndpointsResponse(),
            await self.do_rpcrequest_async('DescribeEndpoints', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_endpoints(
        self,
        request: location_20150612_models.DescribeEndpointsRequest,
    ) -> location_20150612_models.DescribeEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoints_with_options(request, runtime)

    async def describe_endpoints_async(
        self,
        request: location_20150612_models.DescribeEndpointsRequest,
    ) -> location_20150612_models.DescribeEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_endpoints_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: location_20150612_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: location_20150612_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: location_20150612_models.DescribeRegionsRequest,
    ) -> location_20150612_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: location_20150612_models.DescribeRegionsRequest,
    ) -> location_20150612_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_services_with_options(
        self,
        request: location_20150612_models.DescribeServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.DescribeServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.DescribeServicesResponse(),
            self.do_rpcrequest('DescribeServices', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_services_with_options_async(
        self,
        request: location_20150612_models.DescribeServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.DescribeServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.DescribeServicesResponse(),
            await self.do_rpcrequest_async('DescribeServices', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_services(
        self,
        request: location_20150612_models.DescribeServicesRequest,
    ) -> location_20150612_models.DescribeServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_services_with_options(request, runtime)

    async def describe_services_async(
        self,
        request: location_20150612_models.DescribeServicesRequest,
    ) -> location_20150612_models.DescribeServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_services_with_options_async(request, runtime)

    def list_endpoints_with_options(
        self,
        request: location_20150612_models.ListEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.ListEndpointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.ListEndpointsResponse(),
            self.do_rpcrequest('ListEndpoints', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_endpoints_with_options_async(
        self,
        request: location_20150612_models.ListEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.ListEndpointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.ListEndpointsResponse(),
            await self.do_rpcrequest_async('ListEndpoints', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_endpoints(
        self,
        request: location_20150612_models.ListEndpointsRequest,
    ) -> location_20150612_models.ListEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_endpoints_with_options(request, runtime)

    async def list_endpoints_async(
        self,
        request: location_20150612_models.ListEndpointsRequest,
    ) -> location_20150612_models.ListEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_endpoints_with_options_async(request, runtime)

    def list_endpoints_by_ip_with_options(
        self,
        request: location_20150612_models.ListEndpointsByIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.ListEndpointsByIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.ListEndpointsByIpResponse(),
            self.do_rpcrequest('ListEndpointsByIp', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_endpoints_by_ip_with_options_async(
        self,
        request: location_20150612_models.ListEndpointsByIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> location_20150612_models.ListEndpointsByIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            location_20150612_models.ListEndpointsByIpResponse(),
            await self.do_rpcrequest_async('ListEndpointsByIp', '2015-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_endpoints_by_ip(
        self,
        request: location_20150612_models.ListEndpointsByIpRequest,
    ) -> location_20150612_models.ListEndpointsByIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_endpoints_by_ip_with_options(request, runtime)

    async def list_endpoints_by_ip_async(
        self,
        request: location_20150612_models.ListEndpointsByIpRequest,
    ) -> location_20150612_models.ListEndpointsByIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_endpoints_by_ip_with_options_async(request, runtime)
