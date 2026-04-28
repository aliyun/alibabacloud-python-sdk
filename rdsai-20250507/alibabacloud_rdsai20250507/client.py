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
        if not DaraCore.is_null(request.event_mode):
            query['EventMode'] = request.event_mode
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
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ChatMessagesResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
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
        if not DaraCore.is_null(request.event_mode):
            query['EventMode'] = request.event_mode
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
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ChatMessagesResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
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
        if not DaraCore.is_null(request.event_mode):
            query['EventMode'] = request.event_mode
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
        if not DaraCore.is_null(request.event_mode):
            query['EventMode'] = request.event_mode
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

    def create_api_key_with_options(
        self,
        request: main_models.CreateApiKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        if not DaraCore.is_null(request.limit_rate):
            query['LimitRate'] = request.limit_rate
        if not DaraCore.is_null(request.limit_type):
            query['LimitType'] = request.limit_type
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.token_quota):
            query['TokenQuota'] = request.token_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiKey',
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
            main_models.CreateApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_key_with_options_async(
        self,
        request: main_models.CreateApiKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        if not DaraCore.is_null(request.limit_rate):
            query['LimitRate'] = request.limit_rate
        if not DaraCore.is_null(request.limit_type):
            query['LimitType'] = request.limit_type
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.token_quota):
            query['TokenQuota'] = request.token_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiKey',
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
            main_models.CreateApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_key(
        self,
        request: main_models.CreateApiKeyRequest,
    ) -> main_models.CreateApiKeyResponse:
        runtime = RuntimeOptions()
        return self.create_api_key_with_options(request, runtime)

    async def create_api_key_async(
        self,
        request: main_models.CreateApiKeyRequest,
    ) -> main_models.CreateApiKeyResponse:
        runtime = RuntimeOptions()
        return await self.create_api_key_with_options_async(request, runtime)

    def create_app_instance_with_options(
        self,
        tmp_req: main_models.CreateAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateAppInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.components):
            request.components_shrink = Utils.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not DaraCore.is_null(tmp_req.dbinstance_config):
            request.dbinstance_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbinstance_config, 'DBInstanceConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.components_shrink):
            query['Components'] = request.components_shrink
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
        if not DaraCore.is_null(request.initialize_with_existing_data):
            query['InitializeWithExistingData'] = request.initialize_with_existing_data
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
        if not DaraCore.is_null(tmp_req.components):
            request.components_shrink = Utils.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not DaraCore.is_null(tmp_req.dbinstance_config):
            request.dbinstance_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbinstance_config, 'DBInstanceConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.components_shrink):
            query['Components'] = request.components_shrink
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
        if not DaraCore.is_null(request.initialize_with_existing_data):
            query['InitializeWithExistingData'] = request.initialize_with_existing_data
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
        if not DaraCore.is_null(tmp_req.skill_ids):
            request.skill_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.skill_ids, 'SkillIds', 'json')
        if not DaraCore.is_null(tmp_req.tools):
            request.tools_shrink = Utils.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not DaraCore.is_null(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.skill_ids_shrink):
            query['SkillIds'] = request.skill_ids_shrink
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
        if not DaraCore.is_null(tmp_req.skill_ids):
            request.skill_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.skill_ids, 'SkillIds', 'json')
        if not DaraCore.is_null(tmp_req.tools):
            request.tools_shrink = Utils.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not DaraCore.is_null(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.skill_ids_shrink):
            query['SkillIds'] = request.skill_ids_shrink
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

    def create_inspection_task_with_options(
        self,
        request: main_models.CreateInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.inspection_items):
            query['InspectionItems'] = request.inspection_items
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_language):
            query['ReportLanguage'] = request.report_language
        if not DaraCore.is_null(request.report_region_id):
            query['ReportRegionId'] = request.report_region_id
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInspectionTask',
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
            main_models.CreateInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_inspection_task_with_options_async(
        self,
        request: main_models.CreateInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.inspection_items):
            query['InspectionItems'] = request.inspection_items
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_language):
            query['ReportLanguage'] = request.report_language
        if not DaraCore.is_null(request.report_region_id):
            query['ReportRegionId'] = request.report_region_id
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInspectionTask',
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
            main_models.CreateInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_inspection_task(
        self,
        request: main_models.CreateInspectionTaskRequest,
    ) -> main_models.CreateInspectionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_inspection_task_with_options(request, runtime)

    async def create_inspection_task_async(
        self,
        request: main_models.CreateInspectionTaskRequest,
    ) -> main_models.CreateInspectionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_inspection_task_with_options_async(request, runtime)

    def create_scheduled_task_with_options(
        self,
        request: main_models.CreateScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.frequency):
            query['Frequency'] = request.frequency
        if not DaraCore.is_null(request.inspection_items):
            query['InspectionItems'] = request.inspection_items
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_language):
            query['ReportLanguage'] = request.report_language
        if not DaraCore.is_null(request.report_region_id):
            query['ReportRegionId'] = request.report_region_id
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledTask',
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
            main_models.CreateScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_task_with_options_async(
        self,
        request: main_models.CreateScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.frequency):
            query['Frequency'] = request.frequency
        if not DaraCore.is_null(request.inspection_items):
            query['InspectionItems'] = request.inspection_items
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_language):
            query['ReportLanguage'] = request.report_language
        if not DaraCore.is_null(request.report_region_id):
            query['ReportRegionId'] = request.report_region_id
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledTask',
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
            main_models.CreateScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_task(
        self,
        request: main_models.CreateScheduledTaskRequest,
    ) -> main_models.CreateScheduledTaskResponse:
        runtime = RuntimeOptions()
        return self.create_scheduled_task_with_options(request, runtime)

    async def create_scheduled_task_async(
        self,
        request: main_models.CreateScheduledTaskRequest,
    ) -> main_models.CreateScheduledTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_scheduled_task_with_options_async(request, runtime)

    def create_skill_with_options(
        self,
        tmp_req: main_models.CreateSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillResponse:
        tmp_req.validate()
        request = main_models.CreateSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.content):
            request.content_shrink = Utils.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        if not DaraCore.is_null(tmp_req.dbtypes):
            request.dbtypes_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbtypes, 'Dbtypes', 'json')
        query = {}
        if not DaraCore.is_null(request.content_shrink):
            query['Content'] = request.content_shrink
        if not DaraCore.is_null(request.dbtypes_shrink):
            query['Dbtypes'] = request.dbtypes_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkill',
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
            main_models.CreateSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_with_options_async(
        self,
        tmp_req: main_models.CreateSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillResponse:
        tmp_req.validate()
        request = main_models.CreateSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.content):
            request.content_shrink = Utils.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        if not DaraCore.is_null(tmp_req.dbtypes):
            request.dbtypes_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbtypes, 'Dbtypes', 'json')
        query = {}
        if not DaraCore.is_null(request.content_shrink):
            query['Content'] = request.content_shrink
        if not DaraCore.is_null(request.dbtypes_shrink):
            query['Dbtypes'] = request.dbtypes_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkill',
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
            main_models.CreateSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill(
        self,
        request: main_models.CreateSkillRequest,
    ) -> main_models.CreateSkillResponse:
        runtime = RuntimeOptions()
        return self.create_skill_with_options(request, runtime)

    async def create_skill_async(
        self,
        request: main_models.CreateSkillRequest,
    ) -> main_models.CreateSkillResponse:
        runtime = RuntimeOptions()
        return await self.create_skill_with_options_async(request, runtime)

    def delete_api_key_with_options(
        self,
        request: main_models.DeleteApiKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key):
            query['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiKey',
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
            main_models.DeleteApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_key_with_options_async(
        self,
        request: main_models.DeleteApiKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key):
            query['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiKey',
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
            main_models.DeleteApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_key(
        self,
        request: main_models.DeleteApiKeyRequest,
    ) -> main_models.DeleteApiKeyResponse:
        runtime = RuntimeOptions()
        return self.delete_api_key_with_options(request, runtime)

    async def delete_api_key_async(
        self,
        request: main_models.DeleteApiKeyRequest,
    ) -> main_models.DeleteApiKeyResponse:
        runtime = RuntimeOptions()
        return await self.delete_api_key_with_options_async(request, runtime)

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

    def delete_scheduled_task_with_options(
        self,
        request: main_models.DeleteScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scheduled_id):
            query['ScheduledId'] = request.scheduled_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduledTask',
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
            main_models.DeleteScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduled_task_with_options_async(
        self,
        request: main_models.DeleteScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scheduled_id):
            query['ScheduledId'] = request.scheduled_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduledTask',
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
            main_models.DeleteScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduled_task(
        self,
        request: main_models.DeleteScheduledTaskRequest,
    ) -> main_models.DeleteScheduledTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_scheduled_task_with_options(request, runtime)

    async def delete_scheduled_task_async(
        self,
        request: main_models.DeleteScheduledTaskRequest,
    ) -> main_models.DeleteScheduledTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_scheduled_task_with_options_async(request, runtime)

    def delete_skill_with_options(
        self,
        request: main_models.DeleteSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkill',
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
            main_models.DeleteSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_with_options_async(
        self,
        request: main_models.DeleteSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkill',
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
            main_models.DeleteSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill(
        self,
        request: main_models.DeleteSkillRequest,
    ) -> main_models.DeleteSkillResponse:
        runtime = RuntimeOptions()
        return self.delete_skill_with_options(request, runtime)

    async def delete_skill_async(
        self,
        request: main_models.DeleteSkillRequest,
    ) -> main_models.DeleteSkillResponse:
        runtime = RuntimeOptions()
        return await self.delete_skill_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
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
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
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

    def describe_motoken_usage_detail_with_options(
        self,
        request: main_models.DescribeMOTokenUsageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMOTokenUsageDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_name):
            query['ConsumerName'] = request.consumer_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMOTokenUsageDetail',
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
            main_models.DescribeMOTokenUsageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_motoken_usage_detail_with_options_async(
        self,
        request: main_models.DescribeMOTokenUsageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMOTokenUsageDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_name):
            query['ConsumerName'] = request.consumer_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMOTokenUsageDetail',
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
            main_models.DescribeMOTokenUsageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_motoken_usage_detail(
        self,
        request: main_models.DescribeMOTokenUsageDetailRequest,
    ) -> main_models.DescribeMOTokenUsageDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_motoken_usage_detail_with_options(request, runtime)

    async def describe_motoken_usage_detail_async(
        self,
        request: main_models.DescribeMOTokenUsageDetailRequest,
    ) -> main_models.DescribeMOTokenUsageDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_motoken_usage_detail_with_options_async(request, runtime)

    def describe_model_operator_with_options(
        self,
        request: main_models.DescribeModelOperatorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelOperatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModelOperator',
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
            main_models.DescribeModelOperatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_model_operator_with_options_async(
        self,
        request: main_models.DescribeModelOperatorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelOperatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModelOperator',
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
            main_models.DescribeModelOperatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_model_operator(
        self,
        request: main_models.DescribeModelOperatorRequest,
    ) -> main_models.DescribeModelOperatorResponse:
        runtime = RuntimeOptions()
        return self.describe_model_operator_with_options(request, runtime)

    async def describe_model_operator_async(
        self,
        request: main_models.DescribeModelOperatorRequest,
    ) -> main_models.DescribeModelOperatorResponse:
        runtime = RuntimeOptions()
        return await self.describe_model_operator_with_options_async(request, runtime)

    def describe_monitor_data_with_options(
        self,
        tmp_req: main_models.DescribeMonitorDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorDataResponse:
        tmp_req.validate()
        request = main_models.DescribeMonitorDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_key_name):
            request.api_key_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_key_name, 'ApiKeyName', 'json')
        query = {}
        if not DaraCore.is_null(request.api_key_name_shrink):
            query['ApiKeyName'] = request.api_key_name_shrink
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorData',
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
            main_models.DescribeMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_data_with_options_async(
        self,
        tmp_req: main_models.DescribeMonitorDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorDataResponse:
        tmp_req.validate()
        request = main_models.DescribeMonitorDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_key_name):
            request.api_key_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_key_name, 'ApiKeyName', 'json')
        query = {}
        if not DaraCore.is_null(request.api_key_name_shrink):
            query['ApiKeyName'] = request.api_key_name_shrink
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorData',
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
            main_models.DescribeMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_data(
        self,
        request: main_models.DescribeMonitorDataRequest,
    ) -> main_models.DescribeMonitorDataResponse:
        runtime = RuntimeOptions()
        return self.describe_monitor_data_with_options(request, runtime)

    async def describe_monitor_data_async(
        self,
        request: main_models.DescribeMonitorDataRequest,
    ) -> main_models.DescribeMonitorDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitor_data_with_options_async(request, runtime)

    def describe_sandbox_templates_with_options(
        self,
        request: main_models.DescribeSandboxTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSandboxTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSandboxTemplates',
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
            main_models.DescribeSandboxTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sandbox_templates_with_options_async(
        self,
        request: main_models.DescribeSandboxTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSandboxTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSandboxTemplates',
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
            main_models.DescribeSandboxTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sandbox_templates(
        self,
        request: main_models.DescribeSandboxTemplatesRequest,
    ) -> main_models.DescribeSandboxTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_sandbox_templates_with_options(request, runtime)

    async def describe_sandbox_templates_async(
        self,
        request: main_models.DescribeSandboxTemplatesRequest,
    ) -> main_models.DescribeSandboxTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_sandbox_templates_with_options_async(request, runtime)

    def describe_whitelist_ips_with_options(
        self,
        request: main_models.DescribeWhitelistIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWhitelistIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWhitelistIps',
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
            main_models.DescribeWhitelistIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_whitelist_ips_with_options_async(
        self,
        request: main_models.DescribeWhitelistIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWhitelistIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWhitelistIps',
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
            main_models.DescribeWhitelistIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_whitelist_ips(
        self,
        request: main_models.DescribeWhitelistIpsRequest,
    ) -> main_models.DescribeWhitelistIpsResponse:
        runtime = RuntimeOptions()
        return self.describe_whitelist_ips_with_options(request, runtime)

    async def describe_whitelist_ips_async(
        self,
        request: main_models.DescribeWhitelistIpsRequest,
    ) -> main_models.DescribeWhitelistIpsResponse:
        runtime = RuntimeOptions()
        return await self.describe_whitelist_ips_with_options_async(request, runtime)

    def disable_agent_runtime_with_options(
        self,
        request: main_models.DisableAgentRuntimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAgentRuntimeResponse:
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
            action = 'DisableAgentRuntime',
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
            main_models.DisableAgentRuntimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_agent_runtime_with_options_async(
        self,
        request: main_models.DisableAgentRuntimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAgentRuntimeResponse:
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
            action = 'DisableAgentRuntime',
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
            main_models.DisableAgentRuntimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_agent_runtime(
        self,
        request: main_models.DisableAgentRuntimeRequest,
    ) -> main_models.DisableAgentRuntimeResponse:
        runtime = RuntimeOptions()
        return self.disable_agent_runtime_with_options(request, runtime)

    async def disable_agent_runtime_async(
        self,
        request: main_models.DisableAgentRuntimeRequest,
    ) -> main_models.DisableAgentRuntimeResponse:
        runtime = RuntimeOptions()
        return await self.disable_agent_runtime_with_options_async(request, runtime)

    def enable_agent_runtime_with_options(
        self,
        request: main_models.EnableAgentRuntimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAgentRuntimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAgentRuntime',
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
            main_models.EnableAgentRuntimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_agent_runtime_with_options_async(
        self,
        request: main_models.EnableAgentRuntimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAgentRuntimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAgentRuntime',
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
            main_models.EnableAgentRuntimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_agent_runtime(
        self,
        request: main_models.EnableAgentRuntimeRequest,
    ) -> main_models.EnableAgentRuntimeResponse:
        runtime = RuntimeOptions()
        return self.enable_agent_runtime_with_options(request, runtime)

    async def enable_agent_runtime_async(
        self,
        request: main_models.EnableAgentRuntimeRequest,
    ) -> main_models.EnableAgentRuntimeResponse:
        runtime = RuntimeOptions()
        return await self.enable_agent_runtime_with_options_async(request, runtime)

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

    def get_inspection_report_with_options(
        self,
        request: main_models.GetInspectionReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInspectionReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInspectionReport',
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
            main_models.GetInspectionReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inspection_report_with_options_async(
        self,
        request: main_models.GetInspectionReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInspectionReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInspectionReport',
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
            main_models.GetInspectionReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inspection_report(
        self,
        request: main_models.GetInspectionReportRequest,
    ) -> main_models.GetInspectionReportResponse:
        runtime = RuntimeOptions()
        return self.get_inspection_report_with_options(request, runtime)

    async def get_inspection_report_async(
        self,
        request: main_models.GetInspectionReportRequest,
    ) -> main_models.GetInspectionReportResponse:
        runtime = RuntimeOptions()
        return await self.get_inspection_report_with_options_async(request, runtime)

    def get_messages_with_options(
        self,
        request: main_models.GetMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.event_mode):
            query['EventMode'] = request.event_mode
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
        if not DaraCore.is_null(request.event_mode):
            query['EventMode'] = request.event_mode
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

    def get_model_operator_order_with_options(
        self,
        request: main_models.GetModelOperatorOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetModelOperatorOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetModelOperatorOrder',
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
            main_models.GetModelOperatorOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_operator_order_with_options_async(
        self,
        request: main_models.GetModelOperatorOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetModelOperatorOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetModelOperatorOrder',
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
            main_models.GetModelOperatorOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_operator_order(
        self,
        request: main_models.GetModelOperatorOrderRequest,
    ) -> main_models.GetModelOperatorOrderResponse:
        runtime = RuntimeOptions()
        return self.get_model_operator_order_with_options(request, runtime)

    async def get_model_operator_order_async(
        self,
        request: main_models.GetModelOperatorOrderRequest,
    ) -> main_models.GetModelOperatorOrderResponse:
        runtime = RuntimeOptions()
        return await self.get_model_operator_order_with_options_async(request, runtime)

    def get_scheduled_instances_with_options(
        self,
        request: main_models.GetScheduledInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scheduled_id):
            query['ScheduledId'] = request.scheduled_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledInstances',
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
            main_models.GetScheduledInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scheduled_instances_with_options_async(
        self,
        request: main_models.GetScheduledInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scheduled_id):
            query['ScheduledId'] = request.scheduled_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledInstances',
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
            main_models.GetScheduledInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scheduled_instances(
        self,
        request: main_models.GetScheduledInstancesRequest,
    ) -> main_models.GetScheduledInstancesResponse:
        runtime = RuntimeOptions()
        return self.get_scheduled_instances_with_options(request, runtime)

    async def get_scheduled_instances_async(
        self,
        request: main_models.GetScheduledInstancesRequest,
    ) -> main_models.GetScheduledInstancesResponse:
        runtime = RuntimeOptions()
        return await self.get_scheduled_instances_with_options_async(request, runtime)

    def get_scheduled_reports_with_options(
        self,
        request: main_models.GetScheduledReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scheduled_id):
            query['ScheduledId'] = request.scheduled_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledReports',
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
            main_models.GetScheduledReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scheduled_reports_with_options_async(
        self,
        request: main_models.GetScheduledReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scheduled_id):
            query['ScheduledId'] = request.scheduled_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledReports',
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
            main_models.GetScheduledReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scheduled_reports(
        self,
        request: main_models.GetScheduledReportsRequest,
    ) -> main_models.GetScheduledReportsResponse:
        runtime = RuntimeOptions()
        return self.get_scheduled_reports_with_options(request, runtime)

    async def get_scheduled_reports_async(
        self,
        request: main_models.GetScheduledReportsRequest,
    ) -> main_models.GetScheduledReportsResponse:
        runtime = RuntimeOptions()
        return await self.get_scheduled_reports_with_options_async(request, runtime)

    def get_skill_with_options(
        self,
        request: main_models.GetSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkill',
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
            main_models.GetSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_with_options_async(
        self,
        request: main_models.GetSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkill',
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
            main_models.GetSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill(
        self,
        request: main_models.GetSkillRequest,
    ) -> main_models.GetSkillResponse:
        runtime = RuntimeOptions()
        return self.get_skill_with_options(request, runtime)

    async def get_skill_async(
        self,
        request: main_models.GetSkillRequest,
    ) -> main_models.GetSkillResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_with_options_async(request, runtime)

    def get_stand_alone_reports_with_options(
        self,
        request: main_models.GetStandAloneReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandAloneReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStandAloneReports',
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
            main_models.GetStandAloneReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stand_alone_reports_with_options_async(
        self,
        request: main_models.GetStandAloneReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandAloneReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStandAloneReports',
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
            main_models.GetStandAloneReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stand_alone_reports(
        self,
        request: main_models.GetStandAloneReportsRequest,
    ) -> main_models.GetStandAloneReportsResponse:
        runtime = RuntimeOptions()
        return self.get_stand_alone_reports_with_options(request, runtime)

    async def get_stand_alone_reports_async(
        self,
        request: main_models.GetStandAloneReportsRequest,
    ) -> main_models.GetStandAloneReportsResponse:
        runtime = RuntimeOptions()
        return await self.get_stand_alone_reports_with_options_async(request, runtime)

    def list_api_keys_with_options(
        self,
        request: main_models.ListApiKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiKeys',
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
            main_models.ListApiKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_keys_with_options_async(
        self,
        request: main_models.ListApiKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiKeys',
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
            main_models.ListApiKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_keys(
        self,
        request: main_models.ListApiKeysRequest,
    ) -> main_models.ListApiKeysResponse:
        runtime = RuntimeOptions()
        return self.list_api_keys_with_options(request, runtime)

    async def list_api_keys_async(
        self,
        request: main_models.ListApiKeysRequest,
    ) -> main_models.ListApiKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_api_keys_with_options_async(request, runtime)

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

    def list_scheduled_tasks_with_options(
        self,
        request: main_models.ListScheduledTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scheduled_id):
            query['ScheduledId'] = request.scheduled_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledTasks',
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
            main_models.ListScheduledTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheduled_tasks_with_options_async(
        self,
        request: main_models.ListScheduledTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scheduled_id):
            query['ScheduledId'] = request.scheduled_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledTasks',
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
            main_models.ListScheduledTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheduled_tasks(
        self,
        request: main_models.ListScheduledTasksRequest,
    ) -> main_models.ListScheduledTasksResponse:
        runtime = RuntimeOptions()
        return self.list_scheduled_tasks_with_options(request, runtime)

    async def list_scheduled_tasks_async(
        self,
        request: main_models.ListScheduledTasksRequest,
    ) -> main_models.ListScheduledTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_scheduled_tasks_with_options_async(request, runtime)

    def list_skill_with_options(
        self,
        request: main_models.ListSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkill',
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
            main_models.ListSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_with_options_async(
        self,
        request: main_models.ListSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkill',
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
            main_models.ListSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill(
        self,
        request: main_models.ListSkillRequest,
    ) -> main_models.ListSkillResponse:
        runtime = RuntimeOptions()
        return self.list_skill_with_options(request, runtime)

    async def list_skill_async(
        self,
        request: main_models.ListSkillRequest,
    ) -> main_models.ListSkillResponse:
        runtime = RuntimeOptions()
        return await self.list_skill_with_options_async(request, runtime)

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

    def modify_instances_sslwith_options(
        self,
        tmp_req: main_models.ModifyInstancesSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstancesSSLResponse:
        tmp_req.validate()
        request = main_models.ModifyInstancesSSLShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_names):
            request.instance_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_names, 'InstanceNames', 'json')
        query = {}
        if not DaraCore.is_null(request.catype):
            query['CAType'] = request.catype
        if not DaraCore.is_null(request.instance_names_shrink):
            query['InstanceNames'] = request.instance_names_shrink
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
            action = 'ModifyInstancesSSL',
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
            main_models.ModifyInstancesSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instances_sslwith_options_async(
        self,
        tmp_req: main_models.ModifyInstancesSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstancesSSLResponse:
        tmp_req.validate()
        request = main_models.ModifyInstancesSSLShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_names):
            request.instance_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_names, 'InstanceNames', 'json')
        query = {}
        if not DaraCore.is_null(request.catype):
            query['CAType'] = request.catype
        if not DaraCore.is_null(request.instance_names_shrink):
            query['InstanceNames'] = request.instance_names_shrink
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
            action = 'ModifyInstancesSSL',
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
            main_models.ModifyInstancesSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instances_ssl(
        self,
        request: main_models.ModifyInstancesSSLRequest,
    ) -> main_models.ModifyInstancesSSLResponse:
        runtime = RuntimeOptions()
        return self.modify_instances_sslwith_options(request, runtime)

    async def modify_instances_ssl_async(
        self,
        request: main_models.ModifyInstancesSSLRequest,
    ) -> main_models.ModifyInstancesSSLResponse:
        runtime = RuntimeOptions()
        return await self.modify_instances_sslwith_options_async(request, runtime)

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

    def modify_scheduled_task_with_options(
        self,
        request: main_models.ModifyScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.frequency):
            query['Frequency'] = request.frequency
        if not DaraCore.is_null(request.inspection_items):
            query['InspectionItems'] = request.inspection_items
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.report_language):
            query['ReportLanguage'] = request.report_language
        if not DaraCore.is_null(request.scheduled_id):
            query['ScheduledId'] = request.scheduled_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScheduledTask',
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
            main_models.ModifyScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scheduled_task_with_options_async(
        self,
        request: main_models.ModifyScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.frequency):
            query['Frequency'] = request.frequency
        if not DaraCore.is_null(request.inspection_items):
            query['InspectionItems'] = request.inspection_items
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.report_language):
            query['ReportLanguage'] = request.report_language
        if not DaraCore.is_null(request.scheduled_id):
            query['ScheduledId'] = request.scheduled_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScheduledTask',
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
            main_models.ModifyScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scheduled_task(
        self,
        request: main_models.ModifyScheduledTaskRequest,
    ) -> main_models.ModifyScheduledTaskResponse:
        runtime = RuntimeOptions()
        return self.modify_scheduled_task_with_options(request, runtime)

    async def modify_scheduled_task_async(
        self,
        request: main_models.ModifyScheduledTaskRequest,
    ) -> main_models.ModifyScheduledTaskResponse:
        runtime = RuntimeOptions()
        return await self.modify_scheduled_task_with_options_async(request, runtime)

    def modify_whitelist_ips_with_options(
        self,
        request: main_models.ModifyWhitelistIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWhitelistIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_whitelist):
            query['IpWhitelist'] = request.ip_whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWhitelistIps',
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
            main_models.ModifyWhitelistIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_whitelist_ips_with_options_async(
        self,
        request: main_models.ModifyWhitelistIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWhitelistIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_whitelist):
            query['IpWhitelist'] = request.ip_whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWhitelistIps',
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
            main_models.ModifyWhitelistIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_whitelist_ips(
        self,
        request: main_models.ModifyWhitelistIpsRequest,
    ) -> main_models.ModifyWhitelistIpsResponse:
        runtime = RuntimeOptions()
        return self.modify_whitelist_ips_with_options(request, runtime)

    async def modify_whitelist_ips_async(
        self,
        request: main_models.ModifyWhitelistIpsRequest,
    ) -> main_models.ModifyWhitelistIpsResponse:
        runtime = RuntimeOptions()
        return await self.modify_whitelist_ips_with_options_async(request, runtime)

    def rename_api_key_with_options(
        self,
        request: main_models.RenameApiKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenameApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key):
            query['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenameApiKey',
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
            main_models.RenameApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_api_key_with_options_async(
        self,
        request: main_models.RenameApiKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenameApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key):
            query['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenameApiKey',
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
            main_models.RenameApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_api_key(
        self,
        request: main_models.RenameApiKeyRequest,
    ) -> main_models.RenameApiKeyResponse:
        runtime = RuntimeOptions()
        return self.rename_api_key_with_options(request, runtime)

    async def rename_api_key_async(
        self,
        request: main_models.RenameApiKeyRequest,
    ) -> main_models.RenameApiKeyResponse:
        runtime = RuntimeOptions()
        return await self.rename_api_key_with_options_async(request, runtime)

    def reset_api_key_with_options(
        self,
        request: main_models.ResetApiKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key):
            query['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetApiKey',
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
            main_models.ResetApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_api_key_with_options_async(
        self,
        request: main_models.ResetApiKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key):
            query['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetApiKey',
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
            main_models.ResetApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_api_key(
        self,
        request: main_models.ResetApiKeyRequest,
    ) -> main_models.ResetApiKeyResponse:
        runtime = RuntimeOptions()
        return self.reset_api_key_with_options(request, runtime)

    async def reset_api_key_async(
        self,
        request: main_models.ResetApiKeyRequest,
    ) -> main_models.ResetApiKeyResponse:
        runtime = RuntimeOptions()
        return await self.reset_api_key_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
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
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
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

    def update_api_key_quota_with_options(
        self,
        tmp_req: main_models.UpdateApiKeyQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiKeyQuotaResponse:
        tmp_req.validate()
        request = main_models.UpdateApiKeyQuotaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiKeyQuota',
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
            main_models.UpdateApiKeyQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_api_key_quota_with_options_async(
        self,
        tmp_req: main_models.UpdateApiKeyQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiKeyQuotaResponse:
        tmp_req.validate()
        request = main_models.UpdateApiKeyQuotaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiKeyQuota',
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
            main_models.UpdateApiKeyQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_api_key_quota(
        self,
        request: main_models.UpdateApiKeyQuotaRequest,
    ) -> main_models.UpdateApiKeyQuotaResponse:
        runtime = RuntimeOptions()
        return self.update_api_key_quota_with_options(request, runtime)

    async def update_api_key_quota_async(
        self,
        request: main_models.UpdateApiKeyQuotaRequest,
    ) -> main_models.UpdateApiKeyQuotaResponse:
        runtime = RuntimeOptions()
        return await self.update_api_key_quota_with_options_async(request, runtime)

    def update_custom_agent_with_options(
        self,
        tmp_req: main_models.UpdateCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateCustomAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.skill_ids):
            request.skill_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.skill_ids, 'SkillIds', 'json')
        if not DaraCore.is_null(tmp_req.tools):
            request.tools_shrink = Utils.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.skill_ids_shrink):
            query['SkillIds'] = request.skill_ids_shrink
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
        if not DaraCore.is_null(tmp_req.skill_ids):
            request.skill_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.skill_ids, 'SkillIds', 'json')
        if not DaraCore.is_null(tmp_req.tools):
            request.tools_shrink = Utils.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.skill_ids_shrink):
            query['SkillIds'] = request.skill_ids_shrink
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

    def update_skill_with_options(
        self,
        tmp_req: main_models.UpdateSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillResponse:
        tmp_req.validate()
        request = main_models.UpdateSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.content):
            request.content_shrink = Utils.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        if not DaraCore.is_null(tmp_req.dbtypes):
            request.dbtypes_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbtypes, 'Dbtypes', 'json')
        query = {}
        if not DaraCore.is_null(request.content_shrink):
            query['Content'] = request.content_shrink
        if not DaraCore.is_null(request.dbtypes_shrink):
            query['Dbtypes'] = request.dbtypes_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkill',
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
            main_models.UpdateSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_with_options_async(
        self,
        tmp_req: main_models.UpdateSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillResponse:
        tmp_req.validate()
        request = main_models.UpdateSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.content):
            request.content_shrink = Utils.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        if not DaraCore.is_null(tmp_req.dbtypes):
            request.dbtypes_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbtypes, 'Dbtypes', 'json')
        query = {}
        if not DaraCore.is_null(request.content_shrink):
            query['Content'] = request.content_shrink
        if not DaraCore.is_null(request.dbtypes_shrink):
            query['Dbtypes'] = request.dbtypes_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkill',
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
            main_models.UpdateSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill(
        self,
        request: main_models.UpdateSkillRequest,
    ) -> main_models.UpdateSkillResponse:
        runtime = RuntimeOptions()
        return self.update_skill_with_options(request, runtime)

    async def update_skill_async(
        self,
        request: main_models.UpdateSkillRequest,
    ) -> main_models.UpdateSkillResponse:
        runtime = RuntimeOptions()
        return await self.update_skill_with_options_async(request, runtime)
