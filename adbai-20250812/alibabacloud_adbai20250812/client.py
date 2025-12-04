# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_adbai20250812 import models as adbai20250812_models
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
        self._endpoint = self.get_endpoint('adbai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_embodied_aiplatform_with_options(
        self,
        tmp_req: adbai20250812_models.CreateEmbodiedAIPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adbai20250812_models.CreateEmbodiedAIPlatformResponse:
        """
        @summary 创建具身智能平台
        
        @param tmp_req: CreateEmbodiedAIPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEmbodiedAIPlatformResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adbai20250812_models.CreateEmbodiedAIPlatformShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ray_config):
            request.ray_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ray_config, 'RayConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not UtilClient.is_unset(request.ray_config_shrink):
            query['RayConfig'] = request.ray_config_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.webserver_spec_name):
            query['WebserverSpecName'] = request.webserver_spec_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEmbodiedAIPlatform',
            version='2025-08-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adbai20250812_models.CreateEmbodiedAIPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_embodied_aiplatform_with_options_async(
        self,
        tmp_req: adbai20250812_models.CreateEmbodiedAIPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adbai20250812_models.CreateEmbodiedAIPlatformResponse:
        """
        @summary 创建具身智能平台
        
        @param tmp_req: CreateEmbodiedAIPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEmbodiedAIPlatformResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adbai20250812_models.CreateEmbodiedAIPlatformShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ray_config):
            request.ray_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ray_config, 'RayConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not UtilClient.is_unset(request.ray_config_shrink):
            query['RayConfig'] = request.ray_config_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.webserver_spec_name):
            query['WebserverSpecName'] = request.webserver_spec_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEmbodiedAIPlatform',
            version='2025-08-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adbai20250812_models.CreateEmbodiedAIPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_embodied_aiplatform(
        self,
        request: adbai20250812_models.CreateEmbodiedAIPlatformRequest,
    ) -> adbai20250812_models.CreateEmbodiedAIPlatformResponse:
        """
        @summary 创建具身智能平台
        
        @param request: CreateEmbodiedAIPlatformRequest
        @return: CreateEmbodiedAIPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_embodied_aiplatform_with_options(request, runtime)

    async def create_embodied_aiplatform_async(
        self,
        request: adbai20250812_models.CreateEmbodiedAIPlatformRequest,
    ) -> adbai20250812_models.CreateEmbodiedAIPlatformResponse:
        """
        @summary 创建具身智能平台
        
        @param request: CreateEmbodiedAIPlatformRequest
        @return: CreateEmbodiedAIPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_embodied_aiplatform_with_options_async(request, runtime)

    def describe_embodied_aiplatforms_with_options(
        self,
        request: adbai20250812_models.DescribeEmbodiedAIPlatformsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adbai20250812_models.DescribeEmbodiedAIPlatformsResponse:
        """
        @summary 查询具身智能平台
        
        @param request: DescribeEmbodiedAIPlatformsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEmbodiedAIPlatformsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEmbodiedAIPlatforms',
            version='2025-08-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adbai20250812_models.DescribeEmbodiedAIPlatformsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_embodied_aiplatforms_with_options_async(
        self,
        request: adbai20250812_models.DescribeEmbodiedAIPlatformsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adbai20250812_models.DescribeEmbodiedAIPlatformsResponse:
        """
        @summary 查询具身智能平台
        
        @param request: DescribeEmbodiedAIPlatformsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEmbodiedAIPlatformsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEmbodiedAIPlatforms',
            version='2025-08-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adbai20250812_models.DescribeEmbodiedAIPlatformsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_embodied_aiplatforms(
        self,
        request: adbai20250812_models.DescribeEmbodiedAIPlatformsRequest,
    ) -> adbai20250812_models.DescribeEmbodiedAIPlatformsResponse:
        """
        @summary 查询具身智能平台
        
        @param request: DescribeEmbodiedAIPlatformsRequest
        @return: DescribeEmbodiedAIPlatformsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_embodied_aiplatforms_with_options(request, runtime)

    async def describe_embodied_aiplatforms_async(
        self,
        request: adbai20250812_models.DescribeEmbodiedAIPlatformsRequest,
    ) -> adbai20250812_models.DescribeEmbodiedAIPlatformsResponse:
        """
        @summary 查询具身智能平台
        
        @param request: DescribeEmbodiedAIPlatformsRequest
        @return: DescribeEmbodiedAIPlatformsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_embodied_aiplatforms_with_options_async(request, runtime)
