# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_websitebuild20250429 import models as main_models
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
        self._endpoint = self.get_endpoint('websitebuild', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_supabase_for_admin_with_options(
        self,
        request: main_models.AllocateSupabaseForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateSupabaseForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateSupabaseForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateSupabaseForAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_supabase_for_admin_with_options_async(
        self,
        request: main_models.AllocateSupabaseForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateSupabaseForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateSupabaseForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateSupabaseForAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_supabase_for_admin(
        self,
        request: main_models.AllocateSupabaseForAdminRequest,
    ) -> main_models.AllocateSupabaseForAdminResponse:
        runtime = RuntimeOptions()
        return self.allocate_supabase_for_admin_with_options(request, runtime)

    async def allocate_supabase_for_admin_async(
        self,
        request: main_models.AllocateSupabaseForAdminRequest,
    ) -> main_models.AllocateSupabaseForAdminResponse:
        runtime = RuntimeOptions()
        return await self.allocate_supabase_for_admin_with_options_async(request, runtime)

    def batch_check_resource_measure_with_options(
        self,
        request: main_models.BatchCheckResourceMeasureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCheckResourceMeasureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.belong_id):
            query['BelongId'] = request.belong_id
        if not DaraCore.is_null(request.belong_id_type):
            query['BelongIdType'] = request.belong_id_type
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.esp_biz_id):
            query['EspBizId'] = request.esp_biz_id
        if not DaraCore.is_null(request.order_component_params):
            query['OrderComponentParams'] = request.order_component_params
        if not DaraCore.is_null(request.resource_check_items):
            query['ResourceCheckItems'] = request.resource_check_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchCheckResourceMeasure',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCheckResourceMeasureResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_check_resource_measure_with_options_async(
        self,
        request: main_models.BatchCheckResourceMeasureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCheckResourceMeasureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.belong_id):
            query['BelongId'] = request.belong_id
        if not DaraCore.is_null(request.belong_id_type):
            query['BelongIdType'] = request.belong_id_type
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.esp_biz_id):
            query['EspBizId'] = request.esp_biz_id
        if not DaraCore.is_null(request.order_component_params):
            query['OrderComponentParams'] = request.order_component_params
        if not DaraCore.is_null(request.resource_check_items):
            query['ResourceCheckItems'] = request.resource_check_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchCheckResourceMeasure',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCheckResourceMeasureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_check_resource_measure(
        self,
        request: main_models.BatchCheckResourceMeasureRequest,
    ) -> main_models.BatchCheckResourceMeasureResponse:
        runtime = RuntimeOptions()
        return self.batch_check_resource_measure_with_options(request, runtime)

    async def batch_check_resource_measure_async(
        self,
        request: main_models.BatchCheckResourceMeasureRequest,
    ) -> main_models.BatchCheckResourceMeasureResponse:
        runtime = RuntimeOptions()
        return await self.batch_check_resource_measure_with_options_async(request, runtime)

    def bind_app_domain_with_options(
        self,
        request: main_models.BindAppDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAppDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAppDomain',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAppDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_app_domain_with_options_async(
        self,
        request: main_models.BindAppDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAppDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAppDomain',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAppDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_app_domain(
        self,
        request: main_models.BindAppDomainRequest,
    ) -> main_models.BindAppDomainResponse:
        runtime = RuntimeOptions()
        return self.bind_app_domain_with_options(request, runtime)

    async def bind_app_domain_async(
        self,
        request: main_models.BindAppDomainRequest,
    ) -> main_models.BindAppDomainResponse:
        runtime = RuntimeOptions()
        return await self.bind_app_domain_with_options_async(request, runtime)

    def check_resource_measure_with_options(
        self,
        request: main_models.CheckResourceMeasureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckResourceMeasureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.belong_id):
            query['BelongId'] = request.belong_id
        if not DaraCore.is_null(request.belong_id_type):
            query['BelongIdType'] = request.belong_id_type
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.esp_biz_id):
            query['EspBizId'] = request.esp_biz_id
        if not DaraCore.is_null(request.order_component_params):
            query['OrderComponentParams'] = request.order_component_params
        if not DaraCore.is_null(request.resource_code):
            query['ResourceCode'] = request.resource_code
        if not DaraCore.is_null(request.resource_value):
            query['ResourceValue'] = request.resource_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckResourceMeasure',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckResourceMeasureResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_resource_measure_with_options_async(
        self,
        request: main_models.CheckResourceMeasureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckResourceMeasureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.belong_id):
            query['BelongId'] = request.belong_id
        if not DaraCore.is_null(request.belong_id_type):
            query['BelongIdType'] = request.belong_id_type
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.esp_biz_id):
            query['EspBizId'] = request.esp_biz_id
        if not DaraCore.is_null(request.order_component_params):
            query['OrderComponentParams'] = request.order_component_params
        if not DaraCore.is_null(request.resource_code):
            query['ResourceCode'] = request.resource_code
        if not DaraCore.is_null(request.resource_value):
            query['ResourceValue'] = request.resource_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckResourceMeasure',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckResourceMeasureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_resource_measure(
        self,
        request: main_models.CheckResourceMeasureRequest,
    ) -> main_models.CheckResourceMeasureResponse:
        runtime = RuntimeOptions()
        return self.check_resource_measure_with_options(request, runtime)

    async def check_resource_measure_async(
        self,
        request: main_models.CheckResourceMeasureRequest,
    ) -> main_models.CheckResourceMeasureResponse:
        runtime = RuntimeOptions()
        return await self.check_resource_measure_with_options_async(request, runtime)

    def check_user_resource_measure_with_options(
        self,
        request: main_models.CheckUserResourceMeasureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUserResourceMeasureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.belong_id):
            query['BelongId'] = request.belong_id
        if not DaraCore.is_null(request.belong_id_type):
            query['BelongIdType'] = request.belong_id_type
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.esp_biz_id):
            query['EspBizId'] = request.esp_biz_id
        if not DaraCore.is_null(request.order_component_params):
            query['OrderComponentParams'] = request.order_component_params
        if not DaraCore.is_null(request.resource_code):
            query['ResourceCode'] = request.resource_code
        if not DaraCore.is_null(request.resource_value):
            query['ResourceValue'] = request.resource_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckUserResourceMeasure',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUserResourceMeasureResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_user_resource_measure_with_options_async(
        self,
        request: main_models.CheckUserResourceMeasureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUserResourceMeasureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.belong_id):
            query['BelongId'] = request.belong_id
        if not DaraCore.is_null(request.belong_id_type):
            query['BelongIdType'] = request.belong_id_type
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.esp_biz_id):
            query['EspBizId'] = request.esp_biz_id
        if not DaraCore.is_null(request.order_component_params):
            query['OrderComponentParams'] = request.order_component_params
        if not DaraCore.is_null(request.resource_code):
            query['ResourceCode'] = request.resource_code
        if not DaraCore.is_null(request.resource_value):
            query['ResourceValue'] = request.resource_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckUserResourceMeasure',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUserResourceMeasureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_user_resource_measure(
        self,
        request: main_models.CheckUserResourceMeasureRequest,
    ) -> main_models.CheckUserResourceMeasureResponse:
        runtime = RuntimeOptions()
        return self.check_user_resource_measure_with_options(request, runtime)

    async def check_user_resource_measure_async(
        self,
        request: main_models.CheckUserResourceMeasureRequest,
    ) -> main_models.CheckUserResourceMeasureResponse:
        runtime = RuntimeOptions()
        return await self.check_user_resource_measure_with_options_async(request, runtime)

    def copy_app_plugin_config_with_options(
        self,
        request: main_models.CopyAppPluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyAppPluginConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.source_biz_id):
            query['SourceBizId'] = request.source_biz_id
        if not DaraCore.is_null(request.target_biz_id):
            query['TargetBizId'] = request.target_biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyAppPluginConfig',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyAppPluginConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_app_plugin_config_with_options_async(
        self,
        request: main_models.CopyAppPluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyAppPluginConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.source_biz_id):
            query['SourceBizId'] = request.source_biz_id
        if not DaraCore.is_null(request.target_biz_id):
            query['TargetBizId'] = request.target_biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyAppPluginConfig',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyAppPluginConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_app_plugin_config(
        self,
        request: main_models.CopyAppPluginConfigRequest,
    ) -> main_models.CopyAppPluginConfigResponse:
        runtime = RuntimeOptions()
        return self.copy_app_plugin_config_with_options(request, runtime)

    async def copy_app_plugin_config_async(
        self,
        request: main_models.CopyAppPluginConfigRequest,
    ) -> main_models.CopyAppPluginConfigResponse:
        runtime = RuntimeOptions()
        return await self.copy_app_plugin_config_with_options_async(request, runtime)

    def create_aistaff_chat_with_options(
        self,
        request: main_models.CreateAIStaffChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAIStaffChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.chat_id):
            body['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        body_flat = {}
        if not DaraCore.is_null(request.meta_data):
            body_flat['MetaData'] = request.meta_data
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAIStaffChat',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAIStaffChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aistaff_chat_with_options_async(
        self,
        request: main_models.CreateAIStaffChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAIStaffChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.chat_id):
            body['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        body_flat = {}
        if not DaraCore.is_null(request.meta_data):
            body_flat['MetaData'] = request.meta_data
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAIStaffChat',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAIStaffChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aistaff_chat(
        self,
        request: main_models.CreateAIStaffChatRequest,
    ) -> main_models.CreateAIStaffChatResponse:
        runtime = RuntimeOptions()
        return self.create_aistaff_chat_with_options(request, runtime)

    async def create_aistaff_chat_async(
        self,
        request: main_models.CreateAIStaffChatRequest,
    ) -> main_models.CreateAIStaffChatResponse:
        runtime = RuntimeOptions()
        return await self.create_aistaff_chat_with_options_async(request, runtime)

    def create_aistaff_conversation_with_options(
        self,
        request: main_models.CreateAIStaffConversationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAIStaffConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.text):
            body['Text'] = request.text
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAIStaffConversation',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAIStaffConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aistaff_conversation_with_options_async(
        self,
        request: main_models.CreateAIStaffConversationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAIStaffConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.text):
            body['Text'] = request.text
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAIStaffConversation',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAIStaffConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aistaff_conversation(
        self,
        request: main_models.CreateAIStaffConversationRequest,
    ) -> main_models.CreateAIStaffConversationResponse:
        runtime = RuntimeOptions()
        return self.create_aistaff_conversation_with_options(request, runtime)

    async def create_aistaff_conversation_async(
        self,
        request: main_models.CreateAIStaffConversationRequest,
    ) -> main_models.CreateAIStaffConversationResponse:
        runtime = RuntimeOptions()
        return await self.create_aistaff_conversation_with_options_async(request, runtime)

    def create_app_assistant_agent_with_options(
        self,
        request: main_models.CreateAppAssistantAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppAssistantAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.platform_type):
            query['PlatformType'] = request.platform_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppAssistantAgent',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppAssistantAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_assistant_agent_with_options_async(
        self,
        request: main_models.CreateAppAssistantAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppAssistantAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.platform_type):
            query['PlatformType'] = request.platform_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppAssistantAgent',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppAssistantAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_assistant_agent(
        self,
        request: main_models.CreateAppAssistantAgentRequest,
    ) -> main_models.CreateAppAssistantAgentResponse:
        runtime = RuntimeOptions()
        return self.create_app_assistant_agent_with_options(request, runtime)

    async def create_app_assistant_agent_async(
        self,
        request: main_models.CreateAppAssistantAgentRequest,
    ) -> main_models.CreateAppAssistantAgentResponse:
        runtime = RuntimeOptions()
        return await self.create_app_assistant_agent_with_options_async(request, runtime)

    def create_app_assistant_agent_sso_login_with_options(
        self,
        request: main_models.CreateAppAssistantAgentSsoLoginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppAssistantAgentSsoLoginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.platform_type):
            query['PlatformType'] = request.platform_type
        if not DaraCore.is_null(request.target_url):
            query['TargetUrl'] = request.target_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppAssistantAgentSsoLogin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppAssistantAgentSsoLoginResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_assistant_agent_sso_login_with_options_async(
        self,
        request: main_models.CreateAppAssistantAgentSsoLoginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppAssistantAgentSsoLoginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.platform_type):
            query['PlatformType'] = request.platform_type
        if not DaraCore.is_null(request.target_url):
            query['TargetUrl'] = request.target_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppAssistantAgentSsoLogin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppAssistantAgentSsoLoginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_assistant_agent_sso_login(
        self,
        request: main_models.CreateAppAssistantAgentSsoLoginRequest,
    ) -> main_models.CreateAppAssistantAgentSsoLoginResponse:
        runtime = RuntimeOptions()
        return self.create_app_assistant_agent_sso_login_with_options(request, runtime)

    async def create_app_assistant_agent_sso_login_async(
        self,
        request: main_models.CreateAppAssistantAgentSsoLoginRequest,
    ) -> main_models.CreateAppAssistantAgentSsoLoginResponse:
        runtime = RuntimeOptions()
        return await self.create_app_assistant_agent_sso_login_with_options_async(request, runtime)

    def create_app_chat_with_sse(
        self,
        request: main_models.CreateAppChatRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.CreateAppChatResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.chat_id):
            query['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.messages):
            query['Messages'] = request.messages
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppChat',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = resp.event.data
                yield  DaraCore.from_map(
                    main_models.CreateAppChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def create_app_chat_with_sse_async(
        self,
        request: main_models.CreateAppChatRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.CreateAppChatResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.chat_id):
            query['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.messages):
            query['Messages'] = request.messages
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppChat',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = resp.event.data
                yield  DaraCore.from_map(
                    main_models.CreateAppChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def create_app_chat_with_options(
        self,
        request: main_models.CreateAppChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.chat_id):
            query['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.messages):
            query['Messages'] = request.messages
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppChat',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.CreateAppChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_chat_with_options_async(
        self,
        request: main_models.CreateAppChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.chat_id):
            query['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.messages):
            query['Messages'] = request.messages
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppChat',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.CreateAppChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_chat(
        self,
        request: main_models.CreateAppChatRequest,
    ) -> main_models.CreateAppChatResponse:
        runtime = RuntimeOptions()
        return self.create_app_chat_with_options(request, runtime)

    async def create_app_chat_async(
        self,
        request: main_models.CreateAppChatRequest,
    ) -> main_models.CreateAppChatResponse:
        runtime = RuntimeOptions()
        return await self.create_app_chat_with_options_async(request, runtime)

    def create_app_instance_with_options(
        self,
        tmp_req: main_models.CreateAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateAppInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_action):
            query['CreateAction'] = request.create_action
        if not DaraCore.is_null(request.deploy_area):
            query['DeployArea'] = request.deploy_area
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.site_version):
            query['SiteVersion'] = request.site_version
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstance',
            version = '2025-04-29',
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
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_action):
            query['CreateAction'] = request.create_action
        if not DaraCore.is_null(request.deploy_area):
            query['DeployArea'] = request.deploy_area
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.site_version):
            query['SiteVersion'] = request.site_version
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstance',
            version = '2025-04-29',
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

    def create_app_instance_ticket_with_options(
        self,
        request: main_models.CreateAppInstanceTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstanceTicket',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInstanceTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_instance_ticket_with_options_async(
        self,
        request: main_models.CreateAppInstanceTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstanceTicket',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInstanceTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_instance_ticket(
        self,
        request: main_models.CreateAppInstanceTicketRequest,
    ) -> main_models.CreateAppInstanceTicketResponse:
        runtime = RuntimeOptions()
        return self.create_app_instance_ticket_with_options(request, runtime)

    async def create_app_instance_ticket_async(
        self,
        request: main_models.CreateAppInstanceTicketRequest,
    ) -> main_models.CreateAppInstanceTicketResponse:
        runtime = RuntimeOptions()
        return await self.create_app_instance_ticket_with_options_async(request, runtime)

    def create_app_llm_api_key_for_partner_with_options(
        self,
        request: main_models.CreateAppLlmApiKeyForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppLlmApiKeyForPartnerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.ip_white_list):
            body['IpWhiteList'] = request.ip_white_list
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppLlmApiKeyForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppLlmApiKeyForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_llm_api_key_for_partner_with_options_async(
        self,
        request: main_models.CreateAppLlmApiKeyForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppLlmApiKeyForPartnerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.ip_white_list):
            body['IpWhiteList'] = request.ip_white_list
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppLlmApiKeyForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppLlmApiKeyForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_llm_api_key_for_partner(
        self,
        request: main_models.CreateAppLlmApiKeyForPartnerRequest,
    ) -> main_models.CreateAppLlmApiKeyForPartnerResponse:
        runtime = RuntimeOptions()
        return self.create_app_llm_api_key_for_partner_with_options(request, runtime)

    async def create_app_llm_api_key_for_partner_async(
        self,
        request: main_models.CreateAppLlmApiKeyForPartnerRequest,
    ) -> main_models.CreateAppLlmApiKeyForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.create_app_llm_api_key_for_partner_with_options_async(request, runtime)

    def create_app_token_service_with_options(
        self,
        request: main_models.CreateAppTokenServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppTokenServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_action):
            query['CreateAction'] = request.create_action
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppTokenService',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppTokenServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_token_service_with_options_async(
        self,
        request: main_models.CreateAppTokenServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppTokenServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_action):
            query['CreateAction'] = request.create_action
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppTokenService',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppTokenServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_token_service(
        self,
        request: main_models.CreateAppTokenServiceRequest,
    ) -> main_models.CreateAppTokenServiceResponse:
        runtime = RuntimeOptions()
        return self.create_app_token_service_with_options(request, runtime)

    async def create_app_token_service_async(
        self,
        request: main_models.CreateAppTokenServiceRequest,
    ) -> main_models.CreateAppTokenServiceResponse:
        runtime = RuntimeOptions()
        return await self.create_app_token_service_with_options_async(request, runtime)

    def create_logo_task_with_options(
        self,
        request: main_models.CreateLogoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logo_version):
            query['LogoVersion'] = request.logo_version
        if not DaraCore.is_null(request.negative_prompt):
            query['NegativePrompt'] = request.negative_prompt
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogoTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_logo_task_with_options_async(
        self,
        request: main_models.CreateLogoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logo_version):
            query['LogoVersion'] = request.logo_version
        if not DaraCore.is_null(request.negative_prompt):
            query['NegativePrompt'] = request.negative_prompt
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogoTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_logo_task(
        self,
        request: main_models.CreateLogoTaskRequest,
    ) -> main_models.CreateLogoTaskResponse:
        runtime = RuntimeOptions()
        return self.create_logo_task_with_options(request, runtime)

    async def create_logo_task_async(
        self,
        request: main_models.CreateLogoTaskRequest,
    ) -> main_models.CreateLogoTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_logo_task_with_options_async(request, runtime)

    def create_material_directory_with_options(
        self,
        request: main_models.CreateMaterialDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMaterialDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parent_directory_id):
            query['ParentDirectoryId'] = request.parent_directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMaterialDirectory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMaterialDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_material_directory_with_options_async(
        self,
        request: main_models.CreateMaterialDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMaterialDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parent_directory_id):
            query['ParentDirectoryId'] = request.parent_directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMaterialDirectory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMaterialDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_material_directory(
        self,
        request: main_models.CreateMaterialDirectoryRequest,
    ) -> main_models.CreateMaterialDirectoryResponse:
        runtime = RuntimeOptions()
        return self.create_material_directory_with_options(request, runtime)

    async def create_material_directory_async(
        self,
        request: main_models.CreateMaterialDirectoryRequest,
    ) -> main_models.CreateMaterialDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.create_material_directory_with_options_async(request, runtime)

    def delete_app_domain_certificate_with_options(
        self,
        request: main_models.DeleteAppDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppDomainCertificate',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_domain_certificate_with_options_async(
        self,
        request: main_models.DeleteAppDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppDomainCertificate',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_domain_certificate(
        self,
        request: main_models.DeleteAppDomainCertificateRequest,
    ) -> main_models.DeleteAppDomainCertificateResponse:
        runtime = RuntimeOptions()
        return self.delete_app_domain_certificate_with_options(request, runtime)

    async def delete_app_domain_certificate_async(
        self,
        request: main_models.DeleteAppDomainCertificateRequest,
    ) -> main_models.DeleteAppDomainCertificateResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_domain_certificate_with_options_async(request, runtime)

    def delete_app_domain_redirect_with_options(
        self,
        request: main_models.DeleteAppDomainRedirectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppDomainRedirectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppDomainRedirect',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppDomainRedirectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_domain_redirect_with_options_async(
        self,
        request: main_models.DeleteAppDomainRedirectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppDomainRedirectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppDomainRedirect',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppDomainRedirectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_domain_redirect(
        self,
        request: main_models.DeleteAppDomainRedirectRequest,
    ) -> main_models.DeleteAppDomainRedirectResponse:
        runtime = RuntimeOptions()
        return self.delete_app_domain_redirect_with_options(request, runtime)

    async def delete_app_domain_redirect_async(
        self,
        request: main_models.DeleteAppDomainRedirectRequest,
    ) -> main_models.DeleteAppDomainRedirectResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_domain_redirect_with_options_async(request, runtime)

    def delete_app_instance_file_with_options(
        self,
        request: main_models.DeleteAppInstanceFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppInstanceFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppInstanceFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppInstanceFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_instance_file_with_options_async(
        self,
        request: main_models.DeleteAppInstanceFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppInstanceFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppInstanceFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppInstanceFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_instance_file(
        self,
        request: main_models.DeleteAppInstanceFileRequest,
    ) -> main_models.DeleteAppInstanceFileResponse:
        runtime = RuntimeOptions()
        return self.delete_app_instance_file_with_options(request, runtime)

    async def delete_app_instance_file_async(
        self,
        request: main_models.DeleteAppInstanceFileRequest,
    ) -> main_models.DeleteAppInstanceFileResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_instance_file_with_options_async(request, runtime)

    def delete_app_supabase_secrets_with_options(
        self,
        request: main_models.DeleteAppSupabaseSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppSupabaseSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.keys_json):
            query['KeysJson'] = request.keys_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppSupabaseSecrets',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppSupabaseSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_supabase_secrets_with_options_async(
        self,
        request: main_models.DeleteAppSupabaseSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppSupabaseSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.keys_json):
            query['KeysJson'] = request.keys_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppSupabaseSecrets',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppSupabaseSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_supabase_secrets(
        self,
        request: main_models.DeleteAppSupabaseSecretsRequest,
    ) -> main_models.DeleteAppSupabaseSecretsResponse:
        runtime = RuntimeOptions()
        return self.delete_app_supabase_secrets_with_options(request, runtime)

    async def delete_app_supabase_secrets_async(
        self,
        request: main_models.DeleteAppSupabaseSecretsRequest,
    ) -> main_models.DeleteAppSupabaseSecretsResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_supabase_secrets_with_options_async(request, runtime)

    def delete_material_directory_with_options(
        self,
        request: main_models.DeleteMaterialDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaterialDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaterialDirectory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMaterialDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_material_directory_with_options_async(
        self,
        request: main_models.DeleteMaterialDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaterialDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaterialDirectory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMaterialDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_material_directory(
        self,
        request: main_models.DeleteMaterialDirectoryRequest,
    ) -> main_models.DeleteMaterialDirectoryResponse:
        runtime = RuntimeOptions()
        return self.delete_material_directory_with_options(request, runtime)

    async def delete_material_directory_async(
        self,
        request: main_models.DeleteMaterialDirectoryRequest,
    ) -> main_models.DeleteMaterialDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_material_directory_with_options_async(request, runtime)

    def delete_material_task_with_options(
        self,
        tmp_req: main_models.DeleteMaterialTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaterialTaskResponse:
        tmp_req.validate()
        request = main_models.DeleteMaterialTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = {}
        if not DaraCore.is_null(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaterialTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMaterialTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_material_task_with_options_async(
        self,
        tmp_req: main_models.DeleteMaterialTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaterialTaskResponse:
        tmp_req.validate()
        request = main_models.DeleteMaterialTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = {}
        if not DaraCore.is_null(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaterialTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMaterialTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_material_task(
        self,
        request: main_models.DeleteMaterialTaskRequest,
    ) -> main_models.DeleteMaterialTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_material_task_with_options(request, runtime)

    async def delete_material_task_async(
        self,
        request: main_models.DeleteMaterialTaskRequest,
    ) -> main_models.DeleteMaterialTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_material_task_with_options_async(request, runtime)

    def describe_app_domain_dns_record_with_options(
        self,
        request: main_models.DescribeAppDomainDnsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppDomainDnsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppDomainDnsRecord',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppDomainDnsRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_domain_dns_record_with_options_async(
        self,
        request: main_models.DescribeAppDomainDnsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppDomainDnsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppDomainDnsRecord',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppDomainDnsRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_domain_dns_record(
        self,
        request: main_models.DescribeAppDomainDnsRecordRequest,
    ) -> main_models.DescribeAppDomainDnsRecordResponse:
        runtime = RuntimeOptions()
        return self.describe_app_domain_dns_record_with_options(request, runtime)

    async def describe_app_domain_dns_record_async(
        self,
        request: main_models.DescribeAppDomainDnsRecordRequest,
    ) -> main_models.DescribeAppDomainDnsRecordResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_domain_dns_record_with_options_async(request, runtime)

    def dispatch_console_apifor_partner_with_options(
        self,
        request: main_models.DispatchConsoleAPIForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DispatchConsoleAPIForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.live_token):
            query['LiveToken'] = request.live_token
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.site_host):
            query['SiteHost'] = request.site_host
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DispatchConsoleAPIForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DispatchConsoleAPIForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def dispatch_console_apifor_partner_with_options_async(
        self,
        request: main_models.DispatchConsoleAPIForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DispatchConsoleAPIForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.live_token):
            query['LiveToken'] = request.live_token
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.site_host):
            query['SiteHost'] = request.site_host
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DispatchConsoleAPIForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DispatchConsoleAPIForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dispatch_console_apifor_partner(
        self,
        request: main_models.DispatchConsoleAPIForPartnerRequest,
    ) -> main_models.DispatchConsoleAPIForPartnerResponse:
        runtime = RuntimeOptions()
        return self.dispatch_console_apifor_partner_with_options(request, runtime)

    async def dispatch_console_apifor_partner_async(
        self,
        request: main_models.DispatchConsoleAPIForPartnerRequest,
    ) -> main_models.DispatchConsoleAPIForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.dispatch_console_apifor_partner_with_options_async(request, runtime)

    def edit_plugin_config_with_options(
        self,
        request: main_models.EditPluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditPluginConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.plugin_config):
            query['PluginConfig'] = request.plugin_config
        if not DaraCore.is_null(request.plugin_desc):
            query['PluginDesc'] = request.plugin_desc
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.plugin_name):
            query['PluginName'] = request.plugin_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditPluginConfig',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditPluginConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_plugin_config_with_options_async(
        self,
        request: main_models.EditPluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditPluginConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.plugin_config):
            query['PluginConfig'] = request.plugin_config
        if not DaraCore.is_null(request.plugin_desc):
            query['PluginDesc'] = request.plugin_desc
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.plugin_name):
            query['PluginName'] = request.plugin_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditPluginConfig',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditPluginConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_plugin_config(
        self,
        request: main_models.EditPluginConfigRequest,
    ) -> main_models.EditPluginConfigResponse:
        runtime = RuntimeOptions()
        return self.edit_plugin_config_with_options(request, runtime)

    async def edit_plugin_config_async(
        self,
        request: main_models.EditPluginConfigRequest,
    ) -> main_models.EditPluginConfigResponse:
        runtime = RuntimeOptions()
        return await self.edit_plugin_config_with_options_async(request, runtime)

    def export_material_file_with_options(
        self,
        tmp_req: main_models.ExportMaterialFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportMaterialFileResponse:
        tmp_req.validate()
        request = main_models.ExportMaterialFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_ids):
            request.file_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_ids, 'FileIds', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.file_ids_shrink):
            query['FileIds'] = request.file_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportMaterialFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportMaterialFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_material_file_with_options_async(
        self,
        tmp_req: main_models.ExportMaterialFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportMaterialFileResponse:
        tmp_req.validate()
        request = main_models.ExportMaterialFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_ids):
            request.file_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_ids, 'FileIds', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.file_ids_shrink):
            query['FileIds'] = request.file_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportMaterialFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportMaterialFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_material_file(
        self,
        request: main_models.ExportMaterialFileRequest,
    ) -> main_models.ExportMaterialFileResponse:
        runtime = RuntimeOptions()
        return self.export_material_file_with_options(request, runtime)

    async def export_material_file_async(
        self,
        request: main_models.ExportMaterialFileRequest,
    ) -> main_models.ExportMaterialFileResponse:
        runtime = RuntimeOptions()
        return await self.export_material_file_with_options_async(request, runtime)

    def get_aistaff_preview_url_with_options(
        self,
        request: main_models.GetAIStaffPreviewUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAIStaffPreviewUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.restart):
            body['Restart'] = request.restart
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAIStaffPreviewUrl',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAIStaffPreviewUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aistaff_preview_url_with_options_async(
        self,
        request: main_models.GetAIStaffPreviewUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAIStaffPreviewUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.restart):
            body['Restart'] = request.restart
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAIStaffPreviewUrl',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAIStaffPreviewUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aistaff_preview_url(
        self,
        request: main_models.GetAIStaffPreviewUrlRequest,
    ) -> main_models.GetAIStaffPreviewUrlResponse:
        runtime = RuntimeOptions()
        return self.get_aistaff_preview_url_with_options(request, runtime)

    async def get_aistaff_preview_url_async(
        self,
        request: main_models.GetAIStaffPreviewUrlRequest,
    ) -> main_models.GetAIStaffPreviewUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_aistaff_preview_url_with_options_async(request, runtime)

    def get_app_code_workspace_detail_with_options(
        self,
        request: main_models.GetAppCodeWorkspaceDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppCodeWorkspaceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppCodeWorkspaceDetail',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppCodeWorkspaceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_code_workspace_detail_with_options_async(
        self,
        request: main_models.GetAppCodeWorkspaceDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppCodeWorkspaceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppCodeWorkspaceDetail',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppCodeWorkspaceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_code_workspace_detail(
        self,
        request: main_models.GetAppCodeWorkspaceDetailRequest,
    ) -> main_models.GetAppCodeWorkspaceDetailResponse:
        runtime = RuntimeOptions()
        return self.get_app_code_workspace_detail_with_options(request, runtime)

    async def get_app_code_workspace_detail_async(
        self,
        request: main_models.GetAppCodeWorkspaceDetailRequest,
    ) -> main_models.GetAppCodeWorkspaceDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_app_code_workspace_detail_with_options_async(request, runtime)

    def get_app_conversation_with_options(
        self,
        request: main_models.GetAppConversationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppConversationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppConversation',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_conversation_with_options_async(
        self,
        request: main_models.GetAppConversationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppConversationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppConversation',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_conversation(
        self,
        request: main_models.GetAppConversationRequest,
    ) -> main_models.GetAppConversationResponse:
        runtime = RuntimeOptions()
        return self.get_app_conversation_with_options(request, runtime)

    async def get_app_conversation_async(
        self,
        request: main_models.GetAppConversationRequest,
    ) -> main_models.GetAppConversationResponse:
        runtime = RuntimeOptions()
        return await self.get_app_conversation_with_options_async(request, runtime)

    def get_app_conversation_lock_status_with_options(
        self,
        request: main_models.GetAppConversationLockStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppConversationLockStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAppConversationLockStatus',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppConversationLockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_conversation_lock_status_with_options_async(
        self,
        request: main_models.GetAppConversationLockStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppConversationLockStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAppConversationLockStatus',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppConversationLockStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_conversation_lock_status(
        self,
        request: main_models.GetAppConversationLockStatusRequest,
    ) -> main_models.GetAppConversationLockStatusResponse:
        runtime = RuntimeOptions()
        return self.get_app_conversation_lock_status_with_options(request, runtime)

    async def get_app_conversation_lock_status_async(
        self,
        request: main_models.GetAppConversationLockStatusRequest,
    ) -> main_models.GetAppConversationLockStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_app_conversation_lock_status_with_options_async(request, runtime)

    def get_app_database_table_schemas_with_options(
        self,
        request: main_models.GetAppDatabaseTableSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppDatabaseTableSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppDatabaseTableSchemas',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppDatabaseTableSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_database_table_schemas_with_options_async(
        self,
        request: main_models.GetAppDatabaseTableSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppDatabaseTableSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppDatabaseTableSchemas',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppDatabaseTableSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_database_table_schemas(
        self,
        request: main_models.GetAppDatabaseTableSchemasRequest,
    ) -> main_models.GetAppDatabaseTableSchemasResponse:
        runtime = RuntimeOptions()
        return self.get_app_database_table_schemas_with_options(request, runtime)

    async def get_app_database_table_schemas_async(
        self,
        request: main_models.GetAppDatabaseTableSchemasRequest,
    ) -> main_models.GetAppDatabaseTableSchemasResponse:
        runtime = RuntimeOptions()
        return await self.get_app_database_table_schemas_with_options_async(request, runtime)

    def get_app_file_content_with_options(
        self,
        request: main_models.GetAppFileContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppFileContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppFileContent',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppFileContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_file_content_with_options_async(
        self,
        request: main_models.GetAppFileContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppFileContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppFileContent',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppFileContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_file_content(
        self,
        request: main_models.GetAppFileContentRequest,
    ) -> main_models.GetAppFileContentResponse:
        runtime = RuntimeOptions()
        return self.get_app_file_content_with_options(request, runtime)

    async def get_app_file_content_async(
        self,
        request: main_models.GetAppFileContentRequest,
    ) -> main_models.GetAppFileContentResponse:
        runtime = RuntimeOptions()
        return await self.get_app_file_content_with_options_async(request, runtime)

    def get_app_instance_with_options(
        self,
        request: main_models.GetAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_instance_with_options_async(
        self,
        request: main_models.GetAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_instance(
        self,
        request: main_models.GetAppInstanceRequest,
    ) -> main_models.GetAppInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_app_instance_with_options(request, runtime)

    async def get_app_instance_async(
        self,
        request: main_models.GetAppInstanceRequest,
    ) -> main_models.GetAppInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_app_instance_with_options_async(request, runtime)

    def get_app_instance_entitlement_with_options(
        self,
        request: main_models.GetAppInstanceEntitlementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceEntitlementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstanceEntitlement',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceEntitlementResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_instance_entitlement_with_options_async(
        self,
        request: main_models.GetAppInstanceEntitlementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceEntitlementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstanceEntitlement',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceEntitlementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_instance_entitlement(
        self,
        request: main_models.GetAppInstanceEntitlementRequest,
    ) -> main_models.GetAppInstanceEntitlementResponse:
        runtime = RuntimeOptions()
        return self.get_app_instance_entitlement_with_options(request, runtime)

    async def get_app_instance_entitlement_async(
        self,
        request: main_models.GetAppInstanceEntitlementRequest,
    ) -> main_models.GetAppInstanceEntitlementResponse:
        runtime = RuntimeOptions()
        return await self.get_app_instance_entitlement_with_options_async(request, runtime)

    def get_app_instance_for_admin_with_options(
        self,
        request: main_models.GetAppInstanceForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstanceForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceForAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_instance_for_admin_with_options_async(
        self,
        request: main_models.GetAppInstanceForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstanceForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceForAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_instance_for_admin(
        self,
        request: main_models.GetAppInstanceForAdminRequest,
    ) -> main_models.GetAppInstanceForAdminResponse:
        runtime = RuntimeOptions()
        return self.get_app_instance_for_admin_with_options(request, runtime)

    async def get_app_instance_for_admin_async(
        self,
        request: main_models.GetAppInstanceForAdminRequest,
    ) -> main_models.GetAppInstanceForAdminResponse:
        runtime = RuntimeOptions()
        return await self.get_app_instance_for_admin_with_options_async(request, runtime)

    def get_app_instance_for_partner_with_options(
        self,
        request: main_models.GetAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_instance_for_partner_with_options_async(
        self,
        request: main_models.GetAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_instance_for_partner(
        self,
        request: main_models.GetAppInstanceForPartnerRequest,
    ) -> main_models.GetAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return self.get_app_instance_for_partner_with_options(request, runtime)

    async def get_app_instance_for_partner_async(
        self,
        request: main_models.GetAppInstanceForPartnerRequest,
    ) -> main_models.GetAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.get_app_instance_for_partner_with_options_async(request, runtime)

    def get_app_instance_temp_short_url_with_options(
        self,
        request: main_models.GetAppInstanceTempShortUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceTempShortUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstanceTempShortUrl',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceTempShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_instance_temp_short_url_with_options_async(
        self,
        request: main_models.GetAppInstanceTempShortUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceTempShortUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstanceTempShortUrl',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceTempShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_instance_temp_short_url(
        self,
        request: main_models.GetAppInstanceTempShortUrlRequest,
    ) -> main_models.GetAppInstanceTempShortUrlResponse:
        runtime = RuntimeOptions()
        return self.get_app_instance_temp_short_url_with_options(request, runtime)

    async def get_app_instance_temp_short_url_async(
        self,
        request: main_models.GetAppInstanceTempShortUrlRequest,
    ) -> main_models.GetAppInstanceTempShortUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_app_instance_temp_short_url_with_options_async(request, runtime)

    def get_app_plugin_config_with_options(
        self,
        request: main_models.GetAppPluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppPluginConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.plugin_id):
            body['PluginId'] = request.plugin_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAppPluginConfig',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppPluginConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_plugin_config_with_options_async(
        self,
        request: main_models.GetAppPluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppPluginConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.plugin_id):
            body['PluginId'] = request.plugin_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAppPluginConfig',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppPluginConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_plugin_config(
        self,
        request: main_models.GetAppPluginConfigRequest,
    ) -> main_models.GetAppPluginConfigResponse:
        runtime = RuntimeOptions()
        return self.get_app_plugin_config_with_options(request, runtime)

    async def get_app_plugin_config_async(
        self,
        request: main_models.GetAppPluginConfigRequest,
    ) -> main_models.GetAppPluginConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_app_plugin_config_with_options_async(request, runtime)

    def get_app_publish_status_with_options(
        self,
        request: main_models.GetAppPublishStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppPublishStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.deploy_order_id):
            query['DeployOrderId'] = request.deploy_order_id
        if not DaraCore.is_null(request.website_domain):
            query['WebsiteDomain'] = request.website_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppPublishStatus',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppPublishStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_publish_status_with_options_async(
        self,
        request: main_models.GetAppPublishStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppPublishStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.deploy_order_id):
            query['DeployOrderId'] = request.deploy_order_id
        if not DaraCore.is_null(request.website_domain):
            query['WebsiteDomain'] = request.website_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppPublishStatus',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppPublishStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_publish_status(
        self,
        request: main_models.GetAppPublishStatusRequest,
    ) -> main_models.GetAppPublishStatusResponse:
        runtime = RuntimeOptions()
        return self.get_app_publish_status_with_options(request, runtime)

    async def get_app_publish_status_async(
        self,
        request: main_models.GetAppPublishStatusRequest,
    ) -> main_models.GetAppPublishStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_app_publish_status_with_options_async(request, runtime)

    def get_app_recommended_commodities_with_options(
        self,
        request: main_models.GetAppRecommendedCommoditiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppRecommendedCommoditiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.resource_conditions):
            query['ResourceConditions'] = request.resource_conditions
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppRecommendedCommodities',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppRecommendedCommoditiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_recommended_commodities_with_options_async(
        self,
        request: main_models.GetAppRecommendedCommoditiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppRecommendedCommoditiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.resource_conditions):
            query['ResourceConditions'] = request.resource_conditions
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppRecommendedCommodities',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppRecommendedCommoditiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_recommended_commodities(
        self,
        request: main_models.GetAppRecommendedCommoditiesRequest,
    ) -> main_models.GetAppRecommendedCommoditiesResponse:
        runtime = RuntimeOptions()
        return self.get_app_recommended_commodities_with_options(request, runtime)

    async def get_app_recommended_commodities_async(
        self,
        request: main_models.GetAppRecommendedCommoditiesRequest,
    ) -> main_models.GetAppRecommendedCommoditiesResponse:
        runtime = RuntimeOptions()
        return await self.get_app_recommended_commodities_with_options_async(request, runtime)

    def get_app_requirement_with_options(
        self,
        request: main_models.GetAppRequirementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppRequirementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppRequirement',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppRequirementResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_requirement_with_options_async(
        self,
        request: main_models.GetAppRequirementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppRequirementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppRequirement',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppRequirementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_requirement(
        self,
        request: main_models.GetAppRequirementRequest,
    ) -> main_models.GetAppRequirementResponse:
        runtime = RuntimeOptions()
        return self.get_app_requirement_with_options(request, runtime)

    async def get_app_requirement_async(
        self,
        request: main_models.GetAppRequirementRequest,
    ) -> main_models.GetAppRequirementResponse:
        runtime = RuntimeOptions()
        return await self.get_app_requirement_with_options_async(request, runtime)

    def get_app_sandbox_preview_url_with_options(
        self,
        request: main_models.GetAppSandboxPreviewUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSandboxPreviewUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.restart):
            body['Restart'] = request.restart
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSandboxPreviewUrl',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSandboxPreviewUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_sandbox_preview_url_with_options_async(
        self,
        request: main_models.GetAppSandboxPreviewUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSandboxPreviewUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.restart):
            body['Restart'] = request.restart
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSandboxPreviewUrl',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSandboxPreviewUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_sandbox_preview_url(
        self,
        request: main_models.GetAppSandboxPreviewUrlRequest,
    ) -> main_models.GetAppSandboxPreviewUrlResponse:
        runtime = RuntimeOptions()
        return self.get_app_sandbox_preview_url_with_options(request, runtime)

    async def get_app_sandbox_preview_url_async(
        self,
        request: main_models.GetAppSandboxPreviewUrlRequest,
    ) -> main_models.GetAppSandboxPreviewUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_app_sandbox_preview_url_with_options_async(request, runtime)

    def get_app_seo_status_with_options(
        self,
        request: main_models.GetAppSeoStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSeoStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.se_type):
            query['SeType'] = request.se_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSeoStatus',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSeoStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_seo_status_with_options_async(
        self,
        request: main_models.GetAppSeoStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSeoStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.se_type):
            query['SeType'] = request.se_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSeoStatus',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSeoStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_seo_status(
        self,
        request: main_models.GetAppSeoStatusRequest,
    ) -> main_models.GetAppSeoStatusResponse:
        runtime = RuntimeOptions()
        return self.get_app_seo_status_with_options(request, runtime)

    async def get_app_seo_status_async(
        self,
        request: main_models.GetAppSeoStatusRequest,
    ) -> main_models.GetAppSeoStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_app_seo_status_with_options_async(request, runtime)

    def get_app_seo_trends_with_options(
        self,
        request: main_models.GetAppSeoTrendsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSeoTrendsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.se_type):
            query['SeType'] = request.se_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSeoTrends',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSeoTrendsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_seo_trends_with_options_async(
        self,
        request: main_models.GetAppSeoTrendsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSeoTrendsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.se_type):
            query['SeType'] = request.se_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSeoTrends',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSeoTrendsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_seo_trends(
        self,
        request: main_models.GetAppSeoTrendsRequest,
    ) -> main_models.GetAppSeoTrendsResponse:
        runtime = RuntimeOptions()
        return self.get_app_seo_trends_with_options(request, runtime)

    async def get_app_seo_trends_async(
        self,
        request: main_models.GetAppSeoTrendsRequest,
    ) -> main_models.GetAppSeoTrendsResponse:
        runtime = RuntimeOptions()
        return await self.get_app_seo_trends_with_options_async(request, runtime)

    def get_app_sitemap_with_options(
        self,
        request: main_models.GetAppSitemapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSitemapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.se_type):
            query['SeType'] = request.se_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSitemap',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSitemapResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_sitemap_with_options_async(
        self,
        request: main_models.GetAppSitemapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSitemapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.se_type):
            query['SeType'] = request.se_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSitemap',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSitemapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_sitemap(
        self,
        request: main_models.GetAppSitemapRequest,
    ) -> main_models.GetAppSitemapResponse:
        runtime = RuntimeOptions()
        return self.get_app_sitemap_with_options(request, runtime)

    async def get_app_sitemap_async(
        self,
        request: main_models.GetAppSitemapRequest,
    ) -> main_models.GetAppSitemapResponse:
        runtime = RuntimeOptions()
        return await self.get_app_sitemap_with_options_async(request, runtime)

    def get_app_supabase_auth_config_with_options(
        self,
        request: main_models.GetAppSupabaseAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSupabaseAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSupabaseAuthConfig',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSupabaseAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_supabase_auth_config_with_options_async(
        self,
        request: main_models.GetAppSupabaseAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSupabaseAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSupabaseAuthConfig',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSupabaseAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_supabase_auth_config(
        self,
        request: main_models.GetAppSupabaseAuthConfigRequest,
    ) -> main_models.GetAppSupabaseAuthConfigResponse:
        runtime = RuntimeOptions()
        return self.get_app_supabase_auth_config_with_options(request, runtime)

    async def get_app_supabase_auth_config_async(
        self,
        request: main_models.GetAppSupabaseAuthConfigRequest,
    ) -> main_models.GetAppSupabaseAuthConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_app_supabase_auth_config_with_options_async(request, runtime)

    def get_app_supabase_instance_with_options(
        self,
        request: main_models.GetAppSupabaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSupabaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSupabaseInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSupabaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_supabase_instance_with_options_async(
        self,
        request: main_models.GetAppSupabaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSupabaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSupabaseInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSupabaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_supabase_instance(
        self,
        request: main_models.GetAppSupabaseInstanceRequest,
    ) -> main_models.GetAppSupabaseInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_app_supabase_instance_with_options(request, runtime)

    async def get_app_supabase_instance_async(
        self,
        request: main_models.GetAppSupabaseInstanceRequest,
    ) -> main_models.GetAppSupabaseInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_app_supabase_instance_with_options_async(request, runtime)

    def get_app_supabase_secrets_with_options(
        self,
        request: main_models.GetAppSupabaseSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSupabaseSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSupabaseSecrets',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSupabaseSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_supabase_secrets_with_options_async(
        self,
        request: main_models.GetAppSupabaseSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSupabaseSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSupabaseSecrets',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSupabaseSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_supabase_secrets(
        self,
        request: main_models.GetAppSupabaseSecretsRequest,
    ) -> main_models.GetAppSupabaseSecretsResponse:
        runtime = RuntimeOptions()
        return self.get_app_supabase_secrets_with_options(request, runtime)

    async def get_app_supabase_secrets_async(
        self,
        request: main_models.GetAppSupabaseSecretsRequest,
    ) -> main_models.GetAppSupabaseSecretsResponse:
        runtime = RuntimeOptions()
        return await self.get_app_supabase_secrets_with_options_async(request, runtime)

    def get_app_template_with_options(
        self,
        request: main_models.GetAppTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppTemplate',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_template_with_options_async(
        self,
        request: main_models.GetAppTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppTemplate',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_template(
        self,
        request: main_models.GetAppTemplateRequest,
    ) -> main_models.GetAppTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_app_template_with_options(request, runtime)

    async def get_app_template_async(
        self,
        request: main_models.GetAppTemplateRequest,
    ) -> main_models.GetAppTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_app_template_with_options_async(request, runtime)

    def get_app_token_service_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppTokenServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAppTokenService',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppTokenServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_token_service_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppTokenServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAppTokenService',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppTokenServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_token_service(self) -> main_models.GetAppTokenServiceResponse:
        runtime = RuntimeOptions()
        return self.get_app_token_service_with_options(runtime)

    async def get_app_token_service_async(self) -> main_models.GetAppTokenServiceResponse:
        runtime = RuntimeOptions()
        return await self.get_app_token_service_with_options_async(runtime)

    def get_app_workspace_directory_with_options(
        self,
        request: main_models.GetAppWorkspaceDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppWorkspaceDirectoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.deep):
            body['Deep'] = request.deep
        if not DaraCore.is_null(request.file_path):
            body['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAppWorkspaceDirectory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppWorkspaceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_workspace_directory_with_options_async(
        self,
        request: main_models.GetAppWorkspaceDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppWorkspaceDirectoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.deep):
            body['Deep'] = request.deep
        if not DaraCore.is_null(request.file_path):
            body['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAppWorkspaceDirectory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppWorkspaceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_workspace_directory(
        self,
        request: main_models.GetAppWorkspaceDirectoryRequest,
    ) -> main_models.GetAppWorkspaceDirectoryResponse:
        runtime = RuntimeOptions()
        return self.get_app_workspace_directory_with_options(request, runtime)

    async def get_app_workspace_directory_async(
        self,
        request: main_models.GetAppWorkspaceDirectoryRequest,
    ) -> main_models.GetAppWorkspaceDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.get_app_workspace_directory_with_options_async(request, runtime)

    def get_create_logo_task_with_options(
        self,
        request: main_models.GetCreateLogoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreateLogoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreateLogoTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreateLogoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_create_logo_task_with_options_async(
        self,
        request: main_models.GetCreateLogoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreateLogoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreateLogoTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreateLogoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_create_logo_task(
        self,
        request: main_models.GetCreateLogoTaskRequest,
    ) -> main_models.GetCreateLogoTaskResponse:
        runtime = RuntimeOptions()
        return self.get_create_logo_task_with_options(request, runtime)

    async def get_create_logo_task_async(
        self,
        request: main_models.GetCreateLogoTaskRequest,
    ) -> main_models.GetCreateLogoTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_create_logo_task_with_options_async(request, runtime)

    def get_domain_info_for_partner_with_options(
        self,
        request: main_models.GetDomainInfoForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainInfoForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomainInfoForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainInfoForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_info_for_partner_with_options_async(
        self,
        request: main_models.GetDomainInfoForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainInfoForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomainInfoForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainInfoForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_info_for_partner(
        self,
        request: main_models.GetDomainInfoForPartnerRequest,
    ) -> main_models.GetDomainInfoForPartnerResponse:
        runtime = RuntimeOptions()
        return self.get_domain_info_for_partner_with_options(request, runtime)

    async def get_domain_info_for_partner_async(
        self,
        request: main_models.GetDomainInfoForPartnerRequest,
    ) -> main_models.GetDomainInfoForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.get_domain_info_for_partner_with_options_async(request, runtime)

    def get_icp_filing_info_for_partner_with_options(
        self,
        request: main_models.GetIcpFilingInfoForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIcpFilingInfoForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIcpFilingInfoForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIcpFilingInfoForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_icp_filing_info_for_partner_with_options_async(
        self,
        request: main_models.GetIcpFilingInfoForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIcpFilingInfoForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIcpFilingInfoForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIcpFilingInfoForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_icp_filing_info_for_partner(
        self,
        request: main_models.GetIcpFilingInfoForPartnerRequest,
    ) -> main_models.GetIcpFilingInfoForPartnerResponse:
        runtime = RuntimeOptions()
        return self.get_icp_filing_info_for_partner_with_options(request, runtime)

    async def get_icp_filing_info_for_partner_async(
        self,
        request: main_models.GetIcpFilingInfoForPartnerRequest,
    ) -> main_models.GetIcpFilingInfoForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.get_icp_filing_info_for_partner_with_options_async(request, runtime)

    def get_llm_proxy_config_for_admin_with_options(
        self,
        request: main_models.GetLlmProxyConfigForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLlmProxyConfigForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.capability):
            query['Capability'] = request.capability
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLlmProxyConfigForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLlmProxyConfigForAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_llm_proxy_config_for_admin_with_options_async(
        self,
        request: main_models.GetLlmProxyConfigForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLlmProxyConfigForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.capability):
            query['Capability'] = request.capability
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLlmProxyConfigForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLlmProxyConfigForAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_llm_proxy_config_for_admin(
        self,
        request: main_models.GetLlmProxyConfigForAdminRequest,
    ) -> main_models.GetLlmProxyConfigForAdminResponse:
        runtime = RuntimeOptions()
        return self.get_llm_proxy_config_for_admin_with_options(request, runtime)

    async def get_llm_proxy_config_for_admin_async(
        self,
        request: main_models.GetLlmProxyConfigForAdminRequest,
    ) -> main_models.GetLlmProxyConfigForAdminResponse:
        runtime = RuntimeOptions()
        return await self.get_llm_proxy_config_for_admin_with_options_async(request, runtime)

    def get_mini_app_auth_url_with_options(
        self,
        request: main_models.GetMiniAppAuthUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMiniAppAuthUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.redirect_uri):
            query['RedirectUri'] = request.redirect_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMiniAppAuthUrl',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMiniAppAuthUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mini_app_auth_url_with_options_async(
        self,
        request: main_models.GetMiniAppAuthUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMiniAppAuthUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.redirect_uri):
            query['RedirectUri'] = request.redirect_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMiniAppAuthUrl',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMiniAppAuthUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mini_app_auth_url(
        self,
        request: main_models.GetMiniAppAuthUrlRequest,
    ) -> main_models.GetMiniAppAuthUrlResponse:
        runtime = RuntimeOptions()
        return self.get_mini_app_auth_url_with_options(request, runtime)

    async def get_mini_app_auth_url_async(
        self,
        request: main_models.GetMiniAppAuthUrlRequest,
    ) -> main_models.GetMiniAppAuthUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_mini_app_auth_url_with_options_async(request, runtime)

    def get_mini_app_binding_with_options(
        self,
        tmp_req: main_models.GetMiniAppBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMiniAppBindingResponse:
        tmp_req.validate()
        request = main_models.GetMiniAppBindingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.setting_keys):
            request.setting_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.setting_keys, 'SettingKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.setting_keys_shrink):
            query['SettingKeys'] = request.setting_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMiniAppBinding',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMiniAppBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mini_app_binding_with_options_async(
        self,
        tmp_req: main_models.GetMiniAppBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMiniAppBindingResponse:
        tmp_req.validate()
        request = main_models.GetMiniAppBindingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.setting_keys):
            request.setting_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.setting_keys, 'SettingKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.setting_keys_shrink):
            query['SettingKeys'] = request.setting_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMiniAppBinding',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMiniAppBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mini_app_binding(
        self,
        request: main_models.GetMiniAppBindingRequest,
    ) -> main_models.GetMiniAppBindingResponse:
        runtime = RuntimeOptions()
        return self.get_mini_app_binding_with_options(request, runtime)

    async def get_mini_app_binding_async(
        self,
        request: main_models.GetMiniAppBindingRequest,
    ) -> main_models.GetMiniAppBindingResponse:
        runtime = RuntimeOptions()
        return await self.get_mini_app_binding_with_options_async(request, runtime)

    def get_mini_app_binding_for_admin_with_options(
        self,
        request: main_models.GetMiniAppBindingForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMiniAppBindingForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.platform_appid):
            query['PlatformAppid'] = request.platform_appid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMiniAppBindingForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMiniAppBindingForAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mini_app_binding_for_admin_with_options_async(
        self,
        request: main_models.GetMiniAppBindingForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMiniAppBindingForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.platform_appid):
            query['PlatformAppid'] = request.platform_appid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMiniAppBindingForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMiniAppBindingForAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mini_app_binding_for_admin(
        self,
        request: main_models.GetMiniAppBindingForAdminRequest,
    ) -> main_models.GetMiniAppBindingForAdminResponse:
        runtime = RuntimeOptions()
        return self.get_mini_app_binding_for_admin_with_options(request, runtime)

    async def get_mini_app_binding_for_admin_async(
        self,
        request: main_models.GetMiniAppBindingForAdminRequest,
    ) -> main_models.GetMiniAppBindingForAdminResponse:
        runtime = RuntimeOptions()
        return await self.get_mini_app_binding_for_admin_with_options_async(request, runtime)

    def get_user_access_token_for_partner_with_options(
        self,
        request: main_models.GetUserAccessTokenForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAccessTokenForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.site_host):
            query['SiteHost'] = request.site_host
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserAccessTokenForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAccessTokenForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_access_token_for_partner_with_options_async(
        self,
        request: main_models.GetUserAccessTokenForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAccessTokenForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.site_host):
            query['SiteHost'] = request.site_host
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserAccessTokenForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAccessTokenForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_access_token_for_partner(
        self,
        request: main_models.GetUserAccessTokenForPartnerRequest,
    ) -> main_models.GetUserAccessTokenForPartnerResponse:
        runtime = RuntimeOptions()
        return self.get_user_access_token_for_partner_with_options(request, runtime)

    async def get_user_access_token_for_partner_async(
        self,
        request: main_models.GetUserAccessTokenForPartnerRequest,
    ) -> main_models.GetUserAccessTokenForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.get_user_access_token_for_partner_with_options_async(request, runtime)

    def get_user_tmp_identity_for_partner_with_options(
        self,
        request: main_models.GetUserTmpIdentityForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserTmpIdentityForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_purpose):
            query['AuthPurpose'] = request.auth_purpose
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserTmpIdentityForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserTmpIdentityForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_tmp_identity_for_partner_with_options_async(
        self,
        request: main_models.GetUserTmpIdentityForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserTmpIdentityForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_purpose):
            query['AuthPurpose'] = request.auth_purpose
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserTmpIdentityForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserTmpIdentityForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_tmp_identity_for_partner(
        self,
        request: main_models.GetUserTmpIdentityForPartnerRequest,
    ) -> main_models.GetUserTmpIdentityForPartnerResponse:
        runtime = RuntimeOptions()
        return self.get_user_tmp_identity_for_partner_with_options(request, runtime)

    async def get_user_tmp_identity_for_partner_async(
        self,
        request: main_models.GetUserTmpIdentityForPartnerRequest,
    ) -> main_models.GetUserTmpIdentityForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.get_user_tmp_identity_for_partner_with_options_async(request, runtime)

    def introspect_app_instance_ticket_for_preview_with_options(
        self,
        request: main_models.IntrospectAppInstanceTicketForPreviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IntrospectAppInstanceTicketForPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IntrospectAppInstanceTicketForPreview',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IntrospectAppInstanceTicketForPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def introspect_app_instance_ticket_for_preview_with_options_async(
        self,
        request: main_models.IntrospectAppInstanceTicketForPreviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IntrospectAppInstanceTicketForPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IntrospectAppInstanceTicketForPreview',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IntrospectAppInstanceTicketForPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def introspect_app_instance_ticket_for_preview(
        self,
        request: main_models.IntrospectAppInstanceTicketForPreviewRequest,
    ) -> main_models.IntrospectAppInstanceTicketForPreviewResponse:
        runtime = RuntimeOptions()
        return self.introspect_app_instance_ticket_for_preview_with_options(request, runtime)

    async def introspect_app_instance_ticket_for_preview_async(
        self,
        request: main_models.IntrospectAppInstanceTicketForPreviewRequest,
    ) -> main_models.IntrospectAppInstanceTicketForPreviewResponse:
        runtime = RuntimeOptions()
        return await self.introspect_app_instance_ticket_for_preview_with_options_async(request, runtime)

    def list_aistaff_chat_events_with_options(
        self,
        request: main_models.ListAIStaffChatEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAIStaffChatEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        body = {}
        if not DaraCore.is_null(request.chat_id):
            body['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.last_event_id):
            body['LastEventId'] = request.last_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAIStaffChatEvents',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAIStaffChatEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aistaff_chat_events_with_options_async(
        self,
        request: main_models.ListAIStaffChatEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAIStaffChatEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        body = {}
        if not DaraCore.is_null(request.chat_id):
            body['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.last_event_id):
            body['LastEventId'] = request.last_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAIStaffChatEvents',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAIStaffChatEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aistaff_chat_events(
        self,
        request: main_models.ListAIStaffChatEventsRequest,
    ) -> main_models.ListAIStaffChatEventsResponse:
        runtime = RuntimeOptions()
        return self.list_aistaff_chat_events_with_options(request, runtime)

    async def list_aistaff_chat_events_async(
        self,
        request: main_models.ListAIStaffChatEventsRequest,
    ) -> main_models.ListAIStaffChatEventsResponse:
        runtime = RuntimeOptions()
        return await self.list_aistaff_chat_events_with_options_async(request, runtime)

    def list_aistaff_chat_messages_with_options(
        self,
        request: main_models.ListAIStaffChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAIStaffChatMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        body = {}
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_create_time):
            body['StartCreateTime'] = request.start_create_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAIStaffChatMessages',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAIStaffChatMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aistaff_chat_messages_with_options_async(
        self,
        request: main_models.ListAIStaffChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAIStaffChatMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        body = {}
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_create_time):
            body['StartCreateTime'] = request.start_create_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAIStaffChatMessages',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAIStaffChatMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aistaff_chat_messages(
        self,
        request: main_models.ListAIStaffChatMessagesRequest,
    ) -> main_models.ListAIStaffChatMessagesResponse:
        runtime = RuntimeOptions()
        return self.list_aistaff_chat_messages_with_options(request, runtime)

    async def list_aistaff_chat_messages_async(
        self,
        request: main_models.ListAIStaffChatMessagesRequest,
    ) -> main_models.ListAIStaffChatMessagesResponse:
        runtime = RuntimeOptions()
        return await self.list_aistaff_chat_messages_with_options_async(request, runtime)

    def list_app_assistant_agents_with_options(
        self,
        request: main_models.ListAppAssistantAgentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppAssistantAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.platform_type):
            query['PlatformType'] = request.platform_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppAssistantAgents',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppAssistantAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_assistant_agents_with_options_async(
        self,
        request: main_models.ListAppAssistantAgentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppAssistantAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.platform_type):
            query['PlatformType'] = request.platform_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppAssistantAgents',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppAssistantAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_assistant_agents(
        self,
        request: main_models.ListAppAssistantAgentsRequest,
    ) -> main_models.ListAppAssistantAgentsResponse:
        runtime = RuntimeOptions()
        return self.list_app_assistant_agents_with_options(request, runtime)

    async def list_app_assistant_agents_async(
        self,
        request: main_models.ListAppAssistantAgentsRequest,
    ) -> main_models.ListAppAssistantAgentsResponse:
        runtime = RuntimeOptions()
        return await self.list_app_assistant_agents_with_options_async(request, runtime)

    def list_app_chat_messages_with_options(
        self,
        request: main_models.ListAppChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppChatMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chat_id):
            query['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.section_id):
            query['SectionId'] = request.section_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppChatMessages',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppChatMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_chat_messages_with_options_async(
        self,
        request: main_models.ListAppChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppChatMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chat_id):
            query['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.section_id):
            query['SectionId'] = request.section_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppChatMessages',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppChatMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_chat_messages(
        self,
        request: main_models.ListAppChatMessagesRequest,
    ) -> main_models.ListAppChatMessagesResponse:
        runtime = RuntimeOptions()
        return self.list_app_chat_messages_with_options(request, runtime)

    async def list_app_chat_messages_async(
        self,
        request: main_models.ListAppChatMessagesRequest,
    ) -> main_models.ListAppChatMessagesResponse:
        runtime = RuntimeOptions()
        return await self.list_app_chat_messages_with_options_async(request, runtime)

    def list_app_commodity_specifications_for_partner_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppCommoditySpecificationsForPartnerResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListAppCommoditySpecificationsForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppCommoditySpecificationsForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_commodity_specifications_for_partner_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppCommoditySpecificationsForPartnerResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListAppCommoditySpecificationsForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppCommoditySpecificationsForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_commodity_specifications_for_partner(self) -> main_models.ListAppCommoditySpecificationsForPartnerResponse:
        runtime = RuntimeOptions()
        return self.list_app_commodity_specifications_for_partner_with_options(runtime)

    async def list_app_commodity_specifications_for_partner_async(self) -> main_models.ListAppCommoditySpecificationsForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.list_app_commodity_specifications_for_partner_with_options_async(runtime)

    def list_app_commodity_specifications_v2for_partner_with_options(
        self,
        request: main_models.ListAppCommoditySpecificationsV2ForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppCommoditySpecificationsV2ForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppCommoditySpecificationsV2ForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppCommoditySpecificationsV2ForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_commodity_specifications_v2for_partner_with_options_async(
        self,
        request: main_models.ListAppCommoditySpecificationsV2ForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppCommoditySpecificationsV2ForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppCommoditySpecificationsV2ForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppCommoditySpecificationsV2ForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_commodity_specifications_v2for_partner(
        self,
        request: main_models.ListAppCommoditySpecificationsV2ForPartnerRequest,
    ) -> main_models.ListAppCommoditySpecificationsV2ForPartnerResponse:
        runtime = RuntimeOptions()
        return self.list_app_commodity_specifications_v2for_partner_with_options(request, runtime)

    async def list_app_commodity_specifications_v2for_partner_async(
        self,
        request: main_models.ListAppCommoditySpecificationsV2ForPartnerRequest,
    ) -> main_models.ListAppCommoditySpecificationsV2ForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.list_app_commodity_specifications_v2for_partner_with_options_async(request, runtime)

    def list_app_conversation_messages_with_options(
        self,
        request: main_models.ListAppConversationMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppConversationMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        if not DaraCore.is_null(request.start_create_time):
            query['StartCreateTime'] = request.start_create_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppConversationMessages',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppConversationMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_conversation_messages_with_options_async(
        self,
        request: main_models.ListAppConversationMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppConversationMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        if not DaraCore.is_null(request.start_create_time):
            query['StartCreateTime'] = request.start_create_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppConversationMessages',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppConversationMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_conversation_messages(
        self,
        request: main_models.ListAppConversationMessagesRequest,
    ) -> main_models.ListAppConversationMessagesResponse:
        runtime = RuntimeOptions()
        return self.list_app_conversation_messages_with_options(request, runtime)

    async def list_app_conversation_messages_async(
        self,
        request: main_models.ListAppConversationMessagesRequest,
    ) -> main_models.ListAppConversationMessagesResponse:
        runtime = RuntimeOptions()
        return await self.list_app_conversation_messages_with_options_async(request, runtime)

    def list_app_conversations_with_options(
        self,
        request: main_models.ListAppConversationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppConversationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.end_modify_time):
            query['EndModifyTime'] = request.end_modify_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        if not DaraCore.is_null(request.start_modify_time):
            query['StartModifyTime'] = request.start_modify_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppConversations',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppConversationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_conversations_with_options_async(
        self,
        request: main_models.ListAppConversationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppConversationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.end_modify_time):
            query['EndModifyTime'] = request.end_modify_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        if not DaraCore.is_null(request.start_modify_time):
            query['StartModifyTime'] = request.start_modify_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppConversations',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppConversationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_conversations(
        self,
        request: main_models.ListAppConversationsRequest,
    ) -> main_models.ListAppConversationsResponse:
        runtime = RuntimeOptions()
        return self.list_app_conversations_with_options(request, runtime)

    async def list_app_conversations_async(
        self,
        request: main_models.ListAppConversationsRequest,
    ) -> main_models.ListAppConversationsResponse:
        runtime = RuntimeOptions()
        return await self.list_app_conversations_with_options_async(request, runtime)

    def list_app_domain_redirect_records_with_options(
        self,
        request: main_models.ListAppDomainRedirectRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppDomainRedirectRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppDomainRedirectRecords',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppDomainRedirectRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_domain_redirect_records_with_options_async(
        self,
        request: main_models.ListAppDomainRedirectRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppDomainRedirectRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppDomainRedirectRecords',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppDomainRedirectRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_domain_redirect_records(
        self,
        request: main_models.ListAppDomainRedirectRecordsRequest,
    ) -> main_models.ListAppDomainRedirectRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_app_domain_redirect_records_with_options(request, runtime)

    async def list_app_domain_redirect_records_async(
        self,
        request: main_models.ListAppDomainRedirectRecordsRequest,
    ) -> main_models.ListAppDomainRedirectRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_app_domain_redirect_records_with_options_async(request, runtime)

    def list_app_instance_domains_with_options(
        self,
        request: main_models.ListAppInstanceDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstanceDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_keyword):
            query['DomainKeyword'] = request.domain_keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstanceDomains',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_instance_domains_with_options_async(
        self,
        request: main_models.ListAppInstanceDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstanceDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_keyword):
            query['DomainKeyword'] = request.domain_keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstanceDomains',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstanceDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_instance_domains(
        self,
        request: main_models.ListAppInstanceDomainsRequest,
    ) -> main_models.ListAppInstanceDomainsResponse:
        runtime = RuntimeOptions()
        return self.list_app_instance_domains_with_options(request, runtime)

    async def list_app_instance_domains_async(
        self,
        request: main_models.ListAppInstanceDomainsRequest,
    ) -> main_models.ListAppInstanceDomainsResponse:
        runtime = RuntimeOptions()
        return await self.list_app_instance_domains_with_options_async(request, runtime)

    def list_app_instances_with_options(
        self,
        tmp_req: main_models.ListAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstancesResponse:
        tmp_req.validate()
        request = main_models.ListAppInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.end_time_begin):
            query['EndTimeBegin'] = request.end_time_begin
        if not DaraCore.is_null(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstances',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_instances_with_options_async(
        self,
        tmp_req: main_models.ListAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstancesResponse:
        tmp_req.validate()
        request = main_models.ListAppInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.end_time_begin):
            query['EndTimeBegin'] = request.end_time_begin
        if not DaraCore.is_null(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstances',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_instances(
        self,
        request: main_models.ListAppInstancesRequest,
    ) -> main_models.ListAppInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_app_instances_with_options(request, runtime)

    async def list_app_instances_async(
        self,
        request: main_models.ListAppInstancesRequest,
    ) -> main_models.ListAppInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_app_instances_with_options_async(request, runtime)

    def list_app_plugin_configs_with_options(
        self,
        request: main_models.ListAppPluginConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppPluginConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppPluginConfigs',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppPluginConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_plugin_configs_with_options_async(
        self,
        request: main_models.ListAppPluginConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppPluginConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppPluginConfigs',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppPluginConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_plugin_configs(
        self,
        request: main_models.ListAppPluginConfigsRequest,
    ) -> main_models.ListAppPluginConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_app_plugin_configs_with_options(request, runtime)

    async def list_app_plugin_configs_async(
        self,
        request: main_models.ListAppPluginConfigsRequest,
    ) -> main_models.ListAppPluginConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_app_plugin_configs_with_options_async(request, runtime)

    def list_app_plugins_with_options(
        self,
        request: main_models.ListAppPluginsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.phase):
            query['Phase'] = request.phase
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppPlugins',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_plugins_with_options_async(
        self,
        request: main_models.ListAppPluginsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.phase):
            query['Phase'] = request.phase
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppPlugins',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppPluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_plugins(
        self,
        request: main_models.ListAppPluginsRequest,
    ) -> main_models.ListAppPluginsResponse:
        runtime = RuntimeOptions()
        return self.list_app_plugins_with_options(request, runtime)

    async def list_app_plugins_async(
        self,
        request: main_models.ListAppPluginsRequest,
    ) -> main_models.ListAppPluginsResponse:
        runtime = RuntimeOptions()
        return await self.list_app_plugins_with_options_async(request, runtime)

    def list_app_publish_history_with_options(
        self,
        request: main_models.ListAppPublishHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppPublishHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.website_domain):
            query['WebsiteDomain'] = request.website_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppPublishHistory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppPublishHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_publish_history_with_options_async(
        self,
        request: main_models.ListAppPublishHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppPublishHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.website_domain):
            query['WebsiteDomain'] = request.website_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppPublishHistory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppPublishHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_publish_history(
        self,
        request: main_models.ListAppPublishHistoryRequest,
    ) -> main_models.ListAppPublishHistoryResponse:
        runtime = RuntimeOptions()
        return self.list_app_publish_history_with_options(request, runtime)

    async def list_app_publish_history_async(
        self,
        request: main_models.ListAppPublishHistoryRequest,
    ) -> main_models.ListAppPublishHistoryResponse:
        runtime = RuntimeOptions()
        return await self.list_app_publish_history_with_options_async(request, runtime)

    def list_app_template_dicts_with_options(
        self,
        request: main_models.ListAppTemplateDictsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppTemplateDictsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dict_type):
            query['DictType'] = request.dict_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppTemplateDicts',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppTemplateDictsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_template_dicts_with_options_async(
        self,
        request: main_models.ListAppTemplateDictsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppTemplateDictsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dict_type):
            query['DictType'] = request.dict_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppTemplateDicts',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppTemplateDictsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_template_dicts(
        self,
        request: main_models.ListAppTemplateDictsRequest,
    ) -> main_models.ListAppTemplateDictsResponse:
        runtime = RuntimeOptions()
        return self.list_app_template_dicts_with_options(request, runtime)

    async def list_app_template_dicts_async(
        self,
        request: main_models.ListAppTemplateDictsRequest,
    ) -> main_models.ListAppTemplateDictsResponse:
        runtime = RuntimeOptions()
        return await self.list_app_template_dicts_with_options_async(request, runtime)

    def list_app_templates_with_options(
        self,
        request: main_models.ListAppTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.color_scheme):
            query['ColorScheme'] = request.color_scheme
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_version):
            query['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppTemplates',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_templates_with_options_async(
        self,
        request: main_models.ListAppTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.color_scheme):
            query['ColorScheme'] = request.color_scheme
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_version):
            query['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppTemplates',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_templates(
        self,
        request: main_models.ListAppTemplatesRequest,
    ) -> main_models.ListAppTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_app_templates_with_options(request, runtime)

    async def list_app_templates_async(
        self,
        request: main_models.ListAppTemplatesRequest,
    ) -> main_models.ListAppTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_app_templates_with_options_async(request, runtime)

    def list_isv_payment_plugin_configs_with_options(
        self,
        request: main_models.ListIsvPaymentPluginConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIsvPaymentPluginConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIsvPaymentPluginConfigs',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIsvPaymentPluginConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_isv_payment_plugin_configs_with_options_async(
        self,
        request: main_models.ListIsvPaymentPluginConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIsvPaymentPluginConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIsvPaymentPluginConfigs',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIsvPaymentPluginConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_isv_payment_plugin_configs(
        self,
        request: main_models.ListIsvPaymentPluginConfigsRequest,
    ) -> main_models.ListIsvPaymentPluginConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_isv_payment_plugin_configs_with_options(request, runtime)

    async def list_isv_payment_plugin_configs_async(
        self,
        request: main_models.ListIsvPaymentPluginConfigsRequest,
    ) -> main_models.ListIsvPaymentPluginConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_isv_payment_plugin_configs_with_options_async(request, runtime)

    def modify_app_instance_spec_with_options(
        self,
        request: main_models.ModifyAppInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppInstanceSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deploy_area):
            query['DeployArea'] = request.deploy_area
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppInstanceSpec',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_instance_spec_with_options_async(
        self,
        request: main_models.ModifyAppInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppInstanceSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deploy_area):
            query['DeployArea'] = request.deploy_area
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppInstanceSpec',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_instance_spec(
        self,
        request: main_models.ModifyAppInstanceSpecRequest,
    ) -> main_models.ModifyAppInstanceSpecResponse:
        runtime = RuntimeOptions()
        return self.modify_app_instance_spec_with_options(request, runtime)

    async def modify_app_instance_spec_async(
        self,
        request: main_models.ModifyAppInstanceSpecRequest,
    ) -> main_models.ModifyAppInstanceSpecResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_instance_spec_with_options_async(request, runtime)

    def modify_material_directory_with_options(
        self,
        request: main_models.ModifyMaterialDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaterialDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaterialDirectory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaterialDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_material_directory_with_options_async(
        self,
        request: main_models.ModifyMaterialDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaterialDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaterialDirectory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaterialDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_material_directory(
        self,
        request: main_models.ModifyMaterialDirectoryRequest,
    ) -> main_models.ModifyMaterialDirectoryResponse:
        runtime = RuntimeOptions()
        return self.modify_material_directory_with_options(request, runtime)

    async def modify_material_directory_async(
        self,
        request: main_models.ModifyMaterialDirectoryRequest,
    ) -> main_models.ModifyMaterialDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.modify_material_directory_with_options_async(request, runtime)

    def modify_material_file_with_options(
        self,
        request: main_models.ModifyMaterialFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaterialFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaterialFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaterialFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_material_file_with_options_async(
        self,
        request: main_models.ModifyMaterialFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaterialFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaterialFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaterialFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_material_file(
        self,
        request: main_models.ModifyMaterialFileRequest,
    ) -> main_models.ModifyMaterialFileResponse:
        runtime = RuntimeOptions()
        return self.modify_material_file_with_options(request, runtime)

    async def modify_material_file_async(
        self,
        request: main_models.ModifyMaterialFileRequest,
    ) -> main_models.ModifyMaterialFileResponse:
        runtime = RuntimeOptions()
        return await self.modify_material_file_with_options_async(request, runtime)

    def modify_material_file_status_with_options(
        self,
        tmp_req: main_models.ModifyMaterialFileStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaterialFileStatusResponse:
        tmp_req.validate()
        request = main_models.ModifyMaterialFileStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_ids):
            request.file_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_ids, 'FileIds', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.file_ids_shrink):
            query['FileIds'] = request.file_ids_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaterialFileStatus',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaterialFileStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_material_file_status_with_options_async(
        self,
        tmp_req: main_models.ModifyMaterialFileStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaterialFileStatusResponse:
        tmp_req.validate()
        request = main_models.ModifyMaterialFileStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_ids):
            request.file_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_ids, 'FileIds', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.file_ids_shrink):
            query['FileIds'] = request.file_ids_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaterialFileStatus',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaterialFileStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_material_file_status(
        self,
        request: main_models.ModifyMaterialFileStatusRequest,
    ) -> main_models.ModifyMaterialFileStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_material_file_status_with_options(request, runtime)

    async def modify_material_file_status_async(
        self,
        request: main_models.ModifyMaterialFileStatusRequest,
    ) -> main_models.ModifyMaterialFileStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_material_file_status_with_options_async(request, runtime)

    def move_material_directory_with_options(
        self,
        request: main_models.MoveMaterialDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveMaterialDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.parent_directory_id):
            query['ParentDirectoryId'] = request.parent_directory_id
        if not DaraCore.is_null(request.sort_num):
            query['SortNum'] = request.sort_num
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveMaterialDirectory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveMaterialDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_material_directory_with_options_async(
        self,
        request: main_models.MoveMaterialDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveMaterialDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.parent_directory_id):
            query['ParentDirectoryId'] = request.parent_directory_id
        if not DaraCore.is_null(request.sort_num):
            query['SortNum'] = request.sort_num
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveMaterialDirectory',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveMaterialDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_material_directory(
        self,
        request: main_models.MoveMaterialDirectoryRequest,
    ) -> main_models.MoveMaterialDirectoryResponse:
        runtime = RuntimeOptions()
        return self.move_material_directory_with_options(request, runtime)

    async def move_material_directory_async(
        self,
        request: main_models.MoveMaterialDirectoryRequest,
    ) -> main_models.MoveMaterialDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.move_material_directory_with_options_async(request, runtime)

    def move_material_file_with_options(
        self,
        tmp_req: main_models.MoveMaterialFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveMaterialFileResponse:
        tmp_req.validate()
        request = main_models.MoveMaterialFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_ids):
            request.file_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_ids, 'FileIds', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_ids_shrink):
            query['FileIds'] = request.file_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveMaterialFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveMaterialFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_material_file_with_options_async(
        self,
        tmp_req: main_models.MoveMaterialFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveMaterialFileResponse:
        tmp_req.validate()
        request = main_models.MoveMaterialFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_ids):
            request.file_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_ids, 'FileIds', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_ids_shrink):
            query['FileIds'] = request.file_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveMaterialFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveMaterialFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_material_file(
        self,
        request: main_models.MoveMaterialFileRequest,
    ) -> main_models.MoveMaterialFileResponse:
        runtime = RuntimeOptions()
        return self.move_material_file_with_options(request, runtime)

    async def move_material_file_async(
        self,
        request: main_models.MoveMaterialFileRequest,
    ) -> main_models.MoveMaterialFileResponse:
        runtime = RuntimeOptions()
        return await self.move_material_file_with_options_async(request, runtime)

    def operate_app_instance_for_partner_with_options(
        self,
        request: main_models.OperateAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppInstanceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_event):
            query['OperateEvent'] = request.operate_event
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppInstanceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_app_instance_for_partner_with_options_async(
        self,
        request: main_models.OperateAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppInstanceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_event):
            query['OperateEvent'] = request.operate_event
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppInstanceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_app_instance_for_partner(
        self,
        request: main_models.OperateAppInstanceForPartnerRequest,
    ) -> main_models.OperateAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return self.operate_app_instance_for_partner_with_options(request, runtime)

    async def operate_app_instance_for_partner_async(
        self,
        request: main_models.OperateAppInstanceForPartnerRequest,
    ) -> main_models.OperateAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.operate_app_instance_for_partner_with_options_async(request, runtime)

    def operate_app_service_for_partner_with_options(
        self,
        request: main_models.OperateAppServiceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppServiceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_event):
            query['OperateEvent'] = request.operate_event
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAppServiceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppServiceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_app_service_for_partner_with_options_async(
        self,
        request: main_models.OperateAppServiceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppServiceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_event):
            query['OperateEvent'] = request.operate_event
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAppServiceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppServiceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_app_service_for_partner(
        self,
        request: main_models.OperateAppServiceForPartnerRequest,
    ) -> main_models.OperateAppServiceForPartnerResponse:
        runtime = RuntimeOptions()
        return self.operate_app_service_for_partner_with_options(request, runtime)

    async def operate_app_service_for_partner_async(
        self,
        request: main_models.OperateAppServiceForPartnerRequest,
    ) -> main_models.OperateAppServiceForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.operate_app_service_for_partner_with_options_async(request, runtime)

    def operate_app_template_like_with_options(
        self,
        request: main_models.OperateAppTemplateLikeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppTemplateLikeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.liked):
            query['Liked'] = request.liked
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAppTemplateLike',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppTemplateLikeResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_app_template_like_with_options_async(
        self,
        request: main_models.OperateAppTemplateLikeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppTemplateLikeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.liked):
            query['Liked'] = request.liked
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAppTemplateLike',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppTemplateLikeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_app_template_like(
        self,
        request: main_models.OperateAppTemplateLikeRequest,
    ) -> main_models.OperateAppTemplateLikeResponse:
        runtime = RuntimeOptions()
        return self.operate_app_template_like_with_options(request, runtime)

    async def operate_app_template_like_async(
        self,
        request: main_models.OperateAppTemplateLikeRequest,
    ) -> main_models.OperateAppTemplateLikeResponse:
        runtime = RuntimeOptions()
        return await self.operate_app_template_like_with_options_async(request, runtime)

    def operate_supabase_for_admin_with_options(
        self,
        request: main_models.OperateSupabaseForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateSupabaseForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.execute_sql):
            query['ExecuteSql'] = request.execute_sql
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.order_by_clause):
            query['OrderByClause'] = request.order_by_clause
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.where_clause):
            query['WhereClause'] = request.where_clause
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateSupabaseForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateSupabaseForAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_supabase_for_admin_with_options_async(
        self,
        request: main_models.OperateSupabaseForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateSupabaseForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.execute_sql):
            query['ExecuteSql'] = request.execute_sql
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.order_by_clause):
            query['OrderByClause'] = request.order_by_clause
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.where_clause):
            query['WhereClause'] = request.where_clause
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateSupabaseForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateSupabaseForAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_supabase_for_admin(
        self,
        request: main_models.OperateSupabaseForAdminRequest,
    ) -> main_models.OperateSupabaseForAdminResponse:
        runtime = RuntimeOptions()
        return self.operate_supabase_for_admin_with_options(request, runtime)

    async def operate_supabase_for_admin_async(
        self,
        request: main_models.OperateSupabaseForAdminRequest,
    ) -> main_models.OperateSupabaseForAdminResponse:
        runtime = RuntimeOptions()
        return await self.operate_supabase_for_admin_with_options_async(request, runtime)

    def publish_app_instance_with_options(
        self,
        request: main_models.PublishAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.deploy_channel):
            query['DeployChannel'] = request.deploy_channel
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.logical_number):
            query['LogicalNumber'] = request.logical_number
        if not DaraCore.is_null(request.publish_number):
            query['PublishNumber'] = request.publish_number
        if not DaraCore.is_null(request.weapp_action):
            query['WeappAction'] = request.weapp_action
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_app_instance_with_options_async(
        self,
        request: main_models.PublishAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.deploy_channel):
            query['DeployChannel'] = request.deploy_channel
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.logical_number):
            query['LogicalNumber'] = request.logical_number
        if not DaraCore.is_null(request.publish_number):
            query['PublishNumber'] = request.publish_number
        if not DaraCore.is_null(request.weapp_action):
            query['WeappAction'] = request.weapp_action
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_app_instance(
        self,
        request: main_models.PublishAppInstanceRequest,
    ) -> main_models.PublishAppInstanceResponse:
        runtime = RuntimeOptions()
        return self.publish_app_instance_with_options(request, runtime)

    async def publish_app_instance_async(
        self,
        request: main_models.PublishAppInstanceRequest,
    ) -> main_models.PublishAppInstanceResponse:
        runtime = RuntimeOptions()
        return await self.publish_app_instance_with_options_async(request, runtime)

    def push_resource_measure_with_options(
        self,
        request: main_models.PushResourceMeasureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushResourceMeasureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.belong_id):
            query['BelongId'] = request.belong_id
        if not DaraCore.is_null(request.belong_id_type):
            query['BelongIdType'] = request.belong_id_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.measure_data):
            query['MeasureData'] = request.measure_data
        if not DaraCore.is_null(request.meta_data):
            query['MetaData'] = request.meta_data
        if not DaraCore.is_null(request.resource_code):
            query['ResourceCode'] = request.resource_code
        if not DaraCore.is_null(request.use_time):
            query['UseTime'] = request.use_time
        if not DaraCore.is_null(request.use_type):
            query['UseType'] = request.use_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushResourceMeasure',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushResourceMeasureResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_resource_measure_with_options_async(
        self,
        request: main_models.PushResourceMeasureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushResourceMeasureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.belong_id):
            query['BelongId'] = request.belong_id
        if not DaraCore.is_null(request.belong_id_type):
            query['BelongIdType'] = request.belong_id_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.measure_data):
            query['MeasureData'] = request.measure_data
        if not DaraCore.is_null(request.meta_data):
            query['MetaData'] = request.meta_data
        if not DaraCore.is_null(request.resource_code):
            query['ResourceCode'] = request.resource_code
        if not DaraCore.is_null(request.use_time):
            query['UseTime'] = request.use_time
        if not DaraCore.is_null(request.use_type):
            query['UseType'] = request.use_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushResourceMeasure',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushResourceMeasureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_resource_measure(
        self,
        request: main_models.PushResourceMeasureRequest,
    ) -> main_models.PushResourceMeasureResponse:
        runtime = RuntimeOptions()
        return self.push_resource_measure_with_options(request, runtime)

    async def push_resource_measure_async(
        self,
        request: main_models.PushResourceMeasureRequest,
    ) -> main_models.PushResourceMeasureResponse:
        runtime = RuntimeOptions()
        return await self.push_resource_measure_with_options_async(request, runtime)

    def query_inspiration_account_details_with_options(
        self,
        request: main_models.QueryInspirationAccountDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInspirationAccountDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInspirationAccountDetails',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInspirationAccountDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_inspiration_account_details_with_options_async(
        self,
        request: main_models.QueryInspirationAccountDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInspirationAccountDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInspirationAccountDetails',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInspirationAccountDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_inspiration_account_details(
        self,
        request: main_models.QueryInspirationAccountDetailsRequest,
    ) -> main_models.QueryInspirationAccountDetailsResponse:
        runtime = RuntimeOptions()
        return self.query_inspiration_account_details_with_options(request, runtime)

    async def query_inspiration_account_details_async(
        self,
        request: main_models.QueryInspirationAccountDetailsRequest,
    ) -> main_models.QueryInspirationAccountDetailsResponse:
        runtime = RuntimeOptions()
        return await self.query_inspiration_account_details_with_options_async(request, runtime)

    def query_inspiration_balance_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInspirationBalanceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryInspirationBalance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInspirationBalanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_inspiration_balance_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInspirationBalanceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryInspirationBalance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInspirationBalanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_inspiration_balance(self) -> main_models.QueryInspirationBalanceResponse:
        runtime = RuntimeOptions()
        return self.query_inspiration_balance_with_options(runtime)

    async def query_inspiration_balance_async(self) -> main_models.QueryInspirationBalanceResponse:
        runtime = RuntimeOptions()
        return await self.query_inspiration_balance_with_options_async(runtime)

    def query_inspiration_consume_records_with_options(
        self,
        request: main_models.QueryInspirationConsumeRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInspirationConsumeRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInspirationConsumeRecords',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInspirationConsumeRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_inspiration_consume_records_with_options_async(
        self,
        request: main_models.QueryInspirationConsumeRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInspirationConsumeRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInspirationConsumeRecords',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInspirationConsumeRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_inspiration_consume_records(
        self,
        request: main_models.QueryInspirationConsumeRecordsRequest,
    ) -> main_models.QueryInspirationConsumeRecordsResponse:
        runtime = RuntimeOptions()
        return self.query_inspiration_consume_records_with_options(request, runtime)

    async def query_inspiration_consume_records_async(
        self,
        request: main_models.QueryInspirationConsumeRecordsRequest,
    ) -> main_models.QueryInspirationConsumeRecordsResponse:
        runtime = RuntimeOptions()
        return await self.query_inspiration_consume_records_with_options_async(request, runtime)

    def query_material_directory_tree_with_options(
        self,
        request: main_models.QueryMaterialDirectoryTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialDirectoryTreeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.hidden_public):
            query['HiddenPublic'] = request.hidden_public
        if not DaraCore.is_null(request.root):
            query['Root'] = request.root
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialDirectoryTree',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialDirectoryTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_material_directory_tree_with_options_async(
        self,
        request: main_models.QueryMaterialDirectoryTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialDirectoryTreeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.hidden_public):
            query['HiddenPublic'] = request.hidden_public
        if not DaraCore.is_null(request.root):
            query['Root'] = request.root
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialDirectoryTree',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialDirectoryTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_material_directory_tree(
        self,
        request: main_models.QueryMaterialDirectoryTreeRequest,
    ) -> main_models.QueryMaterialDirectoryTreeResponse:
        runtime = RuntimeOptions()
        return self.query_material_directory_tree_with_options(request, runtime)

    async def query_material_directory_tree_async(
        self,
        request: main_models.QueryMaterialDirectoryTreeRequest,
    ) -> main_models.QueryMaterialDirectoryTreeResponse:
        runtime = RuntimeOptions()
        return await self.query_material_directory_tree_with_options_async(request, runtime)

    def query_material_file_detail_with_options(
        self,
        request: main_models.QueryMaterialFileDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialFileDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialFileDetail',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialFileDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_material_file_detail_with_options_async(
        self,
        request: main_models.QueryMaterialFileDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialFileDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialFileDetail',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialFileDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_material_file_detail(
        self,
        request: main_models.QueryMaterialFileDetailRequest,
    ) -> main_models.QueryMaterialFileDetailResponse:
        runtime = RuntimeOptions()
        return self.query_material_file_detail_with_options(request, runtime)

    async def query_material_file_detail_async(
        self,
        request: main_models.QueryMaterialFileDetailRequest,
    ) -> main_models.QueryMaterialFileDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_material_file_detail_with_options_async(request, runtime)

    def query_material_file_list_with_options(
        self,
        tmp_req: main_models.QueryMaterialFileListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialFileListResponse:
        tmp_req.validate()
        request = main_models.QueryMaterialFileListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        if not DaraCore.is_null(tmp_req.suffix_list):
            request.suffix_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.suffix_list, 'SuffixList', 'json')
        if not DaraCore.is_null(tmp_req.type_list):
            request.type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.type_list, 'TypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_file_size):
            query['MaxFileSize'] = request.max_file_size
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.min_file_size):
            query['MinFileSize'] = request.min_file_size
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        if not DaraCore.is_null(request.suffix_list_shrink):
            query['SuffixList'] = request.suffix_list_shrink
        if not DaraCore.is_null(request.type_list_shrink):
            query['TypeList'] = request.type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialFileList',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialFileListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_material_file_list_with_options_async(
        self,
        tmp_req: main_models.QueryMaterialFileListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialFileListResponse:
        tmp_req.validate()
        request = main_models.QueryMaterialFileListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        if not DaraCore.is_null(tmp_req.suffix_list):
            request.suffix_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.suffix_list, 'SuffixList', 'json')
        if not DaraCore.is_null(tmp_req.type_list):
            request.type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.type_list, 'TypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_file_size):
            query['MaxFileSize'] = request.max_file_size
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.min_file_size):
            query['MinFileSize'] = request.min_file_size
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        if not DaraCore.is_null(request.suffix_list_shrink):
            query['SuffixList'] = request.suffix_list_shrink
        if not DaraCore.is_null(request.type_list_shrink):
            query['TypeList'] = request.type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialFileList',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialFileListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_material_file_list(
        self,
        request: main_models.QueryMaterialFileListRequest,
    ) -> main_models.QueryMaterialFileListResponse:
        runtime = RuntimeOptions()
        return self.query_material_file_list_with_options(request, runtime)

    async def query_material_file_list_async(
        self,
        request: main_models.QueryMaterialFileListRequest,
    ) -> main_models.QueryMaterialFileListResponse:
        runtime = RuntimeOptions()
        return await self.query_material_file_list_with_options_async(request, runtime)

    def query_material_file_summary_info_with_options(
        self,
        tmp_req: main_models.QueryMaterialFileSummaryInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialFileSummaryInfoResponse:
        tmp_req.validate()
        request = main_models.QueryMaterialFileSummaryInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        if not DaraCore.is_null(tmp_req.type_list):
            request.type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.type_list, 'TypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        if not DaraCore.is_null(request.type_list_shrink):
            query['TypeList'] = request.type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialFileSummaryInfo',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialFileSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_material_file_summary_info_with_options_async(
        self,
        tmp_req: main_models.QueryMaterialFileSummaryInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialFileSummaryInfoResponse:
        tmp_req.validate()
        request = main_models.QueryMaterialFileSummaryInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        if not DaraCore.is_null(tmp_req.type_list):
            request.type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.type_list, 'TypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        if not DaraCore.is_null(request.type_list_shrink):
            query['TypeList'] = request.type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialFileSummaryInfo',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialFileSummaryInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_material_file_summary_info(
        self,
        request: main_models.QueryMaterialFileSummaryInfoRequest,
    ) -> main_models.QueryMaterialFileSummaryInfoResponse:
        runtime = RuntimeOptions()
        return self.query_material_file_summary_info_with_options(request, runtime)

    async def query_material_file_summary_info_async(
        self,
        request: main_models.QueryMaterialFileSummaryInfoRequest,
    ) -> main_models.QueryMaterialFileSummaryInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_material_file_summary_info_with_options_async(request, runtime)

    def query_material_task_detail_with_options(
        self,
        request: main_models.QueryMaterialTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialTaskDetail',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_material_task_detail_with_options_async(
        self,
        request: main_models.QueryMaterialTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialTaskDetail',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_material_task_detail(
        self,
        request: main_models.QueryMaterialTaskDetailRequest,
    ) -> main_models.QueryMaterialTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.query_material_task_detail_with_options(request, runtime)

    async def query_material_task_detail_async(
        self,
        request: main_models.QueryMaterialTaskDetailRequest,
    ) -> main_models.QueryMaterialTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_material_task_detail_with_options_async(request, runtime)

    def query_material_task_list_with_options(
        self,
        tmp_req: main_models.QueryMaterialTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialTaskListResponse:
        tmp_req.validate()
        request = main_models.QueryMaterialTaskListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        if not DaraCore.is_null(tmp_req.task_type_list):
            request.task_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_type_list, 'TaskTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        if not DaraCore.is_null(request.task_type_list_shrink):
            query['TaskTypeList'] = request.task_type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialTaskList',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_material_task_list_with_options_async(
        self,
        tmp_req: main_models.QueryMaterialTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMaterialTaskListResponse:
        tmp_req.validate()
        request = main_models.QueryMaterialTaskListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        if not DaraCore.is_null(tmp_req.task_type_list):
            request.task_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_type_list, 'TaskTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        if not DaraCore.is_null(request.task_type_list_shrink):
            query['TaskTypeList'] = request.task_type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMaterialTaskList',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMaterialTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_material_task_list(
        self,
        request: main_models.QueryMaterialTaskListRequest,
    ) -> main_models.QueryMaterialTaskListResponse:
        runtime = RuntimeOptions()
        return self.query_material_task_list_with_options(request, runtime)

    async def query_material_task_list_async(
        self,
        request: main_models.QueryMaterialTaskListRequest,
    ) -> main_models.QueryMaterialTaskListResponse:
        runtime = RuntimeOptions()
        return await self.query_material_task_list_with_options_async(request, runtime)

    def query_supabase_auth_configs_for_admin_with_options(
        self,
        request: main_models.QuerySupabaseAuthConfigsForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySupabaseAuthConfigsForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySupabaseAuthConfigsForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySupabaseAuthConfigsForAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_supabase_auth_configs_for_admin_with_options_async(
        self,
        request: main_models.QuerySupabaseAuthConfigsForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySupabaseAuthConfigsForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySupabaseAuthConfigsForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySupabaseAuthConfigsForAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_supabase_auth_configs_for_admin(
        self,
        request: main_models.QuerySupabaseAuthConfigsForAdminRequest,
    ) -> main_models.QuerySupabaseAuthConfigsForAdminResponse:
        runtime = RuntimeOptions()
        return self.query_supabase_auth_configs_for_admin_with_options(request, runtime)

    async def query_supabase_auth_configs_for_admin_async(
        self,
        request: main_models.QuerySupabaseAuthConfigsForAdminRequest,
    ) -> main_models.QuerySupabaseAuthConfigsForAdminResponse:
        runtime = RuntimeOptions()
        return await self.query_supabase_auth_configs_for_admin_with_options_async(request, runtime)

    def query_supabase_configs_for_admin_with_options(
        self,
        request: main_models.QuerySupabaseConfigsForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySupabaseConfigsForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySupabaseConfigsForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySupabaseConfigsForAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_supabase_configs_for_admin_with_options_async(
        self,
        request: main_models.QuerySupabaseConfigsForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySupabaseConfigsForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySupabaseConfigsForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySupabaseConfigsForAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_supabase_configs_for_admin(
        self,
        request: main_models.QuerySupabaseConfigsForAdminRequest,
    ) -> main_models.QuerySupabaseConfigsForAdminResponse:
        runtime = RuntimeOptions()
        return self.query_supabase_configs_for_admin_with_options(request, runtime)

    async def query_supabase_configs_for_admin_async(
        self,
        request: main_models.QuerySupabaseConfigsForAdminRequest,
    ) -> main_models.QuerySupabaseConfigsForAdminResponse:
        runtime = RuntimeOptions()
        return await self.query_supabase_configs_for_admin_with_options_async(request, runtime)

    def query_supabase_instance_info_for_admin_with_options(
        self,
        request: main_models.QuerySupabaseInstanceInfoForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySupabaseInstanceInfoForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySupabaseInstanceInfoForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySupabaseInstanceInfoForAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_supabase_instance_info_for_admin_with_options_async(
        self,
        request: main_models.QuerySupabaseInstanceInfoForAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySupabaseInstanceInfoForAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySupabaseInstanceInfoForAdmin',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySupabaseInstanceInfoForAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_supabase_instance_info_for_admin(
        self,
        request: main_models.QuerySupabaseInstanceInfoForAdminRequest,
    ) -> main_models.QuerySupabaseInstanceInfoForAdminResponse:
        runtime = RuntimeOptions()
        return self.query_supabase_instance_info_for_admin_with_options(request, runtime)

    async def query_supabase_instance_info_for_admin_async(
        self,
        request: main_models.QuerySupabaseInstanceInfoForAdminRequest,
    ) -> main_models.QuerySupabaseInstanceInfoForAdminResponse:
        runtime = RuntimeOptions()
        return await self.query_supabase_instance_info_for_admin_with_options_async(request, runtime)

    def reconnect_app_chat_with_sse(
        self,
        request: main_models.ReconnectAppChatRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ReconnectAppChatResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chat_id):
            query['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.last_event_id):
            query['LastEventId'] = request.last_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReconnectAppChat',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = resp.event.data
                yield  DaraCore.from_map(
                    main_models.ReconnectAppChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def reconnect_app_chat_with_sse_async(
        self,
        request: main_models.ReconnectAppChatRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ReconnectAppChatResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chat_id):
            query['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.last_event_id):
            query['LastEventId'] = request.last_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReconnectAppChat',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = resp.event.data
                yield  DaraCore.from_map(
                    main_models.ReconnectAppChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def reconnect_app_chat_with_options(
        self,
        request: main_models.ReconnectAppChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReconnectAppChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chat_id):
            query['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.last_event_id):
            query['LastEventId'] = request.last_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReconnectAppChat',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.ReconnectAppChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def reconnect_app_chat_with_options_async(
        self,
        request: main_models.ReconnectAppChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReconnectAppChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chat_id):
            query['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.last_event_id):
            query['LastEventId'] = request.last_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReconnectAppChat',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.ReconnectAppChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reconnect_app_chat(
        self,
        request: main_models.ReconnectAppChatRequest,
    ) -> main_models.ReconnectAppChatResponse:
        runtime = RuntimeOptions()
        return self.reconnect_app_chat_with_options(request, runtime)

    async def reconnect_app_chat_async(
        self,
        request: main_models.ReconnectAppChatRequest,
    ) -> main_models.ReconnectAppChatResponse:
        runtime = RuntimeOptions()
        return await self.reconnect_app_chat_with_options_async(request, runtime)

    def refresh_app_instance_ticket_with_options(
        self,
        request: main_models.RefreshAppInstanceTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshAppInstanceTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshAppInstanceTicket',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshAppInstanceTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_app_instance_ticket_with_options_async(
        self,
        request: main_models.RefreshAppInstanceTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshAppInstanceTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshAppInstanceTicket',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshAppInstanceTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_app_instance_ticket(
        self,
        request: main_models.RefreshAppInstanceTicketRequest,
    ) -> main_models.RefreshAppInstanceTicketResponse:
        runtime = RuntimeOptions()
        return self.refresh_app_instance_ticket_with_options(request, runtime)

    async def refresh_app_instance_ticket_async(
        self,
        request: main_models.RefreshAppInstanceTicketRequest,
    ) -> main_models.RefreshAppInstanceTicketResponse:
        runtime = RuntimeOptions()
        return await self.refresh_app_instance_ticket_with_options_async(request, runtime)

    def refund_app_instance_for_partner_with_options(
        self,
        request: main_models.RefundAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefundAppInstanceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.refund_reason):
            query['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefundAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundAppInstanceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_app_instance_for_partner_with_options_async(
        self,
        request: main_models.RefundAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefundAppInstanceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.refund_reason):
            query['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefundAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundAppInstanceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_app_instance_for_partner(
        self,
        request: main_models.RefundAppInstanceForPartnerRequest,
    ) -> main_models.RefundAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return self.refund_app_instance_for_partner_with_options(request, runtime)

    async def refund_app_instance_for_partner_async(
        self,
        request: main_models.RefundAppInstanceForPartnerRequest,
    ) -> main_models.RefundAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.refund_app_instance_for_partner_with_options_async(request, runtime)

    def renew_app_instance_with_options(
        self,
        request: main_models.RenewAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_app_instance_with_options_async(
        self,
        request: main_models.RenewAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_app_instance(
        self,
        request: main_models.RenewAppInstanceRequest,
    ) -> main_models.RenewAppInstanceResponse:
        runtime = RuntimeOptions()
        return self.renew_app_instance_with_options(request, runtime)

    async def renew_app_instance_async(
        self,
        request: main_models.RenewAppInstanceRequest,
    ) -> main_models.RenewAppInstanceResponse:
        runtime = RuntimeOptions()
        return await self.renew_app_instance_with_options_async(request, runtime)

    def renew_app_sandbox_with_options(
        self,
        request: main_models.RenewAppSandboxRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAppSandboxResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAppSandbox',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAppSandboxResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_app_sandbox_with_options_async(
        self,
        request: main_models.RenewAppSandboxRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAppSandboxResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAppSandbox',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAppSandboxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_app_sandbox(
        self,
        request: main_models.RenewAppSandboxRequest,
    ) -> main_models.RenewAppSandboxResponse:
        runtime = RuntimeOptions()
        return self.renew_app_sandbox_with_options(request, runtime)

    async def renew_app_sandbox_async(
        self,
        request: main_models.RenewAppSandboxRequest,
    ) -> main_models.RenewAppSandboxResponse:
        runtime = RuntimeOptions()
        return await self.renew_app_sandbox_with_options_async(request, runtime)

    def rollback_app_code_snapshot_with_options(
        self,
        request: main_models.RollbackAppCodeSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackAppCodeSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        if not DaraCore.is_null(request.target_logical_number):
            query['TargetLogicalNumber'] = request.target_logical_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackAppCodeSnapshot',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackAppCodeSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_app_code_snapshot_with_options_async(
        self,
        request: main_models.RollbackAppCodeSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackAppCodeSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.site_id):
            query['SiteId'] = request.site_id
        if not DaraCore.is_null(request.target_logical_number):
            query['TargetLogicalNumber'] = request.target_logical_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackAppCodeSnapshot',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackAppCodeSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_app_code_snapshot(
        self,
        request: main_models.RollbackAppCodeSnapshotRequest,
    ) -> main_models.RollbackAppCodeSnapshotResponse:
        runtime = RuntimeOptions()
        return self.rollback_app_code_snapshot_with_options(request, runtime)

    async def rollback_app_code_snapshot_async(
        self,
        request: main_models.RollbackAppCodeSnapshotRequest,
    ) -> main_models.RollbackAppCodeSnapshotResponse:
        runtime = RuntimeOptions()
        return await self.rollback_app_code_snapshot_with_options_async(request, runtime)

    def rollback_app_instance_publish_with_options(
        self,
        request: main_models.RollbackAppInstancePublishRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackAppInstancePublishResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.deploy_channel):
            query['DeployChannel'] = request.deploy_channel
        if not DaraCore.is_null(request.publish_number):
            query['PublishNumber'] = request.publish_number
        if not DaraCore.is_null(request.quick_rollback):
            query['QuickRollback'] = request.quick_rollback
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackAppInstancePublish',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackAppInstancePublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_app_instance_publish_with_options_async(
        self,
        request: main_models.RollbackAppInstancePublishRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackAppInstancePublishResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.deploy_channel):
            query['DeployChannel'] = request.deploy_channel
        if not DaraCore.is_null(request.publish_number):
            query['PublishNumber'] = request.publish_number
        if not DaraCore.is_null(request.quick_rollback):
            query['QuickRollback'] = request.quick_rollback
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackAppInstancePublish',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackAppInstancePublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_app_instance_publish(
        self,
        request: main_models.RollbackAppInstancePublishRequest,
    ) -> main_models.RollbackAppInstancePublishResponse:
        runtime = RuntimeOptions()
        return self.rollback_app_instance_publish_with_options(request, runtime)

    async def rollback_app_instance_publish_async(
        self,
        request: main_models.RollbackAppInstancePublishRequest,
    ) -> main_models.RollbackAppInstancePublishResponse:
        runtime = RuntimeOptions()
        return await self.rollback_app_instance_publish_with_options_async(request, runtime)

    def save_app_requirement_with_options(
        self,
        request: main_models.SaveAppRequirementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAppRequirementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        body = {}
        if not DaraCore.is_null(request.prd):
            body['Prd'] = request.prd
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveAppRequirement',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAppRequirementResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_app_requirement_with_options_async(
        self,
        request: main_models.SaveAppRequirementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAppRequirementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        body = {}
        if not DaraCore.is_null(request.prd):
            body['Prd'] = request.prd
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveAppRequirement',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAppRequirementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_app_requirement(
        self,
        request: main_models.SaveAppRequirementRequest,
    ) -> main_models.SaveAppRequirementResponse:
        runtime = RuntimeOptions()
        return self.save_app_requirement_with_options(request, runtime)

    async def save_app_requirement_async(
        self,
        request: main_models.SaveAppRequirementRequest,
    ) -> main_models.SaveAppRequirementResponse:
        runtime = RuntimeOptions()
        return await self.save_app_requirement_with_options_async(request, runtime)

    def save_app_supabase_secrets_with_options(
        self,
        request: main_models.SaveAppSupabaseSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAppSupabaseSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.secrets_json):
            query['SecretsJson'] = request.secrets_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveAppSupabaseSecrets',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAppSupabaseSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_app_supabase_secrets_with_options_async(
        self,
        request: main_models.SaveAppSupabaseSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAppSupabaseSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.secrets_json):
            query['SecretsJson'] = request.secrets_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveAppSupabaseSecrets',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAppSupabaseSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_app_supabase_secrets(
        self,
        request: main_models.SaveAppSupabaseSecretsRequest,
    ) -> main_models.SaveAppSupabaseSecretsResponse:
        runtime = RuntimeOptions()
        return self.save_app_supabase_secrets_with_options(request, runtime)

    async def save_app_supabase_secrets_async(
        self,
        request: main_models.SaveAppSupabaseSecretsRequest,
    ) -> main_models.SaveAppSupabaseSecretsResponse:
        runtime = RuntimeOptions()
        return await self.save_app_supabase_secrets_with_options_async(request, runtime)

    def search_image_with_options(
        self,
        tmp_req: main_models.SearchImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageResponse:
        tmp_req.validate()
        request = main_models.SearchImageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'simple')
        query = {}
        if not DaraCore.is_null(request.color_hex):
            query['ColorHex'] = request.color_hex
        if not DaraCore.is_null(request.has_person):
            query['HasPerson'] = request.has_person
        if not DaraCore.is_null(request.image_category):
            query['ImageCategory'] = request.image_category
        if not DaraCore.is_null(request.image_ratio):
            query['ImageRatio'] = request.image_ratio
        if not DaraCore.is_null(request.max_height):
            query['MaxHeight'] = request.max_height
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.max_width):
            query['MaxWidth'] = request.max_width
        if not DaraCore.is_null(request.min_height):
            query['MinHeight'] = request.min_height
        if not DaraCore.is_null(request.min_width):
            query['MinWidth'] = request.min_width
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.oss_key):
            query['OssKey'] = request.oss_key
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchImage',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_with_options_async(
        self,
        tmp_req: main_models.SearchImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageResponse:
        tmp_req.validate()
        request = main_models.SearchImageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'simple')
        query = {}
        if not DaraCore.is_null(request.color_hex):
            query['ColorHex'] = request.color_hex
        if not DaraCore.is_null(request.has_person):
            query['HasPerson'] = request.has_person
        if not DaraCore.is_null(request.image_category):
            query['ImageCategory'] = request.image_category
        if not DaraCore.is_null(request.image_ratio):
            query['ImageRatio'] = request.image_ratio
        if not DaraCore.is_null(request.max_height):
            query['MaxHeight'] = request.max_height
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.max_width):
            query['MaxWidth'] = request.max_width
        if not DaraCore.is_null(request.min_height):
            query['MinHeight'] = request.min_height
        if not DaraCore.is_null(request.min_width):
            query['MinWidth'] = request.min_width
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.oss_key):
            query['OssKey'] = request.oss_key
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchImage',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image(
        self,
        request: main_models.SearchImageRequest,
    ) -> main_models.SearchImageResponse:
        runtime = RuntimeOptions()
        return self.search_image_with_options(request, runtime)

    async def search_image_async(
        self,
        request: main_models.SearchImageRequest,
    ) -> main_models.SearchImageResponse:
        runtime = RuntimeOptions()
        return await self.search_image_with_options_async(request, runtime)

    def set_app_domain_certificate_with_options(
        self,
        request: main_models.SetAppDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAppDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not DaraCore.is_null(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAppDomainCertificate',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAppDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_app_domain_certificate_with_options_async(
        self,
        request: main_models.SetAppDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAppDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not DaraCore.is_null(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAppDomainCertificate',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAppDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_app_domain_certificate(
        self,
        request: main_models.SetAppDomainCertificateRequest,
    ) -> main_models.SetAppDomainCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_app_domain_certificate_with_options(request, runtime)

    async def set_app_domain_certificate_async(
        self,
        request: main_models.SetAppDomainCertificateRequest,
    ) -> main_models.SetAppDomainCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_app_domain_certificate_with_options_async(request, runtime)

    def submit_app_seo_index_with_options(
        self,
        request: main_models.SubmitAppSeoIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAppSeoIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.se_type):
            query['SeType'] = request.se_type
        if not DaraCore.is_null(request.submit_later):
            query['SubmitLater'] = request.submit_later
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAppSeoIndex',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAppSeoIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_app_seo_index_with_options_async(
        self,
        request: main_models.SubmitAppSeoIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAppSeoIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.se_type):
            query['SeType'] = request.se_type
        if not DaraCore.is_null(request.submit_later):
            query['SubmitLater'] = request.submit_later
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAppSeoIndex',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAppSeoIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_app_seo_index(
        self,
        request: main_models.SubmitAppSeoIndexRequest,
    ) -> main_models.SubmitAppSeoIndexResponse:
        runtime = RuntimeOptions()
        return self.submit_app_seo_index_with_options(request, runtime)

    async def submit_app_seo_index_async(
        self,
        request: main_models.SubmitAppSeoIndexRequest,
    ) -> main_models.SubmitAppSeoIndexResponse:
        runtime = RuntimeOptions()
        return await self.submit_app_seo_index_with_options_async(request, runtime)

    def submit_material_task_with_options(
        self,
        request: main_models.SubmitMaterialTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMaterialTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_param):
            query['TaskParam'] = request.task_param
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMaterialTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMaterialTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_material_task_with_options_async(
        self,
        request: main_models.SubmitMaterialTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMaterialTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_param):
            query['TaskParam'] = request.task_param
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMaterialTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMaterialTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_material_task(
        self,
        request: main_models.SubmitMaterialTaskRequest,
    ) -> main_models.SubmitMaterialTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_material_task_with_options(request, runtime)

    async def submit_material_task_async(
        self,
        request: main_models.SubmitMaterialTaskRequest,
    ) -> main_models.SubmitMaterialTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_material_task_with_options_async(request, runtime)

    def switch_app_conversation_with_options(
        self,
        request: main_models.SwitchAppConversationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchAppConversationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchAppConversation',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchAppConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_app_conversation_with_options_async(
        self,
        request: main_models.SwitchAppConversationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchAppConversationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchAppConversation',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchAppConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_app_conversation(
        self,
        request: main_models.SwitchAppConversationRequest,
    ) -> main_models.SwitchAppConversationResponse:
        runtime = RuntimeOptions()
        return self.switch_app_conversation_with_options(request, runtime)

    async def switch_app_conversation_async(
        self,
        request: main_models.SwitchAppConversationRequest,
    ) -> main_models.SwitchAppConversationResponse:
        runtime = RuntimeOptions()
        return await self.switch_app_conversation_with_options_async(request, runtime)

    def sync_app_instance_for_partner_with_options(
        self,
        tmp_req: main_models.SyncAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncAppInstanceForPartnerResponse:
        tmp_req.validate()
        request = main_models.SyncAppInstanceForPartnerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.app_instance):
            request.app_instance_shrink = Utils.array_to_string_with_specified_style(tmp_req.app_instance, 'AppInstance', 'json')
        query = {}
        if not DaraCore.is_null(request.app_instance_shrink):
            query['AppInstance'] = request.app_instance_shrink
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.operator):
            query['Operator'] = request.operator
        if not DaraCore.is_null(request.source_biz_id):
            query['SourceBizId'] = request.source_biz_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncAppInstanceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_app_instance_for_partner_with_options_async(
        self,
        tmp_req: main_models.SyncAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncAppInstanceForPartnerResponse:
        tmp_req.validate()
        request = main_models.SyncAppInstanceForPartnerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.app_instance):
            request.app_instance_shrink = Utils.array_to_string_with_specified_style(tmp_req.app_instance, 'AppInstance', 'json')
        query = {}
        if not DaraCore.is_null(request.app_instance_shrink):
            query['AppInstance'] = request.app_instance_shrink
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.operator):
            query['Operator'] = request.operator
        if not DaraCore.is_null(request.source_biz_id):
            query['SourceBizId'] = request.source_biz_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncAppInstanceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_app_instance_for_partner(
        self,
        request: main_models.SyncAppInstanceForPartnerRequest,
    ) -> main_models.SyncAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return self.sync_app_instance_for_partner_with_options(request, runtime)

    async def sync_app_instance_for_partner_async(
        self,
        request: main_models.SyncAppInstanceForPartnerRequest,
    ) -> main_models.SyncAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.sync_app_instance_for_partner_with_options_async(request, runtime)

    def unbind_app_domain_with_options(
        self,
        request: main_models.UnbindAppDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAppDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAppDomain',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAppDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_app_domain_with_options_async(
        self,
        request: main_models.UnbindAppDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAppDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAppDomain',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAppDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_app_domain(
        self,
        request: main_models.UnbindAppDomainRequest,
    ) -> main_models.UnbindAppDomainResponse:
        runtime = RuntimeOptions()
        return self.unbind_app_domain_with_options(request, runtime)

    async def unbind_app_domain_async(
        self,
        request: main_models.UnbindAppDomainRequest,
    ) -> main_models.UnbindAppDomainResponse:
        runtime = RuntimeOptions()
        return await self.unbind_app_domain_with_options_async(request, runtime)

    def update_app_chat_message_with_options(
        self,
        request: main_models.UpdateAppChatMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppChatMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.added_meta_data):
            query['AddedMetaData'] = request.added_meta_data
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppChatMessage',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppChatMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_chat_message_with_options_async(
        self,
        request: main_models.UpdateAppChatMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppChatMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.added_meta_data):
            query['AddedMetaData'] = request.added_meta_data
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppChatMessage',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppChatMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_chat_message(
        self,
        request: main_models.UpdateAppChatMessageRequest,
    ) -> main_models.UpdateAppChatMessageResponse:
        runtime = RuntimeOptions()
        return self.update_app_chat_message_with_options(request, runtime)

    async def update_app_chat_message_async(
        self,
        request: main_models.UpdateAppChatMessageRequest,
    ) -> main_models.UpdateAppChatMessageResponse:
        runtime = RuntimeOptions()
        return await self.update_app_chat_message_with_options_async(request, runtime)

    def update_app_code_with_options(
        self,
        request: main_models.UpdateAppCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppCode',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_code_with_options_async(
        self,
        request: main_models.UpdateAppCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppCode',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_code(
        self,
        request: main_models.UpdateAppCodeRequest,
    ) -> main_models.UpdateAppCodeResponse:
        runtime = RuntimeOptions()
        return self.update_app_code_with_options(request, runtime)

    async def update_app_code_async(
        self,
        request: main_models.UpdateAppCodeRequest,
    ) -> main_models.UpdateAppCodeResponse:
        runtime = RuntimeOptions()
        return await self.update_app_code_with_options_async(request, runtime)

    def update_app_file_with_options(
        self,
        request: main_models.UpdateAppFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_file_with_options_async(
        self,
        request: main_models.UpdateAppFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_file(
        self,
        request: main_models.UpdateAppFileRequest,
    ) -> main_models.UpdateAppFileResponse:
        runtime = RuntimeOptions()
        return self.update_app_file_with_options(request, runtime)

    async def update_app_file_async(
        self,
        request: main_models.UpdateAppFileRequest,
    ) -> main_models.UpdateAppFileResponse:
        runtime = RuntimeOptions()
        return await self.update_app_file_with_options_async(request, runtime)

    def update_app_instance_with_options(
        self,
        tmp_req: main_models.UpdateAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppInstanceResponse:
        tmp_req.validate()
        request = main_models.UpdateAppInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deploy_area):
            query['DeployArea'] = request.deploy_area
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.icon_url):
            query['IconUrl'] = request.icon_url
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.site_version):
            query['SiteVersion'] = request.site_version
        if not DaraCore.is_null(request.thumbnail_url):
            query['ThumbnailUrl'] = request.thumbnail_url
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_instance_with_options_async(
        self,
        tmp_req: main_models.UpdateAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppInstanceResponse:
        tmp_req.validate()
        request = main_models.UpdateAppInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deploy_area):
            query['DeployArea'] = request.deploy_area
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.icon_url):
            query['IconUrl'] = request.icon_url
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.site_version):
            query['SiteVersion'] = request.site_version
        if not DaraCore.is_null(request.thumbnail_url):
            query['ThumbnailUrl'] = request.thumbnail_url
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_instance(
        self,
        request: main_models.UpdateAppInstanceRequest,
    ) -> main_models.UpdateAppInstanceResponse:
        runtime = RuntimeOptions()
        return self.update_app_instance_with_options(request, runtime)

    async def update_app_instance_async(
        self,
        request: main_models.UpdateAppInstanceRequest,
    ) -> main_models.UpdateAppInstanceResponse:
        runtime = RuntimeOptions()
        return await self.update_app_instance_with_options_async(request, runtime)

    def update_app_seo_status_with_options(
        self,
        request: main_models.UpdateAppSeoStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppSeoStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.se_type):
            query['SeType'] = request.se_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppSeoStatus',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppSeoStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_seo_status_with_options_async(
        self,
        request: main_models.UpdateAppSeoStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppSeoStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.se_type):
            query['SeType'] = request.se_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppSeoStatus',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppSeoStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_seo_status(
        self,
        request: main_models.UpdateAppSeoStatusRequest,
    ) -> main_models.UpdateAppSeoStatusResponse:
        runtime = RuntimeOptions()
        return self.update_app_seo_status_with_options(request, runtime)

    async def update_app_seo_status_async(
        self,
        request: main_models.UpdateAppSeoStatusRequest,
    ) -> main_models.UpdateAppSeoStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_app_seo_status_with_options_async(request, runtime)

    def update_app_supabase_auth_config_with_options(
        self,
        request: main_models.UpdateAppSupabaseAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppSupabaseAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.configs_json):
            query['ConfigsJson'] = request.configs_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppSupabaseAuthConfig',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppSupabaseAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_supabase_auth_config_with_options_async(
        self,
        request: main_models.UpdateAppSupabaseAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppSupabaseAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.configs_json):
            query['ConfigsJson'] = request.configs_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppSupabaseAuthConfig',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppSupabaseAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_supabase_auth_config(
        self,
        request: main_models.UpdateAppSupabaseAuthConfigRequest,
    ) -> main_models.UpdateAppSupabaseAuthConfigResponse:
        runtime = RuntimeOptions()
        return self.update_app_supabase_auth_config_with_options(request, runtime)

    async def update_app_supabase_auth_config_async(
        self,
        request: main_models.UpdateAppSupabaseAuthConfigRequest,
    ) -> main_models.UpdateAppSupabaseAuthConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_app_supabase_auth_config_with_options_async(request, runtime)

    def update_app_supabase_secret_with_options(
        self,
        request: main_models.UpdateAppSupabaseSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppSupabaseSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.secret_type):
            query['SecretType'] = request.secret_type
        if not DaraCore.is_null(request.secret_value):
            query['SecretValue'] = request.secret_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppSupabaseSecret',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppSupabaseSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_supabase_secret_with_options_async(
        self,
        request: main_models.UpdateAppSupabaseSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppSupabaseSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.secret_type):
            query['SecretType'] = request.secret_type
        if not DaraCore.is_null(request.secret_value):
            query['SecretValue'] = request.secret_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppSupabaseSecret',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppSupabaseSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_supabase_secret(
        self,
        request: main_models.UpdateAppSupabaseSecretRequest,
    ) -> main_models.UpdateAppSupabaseSecretResponse:
        runtime = RuntimeOptions()
        return self.update_app_supabase_secret_with_options(request, runtime)

    async def update_app_supabase_secret_async(
        self,
        request: main_models.UpdateAppSupabaseSecretRequest,
    ) -> main_models.UpdateAppSupabaseSecretResponse:
        runtime = RuntimeOptions()
        return await self.update_app_supabase_secret_with_options_async(request, runtime)

    def update_mini_app_binding_with_options(
        self,
        request: main_models.UpdateMiniAppBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMiniAppBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.setting_key):
            query['SettingKey'] = request.setting_key
        if not DaraCore.is_null(request.setting_value):
            query['SettingValue'] = request.setting_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMiniAppBinding',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMiniAppBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mini_app_binding_with_options_async(
        self,
        request: main_models.UpdateMiniAppBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMiniAppBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.setting_key):
            query['SettingKey'] = request.setting_key
        if not DaraCore.is_null(request.setting_value):
            query['SettingValue'] = request.setting_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMiniAppBinding',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMiniAppBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mini_app_binding(
        self,
        request: main_models.UpdateMiniAppBindingRequest,
    ) -> main_models.UpdateMiniAppBindingResponse:
        runtime = RuntimeOptions()
        return self.update_mini_app_binding_with_options(request, runtime)

    async def update_mini_app_binding_async(
        self,
        request: main_models.UpdateMiniAppBindingRequest,
    ) -> main_models.UpdateMiniAppBindingResponse:
        runtime = RuntimeOptions()
        return await self.update_mini_app_binding_with_options_async(request, runtime)

    def upload_app_site_validation_file_with_options(
        self,
        request: main_models.UploadAppSiteValidationFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadAppSiteValidationFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.file):
            query['File'] = request.file
        if not DaraCore.is_null(request.file_content):
            query['FileContent'] = request.file_content
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.site_host):
            query['SiteHost'] = request.site_host
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadAppSiteValidationFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadAppSiteValidationFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_app_site_validation_file_with_options_async(
        self,
        request: main_models.UploadAppSiteValidationFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadAppSiteValidationFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.file):
            query['File'] = request.file
        if not DaraCore.is_null(request.file_content):
            query['FileContent'] = request.file_content
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.site_host):
            query['SiteHost'] = request.site_host
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadAppSiteValidationFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadAppSiteValidationFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_app_site_validation_file(
        self,
        request: main_models.UploadAppSiteValidationFileRequest,
    ) -> main_models.UploadAppSiteValidationFileResponse:
        runtime = RuntimeOptions()
        return self.upload_app_site_validation_file_with_options(request, runtime)

    async def upload_app_site_validation_file_async(
        self,
        request: main_models.UploadAppSiteValidationFileRequest,
    ) -> main_models.UploadAppSiteValidationFileResponse:
        runtime = RuntimeOptions()
        return await self.upload_app_site_validation_file_with_options_async(request, runtime)

    def upload_material_file_with_options(
        self,
        request: main_models.UploadMaterialFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadMaterialFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadMaterialFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadMaterialFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_material_file_with_options_async(
        self,
        request: main_models.UploadMaterialFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadMaterialFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadMaterialFile',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadMaterialFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_material_file(
        self,
        request: main_models.UploadMaterialFileRequest,
    ) -> main_models.UploadMaterialFileResponse:
        runtime = RuntimeOptions()
        return self.upload_material_file_with_options(request, runtime)

    async def upload_material_file_async(
        self,
        request: main_models.UploadMaterialFileRequest,
    ) -> main_models.UploadMaterialFileResponse:
        runtime = RuntimeOptions()
        return await self.upload_material_file_with_options_async(request, runtime)
