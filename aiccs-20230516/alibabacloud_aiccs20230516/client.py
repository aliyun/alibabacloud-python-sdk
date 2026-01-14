# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aiccs20230516 import models as main_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('aiccs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_agent_with_options(
        self,
        request: main_models.AddAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.extension_pwd):
            query['ExtensionPwd'] = request.extension_pwd
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAgent',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_agent_with_options_async(
        self,
        request: main_models.AddAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.extension_pwd):
            query['ExtensionPwd'] = request.extension_pwd
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAgent',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_agent(
        self,
        request: main_models.AddAgentRequest,
    ) -> main_models.AddAgentResponse:
        runtime = RuntimeOptions()
        return self.add_agent_with_options(request, runtime)

    async def add_agent_async(
        self,
        request: main_models.AddAgentRequest,
    ) -> main_models.AddAgentResponse:
        runtime = RuntimeOptions()
        return await self.add_agent_with_options_async(request, runtime)

    def add_agent_group_with_options(
        self,
        request: main_models.AddAgentGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAgentGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_group_name):
            query['AgentGroupName'] = request.agent_group_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAgentGroup',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAgentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_agent_group_with_options_async(
        self,
        request: main_models.AddAgentGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAgentGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_group_name):
            query['AgentGroupName'] = request.agent_group_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAgentGroup',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAgentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_agent_group(
        self,
        request: main_models.AddAgentGroupRequest,
    ) -> main_models.AddAgentGroupResponse:
        runtime = RuntimeOptions()
        return self.add_agent_group_with_options(request, runtime)

    async def add_agent_group_async(
        self,
        request: main_models.AddAgentGroupRequest,
    ) -> main_models.AddAgentGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_agent_group_with_options_async(request, runtime)

    def add_blacklist_with_options(
        self,
        tmp_req: main_models.AddBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddBlacklistResponse:
        tmp_req.validate()
        request = main_models.AddBlacklistShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not DaraCore.is_null(request.expired_day):
            query['ExpiredDay'] = request.expired_day
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddBlacklist',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_blacklist_with_options_async(
        self,
        tmp_req: main_models.AddBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddBlacklistResponse:
        tmp_req.validate()
        request = main_models.AddBlacklistShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not DaraCore.is_null(request.expired_day):
            query['ExpiredDay'] = request.expired_day
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddBlacklist',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_blacklist(
        self,
        request: main_models.AddBlacklistRequest,
    ) -> main_models.AddBlacklistResponse:
        runtime = RuntimeOptions()
        return self.add_blacklist_with_options(request, runtime)

    async def add_blacklist_async(
        self,
        request: main_models.AddBlacklistRequest,
    ) -> main_models.AddBlacklistResponse:
        runtime = RuntimeOptions()
        return await self.add_blacklist_with_options_async(request, runtime)

    def add_task_with_options(
        self,
        tmp_req: main_models.AddTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTaskResponse:
        tmp_req.validate()
        request = main_models.AddTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.call_time_list):
            request.call_time_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_time_list, 'CallTimeList', 'json')
        if not DaraCore.is_null(tmp_req.repeat_reason):
            request.repeat_reason_shrink = Utils.array_to_string_with_specified_style(tmp_req.repeat_reason, 'RepeatReason', 'json')
        if not DaraCore.is_null(tmp_req.repeat_times):
            request.repeat_times_shrink = Utils.array_to_string_with_specified_style(tmp_req.repeat_times, 'RepeatTimes', 'json')
        if not DaraCore.is_null(tmp_req.send_sms_plan):
            request.send_sms_plan_shrink = Utils.array_to_string_with_specified_style(tmp_req.send_sms_plan, 'SendSmsPlan', 'json')
        query = {}
        if not DaraCore.is_null(request.call_time_list_shrink):
            query['CallTimeList'] = request.call_time_list_shrink
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.flash_sms_template_id):
            query['FlashSmsTemplateId'] = request.flash_sms_template_id
        if not DaraCore.is_null(request.flash_sms_type):
            query['FlashSmsType'] = request.flash_sms_type
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_sleep_val):
            query['PlaySleepVal'] = request.play_sleep_val
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.recall_type):
            query['RecallType'] = request.recall_type
        if not DaraCore.is_null(request.record_path):
            query['RecordPath'] = request.record_path
        if not DaraCore.is_null(request.repeat_count):
            query['RepeatCount'] = request.repeat_count
        if not DaraCore.is_null(request.repeat_interval):
            query['RepeatInterval'] = request.repeat_interval
        if not DaraCore.is_null(request.repeat_reason_shrink):
            query['RepeatReason'] = request.repeat_reason_shrink
        if not DaraCore.is_null(request.repeat_times_shrink):
            query['RepeatTimes'] = request.repeat_times_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.send_sms_plan_shrink):
            query['SendSmsPlan'] = request.send_sms_plan_shrink
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTask',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_task_with_options_async(
        self,
        tmp_req: main_models.AddTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTaskResponse:
        tmp_req.validate()
        request = main_models.AddTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.call_time_list):
            request.call_time_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_time_list, 'CallTimeList', 'json')
        if not DaraCore.is_null(tmp_req.repeat_reason):
            request.repeat_reason_shrink = Utils.array_to_string_with_specified_style(tmp_req.repeat_reason, 'RepeatReason', 'json')
        if not DaraCore.is_null(tmp_req.repeat_times):
            request.repeat_times_shrink = Utils.array_to_string_with_specified_style(tmp_req.repeat_times, 'RepeatTimes', 'json')
        if not DaraCore.is_null(tmp_req.send_sms_plan):
            request.send_sms_plan_shrink = Utils.array_to_string_with_specified_style(tmp_req.send_sms_plan, 'SendSmsPlan', 'json')
        query = {}
        if not DaraCore.is_null(request.call_time_list_shrink):
            query['CallTimeList'] = request.call_time_list_shrink
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.flash_sms_template_id):
            query['FlashSmsTemplateId'] = request.flash_sms_template_id
        if not DaraCore.is_null(request.flash_sms_type):
            query['FlashSmsType'] = request.flash_sms_type
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_sleep_val):
            query['PlaySleepVal'] = request.play_sleep_val
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.recall_type):
            query['RecallType'] = request.recall_type
        if not DaraCore.is_null(request.record_path):
            query['RecordPath'] = request.record_path
        if not DaraCore.is_null(request.repeat_count):
            query['RepeatCount'] = request.repeat_count
        if not DaraCore.is_null(request.repeat_interval):
            query['RepeatInterval'] = request.repeat_interval
        if not DaraCore.is_null(request.repeat_reason_shrink):
            query['RepeatReason'] = request.repeat_reason_shrink
        if not DaraCore.is_null(request.repeat_times_shrink):
            query['RepeatTimes'] = request.repeat_times_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.send_sms_plan_shrink):
            query['SendSmsPlan'] = request.send_sms_plan_shrink
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTask',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_task(
        self,
        request: main_models.AddTaskRequest,
    ) -> main_models.AddTaskResponse:
        runtime = RuntimeOptions()
        return self.add_task_with_options(request, runtime)

    async def add_task_async(
        self,
        request: main_models.AddTaskRequest,
    ) -> main_models.AddTaskResponse:
        runtime = RuntimeOptions()
        return await self.add_task_with_options_async(request, runtime)

    def agent_call_list_with_options(
        self,
        tmp_req: main_models.AgentCallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentCallListResponse:
        tmp_req.validate()
        request = main_models.AgentCallListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.number_md5s):
            request.number_md5s_shrink = Utils.array_to_string_with_specified_style(tmp_req.number_md5s, 'NumberMD5s', 'json')
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.call_date):
            query['CallDate'] = request.call_date
        if not DaraCore.is_null(request.end_call_date):
            query['EndCallDate'] = request.end_call_date
        if not DaraCore.is_null(request.number_md5s_shrink):
            query['NumberMD5s'] = request.number_md5s_shrink
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AgentCallList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AgentCallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def agent_call_list_with_options_async(
        self,
        tmp_req: main_models.AgentCallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentCallListResponse:
        tmp_req.validate()
        request = main_models.AgentCallListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.number_md5s):
            request.number_md5s_shrink = Utils.array_to_string_with_specified_style(tmp_req.number_md5s, 'NumberMD5s', 'json')
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.call_date):
            query['CallDate'] = request.call_date
        if not DaraCore.is_null(request.end_call_date):
            query['EndCallDate'] = request.end_call_date
        if not DaraCore.is_null(request.number_md5s_shrink):
            query['NumberMD5s'] = request.number_md5s_shrink
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AgentCallList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AgentCallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def agent_call_list(
        self,
        request: main_models.AgentCallListRequest,
    ) -> main_models.AgentCallListResponse:
        runtime = RuntimeOptions()
        return self.agent_call_list_with_options(request, runtime)

    async def agent_call_list_async(
        self,
        request: main_models.AgentCallListRequest,
    ) -> main_models.AgentCallListResponse:
        runtime = RuntimeOptions()
        return await self.agent_call_list_with_options_async(request, runtime)

    def agent_cancel_call_with_options(
        self,
        tmp_req: main_models.AgentCancelCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentCancelCallResponse:
        tmp_req.validate()
        request = main_models.AgentCancelCallShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AgentCancelCall',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AgentCancelCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def agent_cancel_call_with_options_async(
        self,
        tmp_req: main_models.AgentCancelCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentCancelCallResponse:
        tmp_req.validate()
        request = main_models.AgentCancelCallShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AgentCancelCall',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AgentCancelCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def agent_cancel_call(
        self,
        request: main_models.AgentCancelCallRequest,
    ) -> main_models.AgentCancelCallResponse:
        runtime = RuntimeOptions()
        return self.agent_cancel_call_with_options(request, runtime)

    async def agent_cancel_call_async(
        self,
        request: main_models.AgentCancelCallRequest,
    ) -> main_models.AgentCancelCallResponse:
        runtime = RuntimeOptions()
        return await self.agent_cancel_call_with_options_async(request, runtime)

    def agent_group_page_with_options(
        self,
        request: main_models.AgentGroupPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentGroupPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_group_id):
            query['AgentGroupId'] = request.agent_group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AgentGroupPage',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AgentGroupPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def agent_group_page_with_options_async(
        self,
        request: main_models.AgentGroupPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentGroupPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_group_id):
            query['AgentGroupId'] = request.agent_group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AgentGroupPage',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AgentGroupPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def agent_group_page(
        self,
        request: main_models.AgentGroupPageRequest,
    ) -> main_models.AgentGroupPageResponse:
        runtime = RuntimeOptions()
        return self.agent_group_page_with_options(request, runtime)

    async def agent_group_page_async(
        self,
        request: main_models.AgentGroupPageRequest,
    ) -> main_models.AgentGroupPageResponse:
        runtime = RuntimeOptions()
        return await self.agent_group_page_with_options_async(request, runtime)

    def agent_import_number_with_options(
        self,
        tmp_req: main_models.AgentImportNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentImportNumberResponse:
        tmp_req.validate()
        request = main_models.AgentImportNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.customers):
            request.customers_shrink = Utils.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.call_type):
            query['CallType'] = request.call_type
        if not DaraCore.is_null(request.customers_shrink):
            query['Customers'] = request.customers_shrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AgentImportNumber',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AgentImportNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def agent_import_number_with_options_async(
        self,
        tmp_req: main_models.AgentImportNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentImportNumberResponse:
        tmp_req.validate()
        request = main_models.AgentImportNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.customers):
            request.customers_shrink = Utils.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.call_type):
            query['CallType'] = request.call_type
        if not DaraCore.is_null(request.customers_shrink):
            query['Customers'] = request.customers_shrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AgentImportNumber',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AgentImportNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def agent_import_number(
        self,
        request: main_models.AgentImportNumberRequest,
    ) -> main_models.AgentImportNumberResponse:
        runtime = RuntimeOptions()
        return self.agent_import_number_with_options(request, runtime)

    async def agent_import_number_async(
        self,
        request: main_models.AgentImportNumberRequest,
    ) -> main_models.AgentImportNumberResponse:
        runtime = RuntimeOptions()
        return await self.agent_import_number_with_options_async(request, runtime)

    def agent_recover_call_with_options(
        self,
        tmp_req: main_models.AgentRecoverCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentRecoverCallResponse:
        tmp_req.validate()
        request = main_models.AgentRecoverCallShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.begin_import_time):
            query['BeginImportTime'] = request.begin_import_time
        if not DaraCore.is_null(request.end_import_time):
            query['EndImportTime'] = request.end_import_time
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AgentRecoverCall',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AgentRecoverCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def agent_recover_call_with_options_async(
        self,
        tmp_req: main_models.AgentRecoverCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentRecoverCallResponse:
        tmp_req.validate()
        request = main_models.AgentRecoverCallShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.begin_import_time):
            query['BeginImportTime'] = request.begin_import_time
        if not DaraCore.is_null(request.end_import_time):
            query['EndImportTime'] = request.end_import_time
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AgentRecoverCall',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AgentRecoverCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def agent_recover_call(
        self,
        request: main_models.AgentRecoverCallRequest,
    ) -> main_models.AgentRecoverCallResponse:
        runtime = RuntimeOptions()
        return self.agent_recover_call_with_options(request, runtime)

    async def agent_recover_call_async(
        self,
        request: main_models.AgentRecoverCallRequest,
    ) -> main_models.AgentRecoverCallResponse:
        runtime = RuntimeOptions()
        return await self.agent_recover_call_with_options_async(request, runtime)

    def call_chat_list_with_options(
        self,
        request: main_models.CallChatListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CallChatListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CallChatList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CallChatListResponse(),
            self.call_api(params, req, runtime)
        )

    async def call_chat_list_with_options_async(
        self,
        request: main_models.CallChatListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CallChatListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CallChatList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CallChatListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def call_chat_list(
        self,
        request: main_models.CallChatListRequest,
    ) -> main_models.CallChatListResponse:
        runtime = RuntimeOptions()
        return self.call_chat_list_with_options(request, runtime)

    async def call_chat_list_async(
        self,
        request: main_models.CallChatListRequest,
    ) -> main_models.CallChatListResponse:
        runtime = RuntimeOptions()
        return await self.call_chat_list_with_options_async(request, runtime)

    def call_number_detail_with_options(
        self,
        request: main_models.CallNumberDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CallNumberDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CallNumberDetail',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CallNumberDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def call_number_detail_with_options_async(
        self,
        request: main_models.CallNumberDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CallNumberDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CallNumberDetail',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CallNumberDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def call_number_detail(
        self,
        request: main_models.CallNumberDetailRequest,
    ) -> main_models.CallNumberDetailResponse:
        runtime = RuntimeOptions()
        return self.call_number_detail_with_options(request, runtime)

    async def call_number_detail_async(
        self,
        request: main_models.CallNumberDetailRequest,
    ) -> main_models.CallNumberDetailResponse:
        runtime = RuntimeOptions()
        return await self.call_number_detail_with_options_async(request, runtime)

    def details_with_options(
        self,
        tmp_req: main_models.DetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetailsResponse:
        tmp_req.validate()
        request = main_models.DetailsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['BatchId'] = request.batch_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.number_status):
            query['NumberStatus'] = request.number_status
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Details',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def details_with_options_async(
        self,
        tmp_req: main_models.DetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetailsResponse:
        tmp_req.validate()
        request = main_models.DetailsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['BatchId'] = request.batch_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.number_status):
            query['NumberStatus'] = request.number_status
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Details',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def details(
        self,
        request: main_models.DetailsRequest,
    ) -> main_models.DetailsResponse:
        runtime = RuntimeOptions()
        return self.details_with_options(request, runtime)

    async def details_async(
        self,
        request: main_models.DetailsRequest,
    ) -> main_models.DetailsResponse:
        runtime = RuntimeOptions()
        return await self.details_with_options_async(request, runtime)

    def edit_task_with_options(
        self,
        tmp_req: main_models.EditTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditTaskResponse:
        tmp_req.validate()
        request = main_models.EditTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.call_time_list):
            request.call_time_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_time_list, 'CallTimeList', 'json')
        if not DaraCore.is_null(tmp_req.repeat_reason):
            request.repeat_reason_shrink = Utils.array_to_string_with_specified_style(tmp_req.repeat_reason, 'RepeatReason', 'json')
        if not DaraCore.is_null(tmp_req.repeat_times):
            request.repeat_times_shrink = Utils.array_to_string_with_specified_style(tmp_req.repeat_times, 'RepeatTimes', 'json')
        if not DaraCore.is_null(tmp_req.send_sms_plan):
            request.send_sms_plan_shrink = Utils.array_to_string_with_specified_style(tmp_req.send_sms_plan, 'SendSmsPlan', 'json')
        query = {}
        if not DaraCore.is_null(request.call_time_list_shrink):
            query['CallTimeList'] = request.call_time_list_shrink
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.flash_sms_template_id):
            query['FlashSmsTemplateId'] = request.flash_sms_template_id
        if not DaraCore.is_null(request.flash_sms_type):
            query['FlashSmsType'] = request.flash_sms_type
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_sleep_val):
            query['PlaySleepVal'] = request.play_sleep_val
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.recall_type):
            query['RecallType'] = request.recall_type
        if not DaraCore.is_null(request.record_path):
            query['RecordPath'] = request.record_path
        if not DaraCore.is_null(request.repeat_count):
            query['RepeatCount'] = request.repeat_count
        if not DaraCore.is_null(request.repeat_interval):
            query['RepeatInterval'] = request.repeat_interval
        if not DaraCore.is_null(request.repeat_reason_shrink):
            query['RepeatReason'] = request.repeat_reason_shrink
        if not DaraCore.is_null(request.repeat_times_shrink):
            query['RepeatTimes'] = request.repeat_times_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.send_sms_plan_shrink):
            query['SendSmsPlan'] = request.send_sms_plan_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditTask',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_task_with_options_async(
        self,
        tmp_req: main_models.EditTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditTaskResponse:
        tmp_req.validate()
        request = main_models.EditTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.call_time_list):
            request.call_time_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_time_list, 'CallTimeList', 'json')
        if not DaraCore.is_null(tmp_req.repeat_reason):
            request.repeat_reason_shrink = Utils.array_to_string_with_specified_style(tmp_req.repeat_reason, 'RepeatReason', 'json')
        if not DaraCore.is_null(tmp_req.repeat_times):
            request.repeat_times_shrink = Utils.array_to_string_with_specified_style(tmp_req.repeat_times, 'RepeatTimes', 'json')
        if not DaraCore.is_null(tmp_req.send_sms_plan):
            request.send_sms_plan_shrink = Utils.array_to_string_with_specified_style(tmp_req.send_sms_plan, 'SendSmsPlan', 'json')
        query = {}
        if not DaraCore.is_null(request.call_time_list_shrink):
            query['CallTimeList'] = request.call_time_list_shrink
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.flash_sms_template_id):
            query['FlashSmsTemplateId'] = request.flash_sms_template_id
        if not DaraCore.is_null(request.flash_sms_type):
            query['FlashSmsType'] = request.flash_sms_type
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_sleep_val):
            query['PlaySleepVal'] = request.play_sleep_val
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.recall_type):
            query['RecallType'] = request.recall_type
        if not DaraCore.is_null(request.record_path):
            query['RecordPath'] = request.record_path
        if not DaraCore.is_null(request.repeat_count):
            query['RepeatCount'] = request.repeat_count
        if not DaraCore.is_null(request.repeat_interval):
            query['RepeatInterval'] = request.repeat_interval
        if not DaraCore.is_null(request.repeat_reason_shrink):
            query['RepeatReason'] = request.repeat_reason_shrink
        if not DaraCore.is_null(request.repeat_times_shrink):
            query['RepeatTimes'] = request.repeat_times_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.send_sms_plan_shrink):
            query['SendSmsPlan'] = request.send_sms_plan_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditTask',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_task(
        self,
        request: main_models.EditTaskRequest,
    ) -> main_models.EditTaskResponse:
        runtime = RuntimeOptions()
        return self.edit_task_with_options(request, runtime)

    async def edit_task_async(
        self,
        request: main_models.EditTaskRequest,
    ) -> main_models.EditTaskResponse:
        runtime = RuntimeOptions()
        return await self.edit_task_with_options_async(request, runtime)

    def import_number_with_options(
        self,
        tmp_req: main_models.ImportNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportNumberResponse:
        tmp_req.validate()
        request = main_models.ImportNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.customers):
            request.customers_shrink = Utils.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not DaraCore.is_null(request.customers_shrink):
            query['Customers'] = request.customers_shrink
        if not DaraCore.is_null(request.fail_return):
            query['FailReturn'] = request.fail_return
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportNumber',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_number_with_options_async(
        self,
        tmp_req: main_models.ImportNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportNumberResponse:
        tmp_req.validate()
        request = main_models.ImportNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.customers):
            request.customers_shrink = Utils.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not DaraCore.is_null(request.customers_shrink):
            query['Customers'] = request.customers_shrink
        if not DaraCore.is_null(request.fail_return):
            query['FailReturn'] = request.fail_return
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportNumber',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_number(
        self,
        request: main_models.ImportNumberRequest,
    ) -> main_models.ImportNumberResponse:
        runtime = RuntimeOptions()
        return self.import_number_with_options(request, runtime)

    async def import_number_async(
        self,
        request: main_models.ImportNumberRequest,
    ) -> main_models.ImportNumberResponse:
        runtime = RuntimeOptions()
        return await self.import_number_with_options_async(request, runtime)

    def import_number_v2with_options(
        self,
        tmp_req: main_models.ImportNumberV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.ImportNumberV2Response:
        tmp_req.validate()
        request = main_models.ImportNumberV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.customers):
            request.customers_shrink = Utils.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.customers_shrink):
            body['Customers'] = request.customers_shrink
        if not DaraCore.is_null(request.fail_return):
            body['FailReturn'] = request.fail_return
        if not DaraCore.is_null(request.out_id):
            body['OutId'] = request.out_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportNumberV2',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportNumberV2Response(),
            self.call_api(params, req, runtime)
        )

    async def import_number_v2with_options_async(
        self,
        tmp_req: main_models.ImportNumberV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.ImportNumberV2Response:
        tmp_req.validate()
        request = main_models.ImportNumberV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.customers):
            request.customers_shrink = Utils.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.customers_shrink):
            body['Customers'] = request.customers_shrink
        if not DaraCore.is_null(request.fail_return):
            body['FailReturn'] = request.fail_return
        if not DaraCore.is_null(request.out_id):
            body['OutId'] = request.out_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportNumberV2',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportNumberV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def import_number_v2(
        self,
        request: main_models.ImportNumberV2Request,
    ) -> main_models.ImportNumberV2Response:
        runtime = RuntimeOptions()
        return self.import_number_v2with_options(request, runtime)

    async def import_number_v2_async(
        self,
        request: main_models.ImportNumberV2Request,
    ) -> main_models.ImportNumberV2Response:
        runtime = RuntimeOptions()
        return await self.import_number_v2with_options_async(request, runtime)

    def join_agent_group_with_options(
        self,
        tmp_req: main_models.JoinAgentGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.JoinAgentGroupResponse:
        tmp_req.validate()
        request = main_models.JoinAgentGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_group_id):
            query['AgentGroupId'] = request.agent_group_id
        if not DaraCore.is_null(request.agent_ids_shrink):
            query['AgentIds'] = request.agent_ids_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'JoinAgentGroup',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.JoinAgentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_agent_group_with_options_async(
        self,
        tmp_req: main_models.JoinAgentGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.JoinAgentGroupResponse:
        tmp_req.validate()
        request = main_models.JoinAgentGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_group_id):
            query['AgentGroupId'] = request.agent_group_id
        if not DaraCore.is_null(request.agent_ids_shrink):
            query['AgentIds'] = request.agent_ids_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'JoinAgentGroup',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.JoinAgentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_agent_group(
        self,
        request: main_models.JoinAgentGroupRequest,
    ) -> main_models.JoinAgentGroupResponse:
        runtime = RuntimeOptions()
        return self.join_agent_group_with_options(request, runtime)

    async def join_agent_group_async(
        self,
        request: main_models.JoinAgentGroupRequest,
    ) -> main_models.JoinAgentGroupResponse:
        runtime = RuntimeOptions()
        return await self.join_agent_group_with_options_async(request, runtime)

    def page_with_options(
        self,
        tmp_req: main_models.PageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PageResponse:
        tmp_req.validate()
        request = main_models.PageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Page',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PageResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_with_options_async(
        self,
        tmp_req: main_models.PageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PageResponse:
        tmp_req.validate()
        request = main_models.PageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Page',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page(
        self,
        request: main_models.PageRequest,
    ) -> main_models.PageResponse:
        runtime = RuntimeOptions()
        return self.page_with_options(request, runtime)

    async def page_async(
        self,
        request: main_models.PageRequest,
    ) -> main_models.PageResponse:
        runtime = RuntimeOptions()
        return await self.page_with_options_async(request, runtime)

    def query_agent_info_with_options(
        self,
        request: main_models.QueryAgentInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAgentInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAgentInfo',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAgentInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_agent_info_with_options_async(
        self,
        request: main_models.QueryAgentInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAgentInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAgentInfo',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAgentInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_agent_info(
        self,
        request: main_models.QueryAgentInfoRequest,
    ) -> main_models.QueryAgentInfoResponse:
        runtime = RuntimeOptions()
        return self.query_agent_info_with_options(request, runtime)

    async def query_agent_info_async(
        self,
        request: main_models.QueryAgentInfoRequest,
    ) -> main_models.QueryAgentInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_agent_info_with_options_async(request, runtime)

    def quick_add_task_with_options(
        self,
        tmp_req: main_models.QuickAddTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuickAddTaskResponse:
        tmp_req.validate()
        request = main_models.QuickAddTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.call_time_list):
            request.call_time_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_time_list, 'CallTimeList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_group_id):
            query['AgentGroupId'] = request.agent_group_id
        if not DaraCore.is_null(request.call_time_list_shrink):
            query['CallTimeList'] = request.call_time_list_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.reference_task_id):
            query['ReferenceTaskId'] = request.reference_task_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sms_template_id):
            query['SmsTemplateId'] = request.sms_template_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuickAddTask',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuickAddTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def quick_add_task_with_options_async(
        self,
        tmp_req: main_models.QuickAddTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuickAddTaskResponse:
        tmp_req.validate()
        request = main_models.QuickAddTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.call_time_list):
            request.call_time_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_time_list, 'CallTimeList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_group_id):
            query['AgentGroupId'] = request.agent_group_id
        if not DaraCore.is_null(request.call_time_list_shrink):
            query['CallTimeList'] = request.call_time_list_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.reference_task_id):
            query['ReferenceTaskId'] = request.reference_task_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sms_template_id):
            query['SmsTemplateId'] = request.sms_template_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuickAddTask',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuickAddTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def quick_add_task(
        self,
        request: main_models.QuickAddTaskRequest,
    ) -> main_models.QuickAddTaskResponse:
        runtime = RuntimeOptions()
        return self.quick_add_task_with_options(request, runtime)

    async def quick_add_task_async(
        self,
        request: main_models.QuickAddTaskRequest,
    ) -> main_models.QuickAddTaskResponse:
        runtime = RuntimeOptions()
        return await self.quick_add_task_with_options_async(request, runtime)

    def quit_agent_group_with_options(
        self,
        tmp_req: main_models.QuitAgentGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuitAgentGroupResponse:
        tmp_req.validate()
        request = main_models.QuitAgentGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_group_id):
            query['AgentGroupId'] = request.agent_group_id
        if not DaraCore.is_null(request.agent_ids_shrink):
            query['AgentIds'] = request.agent_ids_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuitAgentGroup',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuitAgentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def quit_agent_group_with_options_async(
        self,
        tmp_req: main_models.QuitAgentGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuitAgentGroupResponse:
        tmp_req.validate()
        request = main_models.QuitAgentGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_group_id):
            query['AgentGroupId'] = request.agent_group_id
        if not DaraCore.is_null(request.agent_ids_shrink):
            query['AgentIds'] = request.agent_ids_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuitAgentGroup',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuitAgentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def quit_agent_group(
        self,
        request: main_models.QuitAgentGroupRequest,
    ) -> main_models.QuitAgentGroupResponse:
        runtime = RuntimeOptions()
        return self.quit_agent_group_with_options(request, runtime)

    async def quit_agent_group_async(
        self,
        request: main_models.QuitAgentGroupRequest,
    ) -> main_models.QuitAgentGroupResponse:
        runtime = RuntimeOptions()
        return await self.quit_agent_group_with_options_async(request, runtime)

    def sms_template_create_with_options(
        self,
        request: main_models.SmsTemplateCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmsTemplateCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign):
            query['Sign'] = request.sign
        if not DaraCore.is_null(request.sms_type):
            query['SmsType'] = request.sms_type
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmsTemplateCreate',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmsTemplateCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def sms_template_create_with_options_async(
        self,
        request: main_models.SmsTemplateCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmsTemplateCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign):
            query['Sign'] = request.sign
        if not DaraCore.is_null(request.sms_type):
            query['SmsType'] = request.sms_type
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmsTemplateCreate',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmsTemplateCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sms_template_create(
        self,
        request: main_models.SmsTemplateCreateRequest,
    ) -> main_models.SmsTemplateCreateResponse:
        runtime = RuntimeOptions()
        return self.sms_template_create_with_options(request, runtime)

    async def sms_template_create_async(
        self,
        request: main_models.SmsTemplateCreateRequest,
    ) -> main_models.SmsTemplateCreateResponse:
        runtime = RuntimeOptions()
        return await self.sms_template_create_with_options_async(request, runtime)

    def sms_template_page_list_with_options(
        self,
        request: main_models.SmsTemplatePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmsTemplatePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign):
            query['Sign'] = request.sign
        if not DaraCore.is_null(request.sms_type):
            query['SmsType'] = request.sms_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmsTemplatePageList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmsTemplatePageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def sms_template_page_list_with_options_async(
        self,
        request: main_models.SmsTemplatePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmsTemplatePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign):
            query['Sign'] = request.sign
        if not DaraCore.is_null(request.sms_type):
            query['SmsType'] = request.sms_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmsTemplatePageList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmsTemplatePageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sms_template_page_list(
        self,
        request: main_models.SmsTemplatePageListRequest,
    ) -> main_models.SmsTemplatePageListResponse:
        runtime = RuntimeOptions()
        return self.sms_template_page_list_with_options(request, runtime)

    async def sms_template_page_list_async(
        self,
        request: main_models.SmsTemplatePageListRequest,
    ) -> main_models.SmsTemplatePageListResponse:
        runtime = RuntimeOptions()
        return await self.sms_template_page_list_with_options_async(request, runtime)

    def task_call_chats_with_options(
        self,
        request: main_models.TaskCallChatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskCallChatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskCallChats',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskCallChatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_call_chats_with_options_async(
        self,
        request: main_models.TaskCallChatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskCallChatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskCallChats',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskCallChatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_call_chats(
        self,
        request: main_models.TaskCallChatsRequest,
    ) -> main_models.TaskCallChatsResponse:
        runtime = RuntimeOptions()
        return self.task_call_chats_with_options(request, runtime)

    async def task_call_chats_async(
        self,
        request: main_models.TaskCallChatsRequest,
    ) -> main_models.TaskCallChatsResponse:
        runtime = RuntimeOptions()
        return await self.task_call_chats_with_options_async(request, runtime)

    def task_call_info_with_options(
        self,
        request: main_models.TaskCallInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskCallInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskCallInfo',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskCallInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_call_info_with_options_async(
        self,
        request: main_models.TaskCallInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskCallInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskCallInfo',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskCallInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_call_info(
        self,
        request: main_models.TaskCallInfoRequest,
    ) -> main_models.TaskCallInfoResponse:
        runtime = RuntimeOptions()
        return self.task_call_info_with_options(request, runtime)

    async def task_call_info_async(
        self,
        request: main_models.TaskCallInfoRequest,
    ) -> main_models.TaskCallInfoResponse:
        runtime = RuntimeOptions()
        return await self.task_call_info_with_options_async(request, runtime)

    def task_call_list_with_options(
        self,
        tmp_req: main_models.TaskCallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskCallListResponse:
        tmp_req.validate()
        request = main_models.TaskCallListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intent_tags):
            request.intent_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.intent_tags, 'IntentTags', 'json')
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['BatchId'] = request.batch_id
        if not DaraCore.is_null(request.call_date):
            query['CallDate'] = request.call_date
        if not DaraCore.is_null(request.end_call_date):
            query['EndCallDate'] = request.end_call_date
        if not DaraCore.is_null(request.intent_tags_shrink):
            query['IntentTags'] = request.intent_tags_shrink
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskCallList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskCallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_call_list_with_options_async(
        self,
        tmp_req: main_models.TaskCallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskCallListResponse:
        tmp_req.validate()
        request = main_models.TaskCallListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intent_tags):
            request.intent_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.intent_tags, 'IntentTags', 'json')
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['BatchId'] = request.batch_id
        if not DaraCore.is_null(request.call_date):
            query['CallDate'] = request.call_date
        if not DaraCore.is_null(request.end_call_date):
            query['EndCallDate'] = request.end_call_date
        if not DaraCore.is_null(request.intent_tags_shrink):
            query['IntentTags'] = request.intent_tags_shrink
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskCallList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskCallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_call_list(
        self,
        request: main_models.TaskCallListRequest,
    ) -> main_models.TaskCallListResponse:
        runtime = RuntimeOptions()
        return self.task_call_list_with_options(request, runtime)

    async def task_call_list_async(
        self,
        request: main_models.TaskCallListRequest,
    ) -> main_models.TaskCallListResponse:
        runtime = RuntimeOptions()
        return await self.task_call_list_with_options_async(request, runtime)

    def task_cancel_call_with_options(
        self,
        tmp_req: main_models.TaskCancelCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskCancelCallResponse:
        tmp_req.validate()
        request = main_models.TaskCancelCallShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskCancelCall',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskCancelCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_cancel_call_with_options_async(
        self,
        tmp_req: main_models.TaskCancelCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskCancelCallResponse:
        tmp_req.validate()
        request = main_models.TaskCancelCallShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskCancelCall',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskCancelCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_cancel_call(
        self,
        request: main_models.TaskCancelCallRequest,
    ) -> main_models.TaskCancelCallResponse:
        runtime = RuntimeOptions()
        return self.task_cancel_call_with_options(request, runtime)

    async def task_cancel_call_async(
        self,
        request: main_models.TaskCancelCallRequest,
    ) -> main_models.TaskCancelCallResponse:
        runtime = RuntimeOptions()
        return await self.task_cancel_call_with_options_async(request, runtime)

    def task_list_with_options(
        self,
        request: main_models.TaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.last_call_time):
            query['LastCallTime'] = request.last_call_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_list_with_options_async(
        self,
        request: main_models.TaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.last_call_time):
            query['LastCallTime'] = request.last_call_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_list(
        self,
        request: main_models.TaskListRequest,
    ) -> main_models.TaskListResponse:
        runtime = RuntimeOptions()
        return self.task_list_with_options(request, runtime)

    async def task_list_async(
        self,
        request: main_models.TaskListRequest,
    ) -> main_models.TaskListResponse:
        runtime = RuntimeOptions()
        return await self.task_list_with_options_async(request, runtime)

    def task_recover_call_with_options(
        self,
        tmp_req: main_models.TaskRecoverCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskRecoverCallResponse:
        tmp_req.validate()
        request = main_models.TaskRecoverCallShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.begin_import_time):
            query['BeginImportTime'] = request.begin_import_time
        if not DaraCore.is_null(request.end_import_time):
            query['EndImportTime'] = request.end_import_time
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskRecoverCall',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskRecoverCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_recover_call_with_options_async(
        self,
        tmp_req: main_models.TaskRecoverCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskRecoverCallResponse:
        tmp_req.validate()
        request = main_models.TaskRecoverCallShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.numbers):
            request.numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.begin_import_time):
            query['BeginImportTime'] = request.begin_import_time
        if not DaraCore.is_null(request.end_import_time):
            query['EndImportTime'] = request.end_import_time
        if not DaraCore.is_null(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskRecoverCall',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskRecoverCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_recover_call(
        self,
        request: main_models.TaskRecoverCallRequest,
    ) -> main_models.TaskRecoverCallResponse:
        runtime = RuntimeOptions()
        return self.task_recover_call_with_options(request, runtime)

    async def task_recover_call_async(
        self,
        request: main_models.TaskRecoverCallRequest,
    ) -> main_models.TaskRecoverCallResponse:
        runtime = RuntimeOptions()
        return await self.task_recover_call_with_options_async(request, runtime)

    def template_list_with_options(
        self,
        request: main_models.TemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TemplateList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def template_list_with_options_async(
        self,
        request: main_models.TemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TemplateList',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def template_list(
        self,
        request: main_models.TemplateListRequest,
    ) -> main_models.TemplateListResponse:
        runtime = RuntimeOptions()
        return self.template_list_with_options(request, runtime)

    async def template_list_async(
        self,
        request: main_models.TemplateListRequest,
    ) -> main_models.TemplateListResponse:
        runtime = RuntimeOptions()
        return await self.template_list_with_options_async(request, runtime)

    def update_agent_status_with_options(
        self,
        request: main_models.UpdateAgentStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_status):
            query['AgentStatus'] = request.agent_status
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentStatus',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_status_with_options_async(
        self,
        request: main_models.UpdateAgentStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_status):
            query['AgentStatus'] = request.agent_status
        if not DaraCore.is_null(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentStatus',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_status(
        self,
        request: main_models.UpdateAgentStatusRequest,
    ) -> main_models.UpdateAgentStatusResponse:
        runtime = RuntimeOptions()
        return self.update_agent_status_with_options(request, runtime)

    async def update_agent_status_async(
        self,
        request: main_models.UpdateAgentStatusRequest,
    ) -> main_models.UpdateAgentStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_agent_status_with_options_async(request, runtime)

    def update_task_customer_with_options(
        self,
        tmp_req: main_models.UpdateTaskCustomerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskCustomerResponse:
        tmp_req.validate()
        request = main_models.UpdateTaskCustomerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.customers):
            request.customers_shrink = Utils.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not DaraCore.is_null(request.customers_shrink):
            query['Customers'] = request.customers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTaskCustomer',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_customer_with_options_async(
        self,
        tmp_req: main_models.UpdateTaskCustomerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskCustomerResponse:
        tmp_req.validate()
        request = main_models.UpdateTaskCustomerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.customers):
            request.customers_shrink = Utils.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not DaraCore.is_null(request.customers_shrink):
            query['Customers'] = request.customers_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTaskCustomer',
            version = '2023-05-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskCustomerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_customer(
        self,
        request: main_models.UpdateTaskCustomerRequest,
    ) -> main_models.UpdateTaskCustomerResponse:
        runtime = RuntimeOptions()
        return self.update_task_customer_with_options(request, runtime)

    async def update_task_customer_async(
        self,
        request: main_models.UpdateTaskCustomerRequest,
    ) -> main_models.UpdateTaskCustomerResponse:
        runtime = RuntimeOptions()
        return await self.update_task_customer_with_options_async(request, runtime)
