# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
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
        self._endpoint = self.get_endpoint('sfmmultimodalapp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_command_with_options(
        self,
        tmp_req: main_models.CreateCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCommandResponse:
        tmp_req.validate()
        request = main_models.CreateCommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tool_examples):
            request.tool_examples_shrink = Utils.array_to_string_with_specified_style(tmp_req.tool_examples, 'ToolExamples', 'json')
        if not DaraCore.is_null(tmp_req.tool_params):
            request.tool_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.tool_params, 'ToolParams', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.tool_description):
            query['ToolDescription'] = request.tool_description
        if not DaraCore.is_null(request.tool_examples_shrink):
            query['ToolExamples'] = request.tool_examples_shrink
        if not DaraCore.is_null(request.tool_name):
            query['ToolName'] = request.tool_name
        if not DaraCore.is_null(request.tool_params_shrink):
            query['ToolParams'] = request.tool_params_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCommand',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_command_with_options_async(
        self,
        tmp_req: main_models.CreateCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCommandResponse:
        tmp_req.validate()
        request = main_models.CreateCommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tool_examples):
            request.tool_examples_shrink = Utils.array_to_string_with_specified_style(tmp_req.tool_examples, 'ToolExamples', 'json')
        if not DaraCore.is_null(tmp_req.tool_params):
            request.tool_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.tool_params, 'ToolParams', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.tool_description):
            query['ToolDescription'] = request.tool_description
        if not DaraCore.is_null(request.tool_examples_shrink):
            query['ToolExamples'] = request.tool_examples_shrink
        if not DaraCore.is_null(request.tool_name):
            query['ToolName'] = request.tool_name
        if not DaraCore.is_null(request.tool_params_shrink):
            query['ToolParams'] = request.tool_params_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCommand',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_command(
        self,
        request: main_models.CreateCommandRequest,
    ) -> main_models.CreateCommandResponse:
        runtime = RuntimeOptions()
        return self.create_command_with_options(request, runtime)

    async def create_command_async(
        self,
        request: main_models.CreateCommandRequest,
    ) -> main_models.CreateCommandResponse:
        runtime = RuntimeOptions()
        return await self.create_command_with_options_async(request, runtime)

    def create_memory_with_options(
        self,
        tmp_req: main_models.CreateMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemoryResponse:
        tmp_req.validate()
        request = main_models.CreateMemoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.meta_data):
            request.meta_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.meta_data, 'MetaData', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_update):
            query['AutoUpdate'] = request.auto_update
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.messages_json):
            query['MessagesJson'] = request.messages_json
        if not DaraCore.is_null(request.meta_data_shrink):
            query['MetaData'] = request.meta_data_shrink
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMemory',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_memory_with_options_async(
        self,
        tmp_req: main_models.CreateMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemoryResponse:
        tmp_req.validate()
        request = main_models.CreateMemoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.meta_data):
            request.meta_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.meta_data, 'MetaData', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_update):
            query['AutoUpdate'] = request.auto_update
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.messages_json):
            query['MessagesJson'] = request.messages_json
        if not DaraCore.is_null(request.meta_data_shrink):
            query['MetaData'] = request.meta_data_shrink
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMemory',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_memory(
        self,
        request: main_models.CreateMemoryRequest,
    ) -> main_models.CreateMemoryResponse:
        runtime = RuntimeOptions()
        return self.create_memory_with_options(request, runtime)

    async def create_memory_async(
        self,
        request: main_models.CreateMemoryRequest,
    ) -> main_models.CreateMemoryResponse:
        runtime = RuntimeOptions()
        return await self.create_memory_with_options_async(request, runtime)

    def create_mm_app_with_options(
        self,
        tmp_req: main_models.CreateMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMmAppResponse:
        tmp_req.validate()
        request = main_models.CreateMmAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.binding_config):
            request.binding_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.binding_config, 'BindingConfig', 'json')
        if not DaraCore.is_null(tmp_req.conversation_config):
            request.conversation_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.conversation_config, 'ConversationConfig', 'json')
        if not DaraCore.is_null(tmp_req.model_config):
            request.model_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_config, 'ModelConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.binding_config_shrink):
            query['BindingConfig'] = request.binding_config_shrink
        if not DaraCore.is_null(request.conversation_config_shrink):
            query['ConversationConfig'] = request.conversation_config_shrink
        if not DaraCore.is_null(request.model_config_shrink):
            query['ModelConfig'] = request.model_config_shrink
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mm_app_with_options_async(
        self,
        tmp_req: main_models.CreateMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMmAppResponse:
        tmp_req.validate()
        request = main_models.CreateMmAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.binding_config):
            request.binding_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.binding_config, 'BindingConfig', 'json')
        if not DaraCore.is_null(tmp_req.conversation_config):
            request.conversation_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.conversation_config, 'ConversationConfig', 'json')
        if not DaraCore.is_null(tmp_req.model_config):
            request.model_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_config, 'ModelConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.binding_config_shrink):
            query['BindingConfig'] = request.binding_config_shrink
        if not DaraCore.is_null(request.conversation_config_shrink):
            query['ConversationConfig'] = request.conversation_config_shrink
        if not DaraCore.is_null(request.model_config_shrink):
            query['ModelConfig'] = request.model_config_shrink
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mm_app(
        self,
        request: main_models.CreateMmAppRequest,
    ) -> main_models.CreateMmAppResponse:
        runtime = RuntimeOptions()
        return self.create_mm_app_with_options(request, runtime)

    async def create_mm_app_async(
        self,
        request: main_models.CreateMmAppRequest,
    ) -> main_models.CreateMmAppResponse:
        runtime = RuntimeOptions()
        return await self.create_mm_app_with_options_async(request, runtime)

    def create_profile_with_options(
        self,
        tmp_req: main_models.CreateProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProfileResponse:
        tmp_req.validate()
        request = main_models.CreateProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.attributes_shrink):
            query['Attributes'] = request.attributes_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProfile',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_profile_with_options_async(
        self,
        tmp_req: main_models.CreateProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProfileResponse:
        tmp_req.validate()
        request = main_models.CreateProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.attributes_shrink):
            query['Attributes'] = request.attributes_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProfile',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_profile(
        self,
        request: main_models.CreateProfileRequest,
    ) -> main_models.CreateProfileResponse:
        runtime = RuntimeOptions()
        return self.create_profile_with_options(request, runtime)

    async def create_profile_async(
        self,
        request: main_models.CreateProfileRequest,
    ) -> main_models.CreateProfileResponse:
        runtime = RuntimeOptions()
        return await self.create_profile_with_options_async(request, runtime)

    def delete_command_with_options(
        self,
        request: main_models.DeleteCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not DaraCore.is_null(request.tool_id):
            query['ToolId'] = request.tool_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCommand',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_command_with_options_async(
        self,
        request: main_models.DeleteCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not DaraCore.is_null(request.tool_id):
            query['ToolId'] = request.tool_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCommand',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_command(
        self,
        request: main_models.DeleteCommandRequest,
    ) -> main_models.DeleteCommandResponse:
        runtime = RuntimeOptions()
        return self.delete_command_with_options(request, runtime)

    async def delete_command_async(
        self,
        request: main_models.DeleteCommandRequest,
    ) -> main_models.DeleteCommandResponse:
        runtime = RuntimeOptions()
        return await self.delete_command_with_options_async(request, runtime)

    def delete_memory_with_options(
        self,
        request: main_models.DeleteMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.memory_node_id):
            query['MemoryNodeId'] = request.memory_node_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMemory',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_memory_with_options_async(
        self,
        request: main_models.DeleteMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.memory_node_id):
            query['MemoryNodeId'] = request.memory_node_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMemory',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_memory(
        self,
        request: main_models.DeleteMemoryRequest,
    ) -> main_models.DeleteMemoryResponse:
        runtime = RuntimeOptions()
        return self.delete_memory_with_options(request, runtime)

    async def delete_memory_async(
        self,
        request: main_models.DeleteMemoryRequest,
    ) -> main_models.DeleteMemoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_memory_with_options_async(request, runtime)

    def delete_mm_app_with_options(
        self,
        request: main_models.DeleteMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMmAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mm_app_with_options_async(
        self,
        request: main_models.DeleteMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMmAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mm_app(
        self,
        request: main_models.DeleteMmAppRequest,
    ) -> main_models.DeleteMmAppResponse:
        runtime = RuntimeOptions()
        return self.delete_mm_app_with_options(request, runtime)

    async def delete_mm_app_async(
        self,
        request: main_models.DeleteMmAppRequest,
    ) -> main_models.DeleteMmAppResponse:
        runtime = RuntimeOptions()
        return await self.delete_mm_app_with_options_async(request, runtime)

    def delete_profile_with_options(
        self,
        request: main_models.DeleteProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProfile',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_profile_with_options_async(
        self,
        request: main_models.DeleteProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProfile',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_profile(
        self,
        request: main_models.DeleteProfileRequest,
    ) -> main_models.DeleteProfileResponse:
        runtime = RuntimeOptions()
        return self.delete_profile_with_options(request, runtime)

    async def delete_profile_async(
        self,
        request: main_models.DeleteProfileRequest,
    ) -> main_models.DeleteProfileResponse:
        runtime = RuntimeOptions()
        return await self.delete_profile_with_options_async(request, runtime)

    def describe_command_with_options(
        self,
        request: main_models.DescribeCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not DaraCore.is_null(request.tool_id):
            query['ToolId'] = request.tool_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommand',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_command_with_options_async(
        self,
        request: main_models.DescribeCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not DaraCore.is_null(request.tool_id):
            query['ToolId'] = request.tool_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommand',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_command(
        self,
        request: main_models.DescribeCommandRequest,
    ) -> main_models.DescribeCommandResponse:
        runtime = RuntimeOptions()
        return self.describe_command_with_options(request, runtime)

    async def describe_command_async(
        self,
        request: main_models.DescribeCommandRequest,
    ) -> main_models.DescribeCommandResponse:
        runtime = RuntimeOptions()
        return await self.describe_command_with_options_async(request, runtime)

    def describe_mm_app_with_options(
        self,
        request: main_models.DescribeMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMmAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mm_app_with_options_async(
        self,
        request: main_models.DescribeMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMmAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mm_app(
        self,
        request: main_models.DescribeMmAppRequest,
    ) -> main_models.DescribeMmAppResponse:
        runtime = RuntimeOptions()
        return self.describe_mm_app_with_options(request, runtime)

    async def describe_mm_app_async(
        self,
        request: main_models.DescribeMmAppRequest,
    ) -> main_models.DescribeMmAppResponse:
        runtime = RuntimeOptions()
        return await self.describe_mm_app_with_options_async(request, runtime)

    def list_command_with_options(
        self,
        request: main_models.ListCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tool_name):
            query['ToolName'] = request.tool_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommand',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_command_with_options_async(
        self,
        request: main_models.ListCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tool_name):
            query['ToolName'] = request.tool_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommand',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_command(
        self,
        request: main_models.ListCommandRequest,
    ) -> main_models.ListCommandResponse:
        runtime = RuntimeOptions()
        return self.list_command_with_options(request, runtime)

    async def list_command_async(
        self,
        request: main_models.ListCommandRequest,
    ) -> main_models.ListCommandResponse:
        runtime = RuntimeOptions()
        return await self.list_command_with_options_async(request, runtime)

    def list_mm_app_with_options(
        self,
        request: main_models.ListMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMmAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mm_app_with_options_async(
        self,
        request: main_models.ListMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMmAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mm_app(
        self,
        request: main_models.ListMmAppRequest,
    ) -> main_models.ListMmAppResponse:
        runtime = RuntimeOptions()
        return self.list_mm_app_with_options(request, runtime)

    async def list_mm_app_async(
        self,
        request: main_models.ListMmAppRequest,
    ) -> main_models.ListMmAppResponse:
        runtime = RuntimeOptions()
        return await self.list_mm_app_with_options_async(request, runtime)

    def list_published_mm_app_with_options(
        self,
        request: main_models.ListPublishedMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishedMmAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishedMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishedMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_published_mm_app_with_options_async(
        self,
        request: main_models.ListPublishedMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishedMmAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishedMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishedMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_published_mm_app(
        self,
        request: main_models.ListPublishedMmAppRequest,
    ) -> main_models.ListPublishedMmAppResponse:
        runtime = RuntimeOptions()
        return self.list_published_mm_app_with_options(request, runtime)

    async def list_published_mm_app_async(
        self,
        request: main_models.ListPublishedMmAppRequest,
    ) -> main_models.ListPublishedMmAppResponse:
        runtime = RuntimeOptions()
        return await self.list_published_mm_app_with_options_async(request, runtime)

    def mm_app_binding_mcp_with_options(
        self,
        tmp_req: main_models.MmAppBindingMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MmAppBindingMcpResponse:
        tmp_req.validate()
        request = main_models.MmAppBindingMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.mcps):
            request.mcps_shrink = Utils.array_to_string_with_specified_style(tmp_req.mcps, 'Mcps', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.mcps_shrink):
            query['Mcps'] = request.mcps_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MmAppBindingMcp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MmAppBindingMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def mm_app_binding_mcp_with_options_async(
        self,
        tmp_req: main_models.MmAppBindingMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MmAppBindingMcpResponse:
        tmp_req.validate()
        request = main_models.MmAppBindingMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.mcps):
            request.mcps_shrink = Utils.array_to_string_with_specified_style(tmp_req.mcps, 'Mcps', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.mcps_shrink):
            query['Mcps'] = request.mcps_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MmAppBindingMcp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MmAppBindingMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mm_app_binding_mcp(
        self,
        request: main_models.MmAppBindingMcpRequest,
    ) -> main_models.MmAppBindingMcpResponse:
        runtime = RuntimeOptions()
        return self.mm_app_binding_mcp_with_options(request, runtime)

    async def mm_app_binding_mcp_async(
        self,
        request: main_models.MmAppBindingMcpRequest,
    ) -> main_models.MmAppBindingMcpResponse:
        runtime = RuntimeOptions()
        return await self.mm_app_binding_mcp_with_options_async(request, runtime)

    def mm_app_binding_rag_with_options(
        self,
        tmp_req: main_models.MmAppBindingRagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MmAppBindingRagResponse:
        tmp_req.validate()
        request = main_models.MmAppBindingRagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.knowledge_base_code_list):
            request.knowledge_base_code_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_base_code_list, 'KnowledgeBaseCodeList', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.knowledge_base_code_list_shrink):
            query['KnowledgeBaseCodeList'] = request.knowledge_base_code_list_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MmAppBindingRag',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MmAppBindingRagResponse(),
            self.call_api(params, req, runtime)
        )

    async def mm_app_binding_rag_with_options_async(
        self,
        tmp_req: main_models.MmAppBindingRagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MmAppBindingRagResponse:
        tmp_req.validate()
        request = main_models.MmAppBindingRagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.knowledge_base_code_list):
            request.knowledge_base_code_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_base_code_list, 'KnowledgeBaseCodeList', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.knowledge_base_code_list_shrink):
            query['KnowledgeBaseCodeList'] = request.knowledge_base_code_list_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MmAppBindingRag',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MmAppBindingRagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mm_app_binding_rag(
        self,
        request: main_models.MmAppBindingRagRequest,
    ) -> main_models.MmAppBindingRagResponse:
        runtime = RuntimeOptions()
        return self.mm_app_binding_rag_with_options(request, runtime)

    async def mm_app_binding_rag_async(
        self,
        request: main_models.MmAppBindingRagRequest,
    ) -> main_models.MmAppBindingRagResponse:
        runtime = RuntimeOptions()
        return await self.mm_app_binding_rag_with_options_async(request, runtime)

    def patch_memory_config_with_options(
        self,
        request: main_models.PatchMemoryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PatchMemoryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_update):
            query['AutoUpdate'] = request.auto_update
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PatchMemoryConfig',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PatchMemoryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def patch_memory_config_with_options_async(
        self,
        request: main_models.PatchMemoryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PatchMemoryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_update):
            query['AutoUpdate'] = request.auto_update
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PatchMemoryConfig',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PatchMemoryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def patch_memory_config(
        self,
        request: main_models.PatchMemoryConfigRequest,
    ) -> main_models.PatchMemoryConfigResponse:
        runtime = RuntimeOptions()
        return self.patch_memory_config_with_options(request, runtime)

    async def patch_memory_config_async(
        self,
        request: main_models.PatchMemoryConfigRequest,
    ) -> main_models.PatchMemoryConfigResponse:
        runtime = RuntimeOptions()
        return await self.patch_memory_config_with_options_async(request, runtime)

    def publish_mm_app_with_options(
        self,
        request: main_models.PublishMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishMmAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_mm_app_with_options_async(
        self,
        request: main_models.PublishMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishMmAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_mm_app(
        self,
        request: main_models.PublishMmAppRequest,
    ) -> main_models.PublishMmAppResponse:
        runtime = RuntimeOptions()
        return self.publish_mm_app_with_options(request, runtime)

    async def publish_mm_app_async(
        self,
        request: main_models.PublishMmAppRequest,
    ) -> main_models.PublishMmAppResponse:
        runtime = RuntimeOptions()
        return await self.publish_mm_app_with_options_async(request, runtime)

    def query_memory_config_with_options(
        self,
        request: main_models.QueryMemoryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMemoryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMemoryConfig',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMemoryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_memory_config_with_options_async(
        self,
        request: main_models.QueryMemoryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMemoryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMemoryConfig',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMemoryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_memory_config(
        self,
        request: main_models.QueryMemoryConfigRequest,
    ) -> main_models.QueryMemoryConfigResponse:
        runtime = RuntimeOptions()
        return self.query_memory_config_with_options(request, runtime)

    async def query_memory_config_async(
        self,
        request: main_models.QueryMemoryConfigRequest,
    ) -> main_models.QueryMemoryConfigResponse:
        runtime = RuntimeOptions()
        return await self.query_memory_config_with_options_async(request, runtime)

    def query_memory_list_with_options(
        self,
        request: main_models.QueryMemoryListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMemoryListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMemoryList',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMemoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_memory_list_with_options_async(
        self,
        request: main_models.QueryMemoryListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMemoryListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMemoryList',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMemoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_memory_list(
        self,
        request: main_models.QueryMemoryListRequest,
    ) -> main_models.QueryMemoryListResponse:
        runtime = RuntimeOptions()
        return self.query_memory_list_with_options(request, runtime)

    async def query_memory_list_async(
        self,
        request: main_models.QueryMemoryListRequest,
    ) -> main_models.QueryMemoryListResponse:
        runtime = RuntimeOptions()
        return await self.query_memory_list_with_options_async(request, runtime)

    def query_profile_with_options(
        self,
        request: main_models.QueryProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryProfile',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_profile_with_options_async(
        self,
        request: main_models.QueryProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryProfile',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_profile(
        self,
        request: main_models.QueryProfileRequest,
    ) -> main_models.QueryProfileResponse:
        runtime = RuntimeOptions()
        return self.query_profile_with_options(request, runtime)

    async def query_profile_async(
        self,
        request: main_models.QueryProfileRequest,
    ) -> main_models.QueryProfileResponse:
        runtime = RuntimeOptions()
        return await self.query_profile_with_options_async(request, runtime)

    def query_user_profile_with_options(
        self,
        request: main_models.QueryUserProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserProfile',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_profile_with_options_async(
        self,
        request: main_models.QueryUserProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserProfile',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_profile(
        self,
        request: main_models.QueryUserProfileRequest,
    ) -> main_models.QueryUserProfileResponse:
        runtime = RuntimeOptions()
        return self.query_user_profile_with_options(request, runtime)

    async def query_user_profile_async(
        self,
        request: main_models.QueryUserProfileRequest,
    ) -> main_models.QueryUserProfileResponse:
        runtime = RuntimeOptions()
        return await self.query_user_profile_with_options_async(request, runtime)

    def update_command_with_options(
        self,
        tmp_req: main_models.UpdateCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCommandResponse:
        tmp_req.validate()
        request = main_models.UpdateCommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tool_examples):
            request.tool_examples_shrink = Utils.array_to_string_with_specified_style(tmp_req.tool_examples, 'ToolExamples', 'json')
        if not DaraCore.is_null(tmp_req.tool_params):
            request.tool_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.tool_params, 'ToolParams', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.tool_description):
            query['ToolDescription'] = request.tool_description
        if not DaraCore.is_null(request.tool_examples_shrink):
            query['ToolExamples'] = request.tool_examples_shrink
        if not DaraCore.is_null(request.tool_id):
            query['ToolId'] = request.tool_id
        if not DaraCore.is_null(request.tool_name):
            query['ToolName'] = request.tool_name
        if not DaraCore.is_null(request.tool_params_shrink):
            query['ToolParams'] = request.tool_params_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCommand',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_command_with_options_async(
        self,
        tmp_req: main_models.UpdateCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCommandResponse:
        tmp_req.validate()
        request = main_models.UpdateCommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tool_examples):
            request.tool_examples_shrink = Utils.array_to_string_with_specified_style(tmp_req.tool_examples, 'ToolExamples', 'json')
        if not DaraCore.is_null(tmp_req.tool_params):
            request.tool_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.tool_params, 'ToolParams', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.tool_description):
            query['ToolDescription'] = request.tool_description
        if not DaraCore.is_null(request.tool_examples_shrink):
            query['ToolExamples'] = request.tool_examples_shrink
        if not DaraCore.is_null(request.tool_id):
            query['ToolId'] = request.tool_id
        if not DaraCore.is_null(request.tool_name):
            query['ToolName'] = request.tool_name
        if not DaraCore.is_null(request.tool_params_shrink):
            query['ToolParams'] = request.tool_params_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCommand',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_command(
        self,
        request: main_models.UpdateCommandRequest,
    ) -> main_models.UpdateCommandResponse:
        runtime = RuntimeOptions()
        return self.update_command_with_options(request, runtime)

    async def update_command_async(
        self,
        request: main_models.UpdateCommandRequest,
    ) -> main_models.UpdateCommandResponse:
        runtime = RuntimeOptions()
        return await self.update_command_with_options_async(request, runtime)

    def update_memory_with_options(
        self,
        tmp_req: main_models.UpdateMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMemoryResponse:
        tmp_req.validate()
        request = main_models.UpdateMemoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.meta_data):
            request.meta_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.meta_data, 'MetaData', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.memory_node_id):
            query['MemoryNodeId'] = request.memory_node_id
        if not DaraCore.is_null(request.meta_data_shrink):
            query['MetaData'] = request.meta_data_shrink
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMemory',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_memory_with_options_async(
        self,
        tmp_req: main_models.UpdateMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMemoryResponse:
        tmp_req.validate()
        request = main_models.UpdateMemoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.meta_data):
            request.meta_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.meta_data, 'MetaData', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.memory_node_id):
            query['MemoryNodeId'] = request.memory_node_id
        if not DaraCore.is_null(request.meta_data_shrink):
            query['MetaData'] = request.meta_data_shrink
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMemory',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_memory(
        self,
        request: main_models.UpdateMemoryRequest,
    ) -> main_models.UpdateMemoryResponse:
        runtime = RuntimeOptions()
        return self.update_memory_with_options(request, runtime)

    async def update_memory_async(
        self,
        request: main_models.UpdateMemoryRequest,
    ) -> main_models.UpdateMemoryResponse:
        runtime = RuntimeOptions()
        return await self.update_memory_with_options_async(request, runtime)

    def update_mm_app_with_options(
        self,
        tmp_req: main_models.UpdateMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppResponse:
        tmp_req.validate()
        request = main_models.UpdateMmAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.binding_config):
            request.binding_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.binding_config, 'BindingConfig', 'json')
        if not DaraCore.is_null(tmp_req.conversation_config):
            request.conversation_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.conversation_config, 'ConversationConfig', 'json')
        if not DaraCore.is_null(tmp_req.model_config):
            request.model_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_config, 'ModelConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.binding_config_shrink):
            query['BindingConfig'] = request.binding_config_shrink
        if not DaraCore.is_null(request.conversation_config_shrink):
            query['ConversationConfig'] = request.conversation_config_shrink
        if not DaraCore.is_null(request.model_config_shrink):
            query['ModelConfig'] = request.model_config_shrink
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mm_app_with_options_async(
        self,
        tmp_req: main_models.UpdateMmAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppResponse:
        tmp_req.validate()
        request = main_models.UpdateMmAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.binding_config):
            request.binding_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.binding_config, 'BindingConfig', 'json')
        if not DaraCore.is_null(tmp_req.conversation_config):
            request.conversation_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.conversation_config, 'ConversationConfig', 'json')
        if not DaraCore.is_null(tmp_req.model_config):
            request.model_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_config, 'ModelConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.binding_config_shrink):
            query['BindingConfig'] = request.binding_config_shrink
        if not DaraCore.is_null(request.conversation_config_shrink):
            query['ConversationConfig'] = request.conversation_config_shrink
        if not DaraCore.is_null(request.model_config_shrink):
            query['ModelConfig'] = request.model_config_shrink
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmApp',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mm_app(
        self,
        request: main_models.UpdateMmAppRequest,
    ) -> main_models.UpdateMmAppResponse:
        runtime = RuntimeOptions()
        return self.update_mm_app_with_options(request, runtime)

    async def update_mm_app_async(
        self,
        request: main_models.UpdateMmAppRequest,
    ) -> main_models.UpdateMmAppResponse:
        runtime = RuntimeOptions()
        return await self.update_mm_app_with_options_async(request, runtime)

    def update_mm_app_memory_with_options(
        self,
        request: main_models.UpdateMmAppMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmAppMemory',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mm_app_memory_with_options_async(
        self,
        request: main_models.UpdateMmAppMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmAppMemory',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mm_app_memory(
        self,
        request: main_models.UpdateMmAppMemoryRequest,
    ) -> main_models.UpdateMmAppMemoryResponse:
        runtime = RuntimeOptions()
        return self.update_mm_app_memory_with_options(request, runtime)

    async def update_mm_app_memory_async(
        self,
        request: main_models.UpdateMmAppMemoryRequest,
    ) -> main_models.UpdateMmAppMemoryResponse:
        runtime = RuntimeOptions()
        return await self.update_mm_app_memory_with_options_async(request, runtime)

    def update_mm_app_rag_with_options(
        self,
        request: main_models.UpdateMmAppRagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppRagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmAppRag',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppRagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mm_app_rag_with_options_async(
        self,
        request: main_models.UpdateMmAppRagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppRagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmAppRag',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppRagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mm_app_rag(
        self,
        request: main_models.UpdateMmAppRagRequest,
    ) -> main_models.UpdateMmAppRagResponse:
        runtime = RuntimeOptions()
        return self.update_mm_app_rag_with_options(request, runtime)

    async def update_mm_app_rag_async(
        self,
        request: main_models.UpdateMmAppRagRequest,
    ) -> main_models.UpdateMmAppRagResponse:
        runtime = RuntimeOptions()
        return await self.update_mm_app_rag_with_options_async(request, runtime)

    def update_mm_app_rag_config_with_options(
        self,
        request: main_models.UpdateMmAppRagConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppRagConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.prompt_strategy):
            query['PromptStrategy'] = request.prompt_strategy
        if not DaraCore.is_null(request.retrieve_max_length):
            query['RetrieveMaxLength'] = request.retrieve_max_length
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmAppRagConfig',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppRagConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mm_app_rag_config_with_options_async(
        self,
        request: main_models.UpdateMmAppRagConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppRagConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.prompt_strategy):
            query['PromptStrategy'] = request.prompt_strategy
        if not DaraCore.is_null(request.retrieve_max_length):
            query['RetrieveMaxLength'] = request.retrieve_max_length
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmAppRagConfig',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppRagConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mm_app_rag_config(
        self,
        request: main_models.UpdateMmAppRagConfigRequest,
    ) -> main_models.UpdateMmAppRagConfigResponse:
        runtime = RuntimeOptions()
        return self.update_mm_app_rag_config_with_options(request, runtime)

    async def update_mm_app_rag_config_async(
        self,
        request: main_models.UpdateMmAppRagConfigRequest,
    ) -> main_models.UpdateMmAppRagConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_mm_app_rag_config_with_options_async(request, runtime)

    def update_mm_app_rag_weight_with_options(
        self,
        tmp_req: main_models.UpdateMmAppRagWeightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppRagWeightResponse:
        tmp_req.validate()
        request = main_models.UpdateMmAppRagWeightShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rank_weights):
            request.rank_weights_shrink = Utils.array_to_string_with_specified_style(tmp_req.rank_weights, 'RankWeights', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.rank_weights_shrink):
            query['RankWeights'] = request.rank_weights_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmAppRagWeight',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppRagWeightResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mm_app_rag_weight_with_options_async(
        self,
        tmp_req: main_models.UpdateMmAppRagWeightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppRagWeightResponse:
        tmp_req.validate()
        request = main_models.UpdateMmAppRagWeightShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rank_weights):
            request.rank_weights_shrink = Utils.array_to_string_with_specified_style(tmp_req.rank_weights, 'RankWeights', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.rank_weights_shrink):
            query['RankWeights'] = request.rank_weights_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmAppRagWeight',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppRagWeightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mm_app_rag_weight(
        self,
        request: main_models.UpdateMmAppRagWeightRequest,
    ) -> main_models.UpdateMmAppRagWeightResponse:
        runtime = RuntimeOptions()
        return self.update_mm_app_rag_weight_with_options(request, runtime)

    async def update_mm_app_rag_weight_async(
        self,
        request: main_models.UpdateMmAppRagWeightRequest,
    ) -> main_models.UpdateMmAppRagWeightResponse:
        runtime = RuntimeOptions()
        return await self.update_mm_app_rag_weight_with_options_async(request, runtime)

    def update_mm_app_transition_with_options(
        self,
        request: main_models.UpdateMmAppTransitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppTransitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmAppTransition',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppTransitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mm_app_transition_with_options_async(
        self,
        request: main_models.UpdateMmAppTransitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmAppTransitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmAppTransition',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmAppTransitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mm_app_transition(
        self,
        request: main_models.UpdateMmAppTransitionRequest,
    ) -> main_models.UpdateMmAppTransitionResponse:
        runtime = RuntimeOptions()
        return self.update_mm_app_transition_with_options(request, runtime)

    async def update_mm_app_transition_async(
        self,
        request: main_models.UpdateMmAppTransitionRequest,
    ) -> main_models.UpdateMmAppTransitionResponse:
        runtime = RuntimeOptions()
        return await self.update_mm_app_transition_with_options_async(request, runtime)

    def update_profile_with_options(
        self,
        tmp_req: main_models.UpdateProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProfileResponse:
        tmp_req.validate()
        request = main_models.UpdateProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes_operations):
            request.attributes_operations_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes_operations, 'AttributesOperations', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.attributes_operations_shrink):
            query['AttributesOperations'] = request.attributes_operations_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProfile',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_profile_with_options_async(
        self,
        tmp_req: main_models.UpdateProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProfileResponse:
        tmp_req.validate()
        request = main_models.UpdateProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes_operations):
            request.attributes_operations_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes_operations, 'AttributesOperations', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.attributes_operations_shrink):
            query['AttributesOperations'] = request.attributes_operations_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.user_defined_id):
            query['UserDefinedId'] = request.user_defined_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProfile',
            version = '2025-09-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_profile(
        self,
        request: main_models.UpdateProfileRequest,
    ) -> main_models.UpdateProfileResponse:
        runtime = RuntimeOptions()
        return self.update_profile_with_options(request, runtime)

    async def update_profile_async(
        self,
        request: main_models.UpdateProfileRequest,
    ) -> main_models.UpdateProfileResponse:
        runtime = RuntimeOptions()
        return await self.update_profile_with_options_async(request, runtime)
