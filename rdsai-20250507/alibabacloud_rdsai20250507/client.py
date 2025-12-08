# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_rdsai20250507 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
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
        self._endpoint = self.get_endpoint('rdsai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def chat_messages_with_sse(
        self,
        tmp_req: main_models.ChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ChatMessagesResponse, None, None]:
        tmp_req.validate()
        request = main_models.ChatMessagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.inputs):
            request.inputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.inputs_shrink):
            query['Inputs'] = request.inputs_shrink
        if not DaraCore.is_null(request.parent_message_id):
            query['ParentMessageId'] = request.parent_message_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatMessages',
            version = '2025-05-07',
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
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.ChatMessagesResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def chat_messages_with_sse_async(
        self,
        tmp_req: main_models.ChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ChatMessagesResponse, None, None]:
        tmp_req.validate()
        request = main_models.ChatMessagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.inputs):
            request.inputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.inputs_shrink):
            query['Inputs'] = request.inputs_shrink
        if not DaraCore.is_null(request.parent_message_id):
            query['ParentMessageId'] = request.parent_message_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatMessages',
            version = '2025-05-07',
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
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.ChatMessagesResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def chat_messages_with_options(
        self,
        tmp_req: main_models.ChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatMessagesResponse:
        tmp_req.validate()
        request = main_models.ChatMessagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.inputs):
            request.inputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.inputs_shrink):
            query['Inputs'] = request.inputs_shrink
        if not DaraCore.is_null(request.parent_message_id):
            query['ParentMessageId'] = request.parent_message_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatMessages',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_messages_with_options_async(
        self,
        tmp_req: main_models.ChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatMessagesResponse:
        tmp_req.validate()
        request = main_models.ChatMessagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.inputs):
            request.inputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.inputs_shrink):
            query['Inputs'] = request.inputs_shrink
        if not DaraCore.is_null(request.parent_message_id):
            query['ParentMessageId'] = request.parent_message_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatMessages',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_messages(
        self,
        request: main_models.ChatMessagesRequest,
    ) -> main_models.ChatMessagesResponse:
        runtime = RuntimeOptions()
        return self.chat_messages_with_options(request, runtime)

    async def chat_messages_async(
        self,
        request: main_models.ChatMessagesRequest,
    ) -> main_models.ChatMessagesResponse:
        runtime = RuntimeOptions()
        return await self.chat_messages_with_options_async(request, runtime)

    def chat_messages_task_stop_with_options(
        self,
        request: main_models.ChatMessagesTaskStopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatMessagesTaskStopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatMessagesTaskStop',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatMessagesTaskStopResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_messages_task_stop_with_options_async(
        self,
        request: main_models.ChatMessagesTaskStopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatMessagesTaskStopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatMessagesTaskStop',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatMessagesTaskStopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_messages_task_stop(
        self,
        request: main_models.ChatMessagesTaskStopRequest,
    ) -> main_models.ChatMessagesTaskStopResponse:
        runtime = RuntimeOptions()
        return self.chat_messages_task_stop_with_options(request, runtime)

    async def chat_messages_task_stop_async(
        self,
        request: main_models.ChatMessagesTaskStopRequest,
    ) -> main_models.ChatMessagesTaskStopResponse:
        runtime = RuntimeOptions()
        return await self.chat_messages_task_stop_with_options_async(request, runtime)

    def create_app_instance_with_options(
        self,
        tmp_req: main_models.CreateAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateAppInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dbinstance_config):
            request.dbinstance_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbinstance_config, 'DBInstanceConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_config_shrink):
            query['DBInstanceConfig'] = request.dbinstance_config_shrink
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not DaraCore.is_null(request.dashboard_username):
            query['DashboardUsername'] = request.dashboard_username
        if not DaraCore.is_null(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.public_endpoint_enabled):
            query['PublicEndpointEnabled'] = request.public_endpoint_enabled
        if not DaraCore.is_null(request.public_network_access_enabled):
            query['PublicNetworkAccessEnabled'] = request.public_network_access_enabled
        if not DaraCore.is_null(request.ragenabled):
            query['RAGEnabled'] = request.ragenabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstance',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_instance_with_options_async(
        self,
        tmp_req: main_models.CreateAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateAppInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dbinstance_config):
            request.dbinstance_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbinstance_config, 'DBInstanceConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_config_shrink):
            query['DBInstanceConfig'] = request.dbinstance_config_shrink
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not DaraCore.is_null(request.dashboard_username):
            query['DashboardUsername'] = request.dashboard_username
        if not DaraCore.is_null(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.public_endpoint_enabled):
            query['PublicEndpointEnabled'] = request.public_endpoint_enabled
        if not DaraCore.is_null(request.public_network_access_enabled):
            query['PublicNetworkAccessEnabled'] = request.public_network_access_enabled
        if not DaraCore.is_null(request.ragenabled):
            query['RAGEnabled'] = request.ragenabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstance',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_instance(
        self,
        request: main_models.CreateAppInstanceRequest,
    ) -> main_models.CreateAppInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_app_instance_with_options(request, runtime)

    async def create_app_instance_async(
        self,
        request: main_models.CreateAppInstanceRequest,
    ) -> main_models.CreateAppInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_app_instance_with_options_async(request, runtime)

    def create_custom_agent_with_options(
        self,
        tmp_req: main_models.CreateCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomAgentResponse:
        tmp_req.validate()
        request = main_models.CreateCustomAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tools):
            request.tools_shrink = Utils.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not DaraCore.is_null(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.system_prompt):
            query['SystemPrompt'] = request.system_prompt
        if not DaraCore.is_null(request.tools_shrink):
            query['Tools'] = request.tools_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomAgent',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_agent_with_options_async(
        self,
        tmp_req: main_models.CreateCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomAgentResponse:
        tmp_req.validate()
        request = main_models.CreateCustomAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tools):
            request.tools_shrink = Utils.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not DaraCore.is_null(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.system_prompt):
            query['SystemPrompt'] = request.system_prompt
        if not DaraCore.is_null(request.tools_shrink):
            query['Tools'] = request.tools_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomAgent',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_agent(
        self,
        request: main_models.CreateCustomAgentRequest,
    ) -> main_models.CreateCustomAgentResponse:
        runtime = RuntimeOptions()
        return self.create_custom_agent_with_options(request, runtime)

    async def create_custom_agent_async(
        self,
        request: main_models.CreateCustomAgentRequest,
    ) -> main_models.CreateCustomAgentResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_agent_with_options_async(request, runtime)

    def delete_app_instance_with_options(
        self,
        request: main_models.DeleteAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppInstance',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_instance_with_options_async(
        self,
        request: main_models.DeleteAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppInstance',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_instance(
        self,
        request: main_models.DeleteAppInstanceRequest,
    ) -> main_models.DeleteAppInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_app_instance_with_options(request, runtime)

    async def delete_app_instance_async(
        self,
        request: main_models.DeleteAppInstanceRequest,
    ) -> main_models.DeleteAppInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_instance_with_options_async(request, runtime)

    def delete_custom_agent_with_options(
        self,
        request: main_models.DeleteCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomAgent',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_agent_with_options_async(
        self,
        request: main_models.DeleteCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomAgent',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_agent(
        self,
        request: main_models.DeleteCustomAgentRequest,
    ) -> main_models.DeleteCustomAgentResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_agent_with_options(request, runtime)

    async def delete_custom_agent_async(
        self,
        request: main_models.DeleteCustomAgentRequest,
    ) -> main_models.DeleteCustomAgentResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_agent_with_options_async(request, runtime)

    def describe_app_instance_attribute_with_options(
        self,
        request: main_models.DescribeAppInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppInstanceAttribute',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_instance_attribute_with_options_async(
        self,
        request: main_models.DescribeAppInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppInstanceAttribute',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_instance_attribute(
        self,
        request: main_models.DescribeAppInstanceAttributeRequest,
    ) -> main_models.DescribeAppInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_app_instance_attribute_with_options(request, runtime)

    async def describe_app_instance_attribute_async(
        self,
        request: main_models.DescribeAppInstanceAttributeRequest,
    ) -> main_models.DescribeAppInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_instance_attribute_with_options_async(request, runtime)

    def describe_app_instances_with_options(
        self,
        request: main_models.DescribeAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppInstances',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_instances_with_options_async(
        self,
        request: main_models.DescribeAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppInstances',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_instances(
        self,
        request: main_models.DescribeAppInstancesRequest,
    ) -> main_models.DescribeAppInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_app_instances_with_options(request, runtime)

    async def describe_app_instances_async(
        self,
        request: main_models.DescribeAppInstancesRequest,
    ) -> main_models.DescribeAppInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_instances_with_options_async(request, runtime)

    def describe_events_list_with_options(
        self,
        request: main_models.DescribeEventsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventsList',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_list_with_options_async(
        self,
        request: main_models.DescribeEventsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventsList',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events_list(
        self,
        request: main_models.DescribeEventsListRequest,
    ) -> main_models.DescribeEventsListResponse:
        runtime = RuntimeOptions()
        return self.describe_events_list_with_options(request, runtime)

    async def describe_events_list_async(
        self,
        request: main_models.DescribeEventsListRequest,
    ) -> main_models.DescribeEventsListResponse:
        runtime = RuntimeOptions()
        return await self.describe_events_list_with_options_async(request, runtime)

    def describe_instance_auth_info_with_options(
        self,
        request: main_models.DescribeInstanceAuthInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAuthInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAuthInfo',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAuthInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_auth_info_with_options_async(
        self,
        request: main_models.DescribeInstanceAuthInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAuthInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAuthInfo',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAuthInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_auth_info(
        self,
        request: main_models.DescribeInstanceAuthInfoRequest,
    ) -> main_models.DescribeInstanceAuthInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_auth_info_with_options(request, runtime)

    async def describe_instance_auth_info_async(
        self,
        request: main_models.DescribeInstanceAuthInfoRequest,
    ) -> main_models.DescribeInstanceAuthInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_auth_info_with_options_async(request, runtime)

    def describe_instance_endpoints_with_options(
        self,
        request: main_models.DescribeInstanceEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceEndpoints',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_endpoints_with_options_async(
        self,
        request: main_models.DescribeInstanceEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceEndpoints',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_endpoints(
        self,
        request: main_models.DescribeInstanceEndpointsRequest,
    ) -> main_models.DescribeInstanceEndpointsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_endpoints_with_options(request, runtime)

    async def describe_instance_endpoints_async(
        self,
        request: main_models.DescribeInstanceEndpointsRequest,
    ) -> main_models.DescribeInstanceEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_endpoints_with_options_async(request, runtime)

    def describe_instance_ip_whitelist_with_options(
        self,
        request: main_models.DescribeInstanceIpWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceIpWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceIpWhitelist',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_ip_whitelist_with_options_async(
        self,
        request: main_models.DescribeInstanceIpWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceIpWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceIpWhitelist',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ip_whitelist(
        self,
        request: main_models.DescribeInstanceIpWhitelistRequest,
    ) -> main_models.DescribeInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_ip_whitelist_with_options(request, runtime)

    async def describe_instance_ip_whitelist_async(
        self,
        request: main_models.DescribeInstanceIpWhitelistRequest,
    ) -> main_models.DescribeInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_ip_whitelist_with_options_async(request, runtime)

    def describe_instance_ragconfig_with_options(
        self,
        request: main_models.DescribeInstanceRAGConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceRAGConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceRAGConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceRAGConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_ragconfig_with_options_async(
        self,
        request: main_models.DescribeInstanceRAGConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceRAGConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceRAGConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceRAGConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ragconfig(
        self,
        request: main_models.DescribeInstanceRAGConfigRequest,
    ) -> main_models.DescribeInstanceRAGConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_ragconfig_with_options(request, runtime)

    async def describe_instance_ragconfig_async(
        self,
        request: main_models.DescribeInstanceRAGConfigRequest,
    ) -> main_models.DescribeInstanceRAGConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_ragconfig_with_options_async(request, runtime)

    def describe_instance_sslwith_options(
        self,
        request: main_models.DescribeInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSSL',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_sslwith_options_async(
        self,
        request: main_models.DescribeInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSSL',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ssl(
        self,
        request: main_models.DescribeInstanceSSLRequest,
    ) -> main_models.DescribeInstanceSSLResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_sslwith_options(request, runtime)

    async def describe_instance_ssl_async(
        self,
        request: main_models.DescribeInstanceSSLRequest,
    ) -> main_models.DescribeInstanceSSLResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_sslwith_options_async(request, runtime)

    def describe_instance_storage_config_with_options(
        self,
        request: main_models.DescribeInstanceStorageConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceStorageConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceStorageConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceStorageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_storage_config_with_options_async(
        self,
        request: main_models.DescribeInstanceStorageConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceStorageConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceStorageConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceStorageConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_storage_config(
        self,
        request: main_models.DescribeInstanceStorageConfigRequest,
    ) -> main_models.DescribeInstanceStorageConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_storage_config_with_options(request, runtime)

    async def describe_instance_storage_config_async(
        self,
        request: main_models.DescribeInstanceStorageConfigRequest,
    ) -> main_models.DescribeInstanceStorageConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_storage_config_with_options_async(request, runtime)

    def get_conversations_with_options(
        self,
        request: main_models.GetConversationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConversationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.last_id):
            query['LastId'] = request.last_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.pinned):
            query['Pinned'] = request.pinned
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConversations',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConversationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conversations_with_options_async(
        self,
        request: main_models.GetConversationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConversationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.last_id):
            query['LastId'] = request.last_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.pinned):
            query['Pinned'] = request.pinned
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConversations',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConversationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conversations(
        self,
        request: main_models.GetConversationsRequest,
    ) -> main_models.GetConversationsResponse:
        runtime = RuntimeOptions()
        return self.get_conversations_with_options(request, runtime)

    async def get_conversations_async(
        self,
        request: main_models.GetConversationsRequest,
    ) -> main_models.GetConversationsResponse:
        runtime = RuntimeOptions()
        return await self.get_conversations_with_options_async(request, runtime)

    def get_custom_agent_with_options(
        self,
        request: main_models.GetCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomAgent',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_agent_with_options_async(
        self,
        request: main_models.GetCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomAgent',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_agent(
        self,
        request: main_models.GetCustomAgentRequest,
    ) -> main_models.GetCustomAgentResponse:
        runtime = RuntimeOptions()
        return self.get_custom_agent_with_options(request, runtime)

    async def get_custom_agent_async(
        self,
        request: main_models.GetCustomAgentRequest,
    ) -> main_models.GetCustomAgentResponse:
        runtime = RuntimeOptions()
        return await self.get_custom_agent_with_options_async(request, runtime)

    def get_messages_with_options(
        self,
        request: main_models.GetMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.first_id):
            query['FirstId'] = request.first_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMessages',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_messages_with_options_async(
        self,
        request: main_models.GetMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.first_id):
            query['FirstId'] = request.first_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMessages',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_messages(
        self,
        request: main_models.GetMessagesRequest,
    ) -> main_models.GetMessagesResponse:
        runtime = RuntimeOptions()
        return self.get_messages_with_options(request, runtime)

    async def get_messages_async(
        self,
        request: main_models.GetMessagesRequest,
    ) -> main_models.GetMessagesResponse:
        runtime = RuntimeOptions()
        return await self.get_messages_with_options_async(request, runtime)

    def list_custom_agent_with_options(
        self,
        request: main_models.ListCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomAgent',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_agent_with_options_async(
        self,
        request: main_models.ListCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomAgent',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_agent(
        self,
        request: main_models.ListCustomAgentRequest,
    ) -> main_models.ListCustomAgentResponse:
        runtime = RuntimeOptions()
        return self.list_custom_agent_with_options(request, runtime)

    async def list_custom_agent_async(
        self,
        request: main_models.ListCustomAgentRequest,
    ) -> main_models.ListCustomAgentResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_agent_with_options_async(request, runtime)

    def list_custom_agent_tools_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomAgentToolsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListCustomAgentTools',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomAgentToolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_agent_tools_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomAgentToolsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListCustomAgentTools',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomAgentToolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_agent_tools(self) -> main_models.ListCustomAgentToolsResponse:
        runtime = RuntimeOptions()
        return self.list_custom_agent_tools_with_options(runtime)

    async def list_custom_agent_tools_async(self) -> main_models.ListCustomAgentToolsResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_agent_tools_with_options_async(runtime)

    def modify_instance_auth_config_with_options(
        self,
        tmp_req: main_models.ModifyInstanceAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAuthConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyInstanceAuthConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_list):
            request.config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not DaraCore.is_null(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceAuthConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_auth_config_with_options_async(
        self,
        tmp_req: main_models.ModifyInstanceAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAuthConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyInstanceAuthConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_list):
            request.config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not DaraCore.is_null(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceAuthConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_auth_config(
        self,
        request: main_models.ModifyInstanceAuthConfigRequest,
    ) -> main_models.ModifyInstanceAuthConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_auth_config_with_options(request, runtime)

    async def modify_instance_auth_config_async(
        self,
        request: main_models.ModifyInstanceAuthConfigRequest,
    ) -> main_models.ModifyInstanceAuthConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_auth_config_with_options_async(request, runtime)

    def modify_instance_config_with_options(
        self,
        request: main_models.ModifyInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.config_value):
            query['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_config_with_options_async(
        self,
        request: main_models.ModifyInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.config_value):
            query['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_config(
        self,
        request: main_models.ModifyInstanceConfigRequest,
    ) -> main_models.ModifyInstanceConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_config_with_options(request, runtime)

    async def modify_instance_config_async(
        self,
        request: main_models.ModifyInstanceConfigRequest,
    ) -> main_models.ModifyInstanceConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_config_with_options_async(request, runtime)

    def modify_instance_ip_whitelist_with_options(
        self,
        request: main_models.ModifyInstanceIpWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceIpWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.ip_whitelist):
            query['IpWhitelist'] = request.ip_whitelist
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceIpWhitelist',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_ip_whitelist_with_options_async(
        self,
        request: main_models.ModifyInstanceIpWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceIpWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.ip_whitelist):
            query['IpWhitelist'] = request.ip_whitelist
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceIpWhitelist',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ip_whitelist(
        self,
        request: main_models.ModifyInstanceIpWhitelistRequest,
    ) -> main_models.ModifyInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_ip_whitelist_with_options(request, runtime)

    async def modify_instance_ip_whitelist_async(
        self,
        request: main_models.ModifyInstanceIpWhitelistRequest,
    ) -> main_models.ModifyInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_ip_whitelist_with_options_async(request, runtime)

    def modify_instance_ragconfig_with_options(
        self,
        tmp_req: main_models.ModifyInstanceRAGConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceRAGConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyInstanceRAGConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_list):
            request.config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceRAGConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceRAGConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_ragconfig_with_options_async(
        self,
        tmp_req: main_models.ModifyInstanceRAGConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceRAGConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyInstanceRAGConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_list):
            request.config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceRAGConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceRAGConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ragconfig(
        self,
        request: main_models.ModifyInstanceRAGConfigRequest,
    ) -> main_models.ModifyInstanceRAGConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_ragconfig_with_options(request, runtime)

    async def modify_instance_ragconfig_async(
        self,
        request: main_models.ModifyInstanceRAGConfigRequest,
    ) -> main_models.ModifyInstanceRAGConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_ragconfig_with_options_async(request, runtime)

    def modify_instance_sslwith_options(
        self,
        request: main_models.ModifyInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catype):
            query['CAType'] = request.catype
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        if not DaraCore.is_null(request.server_cert):
            query['ServerCert'] = request.server_cert
        if not DaraCore.is_null(request.server_key):
            query['ServerKey'] = request.server_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceSSL',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_sslwith_options_async(
        self,
        request: main_models.ModifyInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catype):
            query['CAType'] = request.catype
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        if not DaraCore.is_null(request.server_cert):
            query['ServerCert'] = request.server_cert
        if not DaraCore.is_null(request.server_key):
            query['ServerKey'] = request.server_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceSSL',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ssl(
        self,
        request: main_models.ModifyInstanceSSLRequest,
    ) -> main_models.ModifyInstanceSSLResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_sslwith_options(request, runtime)

    async def modify_instance_ssl_async(
        self,
        request: main_models.ModifyInstanceSSLRequest,
    ) -> main_models.ModifyInstanceSSLResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_sslwith_options_async(request, runtime)

    def modify_instance_storage_config_with_options(
        self,
        tmp_req: main_models.ModifyInstanceStorageConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceStorageConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyInstanceStorageConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_list):
            request.config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceStorageConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceStorageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_storage_config_with_options_async(
        self,
        tmp_req: main_models.ModifyInstanceStorageConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceStorageConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyInstanceStorageConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_list):
            request.config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceStorageConfig',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceStorageConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_storage_config(
        self,
        request: main_models.ModifyInstanceStorageConfigRequest,
    ) -> main_models.ModifyInstanceStorageConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_storage_config_with_options(request, runtime)

    async def modify_instance_storage_config_async(
        self,
        request: main_models.ModifyInstanceStorageConfigRequest,
    ) -> main_models.ModifyInstanceStorageConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_storage_config_with_options_async(request, runtime)

    def modify_messages_feedbacks_with_options(
        self,
        request: main_models.ModifyMessagesFeedbacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMessagesFeedbacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.rating):
            query['Rating'] = request.rating
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMessagesFeedbacks',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMessagesFeedbacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_messages_feedbacks_with_options_async(
        self,
        request: main_models.ModifyMessagesFeedbacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMessagesFeedbacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.rating):
            query['Rating'] = request.rating
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMessagesFeedbacks',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMessagesFeedbacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_messages_feedbacks(
        self,
        request: main_models.ModifyMessagesFeedbacksRequest,
    ) -> main_models.ModifyMessagesFeedbacksResponse:
        runtime = RuntimeOptions()
        return self.modify_messages_feedbacks_with_options(request, runtime)

    async def modify_messages_feedbacks_async(
        self,
        request: main_models.ModifyMessagesFeedbacksRequest,
    ) -> main_models.ModifyMessagesFeedbacksResponse:
        runtime = RuntimeOptions()
        return await self.modify_messages_feedbacks_with_options_async(request, runtime)

    def reset_instance_password_with_options(
        self,
        request: main_models.ResetInstancePasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetInstancePasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not DaraCore.is_null(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetInstancePassword',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetInstancePasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_instance_password_with_options_async(
        self,
        request: main_models.ResetInstancePasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetInstancePasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not DaraCore.is_null(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetInstancePassword',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetInstancePasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_instance_password(
        self,
        request: main_models.ResetInstancePasswordRequest,
    ) -> main_models.ResetInstancePasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_instance_password_with_options(request, runtime)

    async def reset_instance_password_async(
        self,
        request: main_models.ResetInstancePasswordRequest,
    ) -> main_models.ResetInstancePasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_instance_password_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: main_models.RestartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: main_models.RestartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        request: main_models.RestartInstanceRequest,
    ) -> main_models.RestartInstanceResponse:
        runtime = RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: main_models.RestartInstanceRequest,
    ) -> main_models.RestartInstanceResponse:
        runtime = RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: main_models.StartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: main_models.StartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        request: main_models.StartInstanceRequest,
    ) -> main_models.StartInstanceResponse:
        runtime = RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: main_models.StartInstanceRequest,
    ) -> main_models.StartInstanceResponse:
        runtime = RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: main_models.StopInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: main_models.StopInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        request: main_models.StopInstanceRequest,
    ) -> main_models.StopInstanceResponse:
        runtime = RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: main_models.StopInstanceRequest,
    ) -> main_models.StopInstanceResponse:
        runtime = RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def update_custom_agent_with_options(
        self,
        tmp_req: main_models.UpdateCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateCustomAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tools):
            request.tools_shrink = Utils.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.system_prompt):
            query['SystemPrompt'] = request.system_prompt
        if not DaraCore.is_null(request.tools_shrink):
            query['Tools'] = request.tools_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomAgent',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_agent_with_options_async(
        self,
        tmp_req: main_models.UpdateCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateCustomAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tools):
            request.tools_shrink = Utils.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.system_prompt):
            query['SystemPrompt'] = request.system_prompt
        if not DaraCore.is_null(request.tools_shrink):
            query['Tools'] = request.tools_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomAgent',
            version = '2025-05-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_agent(
        self,
        request: main_models.UpdateCustomAgentRequest,
    ) -> main_models.UpdateCustomAgentResponse:
        runtime = RuntimeOptions()
        return self.update_custom_agent_with_options(request, runtime)

    async def update_custom_agent_async(
        self,
        request: main_models.UpdateCustomAgentRequest,
    ) -> main_models.UpdateCustomAgentResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_agent_with_options_async(request, runtime)
