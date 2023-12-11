# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cdt20210813 import models as cdt20210813_models
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
        self._endpoint = self.get_endpoint('cdt', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_regions_with_options(
        self,
        request: cdt20210813_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: cdt20210813_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: cdt20210813_models.DescribeRegionsRequest,
    ) -> cdt20210813_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: cdt20210813_models.DescribeRegionsRequest,
    ) -> cdt20210813_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def get_cdt_cb_service_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.GetCdtCbServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCdtCbServiceStatus',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.GetCdtCbServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cdt_cb_service_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.GetCdtCbServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCdtCbServiceStatus',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.GetCdtCbServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cdt_cb_service_status(self) -> cdt20210813_models.GetCdtCbServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cdt_cb_service_status_with_options(runtime)

    async def get_cdt_cb_service_status_async(self) -> cdt20210813_models.GetCdtCbServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cdt_cb_service_status_with_options_async(runtime)

    def get_cdt_internet_service_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.GetCdtInternetServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCdtInternetServiceStatus',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.GetCdtInternetServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cdt_internet_service_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.GetCdtInternetServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCdtInternetServiceStatus',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.GetCdtInternetServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cdt_internet_service_status(self) -> cdt20210813_models.GetCdtInternetServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cdt_internet_service_status_with_options(runtime)

    async def get_cdt_internet_service_status_async(self) -> cdt20210813_models.GetCdtInternetServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cdt_internet_service_status_with_options_async(runtime)

    def get_cdt_service_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.GetCdtServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCdtServiceStatus',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.GetCdtServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cdt_service_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.GetCdtServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCdtServiceStatus',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.GetCdtServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cdt_service_status(self) -> cdt20210813_models.GetCdtServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cdt_service_status_with_options(runtime)

    async def get_cdt_service_status_async(self) -> cdt20210813_models.GetCdtServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cdt_service_status_with_options_async(runtime)

    def list_cdt_cross_bord_traffic_with_options(
        self,
        request: cdt20210813_models.ListCdtCrossBordTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.ListCdtCrossBordTrafficResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCdtCrossBordTraffic',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.ListCdtCrossBordTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cdt_cross_bord_traffic_with_options_async(
        self,
        request: cdt20210813_models.ListCdtCrossBordTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.ListCdtCrossBordTrafficResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCdtCrossBordTraffic',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.ListCdtCrossBordTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cdt_cross_bord_traffic(
        self,
        request: cdt20210813_models.ListCdtCrossBordTrafficRequest,
    ) -> cdt20210813_models.ListCdtCrossBordTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cdt_cross_bord_traffic_with_options(request, runtime)

    async def list_cdt_cross_bord_traffic_async(
        self,
        request: cdt20210813_models.ListCdtCrossBordTrafficRequest,
    ) -> cdt20210813_models.ListCdtCrossBordTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cdt_cross_bord_traffic_with_options_async(request, runtime)

    def list_cdt_internet_traffic_with_options(
        self,
        request: cdt20210813_models.ListCdtInternetTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.ListCdtInternetTrafficResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCdtInternetTraffic',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.ListCdtInternetTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cdt_internet_traffic_with_options_async(
        self,
        request: cdt20210813_models.ListCdtInternetTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.ListCdtInternetTrafficResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCdtInternetTraffic',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.ListCdtInternetTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cdt_internet_traffic(
        self,
        request: cdt20210813_models.ListCdtInternetTrafficRequest,
    ) -> cdt20210813_models.ListCdtInternetTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cdt_internet_traffic_with_options(request, runtime)

    async def list_cdt_internet_traffic_async(
        self,
        request: cdt20210813_models.ListCdtInternetTrafficRequest,
    ) -> cdt20210813_models.ListCdtInternetTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cdt_internet_traffic_with_options_async(request, runtime)

    def list_cdt_products_with_options(
        self,
        request: cdt20210813_models.ListCdtProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.ListCdtProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCdtProducts',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.ListCdtProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cdt_products_with_options_async(
        self,
        request: cdt20210813_models.ListCdtProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.ListCdtProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCdtProducts',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.ListCdtProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cdt_products(
        self,
        request: cdt20210813_models.ListCdtProductsRequest,
    ) -> cdt20210813_models.ListCdtProductsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cdt_products_with_options(request, runtime)

    async def list_cdt_products_async(
        self,
        request: cdt20210813_models.ListCdtProductsRequest,
    ) -> cdt20210813_models.ListCdtProductsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cdt_products_with_options_async(request, runtime)

    def list_cdt_traffic_tiers_with_options(
        self,
        request: cdt20210813_models.ListCdtTrafficTiersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.ListCdtTrafficTiersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCdtTrafficTiers',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.ListCdtTrafficTiersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cdt_traffic_tiers_with_options_async(
        self,
        request: cdt20210813_models.ListCdtTrafficTiersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.ListCdtTrafficTiersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCdtTrafficTiers',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.ListCdtTrafficTiersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cdt_traffic_tiers(
        self,
        request: cdt20210813_models.ListCdtTrafficTiersRequest,
    ) -> cdt20210813_models.ListCdtTrafficTiersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cdt_traffic_tiers_with_options(request, runtime)

    async def list_cdt_traffic_tiers_async(
        self,
        request: cdt20210813_models.ListCdtTrafficTiersRequest,
    ) -> cdt20210813_models.ListCdtTrafficTiersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cdt_traffic_tiers_with_options_async(request, runtime)

    def list_switched_cdt_products_with_options(
        self,
        request: cdt20210813_models.ListSwitchedCdtProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.ListSwitchedCdtProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSwitchedCdtProducts',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.ListSwitchedCdtProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_switched_cdt_products_with_options_async(
        self,
        request: cdt20210813_models.ListSwitchedCdtProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.ListSwitchedCdtProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSwitchedCdtProducts',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.ListSwitchedCdtProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_switched_cdt_products(
        self,
        request: cdt20210813_models.ListSwitchedCdtProductsRequest,
    ) -> cdt20210813_models.ListSwitchedCdtProductsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_switched_cdt_products_with_options(request, runtime)

    async def list_switched_cdt_products_async(
        self,
        request: cdt20210813_models.ListSwitchedCdtProductsRequest,
    ) -> cdt20210813_models.ListSwitchedCdtProductsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_switched_cdt_products_with_options_async(request, runtime)

    def open_cdt_cb_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.OpenCdtCbServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenCdtCbService',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.OpenCdtCbServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_cdt_cb_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.OpenCdtCbServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenCdtCbService',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.OpenCdtCbServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_cdt_cb_service(self) -> cdt20210813_models.OpenCdtCbServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_cdt_cb_service_with_options(runtime)

    async def open_cdt_cb_service_async(self) -> cdt20210813_models.OpenCdtCbServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_cdt_cb_service_with_options_async(runtime)

    def open_cdt_internet_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.OpenCdtInternetServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenCdtInternetService',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.OpenCdtInternetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_cdt_internet_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.OpenCdtInternetServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenCdtInternetService',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.OpenCdtInternetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_cdt_internet_service(self) -> cdt20210813_models.OpenCdtInternetServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_cdt_internet_service_with_options(runtime)

    async def open_cdt_internet_service_async(self) -> cdt20210813_models.OpenCdtInternetServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_cdt_internet_service_with_options_async(runtime)

    def open_cdt_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.OpenCdtServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenCdtService',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.OpenCdtServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_cdt_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.OpenCdtServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenCdtService',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.OpenCdtServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_cdt_service(self) -> cdt20210813_models.OpenCdtServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_cdt_service_with_options(runtime)

    async def open_cdt_service_async(self) -> cdt20210813_models.OpenCdtServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_cdt_service_with_options_async(runtime)

    def switch_to_cdt_with_options(
        self,
        request: cdt20210813_models.SwitchToCdtRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.SwitchToCdtResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_type):
            query['BillingType'] = request.billing_type
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchToCdt',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.SwitchToCdtResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_to_cdt_with_options_async(
        self,
        request: cdt20210813_models.SwitchToCdtRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdt20210813_models.SwitchToCdtResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_type):
            query['BillingType'] = request.billing_type
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchToCdt',
            version='2021-08-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdt20210813_models.SwitchToCdtResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_to_cdt(
        self,
        request: cdt20210813_models.SwitchToCdtRequest,
    ) -> cdt20210813_models.SwitchToCdtResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_to_cdt_with_options(request, runtime)

    async def switch_to_cdt_async(
        self,
        request: cdt20210813_models.SwitchToCdtRequest,
    ) -> cdt20210813_models.SwitchToCdtResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_to_cdt_with_options_async(request, runtime)
