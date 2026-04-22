# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

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
        if not DaraCore.is_null(request.device_count):
            query['DeviceCount'] = request.device_count
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
        if not DaraCore.is_null(request.device_count):
            query['DeviceCount'] = request.device_count
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

    def delete_agent_platform_with_options(
        self,
        request: main_models.DeleteAgentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentPlatformResponse:
        request.validate()
        query = {}
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
            action = 'DeleteAgentPlatform',
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
            main_models.DeleteAgentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_platform_with_options_async(
        self,
        request: main_models.DeleteAgentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentPlatformResponse:
        request.validate()
        query = {}
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
            action = 'DeleteAgentPlatform',
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
            main_models.DeleteAgentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_platform(
        self,
        request: main_models.DeleteAgentPlatformRequest,
    ) -> main_models.DeleteAgentPlatformResponse:
        runtime = RuntimeOptions()
        return self.delete_agent_platform_with_options(request, runtime)

    async def delete_agent_platform_async(
        self,
        request: main_models.DeleteAgentPlatformRequest,
    ) -> main_models.DeleteAgentPlatformResponse:
        runtime = RuntimeOptions()
        return await self.delete_agent_platform_with_options_async(request, runtime)

    def delete_embodied_aiplatform_with_options(
        self,
        request: main_models.DeleteEmbodiedAIPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEmbodiedAIPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEmbodiedAIPlatform',
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
            main_models.DeleteEmbodiedAIPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_embodied_aiplatform_with_options_async(
        self,
        request: main_models.DeleteEmbodiedAIPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEmbodiedAIPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEmbodiedAIPlatform',
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
            main_models.DeleteEmbodiedAIPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_embodied_aiplatform(
        self,
        request: main_models.DeleteEmbodiedAIPlatformRequest,
    ) -> main_models.DeleteEmbodiedAIPlatformResponse:
        runtime = RuntimeOptions()
        return self.delete_embodied_aiplatform_with_options(request, runtime)

    async def delete_embodied_aiplatform_async(
        self,
        request: main_models.DeleteEmbodiedAIPlatformRequest,
    ) -> main_models.DeleteEmbodiedAIPlatformResponse:
        runtime = RuntimeOptions()
        return await self.delete_embodied_aiplatform_with_options_async(request, runtime)

    def describe_chat_message_with_sse(
        self,
        request: main_models.DescribeChatMessageRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.DescribeChatMessageResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChatMessage',
            version = '2025-08-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.DescribeChatMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def describe_chat_message_with_sse_async(
        self,
        request: main_models.DescribeChatMessageRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.DescribeChatMessageResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChatMessage',
            version = '2025-08-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.DescribeChatMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def describe_chat_message_with_options(
        self,
        request: main_models.DescribeChatMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChatMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChatMessage',
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
            main_models.DescribeChatMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_chat_message_with_options_async(
        self,
        request: main_models.DescribeChatMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChatMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChatMessage',
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
            main_models.DescribeChatMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_chat_message(
        self,
        request: main_models.DescribeChatMessageRequest,
    ) -> main_models.DescribeChatMessageResponse:
        runtime = RuntimeOptions()
        return self.describe_chat_message_with_options(request, runtime)

    async def describe_chat_message_async(
        self,
        request: main_models.DescribeChatMessageRequest,
    ) -> main_models.DescribeChatMessageResponse:
        runtime = RuntimeOptions()
        return await self.describe_chat_message_with_options_async(request, runtime)

    def describe_eap_device_resource_allocation_with_options(
        self,
        request: main_models.DescribeEapDeviceResourceAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEapDeviceResourceAllocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.device_count):
            query['DeviceCount'] = request.device_count
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEapDeviceResourceAllocation',
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
            main_models.DescribeEapDeviceResourceAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eap_device_resource_allocation_with_options_async(
        self,
        request: main_models.DescribeEapDeviceResourceAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEapDeviceResourceAllocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.device_count):
            query['DeviceCount'] = request.device_count
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEapDeviceResourceAllocation',
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
            main_models.DescribeEapDeviceResourceAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eap_device_resource_allocation(
        self,
        request: main_models.DescribeEapDeviceResourceAllocationRequest,
    ) -> main_models.DescribeEapDeviceResourceAllocationResponse:
        runtime = RuntimeOptions()
        return self.describe_eap_device_resource_allocation_with_options(request, runtime)

    async def describe_eap_device_resource_allocation_async(
        self,
        request: main_models.DescribeEapDeviceResourceAllocationRequest,
    ) -> main_models.DescribeEapDeviceResourceAllocationResponse:
        runtime = RuntimeOptions()
        return await self.describe_eap_device_resource_allocation_with_options_async(request, runtime)

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

    def get_embodied_aiplatform_resource_usage_info_with_options(
        self,
        request: main_models.GetEmbodiedAIPlatformResourceUsageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEmbodiedAIPlatformResourceUsageInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmbodiedAIPlatformResourceUsageInfo',
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
            main_models.GetEmbodiedAIPlatformResourceUsageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_embodied_aiplatform_resource_usage_info_with_options_async(
        self,
        request: main_models.GetEmbodiedAIPlatformResourceUsageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEmbodiedAIPlatformResourceUsageInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmbodiedAIPlatformResourceUsageInfo',
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
            main_models.GetEmbodiedAIPlatformResourceUsageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_embodied_aiplatform_resource_usage_info(
        self,
        request: main_models.GetEmbodiedAIPlatformResourceUsageInfoRequest,
    ) -> main_models.GetEmbodiedAIPlatformResourceUsageInfoResponse:
        runtime = RuntimeOptions()
        return self.get_embodied_aiplatform_resource_usage_info_with_options(request, runtime)

    async def get_embodied_aiplatform_resource_usage_info_async(
        self,
        request: main_models.GetEmbodiedAIPlatformResourceUsageInfoRequest,
    ) -> main_models.GetEmbodiedAIPlatformResourceUsageInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_embodied_aiplatform_resource_usage_info_with_options_async(request, runtime)

    def lock_embodied_aiplatform_with_options(
        self,
        request: main_models.LockEmbodiedAIPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LockEmbodiedAIPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LockEmbodiedAIPlatform',
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
            main_models.LockEmbodiedAIPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_embodied_aiplatform_with_options_async(
        self,
        request: main_models.LockEmbodiedAIPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LockEmbodiedAIPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LockEmbodiedAIPlatform',
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
            main_models.LockEmbodiedAIPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_embodied_aiplatform(
        self,
        request: main_models.LockEmbodiedAIPlatformRequest,
    ) -> main_models.LockEmbodiedAIPlatformResponse:
        runtime = RuntimeOptions()
        return self.lock_embodied_aiplatform_with_options(request, runtime)

    async def lock_embodied_aiplatform_async(
        self,
        request: main_models.LockEmbodiedAIPlatformRequest,
    ) -> main_models.LockEmbodiedAIPlatformResponse:
        runtime = RuntimeOptions()
        return await self.lock_embodied_aiplatform_with_options_async(request, runtime)

    def modify_agent_platform_with_options(
        self,
        tmp_req: main_models.ModifyAgentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAgentPlatformResponse:
        tmp_req.validate()
        request = main_models.ModifyAgentPlatformShrinkRequest()
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
            action = 'ModifyAgentPlatform',
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
            main_models.ModifyAgentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_agent_platform_with_options_async(
        self,
        tmp_req: main_models.ModifyAgentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAgentPlatformResponse:
        tmp_req.validate()
        request = main_models.ModifyAgentPlatformShrinkRequest()
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
            action = 'ModifyAgentPlatform',
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
            main_models.ModifyAgentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_agent_platform(
        self,
        request: main_models.ModifyAgentPlatformRequest,
    ) -> main_models.ModifyAgentPlatformResponse:
        runtime = RuntimeOptions()
        return self.modify_agent_platform_with_options(request, runtime)

    async def modify_agent_platform_async(
        self,
        request: main_models.ModifyAgentPlatformRequest,
    ) -> main_models.ModifyAgentPlatformResponse:
        runtime = RuntimeOptions()
        return await self.modify_agent_platform_with_options_async(request, runtime)

    def modify_embodied_aiplatform_with_options(
        self,
        tmp_req: main_models.ModifyEmbodiedAIPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEmbodiedAIPlatformResponse:
        tmp_req.validate()
        request = main_models.ModifyEmbodiedAIPlatformShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ray_config):
            request.ray_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ray_config, 'RayConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.device_count):
            query['DeviceCount'] = request.device_count
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
            action = 'ModifyEmbodiedAIPlatform',
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
            main_models.ModifyEmbodiedAIPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_embodied_aiplatform_with_options_async(
        self,
        tmp_req: main_models.ModifyEmbodiedAIPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEmbodiedAIPlatformResponse:
        tmp_req.validate()
        request = main_models.ModifyEmbodiedAIPlatformShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ray_config):
            request.ray_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ray_config, 'RayConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.device_count):
            query['DeviceCount'] = request.device_count
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
            action = 'ModifyEmbodiedAIPlatform',
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
            main_models.ModifyEmbodiedAIPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_embodied_aiplatform(
        self,
        request: main_models.ModifyEmbodiedAIPlatformRequest,
    ) -> main_models.ModifyEmbodiedAIPlatformResponse:
        runtime = RuntimeOptions()
        return self.modify_embodied_aiplatform_with_options(request, runtime)

    async def modify_embodied_aiplatform_async(
        self,
        request: main_models.ModifyEmbodiedAIPlatformRequest,
    ) -> main_models.ModifyEmbodiedAIPlatformResponse:
        runtime = RuntimeOptions()
        return await self.modify_embodied_aiplatform_with_options_async(request, runtime)

    def reset_embodied_aiplatform_password_with_options(
        self,
        request: main_models.ResetEmbodiedAIPlatformPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetEmbodiedAIPlatformPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetEmbodiedAIPlatformPassword',
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
            main_models.ResetEmbodiedAIPlatformPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_embodied_aiplatform_password_with_options_async(
        self,
        request: main_models.ResetEmbodiedAIPlatformPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetEmbodiedAIPlatformPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetEmbodiedAIPlatformPassword',
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
            main_models.ResetEmbodiedAIPlatformPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_embodied_aiplatform_password(
        self,
        request: main_models.ResetEmbodiedAIPlatformPasswordRequest,
    ) -> main_models.ResetEmbodiedAIPlatformPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_embodied_aiplatform_password_with_options(request, runtime)

    async def reset_embodied_aiplatform_password_async(
        self,
        request: main_models.ResetEmbodiedAIPlatformPasswordRequest,
    ) -> main_models.ResetEmbodiedAIPlatformPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_embodied_aiplatform_password_with_options_async(request, runtime)

    def unlock_embodied_aiplatform_with_options(
        self,
        request: main_models.UnlockEmbodiedAIPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockEmbodiedAIPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockEmbodiedAIPlatform',
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
            main_models.UnlockEmbodiedAIPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_embodied_aiplatform_with_options_async(
        self,
        request: main_models.UnlockEmbodiedAIPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockEmbodiedAIPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.platform_name):
            query['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockEmbodiedAIPlatform',
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
            main_models.UnlockEmbodiedAIPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_embodied_aiplatform(
        self,
        request: main_models.UnlockEmbodiedAIPlatformRequest,
    ) -> main_models.UnlockEmbodiedAIPlatformResponse:
        runtime = RuntimeOptions()
        return self.unlock_embodied_aiplatform_with_options(request, runtime)

    async def unlock_embodied_aiplatform_async(
        self,
        request: main_models.UnlockEmbodiedAIPlatformRequest,
    ) -> main_models.UnlockEmbodiedAIPlatformResponse:
        runtime = RuntimeOptions()
        return await self.unlock_embodied_aiplatform_with_options_async(request, runtime)
