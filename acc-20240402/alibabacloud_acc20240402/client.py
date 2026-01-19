# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_acc20240402 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
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
        self._endpoint_map = {
            'ap-northeast-2-pop': 'acc.aliyuncs.com',
            'ap-south-1': 'acc.aliyuncs.com',
            'ap-southeast-2': 'acc.aliyuncs.com',
            'cn-beijing-finance-1': 'acc.aliyuncs.com',
            'cn-beijing-finance-pop': 'acc.aliyuncs.com',
            'cn-beijing-gov-1': 'acc.aliyuncs.com',
            'cn-beijing-nu16-b01': 'acc.aliyuncs.com',
            'cn-edge-1': 'acc.aliyuncs.com',
            'cn-fujian': 'acc.aliyuncs.com',
            'cn-haidian-cm12-c01': 'acc.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'acc.aliyuncs.com',
            'cn-hangzhou-finance': 'acc.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'acc.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'acc.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'acc.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'acc.aliyuncs.com',
            'cn-hangzhou-test-306': 'acc.aliyuncs.com',
            'cn-hongkong-finance-pop': 'acc.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'acc.aliyuncs.com',
            'cn-qingdao-nebula': 'acc.aliyuncs.com',
            'cn-shanghai-et15-b01': 'acc.aliyuncs.com',
            'cn-shanghai-et2-b01': 'acc.aliyuncs.com',
            'cn-shanghai-inner': 'acc.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'acc.aliyuncs.com',
            'cn-shenzhen-finance-1': 'acc.aliyuncs.com',
            'cn-shenzhen-inner': 'acc.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'acc.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'acc.aliyuncs.com',
            'cn-wuhan': 'acc.aliyuncs.com',
            'cn-yushanfang': 'acc.aliyuncs.com',
            'cn-zhangbei': 'acc.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'acc.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'acc.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'acc.aliyuncs.com',
            'eu-west-1-oxs': 'acc.aliyuncs.com',
            'rus-west-1-pop': 'acc.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('acc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_image_cache_with_options(
        self,
        tmp_req: main_models.CreateImageCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageCacheResponse:
        tmp_req.validate()
        request = main_models.CreateImageCacheShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network_config):
            request.network_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_config, 'NetworkConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_cache_name):
            query['ImageCacheName'] = request.image_cache_name
        if not DaraCore.is_null(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.network_config_shrink):
            query['NetworkConfig'] = request.network_config_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageCache',
            version = '2024-04-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_cache_with_options_async(
        self,
        tmp_req: main_models.CreateImageCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageCacheResponse:
        tmp_req.validate()
        request = main_models.CreateImageCacheShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network_config):
            request.network_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_config, 'NetworkConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_cache_name):
            query['ImageCacheName'] = request.image_cache_name
        if not DaraCore.is_null(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.network_config_shrink):
            query['NetworkConfig'] = request.network_config_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageCache',
            version = '2024-04-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_cache(
        self,
        request: main_models.CreateImageCacheRequest,
    ) -> main_models.CreateImageCacheResponse:
        runtime = RuntimeOptions()
        return self.create_image_cache_with_options(request, runtime)

    async def create_image_cache_async(
        self,
        request: main_models.CreateImageCacheRequest,
    ) -> main_models.CreateImageCacheResponse:
        runtime = RuntimeOptions()
        return await self.create_image_cache_with_options_async(request, runtime)

    def delete_image_cache_with_options(
        self,
        request: main_models.DeleteImageCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImageCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.image_cache_id):
            query['ImageCacheId'] = request.image_cache_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImageCache',
            version = '2024-04-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_cache_with_options_async(
        self,
        request: main_models.DeleteImageCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImageCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.image_cache_id):
            query['ImageCacheId'] = request.image_cache_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImageCache',
            version = '2024-04-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImageCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image_cache(
        self,
        request: main_models.DeleteImageCacheRequest,
    ) -> main_models.DeleteImageCacheResponse:
        runtime = RuntimeOptions()
        return self.delete_image_cache_with_options(request, runtime)

    async def delete_image_cache_async(
        self,
        request: main_models.DeleteImageCacheRequest,
    ) -> main_models.DeleteImageCacheResponse:
        runtime = RuntimeOptions()
        return await self.delete_image_cache_with_options_async(request, runtime)

    def get_image_cache_with_options(
        self,
        request: main_models.GetImageCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_cache_id):
            query['ImageCacheId'] = request.image_cache_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageCache',
            version = '2024-04-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_cache_with_options_async(
        self,
        request: main_models.GetImageCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_cache_id):
            query['ImageCacheId'] = request.image_cache_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageCache',
            version = '2024-04-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_cache(
        self,
        request: main_models.GetImageCacheRequest,
    ) -> main_models.GetImageCacheResponse:
        runtime = RuntimeOptions()
        return self.get_image_cache_with_options(request, runtime)

    async def get_image_cache_async(
        self,
        request: main_models.GetImageCacheRequest,
    ) -> main_models.GetImageCacheResponse:
        runtime = RuntimeOptions()
        return await self.get_image_cache_with_options_async(request, runtime)

    def list_image_caches_with_options(
        self,
        request: main_models.ListImageCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImageCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_cache_name):
            query['ImageCacheName'] = request.image_cache_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImageCaches',
            version = '2024-04-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImageCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_image_caches_with_options_async(
        self,
        request: main_models.ListImageCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImageCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_cache_name):
            query['ImageCacheName'] = request.image_cache_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImageCaches',
            version = '2024-04-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImageCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_image_caches(
        self,
        request: main_models.ListImageCachesRequest,
    ) -> main_models.ListImageCachesResponse:
        runtime = RuntimeOptions()
        return self.list_image_caches_with_options(request, runtime)

    async def list_image_caches_async(
        self,
        request: main_models.ListImageCachesRequest,
    ) -> main_models.ListImageCachesResponse:
        runtime = RuntimeOptions()
        return await self.list_image_caches_with_options_async(request, runtime)
