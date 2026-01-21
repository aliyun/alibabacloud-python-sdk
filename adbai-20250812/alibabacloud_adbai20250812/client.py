# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_adbai20250812 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_agent_platform_with_options(
        self,
        tmp_req: main_models.CreateAgentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentPlatformResponse:
        tmp_req.validate()
        request = main_models.CreateAgentPlatformShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ai_platform_config):
            request.ai_platform_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ai_platform_config, 'AiPlatformConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.ai_platform_config_shrink):
            query['AiPlatformConfig'] = request.ai_platform_config_shrink
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentPlatform',
            version = '2025-08-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_platform_with_options_async(
        self,
        tmp_req: main_models.CreateAgentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentPlatformResponse:
        tmp_req.validate()
        request = main_models.CreateAgentPlatformShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ai_platform_config):
            request.ai_platform_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ai_platform_config, 'AiPlatformConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.ai_platform_config_shrink):
            query['AiPlatformConfig'] = request.ai_platform_config_shrink
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentPlatform',
            version = '2025-08-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_platform(
        self,
        request: main_models.CreateAgentPlatformRequest,
    ) -> main_models.CreateAgentPlatformResponse:
        runtime = RuntimeOptions()
        return self.create_agent_platform_with_options(request, runtime)

    async def create_agent_platform_async(
        self,
        request: main_models.CreateAgentPlatformRequest,
    ) -> main_models.CreateAgentPlatformResponse:
        runtime = RuntimeOptions()
        return await self.create_agent_platform_with_options_async(request, runtime)

    def create_embodied_aiplatform_with_options(
        self,
        tmp_req: main_models.CreateEmbodiedAIPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEmbodiedAIPlatformResponse:
        tmp_req.validate()
        request = main_models.CreateEmbodiedAIPlatformShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ray_config):
            request.ray_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ray_config, 'RayConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.ray_config_shrink):
            query['RayConfig'] = request.ray_config_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.webserver_spec_name):
            query['WebserverSpecName'] = request.webserver_spec_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEmbodiedAIPlatform',
            version = '2025-08-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEmbodiedAIPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_embodied_aiplatform_with_options_async(
        self,
        tmp_req: main_models.CreateEmbodiedAIPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEmbodiedAIPlatformResponse:
        tmp_req.validate()
        request = main_models.CreateEmbodiedAIPlatformShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ray_config):
            request.ray_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ray_config, 'RayConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.ray_config_shrink):
            query['RayConfig'] = request.ray_config_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.webserver_spec_name):
            query['WebserverSpecName'] = request.webserver_spec_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEmbodiedAIPlatform',
            version = '2025-08-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEmbodiedAIPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_embodied_aiplatform(
        self,
        request: main_models.CreateEmbodiedAIPlatformRequest,
    ) -> main_models.CreateEmbodiedAIPlatformResponse:
        runtime = RuntimeOptions()
        return self.create_embodied_aiplatform_with_options(request, runtime)

    async def create_embodied_aiplatform_async(
        self,
        request: main_models.CreateEmbodiedAIPlatformRequest,
    ) -> main_models.CreateEmbodiedAIPlatformResponse:
        runtime = RuntimeOptions()
        return await self.create_embodied_aiplatform_with_options_async(request, runtime)

    def describe_embodied_aiplatforms_with_options(
        self,
        request: main_models.DescribeEmbodiedAIPlatformsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEmbodiedAIPlatformsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEmbodiedAIPlatforms',
            version = '2025-08-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEmbodiedAIPlatformsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_embodied_aiplatforms_with_options_async(
        self,
        request: main_models.DescribeEmbodiedAIPlatformsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEmbodiedAIPlatformsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEmbodiedAIPlatforms',
            version = '2025-08-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEmbodiedAIPlatformsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_embodied_aiplatforms(
        self,
        request: main_models.DescribeEmbodiedAIPlatformsRequest,
    ) -> main_models.DescribeEmbodiedAIPlatformsResponse:
        runtime = RuntimeOptions()
        return self.describe_embodied_aiplatforms_with_options(request, runtime)

    async def describe_embodied_aiplatforms_async(
        self,
        request: main_models.DescribeEmbodiedAIPlatformsRequest,
    ) -> main_models.DescribeEmbodiedAIPlatformsResponse:
        runtime = RuntimeOptions()
        return await self.describe_embodied_aiplatforms_with_options_async(request, runtime)
