# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_thirdswaicall20251127 import models as main_models
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
        self._endpoint = self.get_endpoint('thirdswaicall', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_call_outbound_instant_with_options(
        self,
        request: main_models.CreateCallOutboundInstantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCallOutboundInstantResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.called_number):
            body['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.caller_number):
            body['CallerNumber'] = request.caller_number
        if not DaraCore.is_null(request.caller_uac_account_id):
            body['CallerUacAccountId'] = request.caller_uac_account_id
        if not DaraCore.is_null(request.current_workspace_id):
            body['CurrentWorkspaceId'] = request.current_workspace_id
        if not DaraCore.is_null(request.customer_line_code):
            body['CustomerLineCode'] = request.customer_line_code
        if not DaraCore.is_null(request.customer_name):
            body['CustomerName'] = request.customer_name
        if not DaraCore.is_null(request.encrypt_call):
            body['EncryptCall'] = request.encrypt_call
        if not DaraCore.is_null(request.prompt_variables):
            body['PromptVariables'] = request.prompt_variables
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCallOutboundInstant',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCallOutboundInstantResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_call_outbound_instant_with_options_async(
        self,
        request: main_models.CreateCallOutboundInstantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCallOutboundInstantResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.called_number):
            body['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.caller_number):
            body['CallerNumber'] = request.caller_number
        if not DaraCore.is_null(request.caller_uac_account_id):
            body['CallerUacAccountId'] = request.caller_uac_account_id
        if not DaraCore.is_null(request.current_workspace_id):
            body['CurrentWorkspaceId'] = request.current_workspace_id
        if not DaraCore.is_null(request.customer_line_code):
            body['CustomerLineCode'] = request.customer_line_code
        if not DaraCore.is_null(request.customer_name):
            body['CustomerName'] = request.customer_name
        if not DaraCore.is_null(request.encrypt_call):
            body['EncryptCall'] = request.encrypt_call
        if not DaraCore.is_null(request.prompt_variables):
            body['PromptVariables'] = request.prompt_variables
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCallOutboundInstant',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCallOutboundInstantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_call_outbound_instant(
        self,
        request: main_models.CreateCallOutboundInstantRequest,
    ) -> main_models.CreateCallOutboundInstantResponse:
        runtime = RuntimeOptions()
        return self.create_call_outbound_instant_with_options(request, runtime)

    async def create_call_outbound_instant_async(
        self,
        request: main_models.CreateCallOutboundInstantRequest,
    ) -> main_models.CreateCallOutboundInstantResponse:
        runtime = RuntimeOptions()
        return await self.create_call_outbound_instant_with_options_async(request, runtime)

    def query_task_concurrency_with_options(
        self,
        request: main_models.QueryTaskConcurrencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskConcurrencyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.application_code):
            body['ApplicationCode'] = request.application_code
        if not DaraCore.is_null(request.caller_uac_account_id):
            body['CallerUacAccountId'] = request.caller_uac_account_id
        if not DaraCore.is_null(request.current_workspace_id):
            body['CurrentWorkspaceId'] = request.current_workspace_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskConcurrency',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskConcurrencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_concurrency_with_options_async(
        self,
        request: main_models.QueryTaskConcurrencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskConcurrencyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.application_code):
            body['ApplicationCode'] = request.application_code
        if not DaraCore.is_null(request.caller_uac_account_id):
            body['CallerUacAccountId'] = request.caller_uac_account_id
        if not DaraCore.is_null(request.current_workspace_id):
            body['CurrentWorkspaceId'] = request.current_workspace_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskConcurrency',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskConcurrencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_concurrency(
        self,
        request: main_models.QueryTaskConcurrencyRequest,
    ) -> main_models.QueryTaskConcurrencyResponse:
        runtime = RuntimeOptions()
        return self.query_task_concurrency_with_options(request, runtime)

    async def query_task_concurrency_async(
        self,
        request: main_models.QueryTaskConcurrencyRequest,
    ) -> main_models.QueryTaskConcurrencyResponse:
        runtime = RuntimeOptions()
        return await self.query_task_concurrency_with_options_async(request, runtime)

    def read_outbound_task_call_list_with_options(
        self,
        tmp_req: main_models.ReadOutboundTaskCallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadOutboundTaskCallListResponse:
        tmp_req.validate()
        request = main_models.ReadOutboundTaskCallListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.display_status_list):
            request.display_status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.display_status_list, 'DisplayStatusList', 'json')
        if not DaraCore.is_null(tmp_req.label_tags):
            request.label_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_tags, 'LabelTags', 'json')
        body = {}
        if not DaraCore.is_null(request.call_end_time_begin):
            body['CallEndTimeBegin'] = request.call_end_time_begin
        if not DaraCore.is_null(request.call_end_time_end):
            body['CallEndTimeEnd'] = request.call_end_time_end
        if not DaraCore.is_null(request.call_start_time_begin):
            body['CallStartTimeBegin'] = request.call_start_time_begin
        if not DaraCore.is_null(request.call_start_time_end):
            body['CallStartTimeEnd'] = request.call_start_time_end
        if not DaraCore.is_null(request.caller_uac_account_id):
            body['CallerUacAccountId'] = request.caller_uac_account_id
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.current_workspace_id):
            body['CurrentWorkspaceId'] = request.current_workspace_id
        if not DaraCore.is_null(request.customer_name_or_phone):
            body['CustomerNameOrPhone'] = request.customer_name_or_phone
        if not DaraCore.is_null(request.display_status_list_shrink):
            body['DisplayStatusList'] = request.display_status_list_shrink
        if not DaraCore.is_null(request.label_tags_shrink):
            body['LabelTags'] = request.label_tags_shrink
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadOutboundTaskCallList',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadOutboundTaskCallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_outbound_task_call_list_with_options_async(
        self,
        tmp_req: main_models.ReadOutboundTaskCallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadOutboundTaskCallListResponse:
        tmp_req.validate()
        request = main_models.ReadOutboundTaskCallListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.display_status_list):
            request.display_status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.display_status_list, 'DisplayStatusList', 'json')
        if not DaraCore.is_null(tmp_req.label_tags):
            request.label_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_tags, 'LabelTags', 'json')
        body = {}
        if not DaraCore.is_null(request.call_end_time_begin):
            body['CallEndTimeBegin'] = request.call_end_time_begin
        if not DaraCore.is_null(request.call_end_time_end):
            body['CallEndTimeEnd'] = request.call_end_time_end
        if not DaraCore.is_null(request.call_start_time_begin):
            body['CallStartTimeBegin'] = request.call_start_time_begin
        if not DaraCore.is_null(request.call_start_time_end):
            body['CallStartTimeEnd'] = request.call_start_time_end
        if not DaraCore.is_null(request.caller_uac_account_id):
            body['CallerUacAccountId'] = request.caller_uac_account_id
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.current_workspace_id):
            body['CurrentWorkspaceId'] = request.current_workspace_id
        if not DaraCore.is_null(request.customer_name_or_phone):
            body['CustomerNameOrPhone'] = request.customer_name_or_phone
        if not DaraCore.is_null(request.display_status_list_shrink):
            body['DisplayStatusList'] = request.display_status_list_shrink
        if not DaraCore.is_null(request.label_tags_shrink):
            body['LabelTags'] = request.label_tags_shrink
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadOutboundTaskCallList',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadOutboundTaskCallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_outbound_task_call_list(
        self,
        request: main_models.ReadOutboundTaskCallListRequest,
    ) -> main_models.ReadOutboundTaskCallListResponse:
        runtime = RuntimeOptions()
        return self.read_outbound_task_call_list_with_options(request, runtime)

    async def read_outbound_task_call_list_async(
        self,
        request: main_models.ReadOutboundTaskCallListRequest,
    ) -> main_models.ReadOutboundTaskCallListResponse:
        runtime = RuntimeOptions()
        return await self.read_outbound_task_call_list_with_options_async(request, runtime)
