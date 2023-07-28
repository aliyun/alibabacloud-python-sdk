# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aiccs20230516 import models as aiccs_20230516_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_blacklist_with_options(
        self,
        tmp_req: aiccs_20230516_models.AddBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.AddBlacklistResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.AddBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.expired_day):
            query['ExpiredDay'] = request.expired_day
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBlacklist',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.AddBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_blacklist_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.AddBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.AddBlacklistResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.AddBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.expired_day):
            query['ExpiredDay'] = request.expired_day
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBlacklist',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.AddBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_blacklist(
        self,
        request: aiccs_20230516_models.AddBlacklistRequest,
    ) -> aiccs_20230516_models.AddBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_blacklist_with_options(request, runtime)

    async def add_blacklist_async(
        self,
        request: aiccs_20230516_models.AddBlacklistRequest,
    ) -> aiccs_20230516_models.AddBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_blacklist_with_options_async(request, runtime)

    def add_task_with_options(
        self,
        tmp_req: aiccs_20230516_models.AddTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.AddTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.AddTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.call_time_list):
            request.call_time_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_time_list, 'CallTimeList', 'json')
        if not UtilClient.is_unset(tmp_req.repeat_reason):
            request.repeat_reason_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_reason, 'RepeatReason', 'json')
        if not UtilClient.is_unset(tmp_req.repeat_times):
            request.repeat_times_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_times, 'RepeatTimes', 'json')
        if not UtilClient.is_unset(tmp_req.send_sms_plan):
            request.send_sms_plan_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.send_sms_plan, 'SendSmsPlan', 'json')
        query = {}
        if not UtilClient.is_unset(request.call_time_list_shrink):
            query['CallTimeList'] = request.call_time_list_shrink
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_sleep_val):
            query['PlaySleepVal'] = request.play_sleep_val
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.recall_type):
            query['RecallType'] = request.recall_type
        if not UtilClient.is_unset(request.record_path):
            query['RecordPath'] = request.record_path
        if not UtilClient.is_unset(request.repeat_count):
            query['RepeatCount'] = request.repeat_count
        if not UtilClient.is_unset(request.repeat_interval):
            query['RepeatInterval'] = request.repeat_interval
        if not UtilClient.is_unset(request.repeat_reason_shrink):
            query['RepeatReason'] = request.repeat_reason_shrink
        if not UtilClient.is_unset(request.repeat_times_shrink):
            query['RepeatTimes'] = request.repeat_times_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_sms_plan_shrink):
            query['SendSmsPlan'] = request.send_sms_plan_shrink
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTask',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.AddTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_task_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.AddTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.AddTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.AddTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.call_time_list):
            request.call_time_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_time_list, 'CallTimeList', 'json')
        if not UtilClient.is_unset(tmp_req.repeat_reason):
            request.repeat_reason_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_reason, 'RepeatReason', 'json')
        if not UtilClient.is_unset(tmp_req.repeat_times):
            request.repeat_times_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_times, 'RepeatTimes', 'json')
        if not UtilClient.is_unset(tmp_req.send_sms_plan):
            request.send_sms_plan_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.send_sms_plan, 'SendSmsPlan', 'json')
        query = {}
        if not UtilClient.is_unset(request.call_time_list_shrink):
            query['CallTimeList'] = request.call_time_list_shrink
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_sleep_val):
            query['PlaySleepVal'] = request.play_sleep_val
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.recall_type):
            query['RecallType'] = request.recall_type
        if not UtilClient.is_unset(request.record_path):
            query['RecordPath'] = request.record_path
        if not UtilClient.is_unset(request.repeat_count):
            query['RepeatCount'] = request.repeat_count
        if not UtilClient.is_unset(request.repeat_interval):
            query['RepeatInterval'] = request.repeat_interval
        if not UtilClient.is_unset(request.repeat_reason_shrink):
            query['RepeatReason'] = request.repeat_reason_shrink
        if not UtilClient.is_unset(request.repeat_times_shrink):
            query['RepeatTimes'] = request.repeat_times_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_sms_plan_shrink):
            query['SendSmsPlan'] = request.send_sms_plan_shrink
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTask',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.AddTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_task(
        self,
        request: aiccs_20230516_models.AddTaskRequest,
    ) -> aiccs_20230516_models.AddTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_task_with_options(request, runtime)

    async def add_task_async(
        self,
        request: aiccs_20230516_models.AddTaskRequest,
    ) -> aiccs_20230516_models.AddTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_task_with_options_async(request, runtime)

    def agent_cancel_call_with_options(
        self,
        tmp_req: aiccs_20230516_models.AgentCancelCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.AgentCancelCallResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.AgentCancelCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AgentCancelCall',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.AgentCancelCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def agent_cancel_call_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.AgentCancelCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.AgentCancelCallResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.AgentCancelCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AgentCancelCall',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.AgentCancelCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def agent_cancel_call(
        self,
        request: aiccs_20230516_models.AgentCancelCallRequest,
    ) -> aiccs_20230516_models.AgentCancelCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.agent_cancel_call_with_options(request, runtime)

    async def agent_cancel_call_async(
        self,
        request: aiccs_20230516_models.AgentCancelCallRequest,
    ) -> aiccs_20230516_models.AgentCancelCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.agent_cancel_call_with_options_async(request, runtime)

    def agent_recover_call_with_options(
        self,
        tmp_req: aiccs_20230516_models.AgentRecoverCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.AgentRecoverCallResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.AgentRecoverCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not UtilClient.is_unset(request.begin_import_time):
            query['BeginImportTime'] = request.begin_import_time
        if not UtilClient.is_unset(request.end_import_time):
            query['EndImportTime'] = request.end_import_time
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AgentRecoverCall',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.AgentRecoverCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def agent_recover_call_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.AgentRecoverCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.AgentRecoverCallResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.AgentRecoverCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not UtilClient.is_unset(request.begin_import_time):
            query['BeginImportTime'] = request.begin_import_time
        if not UtilClient.is_unset(request.end_import_time):
            query['EndImportTime'] = request.end_import_time
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AgentRecoverCall',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.AgentRecoverCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def agent_recover_call(
        self,
        request: aiccs_20230516_models.AgentRecoverCallRequest,
    ) -> aiccs_20230516_models.AgentRecoverCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.agent_recover_call_with_options(request, runtime)

    async def agent_recover_call_async(
        self,
        request: aiccs_20230516_models.AgentRecoverCallRequest,
    ) -> aiccs_20230516_models.AgentRecoverCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.agent_recover_call_with_options_async(request, runtime)

    def details_with_options(
        self,
        tmp_req: aiccs_20230516_models.DetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.DetailsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.DetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.number_status):
            query['NumberStatus'] = request.number_status
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Details',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.DetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def details_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.DetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.DetailsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.DetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.number_status):
            query['NumberStatus'] = request.number_status
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Details',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.DetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def details(
        self,
        request: aiccs_20230516_models.DetailsRequest,
    ) -> aiccs_20230516_models.DetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.details_with_options(request, runtime)

    async def details_async(
        self,
        request: aiccs_20230516_models.DetailsRequest,
    ) -> aiccs_20230516_models.DetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.details_with_options_async(request, runtime)

    def edit_task_with_options(
        self,
        tmp_req: aiccs_20230516_models.EditTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.EditTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.EditTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.call_time_list):
            request.call_time_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_time_list, 'CallTimeList', 'json')
        if not UtilClient.is_unset(tmp_req.repeat_reason):
            request.repeat_reason_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_reason, 'RepeatReason', 'json')
        if not UtilClient.is_unset(tmp_req.repeat_times):
            request.repeat_times_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_times, 'RepeatTimes', 'json')
        if not UtilClient.is_unset(tmp_req.send_sms_plan):
            request.send_sms_plan_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.send_sms_plan, 'SendSmsPlan', 'json')
        query = {}
        if not UtilClient.is_unset(request.call_time_list_shrink):
            query['CallTimeList'] = request.call_time_list_shrink
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_sleep_val):
            query['PlaySleepVal'] = request.play_sleep_val
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.recall_type):
            query['RecallType'] = request.recall_type
        if not UtilClient.is_unset(request.record_path):
            query['RecordPath'] = request.record_path
        if not UtilClient.is_unset(request.repeat_count):
            query['RepeatCount'] = request.repeat_count
        if not UtilClient.is_unset(request.repeat_interval):
            query['RepeatInterval'] = request.repeat_interval
        if not UtilClient.is_unset(request.repeat_reason_shrink):
            query['RepeatReason'] = request.repeat_reason_shrink
        if not UtilClient.is_unset(request.repeat_times_shrink):
            query['RepeatTimes'] = request.repeat_times_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_sms_plan_shrink):
            query['SendSmsPlan'] = request.send_sms_plan_shrink
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditTask',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.EditTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_task_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.EditTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.EditTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.EditTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.call_time_list):
            request.call_time_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_time_list, 'CallTimeList', 'json')
        if not UtilClient.is_unset(tmp_req.repeat_reason):
            request.repeat_reason_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_reason, 'RepeatReason', 'json')
        if not UtilClient.is_unset(tmp_req.repeat_times):
            request.repeat_times_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_times, 'RepeatTimes', 'json')
        if not UtilClient.is_unset(tmp_req.send_sms_plan):
            request.send_sms_plan_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.send_sms_plan, 'SendSmsPlan', 'json')
        query = {}
        if not UtilClient.is_unset(request.call_time_list_shrink):
            query['CallTimeList'] = request.call_time_list_shrink
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_sleep_val):
            query['PlaySleepVal'] = request.play_sleep_val
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.recall_type):
            query['RecallType'] = request.recall_type
        if not UtilClient.is_unset(request.record_path):
            query['RecordPath'] = request.record_path
        if not UtilClient.is_unset(request.repeat_count):
            query['RepeatCount'] = request.repeat_count
        if not UtilClient.is_unset(request.repeat_interval):
            query['RepeatInterval'] = request.repeat_interval
        if not UtilClient.is_unset(request.repeat_reason_shrink):
            query['RepeatReason'] = request.repeat_reason_shrink
        if not UtilClient.is_unset(request.repeat_times_shrink):
            query['RepeatTimes'] = request.repeat_times_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_sms_plan_shrink):
            query['SendSmsPlan'] = request.send_sms_plan_shrink
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditTask',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.EditTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_task(
        self,
        request: aiccs_20230516_models.EditTaskRequest,
    ) -> aiccs_20230516_models.EditTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_task_with_options(request, runtime)

    async def edit_task_async(
        self,
        request: aiccs_20230516_models.EditTaskRequest,
    ) -> aiccs_20230516_models.EditTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_task_with_options_async(request, runtime)

    def import_number_with_options(
        self,
        tmp_req: aiccs_20230516_models.ImportNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.ImportNumberResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.ImportNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.customers):
            request.customers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not UtilClient.is_unset(request.customers_shrink):
            query['Customers'] = request.customers_shrink
        if not UtilClient.is_unset(request.fail_return):
            query['FailReturn'] = request.fail_return
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportNumber',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.ImportNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_number_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.ImportNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.ImportNumberResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.ImportNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.customers):
            request.customers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not UtilClient.is_unset(request.customers_shrink):
            query['Customers'] = request.customers_shrink
        if not UtilClient.is_unset(request.fail_return):
            query['FailReturn'] = request.fail_return
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportNumber',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.ImportNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_number(
        self,
        request: aiccs_20230516_models.ImportNumberRequest,
    ) -> aiccs_20230516_models.ImportNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_number_with_options(request, runtime)

    async def import_number_async(
        self,
        request: aiccs_20230516_models.ImportNumberRequest,
    ) -> aiccs_20230516_models.ImportNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_number_with_options_async(request, runtime)

    def page_with_options(
        self,
        tmp_req: aiccs_20230516_models.PageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.PageResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.PageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Page',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.PageResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.PageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.PageResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.PageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Page',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.PageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page(
        self,
        request: aiccs_20230516_models.PageRequest,
    ) -> aiccs_20230516_models.PageResponse:
        runtime = util_models.RuntimeOptions()
        return self.page_with_options(request, runtime)

    async def page_async(
        self,
        request: aiccs_20230516_models.PageRequest,
    ) -> aiccs_20230516_models.PageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.page_with_options_async(request, runtime)

    def sms_template_create_with_options(
        self,
        request: aiccs_20230516_models.SmsTemplateCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.SmsTemplateCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign):
            query['Sign'] = request.sign
        if not UtilClient.is_unset(request.sms_type):
            query['SmsType'] = request.sms_type
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SmsTemplateCreate',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.SmsTemplateCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def sms_template_create_with_options_async(
        self,
        request: aiccs_20230516_models.SmsTemplateCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.SmsTemplateCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign):
            query['Sign'] = request.sign
        if not UtilClient.is_unset(request.sms_type):
            query['SmsType'] = request.sms_type
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SmsTemplateCreate',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.SmsTemplateCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sms_template_create(
        self,
        request: aiccs_20230516_models.SmsTemplateCreateRequest,
    ) -> aiccs_20230516_models.SmsTemplateCreateResponse:
        runtime = util_models.RuntimeOptions()
        return self.sms_template_create_with_options(request, runtime)

    async def sms_template_create_async(
        self,
        request: aiccs_20230516_models.SmsTemplateCreateRequest,
    ) -> aiccs_20230516_models.SmsTemplateCreateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sms_template_create_with_options_async(request, runtime)

    def sms_template_page_list_with_options(
        self,
        request: aiccs_20230516_models.SmsTemplatePageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.SmsTemplatePageListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign):
            query['Sign'] = request.sign
        if not UtilClient.is_unset(request.sms_type):
            query['SmsType'] = request.sms_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SmsTemplatePageList',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.SmsTemplatePageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def sms_template_page_list_with_options_async(
        self,
        request: aiccs_20230516_models.SmsTemplatePageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.SmsTemplatePageListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign):
            query['Sign'] = request.sign
        if not UtilClient.is_unset(request.sms_type):
            query['SmsType'] = request.sms_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SmsTemplatePageList',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.SmsTemplatePageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sms_template_page_list(
        self,
        request: aiccs_20230516_models.SmsTemplatePageListRequest,
    ) -> aiccs_20230516_models.SmsTemplatePageListResponse:
        runtime = util_models.RuntimeOptions()
        return self.sms_template_page_list_with_options(request, runtime)

    async def sms_template_page_list_async(
        self,
        request: aiccs_20230516_models.SmsTemplatePageListRequest,
    ) -> aiccs_20230516_models.SmsTemplatePageListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sms_template_page_list_with_options_async(request, runtime)

    def task_call_chats_with_options(
        self,
        request: aiccs_20230516_models.TaskCallChatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskCallChatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskCallChats',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskCallChatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_call_chats_with_options_async(
        self,
        request: aiccs_20230516_models.TaskCallChatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskCallChatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskCallChats',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskCallChatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_call_chats(
        self,
        request: aiccs_20230516_models.TaskCallChatsRequest,
    ) -> aiccs_20230516_models.TaskCallChatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.task_call_chats_with_options(request, runtime)

    async def task_call_chats_async(
        self,
        request: aiccs_20230516_models.TaskCallChatsRequest,
    ) -> aiccs_20230516_models.TaskCallChatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.task_call_chats_with_options_async(request, runtime)

    def task_call_info_with_options(
        self,
        request: aiccs_20230516_models.TaskCallInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskCallInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskCallInfo',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskCallInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_call_info_with_options_async(
        self,
        request: aiccs_20230516_models.TaskCallInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskCallInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskCallInfo',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskCallInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_call_info(
        self,
        request: aiccs_20230516_models.TaskCallInfoRequest,
    ) -> aiccs_20230516_models.TaskCallInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.task_call_info_with_options(request, runtime)

    async def task_call_info_async(
        self,
        request: aiccs_20230516_models.TaskCallInfoRequest,
    ) -> aiccs_20230516_models.TaskCallInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.task_call_info_with_options_async(request, runtime)

    def task_call_list_with_options(
        self,
        tmp_req: aiccs_20230516_models.TaskCallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskCallListResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.TaskCallListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_tags):
            request.intent_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intent_tags, 'IntentTags', 'json')
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.end_call_date):
            query['EndCallDate'] = request.end_call_date
        if not UtilClient.is_unset(request.intent_tags_shrink):
            query['IntentTags'] = request.intent_tags_shrink
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskCallList',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskCallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_call_list_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.TaskCallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskCallListResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.TaskCallListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_tags):
            request.intent_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intent_tags, 'IntentTags', 'json')
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.end_call_date):
            query['EndCallDate'] = request.end_call_date
        if not UtilClient.is_unset(request.intent_tags_shrink):
            query['IntentTags'] = request.intent_tags_shrink
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskCallList',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskCallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_call_list(
        self,
        request: aiccs_20230516_models.TaskCallListRequest,
    ) -> aiccs_20230516_models.TaskCallListResponse:
        runtime = util_models.RuntimeOptions()
        return self.task_call_list_with_options(request, runtime)

    async def task_call_list_async(
        self,
        request: aiccs_20230516_models.TaskCallListRequest,
    ) -> aiccs_20230516_models.TaskCallListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.task_call_list_with_options_async(request, runtime)

    def task_cancel_call_with_options(
        self,
        tmp_req: aiccs_20230516_models.TaskCancelCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskCancelCallResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.TaskCancelCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskCancelCall',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskCancelCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_cancel_call_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.TaskCancelCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskCancelCallResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.TaskCancelCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskCancelCall',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskCancelCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_cancel_call(
        self,
        request: aiccs_20230516_models.TaskCancelCallRequest,
    ) -> aiccs_20230516_models.TaskCancelCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.task_cancel_call_with_options(request, runtime)

    async def task_cancel_call_async(
        self,
        request: aiccs_20230516_models.TaskCancelCallRequest,
    ) -> aiccs_20230516_models.TaskCancelCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.task_cancel_call_with_options_async(request, runtime)

    def task_list_with_options(
        self,
        request: aiccs_20230516_models.TaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.last_call_time):
            query['LastCallTime'] = request.last_call_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskList',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_list_with_options_async(
        self,
        request: aiccs_20230516_models.TaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.last_call_time):
            query['LastCallTime'] = request.last_call_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskList',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_list(
        self,
        request: aiccs_20230516_models.TaskListRequest,
    ) -> aiccs_20230516_models.TaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.task_list_with_options(request, runtime)

    async def task_list_async(
        self,
        request: aiccs_20230516_models.TaskListRequest,
    ) -> aiccs_20230516_models.TaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.task_list_with_options_async(request, runtime)

    def task_recover_call_with_options(
        self,
        tmp_req: aiccs_20230516_models.TaskRecoverCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskRecoverCallResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.TaskRecoverCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.begin_import_time):
            query['BeginImportTime'] = request.begin_import_time
        if not UtilClient.is_unset(request.end_import_time):
            query['EndImportTime'] = request.end_import_time
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskRecoverCall',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskRecoverCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_recover_call_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.TaskRecoverCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TaskRecoverCallResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.TaskRecoverCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.numbers):
            request.numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.numbers, 'Numbers', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.begin_import_time):
            query['BeginImportTime'] = request.begin_import_time
        if not UtilClient.is_unset(request.end_import_time):
            query['EndImportTime'] = request.end_import_time
        if not UtilClient.is_unset(request.numbers_shrink):
            query['Numbers'] = request.numbers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskRecoverCall',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TaskRecoverCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_recover_call(
        self,
        request: aiccs_20230516_models.TaskRecoverCallRequest,
    ) -> aiccs_20230516_models.TaskRecoverCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.task_recover_call_with_options(request, runtime)

    async def task_recover_call_async(
        self,
        request: aiccs_20230516_models.TaskRecoverCallRequest,
    ) -> aiccs_20230516_models.TaskRecoverCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.task_recover_call_with_options_async(request, runtime)

    def template_list_with_options(
        self,
        request: aiccs_20230516_models.TemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TemplateList',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def template_list_with_options_async(
        self,
        request: aiccs_20230516_models.TemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.TemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TemplateList',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.TemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def template_list(
        self,
        request: aiccs_20230516_models.TemplateListRequest,
    ) -> aiccs_20230516_models.TemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.template_list_with_options(request, runtime)

    async def template_list_async(
        self,
        request: aiccs_20230516_models.TemplateListRequest,
    ) -> aiccs_20230516_models.TemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.template_list_with_options_async(request, runtime)

    def update_agent_status_with_options(
        self,
        request: aiccs_20230516_models.UpdateAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.UpdateAgentStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_status):
            query['AgentStatus'] = request.agent_status
        if not UtilClient.is_unset(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAgentStatus',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.UpdateAgentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_status_with_options_async(
        self,
        request: aiccs_20230516_models.UpdateAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.UpdateAgentStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_status):
            query['AgentStatus'] = request.agent_status
        if not UtilClient.is_unset(request.agent_tag):
            query['AgentTag'] = request.agent_tag
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAgentStatus',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.UpdateAgentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_status(
        self,
        request: aiccs_20230516_models.UpdateAgentStatusRequest,
    ) -> aiccs_20230516_models.UpdateAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_agent_status_with_options(request, runtime)

    async def update_agent_status_async(
        self,
        request: aiccs_20230516_models.UpdateAgentStatusRequest,
    ) -> aiccs_20230516_models.UpdateAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_agent_status_with_options_async(request, runtime)

    def update_task_customer_with_options(
        self,
        tmp_req: aiccs_20230516_models.UpdateTaskCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.UpdateTaskCustomerResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.UpdateTaskCustomerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.customers):
            request.customers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not UtilClient.is_unset(request.customers_shrink):
            query['Customers'] = request.customers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTaskCustomer',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.UpdateTaskCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_customer_with_options_async(
        self,
        tmp_req: aiccs_20230516_models.UpdateTaskCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20230516_models.UpdateTaskCustomerResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20230516_models.UpdateTaskCustomerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.customers):
            request.customers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.customers, 'Customers', 'json')
        query = {}
        if not UtilClient.is_unset(request.customers_shrink):
            query['Customers'] = request.customers_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTaskCustomer',
            version='2023-05-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20230516_models.UpdateTaskCustomerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_customer(
        self,
        request: aiccs_20230516_models.UpdateTaskCustomerRequest,
    ) -> aiccs_20230516_models.UpdateTaskCustomerResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_task_customer_with_options(request, runtime)

    async def update_task_customer_async(
        self,
        request: aiccs_20230516_models.UpdateTaskCustomerRequest,
    ) -> aiccs_20230516_models.UpdateTaskCustomerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_task_customer_with_options_async(request, runtime)
