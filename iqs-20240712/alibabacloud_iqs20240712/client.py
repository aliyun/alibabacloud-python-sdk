# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iqs20240712 import models as iqs20240712_models
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
        self._endpoint = self.get_endpoint('iqs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_attractions_with_options(
        self,
        request: iqs20240712_models.QueryAttractionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryAttractionsResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAttractionsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryAttractions',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/attractions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20240712_models.QueryAttractionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_attractions_with_options_async(
        self,
        request: iqs20240712_models.QueryAttractionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryAttractionsResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAttractionsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryAttractions',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/attractions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20240712_models.QueryAttractionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_attractions(
        self,
        request: iqs20240712_models.QueryAttractionsRequest,
    ) -> iqs20240712_models.QueryAttractionsResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsRequest
        @return: QueryAttractionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_attractions_with_options(request, headers, runtime)

    async def query_attractions_async(
        self,
        request: iqs20240712_models.QueryAttractionsRequest,
    ) -> iqs20240712_models.QueryAttractionsResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsRequest
        @return: QueryAttractionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_attractions_with_options_async(request, headers, runtime)

    def query_hotels_with_options(
        self,
        request: iqs20240712_models.QueryHotelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryHotelsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryHotelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotelsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryHotels',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/hotels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20240712_models.QueryHotelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hotels_with_options_async(
        self,
        request: iqs20240712_models.QueryHotelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryHotelsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryHotelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotelsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryHotels',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/hotels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20240712_models.QueryHotelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hotels(
        self,
        request: iqs20240712_models.QueryHotelsRequest,
    ) -> iqs20240712_models.QueryHotelsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryHotelsRequest
        @return: QueryHotelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_hotels_with_options(request, headers, runtime)

    async def query_hotels_async(
        self,
        request: iqs20240712_models.QueryHotelsRequest,
    ) -> iqs20240712_models.QueryHotelsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryHotelsRequest
        @return: QueryHotelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_hotels_with_options_async(request, headers, runtime)

    def query_restaurants_with_options(
        self,
        request: iqs20240712_models.QueryRestaurantsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryRestaurantsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRestaurantsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryRestaurants',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/restaurants',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20240712_models.QueryRestaurantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_restaurants_with_options_async(
        self,
        request: iqs20240712_models.QueryRestaurantsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryRestaurantsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRestaurantsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryRestaurants',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/restaurants',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20240712_models.QueryRestaurantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_restaurants(
        self,
        request: iqs20240712_models.QueryRestaurantsRequest,
    ) -> iqs20240712_models.QueryRestaurantsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsRequest
        @return: QueryRestaurantsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_restaurants_with_options(request, headers, runtime)

    async def query_restaurants_async(
        self,
        request: iqs20240712_models.QueryRestaurantsRequest,
    ) -> iqs20240712_models.QueryRestaurantsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsRequest
        @return: QueryRestaurantsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_restaurants_with_options_async(request, headers, runtime)
