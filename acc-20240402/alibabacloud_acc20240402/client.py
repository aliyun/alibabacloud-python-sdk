# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_acc20240402 import models as acc_20240402_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_image_cache_with_options(
        self,
        tmp_req: acc_20240402_models.CreateImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> acc_20240402_models.CreateImageCacheResponse:
        """
        @summary 创建镜像缓存
        
        @param tmp_req: CreateImageCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageCacheResponse
        """
        UtilClient.validate_model(tmp_req)
        request = acc_20240402_models.CreateImageCacheShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network_config):
            request.network_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network_config, 'NetworkConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_cache_name):
            query['ImageCacheName'] = request.image_cache_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.network_config_shrink):
            query['NetworkConfig'] = request.network_config_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageCache',
            version='2024-04-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acc_20240402_models.CreateImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_cache_with_options_async(
        self,
        tmp_req: acc_20240402_models.CreateImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> acc_20240402_models.CreateImageCacheResponse:
        """
        @summary 创建镜像缓存
        
        @param tmp_req: CreateImageCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageCacheResponse
        """
        UtilClient.validate_model(tmp_req)
        request = acc_20240402_models.CreateImageCacheShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network_config):
            request.network_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network_config, 'NetworkConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_cache_name):
            query['ImageCacheName'] = request.image_cache_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.network_config_shrink):
            query['NetworkConfig'] = request.network_config_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageCache',
            version='2024-04-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acc_20240402_models.CreateImageCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_cache(
        self,
        request: acc_20240402_models.CreateImageCacheRequest,
    ) -> acc_20240402_models.CreateImageCacheResponse:
        """
        @summary 创建镜像缓存
        
        @param request: CreateImageCacheRequest
        @return: CreateImageCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_image_cache_with_options(request, runtime)

    async def create_image_cache_async(
        self,
        request: acc_20240402_models.CreateImageCacheRequest,
    ) -> acc_20240402_models.CreateImageCacheResponse:
        """
        @summary 创建镜像缓存
        
        @param request: CreateImageCacheRequest
        @return: CreateImageCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_image_cache_with_options_async(request, runtime)

    def delete_image_cache_with_options(
        self,
        request: acc_20240402_models.DeleteImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> acc_20240402_models.DeleteImageCacheResponse:
        """
        @summary 删除镜像缓存
        
        @param request: DeleteImageCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteImageCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.image_cache_id):
            query['ImageCacheId'] = request.image_cache_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImageCache',
            version='2024-04-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acc_20240402_models.DeleteImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_cache_with_options_async(
        self,
        request: acc_20240402_models.DeleteImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> acc_20240402_models.DeleteImageCacheResponse:
        """
        @summary 删除镜像缓存
        
        @param request: DeleteImageCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteImageCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.image_cache_id):
            query['ImageCacheId'] = request.image_cache_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImageCache',
            version='2024-04-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acc_20240402_models.DeleteImageCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image_cache(
        self,
        request: acc_20240402_models.DeleteImageCacheRequest,
    ) -> acc_20240402_models.DeleteImageCacheResponse:
        """
        @summary 删除镜像缓存
        
        @param request: DeleteImageCacheRequest
        @return: DeleteImageCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_image_cache_with_options(request, runtime)

    async def delete_image_cache_async(
        self,
        request: acc_20240402_models.DeleteImageCacheRequest,
    ) -> acc_20240402_models.DeleteImageCacheResponse:
        """
        @summary 删除镜像缓存
        
        @param request: DeleteImageCacheRequest
        @return: DeleteImageCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_cache_with_options_async(request, runtime)

    def get_image_cache_with_options(
        self,
        request: acc_20240402_models.GetImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> acc_20240402_models.GetImageCacheResponse:
        """
        @summary 查询镜像缓存
        
        @param request: GetImageCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_cache_id):
            query['ImageCacheId'] = request.image_cache_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageCache',
            version='2024-04-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acc_20240402_models.GetImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_cache_with_options_async(
        self,
        request: acc_20240402_models.GetImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> acc_20240402_models.GetImageCacheResponse:
        """
        @summary 查询镜像缓存
        
        @param request: GetImageCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_cache_id):
            query['ImageCacheId'] = request.image_cache_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageCache',
            version='2024-04-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acc_20240402_models.GetImageCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_cache(
        self,
        request: acc_20240402_models.GetImageCacheRequest,
    ) -> acc_20240402_models.GetImageCacheResponse:
        """
        @summary 查询镜像缓存
        
        @param request: GetImageCacheRequest
        @return: GetImageCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_image_cache_with_options(request, runtime)

    async def get_image_cache_async(
        self,
        request: acc_20240402_models.GetImageCacheRequest,
    ) -> acc_20240402_models.GetImageCacheResponse:
        """
        @summary 查询镜像缓存
        
        @param request: GetImageCacheRequest
        @return: GetImageCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_image_cache_with_options_async(request, runtime)

    def list_image_caches_with_options(
        self,
        request: acc_20240402_models.ListImageCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> acc_20240402_models.ListImageCachesResponse:
        """
        @summary 查询镜像缓存
        
        @param request: ListImageCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImageCachesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_cache_name):
            query['ImageCacheName'] = request.image_cache_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImageCaches',
            version='2024-04-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acc_20240402_models.ListImageCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_image_caches_with_options_async(
        self,
        request: acc_20240402_models.ListImageCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> acc_20240402_models.ListImageCachesResponse:
        """
        @summary 查询镜像缓存
        
        @param request: ListImageCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImageCachesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_cache_name):
            query['ImageCacheName'] = request.image_cache_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImageCaches',
            version='2024-04-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acc_20240402_models.ListImageCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_image_caches(
        self,
        request: acc_20240402_models.ListImageCachesRequest,
    ) -> acc_20240402_models.ListImageCachesResponse:
        """
        @summary 查询镜像缓存
        
        @param request: ListImageCachesRequest
        @return: ListImageCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_image_caches_with_options(request, runtime)

    async def list_image_caches_async(
        self,
        request: acc_20240402_models.ListImageCachesRequest,
    ) -> acc_20240402_models.ListImageCachesResponse:
        """
        @summary 查询镜像缓存
        
        @param request: ListImageCachesRequest
        @return: ListImageCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_image_caches_with_options_async(request, runtime)
