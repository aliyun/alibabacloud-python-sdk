# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_trafficfxopen20240815 import models as traffic_fx_open_20240815_models
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
        self._endpoint = self.get_endpoint('trafficfxopen', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def convert_url_with_options(
        self,
        request: traffic_fx_open_20240815_models.ConvertUrlRequest,
        headers: traffic_fx_open_20240815_models.ConvertUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> traffic_fx_open_20240815_models.ConvertUrlResponse:
        """
        @summary 转换联登链接
        
        @param request: ConvertUrlRequest
        @param headers: ConvertUrlHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country_calling_code):
            body['countryCallingCode'] = request.country_calling_code
        if not UtilClient.is_unset(request.jump_url):
            body['jumpUrl'] = request.jump_url
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.third_id):
            body['thirdId'] = request.third_id
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
        if not UtilClient.is_unset(request.xenv):
            body['xenv'] = request.xenv
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['xAcsAirticketAccessToken'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['xAcsAirticketLanguage'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertUrl',
            version='2024-08-15',
            protocol='HTTPS',
            pathname=f'/v1/distribution/trade/convertUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            traffic_fx_open_20240815_models.ConvertUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_url_with_options_async(
        self,
        request: traffic_fx_open_20240815_models.ConvertUrlRequest,
        headers: traffic_fx_open_20240815_models.ConvertUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> traffic_fx_open_20240815_models.ConvertUrlResponse:
        """
        @summary 转换联登链接
        
        @param request: ConvertUrlRequest
        @param headers: ConvertUrlHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country_calling_code):
            body['countryCallingCode'] = request.country_calling_code
        if not UtilClient.is_unset(request.jump_url):
            body['jumpUrl'] = request.jump_url
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.third_id):
            body['thirdId'] = request.third_id
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
        if not UtilClient.is_unset(request.xenv):
            body['xenv'] = request.xenv
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['xAcsAirticketAccessToken'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['xAcsAirticketLanguage'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertUrl',
            version='2024-08-15',
            protocol='HTTPS',
            pathname=f'/v1/distribution/trade/convertUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            traffic_fx_open_20240815_models.ConvertUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_url(
        self,
        request: traffic_fx_open_20240815_models.ConvertUrlRequest,
    ) -> traffic_fx_open_20240815_models.ConvertUrlResponse:
        """
        @summary 转换联登链接
        
        @param request: ConvertUrlRequest
        @return: ConvertUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = traffic_fx_open_20240815_models.ConvertUrlHeaders()
        return self.convert_url_with_options(request, headers, runtime)

    async def convert_url_async(
        self,
        request: traffic_fx_open_20240815_models.ConvertUrlRequest,
    ) -> traffic_fx_open_20240815_models.ConvertUrlResponse:
        """
        @summary 转换联登链接
        
        @param request: ConvertUrlRequest
        @return: ConvertUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = traffic_fx_open_20240815_models.ConvertUrlHeaders()
        return await self.convert_url_with_options_async(request, headers, runtime)

    def get_token_with_options(
        self,
        request: traffic_fx_open_20240815_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> traffic_fx_open_20240815_models.GetTokenResponse:
        """
        @summary 创建token
        
        @param request: GetTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            query['appSecret'] = request.app_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2024-08-15',
            protocol='HTTPS',
            pathname=f'/v1/distribution/trade/getToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            traffic_fx_open_20240815_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: traffic_fx_open_20240815_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> traffic_fx_open_20240815_models.GetTokenResponse:
        """
        @summary 创建token
        
        @param request: GetTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            query['appSecret'] = request.app_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2024-08-15',
            protocol='HTTPS',
            pathname=f'/v1/distribution/trade/getToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            traffic_fx_open_20240815_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: traffic_fx_open_20240815_models.GetTokenRequest,
    ) -> traffic_fx_open_20240815_models.GetTokenResponse:
        """
        @summary 创建token
        
        @param request: GetTokenRequest
        @return: GetTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    async def get_token_async(
        self,
        request: traffic_fx_open_20240815_models.GetTokenRequest,
    ) -> traffic_fx_open_20240815_models.GetTokenResponse:
        """
        @summary 创建token
        
        @param request: GetTokenRequest
        @return: GetTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_token_with_options_async(request, headers, runtime)

    def search_with_options(
        self,
        request: traffic_fx_open_20240815_models.SearchRequest,
        headers: traffic_fx_open_20240815_models.SearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> traffic_fx_open_20240815_models.SearchResponse:
        """
        @summary 分销报价接口
        
        @param request: SearchRequest
        @param headers: SearchHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.search_param):
            body['searchParam'] = request.search_param
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.terminal):
            body['terminal'] = request.terminal
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['xAcsAirticketAccessToken'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['xAcsAirticketLanguage'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Search',
            version='2024-08-15',
            protocol='HTTPS',
            pathname=f'/v1/distribution/trade/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            traffic_fx_open_20240815_models.SearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_with_options_async(
        self,
        request: traffic_fx_open_20240815_models.SearchRequest,
        headers: traffic_fx_open_20240815_models.SearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> traffic_fx_open_20240815_models.SearchResponse:
        """
        @summary 分销报价接口
        
        @param request: SearchRequest
        @param headers: SearchHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.search_param):
            body['searchParam'] = request.search_param
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.terminal):
            body['terminal'] = request.terminal
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['xAcsAirticketAccessToken'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['xAcsAirticketLanguage'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Search',
            version='2024-08-15',
            protocol='HTTPS',
            pathname=f'/v1/distribution/trade/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            traffic_fx_open_20240815_models.SearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search(
        self,
        request: traffic_fx_open_20240815_models.SearchRequest,
    ) -> traffic_fx_open_20240815_models.SearchResponse:
        """
        @summary 分销报价接口
        
        @param request: SearchRequest
        @return: SearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = traffic_fx_open_20240815_models.SearchHeaders()
        return self.search_with_options(request, headers, runtime)

    async def search_async(
        self,
        request: traffic_fx_open_20240815_models.SearchRequest,
    ) -> traffic_fx_open_20240815_models.SearchResponse:
        """
        @summary 分销报价接口
        
        @param request: SearchRequest
        @return: SearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = traffic_fx_open_20240815_models.SearchHeaders()
        return await self.search_with_options_async(request, headers, runtime)
